# SPDX-License-Identifier: Apache-2.0
# Copyright 2011-2022 Blender Foundation

# <pep8 compliant>

import bpy

from pxr import Vt

from .logging import Log
log = Log("utils")


BLENDER_VERSION = f'{bpy.app.version[0]}.{bpy.app.version[1]}'
RENDER_DELEGATE_ADDONS = set()


def title_str(str):
    s = str.replace('_', ' ')
    return s[:1].upper() + s[1:]


def code_str(str):
    return str.replace(' ', '_').replace('.', '_')


def pass_node_reroute(link):
    while isinstance(link.from_node, bpy.types.NodeReroute):
        if not link.from_node.inputs[0].links:
            return None

        link = link.from_node.inputs[0].links[0]

    return link if link.is_valid else None


def update_ui(area_type='PROPERTIES', region_type='WINDOW'):
    for window in bpy.context.window_manager.windows:
        for area in window.screen.areas:
            if area.type == area_type:
                for region in area.regions:
                    if region.type == region_type:
                        region.tag_redraw()


def get_VtValue(val):
    if isinstance(val, str):
        return Vt.Token(val)

    if isinstance(val, bool):
        return Vt.Bool(val)

    if isinstance(val, float):
        return Vt.Float(val)

    if isinstance(val, int):
        return Vt.Int(val)

    return Vt.Bool(val)


def register_delegate(delegate_dir, engine_bl_idname):
    import _usdhydra
    from ..ui import USDHydra_Panel, USDHydra_Operator
    from ..mx_nodes.node_tree import MxNodeTree
    from ..usd_nodes.node_tree import USDTree

    global RENDER_DELEGATE_ADDONS

    _usdhydra.init_delegate(str(delegate_dir))
    USDHydra_Panel.COMPAT_ENGINES.add(engine_bl_idname)
    USDHydra_Operator.COMPAT_ENGINES.add(engine_bl_idname)
    USDTree.COMPAT_ENGINES.add(engine_bl_idname)
    MxNodeTree.COMPAT_ENGINES.add(engine_bl_idname)
    RENDER_DELEGATE_ADDONS.add(engine_bl_idname)


def unregister_delegate(engine_bl_idname):
    from ..ui import USDHydra_Panel, USDHydra_Operator
    from ..mx_nodes.node_tree import MxNodeTree
    from ..usd_nodes.node_tree import USDTree

    try:
        USDHydra_Panel.COMPAT_ENGINES.remove(engine_bl_idname)
        USDHydra_Operator.COMPAT_ENGINES.remove(engine_bl_idname)
        USDTree.COMPAT_ENGINES.remove(engine_bl_idname)
        MxNodeTree.COMPAT_ENGINES.remove(engine_bl_idname)

    except:
        pass


def disable_delegates():
    import addon_utils
    import bpy
    for delegate in RENDER_DELEGATE_ADDONS:
        enabled, loaded = addon_utils.check(delegate)
        log.warn("Delegate state", delegate, loaded, enabled)
        if enabled:
            log.warn("Disable Delegate ", delegate)
            addon_utils.disable(delegate)
            bpy.ops.preferences.addon_disable(module=delegate)


def enable_delegates():
    import addon_utils, sys, importlib
    for delegate in RENDER_DELEGATE_ADDONS:
        enabled, loaded  = addon_utils.check(delegate)
        if not loaded or not loaded:
            mod = sys.modules.get(delegate)
            importlib.reload(mod)
            addon_utils.enable(delegate)
