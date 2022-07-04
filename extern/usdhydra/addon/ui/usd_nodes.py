# SPDX-License-Identifier: Apache-2.0
# Copyright 2011-2022 Blender Foundation

# <pep8 compliant>

import _usdhydra
from . import USDHydra_Panel, USDHydra_ChildPanel, USDHydra_Operator
from ..usd_nodes.nodes.base_node import USDNode

from ..utils.logging import Log
log = Log('ui.usd_nodes')


class USDHYDRA_NODE_PT_usd_stage(USDHydra_Panel):
    bl_label = "USD Node Prims"
    bl_space_type = "NODE_EDITOR"
    bl_region_type = "UI"
    bl_category = "Item"

    @classmethod
    def poll(cls, context):
        node = context.active_node
        return node and isinstance(node, USDNode)

    def draw(self, context):
        layout = self.layout
        usd_node = context.active_node
        stage_prop = usd_node.stage_prop

        # layout.label(text=f"stage: {stage_prop.stage}")

        layout.template_list(
            "USDHYDRA_UL_usd_stage", "",
            stage_prop, "prims",
            stage_prop, "prim_index",
            sort_lock=True
        )


class USDHYDRA_OP_usd_tree_node_print_stage(USDHydra_Operator):
    """ Print selected USD nodetree node stage to console """
    bl_idname = "usdhydra.usd_tree_node_print_stage"
    bl_label = "Print Stage To Console"

    @classmethod
    def poll(cls, context):
        return super().poll(context) and context.space_data.tree_type == 'usdhydra.USDTree' and \
               context.active_node

    def execute(self, context):
        node = context.active_node

        stage = node.stage
        if not stage:
            log.info(f"No USD stage for node {node.name}")
            return {'CANCELLED'}

        usd_str = _usdhydra.stage.export_to_str(stage, True)
        print(usd_str)

        return {'FINISHED'}


class USDHYDRA_OP_usd_tree_node_print_root_layer(USDHydra_Operator):
    """ Print selected USD nodetree node stage to console """
    bl_idname = "usdhydra.usd_tree_node_print_root_layer"
    bl_label = "Print Root Layer To Console"

    @classmethod
    def poll(cls, context):
        return super().poll(context) and context.space_data.tree_type == 'usdhydra.USDTree' and \
               context.active_node

    def execute(self, context):
        node = context.active_node

        stage = node.stage
        if not stage:
            log.info(f"No USD stage for node {node.name}")
            return {'CANCELLED'}

        usd_str = _usdhydra.stage.export_to_str(stage, False)
        print(usd_str)

        return {'FINISHED'}


class USDHYDRA_NODE_PT_usd_nodetree_tools(USDHydra_Panel):
    bl_label = "USD Tools"
    bl_space_type = "NODE_EDITOR"
    bl_region_type = "UI"
    bl_category = "Tool"

    @classmethod
    def poll(cls, context):
        tree = context.space_data.edit_tree
        return super().poll(context) and tree and tree.bl_idname == 'usdhydra.USDTree'

    def draw(self, context):
        # layout = self.layout
        pass


class USDHYDRA_NODE_PT_usd_nodetree_dev(USDHydra_ChildPanel):
    bl_label = "Dev"
    bl_parent_id = 'USDHYDRA_NODE_PT_usd_nodetree_tools'
    bl_space_type = "NODE_EDITOR"
    bl_region_type = "UI"
    bl_category = "Tool"

    @classmethod
    def poll(cls, context):
        from ..properties.preferences import get_addon_pref
        return get_addon_pref().dev_tools

    def draw(self, context):
        layout = self.layout

        layout.operator(USDHYDRA_OP_usd_tree_node_print_stage.bl_idname)
        layout.operator(USDHYDRA_OP_usd_tree_node_print_root_layer.bl_idname)
