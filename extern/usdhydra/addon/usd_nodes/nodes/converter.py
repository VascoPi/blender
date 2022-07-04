# SPDX-License-Identifier: Apache-2.0
# Copyright 2011-2022 Blender Foundation

# <pep8 compliant>

import bpy

from .base_node import USDNode


class FilterNode(USDNode):
    """Takes in USD and filters out matching path or names"""
    bl_idname = 'usdhydra.FilterNode'
    bl_label = "Filter"
    bl_icon = "FILTER"

    def update_data(self, context):
        self.reset()

    filter_path: bpy.props.StringProperty(
        name="Pattern",
        description="USD Path pattern. Use special characters means:\n"
                    "  * - any word or subword\n"
                    "  ** - several words separated by '/' or subword",
        default="/*",
        update=update_data
    )

    def draw_buttons(self, context, layout):
        super().draw_buttons(context, layout)
        layout.prop(self, 'filter_path')

    def compute(self, **kwargs):
        input_stage = self.get_input_link('Input', **kwargs)
        if not input_stage:
            return None

        return self.c_compute(input_stage, self.filter_path)


class MergeNode(USDNode):
    """Merges two USD streams"""
    bl_idname = 'usdhydra.MergeNode'
    bl_label = "Merge"
    bl_icon = "SELECT_EXTEND"
    MAX_INPUTS_NUMBER = 10

    input_names = tuple(f"Input {i + 1}" for i in range(MAX_INPUTS_NUMBER))

    def update_inputs_number(self, context):
        for i in range(self.MAX_INPUTS_NUMBER):
            self.inputs[i].hide = i >= self.inputs_number

    def set_inputs_number(self, value):
        max_i = max((i if input.is_linked else 0) for i, input in enumerate(self.inputs)) + 1
        self["inputs_number"] = value if value > max_i else max_i

    def get_inputs_number(self):
        return self.get("inputs_number", 2)

    inputs_number: bpy.props.IntProperty(
        name="Inputs",
        min=2, max=MAX_INPUTS_NUMBER, default=2,
        update=update_inputs_number, set=set_inputs_number, get=get_inputs_number
    )

    def init(self, context):
        super().init(context)
        self.update_inputs_number(context)

    def draw_buttons(self, context, layout):
        super().draw_buttons(context, layout)
        layout.prop(self, 'inputs_number')

    def compute(self, **kwargs):
        ref_stages = []
        for i in range(len(self.inputs)):
            stage = self.get_input_link(i, **kwargs)
            if stage:
                ref_stages.append(stage)

        if not ref_stages:
            return None

        if len(ref_stages) == 1:
            return ref_stages[0]

        return self.c_compute(*ref_stages)


class RootNode(USDNode):
    """Create root primitive and make it parent for USD primitives"""
    bl_idname = 'usdhydra.RootNode'
    bl_label = "Root"
    bl_icon = "COLLECTION_NEW"

    def update_data(self, context):
        self.reset()

    name: bpy.props.StringProperty(
        name="Name",
        description="Name for USD root primitive",
        default="Root",
        update=update_data
    )
    type:  bpy.props.EnumProperty(
        name="Type",
        description="Filter by type for USD primitives",
        items=(('Xform', "Xform", "Xform primitive type"),
               ('Scope', "Scope", "Scope primitive type"),
               ('SkelRoot', "SkelRoot", "SkelRoot primitive type"),
               ('None', "None", "No primitive type")),
        default='Xform',
        update=update_data
    )

    def draw_buttons(self, context, layout):
        super().draw_buttons(context, layout)
        layout.prop(self, 'name')
        layout.prop(self, 'type')

    def compute(self, **kwargs):
        input_stage = self.get_input_link('Input', **kwargs)

        if not input_stage:
            return None

        if not self.name:
            return input_stage

        return self.c_compute(input_stage, self.name, self.type)
