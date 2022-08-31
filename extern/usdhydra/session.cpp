/* SPDX-License-Identifier: Apache-2.0
 * Copyright 2011-2022 Blender Foundation */

#include <pxr/pxr.h>
#include <pxr/usd/usd/stage.h>
#include <pxr/base/gf/camera.h>
#include <pxr/imaging/glf/drawTarget.h>
#include <pxr/usd/usdGeom/camera.h>
#include <pxr/usdImaging/usdImagingGL/engine.h>
#include <pxr/usdImaging/usdImagingGL/renderParams.h>
#include <pxr/usdImaging/usdAppUtils/camera.h>
#include <pxr/base/plug/plugin.h>
#include <pxr/base/plug/registry.h>

#include "glog/logging.h"

#include "usdImagingLite/engine.h"
#include "usdImagingLite/renderParams.h"
#include "session.h"
#include <intern/usd_writer_world.h>

using namespace pxr;

namespace usdhydra {

BlenderSession::BlenderSession(BL::RenderEngine &b_engine)
    : b_engine(b_engine)
{
}

BlenderSession::~BlenderSession()
{
}

void BlenderSession::create()
{
  string filepath = usdhydra::get_temp_file(".usda");
  stage = UsdStage::CreateNew(filepath);
}

void BlenderSession::reset(BL::Context b_context, Depsgraph *depsgraph, bool is_blender_scene, int stageId, const char *render_delegate)
{
  UsdStageRefPtr new_stage;

  if (is_blender_scene) {
    new_stage = export_scene_to_usd(b_context, depsgraph, render_delegate);
  }
  else {
    new_stage = stageCache->Find(UsdStageCache::Id::FromLongInt(stageId));
  }

  set<SdfPath> existing_paths, new_paths, paths_to_remove;

  for (auto prim : stage->GetPseudoRoot().GetAllChildren()) {
    existing_paths.insert(prim.GetPath());
  }

  for (auto prim : new_stage->GetPseudoRoot().GetAllChildren()) {
    new_paths.insert(prim.GetPath());
  }

  set_difference(existing_paths.begin(), existing_paths.end(),
                 new_paths.begin(), new_paths.end(),
                 inserter(paths_to_remove, paths_to_remove.end()));

  for (auto obj : paths_to_remove) {
    stage->GetPrimAtPath(obj).SetActive(false);
  }

  for (auto prim : new_stage->GetPseudoRoot().GetAllChildren()) {
    UsdPrim override_prim = stage->OverridePrim(stage->GetPseudoRoot().GetPath().AppendChild(prim.GetName()));
    override_prim.SetActive(true);
    override_prim.GetReferences().ClearReferences();
    override_prim.GetReferences().AddReference(new_stage->GetRootLayer()->GetRealPath(), prim.GetPath());
  }
}

void BlenderSession::render_gl(BL::Depsgraph &b_depsgraph, const char *render_delegate)
{
  std::unique_ptr<UsdImagingGLEngine> imagingGLEngine = std::make_unique<UsdImagingGLEngine>();

  if (!imagingGLEngine->SetRendererPlugin(TfToken(render_delegate))) {
    return;
  }

  BL::Scene b_scene = b_depsgraph.scene_eval();

  GlfDrawTargetRefPtr draw_target_ptr = GlfDrawTarget::New(GfVec2i(width, height));

  draw_target_ptr->Bind();
  draw_target_ptr->AddAttachment("color", GL_RGBA, GL_FLOAT, GL_RGBA);

  UsdGeomCamera usd_camera = UsdAppUtilsGetCameraAtPath(stage, SdfPath(TfMakeValidIdentifier(b_scene.camera().data().name())));
  UsdTimeCode usd_timecode = UsdTimeCode(b_scene.frame_current());
  GfCamera gf_camera = usd_camera.GetCamera(usd_timecode);

  imagingGLEngine->SetCameraState(gf_camera.GetFrustum().ComputeViewMatrix(),
                                  gf_camera.GetFrustum().ComputeProjectionMatrix());

  imagingGLEngine->SetRenderViewport(GfVec4d(0, 0, width, height));
  imagingGLEngine->SetRendererAov(HdAovTokens->color);

  render_params.frame = UsdTimeCode(b_scene.frame_current());
  render_params.clearColor = GfVec4f(1.0, 1.0, 1.0, 0.0);

  imagingGLEngine->Render(stage->GetPseudoRoot(), render_params);

  BL::RenderResult b_result = b_engine.begin_result(0, 0, width, height, b_render_layer_name.c_str(), NULL);
  BL::CollectionRef b_render_passes = b_result.layers[0].passes;

  int channels = 4;
  vector<float> pixels(width * height * channels);

  glReadPixels(0, 0, width, height, GL_RGBA, GL_FLOAT, pixels.data());
  draw_target_ptr->Unbind();

  map<string, vector<float>> render_images{{"Combined", pixels}};
  vector<float> images;

  for (BL::RenderPass b_pass : b_render_passes) {
    map<string, vector<float>>::iterator it_image = render_images.find(b_pass.name());
    vector<float> image = it_image->second;

    if (it_image == render_images.end()) {
      image = vector<float>(width * height * channels);
    }

    if (b_pass.channels() != channels) {
      for (int i = image.size(); i >= b_pass.channels(); i -= b_pass.channels()) {
        image.erase(image.end() - i);
      }
    }

    images.insert(images.end(), image.begin(), image.end());
  }

  for (BL::RenderPass b_pass : b_render_passes) {
    b_pass.rect(images.data());
  }

  b_engine.end_result(b_result, false, false, false);
}

void BlenderSession::render(BL::Depsgraph& b_depsgraph, const char* render_delegate)
{
  std::unique_ptr<UsdImagingLiteEngine> imagingLiteEngine = std::make_unique<UsdImagingLiteEngine>();

  if (!imagingLiteEngine->SetRendererPlugin(TfToken(render_delegate))) {
    return;
  }

  BL::Scene b_scene = b_depsgraph.scene_eval();

  UsdGeomCamera usd_camera = UsdAppUtilsGetCameraAtPath(stage, SdfPath(TfMakeValidIdentifier(b_scene.camera().data().name())));
  UsdTimeCode usd_timecode = UsdTimeCode(b_scene.frame_current());
  GfCamera gf_camera = usd_camera.GetCamera(usd_timecode);

  imagingLiteEngine->SetCameraState(gf_camera);

  imagingLiteEngine->SetRenderViewport(GfVec4d(0, 0, width, height));
  imagingLiteEngine->SetRendererAov(HdAovTokens->color);

  UsdImagingLiteRenderParams render_params;

  render_params.frame = UsdTimeCode(b_scene.frame_current());
  render_params.clearColor = GfVec4f(1.0, 1.0, 1.0, 0.0);

  time_begin = chrono::steady_clock::now();

  chrono::time_point<chrono::steady_clock> time_current;
  chrono::milliseconds elapsed_time;

  string formatted_time;

  float percent_done = 0.0;

  int channels = 4;

  map<string, vector<float>> render_images{{"Combined", vector<float>(width * height * channels)}};
  vector<float> &pixels = render_images["Combined"];

  while (true) {
    if (b_engine.test_break()) {
      break;
    }

    imagingLiteEngine->Render(stage->GetPseudoRoot(), render_params);

    percent_done = get_renderer_percent_done(&imagingLiteEngine);
    time_current = chrono::steady_clock::now();
    elapsed_time = chrono::duration_cast<chrono::milliseconds>(time_current - time_begin);
    formatted_time = format_milliseconds(elapsed_time);

    notify_final_render_status(percent_done / 100.0,
      (b_scene.name() + ": " + b_render_layer_name).c_str(),
      ("Render Time: " + formatted_time + " | Done: " + to_string(int(percent_done)) + '%').c_str());

    if (imagingLiteEngine->IsConverged()) {
      break;
    }

    imagingLiteEngine->GetRendererAov(HdAovTokens->color, pixels.data());
    update_render_result(render_images, b_render_layer_name, width, height, channels);
  }

  imagingLiteEngine->GetRendererAov(HdAovTokens->color, pixels.data());
  update_render_result(render_images, b_render_layer_name, width, height, channels);
}

void BlenderSession::view_draw(BL::Depsgraph &b_depsgraph, BL::Context &b_context)
{
  BL::Scene b_scene = b_depsgraph.scene_eval();
  
  ViewSettings view_settings(b_context);

  if (view_settings.get_width() * view_settings.get_height() == 0) {
    return;
  };

  GfCamera gf_camera = view_settings.export_camera();

  vector<GfVec4f> clip_planes = gf_camera.GetClippingPlanes();

  for (int i = 0; i < clip_planes.size(); i++) {
    render_params.clipPlanes.push_back((GfVec4d)clip_planes[i]);
  }

  imagingGLEngine->SetCameraState(gf_camera.GetFrustum().ComputeViewMatrix(),
                                  gf_camera.GetFrustum().ComputeProjectionMatrix());
  imagingGLEngine->SetRenderViewport(GfVec4d((double)view_settings.border[0][0], (double)view_settings.border[0][1],
                                             (double)view_settings.border[1][0], (double)view_settings.border[1][1]));

  b_engine.bind_display_space_shader(b_scene);

  if (get_renderer_percent_done(&imagingGLEngine) == 0.0) {
    time_begin = chrono::steady_clock::now();
  }

  imagingGLEngine->Render(stage->GetPseudoRoot(), render_params);

  b_engine.unbind_display_space_shader();

  glClear(GL_DEPTH_BUFFER_BIT);

  chrono::time_point<chrono::steady_clock> time_current = chrono::steady_clock::now();
  chrono::milliseconds elapsed_time = chrono::duration_cast<chrono::milliseconds>(time_current - time_begin);

  string formatted_time = format_milliseconds(elapsed_time);

  if (!imagingGLEngine->IsConverged()) {
    notify_status(("Time: " + formatted_time + " | Done: " +
                   to_string(int(get_renderer_percent_done(&imagingGLEngine))) + '%').c_str(),
                   "Render");
  }
  else {
    notify_status(("Time: " + formatted_time).c_str(), "Rendering Done", false);
  }
}

void BlenderSession::view_update(BL::Depsgraph &b_depsgraph, BL::Context &b_context, const char *render_delegate)
{
  if (!imagingGLEngine) {
    imagingGLEngine = std::make_unique<UsdImagingGLEngine>();
  }
  
  imagingGLEngine->SetRendererPlugin(TfToken(render_delegate));

  if (imagingGLEngine->IsPauseRendererSupported()) {
    imagingGLEngine->PauseRenderer();
  }

  sync(b_depsgraph, b_context);

  if (imagingGLEngine->IsPauseRendererSupported()) {
    imagingGLEngine->ResumeRenderer();
  }
}

void BlenderSession::sync(BL::Depsgraph &b_depsgraph, BL::Context &b_context)
{
  BL::Scene b_scene = b_depsgraph.scene_eval();
  ViewSettings view_settings(b_context);

  render_params.frame = UsdTimeCode(b_scene.frame_current());
}

void BlenderSession::sync_final_render(BL::Depsgraph& b_depsgraph) {
  BL::Scene b_scene = b_depsgraph.scene_eval();
  b_render_layer_name = b_depsgraph.view_layer().name();

  vector<vector<float>> border ={{0.0, 0.0}, {1.0, 1.0}};

  if (b_scene.render().use_border()) {
    border = {
      {b_scene.render().border_min_x(),
       b_scene.render().border_min_y()},
      {b_scene.render().border_max_x() - b_scene.render().border_min_x(),
       b_scene.render().border_max_y() - b_scene.render().border_min_y()}
    };
  }

  int screen_width = int(b_scene.render().resolution_x() * b_scene.render().resolution_percentage() / 100);
  int screen_height = int(b_scene.render().resolution_y() * b_scene.render().resolution_percentage() / 100);

  width = int(screen_width * border[1][0]);
  height = int(screen_height * border[1][1]);
}

UsdStageRefPtr BlenderSession::export_scene_to_usd(BL::Context b_context, Depsgraph *depsgraph, const char *render_delegate)
{
  LOG(INFO) << "export_scene_to_usd";

  Scene *scene = DEG_get_input_scene(depsgraph);
  World *world = scene->world;

  DEG_graph_build_for_all_objects(depsgraph);

  bContext *C = (bContext *)b_context.ptr.data;
  Main *bmain = CTX_data_main(C);
  USDExportParams usd_export_params;

  usd_export_params.selected_objects_only = false;
  usd_export_params.visible_objects_only = false;

  string filepath = usdhydra::get_temp_file(".usda");
  UsdStageRefPtr usd_stage = UsdStage::CreateNew(filepath);

  usd_stage->SetMetadata(UsdGeomTokens->upAxis, VtValue(UsdGeomTokens->z));
  usd_stage->SetMetadata(UsdGeomTokens->metersPerUnit, static_cast<double>(scene->unit.scale_length));
  usd_stage->GetRootLayer()->SetDocumentation(std::string("Blender v") + BKE_blender_version_string());

  blender::io::usd::create_world(usd_stage, world, render_delegate);
  /* Set up the stage for animated data. */
  /*if (data->params.export_animation) {
    usd_stage->SetTimeCodesPerSecond(FPS);
    usd_stage->SetStartTimeCode(scene->r.sfra);
    usd_stage->SetEndTimeCode(scene->r.efra);
  }*/



  blender::io::usd::USDHierarchyIterator iter(bmain, depsgraph, usd_stage, usd_export_params);

  //if (data->params.export_animation) {
  //  /* Writing the animated frames is not 100% of the work, but it's our best guess. */
  //  float progress_per_frame = 1.0f / std::max(1, (scene->r.efra - scene->r.sfra + 1));

  //  for (float frame = scene->r.sfra; frame <= scene->r.efra; frame++) {
  //    if (G.is_break || (stop != nullptr && *stop)) {
  //      break;
  //    }

  //    /* Update the scene for the next frame to render. */
  //    scene->r.cfra = static_cast<int>(frame);
  //    scene->r.subframe = frame - scene->r.cfra;
  //    BKE_scene_graph_update_for_newframe(data->depsgraph);

  //    iter.set_export_frame(frame);
  //    iter.iterate_and_write();

  //    *progress += progress_per_frame;
  //    *do_update = true;
  //  }
  //}
  //else {
  //  /* If we're not animating, a single iteration over all objects is enough. */
  //  iter.iterate_and_write();
  //}

  iter.iterate_and_write();
  iter.release_writers();

  string s;
  usd_stage->ExportToString(&s);
  usd_stage->Export("d:\\test.usda");
  printf("%s\n", s.c_str());

  return usd_stage;
}

void BlenderSession::update_render_result(map<string, vector<float>> &render_images, string b_render_layer_name, int width, int height, int channels)
{
  BL::RenderResult b_result = b_engine.begin_result(0, 0, width, height, b_render_layer_name.c_str(), NULL);
  BL::CollectionRef b_render_passes = b_result.layers[0].passes;

  vector<float> images;

  for (BL::RenderPass b_pass : b_render_passes) {
    map<string, vector<float>>::iterator it_image = render_images.find(b_pass.name());
    vector<float> image = it_image->second;

    if (it_image == render_images.end()) {
      image = vector<float>(width * height * channels);
    }

    if (b_pass.channels() != channels) {
      for (int i = image.size(); i >= b_pass.channels(); i -= b_pass.channels()) {
        image.erase(image.end() - i);
      }
    }

    images.insert(images.end(), image.begin(), image.end());
  }

  for (BL::RenderPass b_pass : b_render_passes) {
    b_pass.rect(images.data());
  }

  b_engine.end_result(b_result, false, false, false);
}

void BlenderSession::notify_status(const char *info, const char *status, bool redraw)
{
  b_engine.update_stats(status, info);

  if (redraw) {
    b_engine.tag_redraw();
  }
};

void BlenderSession::notify_final_render_status(float progress, const char *title, const char* info)
{
  b_engine.update_progress(progress);
  b_engine.update_stats(title, info);
}

/* ------------------------------------------------------------------------- */
/* Python API for BlenderSession
 */

static PyObject *create_func(PyObject * /*self*/, PyObject *args)
{
  DLOG(INFO) << "create_func";
  PyObject *pyengine;
  if (!PyArg_ParseTuple(args, "O", &pyengine)) {
    Py_RETURN_NONE;
  }

  PointerRNA engineptr;
  RNA_pointer_create(NULL, &RNA_RenderEngine, (void *)PyLong_AsVoidPtr(pyengine), &engineptr);
  BL::RenderEngine engine(engineptr);

  /* create session */
  BlenderSession *session = new BlenderSession(engine);

  session->create();

  return PyLong_FromVoidPtr(session);
}

static PyObject *free_func(PyObject * /*self*/, PyObject *args)
{
  LOG(INFO) << "free_func";
  PyObject *pysession;
  if (!PyArg_ParseTuple(args, "O", &pysession)) {
    Py_RETURN_NONE;
  }

  delete (BlenderSession *)PyLong_AsVoidPtr(pysession);
  Py_RETURN_NONE;
}

static PyObject *reset_func(PyObject * /*self*/, PyObject *args)
{
  LOG(INFO) << "reset_func";
  PyObject *pysession, *pydata, *pycontext, *pydepsgraph;

  int stageId = 0;
  int is_blender_scene = 1;
  const char *render_delegate;

  if (!PyArg_ParseTuple(args, "OOOOiis", &pysession, &pydata, &pycontext, &pydepsgraph, &is_blender_scene, &stageId, &render_delegate)) {
    Py_RETURN_NONE;
  }

  PointerRNA depsgraphptr;
  RNA_pointer_create(NULL, &RNA_Context, (ID *)PyLong_AsVoidPtr(pydepsgraph), &depsgraphptr);
  Depsgraph *depsgraph = (::Depsgraph *)depsgraphptr.data;

  PointerRNA contextptr;
  RNA_pointer_create(NULL, &RNA_Context, (ID *)PyLong_AsVoidPtr(pycontext), &contextptr);
  BL::Context b_context(contextptr);

  BlenderSession *session = (BlenderSession *)PyLong_AsVoidPtr(pysession);

  //PointerRNA dataptr;
  //RNA_main_pointer_create((Main *)PyLong_AsVoidPtr(pydata), &dataptr);
  //BL::BlendData data(dataptr);

  //PointerRNA depsgraphptr;
  //RNA_pointer_create(NULL, &RNA_Depsgraph, (ID *)PyLong_AsVoidPtr(pydepsgraph), &depsgraphptr);
  //BL::Depsgraph depsgraph(depsgraphptr);

  session->reset(b_context, depsgraph, is_blender_scene, stageId, render_delegate);

  Py_RETURN_NONE;
}

static PyObject* final_update_func(PyObject* /*self*/, PyObject* args)
{
  LOG(INFO) << "final_update_func";
  PyObject *pysession, *pydepsgraph;

  if (!PyArg_ParseTuple(args, "OO", &pysession, &pydepsgraph)) {
    Py_RETURN_NONE;
  }

  PointerRNA depsgraphptr;
  RNA_pointer_create(NULL, &RNA_Depsgraph, (ID *)PyLong_AsVoidPtr(pydepsgraph), &depsgraphptr);
  BL::Depsgraph depsgraph(depsgraphptr);

  BlenderSession *session = (BlenderSession *)PyLong_AsVoidPtr(pysession);

  session->sync_final_render(depsgraph);

  Py_RETURN_NONE;
}

static PyObject *render_func(PyObject * /*self*/, PyObject *args)
{
  LOG(INFO) << "render_func";
  PyObject *pysession, *pydepsgraph;
  const char *render_delegate;

  if (!PyArg_ParseTuple(args, "OOs", &pysession, &pydepsgraph, &render_delegate)) {
    Py_RETURN_NONE;
  }

  PointerRNA depsgraphptr;
  RNA_pointer_create(NULL, &RNA_Depsgraph, (ID *)PyLong_AsVoidPtr(pydepsgraph), &depsgraphptr);
  BL::Depsgraph depsgraph(depsgraphptr);

  BlenderSession *session = (BlenderSession *)PyLong_AsVoidPtr(pysession);

  if (strcmp(render_delegate, "HdStormRendererPlugin") == 0) {
    session->render_gl(depsgraph, render_delegate);
  }
  else {
    session->render(depsgraph, render_delegate);
  }

  Py_RETURN_NONE;
}

static PyObject *render_frame_finish_func(PyObject * /*self*/, PyObject *args)
{
  Py_RETURN_NONE;
}

static PyObject *view_update_func(PyObject * /*self*/, PyObject *args)
{
  LOG(INFO) << "view_update_func";
  PyObject *pysession, *pydepsgraph, *pycontext, *pyspaceData, *pyregionData;
  const char *render_delegate;

  if (!PyArg_ParseTuple(args, "OOOOOs", &pysession, &pydepsgraph, &pycontext, &pyspaceData, &pyregionData, &render_delegate)) {
    Py_RETURN_NONE;
  }

  PointerRNA depsgraphptr;
  RNA_pointer_create(NULL, &RNA_Depsgraph, (ID *)PyLong_AsVoidPtr(pydepsgraph), &depsgraphptr);
  BL::Depsgraph b_depsgraph(depsgraphptr);

  PointerRNA contextptr;
  RNA_pointer_create(NULL, &RNA_Context, (ID *)PyLong_AsVoidPtr(pycontext), &contextptr);
  BL::Context b_context(contextptr);

  BlenderSession *session = (BlenderSession *)PyLong_AsVoidPtr(pysession);

  session->view_update(b_depsgraph, b_context, render_delegate);

  Py_RETURN_NONE;
}

static PyObject *view_draw_func(PyObject * /*self*/, PyObject *args)
{
  LOG(INFO) << "view_draw_func";

  PyObject *pysession, *pydepsgraph, *pycontext, *pyspaceData, *pyregionData;

  if (!PyArg_ParseTuple(args, "OOOOO", &pysession, &pydepsgraph, &pycontext, &pyspaceData, &pyregionData)) {
    Py_RETURN_NONE;
  }


  PointerRNA depsgraphptr;
  RNA_pointer_create(NULL, &RNA_Depsgraph, (ID *)PyLong_AsVoidPtr(pydepsgraph), &depsgraphptr);
  BL::Depsgraph b_depsgraph(depsgraphptr);

  PointerRNA contextptr;
  RNA_pointer_create(NULL, &RNA_Context, (ID *)PyLong_AsVoidPtr(pycontext), &contextptr);
  BL::Context b_context(contextptr);

  BlenderSession *session = (BlenderSession *)PyLong_AsVoidPtr(pysession);
  session->view_draw(b_depsgraph, b_context);
  
  ///* Allow Blender to execute other Python scripts. */
  //python_thread_state_save(&session->python_thread_state);

  //session->render(b_depsgraph);

  //python_thread_state_restore(&session->python_thread_state);

  Py_RETURN_NONE;
}

static PyObject* get_render_plugins_func(PyObject* /*self*/, PyObject* args)
{
  PlugRegistry &registry = PlugRegistry::GetInstance();
  TfTokenVector pluginsIds = UsdImagingGLEngine::GetRendererPlugins();
  PyObject *ret = PyTuple_New(pluginsIds.size());
  for (int i = 0; i < pluginsIds.size(); ++i) {
    PyObject *descr = PyDict_New();
    PyDict_SetItemString(descr, "id", PyUnicode_FromString(pluginsIds[i].GetText()));
    PyDict_SetItemString(descr, "name", PyUnicode_FromString(UsdImagingGLEngine::GetRendererDisplayName(pluginsIds[i]).c_str()));

    std::string plugin_name = pluginsIds[i];
    plugin_name = plugin_name.substr(0, plugin_name.size()-6);
    plugin_name[0] = tolower(plugin_name[0]);
    std::string path = "";
    PlugPluginPtr plugin = registry.GetPluginWithName(plugin_name);
    if (plugin) {
        path = plugin->GetPath();
    }
    PyDict_SetItemString(descr, "path", PyUnicode_FromString(path.c_str()));

    PyTuple_SetItem(ret, i, descr);
  }
  return ret;
}

static PyMethodDef methods[] = {
  {"create", create_func, METH_VARARGS, ""},
  {"free", free_func, METH_VARARGS, ""},
  {"render", render_func, METH_VARARGS, ""},
  {"reset", reset_func, METH_VARARGS, ""},
  {"final_update", final_update_func, METH_VARARGS, ""},
  {"render_frame_finish", render_frame_finish_func, METH_VARARGS, ""},
  {"view_update", view_update_func, METH_VARARGS, ""},
  {"view_draw", view_draw_func, METH_VARARGS, ""},
  {"get_render_plugins", get_render_plugins_func, METH_VARARGS, ""},
  {NULL, NULL, 0, NULL},
};

static struct PyModuleDef module = {
  PyModuleDef_HEAD_INIT,
  "session",
  "",
  -1,
  methods,
  NULL,
  NULL,
  NULL,
  NULL,
};

PyObject *addPythonSubmodule_session(PyObject *mod)
{
  PyObject *submodule = PyModule_Create(&module);
  PyModule_AddObject(mod, "session", submodule);
  return submodule;
}

}   // namespace usdhydra
