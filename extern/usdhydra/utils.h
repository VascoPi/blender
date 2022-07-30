/* SPDX-License-Identifier: Apache-2.0
 * Copyright 2011-2022 Blender Foundation */

#pragma once

#include <filesystem>
#include <string>
#include <fstream>
#include <process.h>

#include <Python.h>

using namespace std;

namespace usdhydra {

string get_random_string(const int len);
filesystem::path get_temp_dir(void);
filesystem::path get_temp_pid_dir(void);
string get_temp_file(string suffix, string name = "", bool is_rand = false);

PyObject *addPythonSubmodule_utils(PyObject *mod);

} // namespace usdhydra
