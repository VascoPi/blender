# SPDX-License-Identifier: Apache-2.0
# Copyright 2011-2022 Blender Foundation

# <pep8 compliant>

import tempfile
import _usdhydra
from logging import getLevelName
from pathlib import Path

import bpy
from bpy.types import AddonPreferences, Operator
from bpy.props import StringProperty, BoolProperty, EnumProperty
from bpy_extras.io_utils import ImportHelper

from ..utils import logging
from ..utils.delegate import get_delegates, manager


log = logging.Log('preferences')


class USDHYDRA_ADDON_install_delegate(Operator, ImportHelper):
    bl_idname = "usdhydra.install_render_delegate"
    bl_label = "Add Render Delegate"

    filename_ext = ".zip"
    filepath: bpy.props.StringProperty(
        name="File Path",
        maxlen=1024, subtype="FILE_PATH"
    )
    filter_glob: bpy.props.StringProperty(default="*.zip")

    @classmethod
    def poll(cls, context):
        return manager.is_available

    def execute(self, context):
        manager.filepath = self.filepath
        manager.install_delegate()
        return {'FINISHED'}


class USDHYDRA_ADDON_PT_preferences(AddonPreferences):
    bl_idname = "usdhydra"

    def update_temp_dir(self, value):
        if not Path(self.tmp_dir).exists() or tempfile.gettempdir() == str(Path(self.tmp_dir)):
            log.info(f"Current temp directory is {tempfile.gettempdir()}")
            return

        tempfile.tempdir = Path(self.tmp_dir)
        bpy.context.preferences.addons['usdhydra'].preferences['tmp_dir'] = str(_usdhydra.utils.get_temp_dir())
        log.info(f"Current temp directory is changed to {bpy.context.preferences.addons['usdhydra'].preferences.tmp_dir}")

    def update_log_level(self, context):
        logging.logger.setLevel(self.log_level)
        log.critical(f"Log level is set to {self.log_level}")

    tmp_dir: StringProperty(
        name="Temp Directory",
        description="Set temp directory",
        maxlen=1024,
        subtype='DIR_PATH',
        default=str(_usdhydra.utils.get_temp_dir()),
        update=update_temp_dir,
    )
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
        default=getLevelName(logging.logger.level),
        update=update_log_level,
    )
    show_settings: BoolProperty(
        name="Developer Settings",
        default=False,
    )
    show_delegate: BoolProperty(
        name="Render Delegate",
        default=False,
    )

    def draw(self, context):
        def _draw_settings(layout):
            layout.separator()
            layout.prop(self, "tmp_dir", icon='NONE' if Path(self.tmp_dir).exists() else 'ERROR')
            layout.prop(self, "dev_tools")
            layout.prop(self, "log_level")
            layout.separator()

        def _draw_delegates(layout):
            layout.separator()
            layout.operator(HDUSD_MX_OP_install_delegate.bl_idname, icon='IMPORT',
                            text="Install Delegate..."
                            if manager.is_available
                            else f"Install Delegate...{manager.progress}%")

            _draw_delegate_item(layout)
            layout.separator()

        def _draw_delegate_item(layout):
            for key, value in get_delegates().items():
                row = layout.row(align=True)
                row.alignment = 'LEFT'
                split_name = row.split()
                split_name.label(text=key)
                row.label(text=value)

        icon_close = "DISCLOSURE_TRI_RIGHT"
        icon_open = "DISCLOSURE_TRI_DOWN"

        layout = self.layout
        col = layout.column()

        col.prop(self, "show_settings", icon=icon_open if self.show_settings else icon_close)
        layout = col.column()
        if self.show_settings:
            _draw_settings(layout)

        col.prop(self, "show_delegate", icon=icon_open if self.show_delegate else icon_close)
        layout = col.column()
        if self.show_delegate:
            _draw_delegates(layout)

        row = col.row()
        #row.operator("wm.url_open", text="Main Site", icon='URL').url = bl_info["main_web"]
        #row.operator("wm.url_open", text="Community", icon='COMMUNITY').url = bl_info["community"]


def get_addon_pref():
    return bpy.context.preferences.addons['usdhydra'].preferences
