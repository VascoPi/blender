# SPDX-License-Identifier: Apache-2.0
# Copyright 2011-2022 Blender Foundation

# <pep8 compliant>

import bpy

import _usdhydra

from ..utils import stages


class UsdStagePrim(bpy.types.PropertyGroup):
    path: bpy.props.StringProperty(name='Prim Path', default="")

    @property
    def indent(self):
        return self.path.count('/') - 1


class UsdStage(bpy.types.PropertyGroup):
    prims: bpy.props.CollectionProperty(type=UsdStagePrim)
    prim_index: bpy.props.IntProperty(default=-1)

    @property
    def stage(self):
        return stages.get_by_key(self.name)

    def get_prim_info(self, prim_prop):
        return _usdhydra.stage.prim_get_info(self.stage, prim_prop.path)

    def update_prims(self):
        self.prims.clear()
        self.prim_index = -1

        stage = self.stage
        if not stage:
            return

        prim_info = _usdhydra.stage.prim_get_info(stage, "/")
        for child_name in prim_info['children']:
            prim_prop = self.prims.add()
            prim_prop.path = f"/{child_name}"
            prim_prop.name = child_name


def get_stage_properties(bl_obj, do_create=True):
    key = str(bl_obj.as_pointer())
    stage_prop_list = bpy.context.window_manager.usdhydra.usd_stages
    stage_prop = stage_prop_list.get(key)

    if not stage_prop and do_create:
        stage_prop = stage_prop_list.add()
        stage_prop.name = key
        stage_prop.update_prims()

    return stage_prop


def remove_stage_properties(bl_obj):
    key = str(bl_obj.as_pointer())
    stage_prop_list = bpy.context.window_manager.usdhydra.usd_stages
    ind = next((i for i, stage_prop in enumerate(stage_prop_list) if stage_prop.name == key), -1)
    stage_prop_list.remove(ind)
