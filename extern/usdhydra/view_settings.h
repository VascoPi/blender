/* SPDX-License-Identifier: Apache-2.0
 * Copyright 2011-2022 Blender Foundation */

#pragma once

#include "camera.h"

#include "MEM_guardedalloc.h"
#include "RNA_blender_cpp.h"

namespace usdhydra {

class ViewSettings {
  public:
    ViewSettings(BL::Context b_context);

    ~ViewSettings();

    int get_width();
    int get_height();

    pxr::GfCamera export_camera();

    CameraData camera_data;

    int screen_width;
    int screen_height;
    int border[2][2];
};

} // namespace usdhydra
