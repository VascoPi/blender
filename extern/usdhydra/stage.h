/* SPDX-License-Identifier: Apache-2.0
 * Copyright 2011-2022 Blender Foundation */

#pragma once

#include <memory>

#include <Python.h>

#include <pxr/pxr.h>
#include <pxr/usd/usd/stage.h>
#include <pxr/usd/usd/stageCache.h>

namespace usdhydra {

extern std::unique_ptr<pxr::UsdStageCache> stageCache;
void stage_init();

PyObject *addPythonSubmodule_stage(PyObject *mod);

} // namespace usdhydra
