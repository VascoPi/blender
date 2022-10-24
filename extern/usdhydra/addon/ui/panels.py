# SPDX-License-Identifier: Apache-2.0
# Copyright 2011-2022 Blender Foundation

# <pep8 compliant>

import bpy
#from .material import update_material_ui


def get_panels():
    # follow the Cycles model of excluding panels we don't want

    exclude_panels = {
        'DATA_PT_area',
        'DATA_PT_context_light',
        'DATA_PT_falloff_curve',
        'DATA_PT_light',
        'NODE_DATA_PT_light',
        'DATA_PT_shadow',
        'DATA_PT_spot',
        'DATA_PT_sunsky',
        'RENDERLAYER_PT_layer_options',
        'RENDERLAYER_PT_layer_passes',
        'RENDERLAYER_PT_views',
        'RENDER_PT_antialiasing',
        'RENDER_PT_bake',
        'RENDER_PT_motion_blur',
        'RENDER_PT_performance',
        'RENDER_PT_freestyle',
        'RENDER_PT_post_processing',
        'RENDER_PT_shading',
        'RENDER_PT_simplify',
        'RENDER_PT_stamp',
        'SCENE_PT_simplify',
        'SCENE_PT_audio',
        'WORLD_PT_ambient_occlusion',
        'WORLD_PT_environment_lighting',
        'WORLD_PT_gather',
        'WORLD_PT_indirect_lighting',
        'WORLD_PT_mist',
        'WORLD_PT_preview',
        'WORLD_PT_world',
    }

    for panel in bpy.types.Panel.__subclasses__():
        if hasattr(panel, 'COMPAT_ENGINES') and 'CYCLES' in panel.COMPAT_ENGINES:
            if panel.__name__ not in exclude_panels:
                yield panel


def register():
    # set USDHydra panels filter
    for panel in get_panels():
        panel.COMPAT_ENGINES.add('USDHydraHdStormRendererPlugin')

    # set update for material ui according to MaterialX nodetree header changes
    #bpy.types.NODE_HT_header.append(update_material_ui)


def unregister():
    # remove USDHydra panels filter
    for panel in get_panels():
        if 'USDHydraHdStormRendererPlugin' in panel.COMPAT_ENGINES:
            panel.COMPAT_ENGINES.remove('USDHydraHdStormRendererPlugin')

    # remove update for material ui according to MaterialX nodetree header changes
    #bpy.types.NODE_HT_header.remove(update_material_ui)
