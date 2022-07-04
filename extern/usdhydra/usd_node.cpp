/* SPDX-License-Identifier: Apache-2.0
 * Copyright 2011-2022 Blender Foundation */

#include <Python.h>
#include <iostream>
#include <cstdio>
#include <regex>

#include <boost/algorithm/string/replace.hpp>

#include <pxr/pxr.h>
#include <pxr/usd/usd/stage.h>
#include <pxr/usd/usd/stageCache.h>
#include <pxr/usd/usd/prim.h>
#include <pxr/usd/usd/references.h>

#include <pxr/base/tf/stringUtils.h>

#include <pxr/usd/usdGeom/tokens.h>
#include <pxr/usd/usdGeom/xform.h>
#include <pxr/usd/usdGeom/scope.h>
#include <pxr/usd/usdSkel/root.h>

#include "MEM_guardedalloc.h"
#include "RNA_blender_cpp.h"

#include "glog/logging.h"

#include "usd_node.h"
#include "stage.h"
#include "session.h"
#include "utils.h"

using namespace pxr;

namespace usdhydra {

void getChildPrims(std::vector<UsdPrim> &prims, UsdPrim prim, std::regex &reg)
{
  if (!prim.IsPseudoRoot() && std::regex_match(prim.GetPath().GetAsString(), reg)) {
    prims.push_back(prim);
    return;
  }

  auto childPrims = prim.GetAllChildren();
  for (auto child = childPrims.begin(); child != childPrims.end(); ++child) {
    getChildPrims(prims, *child, reg);
  }
}

UsdStageRefPtr getFilteredStage(UsdStageRefPtr inputStage, const std::string filterPath)
{
  if (!inputStage) {
    return nullptr;
  }
  if (filterPath == "/*" || filterPath == "/**") {
    return inputStage;
  }

  std::string pattern = filterPath;
  boost::replace_all(pattern, "*", "#");          // temporary replacing '*' to '#'
  boost::replace_all(pattern, "/", "\\/");        // for correct regex pattern
  boost::replace_all(pattern, "##", "[\\w\\/]*"); // creation
  boost::replace_all(pattern, "#", "\\w*");

  std::regex reg(pattern);
  std::vector<UsdPrim> prims;
  getChildPrims(prims, inputStage->GetPseudoRoot(), reg);

  UsdStageRefPtr stage = UsdStage::CreateNew(usdhydra::get_temp_file(".usda", "usdnode", true));
  stage->SetMetadata(UsdGeomTokens->metersPerUnit, 1.0);
  stage->SetMetadata(UsdGeomTokens->upAxis, VtValue(UsdGeomTokens->z));

  UsdPrim rootPrim = stage->GetPseudoRoot();
  for (auto prim = prims.begin(); prim != prims.end(); ++prim) {
    UsdPrim overridePrim = stage->OverridePrim(rootPrim.GetPath().AppendChild(prim->GetName()));
    overridePrim.GetReferences().AddReference(inputStage->GetRootLayer()->GetRealPath(), prim->GetPath());
  }

  return stage;
}

static UsdStageRefPtr compute_BlenderDataNode(PyObject *nodeArgs)
{
  DLOG(INFO) << "compute_BlenderDataNode";
  return nullptr;
}

static UsdStageRefPtr compute_UsdFileNode(PyObject *nodeArgs)
{
  DLOG(INFO) << "compute_UsdFileNode";
  char *filePath, *filterPath;
  PyArg_ParseTuple(nodeArgs, "ss", &filePath, &filterPath);
  UsdStageRefPtr inputStage = UsdStage::Open(filePath);

  return getFilteredStage(inputStage, filterPath);
}

static UsdStageRefPtr compute_MergeNode(PyObject *nodeArgs)
{
  LOG(INFO) << "compute_MergeNode";
  UsdStageRefPtr stage = UsdStage::CreateNew(usdhydra::get_temp_file(".usda", "usdnode", true));
  stage->SetMetadata(UsdGeomTokens->metersPerUnit, 1.0);
  stage->SetMetadata(UsdGeomTokens->upAxis, VtValue(UsdGeomTokens->z));

  UsdPrim rootPrim = stage->GetPseudoRoot();

  for (int i = 0; i < Py_SIZE(nodeArgs); i++) {
    long stageId = PyLong_AsLong(PyTuple_GetItem(nodeArgs, i));
    UsdStageRefPtr refStage = stageCache->Find(UsdStageCache::Id::FromLongInt(stageId));
    auto childPrims = refStage->GetPseudoRoot().GetAllChildren();
    for (auto prim = childPrims.begin(); prim != childPrims.end(); ++prim) {
      UsdPrim overridePrim = stage->OverridePrim(rootPrim.GetPath().AppendChild(prim->GetName()));
      overridePrim.GetReferences().AddReference(refStage->GetRootLayer()->GetRealPath(), prim->GetPath());
    }
  }

  return stage;
}

static UsdStageRefPtr compute_FilterNode(PyObject *nodeArgs)
{
  LOG(INFO) << "compute_FilterNode";
  char *filterPath;
  long inputStageId;
  PyArg_ParseTuple(nodeArgs, "ls", &inputStageId, &filterPath);
  
  UsdStageRefPtr inputStage = stageCache->Find(UsdStageCache::Id::FromLongInt(inputStageId));

  return getFilteredStage(inputStage, filterPath);
}

static UsdStageRefPtr compute_RootNode(PyObject *nodeArgs)
{
  LOG(INFO) << "compute_RootNode";
  char *name, *type;
  long inputStageId;
  PyArg_ParseTuple(nodeArgs, "lss", &inputStageId, &name, &type);

  UsdStageRefPtr inputStage = stageCache->Find(UsdStageCache::Id::FromLongInt(inputStageId));

  UsdStageRefPtr stage = UsdStage::CreateNew(usdhydra::get_temp_file(".usda", "usdnode", true));
  stage->SetMetadata(UsdGeomTokens->metersPerUnit, 1.0);
  stage->SetMetadata(UsdGeomTokens->upAxis, VtValue(UsdGeomTokens->z));

  SdfPath path = SdfPath::AbsoluteRootPath().AppendChild(TfToken(name));
  UsdPrim rootPrim;
  if (strcmp(type, "Xform") == 0) {
    rootPrim = UsdGeomXform::Define(stage, path).GetPrim();
  }
  else if (strcmp(type, "Scope") == 0) {
    rootPrim = UsdGeomScope::Define(stage, path).GetPrim();
  }
  else if (strcmp(type, "SkelRoot") == 0) {
    rootPrim = UsdSkelRoot::Define(stage, path).GetPrim();
  }
  else {
    rootPrim = stage->DefinePrim(path);
  }

  auto childPrims = inputStage->GetPseudoRoot().GetAllChildren();
  for (auto prim = childPrims.begin(); prim != childPrims.end(); ++prim) {
    UsdPrim overridePrim = stage->OverridePrim(rootPrim.GetPath().AppendChild(prim->GetName()));
    overridePrim.GetReferences().AddReference(inputStage->GetRootLayer()->GetRealPath(), prim->GetPath());
  }

  return stage;
}

static UsdStageRefPtr compute_InstancingNode(PyObject *nodeArgs)
{
  LOG(INFO) << "compute_InstancingNode";
  return NULL;
}

static UsdStageRefPtr compute_TransformNode(PyObject *nodeArgs)
{
  LOG(INFO) << "compute_TransformNode";
  //std::string name = pxr::TfMakeValidIdentifier(node->name);

  //std::string path = usdhydra_utils::get_temp_dir().u8string();
  std::string path = usdhydra::get_temp_file(".usda");
  LOG(INFO) << path;
  //pxr::UsdStageRefPtr stage = pxr::UsdStage::CreateNew();
  return NULL;
}

static UsdStageRefPtr compute_TransformByEmptyNode(PyObject *nodeArgs)
{
  LOG(INFO) << "compute_TransformByEmptyNode";
  return NULL;
}

static PyObject *compute(PyObject *self, PyObject *args)
{
  char *nodeIdname;
  PyObject *nodeArgs;

  if (!PyArg_ParseTuple(args, "sO", &nodeIdname, &nodeArgs)) {
    Py_RETURN_NONE;
  }
  
  UsdStageRefPtr stage = nullptr;

  if (strcmp(nodeIdname, "usdhydra.UsdFileNode") == 0) {
    stage = compute_UsdFileNode(nodeArgs);
  }
  else if (strcmp(nodeIdname, "usdhydra.MergeNode") == 0) {
    stage = compute_MergeNode(nodeArgs);
  }
  else if (strcmp(nodeIdname, "usdhydra.FilterNode") == 0) {
    stage = compute_FilterNode(nodeArgs);
  }
  else if (strcmp(nodeIdname, "usdhydra.RootNode") == 0) {
    stage = compute_RootNode(nodeArgs);
  }

  if (!stage) {
    Py_RETURN_NONE;
  }

  UsdStageCache::Id id = stageCache->Insert(stage);
  return PyLong_FromLong(id.ToLongInt());
}

static PyMethodDef methods[] = {
  {"compute", compute, METH_VARARGS, ""},
  {NULL, NULL, 0, NULL},
};

static struct PyModuleDef module = {
  PyModuleDef_HEAD_INIT,
  "usd_node",
  "This module provides access to USD nodes evaluation functions.",
  -1,
  methods,
  NULL,
  NULL,
  NULL,
  NULL,
};

PyObject *addPythonSubmodule_usd_node(PyObject *mod)
{
  PyObject *submodule = PyModule_Create(&module);
  PyModule_AddObject(mod, "usd_node", submodule);
  return submodule;
}

}   // namespace usdhydra
