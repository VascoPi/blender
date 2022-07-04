# SPDX-License-Identifier: Apache-2.0
# Copyright 2011-2022 Blender Foundation

# <pep8 compliant>

import bpy


class USDHYDRA_OP_usd_stage_prim_expand(bpy.types.Operator):
    """Expand USD item"""
    bl_idname = "usdhydra.usd_stage_prim_expand"
    bl_label = "Expand"

    index: bpy.props.IntProperty()

    def execute(self, context):
        node = context.active_node
        stage_prop = node.stage_prop
        prims = stage_prop.prims
        prim_prop = prims[self.index]

        if len(prims) > self.index + 1 and prims[self.index + 1].indent > prim_prop.indent:
            next_index = self.index + 1
            item_indent = prim_prop.indent
            removed_items = 0
            while True:
                if next_index >= len(prims):
                    break
                if prims[next_index].indent <= item_indent:
                    break
                prims.remove(next_index)
                removed_items += 1

            if stage_prop.prim_index > self.index:
                stage_prop.prim_index = max(self.index, stage_prop.prim_index - removed_items)

        else:
            prim_info = stage_prop.get_prim_info(prim_prop)

            added_items = 0
            for child_index, child_name in enumerate(prim_info['children'], self.index + 1):
                child_prim_prop = prims.add()
                child_prim_prop.path = f"{prim_info['path']}/{child_name}"
                child_prim_prop.name = child_name

                prims.move(len(prims) - 1, child_index)
                added_items += 1

            if stage_prop.prim_index > self.index:
                stage_prop.prim_index += added_items

        return {'FINISHED'}


# class USDHYDRA_OP_usd_stage_prim_show_hide(bpy.types.Operator):
#     """Show/Hide USD item"""
#     bl_idname = "usdhydra.usd_stage_prim_show_hide"
#     bl_label = "Show/Hide"
#
#     index: bpy.props.IntProperty(default=-1)
#
#     def execute(self, context):
#         if self.index == -1:
#             return {'CANCELLED'}
#
#         node = context.active_node
#         usd_list = node.usdhydra.usd_list
#         items = usd_list.items
#         item = items[self.index]
#
#         prim = usd_list.get_prim(item)
#         im = UsdGeom.Imageable(prim)
#         if im.ComputeVisibility() == 'invisible':
#             im.MakeVisible()
#         else:
#             im.MakeInvisible()
#
#         return {'FINISHED'}


class USDHYDRA_UL_usd_stage(bpy.types.UIList):
    def draw_item(self, context, layout, stage_prop, prim_prop, icon, active_data, active_propname, index):
        if self.layout_type not in {'DEFAULT', 'COMPACT'}:
            return

        for i in range(prim_prop.indent):
            layout.split(factor=0.1)

        prims = stage_prop.prims
        prim_info = stage_prop.get_prim_info(prim_prop)

        col = layout.column()
        if not prim_info['children']:
            icon = 'DOT'
            col.enabled = False
        elif len(prims) > index + 1 and prims[index + 1].indent > prim_prop.indent:
            icon = 'TRIA_DOWN'
        else:
            icon = 'TRIA_RIGHT'

        expand_op = col.operator(USDHYDRA_OP_usd_stage_prim_expand.bl_idname, text="", icon=icon,
                                 emboss=False, depress=False)
        expand_op.index = index

        col = layout.column()
        col.label(text=prim_info['name'])
        col.enabled = prim_info['visible']

        col = layout.column()
        col.alignment = 'RIGHT'
        col.label(text=prim_info['type'])
        col.enabled = prim_info['visible']

        # col = layout.column()
        # col.alignment = 'RIGHT'
        # if prim.GetTypeName() == 'Xform':
        #     icon = 'HIDE_OFF' if visible else 'HIDE_ON'
        # else:
        #     col.enabled = False
        #     icon = 'NONE'
        #
        # visible_op = col.operator(USDHYDRA_OP_usd_stage_prim_show_hide.bl_idname, text="", icon=icon,
        #                           emboss=False, depress=False)
        # visible_op.index = index
