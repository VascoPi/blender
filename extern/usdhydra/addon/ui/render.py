# SPDX-License-Identifier: Apache-2.0
# Copyright 2011-2022 Blender Foundation

# <pep8 compliant>

import bpy

from . import USDHydra_Panel


class USDHYDRA_OP_data_source(bpy.types.Operator):
    """Select render source"""
    bl_idname = "usdhydra.data_source"
    bl_label = "Data Source"

    data_source: bpy.props.StringProperty(default="")
    engine_type: bpy.props.EnumProperty(
        items=(('FINAL', "Final", "For final render"),
               ('VIEWPORT', "Viewport", "For viewport render")),
        default='FINAL'
    )

    def execute(self, context):
        settings = context.scene.usdhydra.final if self.engine_type == 'FINAL' else\
                   context.scene.usdhydra.viewport
        settings.data_source = self.data_source
        settings.nodetree_update(context)

        return {"FINISHED"}


class USDHYDRA_OP_nodetree_camera(bpy.types.Operator):
    """Select camera"""
    bl_idname = "usdhydra.nodetree_camera"
    bl_label = "Camera"
    engine_type: bpy.props.EnumProperty(
        items=(('FINAL', "Final", "For final render"),
               ('VIEWPORT', "Viewport", "For viewport render")),
        default='FINAL'
    )

    nodetree_camera: bpy.props.StringProperty(default="")

    def execute(self, context):
        settings = context.scene.usdhydra.final if self.engine_type == 'FINAL' else \
            context.scene.usdhydra.viewport

        settings.nodetree_camera = self.nodetree_camera
        return {"FINISHED"}


class DataSourceMenu(bpy.types.Menu):
    bl_label = "Data Source"
    engine_type = None

    def draw(self, context):
        layout = self.layout
        node_groups = bpy.data.node_groups
        op_idname = USDHYDRA_OP_data_source.bl_idname

        op = layout.operator(op_idname, text=context.scene.name, icon='SCENE_DATA')
        op.data_source = ""
        op.engine_type = self.engine_type

        for ng in node_groups:
            if ng.bl_idname != 'usdhydra.USDTree':
                continue

            row = layout.row()
            row.enabled = bool(ng.output_node)
            op = row.operator(op_idname, text=ng.name, icon='NODETREE')
            op.data_source = ng.name
            op.engine_type = self.engine_type


class NodetreeCameraMenu(bpy.types.Menu):
    bl_label = "Camera"
    engine_type = None

    def draw(self, context):
        layout = self.layout
        op_idname = USDHYDRA_OP_nodetree_camera.bl_idname
        settings = context.scene.usdhydra.final if self.engine_type == 'FINAL' else \
            context.scene.usdhydra.viewport
        ng = bpy.data.node_groups[settings.data_source]

        output_node = ng.output_node
        if output_node is None:
            return

        stage = output_node.cached_stage()
        if stage is None:
            return

        for prim in stage.TraverseAll():
            if prim.GetTypeName() == 'Camera':
                row = layout.row()
                op = row.operator(op_idname, text=prim.GetPath().pathString)
                op.engine_type = self.engine_type
                op.nodetree_camera = prim.GetPath().pathString


class USDHYDRA_MT_data_source_final(DataSourceMenu):
    """Select data source"""
    bl_idname = "USDHYDRA_MT_data_source_final"
    engine_type = 'FINAL'


class USDHYDRA_MT_nodetree_camera_final(NodetreeCameraMenu):
    """Select camera"""
    bl_idname = "USDHYDRA_MT_nodetree_camera_final"
    engine_type = 'FINAL'


class USDHYDRA_MT_data_source_viewport(DataSourceMenu):
    """Select render source"""
    bl_idname = "USDHYDRA_MT_data_source_viewport"
    engine_type = 'VIEWPORT'


class USDHYDRA_MT_nodetree_camera_viewport(NodetreeCameraMenu):
    """Select camera"""
    bl_idname = "USDHYDRA_MT_nodetree_camera_viewport"
    engine_type = 'VIEWPORT'


class RenderSettingsPanel(USDHydra_Panel):
    bl_context = 'render'
    engine_type = None

    def draw(self, context):
        scene = context.scene
        settings = scene.usdhydra.final if self.engine_type == 'FINAL' else scene.usdhydra.viewport

        layout = self.layout
        layout.use_property_split = True
        layout.use_property_decorate = False

        split = layout.row(align=True).split(factor=0.4)
        col = split.column()
        col.alignment = 'RIGHT'
        col.label(text="Data Source")
        col = split.column()
        col.menu(USDHYDRA_MT_data_source_final.bl_idname if self.engine_type == 'FINAL' else
                 USDHYDRA_MT_data_source_viewport.bl_idname,
                 text=settings.data_source if settings.data_source else scene.name,
                 icon='NODETREE' if settings.data_source else 'SCENE_DATA')

        if settings.data_source:
            split = layout.row(align=True).split(factor=0.4)
            col = split.column()
            col.alignment = 'RIGHT'
            col.label(text="Camera")
            col = split.column()
            col.enabled = settings.nodetree_camera != ''
            col.menu(USDHYDRA_MT_nodetree_camera_final.bl_idname if self.engine_type == 'FINAL' else
                     USDHYDRA_MT_nodetree_camera_viewport.bl_idname,
                     text=settings.nodetree_camera if settings.nodetree_camera else '',
                     icon='CAMERA_DATA')


class USDHYDRA_RENDER_PT_render_settings_final(RenderSettingsPanel):
    """Final render delegate and settings"""
    bl_label = "Final Render Settings"
    engine_type = 'FINAL'


class USDHYDRA_RENDER_PT_render_settings_viewport(RenderSettingsPanel):
    """Viewport render delegate and settings"""
    bl_label = "Viewport Render Settings"
    engine_type = 'VIEWPORT'
