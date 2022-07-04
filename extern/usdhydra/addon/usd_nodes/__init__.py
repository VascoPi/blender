# SPDX-License-Identifier: Apache-2.0
# Copyright 2011-2022 Blender Foundation

# <pep8 compliant>

# from ..utils import logging
# log = logging.Log("usd_nodes")

import bpy

from . import node_tree
from . import nodes


register_trees, unregister_trees = bpy.utils.register_classes_factory([
    node_tree.USDTree,
    # node_tree.RenderTaskTree,
])


def register():
    register_trees()
    nodes.register()


def unregister():
    unregister_trees()
    nodes.unregister()
