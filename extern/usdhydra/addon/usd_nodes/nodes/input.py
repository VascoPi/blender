# SPDX-License-Identifier: Apache-2.0
# Copyright 2011-2022 Blender Foundation

# <pep8 compliant>

from pathlib import Path

import bpy

from .base_node import USDNode


class UsdFileNode(USDNode):
    bl_idname = 'usdhydra.UsdFileNode'
    bl_label = "USD File"
    bl_icon = "FILE"
    bl_width_default = 250
    bl_width_min = 250

    input_names = ()
    use_hard_reset = False

    def update_data(self, context):
        self.reset(True)

    filename: bpy.props.StringProperty(
        name="USD File",
        subtype='FILE_PATH',
        update=update_data,
    )

    filter_path: bpy.props.StringProperty(
        name="Pattern",
        description="USD Path pattern. Use special characters means:\n"
                    "  * - any word or subword\n"
                    "  ** - several words separated by '/' or subword",
        default='/*',
        update=update_data
    )

    def draw_buttons(self, context, layout):
        super().draw_buttons(context, layout)
        layout.prop(self, 'filename')
        layout.prop(self, 'filter_path')

    def compute(self, **kwargs):
        if not self.filename:
            return None

        file = Path(bpy.path.abspath(self.filename))
        if not file.is_file():
            # log.warn("Couldn't find USD file", file, self)
            return None

        return self.c_compute(str(file), self.filter_path)
