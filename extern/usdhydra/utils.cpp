/* SPDX-License-Identifier: Apache-2.0
 * Copyright 2011-2022 Blender Foundation */

#include "utils.h"

namespace usdhydra {

string get_random_string(const int len)
{
  static const char alphanum[] =
      "0123456789"
      "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
      "abcdefghijklmnopqrstuvwxyz";
  string tmp_s;
  tmp_s.reserve(len);

  for (int i = 0; i < len; ++i) {
      tmp_s += alphanum[rand() % (sizeof(alphanum) - 1)];
  }
    
  return tmp_s;
}

filesystem::path get_temp_dir(void)
{
  auto path = filesystem::temp_directory_path() / "usdhydra";

  if (!filesystem::exists(path)) {
    filesystem::create_directory(path);
  }

  return path;
}

filesystem::path get_temp_pid_dir(void)
{
  filesystem::path path = get_temp_dir() / to_string(getpid());

  if (!filesystem::exists(path)) {
    filesystem::create_directory(path);
  }

  return path;
}

filesystem::path get_temp_file(string suffix, string name, bool is_rand)
{
  auto filename = get_random_string(8);
  filesystem::path path;
  if (name.empty()) {
    path = get_temp_pid_dir() / ("tmp" +filename + suffix);
    ofstream(path.c_str());

    return path;
  }

  if (!suffix.empty()) {
    if (is_rand) {
      path = get_temp_pid_dir() / (name + "_" + filename + suffix);
      ofstream(path.c_str());

      return path;
    }

    name += suffix;
  }

  return get_temp_pid_dir() / name;
}

static PyObject *get_temp_file_func(PyObject * /*self*/, PyObject *args)
{
  const char *suffix = "", *name = "";
  bool is_rand = false;

  PyArg_ParseTuple(args, "ssp", &suffix, &name, &is_rand);

  auto path = usdhydra::get_temp_file(suffix, name, is_rand);
  return PyUnicode_FromString(path.u8string().c_str());
}

static PyObject *get_temp_dir_func(PyObject * /*self*/, PyObject * /*args*/)
{
  filesystem::path path = usdhydra::get_temp_dir();
  return PyUnicode_FromString(path.u8string().c_str());
}


static PyMethodDef methods[] = {
  {"get_temp_file", get_temp_file_func, METH_VARARGS, ""},
  {"get_temp_dir", get_temp_dir_func, METH_VARARGS, ""},
  {NULL, NULL, 0, NULL},
};

static struct PyModuleDef module = {
  PyModuleDef_HEAD_INIT,
  "utils",
  "This module provides access to utils functions.",
  -1,
  methods,
  NULL,
  NULL,
  NULL,
  NULL,
};

PyObject *addPythonSubmodule_utils(PyObject *mod)
{
  PyObject *submodule = PyModule_Create(&module);
  PyModule_AddObject(mod, "utils", submodule);
  return submodule;
}

} // namespace usdhydra
