# SPDX-License-Identifier: Apache-2.0
# Copyright 2011-2022 Blender Foundation

# <pep8 compliant>

import bpy
from bpy.types import AddonPreferences, Operator
from bpy.props import StringProperty, BoolProperty, EnumProperty

import _usdhydra

from ..utils import logging
log = logging.Log('preferences')


class USDHYDRA_ADDON_PT_preferences(AddonPreferences):
    bl_idname = "usdhydra"

    def init(self):
        self.update_log_level(None)
        self._init(None)

    def save(self):
        if hasattr(bpy.context, 'scene'):
            bpy.ops.wm.save_userpref()

    # def update_temp_dir(self, value):
    #     if not Path(self.tmp_dir).exists() or tempfile.gettempdir() == str(Path(self.tmp_dir)):
    #         log.info(f"Current temp directory is {tempfile.gettempdir()}")
    #         return
    #
    #     tempfile.tempdir = Path(self.tmp_dir)
    #     bpy.context.preferences.addons['usdhydra'].preferences['tmp_dir'] = str(_usdhydra.utils.get_temp_dir())
    #     log.info(f"Current temp directory is changed to {bpy.context.preferences.addons['usdhydra'].preferences.tmp_dir}")

    def update_log_level(self, context):
        logging.logger.setLevel(self.log_level)
        self.save()

    def _init(self, context):
        _usdhydra.init()
        self.save()

    # tmp_dir: StringProperty(
    #     name="Temp Directory",
    #     description="Set temp directory",
    #     maxlen=1024,
    #     subtype='DIR_PATH',
    #     default=_usdhydra.utils.get_temp_dir(),
    #     update=update_temp_dir,
    # )

    dev_tools: BoolProperty(
        name="Developer Tools",
        description="Enable developer tools",
        default=False,
    )
    log_level: EnumProperty(
        name="Log Level",
        description="Select logging level",
        items=(('DEBUG', "Debug", "Log level DEBUG"),
               ('INFO', "Info", "Log level INFO"),
               ('WARNING', "Warning", "Log level WARN"),
               ('ERROR', "Error", "Log level ERROR"),
               ('CRITICAL', "Critical", "Log level CRITICAL")),
        default='INFO',
        update=update_log_level,
    )

    def draw(self, context):
        layout = self.layout
        layout.separator()
        # layout.prop(self, "tmp_dir", icon='NONE' if Path(self.tmp_dir).exists() else 'ERROR')
        layout.prop(self, "dev_tools")
        layout.prop(self, "log_level")
        layout.separator()

        # row = col.row()
        #row.operator("wm.url_open", text="Main Site", icon='URL').url = bl_info["main_web"]
        #row.operator("wm.url_open", text="Community", icon='COMMUNITY').url = bl_info["community"]


def get_addon_pref():
    return bpy.context.preferences.addons['usdhydra'].preferences
