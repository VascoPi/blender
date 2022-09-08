# SPDX-License-Identifier: Apache-2.0
# Copyright 2011-2022 Blender Foundation

# <pep8 compliant>

import bpy
from bpy.props import (
    EnumProperty,
    FloatProperty,
    IntProperty,
    BoolProperty,
    StringProperty,
    PointerProperty,
    FloatVectorProperty,
)
from .base_node import MxNode


FILE_PATH = r"libraries\bxdf\usd_preview_surface.mtlx"


class MxNode_USD_UsdPreviewSurface(MxNode):
    _file_path = FILE_PATH
    _data_types = {'surfaceshader': {'nd_name': 'ND_UsdPreviewSurface_surfaceshader', 'nd': None}}

    bl_label = 'UsdPreviewSurface'
    bl_idname = 'usdhydra.MxNode_USD_UsdPreviewSurface'
    bl_description = "USD preview surface shader"

    category = 'USD'

    data_type: EnumProperty(name="Type", description="Input Data Type", items=[('surfaceshader', 'Surfaceshader', 'Surfaceshader')], default='surfaceshader', update=MxNode.update_data_type)

    nd_surfaceshader_in_diffuseColor: FloatVectorProperty(name="DiffuseColor", description="", subtype="COLOR", size=3, soft_min=0.0, soft_max=1.0, min=0.0, max=1.0, default=(0.18, 0.18, 0.18), update=MxNode.update_prop)
    nd_surfaceshader_in_emissiveColor: FloatVectorProperty(name="EmissiveColor", description="", subtype="COLOR", size=3, soft_min=0.0, soft_max=1.0, min=0.0, default=(0.0, 0.0, 0.0), update=MxNode.update_prop)
    nd_surfaceshader_in_useSpecularWorkflow: IntProperty(name="UseSpecularWorkflow", description="", default=0, update=MxNode.update_prop)
    nd_surfaceshader_in_specularColor: FloatVectorProperty(name="SpecularColor", description="", subtype="COLOR", size=3, soft_min=0.0, soft_max=1.0, min=0.0, max=1.0, default=(0.0, 0.0, 0.0), update=MxNode.update_prop)
    nd_surfaceshader_in_metallic: FloatProperty(name="Metallic", description="", min=0.0, max=1.0, default=0.0, update=MxNode.update_prop)
    nd_surfaceshader_in_roughness: FloatProperty(name="Roughness", description="", min=0.0, max=1.0, default=0.5, update=MxNode.update_prop)
    nd_surfaceshader_in_clearcoat: FloatProperty(name="Clearcoat", description="", min=0.0, max=1.0, default=0.0, update=MxNode.update_prop)
    nd_surfaceshader_in_clearcoatRoughness: FloatProperty(name="ClearcoatRoughness", description="", min=0.0, max=1.0, default=0.01, update=MxNode.update_prop)
    nd_surfaceshader_in_opacity: FloatProperty(name="Opacity", description="", min=0.0, max=1.0, default=1.0, update=MxNode.update_prop)
    nd_surfaceshader_in_opacityThreshold: FloatProperty(name="OpacityThreshold", description="", min=0.0, max=1.0, default=0.0, update=MxNode.update_prop)
    nd_surfaceshader_in_ior: FloatProperty(name="Ior", description="", min=0.0, soft_max=3.0, default=1.5, update=MxNode.update_prop)
    nd_surfaceshader_in_normal: FloatVectorProperty(name="Normal", description="", subtype="XYZ", size=3, default=(0.0, 0.0, 1.0), update=MxNode.update_prop)
    nd_surfaceshader_in_displacement: FloatProperty(name="Displacement", description="", default=0.0, update=MxNode.update_prop)
    nd_surfaceshader_in_occlusion: FloatProperty(name="Occlusion", description="", min=0.0, max=1.0, default=1.0, update=MxNode.update_prop)
    nd_surfaceshader_out_out: StringProperty(name="Out", description="", update=MxNode.update_prop)


