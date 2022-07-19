# SPDX-License-Identifier: Apache-2.0
# Copyright 2011-2022 Blender Foundation

# <pep8 compliant>
import platform
from pathlib import Path

import bpy


OS = platform.system()
IS_WIN = OS == 'Windows'
IS_MAC = OS == 'Darwin'
IS_LINUX = OS == 'Linux'

LIBS_DIR = Path(r"d:\vasyl\AMD\blender-git\usd\bin_1\USD\install")


def update_ui(area_type='PROPERTIES', region_type='WINDOW'):
    for window in bpy.context.window_manager.windows:
        for area in window.screen.areas:
            if area.type == area_type:
                for region in area.regions:
                    if region.type == region_type:
                        region.tag_redraw()
