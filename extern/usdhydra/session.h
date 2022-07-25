/* SPDX-License-Identifier: Apache-2.0
 * Copyright 2011-2022 Blender Foundation */

#pragma once

#include <Python.h>

#include <pxr/usd/usd/stage.h>
#include <pxr/usdImaging/usdImagingGL/engine.h>

#include "MEM_guardedalloc.h"
#include "RNA_blender_cpp.h"

#include "usd.h"
#include "intern/usd_hierarchy_iterator.h"
#include "BKE_main.h"
#include "BKE_scene.h"
#include "BKE_context.h"
#include "BKE_blender_version.h"

#include "DEG_depsgraph.h"
#include "DEG_depsgraph_query.h"
#include "utils.h"

#include "session.h"
#include "stage.h"
#include "view_settings.h"

namespace usdhydra {

class BlenderSession {
public:
  BlenderSession(BL::RenderEngine &b_engine);
  ~BlenderSession();

  void reset(BL::Context b_context, Depsgraph *depsgraph, bool is_blender_scene, int stageId, std::vector<std::vector<std::string>> materialx_data);
  void render(BL::Depsgraph &b_depsgraph);
  void view_draw(BL::Depsgraph &b_depsgraph, BL::Context &b_context);
  void view_update(BL::Depsgraph &b_depsgraph, BL::Context &b_context);
  void sync(BL::Depsgraph &b_depsgraph, BL::Context &b_context);
  pxr::UsdStageRefPtr export_scene_to_usd(BL::Context b_context, Depsgraph *depsgraph, std::vector<std::vector<std::string>> materialx_data);

public:
  BL::RenderEngine b_engine;
  //BL::BlendData b_data;

  std::unique_ptr<pxr::UsdImagingGLEngine> imagingGLEngine;
  pxr::UsdImagingGLRenderParams render_params;
  pxr::UsdStageRefPtr stage;
};

PyObject *addPythonSubmodule_session(PyObject *mod);

}   // namespace usdhydra
