# SPDX-License-Identifier: Apache-2.0
# Copyright 2011-2022 Blender Foundation

# <pep8 compliant>

import _usdhydra




_stages = {}


def key(bl_obj):
    return str(bl_obj.as_pointer())


def get(bl_obj):
    return _stages.get(key(bl_obj), None)


def get_by_key(key_):
    return _stages.get(key_, None)


def set(bl_obj, stage):
    free(bl_obj)
    if stage:
        _stages[key(bl_obj)] = stage


def free(bl_obj):
    if key(bl_obj) not in _stages:
        return

    stage = _stages.pop(key(bl_obj))
    if stage not in _stages.values():
        _usdhydra.stage.free(stage)


def free_all():
    for stage in _stages.values():
        _usdhydra.stage.free(stage)

    _stages.clear()
