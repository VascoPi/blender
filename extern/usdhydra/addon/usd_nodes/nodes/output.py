# SPDX-License-Identifier: Apache-2.0
# Copyright 2011-2022 Blender Foundation

# <pep8 compliant>

from .base_node import USDNode
# from . import log


class OutputNode(USDNode):
    """Output USD Node"""
    bl_idname = 'usdhydra.OutputNode'
    bl_label = "Output"
    bl_icon = "EXPORT"

    output_name = ""

    def compute(self, **kwargs):
        return self.get_input_link('Input', **kwargs)

    def node_computed(self):
        # notify USD nodetree that Output node was computed
        nodetree = self.id_data
        if self.name == nodetree.output_node.name:
            nodetree.output_node_computed()
