/* SPDX-License-Identifier: Apache-2.0
 * Copyright 2011-2022 Blender Foundation */

#include <algorithm>

#include "view_settings.h"

#include "BLI_math_matrix.h"

using namespace std;

namespace usdhydra {

ViewSettings::ViewSettings(BL::Context b_context)
{
  camera_data = CameraData::init_from_context(b_context);

  screen_width = b_context.region().width();
  screen_height = b_context.region().height();

  float width_half = screen_width / 2.0f;
  float height_half = screen_height / 2.0f;

  BL::Scene b_scene = b_context.scene();

  //getting render border
  int x1 = 0, y1 = 0;
  int x2 = screen_width, y2 = screen_height;

  if (b_context.region_data().view_perspective() == BL::RegionView3D::view_perspective_CAMERA) {
    if (b_scene.render().use_border()) {
      BL::Object b_camera_obj = b_scene.camera();
      BL::Camera b_camera = (BL::Camera)b_camera_obj.data();

      float camera_points[4][3];

      b_camera.view_frame(b_scene, camera_points[0], camera_points[1], camera_points[2], camera_points[3]);

      BL::Array<float, 16> region_persp_matrix = b_context.region_data().perspective_matrix();
      BL::Array<float, 16> camera_world_matrix = b_camera_obj.matrix_world();

      float screen_points[4][2];

      for (int i = 0 ; i < 4; i++) {
        float world_location[] = {camera_points[i][0], camera_points[i][1], camera_points[i][2], 1.0f};
        mul_m4_v4((float(*)[4])camera_world_matrix.data, world_location);
        mul_m4_v4((float(*)[4])region_persp_matrix.data, world_location);

        if (world_location[3] > 0.0) {
          screen_points[i][0] = width_half + width_half * (world_location[0] / world_location[3]);
          screen_points[i][1] = height_half + height_half * (world_location[1] / world_location[3]);
        }
      }

      // getting camera view region
      float x1_f = min({screen_points[0][0], screen_points[1][0], screen_points[2][0], screen_points[3][0]});
      float x2_f = max({screen_points[0][0], screen_points[1][0], screen_points[2][0], screen_points[3][0]});
      float y1_f = min({screen_points[0][1], screen_points[1][1], screen_points[2][1], screen_points[3][1]});
      float y2_f = max({screen_points[0][1], screen_points[1][1], screen_points[2][1], screen_points[3][1]});

      // adjusting region to border
      float x = x1_f, y = y1_f;
      float dx = x2_f - x1_f, dy = y2_f - y1_f;

      x1 = x + b_scene.render().border_min_x() * dx;
      x2 = x + b_scene.render().border_max_x() * dx;
      y1 = y + b_scene.render().border_min_y() * dy;
      y2 = y + b_scene.render().border_max_y() * dy;

      // adjusting to region screen resolution
      x1 = max(min(x1, screen_width), 0);
      x2 = max(min(x2, screen_width), 0);
      y1 = max(min(y1, screen_height), 0);
      y2 = max(min(y2, screen_height), 0);
    }
  }
  else {
    if (((BL::SpaceView3D)b_context.space_data()).use_render_border()) {
      int x = x1, y = y1;
      int dx = x2 - x1, dy = y2 - y1;

      x1 = int(x + ((BL::SpaceView3D)b_context.space_data()).render_border_min_x() * dx);
      x2 = int(x + ((BL::SpaceView3D)b_context.space_data()).render_border_max_x() * dx);
      y1 = int(y + ((BL::SpaceView3D)b_context.space_data()).render_border_min_y() * dy);
      y2 = int(y + ((BL::SpaceView3D)b_context.space_data()).render_border_max_y() * dy);
    }
  }

  border[0][0] = x1;
  border[0][1] = y1;
  border[1][0] = x2 - x1;
  border[1][1] = y2 - y1;
}

ViewSettings::~ViewSettings()
{
}

int ViewSettings::get_width()
{
  return border[1][0];
}

int ViewSettings::get_height()
{
  return border[1][1];
}

pxr::GfCamera ViewSettings::export_camera()
{
  float tile[4] = {(float)border[0][0] / screen_width, (float)border[0][1] / screen_height,
                   (float)border[1][0] / screen_width, (float)border[1][1] / screen_height};
  return camera_data.export_gf(tile);
}

} // namespace usdhydra
