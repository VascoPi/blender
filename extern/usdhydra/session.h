/* SPDX-License-Identifier: Apache-2.0
 * Copyright 2011-2022 Blender Foundation */

#pragma once

#include <chrono>

#include <Python.h>

#include <pxr/usd/usd/stage.h>
#include <pxr/usdImaging/usdImagingGL/engine.h>
#include <pxr/usdImaging/usdAppUtils/camera.h>

#include "MEM_guardedalloc.h"
#include "RNA_blender_cpp.h"

#include "usd.h"
#include "intern/usd_exporter_context.h"
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

const vector<string> preview_allowed_prims = {"World", "Camera", "Floor", "_materials", "preview_", "CircularLight"};

class BlenderSession {
public:
  BlenderSession(BL::RenderEngine &b_engine);
  ~BlenderSession();

  void create();
  void reset(BL::Context b_context, Depsgraph *depsgraph, bool is_blender_scene, int stageId,
             blender::io::usd::materialx_data_type materialx_data, const char *render_delegate, int is_preview);
  void render(BL::Depsgraph &b_depsgraph, const char *render_delegate, HdRenderSettingsMap delegate_settings);
  void render_gl(BL::Depsgraph &b_depsgraph, const char *render_delegate, HdRenderSettingsMap delegate_settings);
  void view_draw(BL::Depsgraph &b_depsgraph, BL::Context &b_context);
  void view_update(BL::Depsgraph &b_depsgraph, BL::Context &b_context, const char *render_delegate, HdRenderSettingsMap delegate_settings);
  void sync(BL::Depsgraph &b_depsgraph, BL::Context &b_context);
  void sync_final_render(BL::Depsgraph &b_depsgraph);
  UsdStageRefPtr export_scene_to_usd(BL::Context b_context, Depsgraph *depsgraph, blender::io::usd::materialx_data_type materialx_data, const char *render_delegate);

  template <typename T>
  float get_renderer_percent_done(T *renderer)
  {
    float percent_done = 0.0;

    VtDictionary render_stats = renderer->get()->GetRenderStats();

    auto it = render_stats.find("percentDone");
    if (it != render_stats.end()) {
      percent_done = (float)it->second.UncheckedGet<double>();
    }

    return round(percent_done * 10.0f) / 10.0f;
  }

protected:
  void update_render_result(map<string, vector<float>> &render_images, string b_render_layer_name, int width, int height, int channels = 4);
  void notify_status(const char *info, const char *status, bool redraw = true);
  void notify_final_render_status(float progress, const char *title, const char *info);

public:
  BL::RenderEngine b_engine;
  //BL::BlendData b_data;

  std::unique_ptr<pxr::UsdImagingGLEngine> imagingGLEngine;
  pxr::UsdImagingGLRenderParams render_params;
  pxr::UsdStageRefPtr stage;

protected:
  chrono::time_point<chrono::steady_clock> time_begin;

  int width;
  int height;
  string b_render_layer_name;
};

PyObject *addPythonSubmodule_session(PyObject *mod);
}   // namespace usdhydra
