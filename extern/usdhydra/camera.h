/* SPDX-License-Identifier: Apache-2.0
 * Copyright 2011-2022 Blender Foundation */

#pragma once

#include <pxr/base/gf/camera.h>

#include "MEM_guardedalloc.h"
#include "RNA_blender_cpp.h"

using namespace std;

namespace usdhydra {

struct CameraData {
  static CameraData init_from_camera(BL::Camera b_camera, float transform[4][4], float ratio, float border[2][2]);
  static CameraData init_from_context(BL::Context b_context);

  pxr::GfCamera export_gf(float tile[4]);

  BL::Camera::type_enum mode;
  float clip_range[2];
  float focal_length = 0.0;
  float sensor_size[2];
  float transform[4][4];
  float lens_shift[2];
  float ortho_size[2];
  tuple<float, float, int> dof_data;
};

} // namespace usdhydra