class MxNode_USD_UsdUVTexture(MxNode):
    _file_path = FILE_PATH
    _data_types = {'float': {'nd_name': 'ND_UsdUVTexture', 'nd': None}}

    bl_label = 'UsdUVTexture'
    bl_idname = 'usdhydra.MxNode_USD_UsdUVTexture'
    bl_description = ""

    category = 'USD'

    data_type: EnumProperty(name="Type", description="Input Data Type", items=[('float', 'Float', 'Float')], default='float', update=MxNode.update_data_type)

    nd_float_in_file: StringProperty(name="File", description="", subtype="FILE_PATH", update=MxNode.update_prop)
    nd_float_in_st: FloatVectorProperty(name="St", description="", subtype="NONE", size=2, update=MxNode.update_prop)
    nd_float_in_wrapS: EnumProperty(name="WrapS", description="", items=(('black', 'Black', 'Black'), ('clamp', 'Clamp', 'Clamp'), ('periodic', 'Periodic', 'Periodic')), default="periodic", update=MxNode.update_prop)
    nd_float_in_wrapT: EnumProperty(name="WrapT", description="", items=(('black', 'Black', 'Black'), ('clamp', 'Clamp', 'Clamp'), ('periodic', 'Periodic', 'Periodic')), default="periodic", update=MxNode.update_prop)
    nd_float_in_fallback: FloatVectorProperty(name="Fallback", description="", subtype="COLOR", size=4, soft_min=0.0, soft_max=1.0, default=(0.0, 0.0, 0.0, 1.0), update=MxNode.update_prop)
    nd_float_in_scale: FloatVectorProperty(name="Scale", description="", subtype="COLOR", size=4, soft_min=0.0, soft_max=1.0, default=(1.0, 1.0, 1.0, 1.0), update=MxNode.update_prop)
    nd_float_in_bias: FloatVectorProperty(name="Bias", description="", subtype="COLOR", size=4, soft_min=0.0, soft_max=1.0, default=(0.0, 0.0, 0.0, 0.0), update=MxNode.update_prop)
    nd_float_out_r: FloatProperty(name="R", description="", update=MxNode.update_prop)
    nd_float_out_g: FloatProperty(name="G", description="", update=MxNode.update_prop)
    nd_float_out_b: FloatProperty(name="B", description="", update=MxNode.update_prop)
    nd_float_out_a: FloatProperty(name="A", description="", update=MxNode.update_prop)
    nd_float_out_rgb: FloatVectorProperty(name="Rgb", description="", subtype="COLOR", size=3, soft_min=0.0, soft_max=1.0, update=MxNode.update_prop)
    nd_float_out_rgba: FloatVectorProperty(name="Rgba", description="", subtype="COLOR", size=4, soft_min=0.0, soft_max=1.0, update=MxNode.update_prop)


