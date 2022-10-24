# SPDX-License-Identifier: Apache-2.0
# Copyright 2011-2022 Blender Foundation

# <pep8 compliant>

import bpy


class USDHydra_Operator(bpy.types.Operator):
    COMPAT_ENGINES = {'USDHydraHdStormRendererPlugin'}

    @classmethod
    def poll(cls, context):
        return context.engine in cls.COMPAT_ENGINES


class USDHydra_Panel(bpy.types.Panel):
    bl_space_type = 'PROPERTIES'
    bl_region_type = 'WINDOW'
    bl_context = 'render'
    COMPAT_ENGINES = {'USDHydraHdStormRendererPlugin'}

    @classmethod
    def poll(cls, context):
        return context.engine in cls.COMPAT_ENGINES


class USDHydra_ChildPanel(bpy.types.Panel):
    bl_space_type = 'PROPERTIES'
    bl_region_type = 'WINDOW'
    bl_parent_id = ''


from . import (
    panels,
    render,
    light,
    world,
    object,
    usd_nodes,
    usd_stage,
)


register_classes, unregister_classes = bpy.utils.register_classes_factory([
    render.USDHYDRA_OP_data_source,
    render.USDHYDRA_OP_nodetree_camera,
    render.USDHYDRA_MT_data_source_final,
    render.USDHYDRA_MT_nodetree_camera_final,
    render.USDHYDRA_MT_nodetree_camera_viewport,
    render.USDHYDRA_MT_data_source_viewport,
    render.USDHYDRA_RENDER_PT_render_settings_final,
    render.USDHYDRA_RENDER_PT_render_settings_viewport,

    light.USDHYDRA_LIGHT_PT_light,

    world.USDHYDRA_WORLD_PT_surface,

    object.USDHYDRA_OBJECT_PT_usd_settings,
    object.USDHYDRA_OP_usd_object_show_hide,

    usd_nodes.USDHYDRA_NODE_PT_usd_stage,
    usd_nodes.USDHYDRA_OP_usd_tree_node_print_stage,
    usd_nodes.USDHYDRA_OP_usd_tree_node_print_root_layer,
    usd_nodes.USDHYDRA_NODE_PT_usd_nodetree_tools,
    usd_nodes.USDHYDRA_NODE_PT_usd_nodetree_dev,

    usd_stage.USDHYDRA_OP_usd_stage_prim_expand,
    # usd_stage.USDHYDRA_OP_usd_stage_prim_show_hide,
    usd_stage.USDHYDRA_UL_usd_stage,
])


def register():
    panels.register()
    register_classes()


def unregister():
    panels.unregister()
    unregister_classes()
