# SPDX-License-Identifier: Apache-2.0
# Copyright 2011-2022 Blender Foundation

# <pep8 compliant>

import bpy

from . import USDHydraProperties
from .usd_stage import UsdStage


class WindowManagerProperties(USDHydraProperties):
    bl_type = bpy.types.WindowManager

    usd_stages: bpy.props.CollectionProperty(type=UsdStage)
