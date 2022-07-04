# SPDX-License-Identifier: Apache-2.0
# Copyright 2011-2022 Blender Foundation

# <pep8 compliant>

import bpy

from .nodes.output import OutputNode

# from ..viewport import usd_collection
# from ..engine.viewport_engine import ViewportEngineNodetree


class USDTree(bpy.types.ShaderNodeTree):
    """
    Holds hierarchy of data and composition of USD for rendering
    The basic (default) graph should be simply

    Read Blender Data (scene) ---> Hydra Render

    When nodes or tree is updated, the node computation is re-run
    """
    bl_label = "USD"
    bl_icon = 'NODETREE'
    bl_idname = 'usdhydra.USDTree'
    COMPAT_ENGINES = {'USDHydra'}

    _is_resetting = False
    _do_update = True

    @classmethod
    def poll(cls, context):
        return context.engine in cls.COMPAT_ENGINES

    @property
    def output_node(self):
        return next((node for node in self.nodes if isinstance(node, OutputNode)), None)

    def _reset_nodes(self, nodes, is_hard):
        self._is_resetting = True

        try:
            nodes = tuple(node for node in nodes if not isinstance(node, (bpy.types.NodeReroute, bpy.types.NodeFrame))
                          and (is_hard or node.use_hard_reset))

            for node in nodes:
                node.free()

            for node in nodes:
                node.final_compute()

        finally:
            self._is_resetting = False

    # this is called from Blender
    def update(self):
        if not self._do_update:
            return

        self._reset_nodes(self.nodes, False)

    def reset(self):
        self._reset_nodes(self.nodes, True)

    def depsgraph_update(self, depsgraph):
        if self._is_resetting:
            return

        for node in self.nodes:
            if not isinstance(node, (bpy.types.NodeReroute, bpy.types.NodeFrame)):
                node.depsgraph_update(depsgraph)

    def frame_change(self, depsgraph):
        if self._is_resetting:
            return

        for node in self.nodes:
            if not isinstance(node, (bpy.types.NodeReroute, bpy.types.NodeFrame)):
                node.frame_change(depsgraph)

    def material_update(self, depsgraph):
        if self._is_resetting:
            return

        for node in self.nodes:
            if not isinstance(node, (bpy.types.NodeReroute, bpy.types.NodeFrame)):
                node.material_update(depsgraph)

    def no_update_call(self, op, *args, **kwargs):
        """This function prevents call of self.update() during calling our function"""
        if not self._do_update:
            return op(*args, **kwargs)

        self._do_update = False
        try:
            return op(*args, **kwargs)
        finally:
            self._do_update = True

    def add_basic_nodes(self, source='SCENE'):
        """ Reset basic node tree structure using scene or USD file as an input """

        def create_nodes():
            self.nodes.clear()

            if source == 'USD_FILE':
                input_node = self.nodes.new("usd.UsdFileNode")
            else:  # default 'SCENE'
                input_node = self.nodes.new("usd.BlenderDataNode")
            input_node.location = (input_node.location[0] - 150, input_node.location[1])

            output_node = self.nodes.new("usd.OutputNode")
            output_node.location = (output_node.location[0] + 150, output_node.location[1])

            self.links.new(input_node.outputs[0], output_node.inputs[0])

        self.no_update_call(create_nodes)
        self.reset()

    def output_node_computed(self):
        context = bpy.context
        # if context.scene.usdhydra.viewport.data_source == self.name:
        #     usd_collection.update(context)
        #
        # if context.scene.usdhydra.final.data_source == self.name:
        #     context.scene.usdhydra.final.nodetree_update(context)
        #
        # ViewportEngineNodetree.nodetree_output_node_computed(self)


def get_usd_nodetree():
    ''' return first USD nodetree found '''
    return next((nodetree for nodetree in bpy.data.node_groups if isinstance(nodetree, USDTree)),
                None)


def reset():
    for nodetree in bpy.data.node_groups:
        if isinstance(nodetree, USDTree):
            nodetree.reset()


def depsgraph_update(depsgraph):
    for nodetree in bpy.data.node_groups:
        if isinstance(nodetree, USDTree):
            nodetree.depsgraph_update(depsgraph)


def frame_change(depsgraph):
    for nodetree in bpy.data.node_groups:
        if isinstance(nodetree, USDTree):
            nodetree.frame_change(depsgraph)


def material_update(material):
    for nodetree in bpy.data.node_groups:
        if isinstance(nodetree, USDTree):
            nodetree.material_update(material)
