/* SPDX-License-Identifier: Apache-2.0
 * Copyright 2011-2022 Blender Foundation */

#include "BLI_math_matrix.h"

#include "camera.h"
#include "utils.h"

namespace usdhydra {

CameraData CameraData::init_from_camera(BL::Camera b_camera, float transform[4][4], float ratio, float border[2][2])
{
  // TODO: add code
  return CameraData();
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
    // TODO: add code
    data = CameraData();
  }
  else if (b_context.region_data().view_perspective() == BL::RegionView3D::view_perspective_CAMERA) {
    BL::Object camera_obj = space_data.camera();

    float border[2][2] = {{0, 0}, {1, 1}};
    data = CameraData::init_from_camera((BL::Camera)camera_obj.data(), (float(*)[4])b_context.region_data().view_matrix().data, ratio, border);

    // This formula was taken from previous plugin with corresponded comment
    // See blender/intern/cycles/blender/blender_camera.cpp:blender_camera_from_view (look for 1.41421f)
    //float zoom = 4.0 / pow((pow(2.0, 0.5) + b_context.region_data().view_camera_zoom() / 50.0), 2);
    float zoom = 2.0 / pow((pow(2.0, 0.5) + b_context.region_data().view_camera_zoom() / 50.0), 2);

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
    // TODO: add code
  }
  else if (this->mode == BL::Camera::type_PANO) {
    // TODO: store panoramic camera settings
  }

  double transform_d[4][4];

  for (int i = 0 ; i < 4; i++)
  for (int j = 0 ; j < 4; j++){
    transform_d[i][j] = (double)transform[i][j];
  }

  gf_camera.SetTransform(pxr::GfMatrix4d(transform_d));
  
  return gf_camera;
}

} //namespace usdhydra
