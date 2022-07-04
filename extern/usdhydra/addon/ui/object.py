# SPDX-License-Identifier: Apache-2.0
# Copyright 2011-2022 Blender Foundation

# <pep8 compliant>

import bpy

#from pxr import UsdGeom

from . import USDHydra_Panel
from ..properties.object import GEOM_TYPES


class USDHYDRA_OP_usd_object_show_hide(bpy.types.Operator):
    """Show/Hide USD object"""
    bl_idname = "usdhydra.usd_object_show_hide"
    bl_label = "Show/Hide"

    def execute(self, context):
        # obj = context.object
        # prim = obj.usdhydra.get_prim()
        # im = UsdGeom.Imageable(prim)
        # if im.ComputeVisibility() == 'invisible':
        #     im.MakeVisible()
        # else:
        #     im.MakeInvisible()

        return {'FINISHED'}


class USDHYDRA_OBJECT_PT_usd_settings(USDHydra_Panel):
    bl_label = "USD Settings"
    bl_context = 'object'

    @classmethod
    def poll(cls, context):
        return super().poll(context) and context.object and context.object.usdhydra.is_usd

    def draw(self, context):
        layout = self.layout
        # obj = context.object
        # prim = obj.usdhydra.get_prim()
        # if not prim:
        #     return
        #
        # layout = self.layout
        # layout.use_property_split = True
        # layout.use_property_decorate = False
        #
        # split = layout.row(align=True).split(factor=0.4)
        # col1 = split.column()
        # col1.alignment = 'RIGHT'
        # col2 = split.column()
        #
        # col1.label(text="Name")
        # col2.label(text=prim.GetName())
        #
        # col1.label(text="Path")
        # col2.label(text=str(prim.GetPath()))
        #
        # col1.label(text="Type")
        # col2.label(text=prim.GetTypeName())
        #
        # if prim.GetTypeName() in GEOM_TYPES:
        #     visible = UsdGeom.Imageable(prim).ComputeVisibility() != 'invisible'
        #     icon = 'HIDE_OFF' if visible else 'HIDE_ON'
        #
        #     col1.label(text="Visibility")
        #     col2.operator(USDHYDRA_OP_usd_object_show_hide.bl_idname,
        #                   text="Hide" if visible else 'Show',
        #                   icon='HIDE_OFF' if visible else 'HIDE_ON',
        #                   emboss=True, depress=False)
        #
        # from ..properties.preferences import get_addon_pref
        # if not get_addon_pref().usd_mesh_assign_material_enabled:
        #     return
        #
        # if prim.GetTypeName() in 'Mesh':
        #     layout.prop(obj.usdhydra, 'material')
