/* SPDX-License-Identifier: Apache-2.0
 * Copyright 2011-2022 Blender Foundation */

#include <math.h>
#include <algorithm>

#include "BLI_math_matrix.h"

#include "camera.h"
#include "utils.h"

namespace usdhydra {

// Core has issues with drawing faces in orthographic camera view with big
// ortho depth (far_clip_plane - near_clip_plane).
// Experimentally found quite suited value = 200
float MAX_ORTHO_DEPTH = 200.0f;

CameraData CameraData::init_from_camera(BL::Camera b_camera, float transform[4][4], float ratio, float border[2][2])
{
  float pos[2] = {border[0][0], border[0][1]};
  float size[2] = {border[1][0], border[1][1]};

  CameraData data = CameraData();

  copy_m4_m4(data.transform, transform);

  data.clip_range[0] = b_camera.clip_start();
  data.clip_range[1] = b_camera.clip_end();
  data.mode = b_camera.type();

  if (b_camera.dof().use_dof()) {

    float focus_distance;

    if (!b_camera.dof().focus_object()) {
      float focus_distance = b_camera.dof().focus_distance();
    } 
    else {
      float obj_pos[] = {b_camera.dof().focus_object().matrix_world()[3],
                         b_camera.dof().focus_object().matrix_world()[7],
                         b_camera.dof().focus_object().matrix_world()[11]};

      float camera_pos[] = {transform[0][3],
                            transform[1][3],
                            transform[2][3]};

      float focus_distance = sqrt(pow((obj_pos[0] - camera_pos[0]), 2) + 
                                  pow((obj_pos[1] - camera_pos[1]), 2) + 
                                  pow((obj_pos[2] - camera_pos[2]), 2));
    }

    data.dof_data = tuple(max(focus_distance, 0.001f),
                          b_camera.dof().aperture_fstop(),
                          b_camera.dof().aperture_blades());
  }

  if (b_camera.sensor_fit() ==BL::Camera::sensor_fit_VERTICAL) {
    data.lens_shift[0] = b_camera.shift_x() / ratio;
    data.lens_shift[1] = b_camera.shift_y();
  } 
  else if ((b_camera.sensor_fit() == BL::Camera::sensor_fit_HORIZONTAL)) {
    data.lens_shift[0] = b_camera.shift_x();
    data.lens_shift[1] = b_camera.shift_y() * ratio;
  } 
  else if ((b_camera.sensor_fit() == BL::Camera::sensor_fit_AUTO)) {

    if (ratio > 1.0f) {
      data.lens_shift[0] = b_camera.shift_x();
      data.lens_shift[1] = b_camera.shift_y() * ratio;
    } 
    else {
      data.lens_shift[0] = b_camera.shift_x() / ratio;
      data.lens_shift[1] = b_camera.shift_y();
    }

  } 
  else {

  }

  data.lens_shift[0] = data.lens_shift[0] / size[0] + (pos[0] + size[0] * 0.5 - 0.5) / size[0];
  data.lens_shift[1] = data.lens_shift[1] / size[1] + (pos[1] + size[1] * 0.5 - 0.5) / size[1];

  if (b_camera.type() == BL::Camera::type_PERSP) {
    data.focal_length = b_camera.lens();

    if (b_camera.sensor_fit() == BL::Camera::sensor_fit_VERTICAL) {
      data.sensor_size[0] = b_camera.sensor_height() * ratio;
      data.sensor_size[1] = b_camera.sensor_height();

    } 
    else if (b_camera.sensor_fit() == BL::Camera::sensor_fit_HORIZONTAL) {
      data.sensor_size[0] = b_camera.sensor_width();
      data.sensor_size[1] = b_camera.sensor_width() / ratio;
    } 
    else {

      if (ratio > 1.0f) {
        data.sensor_size[0] = b_camera.sensor_width();
        data.sensor_size[1] = b_camera.sensor_width() / ratio;
      } 
      else {
        data.sensor_size[0] = b_camera.sensor_width() * ratio;
        data.sensor_size[1] = b_camera.sensor_width();
      }

    }

    data.sensor_size[0] = data.sensor_size[0] * size[0];
    data.sensor_size[1] = data.sensor_size[1] * size[1];

  } 
  else if (b_camera.type() == BL::Camera::type_ORTHO) {
    if (b_camera.sensor_fit() == BL::Camera::sensor_fit_VERTICAL) {
      data.ortho_size[0] = b_camera.ortho_scale() * ratio;
      data.ortho_size[1] = b_camera.ortho_scale();
    } 
    else if (b_camera.sensor_fit() == BL::Camera::sensor_fit_HORIZONTAL) {
      data.ortho_size[0] = b_camera.ortho_scale();
      data.ortho_size[1] = b_camera.ortho_scale() / ratio;
    } 
    else {

      if (ratio > 1.0f) {
        data.ortho_size[0] = b_camera.ortho_scale();
        data.ortho_size[1] = b_camera.ortho_scale() / ratio;
      } 
      else {
        data.ortho_size[0] = b_camera.ortho_scale() * ratio;
        data.ortho_size[1] = b_camera.ortho_scale();
      }

    }

    data.ortho_size[0] = data.ortho_size[0] * size[0];
    data.ortho_size[1] = data.ortho_size[1] * size[1];

    data.clip_range[0] = b_camera.clip_start();
    data.clip_range[1] = min(b_camera.clip_end(), MAX_ORTHO_DEPTH + b_camera.clip_start());

  } 
  else if (b_camera.type() == BL::Camera::type_PANO) {
    // TODO: Recheck parameters for PANO camera
    data.focal_length = b_camera.lens();
    if (b_camera.sensor_fit() == BL::Camera::sensor_fit_VERTICAL) {
      data.sensor_size[0] = b_camera.sensor_height() * ratio;
      data.sensor_size[1] = b_camera.sensor_height();
    } 
    else if (b_camera.sensor_fit() == BL::Camera::sensor_fit_HORIZONTAL) {
      data.sensor_size[0] = b_camera.sensor_height();
      data.sensor_size[1] = b_camera.sensor_height() / ratio;
    } 
    else {

      if (ratio > 1.0f) {
        data.sensor_size[0] = b_camera.sensor_width();
        data.sensor_size[1] = b_camera.sensor_width() / ratio;
      } 
      else {
        data.sensor_size[0] = b_camera.sensor_width() * ratio;
        data.sensor_size[1] = b_camera.sensor_width();
      }

    }

    data.sensor_size[0] = data.sensor_size[0] * size[0];
    data.sensor_size[1] = data.sensor_size[1] * size[1];

  } 
  else {

  }

  return data;
}

CameraData CameraData::init_from_context(BL::Context b_context)
{
  // this constant was found experimentally, didn't find such option in
  // context.space_data or context.region_data
  float VIEWPORT_SENSOR_SIZE = 72.0;

  BL::SpaceView3D space_data = (BL::SpaceView3D)b_context.space_data();

  CameraData data;
  float ratio = (float)b_context.region().width() / (float)b_context.region().height();
  if (b_context.region_data().view_perspective() == BL::RegionView3D::view_perspective_PERSP) {
    data = CameraData();
    data.mode = BL::Camera::type_PERSP;
    data.clip_range[0] = space_data.clip_start();
    data.clip_range[1] = space_data.clip_end();
    data.lens_shift[0] = 0.0;
    data.lens_shift[1] = 0.0;
    data.focal_length = space_data.lens();

    if (ratio > 1.0) {
      data.sensor_size[0] = VIEWPORT_SENSOR_SIZE;
      data.sensor_size[1] = VIEWPORT_SENSOR_SIZE / ratio;
    }
    else {
      data.sensor_size[0] = VIEWPORT_SENSOR_SIZE * ratio;
      data.sensor_size[1] = VIEWPORT_SENSOR_SIZE;
    }

    invert_m4_m4(data.transform, (float(*)[4])b_context.region_data().view_matrix().data);
  }
  else if (b_context.region_data().view_perspective() == BL::RegionView3D::view_perspective_ORTHO) {
    data = CameraData();
    data.mode = BL::Camera::type_ORTHO;
    data.lens_shift[0] = 0.0f;
    data.lens_shift[1] = 0.0f;

    float ortho_size = b_context.region_data().view_distance() * VIEWPORT_SENSOR_SIZE / space_data.lens();
    float ortho_depth = min(space_data.clip_end(), MAX_ORTHO_DEPTH);

    data.clip_range[0] = -ortho_depth * 0.5;
    data.clip_range[1] = ortho_depth * 0.5;

    if (ratio > 1.0f) {
      data.ortho_size[0] = ortho_size;
      data.ortho_size[1] = ortho_size / ratio;
    } else {
      data.ortho_size[0] = ortho_size * ratio;
      data.ortho_size[1] = ortho_size;
    }
    
    invert_m4_m4(data.transform, (float(*)[4])b_context.region_data().view_matrix().data);
  }
  else if (b_context.region_data().view_perspective() == BL::RegionView3D::view_perspective_CAMERA) {
    BL::Object camera_obj = space_data.camera();

    float border[2][2] = {{0, 0}, {1, 1}};

    float inverted_transform[4][4];

    invert_m4_m4(inverted_transform, (float(*)[4])b_context.region_data().view_matrix().data);    

    data = CameraData::init_from_camera((BL::Camera)camera_obj.data(), inverted_transform, ratio, border);

    // This formula was taken from previous plugin with corresponded comment
    // See blender/intern/cycles/blender/blender_camera.cpp:blender_camera_from_view (look for 1.41421f)
    float zoom = 4.0 / pow((pow(2.0, 0.5) + b_context.region_data().view_camera_zoom() / 50.0), 2);

    // Updating lens_shift due to viewport zoom and view_camera_offset
    // view_camera_offset should be multiplied by 2
    data.lens_shift[0] = (data.lens_shift[0] + b_context.region_data().view_camera_offset()[0] * 2) / zoom;
    data.lens_shift[1] = (data.lens_shift[1] + b_context.region_data().view_camera_offset()[1] * 2) / zoom;

    if (data.mode == BL::Camera::type_ORTHO) {
      data.ortho_size[0] *= zoom;
      data.ortho_size[1] *= zoom;
    }
    else {
      data.sensor_size[0] *= zoom;
      data.sensor_size[1] *= zoom;
    }
  }

  return data;
}

pxr::GfCamera CameraData::export_gf(float tile[4])
{
  float tile_pos[2] = {tile[0], tile[1]}, tile_size[2] = {tile[2], tile[3]};

  pxr::GfCamera gf_camera = pxr::GfCamera();

  gf_camera.SetClippingRange(pxr::GfRange1f(this->clip_range[0], this->clip_range[1]));

  vector<float> lens_shift = {(float)(this->lens_shift[0] + tile_pos[0] + tile_size[0] * 0.5 - 0.5) / tile_size[0],
                              (float)(this->lens_shift[1] + tile_pos[1] + tile_size[1] * 0.5 - 0.5) / tile_size[1]};

  if (this->mode == BL::Camera::type_PERSP) {
    gf_camera.SetProjection(pxr::GfCamera::Projection::Perspective);
    gf_camera.SetFocalLength(this->focal_length);

    vector<float> sensor_size = {this->sensor_size[0] * tile_size[0], this->sensor_size[1] * tile_size[1]};

    gf_camera.SetHorizontalAperture(sensor_size[0]);
    gf_camera.SetVerticalAperture(sensor_size[1]);

    gf_camera.SetHorizontalApertureOffset(lens_shift[0] * sensor_size[0]);
    gf_camera.SetVerticalApertureOffset(lens_shift[1] * sensor_size[1]);
  }
  else if (this->mode == BL::Camera::type_ORTHO) {
    gf_camera.SetProjection(pxr::GfCamera::Projection::Orthographic);

    // Use tenths of a world unit accorging to USD docs https://graphics.pixar.com/usd/docs/api/class_gf_camera.html
    float ortho_size[2] = {this->ortho_size[0] * tile_size[0] * 10, 
                           this->ortho_size[1] * tile_size[1] * 10};

    gf_camera.SetHorizontalAperture(ortho_size[0]);
    gf_camera.SetVerticalAperture(ortho_size[1]);

    gf_camera.SetHorizontalApertureOffset(lens_shift[0] * this->ortho_size[0] * tile_size[0] * 10);
    gf_camera.SetVerticalApertureOffset(lens_shift[1] * this->ortho_size[1] * tile_size[1] * 10);
  }
  else if (this->mode == BL::Camera::type_PANO) {
    // TODO: store panoramic camera settings
  }

  double transform_d[4][4];

  for (int i = 0 ; i < 4; i++) {
    for (int j = 0 ; j < 4; j++) {
      transform_d[i][j] = (double)transform[i][j];
    }
  }

  gf_camera.SetTransform(pxr::GfMatrix4d(transform_d));
  
  return gf_camera;
}

} //namespace usdhydra
