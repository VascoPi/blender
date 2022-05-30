# SPDX-License-Identifier: Apache-2.0
# Copyright 2011-2022 Blender Foundation

# <pep8 compliant>


bl_info = {
    "name": "USD Hydra render engine",
    "author": "AMD",
    "version": (2, 0, 0),
    "blender": (3, 1, 0),
    "location": "Info header > Render engine menu",
    "description": "USD Hydra renderer integration",
    "warning": "",
    "doc_url": "",
    "tracker_url": "",
    "support": 'TESTING',
    "category": "Render"
}

# Support 'reload' case.
if "bpy" in locals():
    import importlib
    if "engine" in locals():
        importlib.reload(engine)
    if "ui" in locals():
        importlib.reload(ui)
    # if "operators" in locals():
    #     importlib.reload(operators)
    if "properties" in locals():
        importlib.reload(properties)


from . import (
    engine,
    usd_nodes,
    properties,
    ui,
    handlers,
)


def exit():
    engine.exit()


def register():
    import atexit
    from bpy.utils import register_class
    # from . import ui
    # from . import operators
    # from . import properties
    # from . import presets

    # Make sure we only registered the callback once.
    atexit.unregister(exit)
    atexit.register(exit)

    engine.init()

    properties.register()
    ui.register()
    # operators.register()
    # presets.register()
    usd_nodes.register()
    handlers.register()

    register_class(engine.HdUSDEngine)


def unregister():
    from bpy.utils import unregister_class
    # from . import ui
    # from . import operators
    # from . import properties
    # from . import presets

    # bpy.app.handlers.version_update.remove(version_update.do_versions)

    ui.unregister()
    # operators.unregister()
    properties.unregister()
    # presets.unregister()
    usd_nodes.unregister()
    handlers.unregister()

    unregister_class(engine.HdUSDEngine)