class MxNode_USD_UsdPrimvarReader(MxNode):
    _file_path = FILE_PATH
    _data_types = {'integer': {'nd_name': 'ND_UsdPrimvarReader_integer', 'nd': None}, 'boolean': {'nd_name': 'ND_UsdPrimvarReader_boolean', 'nd': None}, 'string': {'nd_name': 'ND_UsdPrimvarReader_string', 'nd': None}, 'float': {'nd_name': 'ND_UsdPrimvarReader_float', 'nd': None}, 'vector2': {'nd_name': 'ND_UsdPrimvarReader_vector2', 'nd': None}, 'vector3': {'nd_name': 'ND_UsdPrimvarReader_vector3', 'nd': None}, 'vector4': {'nd_name': 'ND_UsdPrimvarReader_vector4', 'nd': None}}

    bl_label = 'UsdPrimvarReader'
    bl_idname = 'usdhydra.MxNode_USD_UsdPrimvarReader'
    bl_description = ""

    category = 'USD'

    data_type: EnumProperty(name="Type", description="Input Data Type", items=[('integer', 'Integer', 'Integer'), ('boolean', 'Boolean', 'Boolean'), ('string', 'String', 'String'), ('float', 'Float', 'Float'), ('vector2', 'Vector2', 'Vector2'), ('vector3', 'Vector3', 'Vector3'), ('vector4', 'Vector4', 'Vector4')], default='integer', update=MxNode.update_data_type)

    nd_integer_in_varname: StringProperty(name="Varname", description="", update=MxNode.update_prop)
    nd_integer_in_fallback: IntProperty(name="Fallback", description="", default=0, update=MxNode.update_prop)
    nd_integer_out_out: IntProperty(name="Out", description="", update=MxNode.update_prop)

    nd_boolean_in_varname: StringProperty(name="Varname", description="", update=MxNode.update_prop)
    nd_boolean_in_fallback: BoolProperty(name="Fallback", description="", default=False, update=MxNode.update_prop)
    nd_boolean_out_out: BoolProperty(name="Out", description="", update=MxNode.update_prop)

    nd_string_in_varname: StringProperty(name="Varname", description="", update=MxNode.update_prop)
    nd_string_in_fallback: StringProperty(name="Fallback", description="", default="", update=MxNode.update_prop)
    nd_string_out_out: StringProperty(name="Out", description="", update=MxNode.update_prop)

    nd_float_in_varname: StringProperty(name="Varname", description="", update=MxNode.update_prop)
    nd_float_in_fallback: FloatProperty(name="Fallback", description="", default=0.0, update=MxNode.update_prop)
    nd_float_out_out: FloatProperty(name="Out", description="", update=MxNode.update_prop)

    nd_vector2_in_varname: StringProperty(name="Varname", description="", update=MxNode.update_prop)
    nd_vector2_in_fallback: FloatVectorProperty(name="Fallback", description="", subtype="NONE", size=2, default=(0.0, 0.0), update=MxNode.update_prop)
    nd_vector2_out_out: FloatVectorProperty(name="Out", description="", subtype="NONE", size=2, update=MxNode.update_prop)

    nd_vector3_in_varname: StringProperty(name="Varname", description="", update=MxNode.update_prop)
    nd_vector3_in_fallback: FloatVectorProperty(name="Fallback", description="", subtype="XYZ", size=3, default=(0.0, 0.0, 0.0), update=MxNode.update_prop)
    nd_vector3_out_out: FloatVectorProperty(name="Out", description="", subtype="XYZ", size=3, update=MxNode.update_prop)

    nd_vector4_in_varname: StringProperty(name="Varname", description="", update=MxNode.update_prop)
    nd_vector4_in_fallback: FloatVectorProperty(name="Fallback", description="", subtype="NONE", size=4, default=(0.0, 0.0, 0.0, 0.0), update=MxNode.update_prop)
    nd_vector4_out_out: FloatVectorProperty(name="Out", description="", subtype="NONE", size=4, update=MxNode.update_prop)


class MxNode_USD_UsdTransform2d(MxNode):
    _file_path = FILE_PATH
    _data_types = {'vector2': {'nd_name': 'ND_UsdTransform2d', 'nd': None}}

    bl_label = 'UsdTransform2d'
    bl_idname = 'usdhydra.MxNode_USD_UsdTransform2d'
    bl_description = ""

    category = 'USD'

    data_type: EnumProperty(name="Type", description="Input Data Type", items=[('vector2', 'Vector2', 'Vector2')], default='vector2', update=MxNode.update_data_type)

    nd_vector2_in_in: FloatVectorProperty(name="In", description="", subtype="NONE", size=2, update=MxNode.update_prop)
    nd_vector2_in_rotation: FloatProperty(name="Rotation", description="", default=0.0, update=MxNode.update_prop)
    nd_vector2_in_scale: FloatVectorProperty(name="Scale", description="", subtype="NONE", size=2, default=(1.0, 1.0), update=MxNode.update_prop)
    nd_vector2_in_translation: FloatVectorProperty(name="Translation", description="", subtype="NONE", size=2, default=(0.0, 0.0), update=MxNode.update_prop)
    nd_vector2_out_out: FloatVectorProperty(name="Out", description="", subtype="NONE", size=2, update=MxNode.update_prop)


mx_node_classes = [MxNode_USD_UsdPreviewSurface, MxNode_USD_UsdUVTexture, MxNode_USD_UsdPrimvarReader, MxNode_USD_UsdTransform2d]
