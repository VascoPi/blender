# SPDX-License-Identifier: Apache-2.0
# Copyright 2011-2022 Blender Foundation

# <pep8 compliant>

import bpy
import _usdhydra
import MaterialX as mx

from .usd_nodes import node_tree
from .utils import stages


def init():
    _usdhydra.init()


def exit():
    _usdhydra.exit()


class USDHydraEngine(bpy.types.RenderEngine):
    bl_idname = 'USDHydra'
    bl_label = "USD Hydra Internal"
    bl_info = "USD Hydra rendering plugin"

    bl_use_preview = True
    bl_use_shading_nodes = True
    bl_use_shading_nodes_custom = False
    bl_use_gpu_context = True

    session = None

    def __init__(self):
        self.session = None

    def __del__(self):
        if not self.session:
            return

        session_free(self.session)

    # final render
    def update(self, data, depsgraph):
        is_blender_scene = not bool(depsgraph.scene.usdhydra.final.data_source)
        stage = 0

        if not is_blender_scene:
            usd_nodetree = node_tree.get_usd_nodetree()
            if not usd_nodetree:
                return

            output_node = usd_nodetree.output_node
            if not output_node:
                return

            stage = stages.get(output_node)
            if not stage:
                return

        if not self.session:
            self.session = session_create(self)

        materialx_data = self.get_materialx_data(data, depsgraph)
        print(materialx_data)
        session_reset(self.session, data, bpy.context, materialx_data, depsgraph, is_blender_scene, stage)

    def render(self, depsgraph):
        if not self.session:
            return

        session_render(self.session, depsgraph)

    def render_frame_finish(self):
        pass

    # viewport render
    def view_update(self, context, depsgraph):
        data = context.blend_data
        is_blender_scene = not bool(context.scene.usdhydra.viewport.data_source)
        stage = 0

        if not is_blender_scene:
            usd_nodetree = node_tree.get_usd_nodetree()
            if not usd_nodetree:
                return

            output_node = usd_nodetree.output_node
            if not output_node:
                return

            stage = stages.get(output_node)
            if not stage:
                return

        if not self.session:
            self.session = session_create(self)

        materialx_data = self.get_materialx_data(context, depsgraph)

        session_reset(self.session, data, context, depsgraph, materialx_data, is_blender_scene, stage)
        session_view_update(self.session, depsgraph, context, context.space_data, context.region_data)

    def view_draw(self, context, depsgraph):
        if not self.session:
            return

        session_view_draw(self.session, depsgraph, context, context.space_data, context.region_data)


    def get_materialx_data(self, context, depsgraph):
        data =[]
        for obj in bpy.context.scene.objects:
            if obj.type in ('EMPTY', 'ARMATURE', 'LIGHT', 'CAMERA'):
                continue

            for mat_slot in obj.material_slots:
                if not mat_slot:
                    continue

                mat = mat_slot.material

                mx_file = _usdhydra.utils.get_temp_file(".mtlx", f'{mat.name}{mat.usdhydra.mx_node_tree.name if mat.usdhydra.mx_node_tree else ""}')
                print(mx_file, str(mx_file))
                doc = mat.usdhydra.export(obj)
                if not doc:
                    # log.warn("MX export failed", mat)
                    return None
                # self.nodedef.getOutput(self.outputs[out_key].name)

                mx.writeToXmlFile(doc, str(mx_file).replace('/', "\\"))
                surfacematerial = next((node for node in doc.getNodes() if node.getCategory() == 'surfacematerial'))

                data.append((mat.name, str(mx_file), surfacematerial.getName()))

        return tuple(data)


def session_create(engine: USDHydraEngine):
    return _usdhydra.session.create(engine.as_pointer())


def session_free(session):
    _usdhydra.session.free(session)


def session_reset(session, data, context, depsgraph, materialx_data, is_blender_scene, stage):
    _usdhydra.session.reset(session, data.as_pointer(), context.as_pointer(), depsgraph.as_pointer(), materialx_data, is_blender_scene, stage)


def session_render(session, depsgraph):
    _usdhydra.session.render(session, depsgraph.as_pointer())


def session_view_draw(session, depsgraph, context, space_data, region_data):
    _usdhydra.session.view_draw(session, depsgraph.as_pointer(), context.as_pointer(),
                             space_data.as_pointer(), region_data.as_pointer())


def session_view_update(session, depsgraph, context, space_data, region_data):
    _usdhydra.session.view_update(session, depsgraph.as_pointer(), context.as_pointer(),
                             space_data.as_pointer(), region_data.as_pointer())
