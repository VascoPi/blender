/* SPDX-License-Identifier: Apache-2.0
 * Copyright 2011-2022 Blender Foundation */

#include "view_settings.h"

using namespace std;

namespace usdhydra {

ViewSettings::ViewSettings(BL::Context b_context)
{
  camera_data = CameraData::init_from_context(b_context);

  screen_width = b_context.region().width();
  screen_height = b_context.region().height();

  BL::Scene b_scene = b_context.scene();

  //getting render border
  int x1 = 0, y1 = 0;
  int x2 = screen_width, y2 = screen_height;

  if (b_context.region_data().view_perspective() == BL::RegionView3D::view_perspective_CAMERA) {
    if (b_scene.render().use_border()) {
      // TODO: add code
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
