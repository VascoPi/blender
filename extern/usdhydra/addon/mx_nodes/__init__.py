# SPDX-License-Identifier: Apache-2.0
# Copyright 2011-2022 Blender Foundation

# <pep8 compliant>

import bpy

from ..utils.logging import Log
log = Log("mx_nodes")

from . import node_tree, nodes


register_trees, unregister_trees = bpy.utils.register_classes_factory([
    node_tree.MxNodeTree,
])


def register():
    register_trees()
    nodes.register()


def unregister():
    unregister_trees()
    nodes.unregister()
