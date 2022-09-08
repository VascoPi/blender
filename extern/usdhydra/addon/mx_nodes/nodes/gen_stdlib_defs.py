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


FILE_PATH = r"libraries\stdlib\stdlib_defs.mtlx"


class MxNode_STD_surfacematerial(MxNode):
    _file_path = FILE_PATH
    _data_types = {'material': {'nd_name': 'ND_surfacematerial', 'nd': None}}

    bl_label = 'Surfacematerial'
    bl_idname = 'usdhydra.MxNode_STD_surfacematerial'
    bl_description = ""

    category = 'material'

    data_type: EnumProperty(name="Type", description="Input Data Type", items=[('material', 'Material', 'Material')], default='material', update=MxNode.update_data_type)

    nd_material_in_surfaceshader: StringProperty(name="Surfaceshader", description="", default="", update=MxNode.update_prop)
    nd_material_in_displacementshader: StringProperty(name="Displacementshader", description="", default="", update=MxNode.update_prop)
    nd_material_out_out: StringProperty(name="Out", description="", update=MxNode.update_prop)


class MxNode_STD_volumematerial(MxNode):
    _file_path = FILE_PATH
    _data_types = {'material': {'nd_name': 'ND_volumematerial', 'nd': None}}

    bl_label = 'Volumematerial'
    bl_idname = 'usdhydra.MxNode_STD_volumematerial'
    bl_description = ""

    category = 'material'

    data_type: EnumProperty(name="Type", description="Input Data Type", items=[('material', 'Material', 'Material')], default='material', update=MxNode.update_data_type)

    nd_material_in_volumeshader: StringProperty(name="Volumeshader", description="", default="", update=MxNode.update_prop)
    nd_material_out_out: StringProperty(name="Out", description="", update=MxNode.update_prop)


class MxNode_STD_surface_unlit(MxNode):
    _file_path = FILE_PATH
    _data_types = {'surfaceshader': {'nd_name': 'ND_surface_unlit', 'nd': None}}

    bl_label = 'Surface unlit'
    bl_idname = 'usdhydra.MxNode_STD_surface_unlit'
    bl_description = "Construct a surface shader from emission and transmission values."

    category = 'shader'

    data_type: EnumProperty(name="Type", description="Input Data Type", items=[('surfaceshader', 'Surfaceshader', 'Surfaceshader')], default='surfaceshader', update=MxNode.update_data_type)

    nd_surfaceshader_in_emission: FloatProperty(name="Emission", description="Surface emission amount.", default=1.0, update=MxNode.update_prop)
    nd_surfaceshader_in_emission_color: FloatVectorProperty(name="Emission color", description="Surface emission color.", subtype="COLOR", size=3, soft_min=0.0, soft_max=1.0, default=(1.0, 1.0, 1.0), update=MxNode.update_prop)
    nd_surfaceshader_in_transmission: FloatProperty(name="Transmission", description="Surface transmission amount.", default=0.0, update=MxNode.update_prop)
    nd_surfaceshader_in_transmission_color: FloatVectorProperty(name="Transmission color", description="Surface transmission color.", subtype="COLOR", size=3, soft_min=0.0, soft_max=1.0, default=(1.0, 1.0, 1.0), update=MxNode.update_prop)
    nd_surfaceshader_in_opacity: FloatProperty(name="Opacity", description="Surface cutout opacity.", default=1.0, update=MxNode.update_prop)
    nd_surfaceshader_out_out: StringProperty(name="Out", description="", update=MxNode.update_prop)


class MxNode_STD_image(MxNode):
    _file_path = FILE_PATH
    _data_types = {'float': {'nd_name': 'ND_image_float', 'nd': None}, 'color3': {'nd_name': 'ND_image_color3', 'nd': None}, 'color4': {'nd_name': 'ND_image_color4', 'nd': None}, 'vector2': {'nd_name': 'ND_image_vector2', 'nd': None}, 'vector3': {'nd_name': 'ND_image_vector3', 'nd': None}, 'vector4': {'nd_name': 'ND_image_vector4', 'nd': None}}

    bl_label = 'Image'
    bl_idname = 'usdhydra.MxNode_STD_image'
    bl_description = ""

    category = 'texture2d'

    bl_width_default = 250

    data_type: EnumProperty(name="Type", description="Input Data Type", items=[('float', 'Float', 'Float'), ('color3', 'Color3', 'Color3'), ('color4', 'Color4', 'Color4'), ('vector2', 'Vector2', 'Vector2'), ('vector3', 'Vector3', 'Vector3'), ('vector4', 'Vector4', 'Vector4')], default='color3', update=MxNode.update_data_type)

    nd_float_in_file: PointerProperty(type=bpy.types.Image, name="Filename", description="", update=MxNode.update_prop)
    nd_float_in_layer: StringProperty(name="Layer", description="", default="", update=MxNode.update_prop)
    nd_float_in_default: FloatProperty(name="Default Color", description="", default=0.0, update=MxNode.update_prop)
    nd_float_in_texcoord: FloatVectorProperty(name="Texture Coordinates", description="", subtype="NONE", size=2, update=MxNode.update_prop)
    nd_float_in_uaddressmode: EnumProperty(name="Address Mode U", description="", items=(('constant', 'Constant', 'Constant'), ('clamp', 'Clamp', 'Clamp'), ('periodic', 'Periodic', 'Periodic'), ('mirror', 'Mirror', 'Mirror')), default="periodic", update=MxNode.update_prop)
    nd_float_in_vaddressmode: EnumProperty(name="Address Mode V", description="", items=(('constant', 'Constant', 'Constant'), ('clamp', 'Clamp', 'Clamp'), ('periodic', 'Periodic', 'Periodic'), ('mirror', 'Mirror', 'Mirror')), default="periodic", update=MxNode.update_prop)
    nd_float_in_filtertype: EnumProperty(name="Filter Type", description="", items=(('closest', 'Closest', 'Closest'), ('linear', 'Linear', 'Linear'), ('cubic', 'Cubic', 'Cubic')), default="linear", update=MxNode.update_prop)
    nd_float_in_framerange: StringProperty(name="Frame Range", description="", default="", update=MxNode.update_prop)
    nd_float_in_frameoffset: IntProperty(name="Frame Offset", description="", default=0, update=MxNode.update_prop)
    nd_float_in_frameendaction: EnumProperty(name="Frame End Action", description="", items=(('constant', 'Constant', 'Constant'), ('clamp', 'Clamp', 'Clamp'), ('periodic', 'Periodic', 'Periodic'), ('mirror', 'Mirror', 'Mirror')), default="constant", update=MxNode.update_prop)
    nd_float_out_out: FloatProperty(name="Out", description="", update=MxNode.update_prop)

    nd_color3_in_file: PointerProperty(type=bpy.types.Image, name="Filename", description="", update=MxNode.update_prop)
    nd_color3_in_layer: StringProperty(name="Layer", description="", default="", update=MxNode.update_prop)
    nd_color3_in_default: FloatVectorProperty(name="Default Color", description="", subtype="COLOR", size=3, soft_min=0.0, soft_max=1.0, default=(0.0, 0.0, 0.0), update=MxNode.update_prop)
    nd_color3_in_texcoord: FloatVectorProperty(name="Texture Coordinates", description="", subtype="NONE", size=2, update=MxNode.update_prop)
    nd_color3_in_uaddressmode: EnumProperty(name="Address Mode U", description="", items=(('constant', 'Constant', 'Constant'), ('clamp', 'Clamp', 'Clamp'), ('periodic', 'Periodic', 'Periodic'), ('mirror', 'Mirror', 'Mirror')), default="periodic", update=MxNode.update_prop)
    nd_color3_in_vaddressmode: EnumProperty(name="Address Mode V", description="", items=(('constant', 'Constant', 'Constant'), ('clamp', 'Clamp', 'Clamp'), ('periodic', 'Periodic', 'Periodic'), ('mirror', 'Mirror', 'Mirror')), default="periodic", update=MxNode.update_prop)
    nd_color3_in_filtertype: EnumProperty(name="Filter Type", description="", items=(('closest', 'Closest', 'Closest'), ('linear', 'Linear', 'Linear'), ('cubic', 'Cubic', 'Cubic')), default="linear", update=MxNode.update_prop)
    nd_color3_in_framerange: StringProperty(name="Frame Range", description="", default="", update=MxNode.update_prop)
    nd_color3_in_frameoffset: IntProperty(name="Frame Offset", description="", default=0, update=MxNode.update_prop)
    nd_color3_in_frameendaction: EnumProperty(name="Frame End Action", description="", items=(('constant', 'Constant', 'Constant'), ('clamp', 'Clamp', 'Clamp'), ('periodic', 'Periodic', 'Periodic'), ('mirror', 'Mirror', 'Mirror')), default="constant", update=MxNode.update_prop)
    nd_color3_out_out: FloatVectorProperty(name="Out", description="", subtype="COLOR", size=3, soft_min=0.0, soft_max=1.0, update=MxNode.update_prop)

    nd_color4_in_file: PointerProperty(type=bpy.types.Image, name="Filename", description="", update=MxNode.update_prop)
    nd_color4_in_layer: StringProperty(name="Layer", description="", default="", update=MxNode.update_prop)
    nd_color4_in_default: FloatVectorProperty(name="Default Color", description="", subtype="COLOR", size=4, soft_min=0.0, soft_max=1.0, default=(0.0, 0.0, 0.0, 0.0), update=MxNode.update_prop)
    nd_color4_in_texcoord: FloatVectorProperty(name="Texture Coordinates", description="", subtype="NONE", size=2, update=MxNode.update_prop)
    nd_color4_in_uaddressmode: EnumProperty(name="Address Mode U", description="", items=(('constant', 'Constant', 'Constant'), ('clamp', 'Clamp', 'Clamp'), ('periodic', 'Periodic', 'Periodic'), ('mirror', 'Mirror', 'Mirror')), default="periodic", update=MxNode.update_prop)
    nd_color4_in_vaddressmode: EnumProperty(name="Address Mode V", description="", items=(('constant', 'Constant', 'Constant'), ('clamp', 'Clamp', 'Clamp'), ('periodic', 'Periodic', 'Periodic'), ('mirror', 'Mirror', 'Mirror')), default="periodic", update=MxNode.update_prop)
    nd_color4_in_filtertype: EnumProperty(name="Filter Type", description="", items=(('closest', 'Closest', 'Closest'), ('linear', 'Linear', 'Linear'), ('cubic', 'Cubic', 'Cubic')), default="linear", update=MxNode.update_prop)
    nd_color4_in_framerange: StringProperty(name="Frame Range", description="", default="", update=MxNode.update_prop)
    nd_color4_in_frameoffset: IntProperty(name="Frame Offset", description="", default=0, update=MxNode.update_prop)
    nd_color4_in_frameendaction: EnumProperty(name="Frame End Action", description="", items=(('constant', 'Constant', 'Constant'), ('clamp', 'Clamp', 'Clamp'), ('periodic', 'Periodic', 'Periodic'), ('mirror', 'Mirror', 'Mirror')), default="constant", update=MxNode.update_prop)
    nd_color4_out_out: FloatVectorProperty(name="Out", description="", subtype="COLOR", size=4, soft_min=0.0, soft_max=1.0, update=MxNode.update_prop)

    nd_vector2_in_file: PointerProperty(type=bpy.types.Image, name="Filename", description="", update=MxNode.update_prop)
    nd_vector2_in_layer: StringProperty(name="Layer", description="", default="", update=MxNode.update_prop)
    nd_vector2_in_default: FloatVectorProperty(name="Default Color", description="", subtype="NONE", size=2, default=(0.0, 0.0), update=MxNode.update_prop)
    nd_vector2_in_texcoord: FloatVectorProperty(name="Texture Coordinates", description="", subtype="NONE", size=2, update=MxNode.update_prop)
    nd_vector2_in_uaddressmode: EnumProperty(name="Address Mode U", description="", items=(('constant', 'Constant', 'Constant'), ('clamp', 'Clamp', 'Clamp'), ('periodic', 'Periodic', 'Periodic'), ('mirror', 'Mirror', 'Mirror')), default="periodic", update=MxNode.update_prop)
    nd_vector2_in_vaddressmode: EnumProperty(name="Address Mode V", description="", items=(('constant', 'Constant', 'Constant'), ('clamp', 'Clamp', 'Clamp'), ('periodic', 'Periodic', 'Periodic'), ('mirror', 'Mirror', 'Mirror')), default="periodic", update=MxNode.update_prop)
    nd_vector2_in_filtertype: EnumProperty(name="Filter Type", description="", items=(('closest', 'Closest', 'Closest'), ('linear', 'Linear', 'Linear'), ('cubic', 'Cubic', 'Cubic')), default="linear", update=MxNode.update_prop)
    nd_vector2_in_framerange: StringProperty(name="Frame Range", description="", default="", update=MxNode.update_prop)
    nd_vector2_in_frameoffset: IntProperty(name="Frame Offset", description="", default=0, update=MxNode.update_prop)
    nd_vector2_in_frameendaction: EnumProperty(name="Frame End Action", description="", items=(('constant', 'Constant', 'Constant'), ('clamp', 'Clamp', 'Clamp'), ('periodic', 'Periodic', 'Periodic'), ('mirror', 'Mirror', 'Mirror')), default="constant", update=MxNode.update_prop)
    nd_vector2_out_out: FloatVectorProperty(name="Out", description="", subtype="NONE", size=2, update=MxNode.update_prop)

    nd_vector3_in_file: PointerProperty(type=bpy.types.Image, name="Filename", description="", update=MxNode.update_prop)
    nd_vector3_in_layer: StringProperty(name="Layer", description="", default="", update=MxNode.update_prop)
    nd_vector3_in_default: FloatVectorProperty(name="Default Color", description="", subtype="XYZ", size=3, default=(0.0, 0.0, 0.0), update=MxNode.update_prop)
    nd_vector3_in_texcoord: FloatVectorProperty(name="Texture Coordinates", description="", subtype="NONE", size=2, update=MxNode.update_prop)
    nd_vector3_in_uaddressmode: EnumProperty(name="Address Mode U", description="", items=(('constant', 'Constant', 'Constant'), ('clamp', 'Clamp', 'Clamp'), ('periodic', 'Periodic', 'Periodic'), ('mirror', 'Mirror', 'Mirror')), default="periodic", update=MxNode.update_prop)
    nd_vector3_in_vaddressmode: EnumProperty(name="Address Mode V", description="", items=(('constant', 'Constant', 'Constant'), ('clamp', 'Clamp', 'Clamp'), ('periodic', 'Periodic', 'Periodic'), ('mirror', 'Mirror', 'Mirror')), default="periodic", update=MxNode.update_prop)
    nd_vector3_in_filtertype: EnumProperty(name="Filter Type", description="", items=(('closest', 'Closest', 'Closest'), ('linear', 'Linear', 'Linear'), ('cubic', 'Cubic', 'Cubic')), default="linear", update=MxNode.update_prop)
    nd_vector3_in_framerange: StringProperty(name="Frame Range", description="", default="", update=MxNode.update_prop)
    nd_vector3_in_frameoffset: IntProperty(name="Frame Offset", description="", default=0, update=MxNode.update_prop)
    nd_vector3_in_frameendaction: EnumProperty(name="Frame End Action", description="", items=(('constant', 'Constant', 'Constant'), ('clamp', 'Clamp', 'Clamp'), ('periodic', 'Periodic', 'Periodic'), ('mirror', 'Mirror', 'Mirror')), default="constant", update=MxNode.update_prop)
    nd_vector3_out_out: FloatVectorProperty(name="Out", description="", subtype="XYZ", size=3, update=MxNode.update_prop)

    nd_vector4_in_file: PointerProperty(type=bpy.types.Image, name="Filename", description="", update=MxNode.update_prop)
    nd_vector4_in_layer: StringProperty(name="Layer", description="", default="", update=MxNode.update_prop)
    nd_vector4_in_default: FloatVectorProperty(name="Default Color", description="", subtype="NONE", size=4, default=(0.0, 0.0, 0.0, 0.0), update=MxNode.update_prop)
    nd_vector4_in_texcoord: FloatVectorProperty(name="Texture Coordinates", description="", subtype="NONE", size=2, update=MxNode.update_prop)
    nd_vector4_in_uaddressmode: EnumProperty(name="Address Mode U", description="", items=(('constant', 'Constant', 'Constant'), ('clamp', 'Clamp', 'Clamp'), ('periodic', 'Periodic', 'Periodic'), ('mirror', 'Mirror', 'Mirror')), default="periodic", update=MxNode.update_prop)
    nd_vector4_in_vaddressmode: EnumProperty(name="Address Mode V", description="", items=(('constant', 'Constant', 'Constant'), ('clamp', 'Clamp', 'Clamp'), ('periodic', 'Periodic', 'Periodic'), ('mirror', 'Mirror', 'Mirror')), default="periodic", update=MxNode.update_prop)
    nd_vector4_in_filtertype: EnumProperty(name="Filter Type", description="", items=(('closest', 'Closest', 'Closest'), ('linear', 'Linear', 'Linear'), ('cubic', 'Cubic', 'Cubic')), default="linear", update=MxNode.update_prop)
    nd_vector4_in_framerange: StringProperty(name="Frame Range", description="", default="", update=MxNode.update_prop)
    nd_vector4_in_frameoffset: IntProperty(name="Frame Offset", description="", default=0, update=MxNode.update_prop)
    nd_vector4_in_frameendaction: EnumProperty(name="Frame End Action", description="", items=(('constant', 'Constant', 'Constant'), ('clamp', 'Clamp', 'Clamp'), ('periodic', 'Periodic', 'Periodic'), ('mirror', 'Mirror', 'Mirror')), default="constant", update=MxNode.update_prop)
    nd_vector4_out_out: FloatVectorProperty(name="Out", description="", subtype="NONE", size=4, update=MxNode.update_prop)


class MxNode_STD_tiledimage(MxNode):
    _file_path = FILE_PATH
    _data_types = {'float': {'nd_name': 'ND_tiledimage_float', 'nd': None}, 'color3': {'nd_name': 'ND_tiledimage_color3', 'nd': None}, 'color4': {'nd_name': 'ND_tiledimage_color4', 'nd': None}, 'vector2': {'nd_name': 'ND_tiledimage_vector2', 'nd': None}, 'vector3': {'nd_name': 'ND_tiledimage_vector3', 'nd': None}, 'vector4': {'nd_name': 'ND_tiledimage_vector4', 'nd': None}}

    bl_label = 'Tiledimage'
    bl_idname = 'usdhydra.MxNode_STD_tiledimage'
    bl_description = ""

    category = 'texture2d'

    bl_width_default = 250

    data_type: EnumProperty(name="Type", description="Input Data Type", items=[('float', 'Float', 'Float'), ('color3', 'Color3', 'Color3'), ('color4', 'Color4', 'Color4'), ('vector2', 'Vector2', 'Vector2'), ('vector3', 'Vector3', 'Vector3'), ('vector4', 'Vector4', 'Vector4')], default='color3', update=MxNode.update_data_type)

    nd_float_in_file: PointerProperty(type=bpy.types.Image, name="File", description="", update=MxNode.update_prop)
    nd_float_in_default: FloatProperty(name="Default", description="", default=0.0, update=MxNode.update_prop)
    nd_float_in_texcoord: FloatVectorProperty(name="Texcoord", description="", subtype="NONE", size=2, update=MxNode.update_prop)
    nd_float_in_uvtiling: FloatVectorProperty(name="Uvtiling", description="", subtype="NONE", size=2, default=(1.0, 1.0), update=MxNode.update_prop)
    nd_float_in_uvoffset: FloatVectorProperty(name="Uvoffset", description="", subtype="NONE", size=2, default=(0.0, 0.0), update=MxNode.update_prop)
    nd_float_in_realworldimagesize: FloatVectorProperty(name="Realworldimagesize", description="", subtype="NONE", size=2, default=(1.0, 1.0), update=MxNode.update_prop)
    nd_float_in_realworldtilesize: FloatVectorProperty(name="Realworldtilesize", description="", subtype="NONE", size=2, default=(1.0, 1.0), update=MxNode.update_prop)
    nd_float_in_filtertype: EnumProperty(name="Filtertype", description="", items=(('closest', 'Closest', 'Closest'), ('linear', 'Linear', 'Linear'), ('cubic', 'Cubic', 'Cubic')), default="linear", update=MxNode.update_prop)
    nd_float_in_framerange: StringProperty(name="Framerange", description="", default="", update=MxNode.update_prop)
    nd_float_in_frameoffset: IntProperty(name="Frameoffset", description="", default=0, update=MxNode.update_prop)
    nd_float_in_frameendaction: EnumProperty(name="Frameendaction", description="", items=(('constant', 'Constant', 'Constant'), ('clamp', 'Clamp', 'Clamp'), ('periodic', 'Periodic', 'Periodic'), ('mirror', 'Mirror', 'Mirror')), default="constant", update=MxNode.update_prop)
    nd_float_out_out: FloatProperty(name="Out", description="", update=MxNode.update_prop)

    nd_color3_in_file: PointerProperty(type=bpy.types.Image, name="File", description="", update=MxNode.update_prop)
    nd_color3_in_default: FloatVectorProperty(name="Default", description="", subtype="COLOR", size=3, soft_min=0.0, soft_max=1.0, default=(0.0, 0.0, 0.0), update=MxNode.update_prop)
    nd_color3_in_texcoord: FloatVectorProperty(name="Texcoord", description="", subtype="NONE", size=2, update=MxNode.update_prop)
    nd_color3_in_uvtiling: FloatVectorProperty(name="Uvtiling", description="", subtype="NONE", size=2, default=(1.0, 1.0), update=MxNode.update_prop)
    nd_color3_in_uvoffset: FloatVectorProperty(name="Uvoffset", description="", subtype="NONE", size=2, default=(0.0, 0.0), update=MxNode.update_prop)
    nd_color3_in_realworldimagesize: FloatVectorProperty(name="Realworldimagesize", description="", subtype="NONE", size=2, default=(1.0, 1.0), update=MxNode.update_prop)
    nd_color3_in_realworldtilesize: FloatVectorProperty(name="Realworldtilesize", description="", subtype="NONE", size=2, default=(1.0, 1.0), update=MxNode.update_prop)
    nd_color3_in_filtertype: EnumProperty(name="Filtertype", description="", items=(('closest', 'Closest', 'Closest'), ('linear', 'Linear', 'Linear'), ('cubic', 'Cubic', 'Cubic')), default="linear", update=MxNode.update_prop)
    nd_color3_in_framerange: StringProperty(name="Framerange", description="", default="", update=MxNode.update_prop)
    nd_color3_in_frameoffset: IntProperty(name="Frameoffset", description="", default=0, update=MxNode.update_prop)
    nd_color3_in_frameendaction: EnumProperty(name="Frameendaction", description="", items=(('constant', 'Constant', 'Constant'), ('clamp', 'Clamp', 'Clamp'), ('periodic', 'Periodic', 'Periodic'), ('mirror', 'Mirror', 'Mirror')), default="constant", update=MxNode.update_prop)
    nd_color3_out_out: FloatVectorProperty(name="Out", description="", subtype="COLOR", size=3, soft_min=0.0, soft_max=1.0, update=MxNode.update_prop)

    nd_color4_in_file: PointerProperty(type=bpy.types.Image, name="File", description="", update=MxNode.update_prop)
    nd_color4_in_default: FloatVectorProperty(name="Default", description="", subtype="COLOR", size=4, soft_min=0.0, soft_max=1.0, default=(0.0, 0.0, 0.0, 0.0), update=MxNode.update_prop)
    nd_color4_in_texcoord: FloatVectorProperty(name="Texcoord", description="", subtype="NONE", size=2, update=MxNode.update_prop)
    nd_color4_in_uvtiling: FloatVectorProperty(name="Uvtiling", description="", subtype="NONE", size=2, default=(1.0, 1.0), update=MxNode.update_prop)
    nd_color4_in_uvoffset: FloatVectorProperty(name="Uvoffset", description="", subtype="NONE", size=2, default=(0.0, 0.0), update=MxNode.update_prop)
    nd_color4_in_realworldimagesize: FloatVectorProperty(name="Realworldimagesize", description="", subtype="NONE", size=2, default=(1.0, 1.0), update=MxNode.update_prop)
    nd_color4_in_realworldtilesize: FloatVectorProperty(name="Realworldtilesize", description="", subtype="NONE", size=2, default=(1.0, 1.0), update=MxNode.update_prop)
    nd_color4_in_filtertype: EnumProperty(name="Filtertype", description="", items=(('closest', 'Closest', 'Closest'), ('linear', 'Linear', 'Linear'), ('cubic', 'Cubic', 'Cubic')), default="linear", update=MxNode.update_prop)
    nd_color4_in_framerange: StringProperty(name="Framerange", description="", default="", update=MxNode.update_prop)
    nd_color4_in_frameoffset: IntProperty(name="Frameoffset", description="", default=0, update=MxNode.update_prop)
    nd_color4_in_frameendaction: EnumProperty(name="Frameendaction", description="", items=(('constant', 'Constant', 'Constant'), ('clamp', 'Clamp', 'Clamp'), ('periodic', 'Periodic', 'Periodic'), ('mirror', 'Mirror', 'Mirror')), default="constant", update=MxNode.update_prop)
    nd_color4_out_out: FloatVectorProperty(name="Out", description="", subtype="COLOR", size=4, soft_min=0.0, soft_max=1.0, update=MxNode.update_prop)

    nd_vector2_in_file: PointerProperty(type=bpy.types.Image, name="File", description="", update=MxNode.update_prop)
    nd_vector2_in_default: FloatVectorProperty(name="Default", description="", subtype="NONE", size=2, default=(0.0, 0.0), update=MxNode.update_prop)
    nd_vector2_in_texcoord: FloatVectorProperty(name="Texcoord", description="", subtype="NONE", size=2, update=MxNode.update_prop)
    nd_vector2_in_uvtiling: FloatVectorProperty(name="Uvtiling", description="", subtype="NONE", size=2, default=(1.0, 1.0), update=MxNode.update_prop)
    nd_vector2_in_uvoffset: FloatVectorProperty(name="Uvoffset", description="", subtype="NONE", size=2, default=(0.0, 0.0), update=MxNode.update_prop)
    nd_vector2_in_realworldimagesize: FloatVectorProperty(name="Realworldimagesize", description="", subtype="NONE", size=2, default=(1.0, 1.0), update=MxNode.update_prop)
    nd_vector2_in_realworldtilesize: FloatVectorProperty(name="Realworldtilesize", description="", subtype="NONE", size=2, default=(1.0, 1.0), update=MxNode.update_prop)
    nd_vector2_in_filtertype: EnumProperty(name="Filtertype", description="", items=(('closest', 'Closest', 'Closest'), ('linear', 'Linear', 'Linear'), ('cubic', 'Cubic', 'Cubic')), default="linear", update=MxNode.update_prop)
    nd_vector2_in_framerange: StringProperty(name="Framerange", description="", default="", update=MxNode.update_prop)
    nd_vector2_in_frameoffset: IntProperty(name="Frameoffset", description="", default=0, update=MxNode.update_prop)
    nd_vector2_in_frameendaction: EnumProperty(name="Frameendaction", description="", items=(('constant', 'Constant', 'Constant'), ('clamp', 'Clamp', 'Clamp'), ('periodic', 'Periodic', 'Periodic'), ('mirror', 'Mirror', 'Mirror')), default="constant", update=MxNode.update_prop)
    nd_vector2_out_out: FloatVectorProperty(name="Out", description="", subtype="NONE", size=2, update=MxNode.update_prop)

    nd_vector3_in_file: PointerProperty(type=bpy.types.Image, name="File", description="", update=MxNode.update_prop)
    nd_vector3_in_default: FloatVectorProperty(name="Default", description="", subtype="XYZ", size=3, default=(0.0, 0.0, 0.0), update=MxNode.update_prop)
    nd_vector3_in_texcoord: FloatVectorProperty(name="Texcoord", description="", subtype="NONE", size=2, update=MxNode.update_prop)
    nd_vector3_in_uvtiling: FloatVectorProperty(name="Uvtiling", description="", subtype="NONE", size=2, default=(1.0, 1.0), update=MxNode.update_prop)
    nd_vector3_in_uvoffset: FloatVectorProperty(name="Uvoffset", description="", subtype="NONE", size=2, default=(0.0, 0.0), update=MxNode.update_prop)
    nd_vector3_in_realworldimagesize: FloatVectorProperty(name="Realworldimagesize", description="", subtype="NONE", size=2, default=(1.0, 1.0), update=MxNode.update_prop)
    nd_vector3_in_realworldtilesize: FloatVectorProperty(name="Realworldtilesize", description="", subtype="NONE", size=2, default=(1.0, 1.0), update=MxNode.update_prop)
    nd_vector3_in_filtertype: EnumProperty(name="Filtertype", description="", items=(('closest', 'Closest', 'Closest'), ('linear', 'Linear', 'Linear'), ('cubic', 'Cubic', 'Cubic')), default="linear", update=MxNode.update_prop)
    nd_vector3_in_framerange: StringProperty(name="Framerange", description="", default="", update=MxNode.update_prop)
    nd_vector3_in_frameoffset: IntProperty(name="Frameoffset", description="", default=0, update=MxNode.update_prop)
    nd_vector3_in_frameendaction: EnumProperty(name="Frameendaction", description="", items=(('constant', 'Constant', 'Constant'), ('clamp', 'Clamp', 'Clamp'), ('periodic', 'Periodic', 'Periodic'), ('mirror', 'Mirror', 'Mirror')), default="constant", update=MxNode.update_prop)
    nd_vector3_out_out: FloatVectorProperty(name="Out", description="", subtype="XYZ", size=3, update=MxNode.update_prop)

    nd_vector4_in_file: PointerProperty(type=bpy.types.Image, name="File", description="", update=MxNode.update_prop)
    nd_vector4_in_default: FloatVectorProperty(name="Default", description="", subtype="NONE", size=4, default=(0.0, 0.0, 0.0, 0.0), update=MxNode.update_prop)
    nd_vector4_in_texcoord: FloatVectorProperty(name="Texcoord", description="", subtype="NONE", size=2, update=MxNode.update_prop)
    nd_vector4_in_uvtiling: FloatVectorProperty(name="Uvtiling", description="", subtype="NONE", size=2, default=(1.0, 1.0), update=MxNode.update_prop)
    nd_vector4_in_uvoffset: FloatVectorProperty(name="Uvoffset", description="", subtype="NONE", size=2, default=(0.0, 0.0), update=MxNode.update_prop)
    nd_vector4_in_realworldimagesize: FloatVectorProperty(name="Realworldimagesize", description="", subtype="NONE", size=2, default=(1.0, 1.0), update=MxNode.update_prop)
    nd_vector4_in_realworldtilesize: FloatVectorProperty(name="Realworldtilesize", description="", subtype="NONE", size=2, default=(1.0, 1.0), update=MxNode.update_prop)
    nd_vector4_in_filtertype: EnumProperty(name="Filtertype", description="", items=(('closest', 'Closest', 'Closest'), ('linear', 'Linear', 'Linear'), ('cubic', 'Cubic', 'Cubic')), default="linear", update=MxNode.update_prop)
    nd_vector4_in_framerange: StringProperty(name="Framerange", description="", default="", update=MxNode.update_prop)
    nd_vector4_in_frameoffset: IntProperty(name="Frameoffset", description="", default=0, update=MxNode.update_prop)
    nd_vector4_in_frameendaction: EnumProperty(name="Frameendaction", description="", items=(('constant', 'Constant', 'Constant'), ('clamp', 'Clamp', 'Clamp'), ('periodic', 'Periodic', 'Periodic'), ('mirror', 'Mirror', 'Mirror')), default="constant", update=MxNode.update_prop)
    nd_vector4_out_out: FloatVectorProperty(name="Out", description="", subtype="NONE", size=4, update=MxNode.update_prop)


class MxNode_STD_triplanarprojection(MxNode):
    _file_path = FILE_PATH
    _data_types = {'float': {'nd_name': 'ND_triplanarprojection_float', 'nd': None}, 'color3': {'nd_name': 'ND_triplanarprojection_color3', 'nd': None}, 'color4': {'nd_name': 'ND_triplanarprojection_color4', 'nd': None}, 'vector2': {'nd_name': 'ND_triplanarprojection_vector2', 'nd': None}, 'vector3': {'nd_name': 'ND_triplanarprojection_vector3', 'nd': None}, 'vector4': {'nd_name': 'ND_triplanarprojection_vector4', 'nd': None}}

    bl_label = 'Triplanarprojection'
    bl_idname = 'usdhydra.MxNode_STD_triplanarprojection'
    bl_description = ""

    category = 'texture3d'

    bl_width_default = 250

    data_type: EnumProperty(name="Type", description="Input Data Type", items=[('float', 'Float', 'Float'), ('color3', 'Color3', 'Color3'), ('color4', 'Color4', 'Color4'), ('vector2', 'Vector2', 'Vector2'), ('vector3', 'Vector3', 'Vector3'), ('vector4', 'Vector4', 'Vector4')], default='color3', update=MxNode.update_data_type)

    nd_float_in_filex: PointerProperty(type=bpy.types.Image, name="Filex", description="", update=MxNode.update_prop)
    nd_float_in_filey: PointerProperty(type=bpy.types.Image, name="Filey", description="", update=MxNode.update_prop)
    nd_float_in_filez: PointerProperty(type=bpy.types.Image, name="Filez", description="", update=MxNode.update_prop)
    nd_float_in_layerx: StringProperty(name="Layerx", description="", default="", update=MxNode.update_prop)
    nd_float_in_layery: StringProperty(name="Layery", description="", default="", update=MxNode.update_prop)
    nd_float_in_layerz: StringProperty(name="Layerz", description="", default="", update=MxNode.update_prop)
    nd_float_in_default: FloatProperty(name="Default", description="", default=0.0, update=MxNode.update_prop)
    nd_float_in_position: FloatVectorProperty(name="Position", description="", subtype="XYZ", size=3, update=MxNode.update_prop)
    nd_float_in_normal: FloatVectorProperty(name="Normal", description="", subtype="XYZ", size=3, update=MxNode.update_prop)
    nd_float_in_filtertype: EnumProperty(name="Filtertype", description="", items=(('closest', 'Closest', 'Closest'), ('linear', 'Linear', 'Linear'), ('cubic', 'Cubic', 'Cubic')), default="linear", update=MxNode.update_prop)
    nd_float_in_framerange: StringProperty(name="Framerange", description="", default="", update=MxNode.update_prop)
    nd_float_in_frameoffset: IntProperty(name="Frameoffset", description="", default=0, update=MxNode.update_prop)
    nd_float_in_frameendaction: EnumProperty(name="Frameendaction", description="", items=(('constant', 'Constant', 'Constant'), ('clamp', 'Clamp', 'Clamp'), ('periodic', 'Periodic', 'Periodic'), ('mirror', 'Mirror', 'Mirror')), default="constant", update=MxNode.update_prop)
    nd_float_out_out: FloatProperty(name="Out", description="", update=MxNode.update_prop)

    nd_color3_in_filex: PointerProperty(type=bpy.types.Image, name="Filex", description="", update=MxNode.update_prop)
    nd_color3_in_filey: PointerProperty(type=bpy.types.Image, name="Filey", description="", update=MxNode.update_prop)
    nd_color3_in_filez: PointerProperty(type=bpy.types.Image, name="Filez", description="", update=MxNode.update_prop)
    nd_color3_in_layerx: StringProperty(name="Layerx", description="", default="", update=MxNode.update_prop)
    nd_color3_in_layery: StringProperty(name="Layery", description="", default="", update=MxNode.update_prop)
    nd_color3_in_layerz: StringProperty(name="Layerz", description="", default="", update=MxNode.update_prop)
    nd_color3_in_default: FloatVectorProperty(name="Default", description="", subtype="COLOR", size=3, soft_min=0.0, soft_max=1.0, default=(0.0, 0.0, 0.0), update=MxNode.update_prop)
    nd_color3_in_position: FloatVectorProperty(name="Position", description="", subtype="XYZ", size=3, update=MxNode.update_prop)
    nd_color3_in_normal: FloatVectorProperty(name="Normal", description="", subtype="XYZ", size=3, update=MxNode.update_prop)
    nd_color3_in_filtertype: EnumProperty(name="Filtertype", description="", items=(('closest', 'Closest', 'Closest'), ('linear', 'Linear', 'Linear'), ('cubic', 'Cubic', 'Cubic')), default="linear", update=MxNode.update_prop)
    nd_color3_in_framerange: StringProperty(name="Framerange", description="", default="", update=MxNode.update_prop)
    nd_color3_in_frameoffset: IntProperty(name="Frameoffset", description="", default=0, update=MxNode.update_prop)
    nd_color3_in_frameendaction: EnumProperty(name="Frameendaction", description="", items=(('constant', 'Constant', 'Constant'), ('clamp', 'Clamp', 'Clamp'), ('periodic', 'Periodic', 'Periodic'), ('mirror', 'Mirror', 'Mirror')), default="constant", update=MxNode.update_prop)
    nd_color3_out_out: FloatVectorProperty(name="Out", description="", subtype="COLOR", size=3, soft_min=0.0, soft_max=1.0, update=MxNode.update_prop)

    nd_color4_in_filex: PointerProperty(type=bpy.types.Image, name="Filex", description="", update=MxNode.update_prop)
    nd_color4_in_filey: PointerProperty(type=bpy.types.Image, name="Filey", description="", update=MxNode.update_prop)
    nd_color4_in_filez: PointerProperty(type=bpy.types.Image, name="Filez", description="", update=MxNode.update_prop)
    nd_color4_in_layerx: StringProperty(name="Layerx", description="", default="", update=MxNode.update_prop)
    nd_color4_in_layery: StringProperty(name="Layery", description="", default="", update=MxNode.update_prop)
    nd_color4_in_layerz: StringProperty(name="Layerz", description="", default="", update=MxNode.update_prop)
    nd_color4_in_default: FloatVectorProperty(name="Default", description="", subtype="COLOR", size=4, soft_min=0.0, soft_max=1.0, default=(0.0, 0.0, 0.0, 0.0), update=MxNode.update_prop)
    nd_color4_in_position: FloatVectorProperty(name="Position", description="", subtype="XYZ", size=3, update=MxNode.update_prop)
    nd_color4_in_normal: FloatVectorProperty(name="Normal", description="", subtype="XYZ", size=3, update=MxNode.update_prop)
    nd_color4_in_filtertype: EnumProperty(name="Filtertype", description="", items=(('closest', 'Closest', 'Closest'), ('linear', 'Linear', 'Linear'), ('cubic', 'Cubic', 'Cubic')), default="linear", update=MxNode.update_prop)
    nd_color4_in_framerange: StringProperty(name="Framerange", description="", default="", update=MxNode.update_prop)
    nd_color4_in_frameoffset: IntProperty(name="Frameoffset", description="", default=0, update=MxNode.update_prop)
    nd_color4_in_frameendaction: EnumProperty(name="Frameendaction", description="", items=(('constant', 'Constant', 'Constant'), ('clamp', 'Clamp', 'Clamp'), ('periodic', 'Periodic', 'Periodic'), ('mirror', 'Mirror', 'Mirror')), default="constant", update=MxNode.update_prop)
    nd_color4_out_out: FloatVectorProperty(name="Out", description="", subtype="COLOR", size=4, soft_min=0.0, soft_max=1.0, update=MxNode.update_prop)

    nd_vector2_in_filex: PointerProperty(type=bpy.types.Image, name="Filex", description="", update=MxNode.update_prop)
    nd_vector2_in_filey: PointerProperty(type=bpy.types.Image, name="Filey", description="", update=MxNode.update_prop)
    nd_vector2_in_filez: PointerProperty(type=bpy.types.Image, name="Filez", description="", update=MxNode.update_prop)
    nd_vector2_in_layerx: StringProperty(name="Layerx", description="", default="", update=MxNode.update_prop)
    nd_vector2_in_layery: StringProperty(name="Layery", description="", default="", update=MxNode.update_prop)
    nd_vector2_in_layerz: StringProperty(name="Layerz", description="", default="", update=MxNode.update_prop)
    nd_vector2_in_default: FloatVectorProperty(name="Default", description="", subtype="NONE", size=2, default=(0.0, 0.0), update=MxNode.update_prop)
    nd_vector2_in_position: FloatVectorProperty(name="Position", description="", subtype="XYZ", size=3, update=MxNode.update_prop)
    nd_vector2_in_normal: FloatVectorProperty(name="Normal", description="", subtype="XYZ", size=3, update=MxNode.update_prop)
    nd_vector2_in_filtertype: EnumProperty(name="Filtertype", description="", items=(('closest', 'Closest', 'Closest'), ('linear', 'Linear', 'Linear'), ('cubic', 'Cubic', 'Cubic')), default="linear", update=MxNode.update_prop)
    nd_vector2_in_framerange: StringProperty(name="Framerange", description="", default="", update=MxNode.update_prop)
    nd_vector2_in_frameoffset: IntProperty(name="Frameoffset", description="", default=0, update=MxNode.update_prop)
    nd_vector2_in_frameendaction: EnumProperty(name="Frameendaction", description="", items=(('constant', 'Constant', 'Constant'), ('clamp', 'Clamp', 'Clamp'), ('periodic', 'Periodic', 'Periodic'), ('mirror', 'Mirror', 'Mirror')), default="constant", update=MxNode.update_prop)
    nd_vector2_out_out: FloatVectorProperty(name="Out", description="", subtype="NONE", size=2, update=MxNode.update_prop)

    nd_vector3_in_filex: PointerProperty(type=bpy.types.Image, name="Filex", description="", update=MxNode.update_prop)
    nd_vector3_in_filey: PointerProperty(type=bpy.types.Image, name="Filey", description="", update=MxNode.update_prop)
    nd_vector3_in_filez: PointerProperty(type=bpy.types.Image, name="Filez", description="", update=MxNode.update_prop)
    nd_vector3_in_layerx: StringProperty(name="Layerx", description="", default="", update=MxNode.update_prop)
    nd_vector3_in_layery: StringProperty(name="Layery", description="", default="", update=MxNode.update_prop)
    nd_vector3_in_layerz: StringProperty(name="Layerz", description="", default="", update=MxNode.update_prop)
    nd_vector3_in_default: FloatVectorProperty(name="Default", description="", subtype="XYZ", size=3, default=(0.0, 0.0, 0.0), update=MxNode.update_prop)
    nd_vector3_in_position: FloatVectorProperty(name="Position", description="", subtype="XYZ", size=3, update=MxNode.update_prop)
    nd_vector3_in_normal: FloatVectorProperty(name="Normal", description="", subtype="XYZ", size=3, update=MxNode.update_prop)
    nd_vector3_in_filtertype: EnumProperty(name="Filtertype", description="", items=(('closest', 'Closest', 'Closest'), ('linear', 'Linear', 'Linear'), ('cubic', 'Cubic', 'Cubic')), default="linear", update=MxNode.update_prop)
    nd_vector3_in_framerange: StringProperty(name="Framerange", description="", default="", update=MxNode.update_prop)
    nd_vector3_in_frameoffset: IntProperty(name="Frameoffset", description="", default=0, update=MxNode.update_prop)
    nd_vector3_in_frameendaction: EnumProperty(name="Frameendaction", description="", items=(('constant', 'Constant', 'Constant'), ('clamp', 'Clamp', 'Clamp'), ('periodic', 'Periodic', 'Periodic'), ('mirror', 'Mirror', 'Mirror')), default="constant", update=MxNode.update_prop)
    nd_vector3_out_out: FloatVectorProperty(name="Out", description="", subtype="XYZ", size=3, update=MxNode.update_prop)

    nd_vector4_in_filex: PointerProperty(type=bpy.types.Image, name="Filex", description="", update=MxNode.update_prop)
    nd_vector4_in_filey: PointerProperty(type=bpy.types.Image, name="Filey", description="", update=MxNode.update_prop)
    nd_vector4_in_filez: PointerProperty(type=bpy.types.Image, name="Filez", description="", update=MxNode.update_prop)
    nd_vector4_in_layerx: StringProperty(name="Layerx", description="", default="", update=MxNode.update_prop)
    nd_vector4_in_layery: StringProperty(name="Layery", description="", default="", update=MxNode.update_prop)
    nd_vector4_in_layerz: StringProperty(name="Layerz", description="", default="", update=MxNode.update_prop)
    nd_vector4_in_default: FloatVectorProperty(name="Default", description="", subtype="NONE", size=4, default=(0.0, 0.0, 0.0, 0.0), update=MxNode.update_prop)
    nd_vector4_in_position: FloatVectorProperty(name="Position", description="", subtype="XYZ", size=3, update=MxNode.update_prop)
    nd_vector4_in_normal: FloatVectorProperty(name="Normal", description="", subtype="XYZ", size=3, update=MxNode.update_prop)
    nd_vector4_in_filtertype: EnumProperty(name="Filtertype", description="", items=(('closest', 'Closest', 'Closest'), ('linear', 'Linear', 'Linear'), ('cubic', 'Cubic', 'Cubic')), default="linear", update=MxNode.update_prop)
    nd_vector4_in_framerange: StringProperty(name="Framerange", description="", default="", update=MxNode.update_prop)
    nd_vector4_in_frameoffset: IntProperty(name="Frameoffset", description="", default=0, update=MxNode.update_prop)
    nd_vector4_in_frameendaction: EnumProperty(name="Frameendaction", description="", items=(('constant', 'Constant', 'Constant'), ('clamp', 'Clamp', 'Clamp'), ('periodic', 'Periodic', 'Periodic'), ('mirror', 'Mirror', 'Mirror')), default="constant", update=MxNode.update_prop)
    nd_vector4_out_out: FloatVectorProperty(name="Out", description="", subtype="NONE", size=4, update=MxNode.update_prop)


class MxNode_STD_constant(MxNode):
    _file_path = FILE_PATH
    _data_types = {'float': {'nd_name': 'ND_constant_float', 'nd': None}, 'color3': {'nd_name': 'ND_constant_color3', 'nd': None}, 'color4': {'nd_name': 'ND_constant_color4', 'nd': None}, 'vector2': {'nd_name': 'ND_constant_vector2', 'nd': None}, 'vector3': {'nd_name': 'ND_constant_vector3', 'nd': None}, 'vector4': {'nd_name': 'ND_constant_vector4', 'nd': None}, 'boolean': {'nd_name': 'ND_constant_boolean', 'nd': None}, 'integer': {'nd_name': 'ND_constant_integer', 'nd': None}, 'string': {'nd_name': 'ND_constant_string', 'nd': None}, 'filename': {'nd_name': 'ND_constant_filename', 'nd': None}}

    bl_label = 'Constant'
    bl_idname = 'usdhydra.MxNode_STD_constant'
    bl_description = ""

    category = 'procedural'

    data_type: EnumProperty(name="Type", description="Input Data Type", items=[('float', 'Float', 'Float'), ('color3', 'Color3', 'Color3'), ('color4', 'Color4', 'Color4'), ('vector2', 'Vector2', 'Vector2'), ('vector3', 'Vector3', 'Vector3'), ('vector4', 'Vector4', 'Vector4'), ('boolean', 'Boolean', 'Boolean'), ('integer', 'Integer', 'Integer'), ('string', 'String', 'String'), ('filename', 'Filename', 'Filename')], default='color3', update=MxNode.update_data_type)

    nd_float_in_value: FloatProperty(name="Value", description="", default=0.0, update=MxNode.update_prop)
    nd_float_out_out: FloatProperty(name="Out", description="", update=MxNode.update_prop)

    nd_color3_in_value: FloatVectorProperty(name="Value", description="", subtype="COLOR", size=3, soft_min=0.0, soft_max=1.0, default=(0.0, 0.0, 0.0), update=MxNode.update_prop)
    nd_color3_out_out: FloatVectorProperty(name="Out", description="", subtype="COLOR", size=3, soft_min=0.0, soft_max=1.0, update=MxNode.update_prop)

    nd_color4_in_value: FloatVectorProperty(name="Value", description="", subtype="COLOR", size=4, soft_min=0.0, soft_max=1.0, default=(0.0, 0.0, 0.0, 0.0), update=MxNode.update_prop)
    nd_color4_out_out: FloatVectorProperty(name="Out", description="", subtype="COLOR", size=4, soft_min=0.0, soft_max=1.0, update=MxNode.update_prop)

    nd_vector2_in_value: FloatVectorProperty(name="Value", description="", subtype="NONE", size=2, default=(0.0, 0.0), update=MxNode.update_prop)
    nd_vector2_out_out: FloatVectorProperty(name="Out", description="", subtype="NONE", size=2, update=MxNode.update_prop)

    nd_vector3_in_value: FloatVectorProperty(name="Value", description="", subtype="XYZ", size=3, default=(0.0, 0.0, 0.0), update=MxNode.update_prop)
    nd_vector3_out_out: FloatVectorProperty(name="Out", description="", subtype="XYZ", size=3, update=MxNode.update_prop)

    nd_vector4_in_value: FloatVectorProperty(name="Value", description="", subtype="NONE", size=4, default=(0.0, 0.0, 0.0, 0.0), update=MxNode.update_prop)
    nd_vector4_out_out: FloatVectorProperty(name="Out", description="", subtype="NONE", size=4, update=MxNode.update_prop)

    nd_boolean_in_value: BoolProperty(name="Value", description="", default=False, update=MxNode.update_prop)
    nd_boolean_out_out: BoolProperty(name="Out", description="", update=MxNode.update_prop)

    nd_integer_in_value: IntProperty(name="Value", description="", default=0, update=MxNode.update_prop)
    nd_integer_out_out: IntProperty(name="Out", description="", update=MxNode.update_prop)

    nd_string_in_value: StringProperty(name="Value", description="", default="", update=MxNode.update_prop)
    nd_string_out_out: StringProperty(name="Out", description="", update=MxNode.update_prop)

    nd_filename_in_value: StringProperty(name="Value", description="", subtype="FILE_PATH", default="", update=MxNode.update_prop)
    nd_filename_out_out: StringProperty(name="Out", description="", subtype="FILE_PATH", update=MxNode.update_prop)


class MxNode_STD_ramplr(MxNode):
    _file_path = FILE_PATH
    _data_types = {'float': {'nd_name': 'ND_ramplr_float', 'nd': None}, 'color3': {'nd_name': 'ND_ramplr_color3', 'nd': None}, 'color4': {'nd_name': 'ND_ramplr_color4', 'nd': None}, 'vector2': {'nd_name': 'ND_ramplr_vector2', 'nd': None}, 'vector3': {'nd_name': 'ND_ramplr_vector3', 'nd': None}, 'vector4': {'nd_name': 'ND_ramplr_vector4', 'nd': None}}

    bl_label = 'Ramplr'
    bl_idname = 'usdhydra.MxNode_STD_ramplr'
    bl_description = ""

    category = 'procedural2d'

    data_type: EnumProperty(name="Type", description="Input Data Type", items=[('float', 'Float', 'Float'), ('color3', 'Color3', 'Color3'), ('color4', 'Color4', 'Color4'), ('vector2', 'Vector2', 'Vector2'), ('vector3', 'Vector3', 'Vector3'), ('vector4', 'Vector4', 'Vector4')], default='color3', update=MxNode.update_data_type)

    nd_float_in_valuel: FloatProperty(name="Valuel", description="", default=0.0, update=MxNode.update_prop)
    nd_float_in_valuer: FloatProperty(name="Valuer", description="", default=0.0, update=MxNode.update_prop)
    nd_float_in_texcoord: FloatVectorProperty(name="Texcoord", description="", subtype="NONE", size=2, update=MxNode.update_prop)
    nd_float_out_out: FloatProperty(name="Out", description="", update=MxNode.update_prop)

    nd_color3_in_valuel: FloatVectorProperty(name="Valuel", description="", subtype="COLOR", size=3, soft_min=0.0, soft_max=1.0, default=(0.0, 0.0, 0.0), update=MxNode.update_prop)
    nd_color3_in_valuer: FloatVectorProperty(name="Valuer", description="", subtype="COLOR", size=3, soft_min=0.0, soft_max=1.0, default=(0.0, 0.0, 0.0), update=MxNode.update_prop)
    nd_color3_in_texcoord: FloatVectorProperty(name="Texcoord", description="", subtype="NONE", size=2, update=MxNode.update_prop)
    nd_color3_out_out: FloatVectorProperty(name="Out", description="", subtype="COLOR", size=3, soft_min=0.0, soft_max=1.0, update=MxNode.update_prop)

    nd_color4_in_valuel: FloatVectorProperty(name="Valuel", description="", subtype="COLOR", size=4, soft_min=0.0, soft_max=1.0, default=(0.0, 0.0, 0.0, 0.0), update=MxNode.update_prop)
    nd_color4_in_valuer: FloatVectorProperty(name="Valuer", description="", subtype="COLOR", size=4, soft_min=0.0, soft_max=1.0, default=(0.0, 0.0, 0.0, 0.0), update=MxNode.update_prop)
    nd_color4_in_texcoord: FloatVectorProperty(name="Texcoord", description="", subtype="NONE", size=2, update=MxNode.update_prop)
    nd_color4_out_out: FloatVectorProperty(name="Out", description="", subtype="COLOR", size=4, soft_min=0.0, soft_max=1.0, update=MxNode.update_prop)

    nd_vector2_in_valuel: FloatVectorProperty(name="Valuel", description="", subtype="NONE", size=2, default=(0.0, 0.0), update=MxNode.update_prop)
    nd_vector2_in_valuer: FloatVectorProperty(name="Valuer", description="", subtype="NONE", size=2, default=(0.0, 0.0), update=MxNode.update_prop)
    nd_vector2_in_texcoord: FloatVectorProperty(name="Texcoord", description="", subtype="NONE", size=2, update=MxNode.update_prop)
    nd_vector2_out_out: FloatVectorProperty(name="Out", description="", subtype="NONE", size=2, update=MxNode.update_prop)

    nd_vector3_in_valuel: FloatVectorProperty(name="Valuel", description="", subtype="XYZ", size=3, default=(0.0, 0.0, 0.0), update=MxNode.update_prop)
    nd_vector3_in_valuer: FloatVectorProperty(name="Valuer", description="", subtype="XYZ", size=3, default=(0.0, 0.0, 0.0), update=MxNode.update_prop)
    nd_vector3_in_texcoord: FloatVectorProperty(name="Texcoord", description="", subtype="NONE", size=2, update=MxNode.update_prop)
    nd_vector3_out_out: FloatVectorProperty(name="Out", description="", subtype="XYZ", size=3, update=MxNode.update_prop)

    nd_vector4_in_valuel: FloatVectorProperty(name="Valuel", description="", subtype="NONE", size=4, default=(0.0, 0.0, 0.0, 0.0), update=MxNode.update_prop)
    nd_vector4_in_valuer: FloatVectorProperty(name="Valuer", description="", subtype="NONE", size=4, default=(0.0, 0.0, 0.0, 0.0), update=MxNode.update_prop)
    nd_vector4_in_texcoord: FloatVectorProperty(name="Texcoord", description="", subtype="NONE", size=2, update=MxNode.update_prop)
    nd_vector4_out_out: FloatVectorProperty(name="Out", description="", subtype="NONE", size=4, update=MxNode.update_prop)


class MxNode_STD_ramptb(MxNode):
    _file_path = FILE_PATH
    _data_types = {'float': {'nd_name': 'ND_ramptb_float', 'nd': None}, 'color3': {'nd_name': 'ND_ramptb_color3', 'nd': None}, 'color4': {'nd_name': 'ND_ramptb_color4', 'nd': None}, 'vector2': {'nd_name': 'ND_ramptb_vector2', 'nd': None}, 'vector3': {'nd_name': 'ND_ramptb_vector3', 'nd': None}, 'vector4': {'nd_name': 'ND_ramptb_vector4', 'nd': None}}

    bl_label = 'Ramptb'
    bl_idname = 'usdhydra.MxNode_STD_ramptb'
    bl_description = ""

    category = 'procedural2d'

    data_type: EnumProperty(name="Type", description="Input Data Type", items=[('float', 'Float', 'Float'), ('color3', 'Color3', 'Color3'), ('color4', 'Color4', 'Color4'), ('vector2', 'Vector2', 'Vector2'), ('vector3', 'Vector3', 'Vector3'), ('vector4', 'Vector4', 'Vector4')], default='color3', update=MxNode.update_data_type)

    nd_float_in_valuet: FloatProperty(name="Valuet", description="", default=0.0, update=MxNode.update_prop)
    nd_float_in_valueb: FloatProperty(name="Valueb", description="", default=0.0, update=MxNode.update_prop)
    nd_float_in_texcoord: FloatVectorProperty(name="Texcoord", description="", subtype="NONE", size=2, update=MxNode.update_prop)
    nd_float_out_out: FloatProperty(name="Out", description="", update=MxNode.update_prop)

    nd_color3_in_valuet: FloatVectorProperty(name="Valuet", description="", subtype="COLOR", size=3, soft_min=0.0, soft_max=1.0, default=(0.0, 0.0, 0.0), update=MxNode.update_prop)
    nd_color3_in_valueb: FloatVectorProperty(name="Valueb", description="", subtype="COLOR", size=3, soft_min=0.0, soft_max=1.0, default=(0.0, 0.0, 0.0), update=MxNode.update_prop)
    nd_color3_in_texcoord: FloatVectorProperty(name="Texcoord", description="", subtype="NONE", size=2, update=MxNode.update_prop)
    nd_color3_out_out: FloatVectorProperty(name="Out", description="", subtype="COLOR", size=3, soft_min=0.0, soft_max=1.0, update=MxNode.update_prop)

    nd_color4_in_valuet: FloatVectorProperty(name="Valuet", description="", subtype="COLOR", size=4, soft_min=0.0, soft_max=1.0, default=(0.0, 0.0, 0.0, 0.0), update=MxNode.update_prop)
    nd_color4_in_valueb: FloatVectorProperty(name="Valueb", description="", subtype="COLOR", size=4, soft_min=0.0, soft_max=1.0, default=(0.0, 0.0, 0.0, 0.0), update=MxNode.update_prop)
    nd_color4_in_texcoord: FloatVectorProperty(name="Texcoord", description="", subtype="NONE", size=2, update=MxNode.update_prop)
    nd_color4_out_out: FloatVectorProperty(name="Out", description="", subtype="COLOR", size=4, soft_min=0.0, soft_max=1.0, update=MxNode.update_prop)

    nd_vector2_in_valuet: FloatVectorProperty(name="Valuet", description="", subtype="NONE", size=2, default=(0.0, 0.0), update=MxNode.update_prop)
    nd_vector2_in_valueb: FloatVectorProperty(name="Valueb", description="", subtype="NONE", size=2, default=(0.0, 0.0), update=MxNode.update_prop)
    nd_vector2_in_texcoord: FloatVectorProperty(name="Texcoord", description="", subtype="NONE", size=2, update=MxNode.update_prop)
    nd_vector2_out_out: FloatVectorProperty(name="Out", description="", subtype="NONE", size=2, update=MxNode.update_prop)

    nd_vector3_in_valuet: FloatVectorProperty(name="Valuet", description="", subtype="XYZ", size=3, default=(0.0, 0.0, 0.0), update=MxNode.update_prop)
    nd_vector3_in_valueb: FloatVectorProperty(name="Valueb", description="", subtype="XYZ", size=3, default=(0.0, 0.0, 0.0), update=MxNode.update_prop)
    nd_vector3_in_texcoord: FloatVectorProperty(name="Texcoord", description="", subtype="NONE", size=2, update=MxNode.update_prop)
    nd_vector3_out_out: FloatVectorProperty(name="Out", description="", subtype="XYZ", size=3, update=MxNode.update_prop)

    nd_vector4_in_valuet: FloatVectorProperty(name="Valuet", description="", subtype="NONE", size=4, default=(0.0, 0.0, 0.0, 0.0), update=MxNode.update_prop)
    nd_vector4_in_valueb: FloatVectorProperty(name="Valueb", description="", subtype="NONE", size=4, default=(0.0, 0.0, 0.0, 0.0), update=MxNode.update_prop)
    nd_vector4_in_texcoord: FloatVectorProperty(name="Texcoord", description="", subtype="NONE", size=2, update=MxNode.update_prop)
    nd_vector4_out_out: FloatVectorProperty(name="Out", description="", subtype="NONE", size=4, update=MxNode.update_prop)


class MxNode_STD_ramp4(MxNode):
    _file_path = FILE_PATH
    _data_types = {'float': {'nd_name': 'ND_ramp4_float', 'nd': None}, 'color3': {'nd_name': 'ND_ramp4_color3', 'nd': None}, 'color4': {'nd_name': 'ND_ramp4_color4', 'nd': None}, 'vector2': {'nd_name': 'ND_ramp4_vector2', 'nd': None}, 'vector3': {'nd_name': 'ND_ramp4_vector3', 'nd': None}, 'vector4': {'nd_name': 'ND_ramp4_vector4', 'nd': None}}

    bl_label = 'Ramp4'
    bl_idname = 'usdhydra.MxNode_STD_ramp4'
    bl_description = ""

    category = 'procedural2d'

    data_type: EnumProperty(name="Type", description="Input Data Type", items=[('float', 'Float', 'Float'), ('color3', 'Color3', 'Color3'), ('color4', 'Color4', 'Color4'), ('vector2', 'Vector2', 'Vector2'), ('vector3', 'Vector3', 'Vector3'), ('vector4', 'Vector4', 'Vector4')], default='color3', update=MxNode.update_data_type)

    nd_float_in_valuetl: FloatProperty(name="Valuetl", description="", default=0.0, update=MxNode.update_prop)
    nd_float_in_valuetr: FloatProperty(name="Valuetr", description="", default=0.0, update=MxNode.update_prop)
    nd_float_in_valuebl: FloatProperty(name="Valuebl", description="", default=0.0, update=MxNode.update_prop)
    nd_float_in_valuebr: FloatProperty(name="Valuebr", description="", default=0.0, update=MxNode.update_prop)
    nd_float_in_texcoord: FloatVectorProperty(name="Texcoord", description="", subtype="NONE", size=2, update=MxNode.update_prop)
    nd_float_out_out: FloatProperty(name="Out", description="", update=MxNode.update_prop)

    nd_color3_in_valuetl: FloatVectorProperty(name="Valuetl", description="", subtype="COLOR", size=3, soft_min=0.0, soft_max=1.0, default=(0.0, 0.0, 0.0), update=MxNode.update_prop)
    nd_color3_in_valuetr: FloatVectorProperty(name="Valuetr", description="", subtype="COLOR", size=3, soft_min=0.0, soft_max=1.0, default=(0.0, 0.0, 0.0), update=MxNode.update_prop)
    nd_color3_in_valuebl: FloatVectorProperty(name="Valuebl", description="", subtype="COLOR", size=3, soft_min=0.0, soft_max=1.0, default=(0.0, 0.0, 0.0), update=MxNode.update_prop)
    nd_color3_in_valuebr: FloatVectorProperty(name="Valuebr", description="", subtype="COLOR", size=3, soft_min=0.0, soft_max=1.0, default=(0.0, 0.0, 0.0), update=MxNode.update_prop)
    nd_color3_in_texcoord: FloatVectorProperty(name="Texcoord", description="", subtype="NONE", size=2, update=MxNode.update_prop)
    nd_color3_out_out: FloatVectorProperty(name="Out", description="", subtype="COLOR", size=3, soft_min=0.0, soft_max=1.0, update=MxNode.update_prop)

    nd_color4_in_valuetl: FloatVectorProperty(name="Valuetl", description="", subtype="COLOR", size=4, soft_min=0.0, soft_max=1.0, default=(0.0, 0.0, 0.0, 0.0), update=MxNode.update_prop)
    nd_color4_in_valuetr: FloatVectorProperty(name="Valuetr", description="", subtype="COLOR", size=4, soft_min=0.0, soft_max=1.0, default=(0.0, 0.0, 0.0, 0.0), update=MxNode.update_prop)
    nd_color4_in_valuebl: FloatVectorProperty(name="Valuebl", description="", subtype="COLOR", size=4, soft_min=0.0, soft_max=1.0, default=(0.0, 0.0, 0.0, 0.0), update=MxNode.update_prop)
    nd_color4_in_valuebr: FloatVectorProperty(name="Valuebr", description="", subtype="COLOR", size=4, soft_min=0.0, soft_max=1.0, default=(0.0, 0.0, 0.0, 0.0), update=MxNode.update_prop)
    nd_color4_in_texcoord: FloatVectorProperty(name="Texcoord", description="", subtype="NONE", size=2, update=MxNode.update_prop)
    nd_color4_out_out: FloatVectorProperty(name="Out", description="", subtype="COLOR", size=4, soft_min=0.0, soft_max=1.0, update=MxNode.update_prop)

    nd_vector2_in_valuetl: FloatVectorProperty(name="Valuetl", description="", subtype="NONE", size=2, default=(0.0, 0.0), update=MxNode.update_prop)
    nd_vector2_in_valuetr: FloatVectorProperty(name="Valuetr", description="", subtype="NONE", size=2, default=(0.0, 0.0), update=MxNode.update_prop)
    nd_vector2_in_valuebl: FloatVectorProperty(name="Valuebl", description="", subtype="NONE", size=2, default=(0.0, 0.0), update=MxNode.update_prop)
    nd_vector2_in_valuebr: FloatVectorProperty(name="Valuebr", description="", subtype="NONE", size=2, default=(0.0, 0.0), update=MxNode.update_prop)
    nd_vector2_in_texcoord: FloatVectorProperty(name="Texcoord", description="", subtype="NONE", size=2, update=MxNode.update_prop)
    nd_vector2_out_out: FloatVectorProperty(name="Out", description="", subtype="NONE", size=2, update=MxNode.update_prop)

    nd_vector3_in_valuetl: FloatVectorProperty(name="Valuetl", description="", subtype="XYZ", size=3, default=(0.0, 0.0, 0.0), update=MxNode.update_prop)
    nd_vector3_in_valuetr: FloatVectorProperty(name="Valuetr", description="", subtype="XYZ", size=3, default=(0.0, 0.0, 0.0), update=MxNode.update_prop)
    nd_vector3_in_valuebl: FloatVectorProperty(name="Valuebl", description="", subtype="XYZ", size=3, default=(0.0, 0.0, 0.0), update=MxNode.update_prop)
    nd_vector3_in_valuebr: FloatVectorProperty(name="Valuebr", description="", subtype="XYZ", size=3, default=(0.0, 0.0, 0.0), update=MxNode.update_prop)
    nd_vector3_in_texcoord: FloatVectorProperty(name="Texcoord", description="", subtype="NONE", size=2, update=MxNode.update_prop)
    nd_vector3_out_out: FloatVectorProperty(name="Out", description="", subtype="XYZ", size=3, update=MxNode.update_prop)

    nd_vector4_in_valuetl: FloatVectorProperty(name="Valuetl", description="", subtype="NONE", size=4, default=(0.0, 0.0, 0.0, 0.0), update=MxNode.update_prop)
    nd_vector4_in_valuetr: FloatVectorProperty(name="Valuetr", description="", subtype="NONE", size=4, default=(0.0, 0.0, 0.0, 0.0), update=MxNode.update_prop)
    nd_vector4_in_valuebl: FloatVectorProperty(name="Valuebl", description="", subtype="NONE", size=4, default=(0.0, 0.0, 0.0, 0.0), update=MxNode.update_prop)
    nd_vector4_in_valuebr: FloatVectorProperty(name="Valuebr", description="", subtype="NONE", size=4, default=(0.0, 0.0, 0.0, 0.0), update=MxNode.update_prop)
    nd_vector4_in_texcoord: FloatVectorProperty(name="Texcoord", description="", subtype="NONE", size=2, update=MxNode.update_prop)
    nd_vector4_out_out: FloatVectorProperty(name="Out", description="", subtype="NONE", size=4, update=MxNode.update_prop)


class MxNode_STD_splitlr(MxNode):
    _file_path = FILE_PATH
    _data_types = {'float': {'nd_name': 'ND_splitlr_float', 'nd': None}, 'color3': {'nd_name': 'ND_splitlr_color3', 'nd': None}, 'color4': {'nd_name': 'ND_splitlr_color4', 'nd': None}, 'vector2': {'nd_name': 'ND_splitlr_vector2', 'nd': None}, 'vector3': {'nd_name': 'ND_splitlr_vector3', 'nd': None}, 'vector4': {'nd_name': 'ND_splitlr_vector4', 'nd': None}}

    bl_label = 'Splitlr'
    bl_idname = 'usdhydra.MxNode_STD_splitlr'
    bl_description = ""

    category = 'procedural2d'

    data_type: EnumProperty(name="Type", description="Input Data Type", items=[('float', 'Float', 'Float'), ('color3', 'Color3', 'Color3'), ('color4', 'Color4', 'Color4'), ('vector2', 'Vector2', 'Vector2'), ('vector3', 'Vector3', 'Vector3'), ('vector4', 'Vector4', 'Vector4')], default='color3', update=MxNode.update_data_type)

    nd_float_in_valuel: FloatProperty(name="Left", description="", default=0.0, update=MxNode.update_prop)
    nd_float_in_valuer: FloatProperty(name="Right", description="", default=0.0, update=MxNode.update_prop)
    nd_float_in_center: FloatProperty(name="Center", description="", min=0.0, max=1.0, default=0.5, update=MxNode.update_prop)
    nd_float_in_texcoord: FloatVectorProperty(name="Texcoord", description="", subtype="NONE", size=2, update=MxNode.update_prop)
    nd_float_out_out: FloatProperty(name="Out", description="", update=MxNode.update_prop)

    nd_color3_in_valuel: FloatVectorProperty(name="Left", description="", subtype="COLOR", size=3, soft_min=0.0, soft_max=1.0, default=(0.0, 0.0, 0.0), update=MxNode.update_prop)
    nd_color3_in_valuer: FloatVectorProperty(name="Right", description="", subtype="COLOR", size=3, soft_min=0.0, soft_max=1.0, default=(0.0, 0.0, 0.0), update=MxNode.update_prop)
    nd_color3_in_center: FloatProperty(name="Center", description="", min=0.0, max=1.0, default=0.5, update=MxNode.update_prop)
    nd_color3_in_texcoord: FloatVectorProperty(name="Texcoord", description="", subtype="NONE", size=2, update=MxNode.update_prop)
    nd_color3_out_out: FloatVectorProperty(name="Out", description="", subtype="COLOR", size=3, soft_min=0.0, soft_max=1.0, update=MxNode.update_prop)

    nd_color4_in_valuel: FloatVectorProperty(name="Left", description="", subtype="COLOR", size=4, soft_min=0.0, soft_max=1.0, default=(0.0, 0.0, 0.0, 0.0), update=MxNode.update_prop)
    nd_color4_in_valuer: FloatVectorProperty(name="Right", description="", subtype="COLOR", size=4, soft_min=0.0, soft_max=1.0, default=(0.0, 0.0, 0.0, 0.0), update=MxNode.update_prop)
    nd_color4_in_center: FloatProperty(name="Center", description="", min=0.0, max=1.0, default=0.5, update=MxNode.update_prop)
    nd_color4_in_texcoord: FloatVectorProperty(name="Texcoord", description="", subtype="NONE", size=2, update=MxNode.update_prop)
    nd_color4_out_out: FloatVectorProperty(name="Out", description="", subtype="COLOR", size=4, soft_min=0.0, soft_max=1.0, update=MxNode.update_prop)

    nd_vector2_in_valuel: FloatVectorProperty(name="Left", description="", subtype="NONE", size=2, default=(0.0, 0.0), update=MxNode.update_prop)
    nd_vector2_in_valuer: FloatVectorProperty(name="Right", description="", subtype="NONE", size=2, default=(0.0, 0.0), update=MxNode.update_prop)
    nd_vector2_in_center: FloatProperty(name="Center", description="", min=0.0, max=1.0, default=0.5, update=MxNode.update_prop)
    nd_vector2_in_texcoord: FloatVectorProperty(name="Texcoord", description="", subtype="NONE", size=2, update=MxNode.update_prop)
    nd_vector2_out_out: FloatVectorProperty(name="Out", description="", subtype="NONE", size=2, update=MxNode.update_prop)

    nd_vector3_in_valuel: FloatVectorProperty(name="Left", description="", subtype="XYZ", size=3, default=(0.0, 0.0, 0.0), update=MxNode.update_prop)
    nd_vector3_in_valuer: FloatVectorProperty(name="Right", description="", subtype="XYZ", size=3, default=(0.0, 0.0, 0.0), update=MxNode.update_prop)
    nd_vector3_in_center: FloatProperty(name="Center", description="", min=0.0, max=1.0, default=0.5, update=MxNode.update_prop)
    nd_vector3_in_texcoord: FloatVectorProperty(name="Texcoord", description="", subtype="NONE", size=2, update=MxNode.update_prop)
    nd_vector3_out_out: FloatVectorProperty(name="Out", description="", subtype="XYZ", size=3, update=MxNode.update_prop)

    nd_vector4_in_valuel: FloatVectorProperty(name="Left", description="", subtype="NONE", size=4, default=(0.0, 0.0, 0.0, 0.0), update=MxNode.update_prop)
    nd_vector4_in_valuer: FloatVectorProperty(name="Right", description="", subtype="NONE", size=4, default=(0.0, 0.0, 0.0, 0.0), update=MxNode.update_prop)
    nd_vector4_in_center: FloatProperty(name="Center", description="", min=0.0, max=1.0, default=0.5, update=MxNode.update_prop)
    nd_vector4_in_texcoord: FloatVectorProperty(name="Texcoord", description="", subtype="NONE", size=2, update=MxNode.update_prop)
    nd_vector4_out_out: FloatVectorProperty(name="Out", description="", subtype="NONE", size=4, update=MxNode.update_prop)


class MxNode_STD_splittb(MxNode):
    _file_path = FILE_PATH
    _data_types = {'float': {'nd_name': 'ND_splittb_float', 'nd': None}, 'color3': {'nd_name': 'ND_splittb_color3', 'nd': None}, 'color4': {'nd_name': 'ND_splittb_color4', 'nd': None}, 'vector2': {'nd_name': 'ND_splittb_vector2', 'nd': None}, 'vector3': {'nd_name': 'ND_splittb_vector3', 'nd': None}, 'vector4': {'nd_name': 'ND_splittb_vector4', 'nd': None}}

    bl_label = 'Splittb'
    bl_idname = 'usdhydra.MxNode_STD_splittb'
    bl_description = ""

    category = 'procedural2d'

    data_type: EnumProperty(name="Type", description="Input Data Type", items=[('float', 'Float', 'Float'), ('color3', 'Color3', 'Color3'), ('color4', 'Color4', 'Color4'), ('vector2', 'Vector2', 'Vector2'), ('vector3', 'Vector3', 'Vector3'), ('vector4', 'Vector4', 'Vector4')], default='color3', update=MxNode.update_data_type)

    nd_float_in_valuet: FloatProperty(name="Top", description="", default=0.0, update=MxNode.update_prop)
    nd_float_in_valueb: FloatProperty(name="Bottom", description="", default=0.0, update=MxNode.update_prop)
    nd_float_in_center: FloatProperty(name="Center", description="", min=0.0, max=1.0, default=0.5, update=MxNode.update_prop)
    nd_float_in_texcoord: FloatVectorProperty(name="Texcoord", description="", subtype="NONE", size=2, update=MxNode.update_prop)
    nd_float_out_out: FloatProperty(name="Out", description="", update=MxNode.update_prop)

    nd_color3_in_valuet: FloatVectorProperty(name="Top", description="", subtype="COLOR", size=3, soft_min=0.0, soft_max=1.0, default=(0.0, 0.0, 0.0), update=MxNode.update_prop)
    nd_color3_in_valueb: FloatVectorProperty(name="Bottom", description="", subtype="COLOR", size=3, soft_min=0.0, soft_max=1.0, default=(0.0, 0.0, 0.0), update=MxNode.update_prop)
    nd_color3_in_center: FloatProperty(name="Center", description="", min=0.0, max=1.0, default=0.5, update=MxNode.update_prop)
    nd_color3_in_texcoord: FloatVectorProperty(name="Texcoord", description="", subtype="NONE", size=2, update=MxNode.update_prop)
    nd_color3_out_out: FloatVectorProperty(name="Out", description="", subtype="COLOR", size=3, soft_min=0.0, soft_max=1.0, update=MxNode.update_prop)

    nd_color4_in_valuet: FloatVectorProperty(name="Top", description="", subtype="COLOR", size=4, soft_min=0.0, soft_max=1.0, default=(0.0, 0.0, 0.0, 0.0), update=MxNode.update_prop)
    nd_color4_in_valueb: FloatVectorProperty(name="Bottom", description="", subtype="COLOR", size=4, soft_min=0.0, soft_max=1.0, default=(0.0, 0.0, 0.0, 0.0), update=MxNode.update_prop)
    nd_color4_in_center: FloatProperty(name="Center", description="", min=0.0, max=1.0, default=0.5, update=MxNode.update_prop)
    nd_color4_in_texcoord: FloatVectorProperty(name="Texcoord", description="", subtype="NONE", size=2, update=MxNode.update_prop)
    nd_color4_out_out: FloatVectorProperty(name="Out", description="", subtype="COLOR", size=4, soft_min=0.0, soft_max=1.0, update=MxNode.update_prop)

    nd_vector2_in_valuet: FloatVectorProperty(name="Top", description="", subtype="NONE", size=2, default=(0.0, 0.0), update=MxNode.update_prop)
    nd_vector2_in_valueb: FloatVectorProperty(name="Bottom", description="", subtype="NONE", size=2, default=(0.0, 0.0), update=MxNode.update_prop)
    nd_vector2_in_center: FloatProperty(name="Center", description="", min=0.0, max=1.0, default=0.5, update=MxNode.update_prop)
    nd_vector2_in_texcoord: FloatVectorProperty(name="Texcoord", description="", subtype="NONE", size=2, update=MxNode.update_prop)
    nd_vector2_out_out: FloatVectorProperty(name="Out", description="", subtype="NONE", size=2, update=MxNode.update_prop)

    nd_vector3_in_valuet: FloatVectorProperty(name="Top", description="", subtype="XYZ", size=3, default=(0.0, 0.0, 0.0), update=MxNode.update_prop)
    nd_vector3_in_valueb: FloatVectorProperty(name="Bottom", description="", subtype="XYZ", size=3, default=(0.0, 0.0, 0.0), update=MxNode.update_prop)
    nd_vector3_in_center: FloatProperty(name="Center", description="", min=0.0, max=1.0, default=0.5, update=MxNode.update_prop)
    nd_vector3_in_texcoord: FloatVectorProperty(name="Texcoord", description="", subtype="NONE", size=2, update=MxNode.update_prop)
    nd_vector3_out_out: FloatVectorProperty(name="Out", description="", subtype="XYZ", size=3, update=MxNode.update_prop)

    nd_vector4_in_valuet: FloatVectorProperty(name="Top", description="", subtype="NONE", size=4, default=(0.0, 0.0, 0.0, 0.0), update=MxNode.update_prop)
    nd_vector4_in_valueb: FloatVectorProperty(name="Bottom", description="", subtype="NONE", size=4, default=(0.0, 0.0, 0.0, 0.0), update=MxNode.update_prop)
    nd_vector4_in_center: FloatProperty(name="Center", description="", min=0.0, max=1.0, default=0.5, update=MxNode.update_prop)
    nd_vector4_in_texcoord: FloatVectorProperty(name="Texcoord", description="", subtype="NONE", size=2, update=MxNode.update_prop)
    nd_vector4_out_out: FloatVectorProperty(name="Out", description="", subtype="NONE", size=4, update=MxNode.update_prop)


class MxNode_STD_noise2d(MxNode):
    _file_path = FILE_PATH
    _data_types = {'float': {'nd_name': 'ND_noise2d_float', 'nd': None}, 'color3': {'nd_name': 'ND_noise2d_color3', 'nd': None}, 'color4': {'nd_name': 'ND_noise2d_color4', 'nd': None}, 'vector2': {'nd_name': 'ND_noise2d_vector2', 'nd': None}, 'vector3': {'nd_name': 'ND_noise2d_vector3', 'nd': None}, 'vector4': {'nd_name': 'ND_noise2d_vector4', 'nd': None}, 'color3FA': {'nd_name': 'ND_noise2d_color3FA', 'nd': None}, 'color4FA': {'nd_name': 'ND_noise2d_color4FA', 'nd': None}, 'vector2FA': {'nd_name': 'ND_noise2d_vector2FA', 'nd': None}, 'vector3FA': {'nd_name': 'ND_noise2d_vector3FA', 'nd': None}, 'vector4FA': {'nd_name': 'ND_noise2d_vector4FA', 'nd': None}}

    bl_label = 'Noise2d'
    bl_idname = 'usdhydra.MxNode_STD_noise2d'
    bl_description = ""

    category = 'procedural2d'

    data_type: EnumProperty(name="Type", description="Input Data Type", items=[('float', 'Float', 'Float'), ('color3', 'Color3', 'Color3'), ('color4', 'Color4', 'Color4'), ('vector2', 'Vector2', 'Vector2'), ('vector3', 'Vector3', 'Vector3'), ('vector4', 'Vector4', 'Vector4'), ('color3FA', 'Color3FA', 'Color3FA'), ('color4FA', 'Color4FA', 'Color4FA'), ('vector2FA', 'Vector2FA', 'Vector2FA'), ('vector3FA', 'Vector3FA', 'Vector3FA'), ('vector4FA', 'Vector4FA', 'Vector4FA')], default='color3', update=MxNode.update_data_type)

    nd_float_in_amplitude: FloatProperty(name="Amplitude", description="", default=1.0, update=MxNode.update_prop)
    nd_float_in_pivot: FloatProperty(name="Pivot", description="", default=0.0, update=MxNode.update_prop)
    nd_float_in_texcoord: FloatVectorProperty(name="Texcoord", description="", subtype="NONE", size=2, update=MxNode.update_prop)
    nd_float_out_out: FloatProperty(name="Out", description="", update=MxNode.update_prop)

    nd_color3_in_amplitude: FloatVectorProperty(name="Amplitude", description="", subtype="XYZ", size=3, default=(1.0, 1.0, 1.0), update=MxNode.update_prop)
    nd_color3_in_pivot: FloatProperty(name="Pivot", description="", default=0.0, update=MxNode.update_prop)
    nd_color3_in_texcoord: FloatVectorProperty(name="Texcoord", description="", subtype="NONE", size=2, update=MxNode.update_prop)
    nd_color3_out_out: FloatVectorProperty(name="Out", description="", subtype="COLOR", size=3, soft_min=0.0, soft_max=1.0, update=MxNode.update_prop)

    nd_color4_in_amplitude: FloatVectorProperty(name="Amplitude", description="", subtype="NONE", size=4, default=(1.0, 1.0, 1.0, 1.0), update=MxNode.update_prop)
    nd_color4_in_pivot: FloatProperty(name="Pivot", description="", default=0.0, update=MxNode.update_prop)
    nd_color4_in_texcoord: FloatVectorProperty(name="Texcoord", description="", subtype="NONE", size=2, update=MxNode.update_prop)
    nd_color4_out_out: FloatVectorProperty(name="Out", description="", subtype="COLOR", size=4, soft_min=0.0, soft_max=1.0, update=MxNode.update_prop)

    nd_vector2_in_amplitude: FloatVectorProperty(name="Amplitude", description="", subtype="NONE", size=2, default=(1.0, 1.0), update=MxNode.update_prop)
    nd_vector2_in_pivot: FloatProperty(name="Pivot", description="", default=0.0, update=MxNode.update_prop)
    nd_vector2_in_texcoord: FloatVectorProperty(name="Texcoord", description="", subtype="NONE", size=2, update=MxNode.update_prop)
    nd_vector2_out_out: FloatVectorProperty(name="Out", description="", subtype="NONE", size=2, update=MxNode.update_prop)

    nd_vector3_in_amplitude: FloatVectorProperty(name="Amplitude", description="", subtype="XYZ", size=3, default=(1.0, 1.0, 1.0), update=MxNode.update_prop)
    nd_vector3_in_pivot: FloatProperty(name="Pivot", description="", default=0.0, update=MxNode.update_prop)
    nd_vector3_in_texcoord: FloatVectorProperty(name="Texcoord", description="", subtype="NONE", size=2, update=MxNode.update_prop)
    nd_vector3_out_out: FloatVectorProperty(name="Out", description="", subtype="XYZ", size=3, update=MxNode.update_prop)

    nd_vector4_in_amplitude: FloatVectorProperty(name="Amplitude", description="", subtype="NONE", size=4, default=(1.0, 1.0, 1.0, 1.0), update=MxNode.update_prop)
    nd_vector4_in_pivot: FloatProperty(name="Pivot", description="", default=0.0, update=MxNode.update_prop)
    nd_vector4_in_texcoord: FloatVectorProperty(name="Texcoord", description="", subtype="NONE", size=2, update=MxNode.update_prop)
    nd_vector4_out_out: FloatVectorProperty(name="Out", description="", subtype="NONE", size=4, update=MxNode.update_prop)

    nd_color3FA_in_amplitude: FloatProperty(name="Amplitude", description="", default=1.0, update=MxNode.update_prop)
    nd_color3FA_in_pivot: FloatProperty(name="Pivot", description="", default=0.0, update=MxNode.update_prop)
    nd_color3FA_in_texcoord: FloatVectorProperty(name="Texcoord", description="", subtype="NONE", size=2, update=MxNode.update_prop)
    nd_color3FA_out_out: FloatVectorProperty(name="Out", description="", subtype="COLOR", size=3, soft_min=0.0, soft_max=1.0, update=MxNode.update_prop)

    nd_color4FA_in_amplitude: FloatProperty(name="Amplitude", description="", default=1.0, update=MxNode.update_prop)
    nd_color4FA_in_pivot: FloatProperty(name="Pivot", description="", default=0.0, update=MxNode.update_prop)
    nd_color4FA_in_texcoord: FloatVectorProperty(name="Texcoord", description="", subtype="NONE", size=2, update=MxNode.update_prop)
    nd_color4FA_out_out: FloatVectorProperty(name="Out", description="", subtype="COLOR", size=4, soft_min=0.0, soft_max=1.0, update=MxNode.update_prop)

    nd_vector2FA_in_amplitude: FloatProperty(name="Amplitude", description="", default=1.0, update=MxNode.update_prop)
    nd_vector2FA_in_pivot: FloatProperty(name="Pivot", description="", default=0.0, update=MxNode.update_prop)
    nd_vector2FA_in_texcoord: FloatVectorProperty(name="Texcoord", description="", subtype="NONE", size=2, update=MxNode.update_prop)
    nd_vector2FA_out_out: FloatVectorProperty(name="Out", description="", subtype="NONE", size=2, update=MxNode.update_prop)

    nd_vector3FA_in_amplitude: FloatProperty(name="Amplitude", description="", default=1.0, update=MxNode.update_prop)
    nd_vector3FA_in_pivot: FloatProperty(name="Pivot", description="", default=0.0, update=MxNode.update_prop)
    nd_vector3FA_in_texcoord: FloatVectorProperty(name="Texcoord", description="", subtype="NONE", size=2, update=MxNode.update_prop)
    nd_vector3FA_out_out: FloatVectorProperty(name="Out", description="", subtype="XYZ", size=3, update=MxNode.update_prop)

    nd_vector4FA_in_amplitude: FloatProperty(name="Amplitude", description="", default=1.0, update=MxNode.update_prop)
    nd_vector4FA_in_pivot: FloatProperty(name="Pivot", description="", default=0.0, update=MxNode.update_prop)
    nd_vector4FA_in_texcoord: FloatVectorProperty(name="Texcoord", description="", subtype="NONE", size=2, update=MxNode.update_prop)
    nd_vector4FA_out_out: FloatVectorProperty(name="Out", description="", subtype="NONE", size=4, update=MxNode.update_prop)


class MxNode_STD_noise3d(MxNode):
    _file_path = FILE_PATH
    _data_types = {'float': {'nd_name': 'ND_noise3d_float', 'nd': None}, 'color3': {'nd_name': 'ND_noise3d_color3', 'nd': None}, 'color4': {'nd_name': 'ND_noise3d_color4', 'nd': None}, 'vector2': {'nd_name': 'ND_noise3d_vector2', 'nd': None}, 'vector3': {'nd_name': 'ND_noise3d_vector3', 'nd': None}, 'vector4': {'nd_name': 'ND_noise3d_vector4', 'nd': None}, 'color3FA': {'nd_name': 'ND_noise3d_color3FA', 'nd': None}, 'color4FA': {'nd_name': 'ND_noise3d_color4FA', 'nd': None}, 'vector2FA': {'nd_name': 'ND_noise3d_vector2FA', 'nd': None}, 'vector3FA': {'nd_name': 'ND_noise3d_vector3FA', 'nd': None}, 'vector4FA': {'nd_name': 'ND_noise3d_vector4FA', 'nd': None}}

    bl_label = 'Noise3d'
    bl_idname = 'usdhydra.MxNode_STD_noise3d'
    bl_description = ""

    category = 'procedural3d'

    data_type: EnumProperty(name="Type", description="Input Data Type", items=[('float', 'Float', 'Float'), ('color3', 'Color3', 'Color3'), ('color4', 'Color4', 'Color4'), ('vector2', 'Vector2', 'Vector2'), ('vector3', 'Vector3', 'Vector3'), ('vector4', 'Vector4', 'Vector4'), ('color3FA', 'Color3FA', 'Color3FA'), ('color4FA', 'Color4FA', 'Color4FA'), ('vector2FA', 'Vector2FA', 'Vector2FA'), ('vector3FA', 'Vector3FA', 'Vector3FA'), ('vector4FA', 'Vector4FA', 'Vector4FA')], default='color3', update=MxNode.update_data_type)

    nd_float_in_amplitude: FloatProperty(name="Amplitude", description="", default=1.0, update=MxNode.update_prop)
    nd_float_in_pivot: FloatProperty(name="Pivot", description="", default=0.0, update=MxNode.update_prop)
    nd_float_in_position: FloatVectorProperty(name="Position", description="", subtype="XYZ", size=3, update=MxNode.update_prop)
    nd_float_out_out: FloatProperty(name="Out", description="", update=MxNode.update_prop)

    nd_color3_in_amplitude: FloatVectorProperty(name="Amplitude", description="", subtype="XYZ", size=3, default=(1.0, 1.0, 1.0), update=MxNode.update_prop)
    nd_color3_in_pivot: FloatProperty(name="Pivot", description="", default=0.0, update=MxNode.update_prop)
    nd_color3_in_position: FloatVectorProperty(name="Position", description="", subtype="XYZ", size=3, update=MxNode.update_prop)
    nd_color3_out_out: FloatVectorProperty(name="Out", description="", subtype="COLOR", size=3, soft_min=0.0, soft_max=1.0, update=MxNode.update_prop)

    nd_color4_in_amplitude: FloatVectorProperty(name="Amplitude", description="", subtype="NONE", size=4, default=(1.0, 1.0, 1.0, 1.0), update=MxNode.update_prop)
    nd_color4_in_pivot: FloatProperty(name="Pivot", description="", default=0.0, update=MxNode.update_prop)
    nd_color4_in_position: FloatVectorProperty(name="Position", description="", subtype="XYZ", size=3, update=MxNode.update_prop)
    nd_color4_out_out: FloatVectorProperty(name="Out", description="", subtype="COLOR", size=4, soft_min=0.0, soft_max=1.0, update=MxNode.update_prop)

    nd_vector2_in_amplitude: FloatVectorProperty(name="Amplitude", description="", subtype="NONE", size=2, default=(1.0, 1.0), update=MxNode.update_prop)
    nd_vector2_in_pivot: FloatProperty(name="Pivot", description="", default=0.0, update=MxNode.update_prop)
    nd_vector2_in_position: FloatVectorProperty(name="Position", description="", subtype="XYZ", size=3, update=MxNode.update_prop)
    nd_vector2_out_out: FloatVectorProperty(name="Out", description="", subtype="NONE", size=2, update=MxNode.update_prop)

    nd_vector3_in_amplitude: FloatVectorProperty(name="Amplitude", description="", subtype="XYZ", size=3, default=(1.0, 1.0, 1.0), update=MxNode.update_prop)
    nd_vector3_in_pivot: FloatProperty(name="Pivot", description="", default=0.0, update=MxNode.update_prop)
    nd_vector3_in_position: FloatVectorProperty(name="Position", description="", subtype="XYZ", size=3, update=MxNode.update_prop)
    nd_vector3_out_out: FloatVectorProperty(name="Out", description="", subtype="XYZ", size=3, update=MxNode.update_prop)

    nd_vector4_in_amplitude: FloatVectorProperty(name="Amplitude", description="", subtype="NONE", size=4, default=(1.0, 1.0, 1.0, 1.0), update=MxNode.update_prop)
    nd_vector4_in_pivot: FloatProperty(name="Pivot", description="", default=0.0, update=MxNode.update_prop)
    nd_vector4_in_position: FloatVectorProperty(name="Position", description="", subtype="XYZ", size=3, update=MxNode.update_prop)
    nd_vector4_out_out: FloatVectorProperty(name="Out", description="", subtype="NONE", size=4, update=MxNode.update_prop)

    nd_color3FA_in_amplitude: FloatProperty(name="Amplitude", description="", default=1.0, update=MxNode.update_prop)
    nd_color3FA_in_pivot: FloatProperty(name="Pivot", description="", default=0.0, update=MxNode.update_prop)
    nd_color3FA_in_position: FloatVectorProperty(name="Position", description="", subtype="XYZ", size=3, update=MxNode.update_prop)
    nd_color3FA_out_out: FloatVectorProperty(name="Out", description="", subtype="COLOR", size=3, soft_min=0.0, soft_max=1.0, update=MxNode.update_prop)

    nd_color4FA_in_amplitude: FloatProperty(name="Amplitude", description="", default=1.0, update=MxNode.update_prop)
    nd_color4FA_in_pivot: FloatProperty(name="Pivot", description="", default=0.0, update=MxNode.update_prop)
    nd_color4FA_in_position: FloatVectorProperty(name="Position", description="", subtype="XYZ", size=3, update=MxNode.update_prop)
    nd_color4FA_out_out: FloatVectorProperty(name="Out", description="", subtype="COLOR", size=4, soft_min=0.0, soft_max=1.0, update=MxNode.update_prop)

    nd_vector2FA_in_amplitude: FloatProperty(name="Amplitude", description="", default=1.0, update=MxNode.update_prop)
    nd_vector2FA_in_pivot: FloatProperty(name="Pivot", description="", default=0.0, update=MxNode.update_prop)
    nd_vector2FA_in_position: FloatVectorProperty(name="Position", description="", subtype="XYZ", size=3, update=MxNode.update_prop)
    nd_vector2FA_out_out: FloatVectorProperty(name="Out", description="", subtype="NONE", size=2, update=MxNode.update_prop)

    nd_vector3FA_in_amplitude: FloatProperty(name="Amplitude", description="", default=1.0, update=MxNode.update_prop)
    nd_vector3FA_in_pivot: FloatProperty(name="Pivot", description="", default=0.0, update=MxNode.update_prop)
    nd_vector3FA_in_position: FloatVectorProperty(name="Position", description="", subtype="XYZ", size=3, update=MxNode.update_prop)
    nd_vector3FA_out_out: FloatVectorProperty(name="Out", description="", subtype="XYZ", size=3, update=MxNode.update_prop)

    nd_vector4FA_in_amplitude: FloatProperty(name="Amplitude", description="", default=1.0, update=MxNode.update_prop)
    nd_vector4FA_in_pivot: FloatProperty(name="Pivot", description="", default=0.0, update=MxNode.update_prop)
    nd_vector4FA_in_position: FloatVectorProperty(name="Position", description="", subtype="XYZ", size=3, update=MxNode.update_prop)
    nd_vector4FA_out_out: FloatVectorProperty(name="Out", description="", subtype="NONE", size=4, update=MxNode.update_prop)


class MxNode_STD_fractal3d(MxNode):
    _file_path = FILE_PATH
    _data_types = {'float': {'nd_name': 'ND_fractal3d_float', 'nd': None}, 'color3': {'nd_name': 'ND_fractal3d_color3', 'nd': None}, 'color4': {'nd_name': 'ND_fractal3d_color4', 'nd': None}, 'vector2': {'nd_name': 'ND_fractal3d_vector2', 'nd': None}, 'vector3': {'nd_name': 'ND_fractal3d_vector3', 'nd': None}, 'vector4': {'nd_name': 'ND_fractal3d_vector4', 'nd': None}, 'color3FA': {'nd_name': 'ND_fractal3d_color3FA', 'nd': None}, 'color4FA': {'nd_name': 'ND_fractal3d_color4FA', 'nd': None}, 'vector2FA': {'nd_name': 'ND_fractal3d_vector2FA', 'nd': None}, 'vector3FA': {'nd_name': 'ND_fractal3d_vector3FA', 'nd': None}, 'vector4FA': {'nd_name': 'ND_fractal3d_vector4FA', 'nd': None}}

    bl_label = 'Fractal3d'
    bl_idname = 'usdhydra.MxNode_STD_fractal3d'
    bl_description = ""

    category = 'procedural3d'

    data_type: EnumProperty(name="Type", description="Input Data Type", items=[('float', 'Float', 'Float'), ('color3', 'Color3', 'Color3'), ('color4', 'Color4', 'Color4'), ('vector2', 'Vector2', 'Vector2'), ('vector3', 'Vector3', 'Vector3'), ('vector4', 'Vector4', 'Vector4'), ('color3FA', 'Color3FA', 'Color3FA'), ('color4FA', 'Color4FA', 'Color4FA'), ('vector2FA', 'Vector2FA', 'Vector2FA'), ('vector3FA', 'Vector3FA', 'Vector3FA'), ('vector4FA', 'Vector4FA', 'Vector4FA')], default='color3', update=MxNode.update_data_type)

    nd_float_in_amplitude: FloatProperty(name="Amplitude", description="", default=1.0, update=MxNode.update_prop)
    nd_float_in_octaves: IntProperty(name="Octaves", description="", default=3, update=MxNode.update_prop)
    nd_float_in_lacunarity: FloatProperty(name="Lacunarity", description="", default=2.0, update=MxNode.update_prop)
    nd_float_in_diminish: FloatProperty(name="Diminish", description="", default=0.5, update=MxNode.update_prop)
    nd_float_in_position: FloatVectorProperty(name="Position", description="", subtype="XYZ", size=3, update=MxNode.update_prop)
    nd_float_out_out: FloatProperty(name="Out", description="", update=MxNode.update_prop)

    nd_color3_in_amplitude: FloatVectorProperty(name="Amplitude", description="", subtype="XYZ", size=3, default=(1.0, 1.0, 1.0), update=MxNode.update_prop)
    nd_color3_in_octaves: IntProperty(name="Octaves", description="", default=3, update=MxNode.update_prop)
    nd_color3_in_lacunarity: FloatProperty(name="Lacunarity", description="", default=2.0, update=MxNode.update_prop)
    nd_color3_in_diminish: FloatProperty(name="Diminish", description="", default=0.5, update=MxNode.update_prop)
    nd_color3_in_position: FloatVectorProperty(name="Position", description="", subtype="XYZ", size=3, update=MxNode.update_prop)
    nd_color3_out_out: FloatVectorProperty(name="Out", description="", subtype="COLOR", size=3, soft_min=0.0, soft_max=1.0, update=MxNode.update_prop)

    nd_color4_in_amplitude: FloatVectorProperty(name="Amplitude", description="", subtype="NONE", size=4, default=(1.0, 1.0, 1.0, 1.0), update=MxNode.update_prop)
    nd_color4_in_octaves: IntProperty(name="Octaves", description="", default=3, update=MxNode.update_prop)
    nd_color4_in_lacunarity: FloatProperty(name="Lacunarity", description="", default=2.0, update=MxNode.update_prop)
    nd_color4_in_diminish: FloatProperty(name="Diminish", description="", default=0.5, update=MxNode.update_prop)
    nd_color4_in_position: FloatVectorProperty(name="Position", description="", subtype="XYZ", size=3, update=MxNode.update_prop)
    nd_color4_out_out: FloatVectorProperty(name="Out", description="", subtype="COLOR", size=4, soft_min=0.0, soft_max=1.0, update=MxNode.update_prop)

    nd_vector2_in_amplitude: FloatVectorProperty(name="Amplitude", description="", subtype="NONE", size=2, default=(1.0, 1.0), update=MxNode.update_prop)
    nd_vector2_in_octaves: IntProperty(name="Octaves", description="", default=3, update=MxNode.update_prop)
    nd_vector2_in_lacunarity: FloatProperty(name="Lacunarity", description="", default=2.0, update=MxNode.update_prop)
    nd_vector2_in_diminish: FloatProperty(name="Diminish", description="", default=0.5, update=MxNode.update_prop)
    nd_vector2_in_position: FloatVectorProperty(name="Position", description="", subtype="XYZ", size=3, update=MxNode.update_prop)
    nd_vector2_out_out: FloatVectorProperty(name="Out", description="", subtype="NONE", size=2, update=MxNode.update_prop)

    nd_vector3_in_amplitude: FloatVectorProperty(name="Amplitude", description="", subtype="XYZ", size=3, default=(1.0, 1.0, 1.0), update=MxNode.update_prop)
    nd_vector3_in_octaves: IntProperty(name="Octaves", description="", default=3, update=MxNode.update_prop)
    nd_vector3_in_lacunarity: FloatProperty(name="Lacunarity", description="", default=2.0, update=MxNode.update_prop)
    nd_vector3_in_diminish: FloatProperty(name="Diminish", description="", default=0.5, update=MxNode.update_prop)
    nd_vector3_in_position: FloatVectorProperty(name="Position", description="", subtype="XYZ", size=3, update=MxNode.update_prop)
    nd_vector3_out_out: FloatVectorProperty(name="Out", description="", subtype="XYZ", size=3, update=MxNode.update_prop)

    nd_vector4_in_amplitude: FloatVectorProperty(name="Amplitude", description="", subtype="NONE", size=4, default=(1.0, 1.0, 1.0, 1.0), update=MxNode.update_prop)
    nd_vector4_in_octaves: IntProperty(name="Octaves", description="", default=3, update=MxNode.update_prop)
    nd_vector4_in_lacunarity: FloatProperty(name="Lacunarity", description="", default=2.0, update=MxNode.update_prop)
    nd_vector4_in_diminish: FloatProperty(name="Diminish", description="", default=0.5, update=MxNode.update_prop)
    nd_vector4_in_position: FloatVectorProperty(name="Position", description="", subtype="XYZ", size=3, update=MxNode.update_prop)
    nd_vector4_out_out: FloatVectorProperty(name="Out", description="", subtype="NONE", size=4, update=MxNode.update_prop)

    nd_color3FA_in_amplitude: FloatProperty(name="Amplitude", description="", default=1.0, update=MxNode.update_prop)
    nd_color3FA_in_octaves: IntProperty(name="Octaves", description="", default=3, update=MxNode.update_prop)
    nd_color3FA_in_lacunarity: FloatProperty(name="Lacunarity", description="", default=2.0, update=MxNode.update_prop)
    nd_color3FA_in_diminish: FloatProperty(name="Diminish", description="", default=0.5, update=MxNode.update_prop)
    nd_color3FA_in_position: FloatVectorProperty(name="Position", description="", subtype="XYZ", size=3, update=MxNode.update_prop)
    nd_color3FA_out_out: FloatVectorProperty(name="Out", description="", subtype="COLOR", size=3, soft_min=0.0, soft_max=1.0, update=MxNode.update_prop)

    nd_color4FA_in_amplitude: FloatProperty(name="Amplitude", description="", default=1.0, update=MxNode.update_prop)
    nd_color4FA_in_octaves: IntProperty(name="Octaves", description="", default=3, update=MxNode.update_prop)
    nd_color4FA_in_lacunarity: FloatProperty(name="Lacunarity", description="", default=2.0, update=MxNode.update_prop)
    nd_color4FA_in_diminish: FloatProperty(name="Diminish", description="", default=0.5, update=MxNode.update_prop)
    nd_color4FA_in_position: FloatVectorProperty(name="Position", description="", subtype="XYZ", size=3, update=MxNode.update_prop)
    nd_color4FA_out_out: FloatVectorProperty(name="Out", description="", subtype="COLOR", size=4, soft_min=0.0, soft_max=1.0, update=MxNode.update_prop)

    nd_vector2FA_in_amplitude: FloatProperty(name="Amplitude", description="", default=1.0, update=MxNode.update_prop)
    nd_vector2FA_in_octaves: IntProperty(name="Octaves", description="", default=3, update=MxNode.update_prop)
    nd_vector2FA_in_lacunarity: FloatProperty(name="Lacunarity", description="", default=2.0, update=MxNode.update_prop)
    nd_vector2FA_in_diminish: FloatProperty(name="Diminish", description="", default=0.5, update=MxNode.update_prop)
    nd_vector2FA_in_position: FloatVectorProperty(name="Position", description="", subtype="XYZ", size=3, update=MxNode.update_prop)
    nd_vector2FA_out_out: FloatVectorProperty(name="Out", description="", subtype="NONE", size=2, update=MxNode.update_prop)

    nd_vector3FA_in_amplitude: FloatProperty(name="Amplitude", description="", default=1.0, update=MxNode.update_prop)
    nd_vector3FA_in_octaves: IntProperty(name="Octaves", description="", default=3, update=MxNode.update_prop)
    nd_vector3FA_in_lacunarity: FloatProperty(name="Lacunarity", description="", default=2.0, update=MxNode.update_prop)
    nd_vector3FA_in_diminish: FloatProperty(name="Diminish", description="", default=0.5, update=MxNode.update_prop)
    nd_vector3FA_in_position: FloatVectorProperty(name="Position", description="", subtype="XYZ", size=3, update=MxNode.update_prop)
    nd_vector3FA_out_out: FloatVectorProperty(name="Out", description="", subtype="XYZ", size=3, update=MxNode.update_prop)

    nd_vector4FA_in_amplitude: FloatProperty(name="Amplitude", description="", default=1.0, update=MxNode.update_prop)
    nd_vector4FA_in_octaves: IntProperty(name="Octaves", description="", default=3, update=MxNode.update_prop)
    nd_vector4FA_in_lacunarity: FloatProperty(name="Lacunarity", description="", default=2.0, update=MxNode.update_prop)
    nd_vector4FA_in_diminish: FloatProperty(name="Diminish", description="", default=0.5, update=MxNode.update_prop)
    nd_vector4FA_in_position: FloatVectorProperty(name="Position", description="", subtype="XYZ", size=3, update=MxNode.update_prop)
    nd_vector4FA_out_out: FloatVectorProperty(name="Out", description="", subtype="NONE", size=4, update=MxNode.update_prop)


class MxNode_STD_cellnoise2d(MxNode):
    _file_path = FILE_PATH
    _data_types = {'float': {'nd_name': 'ND_cellnoise2d_float', 'nd': None}}

    bl_label = 'Cellnoise2d'
    bl_idname = 'usdhydra.MxNode_STD_cellnoise2d'
    bl_description = ""

    category = 'procedural2d'

    data_type: EnumProperty(name="Type", description="Input Data Type", items=[('float', 'Float', 'Float')], default='float', update=MxNode.update_data_type)

    nd_float_in_texcoord: FloatVectorProperty(name="Texcoord", description="", subtype="NONE", size=2, update=MxNode.update_prop)
    nd_float_out_out: FloatProperty(name="Out", description="", update=MxNode.update_prop)


class MxNode_STD_cellnoise3d(MxNode):
    _file_path = FILE_PATH
    _data_types = {'float': {'nd_name': 'ND_cellnoise3d_float', 'nd': None}}

    bl_label = 'Cellnoise3d'
    bl_idname = 'usdhydra.MxNode_STD_cellnoise3d'
    bl_description = ""

    category = 'procedural3d'

    data_type: EnumProperty(name="Type", description="Input Data Type", items=[('float', 'Float', 'Float')], default='float', update=MxNode.update_data_type)

    nd_float_in_position: FloatVectorProperty(name="Position", description="", subtype="XYZ", size=3, update=MxNode.update_prop)
    nd_float_out_out: FloatProperty(name="Out", description="", update=MxNode.update_prop)


class MxNode_STD_worleynoise2d(MxNode):
    _file_path = FILE_PATH
    _data_types = {'float': {'nd_name': 'ND_worleynoise2d_float', 'nd': None}, 'vector2': {'nd_name': 'ND_worleynoise2d_vector2', 'nd': None}, 'vector3': {'nd_name': 'ND_worleynoise2d_vector3', 'nd': None}}

    bl_label = 'Worleynoise2d'
    bl_idname = 'usdhydra.MxNode_STD_worleynoise2d'
    bl_description = ""

    category = 'procedural2d'

    data_type: EnumProperty(name="Type", description="Input Data Type", items=[('float', 'Float', 'Float'), ('vector2', 'Vector2', 'Vector2'), ('vector3', 'Vector3', 'Vector3')], default='float', update=MxNode.update_data_type)

    nd_float_in_texcoord: FloatVectorProperty(name="Texcoord", description="", subtype="NONE", size=2, update=MxNode.update_prop)
    nd_float_in_jitter: FloatProperty(name="Jitter", description="", default=1.0, update=MxNode.update_prop)
    nd_float_out_out: FloatProperty(name="Out", description="", update=MxNode.update_prop)

    nd_vector2_in_texcoord: FloatVectorProperty(name="Texcoord", description="", subtype="NONE", size=2, update=MxNode.update_prop)
    nd_vector2_in_jitter: FloatProperty(name="Jitter", description="", default=1.0, update=MxNode.update_prop)
    nd_vector2_out_out: FloatVectorProperty(name="Out", description="", subtype="NONE", size=2, update=MxNode.update_prop)

    nd_vector3_in_texcoord: FloatVectorProperty(name="Texcoord", description="", subtype="NONE", size=2, update=MxNode.update_prop)
    nd_vector3_in_jitter: FloatProperty(name="Jitter", description="", default=1.0, update=MxNode.update_prop)
    nd_vector3_out_out: FloatVectorProperty(name="Out", description="", subtype="XYZ", size=3, update=MxNode.update_prop)


class MxNode_STD_worleynoise3d(MxNode):
    _file_path = FILE_PATH
    _data_types = {'float': {'nd_name': 'ND_worleynoise3d_float', 'nd': None}, 'vector2': {'nd_name': 'ND_worleynoise3d_vector2', 'nd': None}, 'vector3': {'nd_name': 'ND_worleynoise3d_vector3', 'nd': None}}

    bl_label = 'Worleynoise3d'
    bl_idname = 'usdhydra.MxNode_STD_worleynoise3d'
    bl_description = ""

    category = 'procedural3d'

    data_type: EnumProperty(name="Type", description="Input Data Type", items=[('float', 'Float', 'Float'), ('vector2', 'Vector2', 'Vector2'), ('vector3', 'Vector3', 'Vector3')], default='float', update=MxNode.update_data_type)

    nd_float_in_position: FloatVectorProperty(name="Position", description="", subtype="XYZ", size=3, update=MxNode.update_prop)
    nd_float_in_jitter: FloatProperty(name="Jitter", description="", default=1.0, update=MxNode.update_prop)
    nd_float_out_out: FloatProperty(name="Out", description="", update=MxNode.update_prop)

    nd_vector2_in_position: FloatVectorProperty(name="Position", description="", subtype="XYZ", size=3, update=MxNode.update_prop)
    nd_vector2_in_jitter: FloatProperty(name="Jitter", description="", default=1.0, update=MxNode.update_prop)
    nd_vector2_out_out: FloatVectorProperty(name="Out", description="", subtype="NONE", size=2, update=MxNode.update_prop)

    nd_vector3_in_position: FloatVectorProperty(name="Position", description="", subtype="XYZ", size=3, update=MxNode.update_prop)
    nd_vector3_in_jitter: FloatProperty(name="Jitter", description="", default=1.0, update=MxNode.update_prop)
    nd_vector3_out_out: FloatVectorProperty(name="Out", description="", subtype="XYZ", size=3, update=MxNode.update_prop)


class MxNode_STD_position(MxNode):
    _file_path = FILE_PATH
    _data_types = {'vector3': {'nd_name': 'ND_position_vector3', 'nd': None}}

    bl_label = 'Position'
    bl_idname = 'usdhydra.MxNode_STD_position'
    bl_description = ""

    category = 'geometric'

    data_type: EnumProperty(name="Type", description="Input Data Type", items=[('vector3', 'Vector3', 'Vector3')], default='vector3', update=MxNode.update_data_type)

    nd_vector3_in_space: EnumProperty(name="Space", description="", items=(('model', 'Model', 'Model'), ('object', 'Object', 'Object'), ('world', 'World', 'World')), default="object", update=MxNode.update_prop)
    nd_vector3_out_out: FloatVectorProperty(name="Out", description="", subtype="XYZ", size=3, update=MxNode.update_prop)


class MxNode_STD_normal(MxNode):
    _file_path = FILE_PATH
    _data_types = {'vector3': {'nd_name': 'ND_normal_vector3', 'nd': None}}

    bl_label = 'Normal'
    bl_idname = 'usdhydra.MxNode_STD_normal'
    bl_description = ""

    category = 'geometric'

    data_type: EnumProperty(name="Type", description="Input Data Type", items=[('vector3', 'Vector3', 'Vector3')], default='vector3', update=MxNode.update_data_type)

    nd_vector3_in_space: EnumProperty(name="Space", description="", items=(('model', 'Model', 'Model'), ('object', 'Object', 'Object'), ('world', 'World', 'World')), default="object", update=MxNode.update_prop)
    nd_vector3_out_out: FloatVectorProperty(name="Out", description="", subtype="XYZ", size=3, update=MxNode.update_prop)


class MxNode_STD_tangent(MxNode):
    _file_path = FILE_PATH
    _data_types = {'vector3': {'nd_name': 'ND_tangent_vector3', 'nd': None}}

    bl_label = 'Tangent'
    bl_idname = 'usdhydra.MxNode_STD_tangent'
    bl_description = ""

    category = 'geometric'

    data_type: EnumProperty(name="Type", description="Input Data Type", items=[('vector3', 'Vector3', 'Vector3')], default='vector3', update=MxNode.update_data_type)

    nd_vector3_in_space: EnumProperty(name="Space", description="", items=(('model', 'Model', 'Model'), ('object', 'Object', 'Object'), ('world', 'World', 'World')), default="object", update=MxNode.update_prop)
    nd_vector3_in_index: IntProperty(name="Index", description="", default=0, update=MxNode.update_prop)
    nd_vector3_out_out: FloatVectorProperty(name="Out", description="", subtype="XYZ", size=3, update=MxNode.update_prop)


class MxNode_STD_bitangent(MxNode):
    _file_path = FILE_PATH
    _data_types = {'vector3': {'nd_name': 'ND_bitangent_vector3', 'nd': None}}

    bl_label = 'Bitangent'
    bl_idname = 'usdhydra.MxNode_STD_bitangent'
    bl_description = ""

    category = 'geometric'

    data_type: EnumProperty(name="Type", description="Input Data Type", items=[('vector3', 'Vector3', 'Vector3')], default='vector3', update=MxNode.update_data_type)

    nd_vector3_in_space: EnumProperty(name="Space", description="", items=(('model', 'Model', 'Model'), ('object', 'Object', 'Object'), ('world', 'World', 'World')), default="object", update=MxNode.update_prop)
    nd_vector3_in_index: IntProperty(name="Index", description="", default=0, update=MxNode.update_prop)
    nd_vector3_out_out: FloatVectorProperty(name="Out", description="", subtype="XYZ", size=3, update=MxNode.update_prop)


class MxNode_STD_texcoord(MxNode):
    _file_path = FILE_PATH
    _data_types = {'vector2': {'nd_name': 'ND_texcoord_vector2', 'nd': None}, 'vector3': {'nd_name': 'ND_texcoord_vector3', 'nd': None}}

    bl_label = 'Texcoord'
    bl_idname = 'usdhydra.MxNode_STD_texcoord'
    bl_description = ""

    category = 'geometric'

    data_type: EnumProperty(name="Type", description="Input Data Type", items=[('vector2', 'Vector2', 'Vector2'), ('vector3', 'Vector3', 'Vector3')], default='vector2', update=MxNode.update_data_type)

    nd_vector2_in_index: IntProperty(name="Index", description="", default=0, update=MxNode.update_prop)
    nd_vector2_out_out: FloatVectorProperty(name="Out", description="", subtype="NONE", size=2, update=MxNode.update_prop)

    nd_vector3_in_index: IntProperty(name="Index", description="", default=0, update=MxNode.update_prop)
    nd_vector3_out_out: FloatVectorProperty(name="Out", description="", subtype="XYZ", size=3, update=MxNode.update_prop)


class MxNode_STD_geomcolor(MxNode):
    _file_path = FILE_PATH
    _data_types = {'float': {'nd_name': 'ND_geomcolor_float', 'nd': None}, 'color3': {'nd_name': 'ND_geomcolor_color3', 'nd': None}, 'color4': {'nd_name': 'ND_geomcolor_color4', 'nd': None}}

    bl_label = 'Geomcolor'
    bl_idname = 'usdhydra.MxNode_STD_geomcolor'
    bl_description = ""

    category = 'geometric'

    data_type: EnumProperty(name="Type", description="Input Data Type", items=[('float', 'Float', 'Float'), ('color3', 'Color3', 'Color3'), ('color4', 'Color4', 'Color4')], default='color3', update=MxNode.update_data_type)

    nd_float_in_index: IntProperty(name="Index", description="", default=0, update=MxNode.update_prop)
    nd_float_out_out: FloatProperty(name="Out", description="", update=MxNode.update_prop)

    nd_color3_in_index: IntProperty(name="Index", description="", default=0, update=MxNode.update_prop)
    nd_color3_out_out: FloatVectorProperty(name="Out", description="", subtype="COLOR", size=3, soft_min=0.0, soft_max=1.0, update=MxNode.update_prop)

    nd_color4_in_index: IntProperty(name="Index", description="", default=0, update=MxNode.update_prop)
    nd_color4_out_out: FloatVectorProperty(name="Out", description="", subtype="COLOR", size=4, soft_min=0.0, soft_max=1.0, update=MxNode.update_prop)


class MxNode_STD_geompropvalue(MxNode):
    _file_path = FILE_PATH
    _data_types = {'integer': {'nd_name': 'ND_geompropvalue_integer', 'nd': None}, 'boolean': {'nd_name': 'ND_geompropvalue_boolean', 'nd': None}, 'string': {'nd_name': 'ND_geompropvalue_string', 'nd': None}, 'float': {'nd_name': 'ND_geompropvalue_float', 'nd': None}, 'color3': {'nd_name': 'ND_geompropvalue_color3', 'nd': None}, 'color4': {'nd_name': 'ND_geompropvalue_color4', 'nd': None}, 'vector2': {'nd_name': 'ND_geompropvalue_vector2', 'nd': None}, 'vector3': {'nd_name': 'ND_geompropvalue_vector3', 'nd': None}, 'vector4': {'nd_name': 'ND_geompropvalue_vector4', 'nd': None}}

    bl_label = 'Geompropvalue'
    bl_idname = 'usdhydra.MxNode_STD_geompropvalue'
    bl_description = ""

    category = 'geometric'

    data_type: EnumProperty(name="Type", description="Input Data Type", items=[('integer', 'Integer', 'Integer'), ('boolean', 'Boolean', 'Boolean'), ('string', 'String', 'String'), ('float', 'Float', 'Float'), ('color3', 'Color3', 'Color3'), ('color4', 'Color4', 'Color4'), ('vector2', 'Vector2', 'Vector2'), ('vector3', 'Vector3', 'Vector3'), ('vector4', 'Vector4', 'Vector4')], default='color3', update=MxNode.update_data_type)

    nd_integer_in_geomprop: StringProperty(name="Geomprop", description="", default="", update=MxNode.update_prop)
    nd_integer_in_default: IntProperty(name="Default", description="", default=0, update=MxNode.update_prop)
    nd_integer_out_out: IntProperty(name="Out", description="", update=MxNode.update_prop)

    nd_boolean_in_geomprop: StringProperty(name="Geomprop", description="", default="", update=MxNode.update_prop)
    nd_boolean_in_default: BoolProperty(name="Default", description="", default=False, update=MxNode.update_prop)
    nd_boolean_out_out: BoolProperty(name="Out", description="", update=MxNode.update_prop)

    nd_string_in_geomprop: StringProperty(name="Geomprop", description="", default="", update=MxNode.update_prop)
    nd_string_in_default: StringProperty(name="Default", description="", default="", update=MxNode.update_prop)
    nd_string_out_out: StringProperty(name="Out", description="", update=MxNode.update_prop)

    nd_float_in_geomprop: StringProperty(name="Geomprop", description="", default="", update=MxNode.update_prop)
    nd_float_in_default: FloatProperty(name="Default", description="", default=0.0, update=MxNode.update_prop)
    nd_float_out_out: FloatProperty(name="Out", description="", update=MxNode.update_prop)

    nd_color3_in_geomprop: StringProperty(name="Geomprop", description="", default="", update=MxNode.update_prop)
    nd_color3_in_default: FloatVectorProperty(name="Default", description="", subtype="COLOR", size=3, soft_min=0.0, soft_max=1.0, default=(0.0, 0.0, 0.0), update=MxNode.update_prop)
    nd_color3_out_out: FloatVectorProperty(name="Out", description="", subtype="COLOR", size=3, soft_min=0.0, soft_max=1.0, update=MxNode.update_prop)

    nd_color4_in_geomprop: StringProperty(name="Geomprop", description="", default="", update=MxNode.update_prop)
    nd_color4_in_default: FloatVectorProperty(name="Default", description="", subtype="COLOR", size=4, soft_min=0.0, soft_max=1.0, default=(0.0, 0.0, 0.0, 0.0), update=MxNode.update_prop)
    nd_color4_out_out: FloatVectorProperty(name="Out", description="", subtype="COLOR", size=4, soft_min=0.0, soft_max=1.0, update=MxNode.update_prop)

    nd_vector2_in_geomprop: StringProperty(name="Geomprop", description="", default="", update=MxNode.update_prop)
    nd_vector2_in_default: FloatVectorProperty(name="Default", description="", subtype="NONE", size=2, default=(0.0, 0.0), update=MxNode.update_prop)
    nd_vector2_out_out: FloatVectorProperty(name="Out", description="", subtype="NONE", size=2, update=MxNode.update_prop)

    nd_vector3_in_geomprop: StringProperty(name="Geomprop", description="", default="", update=MxNode.update_prop)
    nd_vector3_in_default: FloatVectorProperty(name="Default", description="", subtype="XYZ", size=3, default=(0.0, 0.0, 0.0), update=MxNode.update_prop)
    nd_vector3_out_out: FloatVectorProperty(name="Out", description="", subtype="XYZ", size=3, update=MxNode.update_prop)

    nd_vector4_in_geomprop: StringProperty(name="Geomprop", description="", default="", update=MxNode.update_prop)
    nd_vector4_in_default: FloatVectorProperty(name="Default", description="", subtype="NONE", size=4, default=(0.0, 0.0, 0.0, 0.0), update=MxNode.update_prop)
    nd_vector4_out_out: FloatVectorProperty(name="Out", description="", subtype="NONE", size=4, update=MxNode.update_prop)


class MxNode_STD_ambientocclusion(MxNode):
    _file_path = FILE_PATH
    _data_types = {'float': {'nd_name': 'ND_ambientocclusion_float', 'nd': None}}

    bl_label = 'Ambientocclusion'
    bl_idname = 'usdhydra.MxNode_STD_ambientocclusion'
    bl_description = ""

    category = 'global'

    data_type: EnumProperty(name="Type", description="Input Data Type", items=[('float', 'Float', 'Float')], default='float', update=MxNode.update_data_type)

    nd_float_in_coneangle: FloatProperty(name="Coneangle", description="", default=90.0, update=MxNode.update_prop)
    nd_float_in_maxdistance: FloatProperty(name="Maxdistance", description="", default=1e+38, update=MxNode.update_prop)
    nd_float_out_out: FloatProperty(name="Out", description="", update=MxNode.update_prop)


class MxNode_STD_frame(MxNode):
    _file_path = FILE_PATH
    _data_types = {'float': {'nd_name': 'ND_frame_float', 'nd': None}}

    bl_label = 'Frame'
    bl_idname = 'usdhydra.MxNode_STD_frame'
    bl_description = ""

    category = 'application'

    data_type: EnumProperty(name="Type", description="Input Data Type", items=[('float', 'Float', 'Float')], default='float', update=MxNode.update_data_type)

    nd_float_out_out: FloatProperty(name="Out", description="", update=MxNode.update_prop)


class MxNode_STD_time(MxNode):
    _file_path = FILE_PATH
    _data_types = {'float': {'nd_name': 'ND_time_float', 'nd': None}}

    bl_label = 'Time'
    bl_idname = 'usdhydra.MxNode_STD_time'
    bl_description = ""

    category = 'application'

    data_type: EnumProperty(name="Type", description="Input Data Type", items=[('float', 'Float', 'Float')], default='float', update=MxNode.update_data_type)

    nd_float_in_fps: FloatProperty(name="Fps", description="", default=24.0, update=MxNode.update_prop)
    nd_float_out_out: FloatProperty(name="Out", description="", update=MxNode.update_prop)


class MxNode_STD_add(MxNode):
    _file_path = FILE_PATH
    _data_types = {'float': {'nd_name': 'ND_add_float', 'nd': None}, 'color3': {'nd_name': 'ND_add_color3', 'nd': None}, 'color4': {'nd_name': 'ND_add_color4', 'nd': None}, 'vector2': {'nd_name': 'ND_add_vector2', 'nd': None}, 'vector3': {'nd_name': 'ND_add_vector3', 'nd': None}, 'vector4': {'nd_name': 'ND_add_vector4', 'nd': None}, 'surfaceshader': {'nd_name': 'ND_add_surfaceshader', 'nd': None}, 'displacementshader': {'nd_name': 'ND_add_displacementshader', 'nd': None}, 'volumeshader': {'nd_name': 'ND_add_volumeshader', 'nd': None}, 'color3FA': {'nd_name': 'ND_add_color3FA', 'nd': None}, 'color4FA': {'nd_name': 'ND_add_color4FA', 'nd': None}, 'vector2FA': {'nd_name': 'ND_add_vector2FA', 'nd': None}, 'vector3FA': {'nd_name': 'ND_add_vector3FA', 'nd': None}, 'vector4FA': {'nd_name': 'ND_add_vector4FA', 'nd': None}}

    bl_label = 'Add'
    bl_idname = 'usdhydra.MxNode_STD_add'
    bl_description = ""

    category = 'math'

    data_type: EnumProperty(name="Type", description="Input Data Type", items=[('float', 'Float', 'Float'), ('color3', 'Color3', 'Color3'), ('color4', 'Color4', 'Color4'), ('vector2', 'Vector2', 'Vector2'), ('vector3', 'Vector3', 'Vector3'), ('vector4', 'Vector4', 'Vector4'), ('surfaceshader', 'Surfaceshader', 'Surfaceshader'), ('displacementshader', 'Displacementshader', 'Displacementshader'), ('volumeshader', 'Volumeshader', 'Volumeshader'), ('color3FA', 'Color3FA', 'Color3FA'), ('color4FA', 'Color4FA', 'Color4FA'), ('vector2FA', 'Vector2FA', 'Vector2FA'), ('vector3FA', 'Vector3FA', 'Vector3FA'), ('vector4FA', 'Vector4FA', 'Vector4FA')], default='color3', update=MxNode.update_data_type)

    nd_float_in_in1: FloatProperty(name="In1", description="", default=0.0, update=MxNode.update_prop)
    nd_float_in_in2: FloatProperty(name="In2", description="", default=0.0, update=MxNode.update_prop)
    nd_float_out_out: FloatProperty(name="Out", description="", update=MxNode.update_prop)

    nd_color3_in_in1: FloatVectorProperty(name="In1", description="", subtype="COLOR", size=3, soft_min=0.0, soft_max=1.0, default=(0.0, 0.0, 0.0), update=MxNode.update_prop)
    nd_color3_in_in2: FloatVectorProperty(name="In2", description="", subtype="COLOR", size=3, soft_min=0.0, soft_max=1.0, default=(0.0, 0.0, 0.0), update=MxNode.update_prop)
    nd_color3_out_out: FloatVectorProperty(name="Out", description="", subtype="COLOR", size=3, soft_min=0.0, soft_max=1.0, update=MxNode.update_prop)

    nd_color4_in_in1: FloatVectorProperty(name="In1", description="", subtype="COLOR", size=4, soft_min=0.0, soft_max=1.0, default=(0.0, 0.0, 0.0, 0.0), update=MxNode.update_prop)
    nd_color4_in_in2: FloatVectorProperty(name="In2", description="", subtype="COLOR", size=4, soft_min=0.0, soft_max=1.0, default=(0.0, 0.0, 0.0, 0.0), update=MxNode.update_prop)
    nd_color4_out_out: FloatVectorProperty(name="Out", description="", subtype="COLOR", size=4, soft_min=0.0, soft_max=1.0, update=MxNode.update_prop)

    nd_vector2_in_in1: FloatVectorProperty(name="In1", description="", subtype="NONE", size=2, default=(0.0, 0.0), update=MxNode.update_prop)
    nd_vector2_in_in2: FloatVectorProperty(name="In2", description="", subtype="NONE", size=2, default=(0.0, 0.0), update=MxNode.update_prop)
    nd_vector2_out_out: FloatVectorProperty(name="Out", description="", subtype="NONE", size=2, update=MxNode.update_prop)

    nd_vector3_in_in1: FloatVectorProperty(name="In1", description="", subtype="XYZ", size=3, default=(0.0, 0.0, 0.0), update=MxNode.update_prop)
    nd_vector3_in_in2: FloatVectorProperty(name="In2", description="", subtype="XYZ", size=3, default=(0.0, 0.0, 0.0), update=MxNode.update_prop)
    nd_vector3_out_out: FloatVectorProperty(name="Out", description="", subtype="XYZ", size=3, update=MxNode.update_prop)

    nd_vector4_in_in1: FloatVectorProperty(name="In1", description="", subtype="NONE", size=4, default=(0.0, 0.0, 0.0, 0.0), update=MxNode.update_prop)
    nd_vector4_in_in2: FloatVectorProperty(name="In2", description="", subtype="NONE", size=4, default=(0.0, 0.0, 0.0, 0.0), update=MxNode.update_prop)
    nd_vector4_out_out: FloatVectorProperty(name="Out", description="", subtype="NONE", size=4, update=MxNode.update_prop)

    nd_surfaceshader_in_in1: StringProperty(name="In1", description="", default="", update=MxNode.update_prop)
    nd_surfaceshader_in_in2: StringProperty(name="In2", description="", default="", update=MxNode.update_prop)
    nd_surfaceshader_out_out: StringProperty(name="Out", description="", update=MxNode.update_prop)

    nd_displacementshader_in_in1: StringProperty(name="In1", description="", default="", update=MxNode.update_prop)
    nd_displacementshader_in_in2: StringProperty(name="In2", description="", default="", update=MxNode.update_prop)
    nd_displacementshader_out_out: StringProperty(name="Out", description="", update=MxNode.update_prop)

    nd_volumeshader_in_in1: StringProperty(name="In1", description="", default="", update=MxNode.update_prop)
    nd_volumeshader_in_in2: StringProperty(name="In2", description="", default="", update=MxNode.update_prop)
    nd_volumeshader_out_out: StringProperty(name="Out", description="", update=MxNode.update_prop)

    nd_color3FA_in_in1: FloatVectorProperty(name="In1", description="", subtype="COLOR", size=3, soft_min=0.0, soft_max=1.0, default=(0.0, 0.0, 0.0), update=MxNode.update_prop)
    nd_color3FA_in_in2: FloatProperty(name="In2", description="", default=0.0, update=MxNode.update_prop)
    nd_color3FA_out_out: FloatVectorProperty(name="Out", description="", subtype="COLOR", size=3, soft_min=0.0, soft_max=1.0, update=MxNode.update_prop)

    nd_color4FA_in_in1: FloatVectorProperty(name="In1", description="", subtype="COLOR", size=4, soft_min=0.0, soft_max=1.0, default=(0.0, 0.0, 0.0, 0.0), update=MxNode.update_prop)
    nd_color4FA_in_in2: FloatProperty(name="In2", description="", default=0.0, update=MxNode.update_prop)
    nd_color4FA_out_out: FloatVectorProperty(name="Out", description="", subtype="COLOR", size=4, soft_min=0.0, soft_max=1.0, update=MxNode.update_prop)

    nd_vector2FA_in_in1: FloatVectorProperty(name="In1", description="", subtype="NONE", size=2, default=(0.0, 0.0), update=MxNode.update_prop)
    nd_vector2FA_in_in2: FloatProperty(name="In2", description="", default=0.0, update=MxNode.update_prop)
    nd_vector2FA_out_out: FloatVectorProperty(name="Out", description="", subtype="NONE", size=2, update=MxNode.update_prop)

    nd_vector3FA_in_in1: FloatVectorProperty(name="In1", description="", subtype="XYZ", size=3, default=(0.0, 0.0, 0.0), update=MxNode.update_prop)
    nd_vector3FA_in_in2: FloatProperty(name="In2", description="", default=0.0, update=MxNode.update_prop)
    nd_vector3FA_out_out: FloatVectorProperty(name="Out", description="", subtype="XYZ", size=3, update=MxNode.update_prop)

    nd_vector4FA_in_in1: FloatVectorProperty(name="In1", description="", subtype="NONE", size=4, default=(0.0, 0.0, 0.0, 0.0), update=MxNode.update_prop)
    nd_vector4FA_in_in2: FloatProperty(name="In2", description="", default=0.0, update=MxNode.update_prop)
    nd_vector4FA_out_out: FloatVectorProperty(name="Out", description="", subtype="NONE", size=4, update=MxNode.update_prop)


class MxNode_STD_subtract(MxNode):
    _file_path = FILE_PATH
    _data_types = {'float': {'nd_name': 'ND_subtract_float', 'nd': None}, 'color3': {'nd_name': 'ND_subtract_color3', 'nd': None}, 'color4': {'nd_name': 'ND_subtract_color4', 'nd': None}, 'vector2': {'nd_name': 'ND_subtract_vector2', 'nd': None}, 'vector3': {'nd_name': 'ND_subtract_vector3', 'nd': None}, 'vector4': {'nd_name': 'ND_subtract_vector4', 'nd': None}, 'color3FA': {'nd_name': 'ND_subtract_color3FA', 'nd': None}, 'color4FA': {'nd_name': 'ND_subtract_color4FA', 'nd': None}, 'vector2FA': {'nd_name': 'ND_subtract_vector2FA', 'nd': None}, 'vector3FA': {'nd_name': 'ND_subtract_vector3FA', 'nd': None}, 'vector4FA': {'nd_name': 'ND_subtract_vector4FA', 'nd': None}}

    bl_label = 'Subtract'
    bl_idname = 'usdhydra.MxNode_STD_subtract'
    bl_description = ""

    category = 'math'

    data_type: EnumProperty(name="Type", description="Input Data Type", items=[('float', 'Float', 'Float'), ('color3', 'Color3', 'Color3'), ('color4', 'Color4', 'Color4'), ('vector2', 'Vector2', 'Vector2'), ('vector3', 'Vector3', 'Vector3'), ('vector4', 'Vector4', 'Vector4'), ('color3FA', 'Color3FA', 'Color3FA'), ('color4FA', 'Color4FA', 'Color4FA'), ('vector2FA', 'Vector2FA', 'Vector2FA'), ('vector3FA', 'Vector3FA', 'Vector3FA'), ('vector4FA', 'Vector4FA', 'Vector4FA')], default='color3', update=MxNode.update_data_type)

    nd_float_in_in1: FloatProperty(name="In1", description="", default=0.0, update=MxNode.update_prop)
    nd_float_in_in2: FloatProperty(name="In2", description="", default=0.0, update=MxNode.update_prop)
    nd_float_out_out: FloatProperty(name="Out", description="", update=MxNode.update_prop)

    nd_color3_in_in1: FloatVectorProperty(name="In1", description="", subtype="COLOR", size=3, soft_min=0.0, soft_max=1.0, default=(0.0, 0.0, 0.0), update=MxNode.update_prop)
    nd_color3_in_in2: FloatVectorProperty(name="In2", description="", subtype="COLOR", size=3, soft_min=0.0, soft_max=1.0, default=(0.0, 0.0, 0.0), update=MxNode.update_prop)
    nd_color3_out_out: FloatVectorProperty(name="Out", description="", subtype="COLOR", size=3, soft_min=0.0, soft_max=1.0, update=MxNode.update_prop)

    nd_color4_in_in1: FloatVectorProperty(name="In1", description="", subtype="COLOR", size=4, soft_min=0.0, soft_max=1.0, default=(0.0, 0.0, 0.0, 0.0), update=MxNode.update_prop)
    nd_color4_in_in2: FloatVectorProperty(name="In2", description="", subtype="COLOR", size=4, soft_min=0.0, soft_max=1.0, default=(0.0, 0.0, 0.0, 0.0), update=MxNode.update_prop)
    nd_color4_out_out: FloatVectorProperty(name="Out", description="", subtype="COLOR", size=4, soft_min=0.0, soft_max=1.0, update=MxNode.update_prop)

    nd_vector2_in_in1: FloatVectorProperty(name="In1", description="", subtype="NONE", size=2, default=(0.0, 0.0), update=MxNode.update_prop)
    nd_vector2_in_in2: FloatVectorProperty(name="In2", description="", subtype="NONE", size=2, default=(0.0, 0.0), update=MxNode.update_prop)
    nd_vector2_out_out: FloatVectorProperty(name="Out", description="", subtype="NONE", size=2, update=MxNode.update_prop)

    nd_vector3_in_in1: FloatVectorProperty(name="In1", description="", subtype="XYZ", size=3, default=(0.0, 0.0, 0.0), update=MxNode.update_prop)
    nd_vector3_in_in2: FloatVectorProperty(name="In2", description="", subtype="XYZ", size=3, default=(0.0, 0.0, 0.0), update=MxNode.update_prop)
    nd_vector3_out_out: FloatVectorProperty(name="Out", description="", subtype="XYZ", size=3, update=MxNode.update_prop)

    nd_vector4_in_in1: FloatVectorProperty(name="In1", description="", subtype="NONE", size=4, default=(0.0, 0.0, 0.0, 0.0), update=MxNode.update_prop)
    nd_vector4_in_in2: FloatVectorProperty(name="In2", description="", subtype="NONE", size=4, default=(0.0, 0.0, 0.0, 0.0), update=MxNode.update_prop)
    nd_vector4_out_out: FloatVectorProperty(name="Out", description="", subtype="NONE", size=4, update=MxNode.update_prop)

    nd_color3FA_in_in1: FloatVectorProperty(name="In1", description="", subtype="COLOR", size=3, soft_min=0.0, soft_max=1.0, default=(0.0, 0.0, 0.0), update=MxNode.update_prop)
    nd_color3FA_in_in2: FloatProperty(name="In2", description="", default=0.0, update=MxNode.update_prop)
    nd_color3FA_out_out: FloatVectorProperty(name="Out", description="", subtype="COLOR", size=3, soft_min=0.0, soft_max=1.0, update=MxNode.update_prop)

    nd_color4FA_in_in1: FloatVectorProperty(name="In1", description="", subtype="COLOR", size=4, soft_min=0.0, soft_max=1.0, default=(0.0, 0.0, 0.0, 0.0), update=MxNode.update_prop)
    nd_color4FA_in_in2: FloatProperty(name="In2", description="", default=0.0, update=MxNode.update_prop)
    nd_color4FA_out_out: FloatVectorProperty(name="Out", description="", subtype="COLOR", size=4, soft_min=0.0, soft_max=1.0, update=MxNode.update_prop)

    nd_vector2FA_in_in1: FloatVectorProperty(name="In1", description="", subtype="NONE", size=2, default=(0.0, 0.0), update=MxNode.update_prop)
    nd_vector2FA_in_in2: FloatProperty(name="In2", description="", default=0.0, update=MxNode.update_prop)
    nd_vector2FA_out_out: FloatVectorProperty(name="Out", description="", subtype="NONE", size=2, update=MxNode.update_prop)

    nd_vector3FA_in_in1: FloatVectorProperty(name="In1", description="", subtype="XYZ", size=3, default=(0.0, 0.0, 0.0), update=MxNode.update_prop)
    nd_vector3FA_in_in2: FloatProperty(name="In2", description="", default=0.0, update=MxNode.update_prop)
    nd_vector3FA_out_out: FloatVectorProperty(name="Out", description="", subtype="XYZ", size=3, update=MxNode.update_prop)

    nd_vector4FA_in_in1: FloatVectorProperty(name="In1", description="", subtype="NONE", size=4, default=(0.0, 0.0, 0.0, 0.0), update=MxNode.update_prop)
    nd_vector4FA_in_in2: FloatProperty(name="In2", description="", default=0.0, update=MxNode.update_prop)
    nd_vector4FA_out_out: FloatVectorProperty(name="Out", description="", subtype="NONE", size=4, update=MxNode.update_prop)


class MxNode_STD_multiply(MxNode):
    _file_path = FILE_PATH
    _data_types = {'float': {'nd_name': 'ND_multiply_float', 'nd': None}, 'color3': {'nd_name': 'ND_multiply_color3', 'nd': None}, 'color4': {'nd_name': 'ND_multiply_color4', 'nd': None}, 'vector2': {'nd_name': 'ND_multiply_vector2', 'nd': None}, 'vector3': {'nd_name': 'ND_multiply_vector3', 'nd': None}, 'vector4': {'nd_name': 'ND_multiply_vector4', 'nd': None}, 'color3FA': {'nd_name': 'ND_multiply_color3FA', 'nd': None}, 'color4FA': {'nd_name': 'ND_multiply_color4FA', 'nd': None}, 'vector2FA': {'nd_name': 'ND_multiply_vector2FA', 'nd': None}, 'vector3FA': {'nd_name': 'ND_multiply_vector3FA', 'nd': None}, 'vector4FA': {'nd_name': 'ND_multiply_vector4FA', 'nd': None}, 'surfaceshaderF': {'nd_name': 'ND_multiply_surfaceshaderF', 'nd': None}, 'displacementshaderF': {'nd_name': 'ND_multiply_displacementshaderF', 'nd': None}, 'volumeshaderF': {'nd_name': 'ND_multiply_volumeshaderF', 'nd': None}, 'surfaceshaderC': {'nd_name': 'ND_multiply_surfaceshaderC', 'nd': None}, 'volumeshaderC': {'nd_name': 'ND_multiply_volumeshaderC', 'nd': None}, 'displacementshaderV': {'nd_name': 'ND_multiply_displacementshaderV', 'nd': None}}

    bl_label = 'Multiply'
    bl_idname = 'usdhydra.MxNode_STD_multiply'
    bl_description = ""

    category = 'math'

    data_type: EnumProperty(name="Type", description="Input Data Type", items=[('float', 'Float', 'Float'), ('color3', 'Color3', 'Color3'), ('color4', 'Color4', 'Color4'), ('vector2', 'Vector2', 'Vector2'), ('vector3', 'Vector3', 'Vector3'), ('vector4', 'Vector4', 'Vector4'), ('color3FA', 'Color3FA', 'Color3FA'), ('color4FA', 'Color4FA', 'Color4FA'), ('vector2FA', 'Vector2FA', 'Vector2FA'), ('vector3FA', 'Vector3FA', 'Vector3FA'), ('vector4FA', 'Vector4FA', 'Vector4FA'), ('surfaceshaderF', 'SurfaceshaderF', 'SurfaceshaderF'), ('displacementshaderF', 'DisplacementshaderF', 'DisplacementshaderF'), ('volumeshaderF', 'VolumeshaderF', 'VolumeshaderF'), ('surfaceshaderC', 'SurfaceshaderC', 'SurfaceshaderC'), ('volumeshaderC', 'VolumeshaderC', 'VolumeshaderC'), ('displacementshaderV', 'DisplacementshaderV', 'DisplacementshaderV')], default='color3', update=MxNode.update_data_type)

    nd_float_in_in1: FloatProperty(name="In1", description="", default=0.0, update=MxNode.update_prop)
    nd_float_in_in2: FloatProperty(name="In2", description="", default=1.0, update=MxNode.update_prop)
    nd_float_out_out: FloatProperty(name="Out", description="", update=MxNode.update_prop)

    nd_color3_in_in1: FloatVectorProperty(name="In1", description="", subtype="COLOR", size=3, soft_min=0.0, soft_max=1.0, default=(0.0, 0.0, 0.0), update=MxNode.update_prop)
    nd_color3_in_in2: FloatVectorProperty(name="In2", description="", subtype="COLOR", size=3, soft_min=0.0, soft_max=1.0, default=(1.0, 1.0, 1.0), update=MxNode.update_prop)
    nd_color3_out_out: FloatVectorProperty(name="Out", description="", subtype="COLOR", size=3, soft_min=0.0, soft_max=1.0, update=MxNode.update_prop)

    nd_color4_in_in1: FloatVectorProperty(name="In1", description="", subtype="COLOR", size=4, soft_min=0.0, soft_max=1.0, default=(0.0, 0.0, 0.0, 0.0), update=MxNode.update_prop)
    nd_color4_in_in2: FloatVectorProperty(name="In2", description="", subtype="COLOR", size=4, soft_min=0.0, soft_max=1.0, default=(1.0, 1.0, 1.0, 1.0), update=MxNode.update_prop)
    nd_color4_out_out: FloatVectorProperty(name="Out", description="", subtype="COLOR", size=4, soft_min=0.0, soft_max=1.0, update=MxNode.update_prop)

    nd_vector2_in_in1: FloatVectorProperty(name="In1", description="", subtype="NONE", size=2, default=(0.0, 0.0), update=MxNode.update_prop)
    nd_vector2_in_in2: FloatVectorProperty(name="In2", description="", subtype="NONE", size=2, default=(1.0, 1.0), update=MxNode.update_prop)
    nd_vector2_out_out: FloatVectorProperty(name="Out", description="", subtype="NONE", size=2, update=MxNode.update_prop)

    nd_vector3_in_in1: FloatVectorProperty(name="In1", description="", subtype="XYZ", size=3, default=(0.0, 0.0, 0.0), update=MxNode.update_prop)
    nd_vector3_in_in2: FloatVectorProperty(name="In2", description="", subtype="XYZ", size=3, default=(1.0, 1.0, 1.0), update=MxNode.update_prop)
    nd_vector3_out_out: FloatVectorProperty(name="Out", description="", subtype="XYZ", size=3, update=MxNode.update_prop)

    nd_vector4_in_in1: FloatVectorProperty(name="In1", description="", subtype="NONE", size=4, default=(0.0, 0.0, 0.0, 0.0), update=MxNode.update_prop)
    nd_vector4_in_in2: FloatVectorProperty(name="In2", description="", subtype="NONE", size=4, default=(1.0, 1.0, 1.0, 1.0), update=MxNode.update_prop)
    nd_vector4_out_out: FloatVectorProperty(name="Out", description="", subtype="NONE", size=4, update=MxNode.update_prop)

    nd_color3FA_in_in1: FloatVectorProperty(name="In1", description="", subtype="COLOR", size=3, soft_min=0.0, soft_max=1.0, default=(0.0, 0.0, 0.0), update=MxNode.update_prop)
    nd_color3FA_in_in2: FloatProperty(name="In2", description="", default=1.0, update=MxNode.update_prop)
    nd_color3FA_out_out: FloatVectorProperty(name="Out", description="", subtype="COLOR", size=3, soft_min=0.0, soft_max=1.0, update=MxNode.update_prop)

    nd_color4FA_in_in1: FloatVectorProperty(name="In1", description="", subtype="COLOR", size=4, soft_min=0.0, soft_max=1.0, default=(0.0, 0.0, 0.0, 0.0), update=MxNode.update_prop)
    nd_color4FA_in_in2: FloatProperty(name="In2", description="", default=1.0, update=MxNode.update_prop)
    nd_color4FA_out_out: FloatVectorProperty(name="Out", description="", subtype="COLOR", size=4, soft_min=0.0, soft_max=1.0, update=MxNode.update_prop)

    nd_vector2FA_in_in1: FloatVectorProperty(name="In1", description="", subtype="NONE", size=2, default=(0.0, 0.0), update=MxNode.update_prop)
    nd_vector2FA_in_in2: FloatProperty(name="In2", description="", default=1.0, update=MxNode.update_prop)
    nd_vector2FA_out_out: FloatVectorProperty(name="Out", description="", subtype="NONE", size=2, update=MxNode.update_prop)

    nd_vector3FA_in_in1: FloatVectorProperty(name="In1", description="", subtype="XYZ", size=3, default=(0.0, 0.0, 0.0), update=MxNode.update_prop)
    nd_vector3FA_in_in2: FloatProperty(name="In2", description="", default=1.0, update=MxNode.update_prop)
    nd_vector3FA_out_out: FloatVectorProperty(name="Out", description="", subtype="XYZ", size=3, update=MxNode.update_prop)

    nd_vector4FA_in_in1: FloatVectorProperty(name="In1", description="", subtype="NONE", size=4, default=(0.0, 0.0, 0.0, 0.0), update=MxNode.update_prop)
    nd_vector4FA_in_in2: FloatProperty(name="In2", description="", default=1.0, update=MxNode.update_prop)
    nd_vector4FA_out_out: FloatVectorProperty(name="Out", description="", subtype="NONE", size=4, update=MxNode.update_prop)

    nd_surfaceshaderF_in_in1: StringProperty(name="In1", description="", default="", update=MxNode.update_prop)
    nd_surfaceshaderF_in_in2: FloatProperty(name="In2", description="", default=1.0, update=MxNode.update_prop)
    nd_surfaceshaderF_out_out: StringProperty(name="Out", description="", update=MxNode.update_prop)

    nd_displacementshaderF_in_in1: StringProperty(name="In1", description="", default="", update=MxNode.update_prop)
    nd_displacementshaderF_in_in2: FloatProperty(name="In2", description="", default=1.0, update=MxNode.update_prop)
    nd_displacementshaderF_out_out: StringProperty(name="Out", description="", update=MxNode.update_prop)

    nd_volumeshaderF_in_in1: StringProperty(name="In1", description="", default="", update=MxNode.update_prop)
    nd_volumeshaderF_in_in2: FloatProperty(name="In2", description="", default=1.0, update=MxNode.update_prop)
    nd_volumeshaderF_out_out: StringProperty(name="Out", description="", update=MxNode.update_prop)

    nd_surfaceshaderC_in_in1: StringProperty(name="In1", description="", default="", update=MxNode.update_prop)
    nd_surfaceshaderC_in_in2: FloatVectorProperty(name="In2", description="", subtype="COLOR", size=3, soft_min=0.0, soft_max=1.0, default=(1.0, 1.0, 1.0), update=MxNode.update_prop)
    nd_surfaceshaderC_out_out: StringProperty(name="Out", description="", update=MxNode.update_prop)

    nd_volumeshaderC_in_in1: StringProperty(name="In1", description="", default="", update=MxNode.update_prop)
    nd_volumeshaderC_in_in2: FloatVectorProperty(name="In2", description="", subtype="COLOR", size=3, soft_min=0.0, soft_max=1.0, default=(1.0, 1.0, 1.0), update=MxNode.update_prop)
    nd_volumeshaderC_out_out: StringProperty(name="Out", description="", update=MxNode.update_prop)

    nd_displacementshaderV_in_in1: StringProperty(name="In1", description="", default="", update=MxNode.update_prop)
    nd_displacementshaderV_in_in2: FloatVectorProperty(name="In2", description="", subtype="XYZ", size=3, default=(1.0, 1.0, 1.0), update=MxNode.update_prop)
    nd_displacementshaderV_out_out: StringProperty(name="Out", description="", update=MxNode.update_prop)


class MxNode_STD_divide(MxNode):
    _file_path = FILE_PATH
    _data_types = {'float': {'nd_name': 'ND_divide_float', 'nd': None}, 'color3': {'nd_name': 'ND_divide_color3', 'nd': None}, 'color4': {'nd_name': 'ND_divide_color4', 'nd': None}, 'vector2': {'nd_name': 'ND_divide_vector2', 'nd': None}, 'vector3': {'nd_name': 'ND_divide_vector3', 'nd': None}, 'vector4': {'nd_name': 'ND_divide_vector4', 'nd': None}, 'color3FA': {'nd_name': 'ND_divide_color3FA', 'nd': None}, 'color4FA': {'nd_name': 'ND_divide_color4FA', 'nd': None}, 'vector2FA': {'nd_name': 'ND_divide_vector2FA', 'nd': None}, 'vector3FA': {'nd_name': 'ND_divide_vector3FA', 'nd': None}, 'vector4FA': {'nd_name': 'ND_divide_vector4FA', 'nd': None}}

    bl_label = 'Divide'
    bl_idname = 'usdhydra.MxNode_STD_divide'
    bl_description = ""

    category = 'math'

    data_type: EnumProperty(name="Type", description="Input Data Type", items=[('float', 'Float', 'Float'), ('color3', 'Color3', 'Color3'), ('color4', 'Color4', 'Color4'), ('vector2', 'Vector2', 'Vector2'), ('vector3', 'Vector3', 'Vector3'), ('vector4', 'Vector4', 'Vector4'), ('color3FA', 'Color3FA', 'Color3FA'), ('color4FA', 'Color4FA', 'Color4FA'), ('vector2FA', 'Vector2FA', 'Vector2FA'), ('vector3FA', 'Vector3FA', 'Vector3FA'), ('vector4FA', 'Vector4FA', 'Vector4FA')], default='color3', update=MxNode.update_data_type)

    nd_float_in_in1: FloatProperty(name="In1", description="", default=0.0, update=MxNode.update_prop)
    nd_float_in_in2: FloatProperty(name="In2", description="", default=1.0, update=MxNode.update_prop)
    nd_float_out_out: FloatProperty(name="Out", description="", update=MxNode.update_prop)

    nd_color3_in_in1: FloatVectorProperty(name="In1", description="", subtype="COLOR", size=3, soft_min=0.0, soft_max=1.0, default=(0.0, 0.0, 0.0), update=MxNode.update_prop)
    nd_color3_in_in2: FloatVectorProperty(name="In2", description="", subtype="COLOR", size=3, soft_min=0.0, soft_max=1.0, default=(1.0, 1.0, 1.0), update=MxNode.update_prop)
    nd_color3_out_out: FloatVectorProperty(name="Out", description="", subtype="COLOR", size=3, soft_min=0.0, soft_max=1.0, update=MxNode.update_prop)

    nd_color4_in_in1: FloatVectorProperty(name="In1", description="", subtype="COLOR", size=4, soft_min=0.0, soft_max=1.0, default=(0.0, 0.0, 0.0, 0.0), update=MxNode.update_prop)
    nd_color4_in_in2: FloatVectorProperty(name="In2", description="", subtype="COLOR", size=4, soft_min=0.0, soft_max=1.0, default=(1.0, 1.0, 1.0, 1.0), update=MxNode.update_prop)
    nd_color4_out_out: FloatVectorProperty(name="Out", description="", subtype="COLOR", size=4, soft_min=0.0, soft_max=1.0, update=MxNode.update_prop)

    nd_vector2_in_in1: FloatVectorProperty(name="In1", description="", subtype="NONE", size=2, default=(0.0, 0.0), update=MxNode.update_prop)
    nd_vector2_in_in2: FloatVectorProperty(name="In2", description="", subtype="NONE", size=2, default=(1.0, 1.0), update=MxNode.update_prop)
    nd_vector2_out_out: FloatVectorProperty(name="Out", description="", subtype="NONE", size=2, update=MxNode.update_prop)

    nd_vector3_in_in1: FloatVectorProperty(name="In1", description="", subtype="XYZ", size=3, default=(0.0, 0.0, 0.0), update=MxNode.update_prop)
    nd_vector3_in_in2: FloatVectorProperty(name="In2", description="", subtype="XYZ", size=3, default=(1.0, 1.0, 1.0), update=MxNode.update_prop)
    nd_vector3_out_out: FloatVectorProperty(name="Out", description="", subtype="XYZ", size=3, update=MxNode.update_prop)

    nd_vector4_in_in1: FloatVectorProperty(name="In1", description="", subtype="NONE", size=4, default=(0.0, 0.0, 0.0, 0.0), update=MxNode.update_prop)
    nd_vector4_in_in2: FloatVectorProperty(name="In2", description="", subtype="NONE", size=4, default=(1.0, 1.0, 1.0, 1.0), update=MxNode.update_prop)
    nd_vector4_out_out: FloatVectorProperty(name="Out", description="", subtype="NONE", size=4, update=MxNode.update_prop)

    nd_color3FA_in_in1: FloatVectorProperty(name="In1", description="", subtype="COLOR", size=3, soft_min=0.0, soft_max=1.0, default=(0.0, 0.0, 0.0), update=MxNode.update_prop)
    nd_color3FA_in_in2: FloatProperty(name="In2", description="", default=1.0, update=MxNode.update_prop)
    nd_color3FA_out_out: FloatVectorProperty(name="Out", description="", subtype="COLOR", size=3, soft_min=0.0, soft_max=1.0, update=MxNode.update_prop)

    nd_color4FA_in_in1: FloatVectorProperty(name="In1", description="", subtype="COLOR", size=4, soft_min=0.0, soft_max=1.0, default=(0.0, 0.0, 0.0, 0.0), update=MxNode.update_prop)
    nd_color4FA_in_in2: FloatProperty(name="In2", description="", default=1.0, update=MxNode.update_prop)
    nd_color4FA_out_out: FloatVectorProperty(name="Out", description="", subtype="COLOR", size=4, soft_min=0.0, soft_max=1.0, update=MxNode.update_prop)

    nd_vector2FA_in_in1: FloatVectorProperty(name="In1", description="", subtype="NONE", size=2, default=(0.0, 0.0), update=MxNode.update_prop)
    nd_vector2FA_in_in2: FloatProperty(name="In2", description="", default=1.0, update=MxNode.update_prop)
    nd_vector2FA_out_out: FloatVectorProperty(name="Out", description="", subtype="NONE", size=2, update=MxNode.update_prop)

    nd_vector3FA_in_in1: FloatVectorProperty(name="In1", description="", subtype="XYZ", size=3, default=(0.0, 0.0, 0.0), update=MxNode.update_prop)
    nd_vector3FA_in_in2: FloatProperty(name="In2", description="", default=1.0, update=MxNode.update_prop)
    nd_vector3FA_out_out: FloatVectorProperty(name="Out", description="", subtype="XYZ", size=3, update=MxNode.update_prop)

    nd_vector4FA_in_in1: FloatVectorProperty(name="In1", description="", subtype="NONE", size=4, default=(0.0, 0.0, 0.0, 0.0), update=MxNode.update_prop)
    nd_vector4FA_in_in2: FloatProperty(name="In2", description="", default=1.0, update=MxNode.update_prop)
    nd_vector4FA_out_out: FloatVectorProperty(name="Out", description="", subtype="NONE", size=4, update=MxNode.update_prop)


class MxNode_STD_modulo(MxNode):
    _file_path = FILE_PATH
    _data_types = {'float': {'nd_name': 'ND_modulo_float', 'nd': None}, 'color3': {'nd_name': 'ND_modulo_color3', 'nd': None}, 'color4': {'nd_name': 'ND_modulo_color4', 'nd': None}, 'vector2': {'nd_name': 'ND_modulo_vector2', 'nd': None}, 'vector3': {'nd_name': 'ND_modulo_vector3', 'nd': None}, 'vector4': {'nd_name': 'ND_modulo_vector4', 'nd': None}, 'color3FA': {'nd_name': 'ND_modulo_color3FA', 'nd': None}, 'color4FA': {'nd_name': 'ND_modulo_color4FA', 'nd': None}, 'vector2FA': {'nd_name': 'ND_modulo_vector2FA', 'nd': None}, 'vector3FA': {'nd_name': 'ND_modulo_vector3FA', 'nd': None}, 'vector4FA': {'nd_name': 'ND_modulo_vector4FA', 'nd': None}}

    bl_label = 'Modulo'
    bl_idname = 'usdhydra.MxNode_STD_modulo'
    bl_description = ""

    category = 'math'

    data_type: EnumProperty(name="Type", description="Input Data Type", items=[('float', 'Float', 'Float'), ('color3', 'Color3', 'Color3'), ('color4', 'Color4', 'Color4'), ('vector2', 'Vector2', 'Vector2'), ('vector3', 'Vector3', 'Vector3'), ('vector4', 'Vector4', 'Vector4'), ('color3FA', 'Color3FA', 'Color3FA'), ('color4FA', 'Color4FA', 'Color4FA'), ('vector2FA', 'Vector2FA', 'Vector2FA'), ('vector3FA', 'Vector3FA', 'Vector3FA'), ('vector4FA', 'Vector4FA', 'Vector4FA')], default='color3', update=MxNode.update_data_type)

    nd_float_in_in1: FloatProperty(name="In1", description="", default=0.0, update=MxNode.update_prop)
    nd_float_in_in2: FloatProperty(name="In2", description="", default=1.0, update=MxNode.update_prop)
    nd_float_out_out: FloatProperty(name="Out", description="", update=MxNode.update_prop)

    nd_color3_in_in1: FloatVectorProperty(name="In1", description="", subtype="COLOR", size=3, soft_min=0.0, soft_max=1.0, default=(0.0, 0.0, 0.0), update=MxNode.update_prop)
    nd_color3_in_in2: FloatVectorProperty(name="In2", description="", subtype="COLOR", size=3, soft_min=0.0, soft_max=1.0, default=(1.0, 1.0, 1.0), update=MxNode.update_prop)
    nd_color3_out_out: FloatVectorProperty(name="Out", description="", subtype="COLOR", size=3, soft_min=0.0, soft_max=1.0, update=MxNode.update_prop)

    nd_color4_in_in1: FloatVectorProperty(name="In1", description="", subtype="COLOR", size=4, soft_min=0.0, soft_max=1.0, default=(0.0, 0.0, 0.0, 0.0), update=MxNode.update_prop)
    nd_color4_in_in2: FloatVectorProperty(name="In2", description="", subtype="COLOR", size=4, soft_min=0.0, soft_max=1.0, default=(1.0, 1.0, 1.0, 1.0), update=MxNode.update_prop)
    nd_color4_out_out: FloatVectorProperty(name="Out", description="", subtype="COLOR", size=4, soft_min=0.0, soft_max=1.0, update=MxNode.update_prop)

    nd_vector2_in_in1: FloatVectorProperty(name="In1", description="", subtype="NONE", size=2, default=(0.0, 0.0), update=MxNode.update_prop)
    nd_vector2_in_in2: FloatVectorProperty(name="In2", description="", subtype="NONE", size=2, default=(1.0, 1.0), update=MxNode.update_prop)
    nd_vector2_out_out: FloatVectorProperty(name="Out", description="", subtype="NONE", size=2, update=MxNode.update_prop)

    nd_vector3_in_in1: FloatVectorProperty(name="In1", description="", subtype="XYZ", size=3, default=(0.0, 0.0, 0.0), update=MxNode.update_prop)
    nd_vector3_in_in2: FloatVectorProperty(name="In2", description="", subtype="XYZ", size=3, default=(1.0, 1.0, 1.0), update=MxNode.update_prop)
    nd_vector3_out_out: FloatVectorProperty(name="Out", description="", subtype="XYZ", size=3, update=MxNode.update_prop)

    nd_vector4_in_in1: FloatVectorProperty(name="In1", description="", subtype="NONE", size=4, default=(0.0, 0.0, 0.0, 0.0), update=MxNode.update_prop)
    nd_vector4_in_in2: FloatVectorProperty(name="In2", description="", subtype="NONE", size=4, default=(1.0, 1.0, 1.0, 1.0), update=MxNode.update_prop)
    nd_vector4_out_out: FloatVectorProperty(name="Out", description="", subtype="NONE", size=4, update=MxNode.update_prop)

    nd_color3FA_in_in1: FloatVectorProperty(name="In1", description="", subtype="COLOR", size=3, soft_min=0.0, soft_max=1.0, default=(0.0, 0.0, 0.0), update=MxNode.update_prop)
    nd_color3FA_in_in2: FloatProperty(name="In2", description="", default=1.0, update=MxNode.update_prop)
    nd_color3FA_out_out: FloatVectorProperty(name="Out", description="", subtype="COLOR", size=3, soft_min=0.0, soft_max=1.0, update=MxNode.update_prop)

    nd_color4FA_in_in1: FloatVectorProperty(name="In1", description="", subtype="COLOR", size=4, soft_min=0.0, soft_max=1.0, default=(0.0, 0.0, 0.0, 0.0), update=MxNode.update_prop)
    nd_color4FA_in_in2: FloatProperty(name="In2", description="", default=1.0, update=MxNode.update_prop)
    nd_color4FA_out_out: FloatVectorProperty(name="Out", description="", subtype="COLOR", size=4, soft_min=0.0, soft_max=1.0, update=MxNode.update_prop)

    nd_vector2FA_in_in1: FloatVectorProperty(name="In1", description="", subtype="NONE", size=2, default=(0.0, 0.0), update=MxNode.update_prop)
    nd_vector2FA_in_in2: FloatProperty(name="In2", description="", default=1.0, update=MxNode.update_prop)
    nd_vector2FA_out_out: FloatVectorProperty(name="Out", description="", subtype="NONE", size=2, update=MxNode.update_prop)

    nd_vector3FA_in_in1: FloatVectorProperty(name="In1", description="", subtype="XYZ", size=3, default=(0.0, 0.0, 0.0), update=MxNode.update_prop)
    nd_vector3FA_in_in2: FloatProperty(name="In2", description="", default=1.0, update=MxNode.update_prop)
    nd_vector3FA_out_out: FloatVectorProperty(name="Out", description="", subtype="XYZ", size=3, update=MxNode.update_prop)

    nd_vector4FA_in_in1: FloatVectorProperty(name="In1", description="", subtype="NONE", size=4, default=(0.0, 0.0, 0.0, 0.0), update=MxNode.update_prop)
    nd_vector4FA_in_in2: FloatProperty(name="In2", description="", default=1.0, update=MxNode.update_prop)
    nd_vector4FA_out_out: FloatVectorProperty(name="Out", description="", subtype="NONE", size=4, update=MxNode.update_prop)


class MxNode_STD_invert(MxNode):
    _file_path = FILE_PATH
    _data_types = {'float': {'nd_name': 'ND_invert_float', 'nd': None}, 'color3': {'nd_name': 'ND_invert_color3', 'nd': None}, 'color4': {'nd_name': 'ND_invert_color4', 'nd': None}, 'vector2': {'nd_name': 'ND_invert_vector2', 'nd': None}, 'vector3': {'nd_name': 'ND_invert_vector3', 'nd': None}, 'vector4': {'nd_name': 'ND_invert_vector4', 'nd': None}, 'color3FA': {'nd_name': 'ND_invert_color3FA', 'nd': None}, 'color4FA': {'nd_name': 'ND_invert_color4FA', 'nd': None}, 'vector2FA': {'nd_name': 'ND_invert_vector2FA', 'nd': None}, 'vector3FA': {'nd_name': 'ND_invert_vector3FA', 'nd': None}, 'vector4FA': {'nd_name': 'ND_invert_vector4FA', 'nd': None}}

    bl_label = 'Invert'
    bl_idname = 'usdhydra.MxNode_STD_invert'
    bl_description = ""

    category = 'math'

    data_type: EnumProperty(name="Type", description="Input Data Type", items=[('float', 'Float', 'Float'), ('color3', 'Color3', 'Color3'), ('color4', 'Color4', 'Color4'), ('vector2', 'Vector2', 'Vector2'), ('vector3', 'Vector3', 'Vector3'), ('vector4', 'Vector4', 'Vector4'), ('color3FA', 'Color3FA', 'Color3FA'), ('color4FA', 'Color4FA', 'Color4FA'), ('vector2FA', 'Vector2FA', 'Vector2FA'), ('vector3FA', 'Vector3FA', 'Vector3FA'), ('vector4FA', 'Vector4FA', 'Vector4FA')], default='color3', update=MxNode.update_data_type)

    nd_float_in_in: FloatProperty(name="In", description="", default=0.0, update=MxNode.update_prop)
    nd_float_in_amount: FloatProperty(name="Amount", description="", default=1.0, update=MxNode.update_prop)
    nd_float_out_out: FloatProperty(name="Out", description="", update=MxNode.update_prop)

    nd_color3_in_in: FloatVectorProperty(name="In", description="", subtype="COLOR", size=3, soft_min=0.0, soft_max=1.0, default=(0.0, 0.0, 0.0), update=MxNode.update_prop)
    nd_color3_in_amount: FloatVectorProperty(name="Amount", description="", subtype="COLOR", size=3, soft_min=0.0, soft_max=1.0, default=(1.0, 1.0, 1.0), update=MxNode.update_prop)
    nd_color3_out_out: FloatVectorProperty(name="Out", description="", subtype="COLOR", size=3, soft_min=0.0, soft_max=1.0, update=MxNode.update_prop)

    nd_color4_in_in: FloatVectorProperty(name="In", description="", subtype="COLOR", size=4, soft_min=0.0, soft_max=1.0, default=(0.0, 0.0, 0.0, 0.0), update=MxNode.update_prop)
    nd_color4_in_amount: FloatVectorProperty(name="Amount", description="", subtype="COLOR", size=4, soft_min=0.0, soft_max=1.0, default=(1.0, 1.0, 1.0, 1.0), update=MxNode.update_prop)
    nd_color4_out_out: FloatVectorProperty(name="Out", description="", subtype="COLOR", size=4, soft_min=0.0, soft_max=1.0, update=MxNode.update_prop)

    nd_vector2_in_in: FloatVectorProperty(name="In", description="", subtype="NONE", size=2, default=(0.0, 0.0), update=MxNode.update_prop)
    nd_vector2_in_amount: FloatVectorProperty(name="Amount", description="", subtype="NONE", size=2, default=(1.0, 1.0), update=MxNode.update_prop)
    nd_vector2_out_out: FloatVectorProperty(name="Out", description="", subtype="NONE", size=2, update=MxNode.update_prop)

    nd_vector3_in_in: FloatVectorProperty(name="In", description="", subtype="XYZ", size=3, default=(0.0, 0.0, 0.0), update=MxNode.update_prop)
    nd_vector3_in_amount: FloatVectorProperty(name="Amount", description="", subtype="XYZ", size=3, default=(1.0, 1.0, 1.0), update=MxNode.update_prop)
    nd_vector3_out_out: FloatVectorProperty(name="Out", description="", subtype="XYZ", size=3, update=MxNode.update_prop)

    nd_vector4_in_in: FloatVectorProperty(name="In", description="", subtype="NONE", size=4, default=(0.0, 0.0, 0.0, 0.0), update=MxNode.update_prop)
    nd_vector4_in_amount: FloatVectorProperty(name="Amount", description="", subtype="NONE", size=4, default=(1.0, 1.0, 1.0, 1.0), update=MxNode.update_prop)
    nd_vector4_out_out: FloatVectorProperty(name="Out", description="", subtype="NONE", size=4, update=MxNode.update_prop)

    nd_color3FA_in_in: FloatVectorProperty(name="In", description="", subtype="COLOR", size=3, soft_min=0.0, soft_max=1.0, default=(0.0, 0.0, 0.0), update=MxNode.update_prop)
    nd_color3FA_in_amount: FloatProperty(name="Amount", description="", default=1.0, update=MxNode.update_prop)
    nd_color3FA_out_out: FloatVectorProperty(name="Out", description="", subtype="COLOR", size=3, soft_min=0.0, soft_max=1.0, update=MxNode.update_prop)

    nd_color4FA_in_in: FloatVectorProperty(name="In", description="", subtype="COLOR", size=4, soft_min=0.0, soft_max=1.0, default=(0.0, 0.0, 0.0, 0.0), update=MxNode.update_prop)
    nd_color4FA_in_amount: FloatProperty(name="Amount", description="", default=1.0, update=MxNode.update_prop)
    nd_color4FA_out_out: FloatVectorProperty(name="Out", description="", subtype="COLOR", size=4, soft_min=0.0, soft_max=1.0, update=MxNode.update_prop)

    nd_vector2FA_in_in: FloatVectorProperty(name="In", description="", subtype="NONE", size=2, default=(0.0, 0.0), update=MxNode.update_prop)
    nd_vector2FA_in_amount: FloatProperty(name="Amount", description="", default=1.0, update=MxNode.update_prop)
    nd_vector2FA_out_out: FloatVectorProperty(name="Out", description="", subtype="NONE", size=2, update=MxNode.update_prop)

    nd_vector3FA_in_in: FloatVectorProperty(name="In", description="", subtype="XYZ", size=3, default=(0.0, 0.0, 0.0), update=MxNode.update_prop)
    nd_vector3FA_in_amount: FloatProperty(name="Amount", description="", default=1.0, update=MxNode.update_prop)
    nd_vector3FA_out_out: FloatVectorProperty(name="Out", description="", subtype="XYZ", size=3, update=MxNode.update_prop)

    nd_vector4FA_in_in: FloatVectorProperty(name="In", description="", subtype="NONE", size=4, default=(0.0, 0.0, 0.0, 0.0), update=MxNode.update_prop)
    nd_vector4FA_in_amount: FloatProperty(name="Amount", description="", default=1.0, update=MxNode.update_prop)
    nd_vector4FA_out_out: FloatVectorProperty(name="Out", description="", subtype="NONE", size=4, update=MxNode.update_prop)


class MxNode_STD_absval(MxNode):
    _file_path = FILE_PATH
    _data_types = {'float': {'nd_name': 'ND_absval_float', 'nd': None}, 'color3': {'nd_name': 'ND_absval_color3', 'nd': None}, 'color4': {'nd_name': 'ND_absval_color4', 'nd': None}, 'vector2': {'nd_name': 'ND_absval_vector2', 'nd': None}, 'vector3': {'nd_name': 'ND_absval_vector3', 'nd': None}, 'vector4': {'nd_name': 'ND_absval_vector4', 'nd': None}}

    bl_label = 'Absval'
    bl_idname = 'usdhydra.MxNode_STD_absval'
    bl_description = ""

    category = 'math'

    data_type: EnumProperty(name="Type", description="Input Data Type", items=[('float', 'Float', 'Float'), ('color3', 'Color3', 'Color3'), ('color4', 'Color4', 'Color4'), ('vector2', 'Vector2', 'Vector2'), ('vector3', 'Vector3', 'Vector3'), ('vector4', 'Vector4', 'Vector4')], default='color3', update=MxNode.update_data_type)

    nd_float_in_in: FloatProperty(name="In", description="", default=0.0, update=MxNode.update_prop)
    nd_float_out_out: FloatProperty(name="Out", description="", update=MxNode.update_prop)

    nd_color3_in_in: FloatVectorProperty(name="In", description="", subtype="COLOR", size=3, soft_min=0.0, soft_max=1.0, default=(0.0, 0.0, 0.0), update=MxNode.update_prop)
    nd_color3_out_out: FloatVectorProperty(name="Out", description="", subtype="COLOR", size=3, soft_min=0.0, soft_max=1.0, update=MxNode.update_prop)

    nd_color4_in_in: FloatVectorProperty(name="In", description="", subtype="COLOR", size=4, soft_min=0.0, soft_max=1.0, default=(0.0, 0.0, 0.0, 0.0), update=MxNode.update_prop)
    nd_color4_out_out: FloatVectorProperty(name="Out", description="", subtype="COLOR", size=4, soft_min=0.0, soft_max=1.0, update=MxNode.update_prop)

    nd_vector2_in_in: FloatVectorProperty(name="In", description="", subtype="NONE", size=2, default=(0.0, 0.0), update=MxNode.update_prop)
    nd_vector2_out_out: FloatVectorProperty(name="Out", description="", subtype="NONE", size=2, update=MxNode.update_prop)

    nd_vector3_in_in: FloatVectorProperty(name="In", description="", subtype="XYZ", size=3, default=(0.0, 0.0, 0.0), update=MxNode.update_prop)
    nd_vector3_out_out: FloatVectorProperty(name="Out", description="", subtype="XYZ", size=3, update=MxNode.update_prop)

    nd_vector4_in_in: FloatVectorProperty(name="In", description="", subtype="NONE", size=4, default=(0.0, 0.0, 0.0, 0.0), update=MxNode.update_prop)
    nd_vector4_out_out: FloatVectorProperty(name="Out", description="", subtype="NONE", size=4, update=MxNode.update_prop)


class MxNode_STD_floor(MxNode):
    _file_path = FILE_PATH
    _data_types = {'float': {'nd_name': 'ND_floor_float', 'nd': None}, 'color3': {'nd_name': 'ND_floor_color3', 'nd': None}, 'color4': {'nd_name': 'ND_floor_color4', 'nd': None}, 'vector2': {'nd_name': 'ND_floor_vector2', 'nd': None}, 'vector3': {'nd_name': 'ND_floor_vector3', 'nd': None}, 'vector4': {'nd_name': 'ND_floor_vector4', 'nd': None}}

    bl_label = 'Floor'
    bl_idname = 'usdhydra.MxNode_STD_floor'
    bl_description = ""

    category = 'math'

    data_type: EnumProperty(name="Type", description="Input Data Type", items=[('float', 'Float', 'Float'), ('color3', 'Color3', 'Color3'), ('color4', 'Color4', 'Color4'), ('vector2', 'Vector2', 'Vector2'), ('vector3', 'Vector3', 'Vector3'), ('vector4', 'Vector4', 'Vector4')], default='color3', update=MxNode.update_data_type)

    nd_float_in_in: FloatProperty(name="In", description="", default=0.0, update=MxNode.update_prop)
    nd_float_out_out: FloatProperty(name="Out", description="", update=MxNode.update_prop)

    nd_color3_in_in: FloatVectorProperty(name="In", description="", subtype="COLOR", size=3, soft_min=0.0, soft_max=1.0, default=(0.0, 0.0, 0.0), update=MxNode.update_prop)
    nd_color3_out_out: FloatVectorProperty(name="Out", description="", subtype="COLOR", size=3, soft_min=0.0, soft_max=1.0, update=MxNode.update_prop)

    nd_color4_in_in: FloatVectorProperty(name="In", description="", subtype="COLOR", size=4, soft_min=0.0, soft_max=1.0, default=(0.0, 0.0, 0.0, 0.0), update=MxNode.update_prop)
    nd_color4_out_out: FloatVectorProperty(name="Out", description="", subtype="COLOR", size=4, soft_min=0.0, soft_max=1.0, update=MxNode.update_prop)

    nd_vector2_in_in: FloatVectorProperty(name="In", description="", subtype="NONE", size=2, default=(0.0, 0.0), update=MxNode.update_prop)
    nd_vector2_out_out: FloatVectorProperty(name="Out", description="", subtype="NONE", size=2, update=MxNode.update_prop)

    nd_vector3_in_in: FloatVectorProperty(name="In", description="", subtype="XYZ", size=3, default=(0.0, 0.0, 0.0), update=MxNode.update_prop)
    nd_vector3_out_out: FloatVectorProperty(name="Out", description="", subtype="XYZ", size=3, update=MxNode.update_prop)

    nd_vector4_in_in: FloatVectorProperty(name="In", description="", subtype="NONE", size=4, default=(0.0, 0.0, 0.0, 0.0), update=MxNode.update_prop)
    nd_vector4_out_out: FloatVectorProperty(name="Out", description="", subtype="NONE", size=4, update=MxNode.update_prop)


class MxNode_STD_ceil(MxNode):
    _file_path = FILE_PATH
    _data_types = {'float': {'nd_name': 'ND_ceil_float', 'nd': None}, 'color3': {'nd_name': 'ND_ceil_color3', 'nd': None}, 'color4': {'nd_name': 'ND_ceil_color4', 'nd': None}, 'vector2': {'nd_name': 'ND_ceil_vector2', 'nd': None}, 'vector3': {'nd_name': 'ND_ceil_vector3', 'nd': None}, 'vector4': {'nd_name': 'ND_ceil_vector4', 'nd': None}}

    bl_label = 'Ceil'
    bl_idname = 'usdhydra.MxNode_STD_ceil'
    bl_description = ""

    category = 'math'

    data_type: EnumProperty(name="Type", description="Input Data Type", items=[('float', 'Float', 'Float'), ('color3', 'Color3', 'Color3'), ('color4', 'Color4', 'Color4'), ('vector2', 'Vector2', 'Vector2'), ('vector3', 'Vector3', 'Vector3'), ('vector4', 'Vector4', 'Vector4')], default='color3', update=MxNode.update_data_type)

    nd_float_in_in: FloatProperty(name="In", description="", default=0.0, update=MxNode.update_prop)
    nd_float_out_out: FloatProperty(name="Out", description="", update=MxNode.update_prop)

    nd_color3_in_in: FloatVectorProperty(name="In", description="", subtype="COLOR", size=3, soft_min=0.0, soft_max=1.0, default=(0.0, 0.0, 0.0), update=MxNode.update_prop)
    nd_color3_out_out: FloatVectorProperty(name="Out", description="", subtype="COLOR", size=3, soft_min=0.0, soft_max=1.0, update=MxNode.update_prop)

    nd_color4_in_in: FloatVectorProperty(name="In", description="", subtype="COLOR", size=4, soft_min=0.0, soft_max=1.0, default=(0.0, 0.0, 0.0, 0.0), update=MxNode.update_prop)
    nd_color4_out_out: FloatVectorProperty(name="Out", description="", subtype="COLOR", size=4, soft_min=0.0, soft_max=1.0, update=MxNode.update_prop)

    nd_vector2_in_in: FloatVectorProperty(name="In", description="", subtype="NONE", size=2, default=(0.0, 0.0), update=MxNode.update_prop)
    nd_vector2_out_out: FloatVectorProperty(name="Out", description="", subtype="NONE", size=2, update=MxNode.update_prop)

    nd_vector3_in_in: FloatVectorProperty(name="In", description="", subtype="XYZ", size=3, default=(0.0, 0.0, 0.0), update=MxNode.update_prop)
    nd_vector3_out_out: FloatVectorProperty(name="Out", description="", subtype="XYZ", size=3, update=MxNode.update_prop)

    nd_vector4_in_in: FloatVectorProperty(name="In", description="", subtype="NONE", size=4, default=(0.0, 0.0, 0.0, 0.0), update=MxNode.update_prop)
    nd_vector4_out_out: FloatVectorProperty(name="Out", description="", subtype="NONE", size=4, update=MxNode.update_prop)


class MxNode_STD_power(MxNode):
    _file_path = FILE_PATH
    _data_types = {'float': {'nd_name': 'ND_power_float', 'nd': None}, 'color3': {'nd_name': 'ND_power_color3', 'nd': None}, 'color4': {'nd_name': 'ND_power_color4', 'nd': None}, 'vector2': {'nd_name': 'ND_power_vector2', 'nd': None}, 'vector3': {'nd_name': 'ND_power_vector3', 'nd': None}, 'vector4': {'nd_name': 'ND_power_vector4', 'nd': None}, 'color3FA': {'nd_name': 'ND_power_color3FA', 'nd': None}, 'color4FA': {'nd_name': 'ND_power_color4FA', 'nd': None}, 'vector2FA': {'nd_name': 'ND_power_vector2FA', 'nd': None}, 'vector3FA': {'nd_name': 'ND_power_vector3FA', 'nd': None}, 'vector4FA': {'nd_name': 'ND_power_vector4FA', 'nd': None}}

    bl_label = 'Power'
    bl_idname = 'usdhydra.MxNode_STD_power'
    bl_description = ""

    category = 'math'

    data_type: EnumProperty(name="Type", description="Input Data Type", items=[('float', 'Float', 'Float'), ('color3', 'Color3', 'Color3'), ('color4', 'Color4', 'Color4'), ('vector2', 'Vector2', 'Vector2'), ('vector3', 'Vector3', 'Vector3'), ('vector4', 'Vector4', 'Vector4'), ('color3FA', 'Color3FA', 'Color3FA'), ('color4FA', 'Color4FA', 'Color4FA'), ('vector2FA', 'Vector2FA', 'Vector2FA'), ('vector3FA', 'Vector3FA', 'Vector3FA'), ('vector4FA', 'Vector4FA', 'Vector4FA')], default='color3', update=MxNode.update_data_type)

    nd_float_in_in1: FloatProperty(name="In1", description="", default=0.0, update=MxNode.update_prop)
    nd_float_in_in2: FloatProperty(name="In2", description="", default=1.0, update=MxNode.update_prop)
    nd_float_out_out: FloatProperty(name="Out", description="", update=MxNode.update_prop)

    nd_color3_in_in1: FloatVectorProperty(name="In1", description="", subtype="COLOR", size=3, soft_min=0.0, soft_max=1.0, default=(0.0, 0.0, 0.0), update=MxNode.update_prop)
    nd_color3_in_in2: FloatVectorProperty(name="In2", description="", subtype="COLOR", size=3, soft_min=0.0, soft_max=1.0, default=(1.0, 1.0, 1.0), update=MxNode.update_prop)
    nd_color3_out_out: FloatVectorProperty(name="Out", description="", subtype="COLOR", size=3, soft_min=0.0, soft_max=1.0, update=MxNode.update_prop)

    nd_color4_in_in1: FloatVectorProperty(name="In1", description="", subtype="COLOR", size=4, soft_min=0.0, soft_max=1.0, default=(0.0, 0.0, 0.0, 0.0), update=MxNode.update_prop)
    nd_color4_in_in2: FloatVectorProperty(name="In2", description="", subtype="COLOR", size=4, soft_min=0.0, soft_max=1.0, default=(1.0, 1.0, 1.0, 1.0), update=MxNode.update_prop)
    nd_color4_out_out: FloatVectorProperty(name="Out", description="", subtype="COLOR", size=4, soft_min=0.0, soft_max=1.0, update=MxNode.update_prop)

    nd_vector2_in_in1: FloatVectorProperty(name="In1", description="", subtype="NONE", size=2, default=(0.0, 0.0), update=MxNode.update_prop)
    nd_vector2_in_in2: FloatVectorProperty(name="In2", description="", subtype="NONE", size=2, default=(1.0, 1.0), update=MxNode.update_prop)
    nd_vector2_out_out: FloatVectorProperty(name="Out", description="", subtype="NONE", size=2, update=MxNode.update_prop)

    nd_vector3_in_in1: FloatVectorProperty(name="In1", description="", subtype="XYZ", size=3, default=(0.0, 0.0, 0.0), update=MxNode.update_prop)
    nd_vector3_in_in2: FloatVectorProperty(name="In2", description="", subtype="XYZ", size=3, default=(1.0, 1.0, 1.0), update=MxNode.update_prop)
    nd_vector3_out_out: FloatVectorProperty(name="Out", description="", subtype="XYZ", size=3, update=MxNode.update_prop)

    nd_vector4_in_in1: FloatVectorProperty(name="In1", description="", subtype="NONE", size=4, default=(0.0, 0.0, 0.0, 0.0), update=MxNode.update_prop)
    nd_vector4_in_in2: FloatVectorProperty(name="In2", description="", subtype="NONE", size=4, default=(1.0, 1.0, 1.0, 1.0), update=MxNode.update_prop)
    nd_vector4_out_out: FloatVectorProperty(name="Out", description="", subtype="NONE", size=4, update=MxNode.update_prop)

    nd_color3FA_in_in1: FloatVectorProperty(name="In1", description="", subtype="COLOR", size=3, soft_min=0.0, soft_max=1.0, default=(0.0, 0.0, 0.0), update=MxNode.update_prop)
    nd_color3FA_in_in2: FloatProperty(name="In2", description="", default=1.0, update=MxNode.update_prop)
    nd_color3FA_out_out: FloatVectorProperty(name="Out", description="", subtype="COLOR", size=3, soft_min=0.0, soft_max=1.0, update=MxNode.update_prop)

    nd_color4FA_in_in1: FloatVectorProperty(name="In1", description="", subtype="COLOR", size=4, soft_min=0.0, soft_max=1.0, default=(0.0, 0.0, 0.0, 0.0), update=MxNode.update_prop)
    nd_color4FA_in_in2: FloatProperty(name="In2", description="", default=1.0, update=MxNode.update_prop)
    nd_color4FA_out_out: FloatVectorProperty(name="Out", description="", subtype="COLOR", size=4, soft_min=0.0, soft_max=1.0, update=MxNode.update_prop)

    nd_vector2FA_in_in1: FloatVectorProperty(name="In1", description="", subtype="NONE", size=2, default=(0.0, 0.0), update=MxNode.update_prop)
    nd_vector2FA_in_in2: FloatProperty(name="In2", description="", default=1.0, update=MxNode.update_prop)
    nd_vector2FA_out_out: FloatVectorProperty(name="Out", description="", subtype="NONE", size=2, update=MxNode.update_prop)

    nd_vector3FA_in_in1: FloatVectorProperty(name="In1", description="", subtype="XYZ", size=3, default=(0.0, 0.0, 0.0), update=MxNode.update_prop)
    nd_vector3FA_in_in2: FloatProperty(name="In2", description="", default=1.0, update=MxNode.update_prop)
    nd_vector3FA_out_out: FloatVectorProperty(name="Out", description="", subtype="XYZ", size=3, update=MxNode.update_prop)

    nd_vector4FA_in_in1: FloatVectorProperty(name="In1", description="", subtype="NONE", size=4, default=(0.0, 0.0, 0.0, 0.0), update=MxNode.update_prop)
    nd_vector4FA_in_in2: FloatProperty(name="In2", description="", default=1.0, update=MxNode.update_prop)
    nd_vector4FA_out_out: FloatVectorProperty(name="Out", description="", subtype="NONE", size=4, update=MxNode.update_prop)


class MxNode_STD_sin(MxNode):
    _file_path = FILE_PATH
    _data_types = {'float': {'nd_name': 'ND_sin_float', 'nd': None}, 'vector2': {'nd_name': 'ND_sin_vector2', 'nd': None}, 'vector3': {'nd_name': 'ND_sin_vector3', 'nd': None}, 'vector4': {'nd_name': 'ND_sin_vector4', 'nd': None}}

    bl_label = 'Sin'
    bl_idname = 'usdhydra.MxNode_STD_sin'
    bl_description = ""

    category = 'math'

    data_type: EnumProperty(name="Type", description="Input Data Type", items=[('float', 'Float', 'Float'), ('vector2', 'Vector2', 'Vector2'), ('vector3', 'Vector3', 'Vector3'), ('vector4', 'Vector4', 'Vector4')], default='float', update=MxNode.update_data_type)

    nd_float_in_in: FloatProperty(name="In", description="", default=0.0, update=MxNode.update_prop)
    nd_float_out_out: FloatProperty(name="Out", description="", update=MxNode.update_prop)

    nd_vector2_in_in: FloatVectorProperty(name="In", description="", subtype="NONE", size=2, default=(0.0, 0.0), update=MxNode.update_prop)
    nd_vector2_out_out: FloatVectorProperty(name="Out", description="", subtype="NONE", size=2, update=MxNode.update_prop)

    nd_vector3_in_in: FloatVectorProperty(name="In", description="", subtype="XYZ", size=3, default=(0.0, 0.0, 0.0), update=MxNode.update_prop)
    nd_vector3_out_out: FloatVectorProperty(name="Out", description="", subtype="XYZ", size=3, update=MxNode.update_prop)

    nd_vector4_in_in: FloatVectorProperty(name="In", description="", subtype="NONE", size=4, default=(0.0, 0.0, 0.0, 0.0), update=MxNode.update_prop)
    nd_vector4_out_out: FloatVectorProperty(name="Out", description="", subtype="NONE", size=4, update=MxNode.update_prop)


class MxNode_STD_cos(MxNode):
    _file_path = FILE_PATH
    _data_types = {'float': {'nd_name': 'ND_cos_float', 'nd': None}, 'vector2': {'nd_name': 'ND_cos_vector2', 'nd': None}, 'vector3': {'nd_name': 'ND_cos_vector3', 'nd': None}, 'vector4': {'nd_name': 'ND_cos_vector4', 'nd': None}}

    bl_label = 'Cos'
    bl_idname = 'usdhydra.MxNode_STD_cos'
    bl_description = ""

    category = 'math'

    data_type: EnumProperty(name="Type", description="Input Data Type", items=[('float', 'Float', 'Float'), ('vector2', 'Vector2', 'Vector2'), ('vector3', 'Vector3', 'Vector3'), ('vector4', 'Vector4', 'Vector4')], default='float', update=MxNode.update_data_type)

    nd_float_in_in: FloatProperty(name="In", description="", default=0.0, update=MxNode.update_prop)
    nd_float_out_out: FloatProperty(name="Out", description="", update=MxNode.update_prop)

    nd_vector2_in_in: FloatVectorProperty(name="In", description="", subtype="NONE", size=2, default=(0.0, 0.0), update=MxNode.update_prop)
    nd_vector2_out_out: FloatVectorProperty(name="Out", description="", subtype="NONE", size=2, update=MxNode.update_prop)

    nd_vector3_in_in: FloatVectorProperty(name="In", description="", subtype="XYZ", size=3, default=(0.0, 0.0, 0.0), update=MxNode.update_prop)
    nd_vector3_out_out: FloatVectorProperty(name="Out", description="", subtype="XYZ", size=3, update=MxNode.update_prop)

    nd_vector4_in_in: FloatVectorProperty(name="In", description="", subtype="NONE", size=4, default=(0.0, 0.0, 0.0, 0.0), update=MxNode.update_prop)
    nd_vector4_out_out: FloatVectorProperty(name="Out", description="", subtype="NONE", size=4, update=MxNode.update_prop)


class MxNode_STD_tan(MxNode):
    _file_path = FILE_PATH
    _data_types = {'float': {'nd_name': 'ND_tan_float', 'nd': None}, 'vector2': {'nd_name': 'ND_tan_vector2', 'nd': None}, 'vector3': {'nd_name': 'ND_tan_vector3', 'nd': None}, 'vector4': {'nd_name': 'ND_tan_vector4', 'nd': None}}

    bl_label = 'Tan'
    bl_idname = 'usdhydra.MxNode_STD_tan'
    bl_description = ""

    category = 'math'

    data_type: EnumProperty(name="Type", description="Input Data Type", items=[('float', 'Float', 'Float'), ('vector2', 'Vector2', 'Vector2'), ('vector3', 'Vector3', 'Vector3'), ('vector4', 'Vector4', 'Vector4')], default='float', update=MxNode.update_data_type)

    nd_float_in_in: FloatProperty(name="In", description="", default=0.0, update=MxNode.update_prop)
    nd_float_out_out: FloatProperty(name="Out", description="", update=MxNode.update_prop)

    nd_vector2_in_in: FloatVectorProperty(name="In", description="", subtype="NONE", size=2, default=(0.0, 0.0), update=MxNode.update_prop)
    nd_vector2_out_out: FloatVectorProperty(name="Out", description="", subtype="NONE", size=2, update=MxNode.update_prop)

    nd_vector3_in_in: FloatVectorProperty(name="In", description="", subtype="XYZ", size=3, default=(0.0, 0.0, 0.0), update=MxNode.update_prop)
    nd_vector3_out_out: FloatVectorProperty(name="Out", description="", subtype="XYZ", size=3, update=MxNode.update_prop)

    nd_vector4_in_in: FloatVectorProperty(name="In", description="", subtype="NONE", size=4, default=(0.0, 0.0, 0.0, 0.0), update=MxNode.update_prop)
    nd_vector4_out_out: FloatVectorProperty(name="Out", description="", subtype="NONE", size=4, update=MxNode.update_prop)


class MxNode_STD_asin(MxNode):
    _file_path = FILE_PATH
    _data_types = {'float': {'nd_name': 'ND_asin_float', 'nd': None}, 'vector2': {'nd_name': 'ND_asin_vector2', 'nd': None}, 'vector3': {'nd_name': 'ND_asin_vector3', 'nd': None}, 'vector4': {'nd_name': 'ND_asin_vector4', 'nd': None}}

    bl_label = 'Asin'
    bl_idname = 'usdhydra.MxNode_STD_asin'
    bl_description = ""

    category = 'math'

    data_type: EnumProperty(name="Type", description="Input Data Type", items=[('float', 'Float', 'Float'), ('vector2', 'Vector2', 'Vector2'), ('vector3', 'Vector3', 'Vector3'), ('vector4', 'Vector4', 'Vector4')], default='float', update=MxNode.update_data_type)

    nd_float_in_in: FloatProperty(name="In", description="", default=0.0, update=MxNode.update_prop)
    nd_float_out_out: FloatProperty(name="Out", description="", update=MxNode.update_prop)

    nd_vector2_in_in: FloatVectorProperty(name="In", description="", subtype="NONE", size=2, default=(0.0, 0.0), update=MxNode.update_prop)
    nd_vector2_out_out: FloatVectorProperty(name="Out", description="", subtype="NONE", size=2, update=MxNode.update_prop)

    nd_vector3_in_in: FloatVectorProperty(name="In", description="", subtype="XYZ", size=3, default=(0.0, 0.0, 0.0), update=MxNode.update_prop)
    nd_vector3_out_out: FloatVectorProperty(name="Out", description="", subtype="XYZ", size=3, update=MxNode.update_prop)

    nd_vector4_in_in: FloatVectorProperty(name="In", description="", subtype="NONE", size=4, default=(0.0, 0.0, 0.0, 0.0), update=MxNode.update_prop)
    nd_vector4_out_out: FloatVectorProperty(name="Out", description="", subtype="NONE", size=4, update=MxNode.update_prop)


class MxNode_STD_acos(MxNode):
    _file_path = FILE_PATH
    _data_types = {'float': {'nd_name': 'ND_acos_float', 'nd': None}, 'vector2': {'nd_name': 'ND_acos_vector2', 'nd': None}, 'vector3': {'nd_name': 'ND_acos_vector3', 'nd': None}, 'vector4': {'nd_name': 'ND_acos_vector4', 'nd': None}}

    bl_label = 'Acos'
    bl_idname = 'usdhydra.MxNode_STD_acos'
    bl_description = ""

    category = 'math'

    data_type: EnumProperty(name="Type", description="Input Data Type", items=[('float', 'Float', 'Float'), ('vector2', 'Vector2', 'Vector2'), ('vector3', 'Vector3', 'Vector3'), ('vector4', 'Vector4', 'Vector4')], default='float', update=MxNode.update_data_type)

    nd_float_in_in: FloatProperty(name="In", description="", default=0.0, update=MxNode.update_prop)
    nd_float_out_out: FloatProperty(name="Out", description="", update=MxNode.update_prop)

    nd_vector2_in_in: FloatVectorProperty(name="In", description="", subtype="NONE", size=2, default=(0.0, 0.0), update=MxNode.update_prop)
    nd_vector2_out_out: FloatVectorProperty(name="Out", description="", subtype="NONE", size=2, update=MxNode.update_prop)

    nd_vector3_in_in: FloatVectorProperty(name="In", description="", subtype="XYZ", size=3, default=(0.0, 0.0, 0.0), update=MxNode.update_prop)
    nd_vector3_out_out: FloatVectorProperty(name="Out", description="", subtype="XYZ", size=3, update=MxNode.update_prop)

    nd_vector4_in_in: FloatVectorProperty(name="In", description="", subtype="NONE", size=4, default=(0.0, 0.0, 0.0, 0.0), update=MxNode.update_prop)
    nd_vector4_out_out: FloatVectorProperty(name="Out", description="", subtype="NONE", size=4, update=MxNode.update_prop)


class MxNode_STD_atan2(MxNode):
    _file_path = FILE_PATH
    _data_types = {'float': {'nd_name': 'ND_atan2_float', 'nd': None}, 'vector2': {'nd_name': 'ND_atan2_vector2', 'nd': None}, 'vector3': {'nd_name': 'ND_atan2_vector3', 'nd': None}, 'vector4': {'nd_name': 'ND_atan2_vector4', 'nd': None}}

    bl_label = 'Atan2'
    bl_idname = 'usdhydra.MxNode_STD_atan2'
    bl_description = ""

    category = 'math'

    data_type: EnumProperty(name="Type", description="Input Data Type", items=[('float', 'Float', 'Float'), ('vector2', 'Vector2', 'Vector2'), ('vector3', 'Vector3', 'Vector3'), ('vector4', 'Vector4', 'Vector4')], default='float', update=MxNode.update_data_type)

    nd_float_in_in1: FloatProperty(name="In1", description="", default=0.0, update=MxNode.update_prop)
    nd_float_in_in2: FloatProperty(name="In2", description="", default=1.0, update=MxNode.update_prop)
    nd_float_out_out: FloatProperty(name="Out", description="", update=MxNode.update_prop)

    nd_vector2_in_in1: FloatVectorProperty(name="In1", description="", subtype="NONE", size=2, default=(1.0, 1.0), update=MxNode.update_prop)
    nd_vector2_in_in2: FloatVectorProperty(name="In2", description="", subtype="NONE", size=2, default=(0.0, 0.0), update=MxNode.update_prop)
    nd_vector2_out_out: FloatVectorProperty(name="Out", description="", subtype="NONE", size=2, update=MxNode.update_prop)

    nd_vector3_in_in1: FloatVectorProperty(name="In1", description="", subtype="XYZ", size=3, default=(1.0, 1.0, 1.0), update=MxNode.update_prop)
    nd_vector3_in_in2: FloatVectorProperty(name="In2", description="", subtype="XYZ", size=3, default=(0.0, 0.0, 0.0), update=MxNode.update_prop)
    nd_vector3_out_out: FloatVectorProperty(name="Out", description="", subtype="XYZ", size=3, update=MxNode.update_prop)

    nd_vector4_in_in1: FloatVectorProperty(name="In1", description="", subtype="NONE", size=4, default=(1.0, 1.0, 1.0, 1.0), update=MxNode.update_prop)
    nd_vector4_in_in2: FloatVectorProperty(name="In2", description="", subtype="NONE", size=4, default=(0.0, 0.0, 0.0, 0.0), update=MxNode.update_prop)
    nd_vector4_out_out: FloatVectorProperty(name="Out", description="", subtype="NONE", size=4, update=MxNode.update_prop)


class MxNode_STD_sqrt(MxNode):
    _file_path = FILE_PATH
    _data_types = {'float': {'nd_name': 'ND_sqrt_float', 'nd': None}, 'vector2': {'nd_name': 'ND_sqrt_vector2', 'nd': None}, 'vector3': {'nd_name': 'ND_sqrt_vector3', 'nd': None}, 'vector4': {'nd_name': 'ND_sqrt_vector4', 'nd': None}}

    bl_label = 'Sqrt'
    bl_idname = 'usdhydra.MxNode_STD_sqrt'
    bl_description = ""

    category = 'math'

    data_type: EnumProperty(name="Type", description="Input Data Type", items=[('float', 'Float', 'Float'), ('vector2', 'Vector2', 'Vector2'), ('vector3', 'Vector3', 'Vector3'), ('vector4', 'Vector4', 'Vector4')], default='float', update=MxNode.update_data_type)

    nd_float_in_in: FloatProperty(name="In", description="", default=0.0, update=MxNode.update_prop)
    nd_float_out_out: FloatProperty(name="Out", description="", update=MxNode.update_prop)

    nd_vector2_in_in: FloatVectorProperty(name="In", description="", subtype="NONE", size=2, default=(0.0, 0.0), update=MxNode.update_prop)
    nd_vector2_out_out: FloatVectorProperty(name="Out", description="", subtype="NONE", size=2, update=MxNode.update_prop)

    nd_vector3_in_in: FloatVectorProperty(name="In", description="", subtype="XYZ", size=3, default=(0.0, 0.0, 0.0), update=MxNode.update_prop)
    nd_vector3_out_out: FloatVectorProperty(name="Out", description="", subtype="XYZ", size=3, update=MxNode.update_prop)

    nd_vector4_in_in: FloatVectorProperty(name="In", description="", subtype="NONE", size=4, default=(0.0, 0.0, 0.0, 0.0), update=MxNode.update_prop)
    nd_vector4_out_out: FloatVectorProperty(name="Out", description="", subtype="NONE", size=4, update=MxNode.update_prop)


class MxNode_STD_ln(MxNode):
    _file_path = FILE_PATH
    _data_types = {'float': {'nd_name': 'ND_ln_float', 'nd': None}, 'vector2': {'nd_name': 'ND_ln_vector2', 'nd': None}, 'vector3': {'nd_name': 'ND_ln_vector3', 'nd': None}, 'vector4': {'nd_name': 'ND_ln_vector4', 'nd': None}}

    bl_label = 'Ln'
    bl_idname = 'usdhydra.MxNode_STD_ln'
    bl_description = ""

    category = 'math'

    data_type: EnumProperty(name="Type", description="Input Data Type", items=[('float', 'Float', 'Float'), ('vector2', 'Vector2', 'Vector2'), ('vector3', 'Vector3', 'Vector3'), ('vector4', 'Vector4', 'Vector4')], default='float', update=MxNode.update_data_type)

    nd_float_in_in: FloatProperty(name="In", description="", default=1.0, update=MxNode.update_prop)
    nd_float_out_out: FloatProperty(name="Out", description="", update=MxNode.update_prop)

    nd_vector2_in_in: FloatVectorProperty(name="In", description="", subtype="NONE", size=2, default=(1.0, 1.0), update=MxNode.update_prop)
    nd_vector2_out_out: FloatVectorProperty(name="Out", description="", subtype="NONE", size=2, update=MxNode.update_prop)

    nd_vector3_in_in: FloatVectorProperty(name="In", description="", subtype="XYZ", size=3, default=(1.0, 1.0, 1.0), update=MxNode.update_prop)
    nd_vector3_out_out: FloatVectorProperty(name="Out", description="", subtype="XYZ", size=3, update=MxNode.update_prop)

    nd_vector4_in_in: FloatVectorProperty(name="In", description="", subtype="NONE", size=4, default=(1.0, 1.0, 1.0, 1.0), update=MxNode.update_prop)
    nd_vector4_out_out: FloatVectorProperty(name="Out", description="", subtype="NONE", size=4, update=MxNode.update_prop)


class MxNode_STD_exp(MxNode):
    _file_path = FILE_PATH
    _data_types = {'float': {'nd_name': 'ND_exp_float', 'nd': None}, 'vector2': {'nd_name': 'ND_exp_vector2', 'nd': None}, 'vector3': {'nd_name': 'ND_exp_vector3', 'nd': None}, 'vector4': {'nd_name': 'ND_exp_vector4', 'nd': None}}

    bl_label = 'Exp'
    bl_idname = 'usdhydra.MxNode_STD_exp'
    bl_description = ""

    category = 'math'

    data_type: EnumProperty(name="Type", description="Input Data Type", items=[('float', 'Float', 'Float'), ('vector2', 'Vector2', 'Vector2'), ('vector3', 'Vector3', 'Vector3'), ('vector4', 'Vector4', 'Vector4')], default='float', update=MxNode.update_data_type)

    nd_float_in_in: FloatProperty(name="In", description="", default=0.0, update=MxNode.update_prop)
    nd_float_out_out: FloatProperty(name="Out", description="", update=MxNode.update_prop)

    nd_vector2_in_in: FloatVectorProperty(name="In", description="", subtype="NONE", size=2, default=(0.0, 0.0), update=MxNode.update_prop)
    nd_vector2_out_out: FloatVectorProperty(name="Out", description="", subtype="NONE", size=2, update=MxNode.update_prop)

    nd_vector3_in_in: FloatVectorProperty(name="In", description="", subtype="XYZ", size=3, default=(0.0, 0.0, 0.0), update=MxNode.update_prop)
    nd_vector3_out_out: FloatVectorProperty(name="Out", description="", subtype="XYZ", size=3, update=MxNode.update_prop)

    nd_vector4_in_in: FloatVectorProperty(name="In", description="", subtype="NONE", size=4, default=(0.0, 0.0, 0.0, 0.0), update=MxNode.update_prop)
    nd_vector4_out_out: FloatVectorProperty(name="Out", description="", subtype="NONE", size=4, update=MxNode.update_prop)


class MxNode_STD_sign(MxNode):
    _file_path = FILE_PATH
    _data_types = {'float': {'nd_name': 'ND_sign_float', 'nd': None}, 'color3': {'nd_name': 'ND_sign_color3', 'nd': None}, 'color4': {'nd_name': 'ND_sign_color4', 'nd': None}, 'vector2': {'nd_name': 'ND_sign_vector2', 'nd': None}, 'vector3': {'nd_name': 'ND_sign_vector3', 'nd': None}, 'vector4': {'nd_name': 'ND_sign_vector4', 'nd': None}}

    bl_label = 'Sign'
    bl_idname = 'usdhydra.MxNode_STD_sign'
    bl_description = ""

    category = 'math'

    data_type: EnumProperty(name="Type", description="Input Data Type", items=[('float', 'Float', 'Float'), ('color3', 'Color3', 'Color3'), ('color4', 'Color4', 'Color4'), ('vector2', 'Vector2', 'Vector2'), ('vector3', 'Vector3', 'Vector3'), ('vector4', 'Vector4', 'Vector4')], default='color3', update=MxNode.update_data_type)

    nd_float_in_in: FloatProperty(name="In", description="", default=0.0, update=MxNode.update_prop)
    nd_float_out_out: FloatProperty(name="Out", description="", update=MxNode.update_prop)

    nd_color3_in_in: FloatVectorProperty(name="In", description="", subtype="COLOR", size=3, soft_min=0.0, soft_max=1.0, default=(0.0, 0.0, 0.0), update=MxNode.update_prop)
    nd_color3_out_out: FloatVectorProperty(name="Out", description="", subtype="COLOR", size=3, soft_min=0.0, soft_max=1.0, update=MxNode.update_prop)

    nd_color4_in_in: FloatVectorProperty(name="In", description="", subtype="COLOR", size=4, soft_min=0.0, soft_max=1.0, default=(0.0, 0.0, 0.0, 0.0), update=MxNode.update_prop)
    nd_color4_out_out: FloatVectorProperty(name="Out", description="", subtype="COLOR", size=4, soft_min=0.0, soft_max=1.0, update=MxNode.update_prop)

    nd_vector2_in_in: FloatVectorProperty(name="In", description="", subtype="NONE", size=2, default=(0.0, 0.0), update=MxNode.update_prop)
    nd_vector2_out_out: FloatVectorProperty(name="Out", description="", subtype="NONE", size=2, update=MxNode.update_prop)

    nd_vector3_in_in: FloatVectorProperty(name="In", description="", subtype="XYZ", size=3, default=(0.0, 0.0, 0.0), update=MxNode.update_prop)
    nd_vector3_out_out: FloatVectorProperty(name="Out", description="", subtype="XYZ", size=3, update=MxNode.update_prop)

    nd_vector4_in_in: FloatVectorProperty(name="In", description="", subtype="NONE", size=4, default=(0.0, 0.0, 0.0, 0.0), update=MxNode.update_prop)
    nd_vector4_out_out: FloatVectorProperty(name="Out", description="", subtype="NONE", size=4, update=MxNode.update_prop)


class MxNode_STD_clamp(MxNode):
    _file_path = FILE_PATH
    _data_types = {'float': {'nd_name': 'ND_clamp_float', 'nd': None}, 'color3': {'nd_name': 'ND_clamp_color3', 'nd': None}, 'color4': {'nd_name': 'ND_clamp_color4', 'nd': None}, 'vector2': {'nd_name': 'ND_clamp_vector2', 'nd': None}, 'vector3': {'nd_name': 'ND_clamp_vector3', 'nd': None}, 'vector4': {'nd_name': 'ND_clamp_vector4', 'nd': None}, 'color3FA': {'nd_name': 'ND_clamp_color3FA', 'nd': None}, 'color4FA': {'nd_name': 'ND_clamp_color4FA', 'nd': None}, 'vector2FA': {'nd_name': 'ND_clamp_vector2FA', 'nd': None}, 'vector3FA': {'nd_name': 'ND_clamp_vector3FA', 'nd': None}, 'vector4FA': {'nd_name': 'ND_clamp_vector4FA', 'nd': None}}

    bl_label = 'Clamp'
    bl_idname = 'usdhydra.MxNode_STD_clamp'
    bl_description = ""

    category = 'math'

    data_type: EnumProperty(name="Type", description="Input Data Type", items=[('float', 'Float', 'Float'), ('color3', 'Color3', 'Color3'), ('color4', 'Color4', 'Color4'), ('vector2', 'Vector2', 'Vector2'), ('vector3', 'Vector3', 'Vector3'), ('vector4', 'Vector4', 'Vector4'), ('color3FA', 'Color3FA', 'Color3FA'), ('color4FA', 'Color4FA', 'Color4FA'), ('vector2FA', 'Vector2FA', 'Vector2FA'), ('vector3FA', 'Vector3FA', 'Vector3FA'), ('vector4FA', 'Vector4FA', 'Vector4FA')], default='color3', update=MxNode.update_data_type)

    nd_float_in_in: FloatProperty(name="In", description="", default=0.0, update=MxNode.update_prop)
    nd_float_in_low: FloatProperty(name="Low", description="", default=0.0, update=MxNode.update_prop)
    nd_float_in_high: FloatProperty(name="High", description="", default=1.0, update=MxNode.update_prop)
    nd_float_out_out: FloatProperty(name="Out", description="", update=MxNode.update_prop)

    nd_color3_in_in: FloatVectorProperty(name="In", description="", subtype="COLOR", size=3, soft_min=0.0, soft_max=1.0, default=(0.0, 0.0, 0.0), update=MxNode.update_prop)
    nd_color3_in_low: FloatVectorProperty(name="Low", description="", subtype="COLOR", size=3, soft_min=0.0, soft_max=1.0, default=(0.0, 0.0, 0.0), update=MxNode.update_prop)
    nd_color3_in_high: FloatVectorProperty(name="High", description="", subtype="COLOR", size=3, soft_min=0.0, soft_max=1.0, default=(1.0, 1.0, 1.0), update=MxNode.update_prop)
    nd_color3_out_out: FloatVectorProperty(name="Out", description="", subtype="COLOR", size=3, soft_min=0.0, soft_max=1.0, update=MxNode.update_prop)

    nd_color4_in_in: FloatVectorProperty(name="In", description="", subtype="COLOR", size=4, soft_min=0.0, soft_max=1.0, default=(0.0, 0.0, 0.0, 0.0), update=MxNode.update_prop)
    nd_color4_in_low: FloatVectorProperty(name="Low", description="", subtype="COLOR", size=4, soft_min=0.0, soft_max=1.0, default=(0.0, 0.0, 0.0, 0.0), update=MxNode.update_prop)
    nd_color4_in_high: FloatVectorProperty(name="High", description="", subtype="COLOR", size=4, soft_min=0.0, soft_max=1.0, default=(1.0, 1.0, 1.0, 1.0), update=MxNode.update_prop)
    nd_color4_out_out: FloatVectorProperty(name="Out", description="", subtype="COLOR", size=4, soft_min=0.0, soft_max=1.0, update=MxNode.update_prop)

    nd_vector2_in_in: FloatVectorProperty(name="In", description="", subtype="NONE", size=2, default=(0.0, 0.0), update=MxNode.update_prop)
    nd_vector2_in_low: FloatVectorProperty(name="Low", description="", subtype="NONE", size=2, default=(0.0, 0.0), update=MxNode.update_prop)
    nd_vector2_in_high: FloatVectorProperty(name="High", description="", subtype="NONE", size=2, default=(1.0, 1.0), update=MxNode.update_prop)
    nd_vector2_out_out: FloatVectorProperty(name="Out", description="", subtype="NONE", size=2, update=MxNode.update_prop)

    nd_vector3_in_in: FloatVectorProperty(name="In", description="", subtype="XYZ", size=3, default=(0.0, 0.0, 0.0), update=MxNode.update_prop)
    nd_vector3_in_low: FloatVectorProperty(name="Low", description="", subtype="XYZ", size=3, default=(0.0, 0.0, 0.0), update=MxNode.update_prop)
    nd_vector3_in_high: FloatVectorProperty(name="High", description="", subtype="XYZ", size=3, default=(1.0, 1.0, 1.0), update=MxNode.update_prop)
    nd_vector3_out_out: FloatVectorProperty(name="Out", description="", subtype="XYZ", size=3, update=MxNode.update_prop)

    nd_vector4_in_in: FloatVectorProperty(name="In", description="", subtype="NONE", size=4, default=(0.0, 0.0, 0.0, 0.0), update=MxNode.update_prop)
    nd_vector4_in_low: FloatVectorProperty(name="Low", description="", subtype="NONE", size=4, default=(0.0, 0.0, 0.0, 0.0), update=MxNode.update_prop)
    nd_vector4_in_high: FloatVectorProperty(name="High", description="", subtype="NONE", size=4, default=(1.0, 1.0, 1.0, 1.0), update=MxNode.update_prop)
    nd_vector4_out_out: FloatVectorProperty(name="Out", description="", subtype="NONE", size=4, update=MxNode.update_prop)

    nd_color3FA_in_in: FloatVectorProperty(name="In", description="", subtype="COLOR", size=3, soft_min=0.0, soft_max=1.0, default=(0.0, 0.0, 0.0), update=MxNode.update_prop)
    nd_color3FA_in_low: FloatProperty(name="Low", description="", default=0.0, update=MxNode.update_prop)
    nd_color3FA_in_high: FloatProperty(name="High", description="", default=1.0, update=MxNode.update_prop)
    nd_color3FA_out_out: FloatVectorProperty(name="Out", description="", subtype="COLOR", size=3, soft_min=0.0, soft_max=1.0, update=MxNode.update_prop)

    nd_color4FA_in_in: FloatVectorProperty(name="In", description="", subtype="COLOR", size=4, soft_min=0.0, soft_max=1.0, default=(0.0, 0.0, 0.0, 0.0), update=MxNode.update_prop)
    nd_color4FA_in_low: FloatProperty(name="Low", description="", default=0.0, update=MxNode.update_prop)
    nd_color4FA_in_high: FloatProperty(name="High", description="", default=1.0, update=MxNode.update_prop)
    nd_color4FA_out_out: FloatVectorProperty(name="Out", description="", subtype="COLOR", size=4, soft_min=0.0, soft_max=1.0, update=MxNode.update_prop)

    nd_vector2FA_in_in: FloatVectorProperty(name="In", description="", subtype="NONE", size=2, default=(0.0, 0.0), update=MxNode.update_prop)
    nd_vector2FA_in_low: FloatProperty(name="Low", description="", default=0.0, update=MxNode.update_prop)
    nd_vector2FA_in_high: FloatProperty(name="High", description="", default=1.0, update=MxNode.update_prop)
    nd_vector2FA_out_out: FloatVectorProperty(name="Out", description="", subtype="NONE", size=2, update=MxNode.update_prop)

    nd_vector3FA_in_in: FloatVectorProperty(name="In", description="", subtype="XYZ", size=3, default=(0.0, 0.0, 0.0), update=MxNode.update_prop)
    nd_vector3FA_in_low: FloatProperty(name="Low", description="", default=0.0, update=MxNode.update_prop)
    nd_vector3FA_in_high: FloatProperty(name="High", description="", default=1.0, update=MxNode.update_prop)
    nd_vector3FA_out_out: FloatVectorProperty(name="Out", description="", subtype="XYZ", size=3, update=MxNode.update_prop)

    nd_vector4FA_in_in: FloatVectorProperty(name="In", description="", subtype="NONE", size=4, default=(0.0, 0.0, 0.0, 0.0), update=MxNode.update_prop)
    nd_vector4FA_in_low: FloatProperty(name="Low", description="", default=0.0, update=MxNode.update_prop)
    nd_vector4FA_in_high: FloatProperty(name="High", description="", default=1.0, update=MxNode.update_prop)
    nd_vector4FA_out_out: FloatVectorProperty(name="Out", description="", subtype="NONE", size=4, update=MxNode.update_prop)


class MxNode_STD_min(MxNode):
    _file_path = FILE_PATH
    _data_types = {'float': {'nd_name': 'ND_min_float', 'nd': None}, 'color3': {'nd_name': 'ND_min_color3', 'nd': None}, 'color4': {'nd_name': 'ND_min_color4', 'nd': None}, 'vector2': {'nd_name': 'ND_min_vector2', 'nd': None}, 'vector3': {'nd_name': 'ND_min_vector3', 'nd': None}, 'vector4': {'nd_name': 'ND_min_vector4', 'nd': None}, 'color3FA': {'nd_name': 'ND_min_color3FA', 'nd': None}, 'color4FA': {'nd_name': 'ND_min_color4FA', 'nd': None}, 'vector2FA': {'nd_name': 'ND_min_vector2FA', 'nd': None}, 'vector3FA': {'nd_name': 'ND_min_vector3FA', 'nd': None}, 'vector4FA': {'nd_name': 'ND_min_vector4FA', 'nd': None}}

    bl_label = 'Min'
    bl_idname = 'usdhydra.MxNode_STD_min'
    bl_description = ""

    category = 'math'

    data_type: EnumProperty(name="Type", description="Input Data Type", items=[('float', 'Float', 'Float'), ('color3', 'Color3', 'Color3'), ('color4', 'Color4', 'Color4'), ('vector2', 'Vector2', 'Vector2'), ('vector3', 'Vector3', 'Vector3'), ('vector4', 'Vector4', 'Vector4'), ('color3FA', 'Color3FA', 'Color3FA'), ('color4FA', 'Color4FA', 'Color4FA'), ('vector2FA', 'Vector2FA', 'Vector2FA'), ('vector3FA', 'Vector3FA', 'Vector3FA'), ('vector4FA', 'Vector4FA', 'Vector4FA')], default='color3', update=MxNode.update_data_type)

    nd_float_in_in1: FloatProperty(name="In1", description="", default=0.0, update=MxNode.update_prop)
    nd_float_in_in2: FloatProperty(name="In2", description="", default=0.0, update=MxNode.update_prop)
    nd_float_out_out: FloatProperty(name="Out", description="", update=MxNode.update_prop)

    nd_color3_in_in1: FloatVectorProperty(name="In1", description="", subtype="COLOR", size=3, soft_min=0.0, soft_max=1.0, default=(0.0, 0.0, 0.0), update=MxNode.update_prop)
    nd_color3_in_in2: FloatVectorProperty(name="In2", description="", subtype="COLOR", size=3, soft_min=0.0, soft_max=1.0, default=(0.0, 0.0, 0.0), update=MxNode.update_prop)
    nd_color3_out_out: FloatVectorProperty(name="Out", description="", subtype="COLOR", size=3, soft_min=0.0, soft_max=1.0, update=MxNode.update_prop)

    nd_color4_in_in1: FloatVectorProperty(name="In1", description="", subtype="COLOR", size=4, soft_min=0.0, soft_max=1.0, default=(0.0, 0.0, 0.0, 0.0), update=MxNode.update_prop)
    nd_color4_in_in2: FloatVectorProperty(name="In2", description="", subtype="COLOR", size=4, soft_min=0.0, soft_max=1.0, default=(0.0, 0.0, 0.0, 0.0), update=MxNode.update_prop)
    nd_color4_out_out: FloatVectorProperty(name="Out", description="", subtype="COLOR", size=4, soft_min=0.0, soft_max=1.0, update=MxNode.update_prop)

    nd_vector2_in_in1: FloatVectorProperty(name="In1", description="", subtype="NONE", size=2, default=(0.0, 0.0), update=MxNode.update_prop)
    nd_vector2_in_in2: FloatVectorProperty(name="In2", description="", subtype="NONE", size=2, default=(0.0, 0.0), update=MxNode.update_prop)
    nd_vector2_out_out: FloatVectorProperty(name="Out", description="", subtype="NONE", size=2, update=MxNode.update_prop)

    nd_vector3_in_in1: FloatVectorProperty(name="In1", description="", subtype="XYZ", size=3, default=(0.0, 0.0, 0.0), update=MxNode.update_prop)
    nd_vector3_in_in2: FloatVectorProperty(name="In2", description="", subtype="XYZ", size=3, default=(0.0, 0.0, 0.0), update=MxNode.update_prop)
    nd_vector3_out_out: FloatVectorProperty(name="Out", description="", subtype="XYZ", size=3, update=MxNode.update_prop)

    nd_vector4_in_in1: FloatVectorProperty(name="In1", description="", subtype="NONE", size=4, default=(0.0, 0.0, 0.0, 0.0), update=MxNode.update_prop)
    nd_vector4_in_in2: FloatVectorProperty(name="In2", description="", subtype="NONE", size=4, default=(0.0, 0.0, 0.0, 0.0), update=MxNode.update_prop)
    nd_vector4_out_out: FloatVectorProperty(name="Out", description="", subtype="NONE", size=4, update=MxNode.update_prop)

    nd_color3FA_in_in1: FloatVectorProperty(name="In1", description="", subtype="COLOR", size=3, soft_min=0.0, soft_max=1.0, default=(0.0, 0.0, 0.0), update=MxNode.update_prop)
    nd_color3FA_in_in2: FloatProperty(name="In2", description="", default=0.0, update=MxNode.update_prop)
    nd_color3FA_out_out: FloatVectorProperty(name="Out", description="", subtype="COLOR", size=3, soft_min=0.0, soft_max=1.0, update=MxNode.update_prop)

    nd_color4FA_in_in1: FloatVectorProperty(name="In1", description="", subtype="COLOR", size=4, soft_min=0.0, soft_max=1.0, default=(0.0, 0.0, 0.0, 0.0), update=MxNode.update_prop)
    nd_color4FA_in_in2: FloatProperty(name="In2", description="", default=0.0, update=MxNode.update_prop)
    nd_color4FA_out_out: FloatVectorProperty(name="Out", description="", subtype="COLOR", size=4, soft_min=0.0, soft_max=1.0, update=MxNode.update_prop)

    nd_vector2FA_in_in1: FloatVectorProperty(name="In1", description="", subtype="NONE", size=2, default=(0.0, 0.0), update=MxNode.update_prop)
    nd_vector2FA_in_in2: FloatProperty(name="In2", description="", default=0.0, update=MxNode.update_prop)
    nd_vector2FA_out_out: FloatVectorProperty(name="Out", description="", subtype="NONE", size=2, update=MxNode.update_prop)

    nd_vector3FA_in_in1: FloatVectorProperty(name="In1", description="", subtype="XYZ", size=3, default=(0.0, 0.0, 0.0), update=MxNode.update_prop)
    nd_vector3FA_in_in2: FloatProperty(name="In2", description="", default=0.0, update=MxNode.update_prop)
    nd_vector3FA_out_out: FloatVectorProperty(name="Out", description="", subtype="XYZ", size=3, update=MxNode.update_prop)

    nd_vector4FA_in_in1: FloatVectorProperty(name="In1", description="", subtype="NONE", size=4, default=(0.0, 0.0, 0.0, 0.0), update=MxNode.update_prop)
    nd_vector4FA_in_in2: FloatProperty(name="In2", description="", default=0.0, update=MxNode.update_prop)
    nd_vector4FA_out_out: FloatVectorProperty(name="Out", description="", subtype="NONE", size=4, update=MxNode.update_prop)


class MxNode_STD_max(MxNode):
    _file_path = FILE_PATH
    _data_types = {'float': {'nd_name': 'ND_max_float', 'nd': None}, 'color3': {'nd_name': 'ND_max_color3', 'nd': None}, 'color4': {'nd_name': 'ND_max_color4', 'nd': None}, 'vector2': {'nd_name': 'ND_max_vector2', 'nd': None}, 'vector3': {'nd_name': 'ND_max_vector3', 'nd': None}, 'vector4': {'nd_name': 'ND_max_vector4', 'nd': None}, 'color3FA': {'nd_name': 'ND_max_color3FA', 'nd': None}, 'color4FA': {'nd_name': 'ND_max_color4FA', 'nd': None}, 'vector2FA': {'nd_name': 'ND_max_vector2FA', 'nd': None}, 'vector3FA': {'nd_name': 'ND_max_vector3FA', 'nd': None}, 'vector4FA': {'nd_name': 'ND_max_vector4FA', 'nd': None}}

    bl_label = 'Max'
    bl_idname = 'usdhydra.MxNode_STD_max'
    bl_description = ""

    category = 'math'

    data_type: EnumProperty(name="Type", description="Input Data Type", items=[('float', 'Float', 'Float'), ('color3', 'Color3', 'Color3'), ('color4', 'Color4', 'Color4'), ('vector2', 'Vector2', 'Vector2'), ('vector3', 'Vector3', 'Vector3'), ('vector4', 'Vector4', 'Vector4'), ('color3FA', 'Color3FA', 'Color3FA'), ('color4FA', 'Color4FA', 'Color4FA'), ('vector2FA', 'Vector2FA', 'Vector2FA'), ('vector3FA', 'Vector3FA', 'Vector3FA'), ('vector4FA', 'Vector4FA', 'Vector4FA')], default='color3', update=MxNode.update_data_type)

    nd_float_in_in1: FloatProperty(name="In1", description="", default=0.0, update=MxNode.update_prop)
    nd_float_in_in2: FloatProperty(name="In2", description="", default=0.0, update=MxNode.update_prop)
    nd_float_out_out: FloatProperty(name="Out", description="", update=MxNode.update_prop)

    nd_color3_in_in1: FloatVectorProperty(name="In1", description="", subtype="COLOR", size=3, soft_min=0.0, soft_max=1.0, default=(0.0, 0.0, 0.0), update=MxNode.update_prop)
    nd_color3_in_in2: FloatVectorProperty(name="In2", description="", subtype="COLOR", size=3, soft_min=0.0, soft_max=1.0, default=(0.0, 0.0, 0.0), update=MxNode.update_prop)
    nd_color3_out_out: FloatVectorProperty(name="Out", description="", subtype="COLOR", size=3, soft_min=0.0, soft_max=1.0, update=MxNode.update_prop)

    nd_color4_in_in1: FloatVectorProperty(name="In1", description="", subtype="COLOR", size=4, soft_min=0.0, soft_max=1.0, default=(0.0, 0.0, 0.0, 0.0), update=MxNode.update_prop)
    nd_color4_in_in2: FloatVectorProperty(name="In2", description="", subtype="COLOR", size=4, soft_min=0.0, soft_max=1.0, default=(0.0, 0.0, 0.0, 0.0), update=MxNode.update_prop)
    nd_color4_out_out: FloatVectorProperty(name="Out", description="", subtype="COLOR", size=4, soft_min=0.0, soft_max=1.0, update=MxNode.update_prop)

    nd_vector2_in_in1: FloatVectorProperty(name="In1", description="", subtype="NONE", size=2, default=(0.0, 0.0), update=MxNode.update_prop)
    nd_vector2_in_in2: FloatVectorProperty(name="In2", description="", subtype="NONE", size=2, default=(0.0, 0.0), update=MxNode.update_prop)
    nd_vector2_out_out: FloatVectorProperty(name="Out", description="", subtype="NONE", size=2, update=MxNode.update_prop)

    nd_vector3_in_in1: FloatVectorProperty(name="In1", description="", subtype="XYZ", size=3, default=(0.0, 0.0, 0.0), update=MxNode.update_prop)
    nd_vector3_in_in2: FloatVectorProperty(name="In2", description="", subtype="XYZ", size=3, default=(0.0, 0.0, 0.0), update=MxNode.update_prop)
    nd_vector3_out_out: FloatVectorProperty(name="Out", description="", subtype="XYZ", size=3, update=MxNode.update_prop)

    nd_vector4_in_in1: FloatVectorProperty(name="In1", description="", subtype="NONE", size=4, default=(0.0, 0.0, 0.0, 0.0), update=MxNode.update_prop)
    nd_vector4_in_in2: FloatVectorProperty(name="In2", description="", subtype="NONE", size=4, default=(0.0, 0.0, 0.0, 0.0), update=MxNode.update_prop)
    nd_vector4_out_out: FloatVectorProperty(name="Out", description="", subtype="NONE", size=4, update=MxNode.update_prop)

    nd_color3FA_in_in1: FloatVectorProperty(name="In1", description="", subtype="COLOR", size=3, soft_min=0.0, soft_max=1.0, default=(0.0, 0.0, 0.0), update=MxNode.update_prop)
    nd_color3FA_in_in2: FloatProperty(name="In2", description="", default=0.0, update=MxNode.update_prop)
    nd_color3FA_out_out: FloatVectorProperty(name="Out", description="", subtype="COLOR", size=3, soft_min=0.0, soft_max=1.0, update=MxNode.update_prop)

    nd_color4FA_in_in1: FloatVectorProperty(name="In1", description="", subtype="COLOR", size=4, soft_min=0.0, soft_max=1.0, default=(0.0, 0.0, 0.0, 0.0), update=MxNode.update_prop)
    nd_color4FA_in_in2: FloatProperty(name="In2", description="", default=0.0, update=MxNode.update_prop)
    nd_color4FA_out_out: FloatVectorProperty(name="Out", description="", subtype="COLOR", size=4, soft_min=0.0, soft_max=1.0, update=MxNode.update_prop)

    nd_vector2FA_in_in1: FloatVectorProperty(name="In1", description="", subtype="NONE", size=2, default=(0.0, 0.0), update=MxNode.update_prop)
    nd_vector2FA_in_in2: FloatProperty(name="In2", description="", default=0.0, update=MxNode.update_prop)
    nd_vector2FA_out_out: FloatVectorProperty(name="Out", description="", subtype="NONE", size=2, update=MxNode.update_prop)

    nd_vector3FA_in_in1: FloatVectorProperty(name="In1", description="", subtype="XYZ", size=3, default=(0.0, 0.0, 0.0), update=MxNode.update_prop)
    nd_vector3FA_in_in2: FloatProperty(name="In2", description="", default=0.0, update=MxNode.update_prop)
    nd_vector3FA_out_out: FloatVectorProperty(name="Out", description="", subtype="XYZ", size=3, update=MxNode.update_prop)

    nd_vector4FA_in_in1: FloatVectorProperty(name="In1", description="", subtype="NONE", size=4, default=(0.0, 0.0, 0.0, 0.0), update=MxNode.update_prop)
    nd_vector4FA_in_in2: FloatProperty(name="In2", description="", default=0.0, update=MxNode.update_prop)
    nd_vector4FA_out_out: FloatVectorProperty(name="Out", description="", subtype="NONE", size=4, update=MxNode.update_prop)


class MxNode_STD_normalize(MxNode):
    _file_path = FILE_PATH
    _data_types = {'vector2': {'nd_name': 'ND_normalize_vector2', 'nd': None}, 'vector3': {'nd_name': 'ND_normalize_vector3', 'nd': None}, 'vector4': {'nd_name': 'ND_normalize_vector4', 'nd': None}}

    bl_label = 'Normalize'
    bl_idname = 'usdhydra.MxNode_STD_normalize'
    bl_description = ""

    category = 'math'

    data_type: EnumProperty(name="Type", description="Input Data Type", items=[('vector2', 'Vector2', 'Vector2'), ('vector3', 'Vector3', 'Vector3'), ('vector4', 'Vector4', 'Vector4')], default='vector2', update=MxNode.update_data_type)

    nd_vector2_in_in: FloatVectorProperty(name="In", description="", subtype="NONE", size=2, default=(0.0, 0.0), update=MxNode.update_prop)
    nd_vector2_out_out: FloatVectorProperty(name="Out", description="", subtype="NONE", size=2, update=MxNode.update_prop)

    nd_vector3_in_in: FloatVectorProperty(name="In", description="", subtype="XYZ", size=3, default=(0.0, 0.0, 0.0), update=MxNode.update_prop)
    nd_vector3_out_out: FloatVectorProperty(name="Out", description="", subtype="XYZ", size=3, update=MxNode.update_prop)

    nd_vector4_in_in: FloatVectorProperty(name="In", description="", subtype="NONE", size=4, default=(0.0, 0.0, 0.0, 0.0), update=MxNode.update_prop)
    nd_vector4_out_out: FloatVectorProperty(name="Out", description="", subtype="NONE", size=4, update=MxNode.update_prop)


class MxNode_STD_magnitude(MxNode):
    _file_path = FILE_PATH
    _data_types = {'vector2': {'nd_name': 'ND_magnitude_vector2', 'nd': None}, 'vector3': {'nd_name': 'ND_magnitude_vector3', 'nd': None}, 'vector4': {'nd_name': 'ND_magnitude_vector4', 'nd': None}}

    bl_label = 'Magnitude'
    bl_idname = 'usdhydra.MxNode_STD_magnitude'
    bl_description = ""

    category = 'math'

    data_type: EnumProperty(name="Type", description="Input Data Type", items=[('vector2', 'Vector2', 'Vector2'), ('vector3', 'Vector3', 'Vector3'), ('vector4', 'Vector4', 'Vector4')], default='vector2', update=MxNode.update_data_type)

    nd_vector2_in_in: FloatVectorProperty(name="In", description="", subtype="NONE", size=2, default=(0.0, 0.0), update=MxNode.update_prop)
    nd_vector2_out_out: FloatProperty(name="Out", description="", update=MxNode.update_prop)

    nd_vector3_in_in: FloatVectorProperty(name="In", description="", subtype="XYZ", size=3, default=(0.0, 0.0, 0.0), update=MxNode.update_prop)
    nd_vector3_out_out: FloatProperty(name="Out", description="", update=MxNode.update_prop)

    nd_vector4_in_in: FloatVectorProperty(name="In", description="", subtype="NONE", size=4, default=(0.0, 0.0, 0.0, 0.0), update=MxNode.update_prop)
    nd_vector4_out_out: FloatProperty(name="Out", description="", update=MxNode.update_prop)


class MxNode_STD_dotproduct(MxNode):
    _file_path = FILE_PATH
    _data_types = {'vector2': {'nd_name': 'ND_dotproduct_vector2', 'nd': None}, 'vector3': {'nd_name': 'ND_dotproduct_vector3', 'nd': None}, 'vector4': {'nd_name': 'ND_dotproduct_vector4', 'nd': None}}

    bl_label = 'Dotproduct'
    bl_idname = 'usdhydra.MxNode_STD_dotproduct'
    bl_description = ""

    category = 'math'

    data_type: EnumProperty(name="Type", description="Input Data Type", items=[('vector2', 'Vector2', 'Vector2'), ('vector3', 'Vector3', 'Vector3'), ('vector4', 'Vector4', 'Vector4')], default='vector2', update=MxNode.update_data_type)

    nd_vector2_in_in1: FloatVectorProperty(name="In1", description="", subtype="NONE", size=2, default=(0.0, 0.0), update=MxNode.update_prop)
    nd_vector2_in_in2: FloatVectorProperty(name="In2", description="", subtype="NONE", size=2, default=(0.0, 0.0), update=MxNode.update_prop)
    nd_vector2_out_out: FloatProperty(name="Out", description="", update=MxNode.update_prop)

    nd_vector3_in_in1: FloatVectorProperty(name="In1", description="", subtype="XYZ", size=3, default=(0.0, 0.0, 0.0), update=MxNode.update_prop)
    nd_vector3_in_in2: FloatVectorProperty(name="In2", description="", subtype="XYZ", size=3, default=(0.0, 0.0, 0.0), update=MxNode.update_prop)
    nd_vector3_out_out: FloatProperty(name="Out", description="", update=MxNode.update_prop)

    nd_vector4_in_in1: FloatVectorProperty(name="In1", description="", subtype="NONE", size=4, default=(0.0, 0.0, 0.0, 0.0), update=MxNode.update_prop)
    nd_vector4_in_in2: FloatVectorProperty(name="In2", description="", subtype="NONE", size=4, default=(0.0, 0.0, 0.0, 0.0), update=MxNode.update_prop)
    nd_vector4_out_out: FloatProperty(name="Out", description="", update=MxNode.update_prop)


class MxNode_STD_crossproduct(MxNode):
    _file_path = FILE_PATH
    _data_types = {'vector3': {'nd_name': 'ND_crossproduct_vector3', 'nd': None}}

    bl_label = 'Crossproduct'
    bl_idname = 'usdhydra.MxNode_STD_crossproduct'
    bl_description = ""

    category = 'math'

    data_type: EnumProperty(name="Type", description="Input Data Type", items=[('vector3', 'Vector3', 'Vector3')], default='vector3', update=MxNode.update_data_type)

    nd_vector3_in_in1: FloatVectorProperty(name="In1", description="", subtype="XYZ", size=3, default=(0.0, 0.0, 0.0), update=MxNode.update_prop)
    nd_vector3_in_in2: FloatVectorProperty(name="In2", description="", subtype="XYZ", size=3, default=(0.0, 0.0, 0.0), update=MxNode.update_prop)
    nd_vector3_out_out: FloatVectorProperty(name="Out", description="", subtype="XYZ", size=3, update=MxNode.update_prop)


class MxNode_STD_transformpoint(MxNode):
    _file_path = FILE_PATH
    _data_types = {'vector3': {'nd_name': 'ND_transformpoint_vector3', 'nd': None}}

    bl_label = 'Transformpoint'
    bl_idname = 'usdhydra.MxNode_STD_transformpoint'
    bl_description = ""

    category = 'math'

    data_type: EnumProperty(name="Type", description="Input Data Type", items=[('vector3', 'Vector3', 'Vector3')], default='vector3', update=MxNode.update_data_type)

    nd_vector3_in_in: FloatVectorProperty(name="In", description="", subtype="XYZ", size=3, default=(0.0, 0.0, 0.0), update=MxNode.update_prop)
    nd_vector3_in_fromspace: StringProperty(name="Fromspace", description="", default="", update=MxNode.update_prop)
    nd_vector3_in_tospace: StringProperty(name="Tospace", description="", default="", update=MxNode.update_prop)
    nd_vector3_out_out: FloatVectorProperty(name="Out", description="", subtype="XYZ", size=3, update=MxNode.update_prop)


class MxNode_STD_transformvector(MxNode):
    _file_path = FILE_PATH
    _data_types = {'vector3': {'nd_name': 'ND_transformvector_vector3', 'nd': None}}

    bl_label = 'Transformvector'
    bl_idname = 'usdhydra.MxNode_STD_transformvector'
    bl_description = ""

    category = 'math'

    data_type: EnumProperty(name="Type", description="Input Data Type", items=[('vector3', 'Vector3', 'Vector3')], default='vector3', update=MxNode.update_data_type)

    nd_vector3_in_in: FloatVectorProperty(name="In", description="", subtype="XYZ", size=3, default=(0.0, 0.0, 0.0), update=MxNode.update_prop)
    nd_vector3_in_fromspace: StringProperty(name="Fromspace", description="", default="", update=MxNode.update_prop)
    nd_vector3_in_tospace: StringProperty(name="Tospace", description="", default="", update=MxNode.update_prop)
    nd_vector3_out_out: FloatVectorProperty(name="Out", description="", subtype="XYZ", size=3, update=MxNode.update_prop)


class MxNode_STD_transformnormal(MxNode):
    _file_path = FILE_PATH
    _data_types = {'vector3': {'nd_name': 'ND_transformnormal_vector3', 'nd': None}}

    bl_label = 'Transformnormal'
    bl_idname = 'usdhydra.MxNode_STD_transformnormal'
    bl_description = ""

    category = 'math'

    data_type: EnumProperty(name="Type", description="Input Data Type", items=[('vector3', 'Vector3', 'Vector3')], default='vector3', update=MxNode.update_data_type)

    nd_vector3_in_in: FloatVectorProperty(name="In", description="", subtype="XYZ", size=3, default=(0.0, 0.0, 1.0), update=MxNode.update_prop)
    nd_vector3_in_fromspace: StringProperty(name="Fromspace", description="", default="", update=MxNode.update_prop)
    nd_vector3_in_tospace: StringProperty(name="Tospace", description="", default="", update=MxNode.update_prop)
    nd_vector3_out_out: FloatVectorProperty(name="Out", description="", subtype="XYZ", size=3, update=MxNode.update_prop)


class MxNode_STD_transformmatrix(MxNode):
    _file_path = FILE_PATH
    _data_types = {'vector2M3': {'nd_name': 'ND_transformmatrix_vector2M3', 'nd': None}, 'vector3': {'nd_name': 'ND_transformmatrix_vector3', 'nd': None}, 'vector3M4': {'nd_name': 'ND_transformmatrix_vector3M4', 'nd': None}, 'vector4': {'nd_name': 'ND_transformmatrix_vector4', 'nd': None}}

    bl_label = 'Transformmatrix'
    bl_idname = 'usdhydra.MxNode_STD_transformmatrix'
    bl_description = ""

    category = 'math'

    data_type: EnumProperty(name="Type", description="Input Data Type", items=[('vector2M3', 'Vector2M3', 'Vector2M3'), ('vector3', 'Vector3', 'Vector3'), ('vector3M4', 'Vector3M4', 'Vector3M4'), ('vector4', 'Vector4', 'Vector4')], default='vector2M3', update=MxNode.update_data_type)

    nd_vector2M3_in_in: FloatVectorProperty(name="In", description="", subtype="NONE", size=2, default=(0.0, 0.0), update=MxNode.update_prop)
    nd_vector2M3_in_mat: FloatVectorProperty(name="Mat", description="", subtype="MATRIX", size=9, default=(1.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 1.0), update=MxNode.update_prop)
    nd_vector2M3_out_out: FloatVectorProperty(name="Out", description="", subtype="NONE", size=2, update=MxNode.update_prop)

    nd_vector3_in_in: FloatVectorProperty(name="In", description="", subtype="XYZ", size=3, default=(0.0, 0.0, 0.0), update=MxNode.update_prop)
    nd_vector3_in_mat: FloatVectorProperty(name="Mat", description="", subtype="MATRIX", size=9, default=(1.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 1.0), update=MxNode.update_prop)
    nd_vector3_out_out: FloatVectorProperty(name="Out", description="", subtype="XYZ", size=3, update=MxNode.update_prop)

    nd_vector3M4_in_in: FloatVectorProperty(name="In", description="", subtype="XYZ", size=3, default=(0.0, 0.0, 0.0), update=MxNode.update_prop)
    nd_vector3M4_in_mat: FloatVectorProperty(name="Mat", description="", subtype="MATRIX", size=16, default=(1.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 1.0), update=MxNode.update_prop)
    nd_vector3M4_out_out: FloatVectorProperty(name="Out", description="", subtype="XYZ", size=3, update=MxNode.update_prop)

    nd_vector4_in_in: FloatVectorProperty(name="In", description="", subtype="NONE", size=4, default=(0.0, 0.0, 0.0, 0.0), update=MxNode.update_prop)
    nd_vector4_in_mat: FloatVectorProperty(name="Mat", description="", subtype="MATRIX", size=16, default=(1.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 1.0), update=MxNode.update_prop)
    nd_vector4_out_out: FloatVectorProperty(name="Out", description="", subtype="NONE", size=4, update=MxNode.update_prop)


class MxNode_STD_normalmap(MxNode):
    _file_path = FILE_PATH
    _data_types = {'vector3': {'nd_name': 'ND_normalmap', 'nd': None}}

    bl_label = 'Normalmap'
    bl_idname = 'usdhydra.MxNode_STD_normalmap'
    bl_description = ""

    category = 'math'

    data_type: EnumProperty(name="Type", description="Input Data Type", items=[('vector3', 'Vector3', 'Vector3')], default='vector3', update=MxNode.update_data_type)

    nd_vector3_in_in: FloatVectorProperty(name="In", description="", subtype="XYZ", size=3, default=(0.5, 0.5, 1.0), update=MxNode.update_prop)
    nd_vector3_in_space: EnumProperty(name="Space", description="", items=(('tangent', 'Tangent', 'Tangent'), ('object', 'Object', 'Object')), default="tangent", update=MxNode.update_prop)
    nd_vector3_in_scale: FloatProperty(name="Scale", description="", default=1.0, update=MxNode.update_prop)
    nd_vector3_in_normal: FloatVectorProperty(name="Normal", description="", subtype="XYZ", size=3, update=MxNode.update_prop)
    nd_vector3_in_tangent: FloatVectorProperty(name="Tangent", description="", subtype="XYZ", size=3, update=MxNode.update_prop)
    nd_vector3_out_out: FloatVectorProperty(name="Out", description="", subtype="XYZ", size=3, update=MxNode.update_prop)


class MxNode_STD_rotate2d(MxNode):
    _file_path = FILE_PATH
    _data_types = {'vector2': {'nd_name': 'ND_rotate2d_vector2', 'nd': None}}

    bl_label = 'Rotate2d'
    bl_idname = 'usdhydra.MxNode_STD_rotate2d'
    bl_description = ""

    category = 'math'

    data_type: EnumProperty(name="Type", description="Input Data Type", items=[('vector2', 'Vector2', 'Vector2')], default='vector2', update=MxNode.update_data_type)

    nd_vector2_in_in: FloatVectorProperty(name="In", description="", subtype="NONE", size=2, default=(0.0, 0.0), update=MxNode.update_prop)
    nd_vector2_in_amount: FloatProperty(name="Amount", description="", default=0.0, update=MxNode.update_prop)
    nd_vector2_out_out: FloatVectorProperty(name="Out", description="", subtype="NONE", size=2, update=MxNode.update_prop)


class MxNode_STD_rotate3d(MxNode):
    _file_path = FILE_PATH
    _data_types = {'vector3': {'nd_name': 'ND_rotate3d_vector3', 'nd': None}}

    bl_label = 'Rotate3d'
    bl_idname = 'usdhydra.MxNode_STD_rotate3d'
    bl_description = ""

    category = 'math'

    data_type: EnumProperty(name="Type", description="Input Data Type", items=[('vector3', 'Vector3', 'Vector3')], default='vector3', update=MxNode.update_data_type)

    nd_vector3_in_in: FloatVectorProperty(name="In", description="", subtype="XYZ", size=3, default=(0.0, 0.0, 0.0), update=MxNode.update_prop)
    nd_vector3_in_amount: FloatProperty(name="Amount", description="", default=0.0, update=MxNode.update_prop)
    nd_vector3_in_axis: FloatVectorProperty(name="Axis", description="", subtype="XYZ", size=3, default=(0.0, 1.0, 0.0), update=MxNode.update_prop)
    nd_vector3_out_out: FloatVectorProperty(name="Out", description="", subtype="XYZ", size=3, update=MxNode.update_prop)


class MxNode_STD_place2d(MxNode):
    _file_path = FILE_PATH
    _data_types = {'vector2': {'nd_name': 'ND_place2d_vector2', 'nd': None}}

    bl_label = 'Place2d'
    bl_idname = 'usdhydra.MxNode_STD_place2d'
    bl_description = ""

    category = 'math'

    data_type: EnumProperty(name="Type", description="Input Data Type", items=[('vector2', 'Vector2', 'Vector2')], default='vector2', update=MxNode.update_data_type)

    nd_vector2_in_texcoord: FloatVectorProperty(name="Texcoord", description="", subtype="NONE", size=2, default=(0.0, 0.0), update=MxNode.update_prop)
    nd_vector2_in_pivot: FloatVectorProperty(name="Pivot", description="", subtype="NONE", size=2, default=(0.0, 0.0), update=MxNode.update_prop)
    nd_vector2_in_scale: FloatVectorProperty(name="Scale", description="", subtype="NONE", size=2, default=(1.0, 1.0), update=MxNode.update_prop)
    nd_vector2_in_rotate: FloatProperty(name="Rotate", description="", default=0.0, update=MxNode.update_prop)
    nd_vector2_in_offset: FloatVectorProperty(name="Offset", description="", subtype="NONE", size=2, default=(0.0, 0.0), update=MxNode.update_prop)
    nd_vector2_out_out: FloatVectorProperty(name="Out", description="", subtype="NONE", size=2, update=MxNode.update_prop)


class MxNode_STD_arrayappend(MxNode):
    _file_path = FILE_PATH
    _data_types = {'integer_integerarray': {'nd_name': 'ND_arrayappend_integer_integerarray', 'nd': None}, 'integerarray_integerarray': {'nd_name': 'ND_arrayappend_integerarray_integerarray', 'nd': None}, 'float_floatarray': {'nd_name': 'ND_arrayappend_float_floatarray', 'nd': None}, 'floatarray_floatarray': {'nd_name': 'ND_arrayappend_floatarray_floatarray', 'nd': None}, 'color3_color3array': {'nd_name': 'ND_arrayappend_color3_color3array', 'nd': None}, 'color3array_color3array': {'nd_name': 'ND_arrayappend_color3array_color3array', 'nd': None}, 'color4_color4array': {'nd_name': 'ND_arrayappend_color4_color4array', 'nd': None}, 'color4array_color4array': {'nd_name': 'ND_arrayappend_color4array_color4array', 'nd': None}, 'vector2_vector2array': {'nd_name': 'ND_arrayappend_vector2_vector2array', 'nd': None}, 'vector2array_vector2array': {'nd_name': 'ND_arrayappend_vector2array_vector2array', 'nd': None}, 'vector3_vector3array': {'nd_name': 'ND_arrayappend_vector3_vector3array', 'nd': None}, 'vector3array_vector3array': {'nd_name': 'ND_arrayappend_vector3array_vector3array', 'nd': None}, 'vector4_vector4array': {'nd_name': 'ND_arrayappend_vector4_vector4array', 'nd': None}, 'vector4array_vector4array': {'nd_name': 'ND_arrayappend_vector4array_vector4array', 'nd': None}, 'string_stringarray': {'nd_name': 'ND_arrayappend_string_stringarray', 'nd': None}, 'stringarray_stringarray': {'nd_name': 'ND_arrayappend_stringarray_stringarray', 'nd': None}}

    bl_label = 'Arrayappend'
    bl_idname = 'usdhydra.MxNode_STD_arrayappend'
    bl_description = ""

    category = 'math'

    data_type: EnumProperty(name="Type", description="Input Data Type", items=[('integer_integerarray', 'Integer integerarray', 'Integer integerarray'), ('integerarray_integerarray', 'Integerarray integerarray', 'Integerarray integerarray'), ('float_floatarray', 'Float floatarray', 'Float floatarray'), ('floatarray_floatarray', 'Floatarray floatarray', 'Floatarray floatarray'), ('color3_color3array', 'Color3 color3array', 'Color3 color3array'), ('color3array_color3array', 'Color3array color3array', 'Color3array color3array'), ('color4_color4array', 'Color4 color4array', 'Color4 color4array'), ('color4array_color4array', 'Color4array color4array', 'Color4array color4array'), ('vector2_vector2array', 'Vector2 vector2array', 'Vector2 vector2array'), ('vector2array_vector2array', 'Vector2array vector2array', 'Vector2array vector2array'), ('vector3_vector3array', 'Vector3 vector3array', 'Vector3 vector3array'), ('vector3array_vector3array', 'Vector3array vector3array', 'Vector3array vector3array'), ('vector4_vector4array', 'Vector4 vector4array', 'Vector4 vector4array'), ('vector4array_vector4array', 'Vector4array vector4array', 'Vector4array vector4array'), ('string_stringarray', 'String stringarray', 'String stringarray'), ('stringarray_stringarray', 'Stringarray stringarray', 'Stringarray stringarray')], default='integer_integerarray', update=MxNode.update_data_type)

    nd_integer_integerarray_in_in1: IntProperty(name="In1", description="", default=0, update=MxNode.update_prop)
    nd_integer_integerarray_in_in2: IntProperty(name="In2", description="", default=0, update=MxNode.update_prop)
    nd_integer_integerarray_out_out: StringProperty(name="Out", description="", update=MxNode.update_prop)

    nd_integerarray_integerarray_in_in1: StringProperty(name="In1", description="", default="", update=MxNode.update_prop)
    nd_integerarray_integerarray_in_in2: IntProperty(name="In2", description="", default=0, update=MxNode.update_prop)
    nd_integerarray_integerarray_out_out: StringProperty(name="Out", description="", update=MxNode.update_prop)

    nd_float_floatarray_in_in1: FloatProperty(name="In1", description="", default=0.0, update=MxNode.update_prop)
    nd_float_floatarray_in_in2: FloatProperty(name="In2", description="", default=0.0, update=MxNode.update_prop)
    nd_float_floatarray_out_out: StringProperty(name="Out", description="", update=MxNode.update_prop)

    nd_floatarray_floatarray_in_in1: StringProperty(name="In1", description="", default="", update=MxNode.update_prop)
    nd_floatarray_floatarray_in_in2: FloatProperty(name="In2", description="", default=0.0, update=MxNode.update_prop)
    nd_floatarray_floatarray_out_out: StringProperty(name="Out", description="", update=MxNode.update_prop)

    nd_color3_color3array_in_in1: FloatVectorProperty(name="In1", description="", subtype="COLOR", size=3, soft_min=0.0, soft_max=1.0, default=(0.0, 0.0, 0.0), update=MxNode.update_prop)
    nd_color3_color3array_in_in2: FloatVectorProperty(name="In2", description="", subtype="COLOR", size=3, soft_min=0.0, soft_max=1.0, default=(0.0, 0.0, 0.0), update=MxNode.update_prop)
    nd_color3_color3array_out_out: StringProperty(name="Out", description="", update=MxNode.update_prop)

    nd_color3array_color3array_in_in1: StringProperty(name="In1", description="", default="", update=MxNode.update_prop)
    nd_color3array_color3array_in_in2: FloatVectorProperty(name="In2", description="", subtype="COLOR", size=3, soft_min=0.0, soft_max=1.0, default=(0.0, 0.0, 0.0), update=MxNode.update_prop)
    nd_color3array_color3array_out_out: StringProperty(name="Out", description="", update=MxNode.update_prop)

    nd_color4_color4array_in_in1: FloatVectorProperty(name="In1", description="", subtype="COLOR", size=4, soft_min=0.0, soft_max=1.0, default=(0.0, 0.0, 0.0, 0.0), update=MxNode.update_prop)
    nd_color4_color4array_in_in2: FloatVectorProperty(name="In2", description="", subtype="COLOR", size=4, soft_min=0.0, soft_max=1.0, default=(0.0, 0.0, 0.0, 0.0), update=MxNode.update_prop)
    nd_color4_color4array_out_out: StringProperty(name="Out", description="", update=MxNode.update_prop)

    nd_color4array_color4array_in_in1: StringProperty(name="In1", description="", default="", update=MxNode.update_prop)
    nd_color4array_color4array_in_in2: FloatVectorProperty(name="In2", description="", subtype="COLOR", size=4, soft_min=0.0, soft_max=1.0, default=(0.0, 0.0, 0.0, 0.0), update=MxNode.update_prop)
    nd_color4array_color4array_out_out: StringProperty(name="Out", description="", update=MxNode.update_prop)

    nd_vector2_vector2array_in_in1: FloatVectorProperty(name="In1", description="", subtype="NONE", size=2, default=(0.0, 0.0), update=MxNode.update_prop)
    nd_vector2_vector2array_in_in2: FloatVectorProperty(name="In2", description="", subtype="NONE", size=2, default=(0.0, 0.0), update=MxNode.update_prop)
    nd_vector2_vector2array_out_out: StringProperty(name="Out", description="", update=MxNode.update_prop)

    nd_vector2array_vector2array_in_in1: StringProperty(name="In1", description="", default="", update=MxNode.update_prop)
    nd_vector2array_vector2array_in_in2: FloatVectorProperty(name="In2", description="", subtype="NONE", size=2, default=(0.0, 0.0), update=MxNode.update_prop)
    nd_vector2array_vector2array_out_out: StringProperty(name="Out", description="", update=MxNode.update_prop)

    nd_vector3_vector3array_in_in1: FloatVectorProperty(name="In1", description="", subtype="XYZ", size=3, default=(0.0, 0.0, 0.0), update=MxNode.update_prop)
    nd_vector3_vector3array_in_in2: FloatVectorProperty(name="In2", description="", subtype="XYZ", size=3, default=(0.0, 0.0, 0.0), update=MxNode.update_prop)
    nd_vector3_vector3array_out_out: StringProperty(name="Out", description="", update=MxNode.update_prop)

    nd_vector3array_vector3array_in_in1: StringProperty(name="In1", description="", default="", update=MxNode.update_prop)
    nd_vector3array_vector3array_in_in2: FloatVectorProperty(name="In2", description="", subtype="XYZ", size=3, default=(0.0, 0.0, 0.0), update=MxNode.update_prop)
    nd_vector3array_vector3array_out_out: StringProperty(name="Out", description="", update=MxNode.update_prop)

    nd_vector4_vector4array_in_in1: FloatVectorProperty(name="In1", description="", subtype="NONE", size=4, default=(0.0, 0.0, 0.0, 0.0), update=MxNode.update_prop)
    nd_vector4_vector4array_in_in2: FloatVectorProperty(name="In2", description="", subtype="NONE", size=4, default=(0.0, 0.0, 0.0, 0.0), update=MxNode.update_prop)
    nd_vector4_vector4array_out_out: StringProperty(name="Out", description="", update=MxNode.update_prop)

    nd_vector4array_vector4array_in_in1: StringProperty(name="In1", description="", default="", update=MxNode.update_prop)
    nd_vector4array_vector4array_in_in2: FloatVectorProperty(name="In2", description="", subtype="NONE", size=4, default=(0.0, 0.0, 0.0, 0.0), update=MxNode.update_prop)
    nd_vector4array_vector4array_out_out: StringProperty(name="Out", description="", update=MxNode.update_prop)

    nd_string_stringarray_in_in1: StringProperty(name="In1", description="", default="", update=MxNode.update_prop)
    nd_string_stringarray_in_in2: StringProperty(name="In2", description="", default="", update=MxNode.update_prop)
    nd_string_stringarray_out_out: StringProperty(name="Out", description="", update=MxNode.update_prop)

    nd_stringarray_stringarray_in_in1: StringProperty(name="In1", description="", default="", update=MxNode.update_prop)
    nd_stringarray_stringarray_in_in2: StringProperty(name="In2", description="", default="", update=MxNode.update_prop)
    nd_stringarray_stringarray_out_out: StringProperty(name="Out", description="", update=MxNode.update_prop)


class MxNode_STD_remap(MxNode):
    _file_path = FILE_PATH
    _data_types = {'float': {'nd_name': 'ND_remap_float', 'nd': None}, 'color3': {'nd_name': 'ND_remap_color3', 'nd': None}, 'color4': {'nd_name': 'ND_remap_color4', 'nd': None}, 'vector2': {'nd_name': 'ND_remap_vector2', 'nd': None}, 'vector3': {'nd_name': 'ND_remap_vector3', 'nd': None}, 'vector4': {'nd_name': 'ND_remap_vector4', 'nd': None}, 'color3FA': {'nd_name': 'ND_remap_color3FA', 'nd': None}, 'color4FA': {'nd_name': 'ND_remap_color4FA', 'nd': None}, 'vector2FA': {'nd_name': 'ND_remap_vector2FA', 'nd': None}, 'vector3FA': {'nd_name': 'ND_remap_vector3FA', 'nd': None}, 'vector4FA': {'nd_name': 'ND_remap_vector4FA', 'nd': None}}

    bl_label = 'Remap'
    bl_idname = 'usdhydra.MxNode_STD_remap'
    bl_description = ""

    category = 'adjustment'

    data_type: EnumProperty(name="Type", description="Input Data Type", items=[('float', 'Float', 'Float'), ('color3', 'Color3', 'Color3'), ('color4', 'Color4', 'Color4'), ('vector2', 'Vector2', 'Vector2'), ('vector3', 'Vector3', 'Vector3'), ('vector4', 'Vector4', 'Vector4'), ('color3FA', 'Color3FA', 'Color3FA'), ('color4FA', 'Color4FA', 'Color4FA'), ('vector2FA', 'Vector2FA', 'Vector2FA'), ('vector3FA', 'Vector3FA', 'Vector3FA'), ('vector4FA', 'Vector4FA', 'Vector4FA')], default='color3', update=MxNode.update_data_type)

    nd_float_in_in: FloatProperty(name="In", description="", default=0.0, update=MxNode.update_prop)
    nd_float_in_inlow: FloatProperty(name="Inlow", description="", default=0.0, update=MxNode.update_prop)
    nd_float_in_inhigh: FloatProperty(name="Inhigh", description="", default=1.0, update=MxNode.update_prop)
    nd_float_in_outlow: FloatProperty(name="Outlow", description="", default=0.0, update=MxNode.update_prop)
    nd_float_in_outhigh: FloatProperty(name="Outhigh", description="", default=1.0, update=MxNode.update_prop)
    nd_float_out_out: FloatProperty(name="Out", description="", update=MxNode.update_prop)

    nd_color3_in_in: FloatVectorProperty(name="In", description="", subtype="COLOR", size=3, soft_min=0.0, soft_max=1.0, default=(0.0, 0.0, 0.0), update=MxNode.update_prop)
    nd_color3_in_inlow: FloatVectorProperty(name="Inlow", description="", subtype="COLOR", size=3, soft_min=0.0, soft_max=1.0, default=(0.0, 0.0, 0.0), update=MxNode.update_prop)
    nd_color3_in_inhigh: FloatVectorProperty(name="Inhigh", description="", subtype="COLOR", size=3, soft_min=0.0, soft_max=1.0, default=(1.0, 1.0, 1.0), update=MxNode.update_prop)
    nd_color3_in_outlow: FloatVectorProperty(name="Outlow", description="", subtype="COLOR", size=3, soft_min=0.0, soft_max=1.0, default=(0.0, 0.0, 0.0), update=MxNode.update_prop)
    nd_color3_in_outhigh: FloatVectorProperty(name="Outhigh", description="", subtype="COLOR", size=3, soft_min=0.0, soft_max=1.0, default=(1.0, 1.0, 1.0), update=MxNode.update_prop)
    nd_color3_out_out: FloatVectorProperty(name="Out", description="", subtype="COLOR", size=3, soft_min=0.0, soft_max=1.0, update=MxNode.update_prop)

    nd_color4_in_in: FloatVectorProperty(name="In", description="", subtype="COLOR", size=4, soft_min=0.0, soft_max=1.0, default=(0.0, 0.0, 0.0, 0.0), update=MxNode.update_prop)
    nd_color4_in_inlow: FloatVectorProperty(name="Inlow", description="", subtype="COLOR", size=4, soft_min=0.0, soft_max=1.0, default=(0.0, 0.0, 0.0, 0.0), update=MxNode.update_prop)
    nd_color4_in_inhigh: FloatVectorProperty(name="Inhigh", description="", subtype="COLOR", size=4, soft_min=0.0, soft_max=1.0, default=(1.0, 1.0, 1.0, 1.0), update=MxNode.update_prop)
    nd_color4_in_outlow: FloatVectorProperty(name="Outlow", description="", subtype="COLOR", size=4, soft_min=0.0, soft_max=1.0, default=(0.0, 0.0, 0.0, 0.0), update=MxNode.update_prop)
    nd_color4_in_outhigh: FloatVectorProperty(name="Outhigh", description="", subtype="COLOR", size=4, soft_min=0.0, soft_max=1.0, default=(1.0, 1.0, 1.0, 1.0), update=MxNode.update_prop)
    nd_color4_out_out: FloatVectorProperty(name="Out", description="", subtype="COLOR", size=4, soft_min=0.0, soft_max=1.0, update=MxNode.update_prop)

    nd_vector2_in_in: FloatVectorProperty(name="In", description="", subtype="NONE", size=2, default=(0.0, 0.0), update=MxNode.update_prop)
    nd_vector2_in_inlow: FloatVectorProperty(name="Inlow", description="", subtype="NONE", size=2, default=(0.0, 0.0), update=MxNode.update_prop)
    nd_vector2_in_inhigh: FloatVectorProperty(name="Inhigh", description="", subtype="NONE", size=2, default=(1.0, 1.0), update=MxNode.update_prop)
    nd_vector2_in_outlow: FloatVectorProperty(name="Outlow", description="", subtype="NONE", size=2, default=(0.0, 0.0), update=MxNode.update_prop)
    nd_vector2_in_outhigh: FloatVectorProperty(name="Outhigh", description="", subtype="NONE", size=2, default=(1.0, 1.0), update=MxNode.update_prop)
    nd_vector2_out_out: FloatVectorProperty(name="Out", description="", subtype="NONE", size=2, update=MxNode.update_prop)

    nd_vector3_in_in: FloatVectorProperty(name="In", description="", subtype="XYZ", size=3, default=(0.0, 0.0, 0.0), update=MxNode.update_prop)
    nd_vector3_in_inlow: FloatVectorProperty(name="Inlow", description="", subtype="XYZ", size=3, default=(0.0, 0.0, 0.0), update=MxNode.update_prop)
    nd_vector3_in_inhigh: FloatVectorProperty(name="Inhigh", description="", subtype="XYZ", size=3, default=(1.0, 1.0, 1.0), update=MxNode.update_prop)
    nd_vector3_in_outlow: FloatVectorProperty(name="Outlow", description="", subtype="XYZ", size=3, default=(0.0, 0.0, 0.0), update=MxNode.update_prop)
    nd_vector3_in_outhigh: FloatVectorProperty(name="Outhigh", description="", subtype="XYZ", size=3, default=(1.0, 1.0, 1.0), update=MxNode.update_prop)
    nd_vector3_out_out: FloatVectorProperty(name="Out", description="", subtype="XYZ", size=3, update=MxNode.update_prop)

    nd_vector4_in_in: FloatVectorProperty(name="In", description="", subtype="NONE", size=4, default=(0.0, 0.0, 0.0, 0.0), update=MxNode.update_prop)
    nd_vector4_in_inlow: FloatVectorProperty(name="Inlow", description="", subtype="NONE", size=4, default=(0.0, 0.0, 0.0, 0.0), update=MxNode.update_prop)
    nd_vector4_in_inhigh: FloatVectorProperty(name="Inhigh", description="", subtype="NONE", size=4, default=(1.0, 1.0, 1.0, 1.0), update=MxNode.update_prop)
    nd_vector4_in_outlow: FloatVectorProperty(name="Outlow", description="", subtype="NONE", size=4, default=(0.0, 0.0, 0.0, 0.0), update=MxNode.update_prop)
    nd_vector4_in_outhigh: FloatVectorProperty(name="Outhigh", description="", subtype="NONE", size=4, default=(1.0, 1.0, 1.0, 1.0), update=MxNode.update_prop)
    nd_vector4_out_out: FloatVectorProperty(name="Out", description="", subtype="NONE", size=4, update=MxNode.update_prop)

    nd_color3FA_in_in: FloatVectorProperty(name="In", description="", subtype="COLOR", size=3, soft_min=0.0, soft_max=1.0, default=(0.0, 0.0, 0.0), update=MxNode.update_prop)
    nd_color3FA_in_inlow: FloatProperty(name="Inlow", description="", default=0.0, update=MxNode.update_prop)
    nd_color3FA_in_inhigh: FloatProperty(name="Inhigh", description="", default=1.0, update=MxNode.update_prop)
    nd_color3FA_in_outlow: FloatProperty(name="Outlow", description="", default=0.0, update=MxNode.update_prop)
    nd_color3FA_in_outhigh: FloatProperty(name="Outhigh", description="", default=1.0, update=MxNode.update_prop)
    nd_color3FA_out_out: FloatVectorProperty(name="Out", description="", subtype="COLOR", size=3, soft_min=0.0, soft_max=1.0, update=MxNode.update_prop)

    nd_color4FA_in_in: FloatVectorProperty(name="In", description="", subtype="COLOR", size=4, soft_min=0.0, soft_max=1.0, default=(0.0, 0.0, 0.0, 0.0), update=MxNode.update_prop)
    nd_color4FA_in_inlow: FloatProperty(name="Inlow", description="", default=0.0, update=MxNode.update_prop)
    nd_color4FA_in_inhigh: FloatProperty(name="Inhigh", description="", default=1.0, update=MxNode.update_prop)
    nd_color4FA_in_outlow: FloatProperty(name="Outlow", description="", default=0.0, update=MxNode.update_prop)
    nd_color4FA_in_outhigh: FloatProperty(name="Outhigh", description="", default=1.0, update=MxNode.update_prop)
    nd_color4FA_out_out: FloatVectorProperty(name="Out", description="", subtype="COLOR", size=4, soft_min=0.0, soft_max=1.0, update=MxNode.update_prop)

    nd_vector2FA_in_in: FloatVectorProperty(name="In", description="", subtype="NONE", size=2, default=(0.0, 0.0), update=MxNode.update_prop)
    nd_vector2FA_in_inlow: FloatProperty(name="Inlow", description="", default=0.0, update=MxNode.update_prop)
    nd_vector2FA_in_inhigh: FloatProperty(name="Inhigh", description="", default=1.0, update=MxNode.update_prop)
    nd_vector2FA_in_outlow: FloatProperty(name="Outlow", description="", default=0.0, update=MxNode.update_prop)
    nd_vector2FA_in_outhigh: FloatProperty(name="Outhigh", description="", default=1.0, update=MxNode.update_prop)
    nd_vector2FA_out_out: FloatVectorProperty(name="Out", description="", subtype="NONE", size=2, update=MxNode.update_prop)

    nd_vector3FA_in_in: FloatVectorProperty(name="In", description="", subtype="XYZ", size=3, default=(0.0, 0.0, 0.0), update=MxNode.update_prop)
    nd_vector3FA_in_inlow: FloatProperty(name="Inlow", description="", default=0.0, update=MxNode.update_prop)
    nd_vector3FA_in_inhigh: FloatProperty(name="Inhigh", description="", default=1.0, update=MxNode.update_prop)
    nd_vector3FA_in_outlow: FloatProperty(name="Outlow", description="", default=0.0, update=MxNode.update_prop)
    nd_vector3FA_in_outhigh: FloatProperty(name="Outhigh", description="", default=1.0, update=MxNode.update_prop)
    nd_vector3FA_out_out: FloatVectorProperty(name="Out", description="", subtype="XYZ", size=3, update=MxNode.update_prop)

    nd_vector4FA_in_in: FloatVectorProperty(name="In", description="", subtype="NONE", size=4, default=(0.0, 0.0, 0.0, 0.0), update=MxNode.update_prop)
    nd_vector4FA_in_inlow: FloatProperty(name="Inlow", description="", default=0.0, update=MxNode.update_prop)
    nd_vector4FA_in_inhigh: FloatProperty(name="Inhigh", description="", default=1.0, update=MxNode.update_prop)
    nd_vector4FA_in_outlow: FloatProperty(name="Outlow", description="", default=0.0, update=MxNode.update_prop)
    nd_vector4FA_in_outhigh: FloatProperty(name="Outhigh", description="", default=1.0, update=MxNode.update_prop)
    nd_vector4FA_out_out: FloatVectorProperty(name="Out", description="", subtype="NONE", size=4, update=MxNode.update_prop)


class MxNode_STD_smoothstep(MxNode):
    _file_path = FILE_PATH
    _data_types = {'float': {'nd_name': 'ND_smoothstep_float', 'nd': None}, 'color3': {'nd_name': 'ND_smoothstep_color3', 'nd': None}, 'color4': {'nd_name': 'ND_smoothstep_color4', 'nd': None}, 'vector2': {'nd_name': 'ND_smoothstep_vector2', 'nd': None}, 'vector3': {'nd_name': 'ND_smoothstep_vector3', 'nd': None}, 'vector4': {'nd_name': 'ND_smoothstep_vector4', 'nd': None}, 'color3FA': {'nd_name': 'ND_smoothstep_color3FA', 'nd': None}, 'color4FA': {'nd_name': 'ND_smoothstep_color4FA', 'nd': None}, 'vector2FA': {'nd_name': 'ND_smoothstep_vector2FA', 'nd': None}, 'vector3FA': {'nd_name': 'ND_smoothstep_vector3FA', 'nd': None}, 'vector4FA': {'nd_name': 'ND_smoothstep_vector4FA', 'nd': None}}

    bl_label = 'Smoothstep'
    bl_idname = 'usdhydra.MxNode_STD_smoothstep'
    bl_description = ""

    category = 'adjustment'

    data_type: EnumProperty(name="Type", description="Input Data Type", items=[('float', 'Float', 'Float'), ('color3', 'Color3', 'Color3'), ('color4', 'Color4', 'Color4'), ('vector2', 'Vector2', 'Vector2'), ('vector3', 'Vector3', 'Vector3'), ('vector4', 'Vector4', 'Vector4'), ('color3FA', 'Color3FA', 'Color3FA'), ('color4FA', 'Color4FA', 'Color4FA'), ('vector2FA', 'Vector2FA', 'Vector2FA'), ('vector3FA', 'Vector3FA', 'Vector3FA'), ('vector4FA', 'Vector4FA', 'Vector4FA')], default='color3', update=MxNode.update_data_type)

    nd_float_in_in: FloatProperty(name="In", description="", default=0.0, update=MxNode.update_prop)
    nd_float_in_low: FloatProperty(name="Low", description="", default=0.0, update=MxNode.update_prop)
    nd_float_in_high: FloatProperty(name="High", description="", default=1.0, update=MxNode.update_prop)
    nd_float_out_out: FloatProperty(name="Out", description="", update=MxNode.update_prop)

    nd_color3_in_in: FloatVectorProperty(name="In", description="", subtype="COLOR", size=3, soft_min=0.0, soft_max=1.0, default=(0.0, 0.0, 0.0), update=MxNode.update_prop)
    nd_color3_in_low: FloatVectorProperty(name="Low", description="", subtype="COLOR", size=3, soft_min=0.0, soft_max=1.0, default=(0.0, 0.0, 0.0), update=MxNode.update_prop)
    nd_color3_in_high: FloatVectorProperty(name="High", description="", subtype="COLOR", size=3, soft_min=0.0, soft_max=1.0, default=(1.0, 1.0, 1.0), update=MxNode.update_prop)
    nd_color3_out_out: FloatVectorProperty(name="Out", description="", subtype="COLOR", size=3, soft_min=0.0, soft_max=1.0, update=MxNode.update_prop)

    nd_color4_in_in: FloatVectorProperty(name="In", description="", subtype="COLOR", size=4, soft_min=0.0, soft_max=1.0, default=(0.0, 0.0, 0.0, 0.0), update=MxNode.update_prop)
    nd_color4_in_low: FloatVectorProperty(name="Low", description="", subtype="COLOR", size=4, soft_min=0.0, soft_max=1.0, default=(0.0, 0.0, 0.0, 0.0), update=MxNode.update_prop)
    nd_color4_in_high: FloatVectorProperty(name="High", description="", subtype="COLOR", size=4, soft_min=0.0, soft_max=1.0, default=(1.0, 1.0, 1.0, 1.0), update=MxNode.update_prop)
    nd_color4_out_out: FloatVectorProperty(name="Out", description="", subtype="COLOR", size=4, soft_min=0.0, soft_max=1.0, update=MxNode.update_prop)

    nd_vector2_in_in: FloatVectorProperty(name="In", description="", subtype="NONE", size=2, default=(0.0, 0.0), update=MxNode.update_prop)
    nd_vector2_in_low: FloatVectorProperty(name="Low", description="", subtype="NONE", size=2, default=(0.0, 0.0), update=MxNode.update_prop)
    nd_vector2_in_high: FloatVectorProperty(name="High", description="", subtype="NONE", size=2, default=(1.0, 1.0), update=MxNode.update_prop)
    nd_vector2_out_out: FloatVectorProperty(name="Out", description="", subtype="NONE", size=2, update=MxNode.update_prop)

    nd_vector3_in_in: FloatVectorProperty(name="In", description="", subtype="XYZ", size=3, default=(0.0, 0.0, 0.0), update=MxNode.update_prop)
    nd_vector3_in_low: FloatVectorProperty(name="Low", description="", subtype="XYZ", size=3, default=(0.0, 0.0, 0.0), update=MxNode.update_prop)
    nd_vector3_in_high: FloatVectorProperty(name="High", description="", subtype="XYZ", size=3, default=(1.0, 1.0, 1.0), update=MxNode.update_prop)
    nd_vector3_out_out: FloatVectorProperty(name="Out", description="", subtype="XYZ", size=3, update=MxNode.update_prop)

    nd_vector4_in_in: FloatVectorProperty(name="In", description="", subtype="NONE", size=4, default=(0.0, 0.0, 0.0, 0.0), update=MxNode.update_prop)
    nd_vector4_in_low: FloatVectorProperty(name="Low", description="", subtype="NONE", size=4, default=(0.0, 0.0, 0.0, 0.0), update=MxNode.update_prop)
    nd_vector4_in_high: FloatVectorProperty(name="High", description="", subtype="NONE", size=4, default=(1.0, 1.0, 1.0, 1.0), update=MxNode.update_prop)
    nd_vector4_out_out: FloatVectorProperty(name="Out", description="", subtype="NONE", size=4, update=MxNode.update_prop)

    nd_color3FA_in_in: FloatVectorProperty(name="In", description="", subtype="COLOR", size=3, soft_min=0.0, soft_max=1.0, default=(0.0, 0.0, 0.0), update=MxNode.update_prop)
    nd_color3FA_in_low: FloatProperty(name="Low", description="", default=0.0, update=MxNode.update_prop)
    nd_color3FA_in_high: FloatProperty(name="High", description="", default=1.0, update=MxNode.update_prop)
    nd_color3FA_out_out: FloatVectorProperty(name="Out", description="", subtype="COLOR", size=3, soft_min=0.0, soft_max=1.0, update=MxNode.update_prop)

    nd_color4FA_in_in: FloatVectorProperty(name="In", description="", subtype="COLOR", size=4, soft_min=0.0, soft_max=1.0, default=(0.0, 0.0, 0.0, 0.0), update=MxNode.update_prop)
    nd_color4FA_in_low: FloatProperty(name="Low", description="", default=0.0, update=MxNode.update_prop)
    nd_color4FA_in_high: FloatProperty(name="High", description="", default=1.0, update=MxNode.update_prop)
    nd_color4FA_out_out: FloatVectorProperty(name="Out", description="", subtype="COLOR", size=4, soft_min=0.0, soft_max=1.0, update=MxNode.update_prop)

    nd_vector2FA_in_in: FloatVectorProperty(name="In", description="", subtype="NONE", size=2, default=(0.0, 0.0), update=MxNode.update_prop)
    nd_vector2FA_in_low: FloatProperty(name="Low", description="", default=0.0, update=MxNode.update_prop)
    nd_vector2FA_in_high: FloatProperty(name="High", description="", default=1.0, update=MxNode.update_prop)
    nd_vector2FA_out_out: FloatVectorProperty(name="Out", description="", subtype="NONE", size=2, update=MxNode.update_prop)

    nd_vector3FA_in_in: FloatVectorProperty(name="In", description="", subtype="XYZ", size=3, default=(0.0, 0.0, 0.0), update=MxNode.update_prop)
    nd_vector3FA_in_low: FloatProperty(name="Low", description="", default=0.0, update=MxNode.update_prop)
    nd_vector3FA_in_high: FloatProperty(name="High", description="", default=1.0, update=MxNode.update_prop)
    nd_vector3FA_out_out: FloatVectorProperty(name="Out", description="", subtype="XYZ", size=3, update=MxNode.update_prop)

    nd_vector4FA_in_in: FloatVectorProperty(name="In", description="", subtype="NONE", size=4, default=(0.0, 0.0, 0.0, 0.0), update=MxNode.update_prop)
    nd_vector4FA_in_low: FloatProperty(name="Low", description="", default=0.0, update=MxNode.update_prop)
    nd_vector4FA_in_high: FloatProperty(name="High", description="", default=1.0, update=MxNode.update_prop)
    nd_vector4FA_out_out: FloatVectorProperty(name="Out", description="", subtype="NONE", size=4, update=MxNode.update_prop)


class MxNode_STD_curveadjust(MxNode):
    _file_path = FILE_PATH
    _data_types = {'float': {'nd_name': 'ND_curveadjust_float', 'nd': None}, 'color3': {'nd_name': 'ND_curveadjust_color3', 'nd': None}, 'color4': {'nd_name': 'ND_curveadjust_color4', 'nd': None}, 'vector2': {'nd_name': 'ND_curveadjust_vector2', 'nd': None}, 'vector3': {'nd_name': 'ND_curveadjust_vector3', 'nd': None}, 'vector4': {'nd_name': 'ND_curveadjust_vector4', 'nd': None}}

    bl_label = 'Curveadjust'
    bl_idname = 'usdhydra.MxNode_STD_curveadjust'
    bl_description = ""

    category = 'adjustment'

    data_type: EnumProperty(name="Type", description="Input Data Type", items=[('float', 'Float', 'Float'), ('color3', 'Color3', 'Color3'), ('color4', 'Color4', 'Color4'), ('vector2', 'Vector2', 'Vector2'), ('vector3', 'Vector3', 'Vector3'), ('vector4', 'Vector4', 'Vector4')], default='color3', update=MxNode.update_data_type)

    nd_float_in_in: FloatProperty(name="In", description="", default=0.0, update=MxNode.update_prop)
    nd_float_in_knots: StringProperty(name="Knots", description="", default="", update=MxNode.update_prop)
    nd_float_out_out: FloatProperty(name="Out", description="", update=MxNode.update_prop)

    nd_color3_in_in: FloatVectorProperty(name="In", description="", subtype="COLOR", size=3, soft_min=0.0, soft_max=1.0, default=(0.0, 0.0, 0.0), update=MxNode.update_prop)
    nd_color3_in_knots: StringProperty(name="Knots", description="", default="", update=MxNode.update_prop)
    nd_color3_out_out: FloatVectorProperty(name="Out", description="", subtype="COLOR", size=3, soft_min=0.0, soft_max=1.0, update=MxNode.update_prop)

    nd_color4_in_in: FloatVectorProperty(name="In", description="", subtype="COLOR", size=4, soft_min=0.0, soft_max=1.0, default=(0.0, 0.0, 0.0, 0.0), update=MxNode.update_prop)
    nd_color4_in_knots: StringProperty(name="Knots", description="", default="", update=MxNode.update_prop)
    nd_color4_out_out: FloatVectorProperty(name="Out", description="", subtype="COLOR", size=4, soft_min=0.0, soft_max=1.0, update=MxNode.update_prop)

    nd_vector2_in_in: FloatVectorProperty(name="In", description="", subtype="NONE", size=2, default=(0.0, 0.0), update=MxNode.update_prop)
    nd_vector2_in_knots: StringProperty(name="Knots", description="", default="", update=MxNode.update_prop)
    nd_vector2_out_out: FloatVectorProperty(name="Out", description="", subtype="NONE", size=2, update=MxNode.update_prop)

    nd_vector3_in_in: FloatVectorProperty(name="In", description="", subtype="XYZ", size=3, default=(0.0, 0.0, 0.0), update=MxNode.update_prop)
    nd_vector3_in_knots: StringProperty(name="Knots", description="", default="", update=MxNode.update_prop)
    nd_vector3_out_out: FloatVectorProperty(name="Out", description="", subtype="XYZ", size=3, update=MxNode.update_prop)

    nd_vector4_in_in: FloatVectorProperty(name="In", description="", subtype="NONE", size=4, default=(0.0, 0.0, 0.0, 0.0), update=MxNode.update_prop)
    nd_vector4_in_knots: StringProperty(name="Knots", description="", default="", update=MxNode.update_prop)
    nd_vector4_out_out: FloatVectorProperty(name="Out", description="", subtype="NONE", size=4, update=MxNode.update_prop)


class MxNode_STD_luminance(MxNode):
    _file_path = FILE_PATH
    _data_types = {'color3': {'nd_name': 'ND_luminance_color3', 'nd': None}, 'color4': {'nd_name': 'ND_luminance_color4', 'nd': None}}

    bl_label = 'Luminance'
    bl_idname = 'usdhydra.MxNode_STD_luminance'
    bl_description = ""

    category = 'adjustment'

    data_type: EnumProperty(name="Type", description="Input Data Type", items=[('color3', 'Color3', 'Color3'), ('color4', 'Color4', 'Color4')], default='color3', update=MxNode.update_data_type)

    nd_color3_in_in: FloatVectorProperty(name="In", description="", subtype="COLOR", size=3, soft_min=0.0, soft_max=1.0, default=(0.0, 0.0, 0.0), update=MxNode.update_prop)
    nd_color3_in_lumacoeffs: FloatVectorProperty(name="Lumacoeffs", description="", subtype="COLOR", size=3, soft_min=0.0, soft_max=1.0, default=(0.2722287, 0.6740818, 0.0536895), update=MxNode.update_prop)
    nd_color3_out_out: FloatVectorProperty(name="Out", description="", subtype="COLOR", size=3, soft_min=0.0, soft_max=1.0, update=MxNode.update_prop)

    nd_color4_in_in: FloatVectorProperty(name="In", description="", subtype="COLOR", size=4, soft_min=0.0, soft_max=1.0, default=(0.0, 0.0, 0.0, 0.0), update=MxNode.update_prop)
    nd_color4_in_lumacoeffs: FloatVectorProperty(name="Lumacoeffs", description="", subtype="COLOR", size=3, soft_min=0.0, soft_max=1.0, default=(0.2722287, 0.6740818, 0.0536895), update=MxNode.update_prop)
    nd_color4_out_out: FloatVectorProperty(name="Out", description="", subtype="COLOR", size=4, soft_min=0.0, soft_max=1.0, update=MxNode.update_prop)


class MxNode_STD_rgbtohsv(MxNode):
    _file_path = FILE_PATH
    _data_types = {'color3': {'nd_name': 'ND_rgbtohsv_color3', 'nd': None}, 'color4': {'nd_name': 'ND_rgbtohsv_color4', 'nd': None}}

    bl_label = 'Rgbtohsv'
    bl_idname = 'usdhydra.MxNode_STD_rgbtohsv'
    bl_description = ""

    category = 'adjustment'

    data_type: EnumProperty(name="Type", description="Input Data Type", items=[('color3', 'Color3', 'Color3'), ('color4', 'Color4', 'Color4')], default='color3', update=MxNode.update_data_type)

    nd_color3_in_in: FloatVectorProperty(name="In", description="", subtype="COLOR", size=3, soft_min=0.0, soft_max=1.0, default=(0.0, 0.0, 0.0), update=MxNode.update_prop)
    nd_color3_out_out: FloatVectorProperty(name="Out", description="", subtype="COLOR", size=3, soft_min=0.0, soft_max=1.0, update=MxNode.update_prop)

    nd_color4_in_in: FloatVectorProperty(name="In", description="", subtype="COLOR", size=4, soft_min=0.0, soft_max=1.0, default=(0.0, 0.0, 0.0, 0.0), update=MxNode.update_prop)
    nd_color4_out_out: FloatVectorProperty(name="Out", description="", subtype="COLOR", size=4, soft_min=0.0, soft_max=1.0, update=MxNode.update_prop)


class MxNode_STD_hsvtorgb(MxNode):
    _file_path = FILE_PATH
    _data_types = {'color3': {'nd_name': 'ND_hsvtorgb_color3', 'nd': None}, 'color4': {'nd_name': 'ND_hsvtorgb_color4', 'nd': None}}

    bl_label = 'Hsvtorgb'
    bl_idname = 'usdhydra.MxNode_STD_hsvtorgb'
    bl_description = ""

    category = 'adjustment'

    data_type: EnumProperty(name="Type", description="Input Data Type", items=[('color3', 'Color3', 'Color3'), ('color4', 'Color4', 'Color4')], default='color3', update=MxNode.update_data_type)

    nd_color3_in_in: FloatVectorProperty(name="In", description="", subtype="COLOR", size=3, soft_min=0.0, soft_max=1.0, default=(0.0, 0.0, 0.0), update=MxNode.update_prop)
    nd_color3_out_out: FloatVectorProperty(name="Out", description="", subtype="COLOR", size=3, soft_min=0.0, soft_max=1.0, update=MxNode.update_prop)

    nd_color4_in_in: FloatVectorProperty(name="In", description="", subtype="COLOR", size=4, soft_min=0.0, soft_max=1.0, default=(0.0, 0.0, 0.0, 0.0), update=MxNode.update_prop)
    nd_color4_out_out: FloatVectorProperty(name="Out", description="", subtype="COLOR", size=4, soft_min=0.0, soft_max=1.0, update=MxNode.update_prop)


class MxNode_STD_contrast(MxNode):
    _file_path = FILE_PATH
    _data_types = {'float': {'nd_name': 'ND_contrast_float', 'nd': None}, 'color3': {'nd_name': 'ND_contrast_color3', 'nd': None}, 'color4': {'nd_name': 'ND_contrast_color4', 'nd': None}, 'vector2': {'nd_name': 'ND_contrast_vector2', 'nd': None}, 'vector3': {'nd_name': 'ND_contrast_vector3', 'nd': None}, 'vector4': {'nd_name': 'ND_contrast_vector4', 'nd': None}, 'color3FA': {'nd_name': 'ND_contrast_color3FA', 'nd': None}, 'color4FA': {'nd_name': 'ND_contrast_color4FA', 'nd': None}, 'vector2FA': {'nd_name': 'ND_contrast_vector2FA', 'nd': None}, 'vector3FA': {'nd_name': 'ND_contrast_vector3FA', 'nd': None}, 'vector4FA': {'nd_name': 'ND_contrast_vector4FA', 'nd': None}}

    bl_label = 'Contrast'
    bl_idname = 'usdhydra.MxNode_STD_contrast'
    bl_description = ""

    category = 'adjustment'

    data_type: EnumProperty(name="Type", description="Input Data Type", items=[('float', 'Float', 'Float'), ('color3', 'Color3', 'Color3'), ('color4', 'Color4', 'Color4'), ('vector2', 'Vector2', 'Vector2'), ('vector3', 'Vector3', 'Vector3'), ('vector4', 'Vector4', 'Vector4'), ('color3FA', 'Color3FA', 'Color3FA'), ('color4FA', 'Color4FA', 'Color4FA'), ('vector2FA', 'Vector2FA', 'Vector2FA'), ('vector3FA', 'Vector3FA', 'Vector3FA'), ('vector4FA', 'Vector4FA', 'Vector4FA')], default='color3', update=MxNode.update_data_type)

    nd_float_in_in: FloatProperty(name="In", description="", default=0.0, update=MxNode.update_prop)
    nd_float_in_amount: FloatProperty(name="Amount", description="", default=1.0, update=MxNode.update_prop)
    nd_float_in_pivot: FloatProperty(name="Pivot", description="", default=0.5, update=MxNode.update_prop)
    nd_float_out_out: FloatProperty(name="Out", description="", update=MxNode.update_prop)

    nd_color3_in_in: FloatVectorProperty(name="In", description="", subtype="COLOR", size=3, soft_min=0.0, soft_max=1.0, default=(0.0, 0.0, 0.0), update=MxNode.update_prop)
    nd_color3_in_amount: FloatVectorProperty(name="Amount", description="", subtype="COLOR", size=3, soft_min=0.0, soft_max=1.0, default=(1.0, 1.0, 1.0), update=MxNode.update_prop)
    nd_color3_in_pivot: FloatVectorProperty(name="Pivot", description="", subtype="COLOR", size=3, soft_min=0.0, soft_max=1.0, default=(0.5, 0.5, 0.5), update=MxNode.update_prop)
    nd_color3_out_out: FloatVectorProperty(name="Out", description="", subtype="COLOR", size=3, soft_min=0.0, soft_max=1.0, update=MxNode.update_prop)

    nd_color4_in_in: FloatVectorProperty(name="In", description="", subtype="COLOR", size=4, soft_min=0.0, soft_max=1.0, default=(0.0, 0.0, 0.0, 0.0), update=MxNode.update_prop)
    nd_color4_in_amount: FloatVectorProperty(name="Amount", description="", subtype="COLOR", size=4, soft_min=0.0, soft_max=1.0, default=(1.0, 1.0, 1.0, 1.0), update=MxNode.update_prop)
    nd_color4_in_pivot: FloatVectorProperty(name="Pivot", description="", subtype="COLOR", size=4, soft_min=0.0, soft_max=1.0, default=(0.5, 0.5, 0.5, 0.5), update=MxNode.update_prop)
    nd_color4_out_out: FloatVectorProperty(name="Out", description="", subtype="COLOR", size=4, soft_min=0.0, soft_max=1.0, update=MxNode.update_prop)

    nd_vector2_in_in: FloatVectorProperty(name="In", description="", subtype="NONE", size=2, default=(0.0, 0.0), update=MxNode.update_prop)
    nd_vector2_in_amount: FloatVectorProperty(name="Amount", description="", subtype="NONE", size=2, default=(1.0, 1.0), update=MxNode.update_prop)
    nd_vector2_in_pivot: FloatVectorProperty(name="Pivot", description="", subtype="NONE", size=2, default=(0.5, 0.5), update=MxNode.update_prop)
    nd_vector2_out_out: FloatVectorProperty(name="Out", description="", subtype="NONE", size=2, update=MxNode.update_prop)

    nd_vector3_in_in: FloatVectorProperty(name="In", description="", subtype="XYZ", size=3, default=(0.0, 0.0, 0.0), update=MxNode.update_prop)
    nd_vector3_in_amount: FloatVectorProperty(name="Amount", description="", subtype="XYZ", size=3, default=(1.0, 1.0, 1.0), update=MxNode.update_prop)
    nd_vector3_in_pivot: FloatVectorProperty(name="Pivot", description="", subtype="XYZ", size=3, default=(0.5, 0.5, 0.5), update=MxNode.update_prop)
    nd_vector3_out_out: FloatVectorProperty(name="Out", description="", subtype="XYZ", size=3, update=MxNode.update_prop)

    nd_vector4_in_in: FloatVectorProperty(name="In", description="", subtype="NONE", size=4, default=(0.0, 0.0, 0.0, 0.0), update=MxNode.update_prop)
    nd_vector4_in_amount: FloatVectorProperty(name="Amount", description="", subtype="NONE", size=4, default=(1.0, 1.0, 1.0, 1.0), update=MxNode.update_prop)
    nd_vector4_in_pivot: FloatVectorProperty(name="Pivot", description="", subtype="NONE", size=4, default=(0.5, 0.5, 0.5, 0.5), update=MxNode.update_prop)
    nd_vector4_out_out: FloatVectorProperty(name="Out", description="", subtype="NONE", size=4, update=MxNode.update_prop)

    nd_color3FA_in_in: FloatVectorProperty(name="In", description="", subtype="COLOR", size=3, soft_min=0.0, soft_max=1.0, default=(0.0, 0.0, 0.0), update=MxNode.update_prop)
    nd_color3FA_in_amount: FloatProperty(name="Amount", description="", default=1.0, update=MxNode.update_prop)
    nd_color3FA_in_pivot: FloatProperty(name="Pivot", description="", default=0.5, update=MxNode.update_prop)
    nd_color3FA_out_out: FloatVectorProperty(name="Out", description="", subtype="COLOR", size=3, soft_min=0.0, soft_max=1.0, update=MxNode.update_prop)

    nd_color4FA_in_in: FloatVectorProperty(name="In", description="", subtype="COLOR", size=4, soft_min=0.0, soft_max=1.0, default=(0.0, 0.0, 0.0, 0.0), update=MxNode.update_prop)
    nd_color4FA_in_amount: FloatProperty(name="Amount", description="", default=1.0, update=MxNode.update_prop)
    nd_color4FA_in_pivot: FloatProperty(name="Pivot", description="", default=0.5, update=MxNode.update_prop)
    nd_color4FA_out_out: FloatVectorProperty(name="Out", description="", subtype="COLOR", size=4, soft_min=0.0, soft_max=1.0, update=MxNode.update_prop)

    nd_vector2FA_in_in: FloatVectorProperty(name="In", description="", subtype="NONE", size=2, default=(0.0, 0.0), update=MxNode.update_prop)
    nd_vector2FA_in_amount: FloatProperty(name="Amount", description="", default=1.0, update=MxNode.update_prop)
    nd_vector2FA_in_pivot: FloatProperty(name="Pivot", description="", default=0.5, update=MxNode.update_prop)
    nd_vector2FA_out_out: FloatVectorProperty(name="Out", description="", subtype="NONE", size=2, update=MxNode.update_prop)

    nd_vector3FA_in_in: FloatVectorProperty(name="In", description="", subtype="XYZ", size=3, default=(0.0, 0.0, 0.0), update=MxNode.update_prop)
    nd_vector3FA_in_amount: FloatProperty(name="Amount", description="", default=1.0, update=MxNode.update_prop)
    nd_vector3FA_in_pivot: FloatProperty(name="Pivot", description="", default=0.5, update=MxNode.update_prop)
    nd_vector3FA_out_out: FloatVectorProperty(name="Out", description="", subtype="XYZ", size=3, update=MxNode.update_prop)

    nd_vector4FA_in_in: FloatVectorProperty(name="In", description="", subtype="NONE", size=4, default=(0.0, 0.0, 0.0, 0.0), update=MxNode.update_prop)
    nd_vector4FA_in_amount: FloatProperty(name="Amount", description="", default=1.0, update=MxNode.update_prop)
    nd_vector4FA_in_pivot: FloatProperty(name="Pivot", description="", default=0.5, update=MxNode.update_prop)
    nd_vector4FA_out_out: FloatVectorProperty(name="Out", description="", subtype="NONE", size=4, update=MxNode.update_prop)


class MxNode_STD_range(MxNode):
    _file_path = FILE_PATH
    _data_types = {'float': {'nd_name': 'ND_range_float', 'nd': None}, 'color3': {'nd_name': 'ND_range_color3', 'nd': None}, 'color4': {'nd_name': 'ND_range_color4', 'nd': None}, 'vector2': {'nd_name': 'ND_range_vector2', 'nd': None}, 'vector3': {'nd_name': 'ND_range_vector3', 'nd': None}, 'vector4': {'nd_name': 'ND_range_vector4', 'nd': None}, 'color3FA': {'nd_name': 'ND_range_color3FA', 'nd': None}, 'color4FA': {'nd_name': 'ND_range_color4FA', 'nd': None}, 'vector2FA': {'nd_name': 'ND_range_vector2FA', 'nd': None}, 'vector3FA': {'nd_name': 'ND_range_vector3FA', 'nd': None}, 'vector4FA': {'nd_name': 'ND_range_vector4FA', 'nd': None}}

    bl_label = 'Range'
    bl_idname = 'usdhydra.MxNode_STD_range'
    bl_description = ""

    category = 'adjustment'

    data_type: EnumProperty(name="Type", description="Input Data Type", items=[('float', 'Float', 'Float'), ('color3', 'Color3', 'Color3'), ('color4', 'Color4', 'Color4'), ('vector2', 'Vector2', 'Vector2'), ('vector3', 'Vector3', 'Vector3'), ('vector4', 'Vector4', 'Vector4'), ('color3FA', 'Color3FA', 'Color3FA'), ('color4FA', 'Color4FA', 'Color4FA'), ('vector2FA', 'Vector2FA', 'Vector2FA'), ('vector3FA', 'Vector3FA', 'Vector3FA'), ('vector4FA', 'Vector4FA', 'Vector4FA')], default='color3', update=MxNode.update_data_type)

    nd_float_in_in: FloatProperty(name="In", description="", default=0.0, update=MxNode.update_prop)
    nd_float_in_inlow: FloatProperty(name="Inlow", description="", default=0.0, update=MxNode.update_prop)
    nd_float_in_inhigh: FloatProperty(name="Inhigh", description="", default=1.0, update=MxNode.update_prop)
    nd_float_in_gamma: FloatProperty(name="Gamma", description="", default=1.0, update=MxNode.update_prop)
    nd_float_in_outlow: FloatProperty(name="Outlow", description="", default=0.0, update=MxNode.update_prop)
    nd_float_in_outhigh: FloatProperty(name="Outhigh", description="", default=1.0, update=MxNode.update_prop)
    nd_float_in_doclamp: BoolProperty(name="Doclamp", description="", default=False, update=MxNode.update_prop)
    nd_float_out_out: FloatProperty(name="Out", description="", update=MxNode.update_prop)

    nd_color3_in_in: FloatVectorProperty(name="In", description="", subtype="COLOR", size=3, soft_min=0.0, soft_max=1.0, default=(0.0, 0.0, 0.0), update=MxNode.update_prop)
    nd_color3_in_inlow: FloatVectorProperty(name="Inlow", description="", subtype="COLOR", size=3, soft_min=0.0, soft_max=1.0, default=(0.0, 0.0, 0.0), update=MxNode.update_prop)
    nd_color3_in_inhigh: FloatVectorProperty(name="Inhigh", description="", subtype="COLOR", size=3, soft_min=0.0, soft_max=1.0, default=(1.0, 1.0, 1.0), update=MxNode.update_prop)
    nd_color3_in_gamma: FloatVectorProperty(name="Gamma", description="", subtype="COLOR", size=3, soft_min=0.0, soft_max=1.0, default=(1.0, 1.0, 1.0), update=MxNode.update_prop)
    nd_color3_in_outlow: FloatVectorProperty(name="Outlow", description="", subtype="COLOR", size=3, soft_min=0.0, soft_max=1.0, default=(0.0, 0.0, 0.0), update=MxNode.update_prop)
    nd_color3_in_outhigh: FloatVectorProperty(name="Outhigh", description="", subtype="COLOR", size=3, soft_min=0.0, soft_max=1.0, default=(1.0, 1.0, 1.0), update=MxNode.update_prop)
    nd_color3_in_doclamp: BoolProperty(name="Doclamp", description="", default=False, update=MxNode.update_prop)
    nd_color3_out_out: FloatVectorProperty(name="Out", description="", subtype="COLOR", size=3, soft_min=0.0, soft_max=1.0, update=MxNode.update_prop)

    nd_color4_in_in: FloatVectorProperty(name="In", description="", subtype="COLOR", size=4, soft_min=0.0, soft_max=1.0, default=(0.0, 0.0, 0.0, 0.0), update=MxNode.update_prop)
    nd_color4_in_inlow: FloatVectorProperty(name="Inlow", description="", subtype="COLOR", size=4, soft_min=0.0, soft_max=1.0, default=(0.0, 0.0, 0.0, 0.0), update=MxNode.update_prop)
    nd_color4_in_inhigh: FloatVectorProperty(name="Inhigh", description="", subtype="COLOR", size=4, soft_min=0.0, soft_max=1.0, default=(1.0, 1.0, 1.0, 1.0), update=MxNode.update_prop)
    nd_color4_in_gamma: FloatVectorProperty(name="Gamma", description="", subtype="COLOR", size=4, soft_min=0.0, soft_max=1.0, default=(1.0, 1.0, 1.0, 1.0), update=MxNode.update_prop)
    nd_color4_in_outlow: FloatVectorProperty(name="Outlow", description="", subtype="COLOR", size=4, soft_min=0.0, soft_max=1.0, default=(0.0, 0.0, 0.0, 0.0), update=MxNode.update_prop)
    nd_color4_in_outhigh: FloatVectorProperty(name="Outhigh", description="", subtype="COLOR", size=4, soft_min=0.0, soft_max=1.0, default=(1.0, 1.0, 1.0, 1.0), update=MxNode.update_prop)
    nd_color4_in_doclamp: BoolProperty(name="Doclamp", description="", default=False, update=MxNode.update_prop)
    nd_color4_out_out: FloatVectorProperty(name="Out", description="", subtype="COLOR", size=4, soft_min=0.0, soft_max=1.0, update=MxNode.update_prop)

    nd_vector2_in_in: FloatVectorProperty(name="In", description="", subtype="NONE", size=2, default=(0.0, 0.0), update=MxNode.update_prop)
    nd_vector2_in_inlow: FloatVectorProperty(name="Inlow", description="", subtype="NONE", size=2, default=(0.0, 0.0), update=MxNode.update_prop)
    nd_vector2_in_inhigh: FloatVectorProperty(name="Inhigh", description="", subtype="NONE", size=2, default=(1.0, 1.0), update=MxNode.update_prop)
    nd_vector2_in_gamma: FloatVectorProperty(name="Gamma", description="", subtype="NONE", size=2, default=(1.0, 1.0), update=MxNode.update_prop)
    nd_vector2_in_outlow: FloatVectorProperty(name="Outlow", description="", subtype="NONE", size=2, default=(0.0, 0.0), update=MxNode.update_prop)
    nd_vector2_in_outhigh: FloatVectorProperty(name="Outhigh", description="", subtype="NONE", size=2, default=(1.0, 1.0), update=MxNode.update_prop)
    nd_vector2_in_doclamp: BoolProperty(name="Doclamp", description="", default=False, update=MxNode.update_prop)
    nd_vector2_out_out: FloatVectorProperty(name="Out", description="", subtype="NONE", size=2, update=MxNode.update_prop)

    nd_vector3_in_in: FloatVectorProperty(name="In", description="", subtype="XYZ", size=3, default=(0.0, 0.0, 0.0), update=MxNode.update_prop)
    nd_vector3_in_inlow: FloatVectorProperty(name="Inlow", description="", subtype="XYZ", size=3, default=(0.0, 0.0, 0.0), update=MxNode.update_prop)
    nd_vector3_in_inhigh: FloatVectorProperty(name="Inhigh", description="", subtype="XYZ", size=3, default=(1.0, 1.0, 1.0), update=MxNode.update_prop)
    nd_vector3_in_gamma: FloatVectorProperty(name="Gamma", description="", subtype="XYZ", size=3, default=(1.0, 1.0, 1.0), update=MxNode.update_prop)
    nd_vector3_in_outlow: FloatVectorProperty(name="Outlow", description="", subtype="XYZ", size=3, default=(0.0, 0.0, 0.0), update=MxNode.update_prop)
    nd_vector3_in_outhigh: FloatVectorProperty(name="Outhigh", description="", subtype="XYZ", size=3, default=(1.0, 1.0, 1.0), update=MxNode.update_prop)
    nd_vector3_in_doclamp: BoolProperty(name="Doclamp", description="", default=False, update=MxNode.update_prop)
    nd_vector3_out_out: FloatVectorProperty(name="Out", description="", subtype="XYZ", size=3, update=MxNode.update_prop)

    nd_vector4_in_in: FloatVectorProperty(name="In", description="", subtype="NONE", size=4, default=(0.0, 0.0, 0.0, 0.0), update=MxNode.update_prop)
    nd_vector4_in_inlow: FloatVectorProperty(name="Inlow", description="", subtype="NONE", size=4, default=(0.0, 0.0, 0.0, 0.0), update=MxNode.update_prop)
    nd_vector4_in_inhigh: FloatVectorProperty(name="Inhigh", description="", subtype="NONE", size=4, default=(1.0, 1.0, 1.0, 1.0), update=MxNode.update_prop)
    nd_vector4_in_gamma: FloatVectorProperty(name="Gamma", description="", subtype="NONE", size=4, default=(1.0, 1.0, 1.0, 1.0), update=MxNode.update_prop)
    nd_vector4_in_outlow: FloatVectorProperty(name="Outlow", description="", subtype="NONE", size=4, default=(0.0, 0.0, 0.0, 0.0), update=MxNode.update_prop)
    nd_vector4_in_outhigh: FloatVectorProperty(name="Outhigh", description="", subtype="NONE", size=4, default=(1.0, 1.0, 1.0, 1.0), update=MxNode.update_prop)
    nd_vector4_in_doclamp: BoolProperty(name="Doclamp", description="", default=False, update=MxNode.update_prop)
    nd_vector4_out_out: FloatVectorProperty(name="Out", description="", subtype="NONE", size=4, update=MxNode.update_prop)

    nd_color3FA_in_in: FloatVectorProperty(name="In", description="", subtype="COLOR", size=3, soft_min=0.0, soft_max=1.0, default=(0.0, 0.0, 0.0), update=MxNode.update_prop)
    nd_color3FA_in_inlow: FloatProperty(name="Inlow", description="", default=0.0, update=MxNode.update_prop)
    nd_color3FA_in_inhigh: FloatProperty(name="Inhigh", description="", default=1.0, update=MxNode.update_prop)
    nd_color3FA_in_gamma: FloatProperty(name="Gamma", description="", default=1.0, update=MxNode.update_prop)
    nd_color3FA_in_outlow: FloatProperty(name="Outlow", description="", default=0.0, update=MxNode.update_prop)
    nd_color3FA_in_outhigh: FloatProperty(name="Outhigh", description="", default=1.0, update=MxNode.update_prop)
    nd_color3FA_in_doclamp: BoolProperty(name="Doclamp", description="", default=False, update=MxNode.update_prop)
    nd_color3FA_out_out: FloatVectorProperty(name="Out", description="", subtype="COLOR", size=3, soft_min=0.0, soft_max=1.0, update=MxNode.update_prop)

    nd_color4FA_in_in: FloatVectorProperty(name="In", description="", subtype="COLOR", size=4, soft_min=0.0, soft_max=1.0, default=(0.0, 0.0, 0.0, 0.0), update=MxNode.update_prop)
    nd_color4FA_in_inlow: FloatProperty(name="Inlow", description="", default=0.0, update=MxNode.update_prop)
    nd_color4FA_in_inhigh: FloatProperty(name="Inhigh", description="", default=1.0, update=MxNode.update_prop)
    nd_color4FA_in_gamma: FloatProperty(name="Gamma", description="", default=1.0, update=MxNode.update_prop)
    nd_color4FA_in_outlow: FloatProperty(name="Outlow", description="", default=0.0, update=MxNode.update_prop)
    nd_color4FA_in_outhigh: FloatProperty(name="Outhigh", description="", default=1.0, update=MxNode.update_prop)
    nd_color4FA_in_doclamp: BoolProperty(name="Doclamp", description="", default=False, update=MxNode.update_prop)
    nd_color4FA_out_out: FloatVectorProperty(name="Out", description="", subtype="COLOR", size=4, soft_min=0.0, soft_max=1.0, update=MxNode.update_prop)

    nd_vector2FA_in_in: FloatVectorProperty(name="In", description="", subtype="NONE", size=2, default=(0.0, 0.0), update=MxNode.update_prop)
    nd_vector2FA_in_inlow: FloatProperty(name="Inlow", description="", default=0.0, update=MxNode.update_prop)
    nd_vector2FA_in_inhigh: FloatProperty(name="Inhigh", description="", default=1.0, update=MxNode.update_prop)
    nd_vector2FA_in_gamma: FloatProperty(name="Gamma", description="", default=1.0, update=MxNode.update_prop)
    nd_vector2FA_in_outlow: FloatProperty(name="Outlow", description="", default=0.0, update=MxNode.update_prop)
    nd_vector2FA_in_outhigh: FloatProperty(name="Outhigh", description="", default=1.0, update=MxNode.update_prop)
    nd_vector2FA_in_doclamp: BoolProperty(name="Doclamp", description="", default=False, update=MxNode.update_prop)
    nd_vector2FA_out_out: FloatVectorProperty(name="Out", description="", subtype="NONE", size=2, update=MxNode.update_prop)

    nd_vector3FA_in_in: FloatVectorProperty(name="In", description="", subtype="XYZ", size=3, default=(0.0, 0.0, 0.0), update=MxNode.update_prop)
    nd_vector3FA_in_inlow: FloatProperty(name="Inlow", description="", default=0.0, update=MxNode.update_prop)
    nd_vector3FA_in_inhigh: FloatProperty(name="Inhigh", description="", default=1.0, update=MxNode.update_prop)
    nd_vector3FA_in_gamma: FloatProperty(name="Gamma", description="", default=1.0, update=MxNode.update_prop)
    nd_vector3FA_in_outlow: FloatProperty(name="Outlow", description="", default=0.0, update=MxNode.update_prop)
    nd_vector3FA_in_outhigh: FloatProperty(name="Outhigh", description="", default=1.0, update=MxNode.update_prop)
    nd_vector3FA_in_doclamp: BoolProperty(name="Doclamp", description="", default=False, update=MxNode.update_prop)
    nd_vector3FA_out_out: FloatVectorProperty(name="Out", description="", subtype="XYZ", size=3, update=MxNode.update_prop)

    nd_vector4FA_in_in: FloatVectorProperty(name="In", description="", subtype="NONE", size=4, default=(0.0, 0.0, 0.0, 0.0), update=MxNode.update_prop)
    nd_vector4FA_in_inlow: FloatProperty(name="Inlow", description="", default=0.0, update=MxNode.update_prop)
    nd_vector4FA_in_inhigh: FloatProperty(name="Inhigh", description="", default=1.0, update=MxNode.update_prop)
    nd_vector4FA_in_gamma: FloatProperty(name="Gamma", description="", default=1.0, update=MxNode.update_prop)
    nd_vector4FA_in_outlow: FloatProperty(name="Outlow", description="", default=0.0, update=MxNode.update_prop)
    nd_vector4FA_in_outhigh: FloatProperty(name="Outhigh", description="", default=1.0, update=MxNode.update_prop)
    nd_vector4FA_in_doclamp: BoolProperty(name="Doclamp", description="", default=False, update=MxNode.update_prop)
    nd_vector4FA_out_out: FloatVectorProperty(name="Out", description="", subtype="NONE", size=4, update=MxNode.update_prop)


class MxNode_STD_hsvadjust(MxNode):
    _file_path = FILE_PATH
    _data_types = {'color3': {'nd_name': 'ND_hsvadjust_color3', 'nd': None}, 'color4': {'nd_name': 'ND_hsvadjust_color4', 'nd': None}}

    bl_label = 'Hsvadjust'
    bl_idname = 'usdhydra.MxNode_STD_hsvadjust'
    bl_description = ""

    category = 'adjustment'

    data_type: EnumProperty(name="Type", description="Input Data Type", items=[('color3', 'Color3', 'Color3'), ('color4', 'Color4', 'Color4')], default='color3', update=MxNode.update_data_type)

    nd_color3_in_in: FloatVectorProperty(name="In", description="", subtype="COLOR", size=3, soft_min=0.0, soft_max=1.0, default=(0.0, 0.0, 0.0), update=MxNode.update_prop)
    nd_color3_in_amount: FloatVectorProperty(name="Amount", description="", subtype="XYZ", size=3, default=(0.0, 1.0, 1.0), update=MxNode.update_prop)
    nd_color3_out_out: FloatVectorProperty(name="Out", description="", subtype="COLOR", size=3, soft_min=0.0, soft_max=1.0, update=MxNode.update_prop)

    nd_color4_in_in: FloatVectorProperty(name="In", description="", subtype="COLOR", size=4, soft_min=0.0, soft_max=1.0, default=(0.0, 0.0, 0.0, 0.0), update=MxNode.update_prop)
    nd_color4_in_amount: FloatVectorProperty(name="Amount", description="", subtype="XYZ", size=3, default=(0.0, 1.0, 1.0), update=MxNode.update_prop)
    nd_color4_out_out: FloatVectorProperty(name="Out", description="", subtype="COLOR", size=4, soft_min=0.0, soft_max=1.0, update=MxNode.update_prop)


class MxNode_STD_saturate(MxNode):
    _file_path = FILE_PATH
    _data_types = {'color3': {'nd_name': 'ND_saturate_color3', 'nd': None}, 'color4': {'nd_name': 'ND_saturate_color4', 'nd': None}}

    bl_label = 'Saturate'
    bl_idname = 'usdhydra.MxNode_STD_saturate'
    bl_description = ""

    category = 'adjustment'

    data_type: EnumProperty(name="Type", description="Input Data Type", items=[('color3', 'Color3', 'Color3'), ('color4', 'Color4', 'Color4')], default='color3', update=MxNode.update_data_type)

    nd_color3_in_in: FloatVectorProperty(name="In", description="", subtype="COLOR", size=3, soft_min=0.0, soft_max=1.0, default=(0.0, 0.0, 0.0), update=MxNode.update_prop)
    nd_color3_in_amount: FloatProperty(name="Amount", description="", default=1.0, update=MxNode.update_prop)
    nd_color3_in_lumacoeffs: FloatVectorProperty(name="Lumacoeffs", description="", subtype="COLOR", size=3, soft_min=0.0, soft_max=1.0, default=(0.2722287, 0.6740818, 0.0536895), update=MxNode.update_prop)
    nd_color3_out_out: FloatVectorProperty(name="Out", description="", subtype="COLOR", size=3, soft_min=0.0, soft_max=1.0, update=MxNode.update_prop)

    nd_color4_in_in: FloatVectorProperty(name="In", description="", subtype="COLOR", size=4, soft_min=0.0, soft_max=1.0, default=(0.0, 0.0, 0.0, 0.0), update=MxNode.update_prop)
    nd_color4_in_amount: FloatProperty(name="Amount", description="", default=1.0, update=MxNode.update_prop)
    nd_color4_in_lumacoeffs: FloatVectorProperty(name="Lumacoeffs", description="", subtype="COLOR", size=3, soft_min=0.0, soft_max=1.0, default=(0.2722287, 0.6740818, 0.0536895), update=MxNode.update_prop)
    nd_color4_out_out: FloatVectorProperty(name="Out", description="", subtype="COLOR", size=4, soft_min=0.0, soft_max=1.0, update=MxNode.update_prop)


class MxNode_STD_premult(MxNode):
    _file_path = FILE_PATH
    _data_types = {'color4': {'nd_name': 'ND_premult_color4', 'nd': None}}

    bl_label = 'Premult'
    bl_idname = 'usdhydra.MxNode_STD_premult'
    bl_description = ""

    category = 'compositing'

    data_type: EnumProperty(name="Type", description="Input Data Type", items=[('color4', 'Color4', 'Color4')], default='color4', update=MxNode.update_data_type)

    nd_color4_in_in: FloatVectorProperty(name="In", description="", subtype="COLOR", size=4, soft_min=0.0, soft_max=1.0, default=(0.0, 0.0, 0.0, 1.0), update=MxNode.update_prop)
    nd_color4_out_out: FloatVectorProperty(name="Out", description="", subtype="COLOR", size=4, soft_min=0.0, soft_max=1.0, update=MxNode.update_prop)


class MxNode_STD_unpremult(MxNode):
    _file_path = FILE_PATH
    _data_types = {'color4': {'nd_name': 'ND_unpremult_color4', 'nd': None}}

    bl_label = 'Unpremult'
    bl_idname = 'usdhydra.MxNode_STD_unpremult'
    bl_description = ""

    category = 'compositing'

    data_type: EnumProperty(name="Type", description="Input Data Type", items=[('color4', 'Color4', 'Color4')], default='color4', update=MxNode.update_data_type)

    nd_color4_in_in: FloatVectorProperty(name="In", description="", subtype="COLOR", size=4, soft_min=0.0, soft_max=1.0, default=(0.0, 0.0, 0.0, 1.0), update=MxNode.update_prop)
    nd_color4_out_out: FloatVectorProperty(name="Out", description="", subtype="COLOR", size=4, soft_min=0.0, soft_max=1.0, update=MxNode.update_prop)


class MxNode_STD_plus(MxNode):
    _file_path = FILE_PATH
    _data_types = {'float': {'nd_name': 'ND_plus_float', 'nd': None}, 'color3': {'nd_name': 'ND_plus_color3', 'nd': None}, 'color4': {'nd_name': 'ND_plus_color4', 'nd': None}}

    bl_label = 'Plus'
    bl_idname = 'usdhydra.MxNode_STD_plus'
    bl_description = ""

    category = 'compositing'

    data_type: EnumProperty(name="Type", description="Input Data Type", items=[('float', 'Float', 'Float'), ('color3', 'Color3', 'Color3'), ('color4', 'Color4', 'Color4')], default='color3', update=MxNode.update_data_type)

    nd_float_in_fg: FloatProperty(name="Fg", description="", default=0.0, update=MxNode.update_prop)
    nd_float_in_bg: FloatProperty(name="Bg", description="", default=0.0, update=MxNode.update_prop)
    nd_float_in_mix: FloatProperty(name="Mix", description="", default=1.0, update=MxNode.update_prop)
    nd_float_out_out: FloatProperty(name="Out", description="", update=MxNode.update_prop)

    nd_color3_in_fg: FloatVectorProperty(name="Fg", description="", subtype="COLOR", size=3, soft_min=0.0, soft_max=1.0, default=(0.0, 0.0, 0.0), update=MxNode.update_prop)
    nd_color3_in_bg: FloatVectorProperty(name="Bg", description="", subtype="COLOR", size=3, soft_min=0.0, soft_max=1.0, default=(0.0, 0.0, 0.0), update=MxNode.update_prop)
    nd_color3_in_mix: FloatProperty(name="Mix", description="", default=1.0, update=MxNode.update_prop)
    nd_color3_out_out: FloatVectorProperty(name="Out", description="", subtype="COLOR", size=3, soft_min=0.0, soft_max=1.0, update=MxNode.update_prop)

    nd_color4_in_fg: FloatVectorProperty(name="Fg", description="", subtype="COLOR", size=4, soft_min=0.0, soft_max=1.0, default=(0.0, 0.0, 0.0, 0.0), update=MxNode.update_prop)
    nd_color4_in_bg: FloatVectorProperty(name="Bg", description="", subtype="COLOR", size=4, soft_min=0.0, soft_max=1.0, default=(0.0, 0.0, 0.0, 0.0), update=MxNode.update_prop)
    nd_color4_in_mix: FloatProperty(name="Mix", description="", default=1.0, update=MxNode.update_prop)
    nd_color4_out_out: FloatVectorProperty(name="Out", description="", subtype="COLOR", size=4, soft_min=0.0, soft_max=1.0, update=MxNode.update_prop)


class MxNode_STD_minus(MxNode):
    _file_path = FILE_PATH
    _data_types = {'float': {'nd_name': 'ND_minus_float', 'nd': None}, 'color3': {'nd_name': 'ND_minus_color3', 'nd': None}, 'color4': {'nd_name': 'ND_minus_color4', 'nd': None}}

    bl_label = 'Minus'
    bl_idname = 'usdhydra.MxNode_STD_minus'
    bl_description = ""

    category = 'compositing'

    data_type: EnumProperty(name="Type", description="Input Data Type", items=[('float', 'Float', 'Float'), ('color3', 'Color3', 'Color3'), ('color4', 'Color4', 'Color4')], default='color3', update=MxNode.update_data_type)

    nd_float_in_fg: FloatProperty(name="Fg", description="", default=0.0, update=MxNode.update_prop)
    nd_float_in_bg: FloatProperty(name="Bg", description="", default=0.0, update=MxNode.update_prop)
    nd_float_in_mix: FloatProperty(name="Mix", description="", default=1.0, update=MxNode.update_prop)
    nd_float_out_out: FloatProperty(name="Out", description="", update=MxNode.update_prop)

    nd_color3_in_fg: FloatVectorProperty(name="Fg", description="", subtype="COLOR", size=3, soft_min=0.0, soft_max=1.0, default=(0.0, 0.0, 0.0), update=MxNode.update_prop)
    nd_color3_in_bg: FloatVectorProperty(name="Bg", description="", subtype="COLOR", size=3, soft_min=0.0, soft_max=1.0, default=(0.0, 0.0, 0.0), update=MxNode.update_prop)
    nd_color3_in_mix: FloatProperty(name="Mix", description="", default=1.0, update=MxNode.update_prop)
    nd_color3_out_out: FloatVectorProperty(name="Out", description="", subtype="COLOR", size=3, soft_min=0.0, soft_max=1.0, update=MxNode.update_prop)

    nd_color4_in_fg: FloatVectorProperty(name="Fg", description="", subtype="COLOR", size=4, soft_min=0.0, soft_max=1.0, default=(0.0, 0.0, 0.0, 0.0), update=MxNode.update_prop)
    nd_color4_in_bg: FloatVectorProperty(name="Bg", description="", subtype="COLOR", size=4, soft_min=0.0, soft_max=1.0, default=(0.0, 0.0, 0.0, 0.0), update=MxNode.update_prop)
    nd_color4_in_mix: FloatProperty(name="Mix", description="", default=1.0, update=MxNode.update_prop)
    nd_color4_out_out: FloatVectorProperty(name="Out", description="", subtype="COLOR", size=4, soft_min=0.0, soft_max=1.0, update=MxNode.update_prop)


class MxNode_STD_difference(MxNode):
    _file_path = FILE_PATH
    _data_types = {'float': {'nd_name': 'ND_difference_float', 'nd': None}, 'color3': {'nd_name': 'ND_difference_color3', 'nd': None}, 'color4': {'nd_name': 'ND_difference_color4', 'nd': None}}

    bl_label = 'Difference'
    bl_idname = 'usdhydra.MxNode_STD_difference'
    bl_description = ""

    category = 'compositing'

    data_type: EnumProperty(name="Type", description="Input Data Type", items=[('float', 'Float', 'Float'), ('color3', 'Color3', 'Color3'), ('color4', 'Color4', 'Color4')], default='color3', update=MxNode.update_data_type)

    nd_float_in_fg: FloatProperty(name="Fg", description="", default=0.0, update=MxNode.update_prop)
    nd_float_in_bg: FloatProperty(name="Bg", description="", default=0.0, update=MxNode.update_prop)
    nd_float_in_mix: FloatProperty(name="Mix", description="", default=1.0, update=MxNode.update_prop)
    nd_float_out_out: FloatProperty(name="Out", description="", update=MxNode.update_prop)

    nd_color3_in_fg: FloatVectorProperty(name="Fg", description="", subtype="COLOR", size=3, soft_min=0.0, soft_max=1.0, default=(0.0, 0.0, 0.0), update=MxNode.update_prop)
    nd_color3_in_bg: FloatVectorProperty(name="Bg", description="", subtype="COLOR", size=3, soft_min=0.0, soft_max=1.0, default=(0.0, 0.0, 0.0), update=MxNode.update_prop)
    nd_color3_in_mix: FloatProperty(name="Mix", description="", default=1.0, update=MxNode.update_prop)
    nd_color3_out_out: FloatVectorProperty(name="Out", description="", subtype="COLOR", size=3, soft_min=0.0, soft_max=1.0, update=MxNode.update_prop)

    nd_color4_in_fg: FloatVectorProperty(name="Fg", description="", subtype="COLOR", size=4, soft_min=0.0, soft_max=1.0, default=(0.0, 0.0, 0.0, 0.0), update=MxNode.update_prop)
    nd_color4_in_bg: FloatVectorProperty(name="Bg", description="", subtype="COLOR", size=4, soft_min=0.0, soft_max=1.0, default=(0.0, 0.0, 0.0, 0.0), update=MxNode.update_prop)
    nd_color4_in_mix: FloatProperty(name="Mix", description="", default=1.0, update=MxNode.update_prop)
    nd_color4_out_out: FloatVectorProperty(name="Out", description="", subtype="COLOR", size=4, soft_min=0.0, soft_max=1.0, update=MxNode.update_prop)


class MxNode_STD_burn(MxNode):
    _file_path = FILE_PATH
    _data_types = {'float': {'nd_name': 'ND_burn_float', 'nd': None}, 'color3': {'nd_name': 'ND_burn_color3', 'nd': None}, 'color4': {'nd_name': 'ND_burn_color4', 'nd': None}}

    bl_label = 'Burn'
    bl_idname = 'usdhydra.MxNode_STD_burn'
    bl_description = ""

    category = 'compositing'

    data_type: EnumProperty(name="Type", description="Input Data Type", items=[('float', 'Float', 'Float'), ('color3', 'Color3', 'Color3'), ('color4', 'Color4', 'Color4')], default='color3', update=MxNode.update_data_type)

    nd_float_in_fg: FloatProperty(name="Fg", description="", default=0.0, update=MxNode.update_prop)
    nd_float_in_bg: FloatProperty(name="Bg", description="", default=0.0, update=MxNode.update_prop)
    nd_float_in_mix: FloatProperty(name="Mix", description="", default=1.0, update=MxNode.update_prop)
    nd_float_out_out: FloatProperty(name="Out", description="", update=MxNode.update_prop)

    nd_color3_in_fg: FloatVectorProperty(name="Fg", description="", subtype="COLOR", size=3, soft_min=0.0, soft_max=1.0, default=(0.0, 0.0, 0.0), update=MxNode.update_prop)
    nd_color3_in_bg: FloatVectorProperty(name="Bg", description="", subtype="COLOR", size=3, soft_min=0.0, soft_max=1.0, default=(0.0, 0.0, 0.0), update=MxNode.update_prop)
    nd_color3_in_mix: FloatProperty(name="Mix", description="", default=1.0, update=MxNode.update_prop)
    nd_color3_out_out: FloatVectorProperty(name="Out", description="", subtype="COLOR", size=3, soft_min=0.0, soft_max=1.0, update=MxNode.update_prop)

    nd_color4_in_fg: FloatVectorProperty(name="Fg", description="", subtype="COLOR", size=4, soft_min=0.0, soft_max=1.0, default=(0.0, 0.0, 0.0, 0.0), update=MxNode.update_prop)
    nd_color4_in_bg: FloatVectorProperty(name="Bg", description="", subtype="COLOR", size=4, soft_min=0.0, soft_max=1.0, default=(0.0, 0.0, 0.0, 0.0), update=MxNode.update_prop)
    nd_color4_in_mix: FloatProperty(name="Mix", description="", default=1.0, update=MxNode.update_prop)
    nd_color4_out_out: FloatVectorProperty(name="Out", description="", subtype="COLOR", size=4, soft_min=0.0, soft_max=1.0, update=MxNode.update_prop)


class MxNode_STD_dodge(MxNode):
    _file_path = FILE_PATH
    _data_types = {'float': {'nd_name': 'ND_dodge_float', 'nd': None}, 'color3': {'nd_name': 'ND_dodge_color3', 'nd': None}, 'color4': {'nd_name': 'ND_dodge_color4', 'nd': None}}

    bl_label = 'Dodge'
    bl_idname = 'usdhydra.MxNode_STD_dodge'
    bl_description = ""

    category = 'compositing'

    data_type: EnumProperty(name="Type", description="Input Data Type", items=[('float', 'Float', 'Float'), ('color3', 'Color3', 'Color3'), ('color4', 'Color4', 'Color4')], default='color3', update=MxNode.update_data_type)

    nd_float_in_fg: FloatProperty(name="Fg", description="", default=0.0, update=MxNode.update_prop)
    nd_float_in_bg: FloatProperty(name="Bg", description="", default=0.0, update=MxNode.update_prop)
    nd_float_in_mix: FloatProperty(name="Mix", description="", default=1.0, update=MxNode.update_prop)
    nd_float_out_out: FloatProperty(name="Out", description="", update=MxNode.update_prop)

    nd_color3_in_fg: FloatVectorProperty(name="Fg", description="", subtype="COLOR", size=3, soft_min=0.0, soft_max=1.0, default=(0.0, 0.0, 0.0), update=MxNode.update_prop)
    nd_color3_in_bg: FloatVectorProperty(name="Bg", description="", subtype="COLOR", size=3, soft_min=0.0, soft_max=1.0, default=(0.0, 0.0, 0.0), update=MxNode.update_prop)
    nd_color3_in_mix: FloatProperty(name="Mix", description="", default=1.0, update=MxNode.update_prop)
    nd_color3_out_out: FloatVectorProperty(name="Out", description="", subtype="COLOR", size=3, soft_min=0.0, soft_max=1.0, update=MxNode.update_prop)

    nd_color4_in_fg: FloatVectorProperty(name="Fg", description="", subtype="COLOR", size=4, soft_min=0.0, soft_max=1.0, default=(0.0, 0.0, 0.0, 0.0), update=MxNode.update_prop)
    nd_color4_in_bg: FloatVectorProperty(name="Bg", description="", subtype="COLOR", size=4, soft_min=0.0, soft_max=1.0, default=(0.0, 0.0, 0.0, 0.0), update=MxNode.update_prop)
    nd_color4_in_mix: FloatProperty(name="Mix", description="", default=1.0, update=MxNode.update_prop)
    nd_color4_out_out: FloatVectorProperty(name="Out", description="", subtype="COLOR", size=4, soft_min=0.0, soft_max=1.0, update=MxNode.update_prop)


class MxNode_STD_screen(MxNode):
    _file_path = FILE_PATH
    _data_types = {'float': {'nd_name': 'ND_screen_float', 'nd': None}, 'color3': {'nd_name': 'ND_screen_color3', 'nd': None}, 'color4': {'nd_name': 'ND_screen_color4', 'nd': None}}

    bl_label = 'Screen'
    bl_idname = 'usdhydra.MxNode_STD_screen'
    bl_description = ""

    category = 'compositing'

    data_type: EnumProperty(name="Type", description="Input Data Type", items=[('float', 'Float', 'Float'), ('color3', 'Color3', 'Color3'), ('color4', 'Color4', 'Color4')], default='color3', update=MxNode.update_data_type)

    nd_float_in_fg: FloatProperty(name="Fg", description="", default=0.0, update=MxNode.update_prop)
    nd_float_in_bg: FloatProperty(name="Bg", description="", default=0.0, update=MxNode.update_prop)
    nd_float_in_mix: FloatProperty(name="Mix", description="", default=1.0, update=MxNode.update_prop)
    nd_float_out_out: FloatProperty(name="Out", description="", update=MxNode.update_prop)

    nd_color3_in_fg: FloatVectorProperty(name="Fg", description="", subtype="COLOR", size=3, soft_min=0.0, soft_max=1.0, default=(0.0, 0.0, 0.0), update=MxNode.update_prop)
    nd_color3_in_bg: FloatVectorProperty(name="Bg", description="", subtype="COLOR", size=3, soft_min=0.0, soft_max=1.0, default=(0.0, 0.0, 0.0), update=MxNode.update_prop)
    nd_color3_in_mix: FloatProperty(name="Mix", description="", default=1.0, update=MxNode.update_prop)
    nd_color3_out_out: FloatVectorProperty(name="Out", description="", subtype="COLOR", size=3, soft_min=0.0, soft_max=1.0, update=MxNode.update_prop)

    nd_color4_in_fg: FloatVectorProperty(name="Fg", description="", subtype="COLOR", size=4, soft_min=0.0, soft_max=1.0, default=(0.0, 0.0, 0.0, 0.0), update=MxNode.update_prop)
    nd_color4_in_bg: FloatVectorProperty(name="Bg", description="", subtype="COLOR", size=4, soft_min=0.0, soft_max=1.0, default=(0.0, 0.0, 0.0, 0.0), update=MxNode.update_prop)
    nd_color4_in_mix: FloatProperty(name="Mix", description="", default=1.0, update=MxNode.update_prop)
    nd_color4_out_out: FloatVectorProperty(name="Out", description="", subtype="COLOR", size=4, soft_min=0.0, soft_max=1.0, update=MxNode.update_prop)


class MxNode_STD_overlay(MxNode):
    _file_path = FILE_PATH
    _data_types = {'float': {'nd_name': 'ND_overlay_float', 'nd': None}, 'color3': {'nd_name': 'ND_overlay_color3', 'nd': None}, 'color4': {'nd_name': 'ND_overlay_color4', 'nd': None}}

    bl_label = 'Overlay'
    bl_idname = 'usdhydra.MxNode_STD_overlay'
    bl_description = ""

    category = 'compositing'

    data_type: EnumProperty(name="Type", description="Input Data Type", items=[('float', 'Float', 'Float'), ('color3', 'Color3', 'Color3'), ('color4', 'Color4', 'Color4')], default='color3', update=MxNode.update_data_type)

    nd_float_in_fg: FloatProperty(name="Fg", description="", default=0.0, update=MxNode.update_prop)
    nd_float_in_bg: FloatProperty(name="Bg", description="", default=0.0, update=MxNode.update_prop)
    nd_float_in_mix: FloatProperty(name="Mix", description="", default=1.0, update=MxNode.update_prop)
    nd_float_out_out: FloatProperty(name="Out", description="", update=MxNode.update_prop)

    nd_color3_in_fg: FloatVectorProperty(name="Fg", description="", subtype="COLOR", size=3, soft_min=0.0, soft_max=1.0, default=(0.0, 0.0, 0.0), update=MxNode.update_prop)
    nd_color3_in_bg: FloatVectorProperty(name="Bg", description="", subtype="COLOR", size=3, soft_min=0.0, soft_max=1.0, default=(0.0, 0.0, 0.0), update=MxNode.update_prop)
    nd_color3_in_mix: FloatProperty(name="Mix", description="", default=1.0, update=MxNode.update_prop)
    nd_color3_out_out: FloatVectorProperty(name="Out", description="", subtype="COLOR", size=3, soft_min=0.0, soft_max=1.0, update=MxNode.update_prop)

    nd_color4_in_fg: FloatVectorProperty(name="Fg", description="", subtype="COLOR", size=4, soft_min=0.0, soft_max=1.0, default=(0.0, 0.0, 0.0, 0.0), update=MxNode.update_prop)
    nd_color4_in_bg: FloatVectorProperty(name="Bg", description="", subtype="COLOR", size=4, soft_min=0.0, soft_max=1.0, default=(0.0, 0.0, 0.0, 0.0), update=MxNode.update_prop)
    nd_color4_in_mix: FloatProperty(name="Mix", description="", default=1.0, update=MxNode.update_prop)
    nd_color4_out_out: FloatVectorProperty(name="Out", description="", subtype="COLOR", size=4, soft_min=0.0, soft_max=1.0, update=MxNode.update_prop)


class MxNode_STD_disjointover(MxNode):
    _file_path = FILE_PATH
    _data_types = {'color4': {'nd_name': 'ND_disjointover_color4', 'nd': None}}

    bl_label = 'Disjointover'
    bl_idname = 'usdhydra.MxNode_STD_disjointover'
    bl_description = ""

    category = 'compositing'

    data_type: EnumProperty(name="Type", description="Input Data Type", items=[('color4', 'Color4', 'Color4')], default='color4', update=MxNode.update_data_type)

    nd_color4_in_fg: FloatVectorProperty(name="Fg", description="", subtype="COLOR", size=4, soft_min=0.0, soft_max=1.0, default=(0.0, 0.0, 0.0, 0.0), update=MxNode.update_prop)
    nd_color4_in_bg: FloatVectorProperty(name="Bg", description="", subtype="COLOR", size=4, soft_min=0.0, soft_max=1.0, default=(0.0, 0.0, 0.0, 0.0), update=MxNode.update_prop)
    nd_color4_in_mix: FloatProperty(name="Mix", description="", default=1.0, update=MxNode.update_prop)
    nd_color4_out_out: FloatVectorProperty(name="Out", description="", subtype="COLOR", size=4, soft_min=0.0, soft_max=1.0, update=MxNode.update_prop)


class MxNode_STD_in(MxNode):
    _file_path = FILE_PATH
    _data_types = {'color4': {'nd_name': 'ND_in_color4', 'nd': None}}

    bl_label = 'In'
    bl_idname = 'usdhydra.MxNode_STD_in'
    bl_description = ""

    category = 'compositing'

    data_type: EnumProperty(name="Type", description="Input Data Type", items=[('color4', 'Color4', 'Color4')], default='color4', update=MxNode.update_data_type)

    nd_color4_in_fg: FloatVectorProperty(name="Fg", description="", subtype="COLOR", size=4, soft_min=0.0, soft_max=1.0, default=(0.0, 0.0, 0.0, 0.0), update=MxNode.update_prop)
    nd_color4_in_bg: FloatVectorProperty(name="Bg", description="", subtype="COLOR", size=4, soft_min=0.0, soft_max=1.0, default=(0.0, 0.0, 0.0, 0.0), update=MxNode.update_prop)
    nd_color4_in_mix: FloatProperty(name="Mix", description="", default=1.0, update=MxNode.update_prop)
    nd_color4_out_out: FloatVectorProperty(name="Out", description="", subtype="COLOR", size=4, soft_min=0.0, soft_max=1.0, update=MxNode.update_prop)


class MxNode_STD_mask(MxNode):
    _file_path = FILE_PATH
    _data_types = {'color4': {'nd_name': 'ND_mask_color4', 'nd': None}}

    bl_label = 'Mask'
    bl_idname = 'usdhydra.MxNode_STD_mask'
    bl_description = ""

    category = 'compositing'

    data_type: EnumProperty(name="Type", description="Input Data Type", items=[('color4', 'Color4', 'Color4')], default='color4', update=MxNode.update_data_type)

    nd_color4_in_fg: FloatVectorProperty(name="Fg", description="", subtype="COLOR", size=4, soft_min=0.0, soft_max=1.0, default=(0.0, 0.0, 0.0, 0.0), update=MxNode.update_prop)
    nd_color4_in_bg: FloatVectorProperty(name="Bg", description="", subtype="COLOR", size=4, soft_min=0.0, soft_max=1.0, default=(0.0, 0.0, 0.0, 0.0), update=MxNode.update_prop)
    nd_color4_in_mix: FloatProperty(name="Mix", description="", default=1.0, update=MxNode.update_prop)
    nd_color4_out_out: FloatVectorProperty(name="Out", description="", subtype="COLOR", size=4, soft_min=0.0, soft_max=1.0, update=MxNode.update_prop)


class MxNode_STD_matte(MxNode):
    _file_path = FILE_PATH
    _data_types = {'color4': {'nd_name': 'ND_matte_color4', 'nd': None}}

    bl_label = 'Matte'
    bl_idname = 'usdhydra.MxNode_STD_matte'
    bl_description = ""

    category = 'compositing'

    data_type: EnumProperty(name="Type", description="Input Data Type", items=[('color4', 'Color4', 'Color4')], default='color4', update=MxNode.update_data_type)

    nd_color4_in_fg: FloatVectorProperty(name="Fg", description="", subtype="COLOR", size=4, soft_min=0.0, soft_max=1.0, default=(0.0, 0.0, 0.0, 0.0), update=MxNode.update_prop)
    nd_color4_in_bg: FloatVectorProperty(name="Bg", description="", subtype="COLOR", size=4, soft_min=0.0, soft_max=1.0, default=(0.0, 0.0, 0.0, 0.0), update=MxNode.update_prop)
    nd_color4_in_mix: FloatProperty(name="Mix", description="", default=1.0, update=MxNode.update_prop)
    nd_color4_out_out: FloatVectorProperty(name="Out", description="", subtype="COLOR", size=4, soft_min=0.0, soft_max=1.0, update=MxNode.update_prop)


class MxNode_STD_out(MxNode):
    _file_path = FILE_PATH
    _data_types = {'color4': {'nd_name': 'ND_out_color4', 'nd': None}}

    bl_label = 'Out'
    bl_idname = 'usdhydra.MxNode_STD_out'
    bl_description = ""

    category = 'compositing'

    data_type: EnumProperty(name="Type", description="Input Data Type", items=[('color4', 'Color4', 'Color4')], default='color4', update=MxNode.update_data_type)

    nd_color4_in_fg: FloatVectorProperty(name="Fg", description="", subtype="COLOR", size=4, soft_min=0.0, soft_max=1.0, default=(0.0, 0.0, 0.0, 0.0), update=MxNode.update_prop)
    nd_color4_in_bg: FloatVectorProperty(name="Bg", description="", subtype="COLOR", size=4, soft_min=0.0, soft_max=1.0, default=(0.0, 0.0, 0.0, 0.0), update=MxNode.update_prop)
    nd_color4_in_mix: FloatProperty(name="Mix", description="", default=1.0, update=MxNode.update_prop)
    nd_color4_out_out: FloatVectorProperty(name="Out", description="", subtype="COLOR", size=4, soft_min=0.0, soft_max=1.0, update=MxNode.update_prop)


class MxNode_STD_over(MxNode):
    _file_path = FILE_PATH
    _data_types = {'color4': {'nd_name': 'ND_over_color4', 'nd': None}}

    bl_label = 'Over'
    bl_idname = 'usdhydra.MxNode_STD_over'
    bl_description = ""

    category = 'compositing'

    data_type: EnumProperty(name="Type", description="Input Data Type", items=[('color4', 'Color4', 'Color4')], default='color4', update=MxNode.update_data_type)

    nd_color4_in_fg: FloatVectorProperty(name="Fg", description="", subtype="COLOR", size=4, soft_min=0.0, soft_max=1.0, default=(0.0, 0.0, 0.0, 0.0), update=MxNode.update_prop)
    nd_color4_in_bg: FloatVectorProperty(name="Bg", description="", subtype="COLOR", size=4, soft_min=0.0, soft_max=1.0, default=(0.0, 0.0, 0.0, 0.0), update=MxNode.update_prop)
    nd_color4_in_mix: FloatProperty(name="Mix", description="", default=1.0, update=MxNode.update_prop)
    nd_color4_out_out: FloatVectorProperty(name="Out", description="", subtype="COLOR", size=4, soft_min=0.0, soft_max=1.0, update=MxNode.update_prop)


class MxNode_STD_inside(MxNode):
    _file_path = FILE_PATH
    _data_types = {'float': {'nd_name': 'ND_inside_float', 'nd': None}, 'color3': {'nd_name': 'ND_inside_color3', 'nd': None}, 'color4': {'nd_name': 'ND_inside_color4', 'nd': None}}

    bl_label = 'Inside'
    bl_idname = 'usdhydra.MxNode_STD_inside'
    bl_description = ""

    category = 'compositing'

    data_type: EnumProperty(name="Type", description="Input Data Type", items=[('float', 'Float', 'Float'), ('color3', 'Color3', 'Color3'), ('color4', 'Color4', 'Color4')], default='color3', update=MxNode.update_data_type)

    nd_float_in_in: FloatProperty(name="In", description="", default=0.0, update=MxNode.update_prop)
    nd_float_in_mask: FloatProperty(name="Mask", description="", default=1.0, update=MxNode.update_prop)
    nd_float_out_out: FloatProperty(name="Out", description="", update=MxNode.update_prop)

    nd_color3_in_in: FloatVectorProperty(name="In", description="", subtype="COLOR", size=3, soft_min=0.0, soft_max=1.0, default=(0.0, 0.0, 0.0), update=MxNode.update_prop)
    nd_color3_in_mask: FloatProperty(name="Mask", description="", default=1.0, update=MxNode.update_prop)
    nd_color3_out_out: FloatVectorProperty(name="Out", description="", subtype="COLOR", size=3, soft_min=0.0, soft_max=1.0, update=MxNode.update_prop)

    nd_color4_in_in: FloatVectorProperty(name="In", description="", subtype="COLOR", size=4, soft_min=0.0, soft_max=1.0, default=(0.0, 0.0, 0.0, 0.0), update=MxNode.update_prop)
    nd_color4_in_mask: FloatProperty(name="Mask", description="", default=1.0, update=MxNode.update_prop)
    nd_color4_out_out: FloatVectorProperty(name="Out", description="", subtype="COLOR", size=4, soft_min=0.0, soft_max=1.0, update=MxNode.update_prop)


class MxNode_STD_outside(MxNode):
    _file_path = FILE_PATH
    _data_types = {'float': {'nd_name': 'ND_outside_float', 'nd': None}, 'color3': {'nd_name': 'ND_outside_color3', 'nd': None}, 'color4': {'nd_name': 'ND_outside_color4', 'nd': None}}

    bl_label = 'Outside'
    bl_idname = 'usdhydra.MxNode_STD_outside'
    bl_description = ""

    category = 'compositing'

    data_type: EnumProperty(name="Type", description="Input Data Type", items=[('float', 'Float', 'Float'), ('color3', 'Color3', 'Color3'), ('color4', 'Color4', 'Color4')], default='color3', update=MxNode.update_data_type)

    nd_float_in_in: FloatProperty(name="In", description="", default=0.0, update=MxNode.update_prop)
    nd_float_in_mask: FloatProperty(name="Mask", description="", default=0.0, update=MxNode.update_prop)
    nd_float_out_out: FloatProperty(name="Out", description="", update=MxNode.update_prop)

    nd_color3_in_in: FloatVectorProperty(name="In", description="", subtype="COLOR", size=3, soft_min=0.0, soft_max=1.0, default=(0.0, 0.0, 0.0), update=MxNode.update_prop)
    nd_color3_in_mask: FloatProperty(name="Mask", description="", default=0.0, update=MxNode.update_prop)
    nd_color3_out_out: FloatVectorProperty(name="Out", description="", subtype="COLOR", size=3, soft_min=0.0, soft_max=1.0, update=MxNode.update_prop)

    nd_color4_in_in: FloatVectorProperty(name="In", description="", subtype="COLOR", size=4, soft_min=0.0, soft_max=1.0, default=(0.0, 0.0, 0.0, 0.0), update=MxNode.update_prop)
    nd_color4_in_mask: FloatProperty(name="Mask", description="", default=0.0, update=MxNode.update_prop)
    nd_color4_out_out: FloatVectorProperty(name="Out", description="", subtype="COLOR", size=4, soft_min=0.0, soft_max=1.0, update=MxNode.update_prop)


class MxNode_STD_mix(MxNode):
    _file_path = FILE_PATH
    _data_types = {'float': {'nd_name': 'ND_mix_float', 'nd': None}, 'color3': {'nd_name': 'ND_mix_color3', 'nd': None}, 'color4': {'nd_name': 'ND_mix_color4', 'nd': None}, 'vector2': {'nd_name': 'ND_mix_vector2', 'nd': None}, 'vector3': {'nd_name': 'ND_mix_vector3', 'nd': None}, 'vector4': {'nd_name': 'ND_mix_vector4', 'nd': None}, 'surfaceshader': {'nd_name': 'ND_mix_surfaceshader', 'nd': None}, 'displacementshader': {'nd_name': 'ND_mix_displacementshader', 'nd': None}, 'volumeshader': {'nd_name': 'ND_mix_volumeshader', 'nd': None}}

    bl_label = 'Mix'
    bl_idname = 'usdhydra.MxNode_STD_mix'
    bl_description = ""

    category = 'compositing'

    data_type: EnumProperty(name="Type", description="Input Data Type", items=[('float', 'Float', 'Float'), ('color3', 'Color3', 'Color3'), ('color4', 'Color4', 'Color4'), ('vector2', 'Vector2', 'Vector2'), ('vector3', 'Vector3', 'Vector3'), ('vector4', 'Vector4', 'Vector4'), ('surfaceshader', 'Surfaceshader', 'Surfaceshader'), ('displacementshader', 'Displacementshader', 'Displacementshader'), ('volumeshader', 'Volumeshader', 'Volumeshader')], default='color3', update=MxNode.update_data_type)

    nd_float_in_fg: FloatProperty(name="Fg", description="", default=0.0, update=MxNode.update_prop)
    nd_float_in_bg: FloatProperty(name="Bg", description="", default=0.0, update=MxNode.update_prop)
    nd_float_in_mix: FloatProperty(name="Mix", description="", default=0.0, update=MxNode.update_prop)
    nd_float_out_out: FloatProperty(name="Out", description="", update=MxNode.update_prop)

    nd_color3_in_fg: FloatVectorProperty(name="Fg", description="", subtype="COLOR", size=3, soft_min=0.0, soft_max=1.0, default=(0.0, 0.0, 0.0), update=MxNode.update_prop)
    nd_color3_in_bg: FloatVectorProperty(name="Bg", description="", subtype="COLOR", size=3, soft_min=0.0, soft_max=1.0, default=(0.0, 0.0, 0.0), update=MxNode.update_prop)
    nd_color3_in_mix: FloatProperty(name="Mix", description="", default=0.0, update=MxNode.update_prop)
    nd_color3_out_out: FloatVectorProperty(name="Out", description="", subtype="COLOR", size=3, soft_min=0.0, soft_max=1.0, update=MxNode.update_prop)

    nd_color4_in_fg: FloatVectorProperty(name="Fg", description="", subtype="COLOR", size=4, soft_min=0.0, soft_max=1.0, default=(0.0, 0.0, 0.0, 0.0), update=MxNode.update_prop)
    nd_color4_in_bg: FloatVectorProperty(name="Bg", description="", subtype="COLOR", size=4, soft_min=0.0, soft_max=1.0, default=(0.0, 0.0, 0.0, 0.0), update=MxNode.update_prop)
    nd_color4_in_mix: FloatProperty(name="Mix", description="", default=0.0, update=MxNode.update_prop)
    nd_color4_out_out: FloatVectorProperty(name="Out", description="", subtype="COLOR", size=4, soft_min=0.0, soft_max=1.0, update=MxNode.update_prop)

    nd_vector2_in_fg: FloatVectorProperty(name="Fg", description="", subtype="NONE", size=2, default=(0.0, 0.0), update=MxNode.update_prop)
    nd_vector2_in_bg: FloatVectorProperty(name="Bg", description="", subtype="NONE", size=2, default=(0.0, 0.0), update=MxNode.update_prop)
    nd_vector2_in_mix: FloatProperty(name="Mix", description="", default=0.0, update=MxNode.update_prop)
    nd_vector2_out_out: FloatVectorProperty(name="Out", description="", subtype="NONE", size=2, update=MxNode.update_prop)

    nd_vector3_in_fg: FloatVectorProperty(name="Fg", description="", subtype="XYZ", size=3, default=(0.0, 0.0, 0.0), update=MxNode.update_prop)
    nd_vector3_in_bg: FloatVectorProperty(name="Bg", description="", subtype="XYZ", size=3, default=(0.0, 0.0, 0.0), update=MxNode.update_prop)
    nd_vector3_in_mix: FloatProperty(name="Mix", description="", default=0.0, update=MxNode.update_prop)
    nd_vector3_out_out: FloatVectorProperty(name="Out", description="", subtype="XYZ", size=3, update=MxNode.update_prop)

    nd_vector4_in_fg: FloatVectorProperty(name="Fg", description="", subtype="NONE", size=4, default=(0.0, 0.0, 0.0, 0.0), update=MxNode.update_prop)
    nd_vector4_in_bg: FloatVectorProperty(name="Bg", description="", subtype="NONE", size=4, default=(0.0, 0.0, 0.0, 0.0), update=MxNode.update_prop)
    nd_vector4_in_mix: FloatProperty(name="Mix", description="", default=0.0, update=MxNode.update_prop)
    nd_vector4_out_out: FloatVectorProperty(name="Out", description="", subtype="NONE", size=4, update=MxNode.update_prop)

    nd_surfaceshader_in_fg: StringProperty(name="Fg", description="", default="", update=MxNode.update_prop)
    nd_surfaceshader_in_bg: StringProperty(name="Bg", description="", default="", update=MxNode.update_prop)
    nd_surfaceshader_in_mix: FloatProperty(name="Mix", description="", default=0.0, update=MxNode.update_prop)
    nd_surfaceshader_out_out: StringProperty(name="Out", description="", update=MxNode.update_prop)

    nd_displacementshader_in_fg: StringProperty(name="Fg", description="", default="", update=MxNode.update_prop)
    nd_displacementshader_in_bg: StringProperty(name="Bg", description="", default="", update=MxNode.update_prop)
    nd_displacementshader_in_mix: FloatProperty(name="Mix", description="", default=0.0, update=MxNode.update_prop)
    nd_displacementshader_out_out: StringProperty(name="Out", description="", update=MxNode.update_prop)

    nd_volumeshader_in_fg: StringProperty(name="Fg", description="", default="", update=MxNode.update_prop)
    nd_volumeshader_in_bg: StringProperty(name="Bg", description="", default="", update=MxNode.update_prop)
    nd_volumeshader_in_mix: FloatProperty(name="Mix", description="", default=0.0, update=MxNode.update_prop)
    nd_volumeshader_out_out: StringProperty(name="Out", description="", update=MxNode.update_prop)


class MxNode_STD_ifgreater(MxNode):
    _file_path = FILE_PATH
    _data_types = {'float': {'nd_name': 'ND_ifgreater_float', 'nd': None}, 'color3': {'nd_name': 'ND_ifgreater_color3', 'nd': None}, 'color4': {'nd_name': 'ND_ifgreater_color4', 'nd': None}, 'vector2': {'nd_name': 'ND_ifgreater_vector2', 'nd': None}, 'vector3': {'nd_name': 'ND_ifgreater_vector3', 'nd': None}, 'vector4': {'nd_name': 'ND_ifgreater_vector4', 'nd': None}, 'floatI': {'nd_name': 'ND_ifgreater_floatI', 'nd': None}, 'color3I': {'nd_name': 'ND_ifgreater_color3I', 'nd': None}, 'color4I': {'nd_name': 'ND_ifgreater_color4I', 'nd': None}, 'vector2I': {'nd_name': 'ND_ifgreater_vector2I', 'nd': None}, 'vector3I': {'nd_name': 'ND_ifgreater_vector3I', 'nd': None}, 'vector4I': {'nd_name': 'ND_ifgreater_vector4I', 'nd': None}}

    bl_label = 'Ifgreater'
    bl_idname = 'usdhydra.MxNode_STD_ifgreater'
    bl_description = ""

    category = 'conditional'

    data_type: EnumProperty(name="Type", description="Input Data Type", items=[('float', 'Float', 'Float'), ('color3', 'Color3', 'Color3'), ('color4', 'Color4', 'Color4'), ('vector2', 'Vector2', 'Vector2'), ('vector3', 'Vector3', 'Vector3'), ('vector4', 'Vector4', 'Vector4'), ('floatI', 'FloatI', 'FloatI'), ('color3I', 'Color3I', 'Color3I'), ('color4I', 'Color4I', 'Color4I'), ('vector2I', 'Vector2I', 'Vector2I'), ('vector3I', 'Vector3I', 'Vector3I'), ('vector4I', 'Vector4I', 'Vector4I')], default='color3', update=MxNode.update_data_type)

    nd_float_in_value1: FloatProperty(name="Value1", description="", default=1.0, update=MxNode.update_prop)
    nd_float_in_value2: FloatProperty(name="Value2", description="", default=0.0, update=MxNode.update_prop)
    nd_float_in_in1: FloatProperty(name="In1", description="", default=0.0, update=MxNode.update_prop)
    nd_float_in_in2: FloatProperty(name="In2", description="", default=0.0, update=MxNode.update_prop)
    nd_float_out_out: FloatProperty(name="Out", description="", update=MxNode.update_prop)

    nd_color3_in_value1: FloatProperty(name="Value1", description="", default=1.0, update=MxNode.update_prop)
    nd_color3_in_value2: FloatProperty(name="Value2", description="", default=0.0, update=MxNode.update_prop)
    nd_color3_in_in1: FloatVectorProperty(name="In1", description="", subtype="COLOR", size=3, soft_min=0.0, soft_max=1.0, default=(0.0, 0.0, 0.0), update=MxNode.update_prop)
    nd_color3_in_in2: FloatVectorProperty(name="In2", description="", subtype="COLOR", size=3, soft_min=0.0, soft_max=1.0, default=(0.0, 0.0, 0.0), update=MxNode.update_prop)
    nd_color3_out_out: FloatVectorProperty(name="Out", description="", subtype="COLOR", size=3, soft_min=0.0, soft_max=1.0, update=MxNode.update_prop)

    nd_color4_in_value1: FloatProperty(name="Value1", description="", default=1.0, update=MxNode.update_prop)
    nd_color4_in_value2: FloatProperty(name="Value2", description="", default=0.0, update=MxNode.update_prop)
    nd_color4_in_in1: FloatVectorProperty(name="In1", description="", subtype="COLOR", size=4, soft_min=0.0, soft_max=1.0, default=(0.0, 0.0, 0.0, 0.0), update=MxNode.update_prop)
    nd_color4_in_in2: FloatVectorProperty(name="In2", description="", subtype="COLOR", size=4, soft_min=0.0, soft_max=1.0, default=(0.0, 0.0, 0.0, 0.0), update=MxNode.update_prop)
    nd_color4_out_out: FloatVectorProperty(name="Out", description="", subtype="COLOR", size=4, soft_min=0.0, soft_max=1.0, update=MxNode.update_prop)

    nd_vector2_in_value1: FloatProperty(name="Value1", description="", default=1.0, update=MxNode.update_prop)
    nd_vector2_in_value2: FloatProperty(name="Value2", description="", default=0.0, update=MxNode.update_prop)
    nd_vector2_in_in1: FloatVectorProperty(name="In1", description="", subtype="NONE", size=2, default=(0.0, 0.0), update=MxNode.update_prop)
    nd_vector2_in_in2: FloatVectorProperty(name="In2", description="", subtype="NONE", size=2, default=(0.0, 0.0), update=MxNode.update_prop)
    nd_vector2_out_out: FloatVectorProperty(name="Out", description="", subtype="NONE", size=2, update=MxNode.update_prop)

    nd_vector3_in_value1: FloatProperty(name="Value1", description="", default=1.0, update=MxNode.update_prop)
    nd_vector3_in_value2: FloatProperty(name="Value2", description="", default=0.0, update=MxNode.update_prop)
    nd_vector3_in_in1: FloatVectorProperty(name="In1", description="", subtype="XYZ", size=3, default=(0.0, 0.0, 0.0), update=MxNode.update_prop)
    nd_vector3_in_in2: FloatVectorProperty(name="In2", description="", subtype="XYZ", size=3, default=(0.0, 0.0, 0.0), update=MxNode.update_prop)
    nd_vector3_out_out: FloatVectorProperty(name="Out", description="", subtype="XYZ", size=3, update=MxNode.update_prop)

    nd_vector4_in_value1: FloatProperty(name="Value1", description="", default=1.0, update=MxNode.update_prop)
    nd_vector4_in_value2: FloatProperty(name="Value2", description="", default=0.0, update=MxNode.update_prop)
    nd_vector4_in_in1: FloatVectorProperty(name="In1", description="", subtype="NONE", size=4, default=(0.0, 0.0, 0.0, 0.0), update=MxNode.update_prop)
    nd_vector4_in_in2: FloatVectorProperty(name="In2", description="", subtype="NONE", size=4, default=(0.0, 0.0, 0.0, 0.0), update=MxNode.update_prop)
    nd_vector4_out_out: FloatVectorProperty(name="Out", description="", subtype="NONE", size=4, update=MxNode.update_prop)

    nd_floatI_in_value1: IntProperty(name="Value1", description="", default=1, update=MxNode.update_prop)
    nd_floatI_in_value2: IntProperty(name="Value2", description="", default=0, update=MxNode.update_prop)
    nd_floatI_in_in1: FloatProperty(name="In1", description="", default=0.0, update=MxNode.update_prop)
    nd_floatI_in_in2: FloatProperty(name="In2", description="", default=0.0, update=MxNode.update_prop)
    nd_floatI_out_out: FloatProperty(name="Out", description="", update=MxNode.update_prop)

    nd_color3I_in_value1: IntProperty(name="Value1", description="", default=1, update=MxNode.update_prop)
    nd_color3I_in_value2: IntProperty(name="Value2", description="", default=0, update=MxNode.update_prop)
    nd_color3I_in_in1: FloatVectorProperty(name="In1", description="", subtype="COLOR", size=3, soft_min=0.0, soft_max=1.0, default=(0.0, 0.0, 0.0), update=MxNode.update_prop)
    nd_color3I_in_in2: FloatVectorProperty(name="In2", description="", subtype="COLOR", size=3, soft_min=0.0, soft_max=1.0, default=(0.0, 0.0, 0.0), update=MxNode.update_prop)
    nd_color3I_out_out: FloatVectorProperty(name="Out", description="", subtype="COLOR", size=3, soft_min=0.0, soft_max=1.0, update=MxNode.update_prop)

    nd_color4I_in_value1: IntProperty(name="Value1", description="", default=1, update=MxNode.update_prop)
    nd_color4I_in_value2: IntProperty(name="Value2", description="", default=0, update=MxNode.update_prop)
    nd_color4I_in_in1: FloatVectorProperty(name="In1", description="", subtype="COLOR", size=4, soft_min=0.0, soft_max=1.0, default=(0.0, 0.0, 0.0, 0.0), update=MxNode.update_prop)
    nd_color4I_in_in2: FloatVectorProperty(name="In2", description="", subtype="COLOR", size=4, soft_min=0.0, soft_max=1.0, default=(0.0, 0.0, 0.0, 0.0), update=MxNode.update_prop)
    nd_color4I_out_out: FloatVectorProperty(name="Out", description="", subtype="COLOR", size=4, soft_min=0.0, soft_max=1.0, update=MxNode.update_prop)

    nd_vector2I_in_value1: IntProperty(name="Value1", description="", default=1, update=MxNode.update_prop)
    nd_vector2I_in_value2: IntProperty(name="Value2", description="", default=0, update=MxNode.update_prop)
    nd_vector2I_in_in1: FloatVectorProperty(name="In1", description="", subtype="NONE", size=2, default=(0.0, 0.0), update=MxNode.update_prop)
    nd_vector2I_in_in2: FloatVectorProperty(name="In2", description="", subtype="NONE", size=2, default=(0.0, 0.0), update=MxNode.update_prop)
    nd_vector2I_out_out: FloatVectorProperty(name="Out", description="", subtype="NONE", size=2, update=MxNode.update_prop)

    nd_vector3I_in_value1: IntProperty(name="Value1", description="", default=1, update=MxNode.update_prop)
    nd_vector3I_in_value2: IntProperty(name="Value2", description="", default=0, update=MxNode.update_prop)
    nd_vector3I_in_in1: FloatVectorProperty(name="In1", description="", subtype="XYZ", size=3, default=(0.0, 0.0, 0.0), update=MxNode.update_prop)
    nd_vector3I_in_in2: FloatVectorProperty(name="In2", description="", subtype="XYZ", size=3, default=(0.0, 0.0, 0.0), update=MxNode.update_prop)
    nd_vector3I_out_out: FloatVectorProperty(name="Out", description="", subtype="XYZ", size=3, update=MxNode.update_prop)

    nd_vector4I_in_value1: IntProperty(name="Value1", description="", default=1, update=MxNode.update_prop)
    nd_vector4I_in_value2: IntProperty(name="Value2", description="", default=0, update=MxNode.update_prop)
    nd_vector4I_in_in1: FloatVectorProperty(name="In1", description="", subtype="NONE", size=4, default=(0.0, 0.0, 0.0, 0.0), update=MxNode.update_prop)
    nd_vector4I_in_in2: FloatVectorProperty(name="In2", description="", subtype="NONE", size=4, default=(0.0, 0.0, 0.0, 0.0), update=MxNode.update_prop)
    nd_vector4I_out_out: FloatVectorProperty(name="Out", description="", subtype="NONE", size=4, update=MxNode.update_prop)


class MxNode_STD_ifgreatereq(MxNode):
    _file_path = FILE_PATH
    _data_types = {'float': {'nd_name': 'ND_ifgreatereq_float', 'nd': None}, 'color3': {'nd_name': 'ND_ifgreatereq_color3', 'nd': None}, 'color4': {'nd_name': 'ND_ifgreatereq_color4', 'nd': None}, 'vector2': {'nd_name': 'ND_ifgreatereq_vector2', 'nd': None}, 'vector3': {'nd_name': 'ND_ifgreatereq_vector3', 'nd': None}, 'vector4': {'nd_name': 'ND_ifgreatereq_vector4', 'nd': None}, 'floatI': {'nd_name': 'ND_ifgreatereq_floatI', 'nd': None}, 'color3I': {'nd_name': 'ND_ifgreatereq_color3I', 'nd': None}, 'color4I': {'nd_name': 'ND_ifgreatereq_color4I', 'nd': None}, 'vector2I': {'nd_name': 'ND_ifgreatereq_vector2I', 'nd': None}, 'vector3I': {'nd_name': 'ND_ifgreatereq_vector3I', 'nd': None}, 'vector4I': {'nd_name': 'ND_ifgreatereq_vector4I', 'nd': None}}

    bl_label = 'Ifgreatereq'
    bl_idname = 'usdhydra.MxNode_STD_ifgreatereq'
    bl_description = ""

    category = 'conditional'

    data_type: EnumProperty(name="Type", description="Input Data Type", items=[('float', 'Float', 'Float'), ('color3', 'Color3', 'Color3'), ('color4', 'Color4', 'Color4'), ('vector2', 'Vector2', 'Vector2'), ('vector3', 'Vector3', 'Vector3'), ('vector4', 'Vector4', 'Vector4'), ('floatI', 'FloatI', 'FloatI'), ('color3I', 'Color3I', 'Color3I'), ('color4I', 'Color4I', 'Color4I'), ('vector2I', 'Vector2I', 'Vector2I'), ('vector3I', 'Vector3I', 'Vector3I'), ('vector4I', 'Vector4I', 'Vector4I')], default='color3', update=MxNode.update_data_type)

    nd_float_in_value1: FloatProperty(name="Value1", description="", default=1.0, update=MxNode.update_prop)
    nd_float_in_value2: FloatProperty(name="Value2", description="", default=0.0, update=MxNode.update_prop)
    nd_float_in_in1: FloatProperty(name="In1", description="", default=0.0, update=MxNode.update_prop)
    nd_float_in_in2: FloatProperty(name="In2", description="", default=0.0, update=MxNode.update_prop)
    nd_float_out_out: FloatProperty(name="Out", description="", update=MxNode.update_prop)

    nd_color3_in_value1: FloatProperty(name="Value1", description="", default=1.0, update=MxNode.update_prop)
    nd_color3_in_value2: FloatProperty(name="Value2", description="", default=0.0, update=MxNode.update_prop)
    nd_color3_in_in1: FloatVectorProperty(name="In1", description="", subtype="COLOR", size=3, soft_min=0.0, soft_max=1.0, default=(0.0, 0.0, 0.0), update=MxNode.update_prop)
    nd_color3_in_in2: FloatVectorProperty(name="In2", description="", subtype="COLOR", size=3, soft_min=0.0, soft_max=1.0, default=(0.0, 0.0, 0.0), update=MxNode.update_prop)
    nd_color3_out_out: FloatVectorProperty(name="Out", description="", subtype="COLOR", size=3, soft_min=0.0, soft_max=1.0, update=MxNode.update_prop)

    nd_color4_in_value1: FloatProperty(name="Value1", description="", default=1.0, update=MxNode.update_prop)
    nd_color4_in_value2: FloatProperty(name="Value2", description="", default=0.0, update=MxNode.update_prop)
    nd_color4_in_in1: FloatVectorProperty(name="In1", description="", subtype="COLOR", size=4, soft_min=0.0, soft_max=1.0, default=(0.0, 0.0, 0.0, 0.0), update=MxNode.update_prop)
    nd_color4_in_in2: FloatVectorProperty(name="In2", description="", subtype="COLOR", size=4, soft_min=0.0, soft_max=1.0, default=(0.0, 0.0, 0.0, 0.0), update=MxNode.update_prop)
    nd_color4_out_out: FloatVectorProperty(name="Out", description="", subtype="COLOR", size=4, soft_min=0.0, soft_max=1.0, update=MxNode.update_prop)

    nd_vector2_in_value1: FloatProperty(name="Value1", description="", default=1.0, update=MxNode.update_prop)
    nd_vector2_in_value2: FloatProperty(name="Value2", description="", default=0.0, update=MxNode.update_prop)
    nd_vector2_in_in1: FloatVectorProperty(name="In1", description="", subtype="NONE", size=2, default=(0.0, 0.0), update=MxNode.update_prop)
    nd_vector2_in_in2: FloatVectorProperty(name="In2", description="", subtype="NONE", size=2, default=(0.0, 0.0), update=MxNode.update_prop)
    nd_vector2_out_out: FloatVectorProperty(name="Out", description="", subtype="NONE", size=2, update=MxNode.update_prop)

    nd_vector3_in_value1: FloatProperty(name="Value1", description="", default=1.0, update=MxNode.update_prop)
    nd_vector3_in_value2: FloatProperty(name="Value2", description="", default=0.0, update=MxNode.update_prop)
    nd_vector3_in_in1: FloatVectorProperty(name="In1", description="", subtype="XYZ", size=3, default=(0.0, 0.0, 0.0), update=MxNode.update_prop)
    nd_vector3_in_in2: FloatVectorProperty(name="In2", description="", subtype="XYZ", size=3, default=(0.0, 0.0, 0.0), update=MxNode.update_prop)
    nd_vector3_out_out: FloatVectorProperty(name="Out", description="", subtype="XYZ", size=3, update=MxNode.update_prop)

    nd_vector4_in_value1: FloatProperty(name="Value1", description="", default=1.0, update=MxNode.update_prop)
    nd_vector4_in_value2: FloatProperty(name="Value2", description="", default=0.0, update=MxNode.update_prop)
    nd_vector4_in_in1: FloatVectorProperty(name="In1", description="", subtype="NONE", size=4, default=(0.0, 0.0, 0.0, 0.0), update=MxNode.update_prop)
    nd_vector4_in_in2: FloatVectorProperty(name="In2", description="", subtype="NONE", size=4, default=(0.0, 0.0, 0.0, 0.0), update=MxNode.update_prop)
    nd_vector4_out_out: FloatVectorProperty(name="Out", description="", subtype="NONE", size=4, update=MxNode.update_prop)

    nd_floatI_in_value1: IntProperty(name="Value1", description="", default=1, update=MxNode.update_prop)
    nd_floatI_in_value2: IntProperty(name="Value2", description="", default=0, update=MxNode.update_prop)
    nd_floatI_in_in1: FloatProperty(name="In1", description="", default=0.0, update=MxNode.update_prop)
    nd_floatI_in_in2: FloatProperty(name="In2", description="", default=0.0, update=MxNode.update_prop)
    nd_floatI_out_out: FloatProperty(name="Out", description="", update=MxNode.update_prop)

    nd_color3I_in_value1: IntProperty(name="Value1", description="", default=1, update=MxNode.update_prop)
    nd_color3I_in_value2: IntProperty(name="Value2", description="", default=0, update=MxNode.update_prop)
    nd_color3I_in_in1: FloatVectorProperty(name="In1", description="", subtype="COLOR", size=3, soft_min=0.0, soft_max=1.0, default=(0.0, 0.0, 0.0), update=MxNode.update_prop)
    nd_color3I_in_in2: FloatVectorProperty(name="In2", description="", subtype="COLOR", size=3, soft_min=0.0, soft_max=1.0, default=(0.0, 0.0, 0.0), update=MxNode.update_prop)
    nd_color3I_out_out: FloatVectorProperty(name="Out", description="", subtype="COLOR", size=3, soft_min=0.0, soft_max=1.0, update=MxNode.update_prop)

    nd_color4I_in_value1: IntProperty(name="Value1", description="", default=1, update=MxNode.update_prop)
    nd_color4I_in_value2: IntProperty(name="Value2", description="", default=0, update=MxNode.update_prop)
    nd_color4I_in_in1: FloatVectorProperty(name="In1", description="", subtype="COLOR", size=4, soft_min=0.0, soft_max=1.0, default=(0.0, 0.0, 0.0, 0.0), update=MxNode.update_prop)
    nd_color4I_in_in2: FloatVectorProperty(name="In2", description="", subtype="COLOR", size=4, soft_min=0.0, soft_max=1.0, default=(0.0, 0.0, 0.0, 0.0), update=MxNode.update_prop)
    nd_color4I_out_out: FloatVectorProperty(name="Out", description="", subtype="COLOR", size=4, soft_min=0.0, soft_max=1.0, update=MxNode.update_prop)

    nd_vector2I_in_value1: IntProperty(name="Value1", description="", default=1, update=MxNode.update_prop)
    nd_vector2I_in_value2: IntProperty(name="Value2", description="", default=0, update=MxNode.update_prop)
    nd_vector2I_in_in1: FloatVectorProperty(name="In1", description="", subtype="NONE", size=2, default=(0.0, 0.0), update=MxNode.update_prop)
    nd_vector2I_in_in2: FloatVectorProperty(name="In2", description="", subtype="NONE", size=2, default=(0.0, 0.0), update=MxNode.update_prop)
    nd_vector2I_out_out: FloatVectorProperty(name="Out", description="", subtype="NONE", size=2, update=MxNode.update_prop)

    nd_vector3I_in_value1: IntProperty(name="Value1", description="", default=1, update=MxNode.update_prop)
    nd_vector3I_in_value2: IntProperty(name="Value2", description="", default=0, update=MxNode.update_prop)
    nd_vector3I_in_in1: FloatVectorProperty(name="In1", description="", subtype="XYZ", size=3, default=(0.0, 0.0, 0.0), update=MxNode.update_prop)
    nd_vector3I_in_in2: FloatVectorProperty(name="In2", description="", subtype="XYZ", size=3, default=(0.0, 0.0, 0.0), update=MxNode.update_prop)
    nd_vector3I_out_out: FloatVectorProperty(name="Out", description="", subtype="XYZ", size=3, update=MxNode.update_prop)

    nd_vector4I_in_value1: IntProperty(name="Value1", description="", default=1, update=MxNode.update_prop)
    nd_vector4I_in_value2: IntProperty(name="Value2", description="", default=0, update=MxNode.update_prop)
    nd_vector4I_in_in1: FloatVectorProperty(name="In1", description="", subtype="NONE", size=4, default=(0.0, 0.0, 0.0, 0.0), update=MxNode.update_prop)
    nd_vector4I_in_in2: FloatVectorProperty(name="In2", description="", subtype="NONE", size=4, default=(0.0, 0.0, 0.0, 0.0), update=MxNode.update_prop)
    nd_vector4I_out_out: FloatVectorProperty(name="Out", description="", subtype="NONE", size=4, update=MxNode.update_prop)


class MxNode_STD_ifequal(MxNode):
    _file_path = FILE_PATH
    _data_types = {'float': {'nd_name': 'ND_ifequal_float', 'nd': None}, 'color3': {'nd_name': 'ND_ifequal_color3', 'nd': None}, 'color4': {'nd_name': 'ND_ifequal_color4', 'nd': None}, 'vector2': {'nd_name': 'ND_ifequal_vector2', 'nd': None}, 'vector3': {'nd_name': 'ND_ifequal_vector3', 'nd': None}, 'vector4': {'nd_name': 'ND_ifequal_vector4', 'nd': None}, 'floatI': {'nd_name': 'ND_ifequal_floatI', 'nd': None}, 'color3I': {'nd_name': 'ND_ifequal_color3I', 'nd': None}, 'color4I': {'nd_name': 'ND_ifequal_color4I', 'nd': None}, 'vector2I': {'nd_name': 'ND_ifequal_vector2I', 'nd': None}, 'vector3I': {'nd_name': 'ND_ifequal_vector3I', 'nd': None}, 'vector4I': {'nd_name': 'ND_ifequal_vector4I', 'nd': None}, 'floatB': {'nd_name': 'ND_ifequal_floatB', 'nd': None}, 'color3B': {'nd_name': 'ND_ifequal_color3B', 'nd': None}, 'color4B': {'nd_name': 'ND_ifequal_color4B', 'nd': None}, 'vector2B': {'nd_name': 'ND_ifequal_vector2B', 'nd': None}, 'vector3B': {'nd_name': 'ND_ifequal_vector3B', 'nd': None}, 'vector4B': {'nd_name': 'ND_ifequal_vector4B', 'nd': None}}

    bl_label = 'Ifequal'
    bl_idname = 'usdhydra.MxNode_STD_ifequal'
    bl_description = ""

    category = 'conditional'

    data_type: EnumProperty(name="Type", description="Input Data Type", items=[('float', 'Float', 'Float'), ('color3', 'Color3', 'Color3'), ('color4', 'Color4', 'Color4'), ('vector2', 'Vector2', 'Vector2'), ('vector3', 'Vector3', 'Vector3'), ('vector4', 'Vector4', 'Vector4'), ('floatI', 'FloatI', 'FloatI'), ('color3I', 'Color3I', 'Color3I'), ('color4I', 'Color4I', 'Color4I'), ('vector2I', 'Vector2I', 'Vector2I'), ('vector3I', 'Vector3I', 'Vector3I'), ('vector4I', 'Vector4I', 'Vector4I'), ('floatB', 'FloatB', 'FloatB'), ('color3B', 'Color3B', 'Color3B'), ('color4B', 'Color4B', 'Color4B'), ('vector2B', 'Vector2B', 'Vector2B'), ('vector3B', 'Vector3B', 'Vector3B'), ('vector4B', 'Vector4B', 'Vector4B')], default='color3', update=MxNode.update_data_type)

    nd_float_in_value1: FloatProperty(name="Value1", description="", default=0.0, update=MxNode.update_prop)
    nd_float_in_value2: FloatProperty(name="Value2", description="", default=0.0, update=MxNode.update_prop)
    nd_float_in_in1: FloatProperty(name="In1", description="", default=0.0, update=MxNode.update_prop)
    nd_float_in_in2: FloatProperty(name="In2", description="", default=0.0, update=MxNode.update_prop)
    nd_float_out_out: FloatProperty(name="Out", description="", update=MxNode.update_prop)

    nd_color3_in_value1: FloatProperty(name="Value1", description="", default=0.0, update=MxNode.update_prop)
    nd_color3_in_value2: FloatProperty(name="Value2", description="", default=0.0, update=MxNode.update_prop)
    nd_color3_in_in1: FloatVectorProperty(name="In1", description="", subtype="COLOR", size=3, soft_min=0.0, soft_max=1.0, default=(0.0, 0.0, 0.0), update=MxNode.update_prop)
    nd_color3_in_in2: FloatVectorProperty(name="In2", description="", subtype="COLOR", size=3, soft_min=0.0, soft_max=1.0, default=(0.0, 0.0, 0.0), update=MxNode.update_prop)
    nd_color3_out_out: FloatVectorProperty(name="Out", description="", subtype="COLOR", size=3, soft_min=0.0, soft_max=1.0, update=MxNode.update_prop)

    nd_color4_in_value1: FloatProperty(name="Value1", description="", default=0.0, update=MxNode.update_prop)
    nd_color4_in_value2: FloatProperty(name="Value2", description="", default=0.0, update=MxNode.update_prop)
    nd_color4_in_in1: FloatVectorProperty(name="In1", description="", subtype="COLOR", size=4, soft_min=0.0, soft_max=1.0, default=(0.0, 0.0, 0.0, 0.0), update=MxNode.update_prop)
    nd_color4_in_in2: FloatVectorProperty(name="In2", description="", subtype="COLOR", size=4, soft_min=0.0, soft_max=1.0, default=(0.0, 0.0, 0.0, 0.0), update=MxNode.update_prop)
    nd_color4_out_out: FloatVectorProperty(name="Out", description="", subtype="COLOR", size=4, soft_min=0.0, soft_max=1.0, update=MxNode.update_prop)

    nd_vector2_in_value1: FloatProperty(name="Value1", description="", default=0.0, update=MxNode.update_prop)
    nd_vector2_in_value2: FloatProperty(name="Value2", description="", default=0.0, update=MxNode.update_prop)
    nd_vector2_in_in1: FloatVectorProperty(name="In1", description="", subtype="NONE", size=2, default=(0.0, 0.0), update=MxNode.update_prop)
    nd_vector2_in_in2: FloatVectorProperty(name="In2", description="", subtype="NONE", size=2, default=(0.0, 0.0), update=MxNode.update_prop)
    nd_vector2_out_out: FloatVectorProperty(name="Out", description="", subtype="NONE", size=2, update=MxNode.update_prop)

    nd_vector3_in_value1: FloatProperty(name="Value1", description="", default=0.0, update=MxNode.update_prop)
    nd_vector3_in_value2: FloatProperty(name="Value2", description="", default=0.0, update=MxNode.update_prop)
    nd_vector3_in_in1: FloatVectorProperty(name="In1", description="", subtype="XYZ", size=3, default=(0.0, 0.0, 0.0), update=MxNode.update_prop)
    nd_vector3_in_in2: FloatVectorProperty(name="In2", description="", subtype="XYZ", size=3, default=(0.0, 0.0, 0.0), update=MxNode.update_prop)
    nd_vector3_out_out: FloatVectorProperty(name="Out", description="", subtype="XYZ", size=3, update=MxNode.update_prop)

    nd_vector4_in_value1: FloatProperty(name="Value1", description="", default=0.0, update=MxNode.update_prop)
    nd_vector4_in_value2: FloatProperty(name="Value2", description="", default=0.0, update=MxNode.update_prop)
    nd_vector4_in_in1: FloatVectorProperty(name="In1", description="", subtype="NONE", size=4, default=(0.0, 0.0, 0.0, 0.0), update=MxNode.update_prop)
    nd_vector4_in_in2: FloatVectorProperty(name="In2", description="", subtype="NONE", size=4, default=(0.0, 0.0, 0.0, 0.0), update=MxNode.update_prop)
    nd_vector4_out_out: FloatVectorProperty(name="Out", description="", subtype="NONE", size=4, update=MxNode.update_prop)

    nd_floatI_in_value1: IntProperty(name="Value1", description="", default=0, update=MxNode.update_prop)
    nd_floatI_in_value2: IntProperty(name="Value2", description="", default=0, update=MxNode.update_prop)
    nd_floatI_in_in1: FloatProperty(name="In1", description="", default=0.0, update=MxNode.update_prop)
    nd_floatI_in_in2: FloatProperty(name="In2", description="", default=0.0, update=MxNode.update_prop)
    nd_floatI_out_out: FloatProperty(name="Out", description="", update=MxNode.update_prop)

    nd_color3I_in_value1: IntProperty(name="Value1", description="", default=0, update=MxNode.update_prop)
    nd_color3I_in_value2: IntProperty(name="Value2", description="", default=0, update=MxNode.update_prop)
    nd_color3I_in_in1: FloatVectorProperty(name="In1", description="", subtype="COLOR", size=3, soft_min=0.0, soft_max=1.0, default=(0.0, 0.0, 0.0), update=MxNode.update_prop)
    nd_color3I_in_in2: FloatVectorProperty(name="In2", description="", subtype="COLOR", size=3, soft_min=0.0, soft_max=1.0, default=(0.0, 0.0, 0.0), update=MxNode.update_prop)
    nd_color3I_out_out: FloatVectorProperty(name="Out", description="", subtype="COLOR", size=3, soft_min=0.0, soft_max=1.0, update=MxNode.update_prop)

    nd_color4I_in_value1: IntProperty(name="Value1", description="", default=0, update=MxNode.update_prop)
    nd_color4I_in_value2: IntProperty(name="Value2", description="", default=0, update=MxNode.update_prop)
    nd_color4I_in_in1: FloatVectorProperty(name="In1", description="", subtype="COLOR", size=4, soft_min=0.0, soft_max=1.0, default=(0.0, 0.0, 0.0, 0.0), update=MxNode.update_prop)
    nd_color4I_in_in2: FloatVectorProperty(name="In2", description="", subtype="COLOR", size=4, soft_min=0.0, soft_max=1.0, default=(0.0, 0.0, 0.0, 0.0), update=MxNode.update_prop)
    nd_color4I_out_out: FloatVectorProperty(name="Out", description="", subtype="COLOR", size=4, soft_min=0.0, soft_max=1.0, update=MxNode.update_prop)

    nd_vector2I_in_value1: IntProperty(name="Value1", description="", default=0, update=MxNode.update_prop)
    nd_vector2I_in_value2: IntProperty(name="Value2", description="", default=0, update=MxNode.update_prop)
    nd_vector2I_in_in1: FloatVectorProperty(name="In1", description="", subtype="NONE", size=2, default=(0.0, 0.0), update=MxNode.update_prop)
    nd_vector2I_in_in2: FloatVectorProperty(name="In2", description="", subtype="NONE", size=2, default=(0.0, 0.0), update=MxNode.update_prop)
    nd_vector2I_out_out: FloatVectorProperty(name="Out", description="", subtype="NONE", size=2, update=MxNode.update_prop)

    nd_vector3I_in_value1: IntProperty(name="Value1", description="", default=0, update=MxNode.update_prop)
    nd_vector3I_in_value2: IntProperty(name="Value2", description="", default=0, update=MxNode.update_prop)
    nd_vector3I_in_in1: FloatVectorProperty(name="In1", description="", subtype="XYZ", size=3, default=(0.0, 0.0, 0.0), update=MxNode.update_prop)
    nd_vector3I_in_in2: FloatVectorProperty(name="In2", description="", subtype="XYZ", size=3, default=(0.0, 0.0, 0.0), update=MxNode.update_prop)
    nd_vector3I_out_out: FloatVectorProperty(name="Out", description="", subtype="XYZ", size=3, update=MxNode.update_prop)

    nd_vector4I_in_value1: IntProperty(name="Value1", description="", default=0, update=MxNode.update_prop)
    nd_vector4I_in_value2: IntProperty(name="Value2", description="", default=0, update=MxNode.update_prop)
    nd_vector4I_in_in1: FloatVectorProperty(name="In1", description="", subtype="NONE", size=4, default=(0.0, 0.0, 0.0, 0.0), update=MxNode.update_prop)
    nd_vector4I_in_in2: FloatVectorProperty(name="In2", description="", subtype="NONE", size=4, default=(0.0, 0.0, 0.0, 0.0), update=MxNode.update_prop)
    nd_vector4I_out_out: FloatVectorProperty(name="Out", description="", subtype="NONE", size=4, update=MxNode.update_prop)

    nd_floatB_in_value1: BoolProperty(name="Value1", description="", default=False, update=MxNode.update_prop)
    nd_floatB_in_value2: BoolProperty(name="Value2", description="", default=False, update=MxNode.update_prop)
    nd_floatB_in_in1: FloatProperty(name="In1", description="", default=0.0, update=MxNode.update_prop)
    nd_floatB_in_in2: FloatProperty(name="In2", description="", default=0.0, update=MxNode.update_prop)
    nd_floatB_out_out: FloatProperty(name="Out", description="", update=MxNode.update_prop)

    nd_color3B_in_value1: BoolProperty(name="Value1", description="", default=False, update=MxNode.update_prop)
    nd_color3B_in_value2: BoolProperty(name="Value2", description="", default=False, update=MxNode.update_prop)
    nd_color3B_in_in1: FloatVectorProperty(name="In1", description="", subtype="COLOR", size=3, soft_min=0.0, soft_max=1.0, default=(0.0, 0.0, 0.0), update=MxNode.update_prop)
    nd_color3B_in_in2: FloatVectorProperty(name="In2", description="", subtype="COLOR", size=3, soft_min=0.0, soft_max=1.0, default=(0.0, 0.0, 0.0), update=MxNode.update_prop)
    nd_color3B_out_out: FloatVectorProperty(name="Out", description="", subtype="COLOR", size=3, soft_min=0.0, soft_max=1.0, update=MxNode.update_prop)

    nd_color4B_in_value1: BoolProperty(name="Value1", description="", default=False, update=MxNode.update_prop)
    nd_color4B_in_value2: BoolProperty(name="Value2", description="", default=False, update=MxNode.update_prop)
    nd_color4B_in_in1: FloatVectorProperty(name="In1", description="", subtype="COLOR", size=4, soft_min=0.0, soft_max=1.0, default=(0.0, 0.0, 0.0, 0.0), update=MxNode.update_prop)
    nd_color4B_in_in2: FloatVectorProperty(name="In2", description="", subtype="COLOR", size=4, soft_min=0.0, soft_max=1.0, default=(0.0, 0.0, 0.0, 0.0), update=MxNode.update_prop)
    nd_color4B_out_out: FloatVectorProperty(name="Out", description="", subtype="COLOR", size=4, soft_min=0.0, soft_max=1.0, update=MxNode.update_prop)

    nd_vector2B_in_value1: BoolProperty(name="Value1", description="", default=False, update=MxNode.update_prop)
    nd_vector2B_in_value2: BoolProperty(name="Value2", description="", default=False, update=MxNode.update_prop)
    nd_vector2B_in_in1: FloatVectorProperty(name="In1", description="", subtype="NONE", size=2, default=(0.0, 0.0), update=MxNode.update_prop)
    nd_vector2B_in_in2: FloatVectorProperty(name="In2", description="", subtype="NONE", size=2, default=(0.0, 0.0), update=MxNode.update_prop)
    nd_vector2B_out_out: FloatVectorProperty(name="Out", description="", subtype="NONE", size=2, update=MxNode.update_prop)

    nd_vector3B_in_value1: BoolProperty(name="Value1", description="", default=False, update=MxNode.update_prop)
    nd_vector3B_in_value2: BoolProperty(name="Value2", description="", default=False, update=MxNode.update_prop)
    nd_vector3B_in_in1: FloatVectorProperty(name="In1", description="", subtype="XYZ", size=3, default=(0.0, 0.0, 0.0), update=MxNode.update_prop)
    nd_vector3B_in_in2: FloatVectorProperty(name="In2", description="", subtype="XYZ", size=3, default=(0.0, 0.0, 0.0), update=MxNode.update_prop)
    nd_vector3B_out_out: FloatVectorProperty(name="Out", description="", subtype="XYZ", size=3, update=MxNode.update_prop)

    nd_vector4B_in_value1: BoolProperty(name="Value1", description="", default=False, update=MxNode.update_prop)
    nd_vector4B_in_value2: BoolProperty(name="Value2", description="", default=False, update=MxNode.update_prop)
    nd_vector4B_in_in1: FloatVectorProperty(name="In1", description="", subtype="NONE", size=4, default=(0.0, 0.0, 0.0, 0.0), update=MxNode.update_prop)
    nd_vector4B_in_in2: FloatVectorProperty(name="In2", description="", subtype="NONE", size=4, default=(0.0, 0.0, 0.0, 0.0), update=MxNode.update_prop)
    nd_vector4B_out_out: FloatVectorProperty(name="Out", description="", subtype="NONE", size=4, update=MxNode.update_prop)


class MxNode_STD_switch(MxNode):
    _file_path = FILE_PATH
    _data_types = {'float': {'nd_name': 'ND_switch_float', 'nd': None}, 'color3': {'nd_name': 'ND_switch_color3', 'nd': None}, 'color4': {'nd_name': 'ND_switch_color4', 'nd': None}, 'vector2': {'nd_name': 'ND_switch_vector2', 'nd': None}, 'vector3': {'nd_name': 'ND_switch_vector3', 'nd': None}, 'vector4': {'nd_name': 'ND_switch_vector4', 'nd': None}, 'floatI': {'nd_name': 'ND_switch_floatI', 'nd': None}, 'color3I': {'nd_name': 'ND_switch_color3I', 'nd': None}, 'color4I': {'nd_name': 'ND_switch_color4I', 'nd': None}, 'vector2I': {'nd_name': 'ND_switch_vector2I', 'nd': None}, 'vector3I': {'nd_name': 'ND_switch_vector3I', 'nd': None}, 'vector4I': {'nd_name': 'ND_switch_vector4I', 'nd': None}}

    bl_label = 'Switch'
    bl_idname = 'usdhydra.MxNode_STD_switch'
    bl_description = ""

    category = 'conditional'

    data_type: EnumProperty(name="Type", description="Input Data Type", items=[('float', 'Float', 'Float'), ('color3', 'Color3', 'Color3'), ('color4', 'Color4', 'Color4'), ('vector2', 'Vector2', 'Vector2'), ('vector3', 'Vector3', 'Vector3'), ('vector4', 'Vector4', 'Vector4'), ('floatI', 'FloatI', 'FloatI'), ('color3I', 'Color3I', 'Color3I'), ('color4I', 'Color4I', 'Color4I'), ('vector2I', 'Vector2I', 'Vector2I'), ('vector3I', 'Vector3I', 'Vector3I'), ('vector4I', 'Vector4I', 'Vector4I')], default='color3', update=MxNode.update_data_type)

    nd_float_in_in1: FloatProperty(name="In1", description="", default=0.0, update=MxNode.update_prop)
    nd_float_in_in2: FloatProperty(name="In2", description="", default=0.0, update=MxNode.update_prop)
    nd_float_in_in3: FloatProperty(name="In3", description="", default=0.0, update=MxNode.update_prop)
    nd_float_in_in4: FloatProperty(name="In4", description="", default=0.0, update=MxNode.update_prop)
    nd_float_in_in5: FloatProperty(name="In5", description="", default=0.0, update=MxNode.update_prop)
    nd_float_in_which: FloatProperty(name="Which", description="", default=0.0, update=MxNode.update_prop)
    nd_float_out_out: FloatProperty(name="Out", description="", update=MxNode.update_prop)

    nd_color3_in_in1: FloatVectorProperty(name="In1", description="", subtype="COLOR", size=3, soft_min=0.0, soft_max=1.0, default=(0.0, 0.0, 0.0), update=MxNode.update_prop)
    nd_color3_in_in2: FloatVectorProperty(name="In2", description="", subtype="COLOR", size=3, soft_min=0.0, soft_max=1.0, default=(0.0, 0.0, 0.0), update=MxNode.update_prop)
    nd_color3_in_in3: FloatVectorProperty(name="In3", description="", subtype="COLOR", size=3, soft_min=0.0, soft_max=1.0, default=(0.0, 0.0, 0.0), update=MxNode.update_prop)
    nd_color3_in_in4: FloatVectorProperty(name="In4", description="", subtype="COLOR", size=3, soft_min=0.0, soft_max=1.0, default=(0.0, 0.0, 0.0), update=MxNode.update_prop)
    nd_color3_in_in5: FloatVectorProperty(name="In5", description="", subtype="COLOR", size=3, soft_min=0.0, soft_max=1.0, default=(0.0, 0.0, 0.0), update=MxNode.update_prop)
    nd_color3_in_which: FloatProperty(name="Which", description="", default=0.0, update=MxNode.update_prop)
    nd_color3_out_out: FloatVectorProperty(name="Out", description="", subtype="COLOR", size=3, soft_min=0.0, soft_max=1.0, update=MxNode.update_prop)

    nd_color4_in_in1: FloatVectorProperty(name="In1", description="", subtype="COLOR", size=4, soft_min=0.0, soft_max=1.0, default=(0.0, 0.0, 0.0, 0.0), update=MxNode.update_prop)
    nd_color4_in_in2: FloatVectorProperty(name="In2", description="", subtype="COLOR", size=4, soft_min=0.0, soft_max=1.0, default=(0.0, 0.0, 0.0, 0.0), update=MxNode.update_prop)
    nd_color4_in_in3: FloatVectorProperty(name="In3", description="", subtype="COLOR", size=4, soft_min=0.0, soft_max=1.0, default=(0.0, 0.0, 0.0, 0.0), update=MxNode.update_prop)
    nd_color4_in_in4: FloatVectorProperty(name="In4", description="", subtype="COLOR", size=4, soft_min=0.0, soft_max=1.0, default=(0.0, 0.0, 0.0, 0.0), update=MxNode.update_prop)
    nd_color4_in_in5: FloatVectorProperty(name="In5", description="", subtype="COLOR", size=4, soft_min=0.0, soft_max=1.0, default=(0.0, 0.0, 0.0, 0.0), update=MxNode.update_prop)
    nd_color4_in_which: FloatProperty(name="Which", description="", default=0.0, update=MxNode.update_prop)
    nd_color4_out_out: FloatVectorProperty(name="Out", description="", subtype="COLOR", size=4, soft_min=0.0, soft_max=1.0, update=MxNode.update_prop)

    nd_vector2_in_in1: FloatVectorProperty(name="In1", description="", subtype="NONE", size=2, default=(0.0, 0.0), update=MxNode.update_prop)
    nd_vector2_in_in2: FloatVectorProperty(name="In2", description="", subtype="NONE", size=2, default=(0.0, 0.0), update=MxNode.update_prop)
    nd_vector2_in_in3: FloatVectorProperty(name="In3", description="", subtype="NONE", size=2, default=(0.0, 0.0), update=MxNode.update_prop)
    nd_vector2_in_in4: FloatVectorProperty(name="In4", description="", subtype="NONE", size=2, default=(0.0, 0.0), update=MxNode.update_prop)
    nd_vector2_in_in5: FloatVectorProperty(name="In5", description="", subtype="NONE", size=2, default=(0.0, 0.0), update=MxNode.update_prop)
    nd_vector2_in_which: FloatProperty(name="Which", description="", default=0.0, update=MxNode.update_prop)
    nd_vector2_out_out: FloatVectorProperty(name="Out", description="", subtype="NONE", size=2, update=MxNode.update_prop)

    nd_vector3_in_in1: FloatVectorProperty(name="In1", description="", subtype="XYZ", size=3, default=(0.0, 0.0, 0.0), update=MxNode.update_prop)
    nd_vector3_in_in2: FloatVectorProperty(name="In2", description="", subtype="XYZ", size=3, default=(0.0, 0.0, 0.0), update=MxNode.update_prop)
    nd_vector3_in_in3: FloatVectorProperty(name="In3", description="", subtype="XYZ", size=3, default=(0.0, 0.0, 0.0), update=MxNode.update_prop)
    nd_vector3_in_in4: FloatVectorProperty(name="In4", description="", subtype="XYZ", size=3, default=(0.0, 0.0, 0.0), update=MxNode.update_prop)
    nd_vector3_in_in5: FloatVectorProperty(name="In5", description="", subtype="XYZ", size=3, default=(0.0, 0.0, 0.0), update=MxNode.update_prop)
    nd_vector3_in_which: FloatProperty(name="Which", description="", default=0.0, update=MxNode.update_prop)
    nd_vector3_out_out: FloatVectorProperty(name="Out", description="", subtype="XYZ", size=3, update=MxNode.update_prop)

    nd_vector4_in_in1: FloatVectorProperty(name="In1", description="", subtype="NONE", size=4, default=(0.0, 0.0, 0.0, 0.0), update=MxNode.update_prop)
    nd_vector4_in_in2: FloatVectorProperty(name="In2", description="", subtype="NONE", size=4, default=(0.0, 0.0, 0.0, 0.0), update=MxNode.update_prop)
    nd_vector4_in_in3: FloatVectorProperty(name="In3", description="", subtype="NONE", size=4, default=(0.0, 0.0, 0.0, 0.0), update=MxNode.update_prop)
    nd_vector4_in_in4: FloatVectorProperty(name="In4", description="", subtype="NONE", size=4, default=(0.0, 0.0, 0.0, 0.0), update=MxNode.update_prop)
    nd_vector4_in_in5: FloatVectorProperty(name="In5", description="", subtype="NONE", size=4, default=(0.0, 0.0, 0.0, 0.0), update=MxNode.update_prop)
    nd_vector4_in_which: FloatProperty(name="Which", description="", default=0.0, update=MxNode.update_prop)
    nd_vector4_out_out: FloatVectorProperty(name="Out", description="", subtype="NONE", size=4, update=MxNode.update_prop)

    nd_floatI_in_in1: FloatProperty(name="In1", description="", default=0.0, update=MxNode.update_prop)
    nd_floatI_in_in2: FloatProperty(name="In2", description="", default=0.0, update=MxNode.update_prop)
    nd_floatI_in_in3: FloatProperty(name="In3", description="", default=0.0, update=MxNode.update_prop)
    nd_floatI_in_in4: FloatProperty(name="In4", description="", default=0.0, update=MxNode.update_prop)
    nd_floatI_in_in5: FloatProperty(name="In5", description="", default=0.0, update=MxNode.update_prop)
    nd_floatI_in_which: IntProperty(name="Which", description="", default=0, update=MxNode.update_prop)
    nd_floatI_out_out: FloatProperty(name="Out", description="", update=MxNode.update_prop)

    nd_color3I_in_in1: FloatVectorProperty(name="In1", description="", subtype="COLOR", size=3, soft_min=0.0, soft_max=1.0, default=(0.0, 0.0, 0.0), update=MxNode.update_prop)
    nd_color3I_in_in2: FloatVectorProperty(name="In2", description="", subtype="COLOR", size=3, soft_min=0.0, soft_max=1.0, default=(0.0, 0.0, 0.0), update=MxNode.update_prop)
    nd_color3I_in_in3: FloatVectorProperty(name="In3", description="", subtype="COLOR", size=3, soft_min=0.0, soft_max=1.0, default=(0.0, 0.0, 0.0), update=MxNode.update_prop)
    nd_color3I_in_in4: FloatVectorProperty(name="In4", description="", subtype="COLOR", size=3, soft_min=0.0, soft_max=1.0, default=(0.0, 0.0, 0.0), update=MxNode.update_prop)
    nd_color3I_in_in5: FloatVectorProperty(name="In5", description="", subtype="COLOR", size=3, soft_min=0.0, soft_max=1.0, default=(0.0, 0.0, 0.0), update=MxNode.update_prop)
    nd_color3I_in_which: IntProperty(name="Which", description="", default=0, update=MxNode.update_prop)
    nd_color3I_out_out: FloatVectorProperty(name="Out", description="", subtype="COLOR", size=3, soft_min=0.0, soft_max=1.0, update=MxNode.update_prop)

    nd_color4I_in_in1: FloatVectorProperty(name="In1", description="", subtype="COLOR", size=4, soft_min=0.0, soft_max=1.0, default=(0.0, 0.0, 0.0, 0.0), update=MxNode.update_prop)
    nd_color4I_in_in2: FloatVectorProperty(name="In2", description="", subtype="COLOR", size=4, soft_min=0.0, soft_max=1.0, default=(0.0, 0.0, 0.0, 0.0), update=MxNode.update_prop)
    nd_color4I_in_in3: FloatVectorProperty(name="In3", description="", subtype="COLOR", size=4, soft_min=0.0, soft_max=1.0, default=(0.0, 0.0, 0.0, 0.0), update=MxNode.update_prop)
    nd_color4I_in_in4: FloatVectorProperty(name="In4", description="", subtype="COLOR", size=4, soft_min=0.0, soft_max=1.0, default=(0.0, 0.0, 0.0, 0.0), update=MxNode.update_prop)
    nd_color4I_in_in5: FloatVectorProperty(name="In5", description="", subtype="COLOR", size=4, soft_min=0.0, soft_max=1.0, default=(0.0, 0.0, 0.0, 0.0), update=MxNode.update_prop)
    nd_color4I_in_which: IntProperty(name="Which", description="", default=0, update=MxNode.update_prop)
    nd_color4I_out_out: FloatVectorProperty(name="Out", description="", subtype="COLOR", size=4, soft_min=0.0, soft_max=1.0, update=MxNode.update_prop)

    nd_vector2I_in_in1: FloatVectorProperty(name="In1", description="", subtype="NONE", size=2, default=(0.0, 0.0), update=MxNode.update_prop)
    nd_vector2I_in_in2: FloatVectorProperty(name="In2", description="", subtype="NONE", size=2, default=(0.0, 0.0), update=MxNode.update_prop)
    nd_vector2I_in_in3: FloatVectorProperty(name="In3", description="", subtype="NONE", size=2, default=(0.0, 0.0), update=MxNode.update_prop)
    nd_vector2I_in_in4: FloatVectorProperty(name="In4", description="", subtype="NONE", size=2, default=(0.0, 0.0), update=MxNode.update_prop)
    nd_vector2I_in_in5: FloatVectorProperty(name="In5", description="", subtype="NONE", size=2, default=(0.0, 0.0), update=MxNode.update_prop)
    nd_vector2I_in_which: IntProperty(name="Which", description="", default=0, update=MxNode.update_prop)
    nd_vector2I_out_out: FloatVectorProperty(name="Out", description="", subtype="NONE", size=2, update=MxNode.update_prop)

    nd_vector3I_in_in1: FloatVectorProperty(name="In1", description="", subtype="XYZ", size=3, default=(0.0, 0.0, 0.0), update=MxNode.update_prop)
    nd_vector3I_in_in2: FloatVectorProperty(name="In2", description="", subtype="XYZ", size=3, default=(0.0, 0.0, 0.0), update=MxNode.update_prop)
    nd_vector3I_in_in3: FloatVectorProperty(name="In3", description="", subtype="XYZ", size=3, default=(0.0, 0.0, 0.0), update=MxNode.update_prop)
    nd_vector3I_in_in4: FloatVectorProperty(name="In4", description="", subtype="XYZ", size=3, default=(0.0, 0.0, 0.0), update=MxNode.update_prop)
    nd_vector3I_in_in5: FloatVectorProperty(name="In5", description="", subtype="XYZ", size=3, default=(0.0, 0.0, 0.0), update=MxNode.update_prop)
    nd_vector3I_in_which: IntProperty(name="Which", description="", default=0, update=MxNode.update_prop)
    nd_vector3I_out_out: FloatVectorProperty(name="Out", description="", subtype="XYZ", size=3, update=MxNode.update_prop)

    nd_vector4I_in_in1: FloatVectorProperty(name="In1", description="", subtype="NONE", size=4, default=(0.0, 0.0, 0.0, 0.0), update=MxNode.update_prop)
    nd_vector4I_in_in2: FloatVectorProperty(name="In2", description="", subtype="NONE", size=4, default=(0.0, 0.0, 0.0, 0.0), update=MxNode.update_prop)
    nd_vector4I_in_in3: FloatVectorProperty(name="In3", description="", subtype="NONE", size=4, default=(0.0, 0.0, 0.0, 0.0), update=MxNode.update_prop)
    nd_vector4I_in_in4: FloatVectorProperty(name="In4", description="", subtype="NONE", size=4, default=(0.0, 0.0, 0.0, 0.0), update=MxNode.update_prop)
    nd_vector4I_in_in5: FloatVectorProperty(name="In5", description="", subtype="NONE", size=4, default=(0.0, 0.0, 0.0, 0.0), update=MxNode.update_prop)
    nd_vector4I_in_which: IntProperty(name="Which", description="", default=0, update=MxNode.update_prop)
    nd_vector4I_out_out: FloatVectorProperty(name="Out", description="", subtype="NONE", size=4, update=MxNode.update_prop)


class MxNode_STD_convert(MxNode):
    _file_path = FILE_PATH
    _data_types = {'float_color3': {'nd_name': 'ND_convert_float_color3', 'nd': None}, 'float_color4': {'nd_name': 'ND_convert_float_color4', 'nd': None}, 'float_vector2': {'nd_name': 'ND_convert_float_vector2', 'nd': None}, 'float_vector3': {'nd_name': 'ND_convert_float_vector3', 'nd': None}, 'float_vector4': {'nd_name': 'ND_convert_float_vector4', 'nd': None}, 'vector2_vector3': {'nd_name': 'ND_convert_vector2_vector3', 'nd': None}, 'vector3_color3': {'nd_name': 'ND_convert_vector3_color3', 'nd': None}, 'vector3_vector2': {'nd_name': 'ND_convert_vector3_vector2', 'nd': None}, 'vector3_vector4': {'nd_name': 'ND_convert_vector3_vector4', 'nd': None}, 'vector4_color4': {'nd_name': 'ND_convert_vector4_color4', 'nd': None}, 'vector4_vector3': {'nd_name': 'ND_convert_vector4_vector3', 'nd': None}, 'color3_vector3': {'nd_name': 'ND_convert_color3_vector3', 'nd': None}, 'color4_vector4': {'nd_name': 'ND_convert_color4_vector4', 'nd': None}, 'color3_color4': {'nd_name': 'ND_convert_color3_color4', 'nd': None}, 'color4_color3': {'nd_name': 'ND_convert_color4_color3', 'nd': None}, 'boolean_float': {'nd_name': 'ND_convert_boolean_float', 'nd': None}, 'integer_float': {'nd_name': 'ND_convert_integer_float', 'nd': None}}

    bl_label = 'Convert'
    bl_idname = 'usdhydra.MxNode_STD_convert'
    bl_description = ""

    category = 'channel'

    data_type: EnumProperty(name="Type", description="Input Data Type", items=[('float_color3', 'Float color3', 'Float color3'), ('float_color4', 'Float color4', 'Float color4'), ('float_vector2', 'Float vector2', 'Float vector2'), ('float_vector3', 'Float vector3', 'Float vector3'), ('float_vector4', 'Float vector4', 'Float vector4'), ('vector2_vector3', 'Vector2 vector3', 'Vector2 vector3'), ('vector3_color3', 'Vector3 color3', 'Vector3 color3'), ('vector3_vector2', 'Vector3 vector2', 'Vector3 vector2'), ('vector3_vector4', 'Vector3 vector4', 'Vector3 vector4'), ('vector4_color4', 'Vector4 color4', 'Vector4 color4'), ('vector4_vector3', 'Vector4 vector3', 'Vector4 vector3'), ('color3_vector3', 'Color3 vector3', 'Color3 vector3'), ('color4_vector4', 'Color4 vector4', 'Color4 vector4'), ('color3_color4', 'Color3 color4', 'Color3 color4'), ('color4_color3', 'Color4 color3', 'Color4 color3'), ('boolean_float', 'Boolean float', 'Boolean float'), ('integer_float', 'Integer float', 'Integer float')], default='float_color3', update=MxNode.update_data_type)

    nd_float_color3_in_in: FloatProperty(name="In", description="", default=0.0, update=MxNode.update_prop)
    nd_float_color3_out_out: FloatVectorProperty(name="Out", description="", subtype="COLOR", size=3, soft_min=0.0, soft_max=1.0, update=MxNode.update_prop)

    nd_float_color4_in_in: FloatProperty(name="In", description="", default=0.0, update=MxNode.update_prop)
    nd_float_color4_out_out: FloatVectorProperty(name="Out", description="", subtype="COLOR", size=4, soft_min=0.0, soft_max=1.0, update=MxNode.update_prop)

    nd_float_vector2_in_in: FloatProperty(name="In", description="", default=0.0, update=MxNode.update_prop)
    nd_float_vector2_out_out: FloatVectorProperty(name="Out", description="", subtype="NONE", size=2, update=MxNode.update_prop)

    nd_float_vector3_in_in: FloatProperty(name="In", description="", default=0.0, update=MxNode.update_prop)
    nd_float_vector3_out_out: FloatVectorProperty(name="Out", description="", subtype="XYZ", size=3, update=MxNode.update_prop)

    nd_float_vector4_in_in: FloatProperty(name="In", description="", default=0.0, update=MxNode.update_prop)
    nd_float_vector4_out_out: FloatVectorProperty(name="Out", description="", subtype="NONE", size=4, update=MxNode.update_prop)

    nd_vector2_vector3_in_in: FloatVectorProperty(name="In", description="", subtype="NONE", size=2, default=(0.0, 0.0), update=MxNode.update_prop)
    nd_vector2_vector3_out_out: FloatVectorProperty(name="Out", description="", subtype="XYZ", size=3, update=MxNode.update_prop)

    nd_vector3_color3_in_in: FloatVectorProperty(name="In", description="", subtype="XYZ", size=3, default=(0.0, 0.0, 0.0), update=MxNode.update_prop)
    nd_vector3_color3_out_out: FloatVectorProperty(name="Out", description="", subtype="COLOR", size=3, soft_min=0.0, soft_max=1.0, update=MxNode.update_prop)

    nd_vector3_vector2_in_in: FloatVectorProperty(name="In", description="", subtype="XYZ", size=3, default=(0.0, 0.0, 0.0), update=MxNode.update_prop)
    nd_vector3_vector2_out_out: FloatVectorProperty(name="Out", description="", subtype="NONE", size=2, update=MxNode.update_prop)

    nd_vector3_vector4_in_in: FloatVectorProperty(name="In", description="", subtype="XYZ", size=3, default=(0.0, 0.0, 0.0), update=MxNode.update_prop)
    nd_vector3_vector4_out_out: FloatVectorProperty(name="Out", description="", subtype="NONE", size=4, update=MxNode.update_prop)

    nd_vector4_color4_in_in: FloatVectorProperty(name="In", description="", subtype="NONE", size=4, default=(0.0, 0.0, 0.0, 0.0), update=MxNode.update_prop)
    nd_vector4_color4_out_out: FloatVectorProperty(name="Out", description="", subtype="COLOR", size=4, soft_min=0.0, soft_max=1.0, update=MxNode.update_prop)

    nd_vector4_vector3_in_in: FloatVectorProperty(name="In", description="", subtype="NONE", size=4, default=(0.0, 0.0, 0.0, 0.0), update=MxNode.update_prop)
    nd_vector4_vector3_out_out: FloatVectorProperty(name="Out", description="", subtype="XYZ", size=3, update=MxNode.update_prop)

    nd_color3_vector3_in_in: FloatVectorProperty(name="In", description="", subtype="COLOR", size=3, soft_min=0.0, soft_max=1.0, default=(0.0, 0.0, 0.0), update=MxNode.update_prop)
    nd_color3_vector3_out_out: FloatVectorProperty(name="Out", description="", subtype="XYZ", size=3, update=MxNode.update_prop)

    nd_color4_vector4_in_in: FloatVectorProperty(name="In", description="", subtype="COLOR", size=4, soft_min=0.0, soft_max=1.0, default=(0.0, 0.0, 0.0, 0.0), update=MxNode.update_prop)
    nd_color4_vector4_out_out: FloatVectorProperty(name="Out", description="", subtype="NONE", size=4, update=MxNode.update_prop)

    nd_color3_color4_in_in: FloatVectorProperty(name="In", description="", subtype="COLOR", size=3, soft_min=0.0, soft_max=1.0, default=(0.0, 0.0, 0.0), update=MxNode.update_prop)
    nd_color3_color4_out_out: FloatVectorProperty(name="Out", description="", subtype="COLOR", size=4, soft_min=0.0, soft_max=1.0, update=MxNode.update_prop)

    nd_color4_color3_in_in: FloatVectorProperty(name="In", description="", subtype="COLOR", size=4, soft_min=0.0, soft_max=1.0, default=(0.0, 0.0, 0.0, 0.0), update=MxNode.update_prop)
    nd_color4_color3_out_out: FloatVectorProperty(name="Out", description="", subtype="COLOR", size=3, soft_min=0.0, soft_max=1.0, update=MxNode.update_prop)

    nd_boolean_float_in_in: BoolProperty(name="In", description="", default=False, update=MxNode.update_prop)
    nd_boolean_float_out_out: FloatProperty(name="Out", description="", update=MxNode.update_prop)

    nd_integer_float_in_in: IntProperty(name="In", description="", default=0, update=MxNode.update_prop)
    nd_integer_float_out_out: FloatProperty(name="Out", description="", update=MxNode.update_prop)


class MxNode_STD_swizzle(MxNode):
    _file_path = FILE_PATH
    _data_types = {'float_color3': {'nd_name': 'ND_swizzle_float_color3', 'nd': None}, 'float_color4': {'nd_name': 'ND_swizzle_float_color4', 'nd': None}, 'float_vector2': {'nd_name': 'ND_swizzle_float_vector2', 'nd': None}, 'float_vector3': {'nd_name': 'ND_swizzle_float_vector3', 'nd': None}, 'float_vector4': {'nd_name': 'ND_swizzle_float_vector4', 'nd': None}, 'color3_float': {'nd_name': 'ND_swizzle_color3_float', 'nd': None}, 'color3_color3': {'nd_name': 'ND_swizzle_color3_color3', 'nd': None}, 'color3_color4': {'nd_name': 'ND_swizzle_color3_color4', 'nd': None}, 'color3_vector2': {'nd_name': 'ND_swizzle_color3_vector2', 'nd': None}, 'color3_vector3': {'nd_name': 'ND_swizzle_color3_vector3', 'nd': None}, 'color3_vector4': {'nd_name': 'ND_swizzle_color3_vector4', 'nd': None}, 'color4_float': {'nd_name': 'ND_swizzle_color4_float', 'nd': None}, 'color4_color3': {'nd_name': 'ND_swizzle_color4_color3', 'nd': None}, 'color4_color4': {'nd_name': 'ND_swizzle_color4_color4', 'nd': None}, 'color4_vector2': {'nd_name': 'ND_swizzle_color4_vector2', 'nd': None}, 'color4_vector3': {'nd_name': 'ND_swizzle_color4_vector3', 'nd': None}, 'color4_vector4': {'nd_name': 'ND_swizzle_color4_vector4', 'nd': None}, 'vector2_float': {'nd_name': 'ND_swizzle_vector2_float', 'nd': None}, 'vector2_color3': {'nd_name': 'ND_swizzle_vector2_color3', 'nd': None}, 'vector2_color4': {'nd_name': 'ND_swizzle_vector2_color4', 'nd': None}, 'vector2_vector2': {'nd_name': 'ND_swizzle_vector2_vector2', 'nd': None}, 'vector2_vector3': {'nd_name': 'ND_swizzle_vector2_vector3', 'nd': None}, 'vector2_vector4': {'nd_name': 'ND_swizzle_vector2_vector4', 'nd': None}, 'vector3_float': {'nd_name': 'ND_swizzle_vector3_float', 'nd': None}, 'vector3_color3': {'nd_name': 'ND_swizzle_vector3_color3', 'nd': None}, 'vector3_color4': {'nd_name': 'ND_swizzle_vector3_color4', 'nd': None}, 'vector3_vector2': {'nd_name': 'ND_swizzle_vector3_vector2', 'nd': None}, 'vector3_vector3': {'nd_name': 'ND_swizzle_vector3_vector3', 'nd': None}, 'vector3_vector4': {'nd_name': 'ND_swizzle_vector3_vector4', 'nd': None}, 'vector4_float': {'nd_name': 'ND_swizzle_vector4_float', 'nd': None}, 'vector4_color3': {'nd_name': 'ND_swizzle_vector4_color3', 'nd': None}, 'vector4_color4': {'nd_name': 'ND_swizzle_vector4_color4', 'nd': None}, 'vector4_vector2': {'nd_name': 'ND_swizzle_vector4_vector2', 'nd': None}, 'vector4_vector3': {'nd_name': 'ND_swizzle_vector4_vector3', 'nd': None}, 'vector4_vector4': {'nd_name': 'ND_swizzle_vector4_vector4', 'nd': None}}

    bl_label = 'Swizzle'
    bl_idname = 'usdhydra.MxNode_STD_swizzle'
    bl_description = ""

    category = 'channel'

    data_type: EnumProperty(name="Type", description="Input Data Type", items=[('float_color3', 'Float color3', 'Float color3'), ('float_color4', 'Float color4', 'Float color4'), ('float_vector2', 'Float vector2', 'Float vector2'), ('float_vector3', 'Float vector3', 'Float vector3'), ('float_vector4', 'Float vector4', 'Float vector4'), ('color3_float', 'Color3 float', 'Color3 float'), ('color3_color3', 'Color3 color3', 'Color3 color3'), ('color3_color4', 'Color3 color4', 'Color3 color4'), ('color3_vector2', 'Color3 vector2', 'Color3 vector2'), ('color3_vector3', 'Color3 vector3', 'Color3 vector3'), ('color3_vector4', 'Color3 vector4', 'Color3 vector4'), ('color4_float', 'Color4 float', 'Color4 float'), ('color4_color3', 'Color4 color3', 'Color4 color3'), ('color4_color4', 'Color4 color4', 'Color4 color4'), ('color4_vector2', 'Color4 vector2', 'Color4 vector2'), ('color4_vector3', 'Color4 vector3', 'Color4 vector3'), ('color4_vector4', 'Color4 vector4', 'Color4 vector4'), ('vector2_float', 'Vector2 float', 'Vector2 float'), ('vector2_color3', 'Vector2 color3', 'Vector2 color3'), ('vector2_color4', 'Vector2 color4', 'Vector2 color4'), ('vector2_vector2', 'Vector2 vector2', 'Vector2 vector2'), ('vector2_vector3', 'Vector2 vector3', 'Vector2 vector3'), ('vector2_vector4', 'Vector2 vector4', 'Vector2 vector4'), ('vector3_float', 'Vector3 float', 'Vector3 float'), ('vector3_color3', 'Vector3 color3', 'Vector3 color3'), ('vector3_color4', 'Vector3 color4', 'Vector3 color4'), ('vector3_vector2', 'Vector3 vector2', 'Vector3 vector2'), ('vector3_vector3', 'Vector3 vector3', 'Vector3 vector3'), ('vector3_vector4', 'Vector3 vector4', 'Vector3 vector4'), ('vector4_float', 'Vector4 float', 'Vector4 float'), ('vector4_color3', 'Vector4 color3', 'Vector4 color3'), ('vector4_color4', 'Vector4 color4', 'Vector4 color4'), ('vector4_vector2', 'Vector4 vector2', 'Vector4 vector2'), ('vector4_vector3', 'Vector4 vector3', 'Vector4 vector3'), ('vector4_vector4', 'Vector4 vector4', 'Vector4 vector4')], default='float_color3', update=MxNode.update_data_type)

    nd_float_color3_in_in: FloatProperty(name="In", description="", default=0.0, update=MxNode.update_prop)
    nd_float_color3_in_channels: StringProperty(name="Channels", description="", default="rrr", update=MxNode.update_prop)
    nd_float_color3_out_out: FloatVectorProperty(name="Out", description="", subtype="COLOR", size=3, soft_min=0.0, soft_max=1.0, update=MxNode.update_prop)

    nd_float_color4_in_in: FloatProperty(name="In", description="", default=0.0, update=MxNode.update_prop)
    nd_float_color4_in_channels: StringProperty(name="Channels", description="", default="rrrr", update=MxNode.update_prop)
    nd_float_color4_out_out: FloatVectorProperty(name="Out", description="", subtype="COLOR", size=4, soft_min=0.0, soft_max=1.0, update=MxNode.update_prop)

    nd_float_vector2_in_in: FloatProperty(name="In", description="", default=0.0, update=MxNode.update_prop)
    nd_float_vector2_in_channels: StringProperty(name="Channels", description="", default="xx", update=MxNode.update_prop)
    nd_float_vector2_out_out: FloatVectorProperty(name="Out", description="", subtype="NONE", size=2, update=MxNode.update_prop)

    nd_float_vector3_in_in: FloatProperty(name="In", description="", default=0.0, update=MxNode.update_prop)
    nd_float_vector3_in_channels: StringProperty(name="Channels", description="", default="xxx", update=MxNode.update_prop)
    nd_float_vector3_out_out: FloatVectorProperty(name="Out", description="", subtype="XYZ", size=3, update=MxNode.update_prop)

    nd_float_vector4_in_in: FloatProperty(name="In", description="", default=0.0, update=MxNode.update_prop)
    nd_float_vector4_in_channels: StringProperty(name="Channels", description="", default="xxxx", update=MxNode.update_prop)
    nd_float_vector4_out_out: FloatVectorProperty(name="Out", description="", subtype="NONE", size=4, update=MxNode.update_prop)

    nd_color3_float_in_in: FloatVectorProperty(name="In", description="", subtype="COLOR", size=3, soft_min=0.0, soft_max=1.0, default=(0.0, 0.0, 0.0), update=MxNode.update_prop)
    nd_color3_float_in_channels: StringProperty(name="Channels", description="", default="r", update=MxNode.update_prop)
    nd_color3_float_out_out: FloatProperty(name="Out", description="", update=MxNode.update_prop)

    nd_color3_color3_in_in: FloatVectorProperty(name="In", description="", subtype="COLOR", size=3, soft_min=0.0, soft_max=1.0, default=(0.0, 0.0, 0.0), update=MxNode.update_prop)
    nd_color3_color3_in_channels: StringProperty(name="Channels", description="", default="rrr", update=MxNode.update_prop)
    nd_color3_color3_out_out: FloatVectorProperty(name="Out", description="", subtype="COLOR", size=3, soft_min=0.0, soft_max=1.0, update=MxNode.update_prop)

    nd_color3_color4_in_in: FloatVectorProperty(name="In", description="", subtype="COLOR", size=3, soft_min=0.0, soft_max=1.0, default=(0.0, 0.0, 0.0), update=MxNode.update_prop)
    nd_color3_color4_in_channels: StringProperty(name="Channels", description="", default="rrrr", update=MxNode.update_prop)
    nd_color3_color4_out_out: FloatVectorProperty(name="Out", description="", subtype="COLOR", size=4, soft_min=0.0, soft_max=1.0, update=MxNode.update_prop)

    nd_color3_vector2_in_in: FloatVectorProperty(name="In", description="", subtype="COLOR", size=3, soft_min=0.0, soft_max=1.0, default=(0.0, 0.0, 0.0), update=MxNode.update_prop)
    nd_color3_vector2_in_channels: StringProperty(name="Channels", description="", default="rr", update=MxNode.update_prop)
    nd_color3_vector2_out_out: FloatVectorProperty(name="Out", description="", subtype="NONE", size=2, update=MxNode.update_prop)

    nd_color3_vector3_in_in: FloatVectorProperty(name="In", description="", subtype="COLOR", size=3, soft_min=0.0, soft_max=1.0, default=(0.0, 0.0, 0.0), update=MxNode.update_prop)
    nd_color3_vector3_in_channels: StringProperty(name="Channels", description="", default="rrr", update=MxNode.update_prop)
    nd_color3_vector3_out_out: FloatVectorProperty(name="Out", description="", subtype="XYZ", size=3, update=MxNode.update_prop)

    nd_color3_vector4_in_in: FloatVectorProperty(name="In", description="", subtype="COLOR", size=3, soft_min=0.0, soft_max=1.0, default=(0.0, 0.0, 0.0), update=MxNode.update_prop)
    nd_color3_vector4_in_channels: StringProperty(name="Channels", description="", default="rrrr", update=MxNode.update_prop)
    nd_color3_vector4_out_out: FloatVectorProperty(name="Out", description="", subtype="NONE", size=4, update=MxNode.update_prop)

    nd_color4_float_in_in: FloatVectorProperty(name="In", description="", subtype="COLOR", size=4, soft_min=0.0, soft_max=1.0, default=(0.0, 0.0, 0.0, 0.0), update=MxNode.update_prop)
    nd_color4_float_in_channels: StringProperty(name="Channels", description="", default="r", update=MxNode.update_prop)
    nd_color4_float_out_out: FloatProperty(name="Out", description="", update=MxNode.update_prop)

    nd_color4_color3_in_in: FloatVectorProperty(name="In", description="", subtype="COLOR", size=4, soft_min=0.0, soft_max=1.0, default=(0.0, 0.0, 0.0, 0.0), update=MxNode.update_prop)
    nd_color4_color3_in_channels: StringProperty(name="Channels", description="", default="rrr", update=MxNode.update_prop)
    nd_color4_color3_out_out: FloatVectorProperty(name="Out", description="", subtype="COLOR", size=3, soft_min=0.0, soft_max=1.0, update=MxNode.update_prop)

    nd_color4_color4_in_in: FloatVectorProperty(name="In", description="", subtype="COLOR", size=4, soft_min=0.0, soft_max=1.0, default=(0.0, 0.0, 0.0, 0.0), update=MxNode.update_prop)
    nd_color4_color4_in_channels: StringProperty(name="Channels", description="", default="rrrr", update=MxNode.update_prop)
    nd_color4_color4_out_out: FloatVectorProperty(name="Out", description="", subtype="COLOR", size=4, soft_min=0.0, soft_max=1.0, update=MxNode.update_prop)

    nd_color4_vector2_in_in: FloatVectorProperty(name="In", description="", subtype="COLOR", size=4, soft_min=0.0, soft_max=1.0, default=(0.0, 0.0, 0.0, 0.0), update=MxNode.update_prop)
    nd_color4_vector2_in_channels: StringProperty(name="Channels", description="", default="rr", update=MxNode.update_prop)
    nd_color4_vector2_out_out: FloatVectorProperty(name="Out", description="", subtype="NONE", size=2, update=MxNode.update_prop)

    nd_color4_vector3_in_in: FloatVectorProperty(name="In", description="", subtype="COLOR", size=4, soft_min=0.0, soft_max=1.0, default=(0.0, 0.0, 0.0, 0.0), update=MxNode.update_prop)
    nd_color4_vector3_in_channels: StringProperty(name="Channels", description="", default="rrr", update=MxNode.update_prop)
    nd_color4_vector3_out_out: FloatVectorProperty(name="Out", description="", subtype="XYZ", size=3, update=MxNode.update_prop)

    nd_color4_vector4_in_in: FloatVectorProperty(name="In", description="", subtype="COLOR", size=4, soft_min=0.0, soft_max=1.0, default=(0.0, 0.0, 0.0, 0.0), update=MxNode.update_prop)
    nd_color4_vector4_in_channels: StringProperty(name="Channels", description="", default="rrrr", update=MxNode.update_prop)
    nd_color4_vector4_out_out: FloatVectorProperty(name="Out", description="", subtype="NONE", size=4, update=MxNode.update_prop)

    nd_vector2_float_in_in: FloatVectorProperty(name="In", description="", subtype="NONE", size=2, default=(0.0, 0.0), update=MxNode.update_prop)
    nd_vector2_float_in_channels: StringProperty(name="Channels", description="", default="x", update=MxNode.update_prop)
    nd_vector2_float_out_out: FloatProperty(name="Out", description="", update=MxNode.update_prop)

    nd_vector2_color3_in_in: FloatVectorProperty(name="In", description="", subtype="NONE", size=2, default=(0.0, 0.0), update=MxNode.update_prop)
    nd_vector2_color3_in_channels: StringProperty(name="Channels", description="", default="xxx", update=MxNode.update_prop)
    nd_vector2_color3_out_out: FloatVectorProperty(name="Out", description="", subtype="COLOR", size=3, soft_min=0.0, soft_max=1.0, update=MxNode.update_prop)

    nd_vector2_color4_in_in: FloatVectorProperty(name="In", description="", subtype="NONE", size=2, default=(0.0, 0.0), update=MxNode.update_prop)
    nd_vector2_color4_in_channels: StringProperty(name="Channels", description="", default="xxxx", update=MxNode.update_prop)
    nd_vector2_color4_out_out: FloatVectorProperty(name="Out", description="", subtype="COLOR", size=4, soft_min=0.0, soft_max=1.0, update=MxNode.update_prop)

    nd_vector2_vector2_in_in: FloatVectorProperty(name="In", description="", subtype="NONE", size=2, default=(0.0, 0.0), update=MxNode.update_prop)
    nd_vector2_vector2_in_channels: StringProperty(name="Channels", description="", default="xx", update=MxNode.update_prop)
    nd_vector2_vector2_out_out: FloatVectorProperty(name="Out", description="", subtype="NONE", size=2, update=MxNode.update_prop)

    nd_vector2_vector3_in_in: FloatVectorProperty(name="In", description="", subtype="NONE", size=2, default=(0.0, 0.0), update=MxNode.update_prop)
    nd_vector2_vector3_in_channels: StringProperty(name="Channels", description="", default="xxx", update=MxNode.update_prop)
    nd_vector2_vector3_out_out: FloatVectorProperty(name="Out", description="", subtype="XYZ", size=3, update=MxNode.update_prop)

    nd_vector2_vector4_in_in: FloatVectorProperty(name="In", description="", subtype="NONE", size=2, default=(0.0, 0.0), update=MxNode.update_prop)
    nd_vector2_vector4_in_channels: StringProperty(name="Channels", description="", default="xxxx", update=MxNode.update_prop)
    nd_vector2_vector4_out_out: FloatVectorProperty(name="Out", description="", subtype="NONE", size=4, update=MxNode.update_prop)

    nd_vector3_float_in_in: FloatVectorProperty(name="In", description="", subtype="XYZ", size=3, default=(0.0, 0.0, 0.0), update=MxNode.update_prop)
    nd_vector3_float_in_channels: StringProperty(name="Channels", description="", default="x", update=MxNode.update_prop)
    nd_vector3_float_out_out: FloatProperty(name="Out", description="", update=MxNode.update_prop)

    nd_vector3_color3_in_in: FloatVectorProperty(name="In", description="", subtype="XYZ", size=3, default=(0.0, 0.0, 0.0), update=MxNode.update_prop)
    nd_vector3_color3_in_channels: StringProperty(name="Channels", description="", default="xxx", update=MxNode.update_prop)
    nd_vector3_color3_out_out: FloatVectorProperty(name="Out", description="", subtype="COLOR", size=3, soft_min=0.0, soft_max=1.0, update=MxNode.update_prop)

    nd_vector3_color4_in_in: FloatVectorProperty(name="In", description="", subtype="XYZ", size=3, default=(0.0, 0.0, 0.0), update=MxNode.update_prop)
    nd_vector3_color4_in_channels: StringProperty(name="Channels", description="", default="xxxx", update=MxNode.update_prop)
    nd_vector3_color4_out_out: FloatVectorProperty(name="Out", description="", subtype="COLOR", size=4, soft_min=0.0, soft_max=1.0, update=MxNode.update_prop)

    nd_vector3_vector2_in_in: FloatVectorProperty(name="In", description="", subtype="XYZ", size=3, default=(0.0, 0.0, 0.0), update=MxNode.update_prop)
    nd_vector3_vector2_in_channels: StringProperty(name="Channels", description="", default="xx", update=MxNode.update_prop)
    nd_vector3_vector2_out_out: FloatVectorProperty(name="Out", description="", subtype="NONE", size=2, update=MxNode.update_prop)

    nd_vector3_vector3_in_in: FloatVectorProperty(name="In", description="", subtype="XYZ", size=3, default=(0.0, 0.0, 0.0), update=MxNode.update_prop)
    nd_vector3_vector3_in_channels: StringProperty(name="Channels", description="", default="xxx", update=MxNode.update_prop)
    nd_vector3_vector3_out_out: FloatVectorProperty(name="Out", description="", subtype="XYZ", size=3, update=MxNode.update_prop)

    nd_vector3_vector4_in_in: FloatVectorProperty(name="In", description="", subtype="XYZ", size=3, default=(0.0, 0.0, 0.0), update=MxNode.update_prop)
    nd_vector3_vector4_in_channels: StringProperty(name="Channels", description="", default="xxxx", update=MxNode.update_prop)
    nd_vector3_vector4_out_out: FloatVectorProperty(name="Out", description="", subtype="NONE", size=4, update=MxNode.update_prop)

    nd_vector4_float_in_in: FloatVectorProperty(name="In", description="", subtype="NONE", size=4, default=(0.0, 0.0, 0.0, 0.0), update=MxNode.update_prop)
    nd_vector4_float_in_channels: StringProperty(name="Channels", description="", default="x", update=MxNode.update_prop)
    nd_vector4_float_out_out: FloatProperty(name="Out", description="", update=MxNode.update_prop)

    nd_vector4_color3_in_in: FloatVectorProperty(name="In", description="", subtype="NONE", size=4, default=(0.0, 0.0, 0.0, 0.0), update=MxNode.update_prop)
    nd_vector4_color3_in_channels: StringProperty(name="Channels", description="", default="xxx", update=MxNode.update_prop)
    nd_vector4_color3_out_out: FloatVectorProperty(name="Out", description="", subtype="COLOR", size=3, soft_min=0.0, soft_max=1.0, update=MxNode.update_prop)

    nd_vector4_color4_in_in: FloatVectorProperty(name="In", description="", subtype="NONE", size=4, default=(0.0, 0.0, 0.0, 0.0), update=MxNode.update_prop)
    nd_vector4_color4_in_channels: StringProperty(name="Channels", description="", default="xxxx", update=MxNode.update_prop)
    nd_vector4_color4_out_out: FloatVectorProperty(name="Out", description="", subtype="COLOR", size=4, soft_min=0.0, soft_max=1.0, update=MxNode.update_prop)

    nd_vector4_vector2_in_in: FloatVectorProperty(name="In", description="", subtype="NONE", size=4, default=(0.0, 0.0, 0.0, 0.0), update=MxNode.update_prop)
    nd_vector4_vector2_in_channels: StringProperty(name="Channels", description="", default="xx", update=MxNode.update_prop)
    nd_vector4_vector2_out_out: FloatVectorProperty(name="Out", description="", subtype="NONE", size=2, update=MxNode.update_prop)

    nd_vector4_vector3_in_in: FloatVectorProperty(name="In", description="", subtype="NONE", size=4, default=(0.0, 0.0, 0.0, 0.0), update=MxNode.update_prop)
    nd_vector4_vector3_in_channels: StringProperty(name="Channels", description="", default="xxx", update=MxNode.update_prop)
    nd_vector4_vector3_out_out: FloatVectorProperty(name="Out", description="", subtype="XYZ", size=3, update=MxNode.update_prop)

    nd_vector4_vector4_in_in: FloatVectorProperty(name="In", description="", subtype="NONE", size=4, default=(0.0, 0.0, 0.0, 0.0), update=MxNode.update_prop)
    nd_vector4_vector4_in_channels: StringProperty(name="Channels", description="", default="xxxx", update=MxNode.update_prop)
    nd_vector4_vector4_out_out: FloatVectorProperty(name="Out", description="", subtype="NONE", size=4, update=MxNode.update_prop)


class MxNode_STD_combine2(MxNode):
    _file_path = FILE_PATH
    _data_types = {'vector2': {'nd_name': 'ND_combine2_vector2', 'nd': None}, 'color4CF': {'nd_name': 'ND_combine2_color4CF', 'nd': None}, 'vector4VF': {'nd_name': 'ND_combine2_vector4VF', 'nd': None}, 'vector4VV': {'nd_name': 'ND_combine2_vector4VV', 'nd': None}}

    bl_label = 'Combine2'
    bl_idname = 'usdhydra.MxNode_STD_combine2'
    bl_description = ""

    category = 'channel'

    data_type: EnumProperty(name="Type", description="Input Data Type", items=[('vector2', 'Vector2', 'Vector2'), ('color4CF', 'Color4CF', 'Color4CF'), ('vector4VF', 'Vector4VF', 'Vector4VF'), ('vector4VV', 'Vector4VV', 'Vector4VV')], default='vector2', update=MxNode.update_data_type)

    nd_vector2_in_in1: FloatProperty(name="In1", description="", default=0.0, update=MxNode.update_prop)
    nd_vector2_in_in2: FloatProperty(name="In2", description="", default=0.0, update=MxNode.update_prop)
    nd_vector2_out_out: FloatVectorProperty(name="Out", description="", subtype="NONE", size=2, update=MxNode.update_prop)

    nd_color4CF_in_in1: FloatVectorProperty(name="In1", description="", subtype="COLOR", size=3, soft_min=0.0, soft_max=1.0, default=(0.0, 0.0, 0.0), update=MxNode.update_prop)
    nd_color4CF_in_in2: FloatProperty(name="In2", description="", default=0.0, update=MxNode.update_prop)
    nd_color4CF_out_out: FloatVectorProperty(name="Out", description="", subtype="COLOR", size=4, soft_min=0.0, soft_max=1.0, update=MxNode.update_prop)

    nd_vector4VF_in_in1: FloatVectorProperty(name="In1", description="", subtype="XYZ", size=3, default=(0.0, 0.0, 0.0), update=MxNode.update_prop)
    nd_vector4VF_in_in2: FloatProperty(name="In2", description="", default=0.0, update=MxNode.update_prop)
    nd_vector4VF_out_out: FloatVectorProperty(name="Out", description="", subtype="NONE", size=4, update=MxNode.update_prop)

    nd_vector4VV_in_in1: FloatVectorProperty(name="In1", description="", subtype="NONE", size=2, default=(0.0, 0.0), update=MxNode.update_prop)
    nd_vector4VV_in_in2: FloatVectorProperty(name="In2", description="", subtype="NONE", size=2, default=(0.0, 0.0), update=MxNode.update_prop)
    nd_vector4VV_out_out: FloatVectorProperty(name="Out", description="", subtype="NONE", size=4, update=MxNode.update_prop)


class MxNode_STD_combine3(MxNode):
    _file_path = FILE_PATH
    _data_types = {'color3': {'nd_name': 'ND_combine3_color3', 'nd': None}, 'vector3': {'nd_name': 'ND_combine3_vector3', 'nd': None}}

    bl_label = 'Combine3'
    bl_idname = 'usdhydra.MxNode_STD_combine3'
    bl_description = ""

    category = 'channel'

    data_type: EnumProperty(name="Type", description="Input Data Type", items=[('color3', 'Color3', 'Color3'), ('vector3', 'Vector3', 'Vector3')], default='color3', update=MxNode.update_data_type)

    nd_color3_in_in1: FloatProperty(name="In1", description="", default=0.0, update=MxNode.update_prop)
    nd_color3_in_in2: FloatProperty(name="In2", description="", default=0.0, update=MxNode.update_prop)
    nd_color3_in_in3: FloatProperty(name="In3", description="", default=0.0, update=MxNode.update_prop)
    nd_color3_out_out: FloatVectorProperty(name="Out", description="", subtype="COLOR", size=3, soft_min=0.0, soft_max=1.0, update=MxNode.update_prop)

    nd_vector3_in_in1: FloatProperty(name="In1", description="", default=0.0, update=MxNode.update_prop)
    nd_vector3_in_in2: FloatProperty(name="In2", description="", default=0.0, update=MxNode.update_prop)
    nd_vector3_in_in3: FloatProperty(name="In3", description="", default=0.0, update=MxNode.update_prop)
    nd_vector3_out_out: FloatVectorProperty(name="Out", description="", subtype="XYZ", size=3, update=MxNode.update_prop)


class MxNode_STD_combine4(MxNode):
    _file_path = FILE_PATH
    _data_types = {'color4': {'nd_name': 'ND_combine4_color4', 'nd': None}, 'vector4': {'nd_name': 'ND_combine4_vector4', 'nd': None}}

    bl_label = 'Combine4'
    bl_idname = 'usdhydra.MxNode_STD_combine4'
    bl_description = ""

    category = 'channel'

    data_type: EnumProperty(name="Type", description="Input Data Type", items=[('color4', 'Color4', 'Color4'), ('vector4', 'Vector4', 'Vector4')], default='color4', update=MxNode.update_data_type)

    nd_color4_in_in1: FloatProperty(name="In1", description="", default=0.0, update=MxNode.update_prop)
    nd_color4_in_in2: FloatProperty(name="In2", description="", default=0.0, update=MxNode.update_prop)
    nd_color4_in_in3: FloatProperty(name="In3", description="", default=0.0, update=MxNode.update_prop)
    nd_color4_in_in4: FloatProperty(name="In4", description="", default=0.0, update=MxNode.update_prop)
    nd_color4_out_out: FloatVectorProperty(name="Out", description="", subtype="COLOR", size=4, soft_min=0.0, soft_max=1.0, update=MxNode.update_prop)

    nd_vector4_in_in1: FloatProperty(name="In1", description="", default=0.0, update=MxNode.update_prop)
    nd_vector4_in_in2: FloatProperty(name="In2", description="", default=0.0, update=MxNode.update_prop)
    nd_vector4_in_in3: FloatProperty(name="In3", description="", default=0.0, update=MxNode.update_prop)
    nd_vector4_in_in4: FloatProperty(name="In4", description="", default=0.0, update=MxNode.update_prop)
    nd_vector4_out_out: FloatVectorProperty(name="Out", description="", subtype="NONE", size=4, update=MxNode.update_prop)


class MxNode_STD_extract(MxNode):
    _file_path = FILE_PATH
    _data_types = {'color3': {'nd_name': 'ND_extract_color3', 'nd': None}, 'color4': {'nd_name': 'ND_extract_color4', 'nd': None}, 'vector2': {'nd_name': 'ND_extract_vector2', 'nd': None}, 'vector3': {'nd_name': 'ND_extract_vector3', 'nd': None}, 'vector4': {'nd_name': 'ND_extract_vector4', 'nd': None}}

    bl_label = 'Extract'
    bl_idname = 'usdhydra.MxNode_STD_extract'
    bl_description = ""

    category = 'channel'

    data_type: EnumProperty(name="Type", description="Input Data Type", items=[('color3', 'Color3', 'Color3'), ('color4', 'Color4', 'Color4'), ('vector2', 'Vector2', 'Vector2'), ('vector3', 'Vector3', 'Vector3'), ('vector4', 'Vector4', 'Vector4')], default='color3', update=MxNode.update_data_type)

    nd_color3_in_in: FloatVectorProperty(name="In", description="", subtype="COLOR", size=3, soft_min=0.0, soft_max=1.0, default=(0.0, 0.0, 0.0), update=MxNode.update_prop)
    nd_color3_in_index: IntProperty(name="Index", description="", min=0, max=2, default=0, update=MxNode.update_prop)
    nd_color3_out_out: FloatProperty(name="Out", description="", update=MxNode.update_prop)

    nd_color4_in_in: FloatVectorProperty(name="In", description="", subtype="COLOR", size=4, soft_min=0.0, soft_max=1.0, default=(0.0, 0.0, 0.0, 0.0), update=MxNode.update_prop)
    nd_color4_in_index: IntProperty(name="Index", description="", min=0, max=3, default=0, update=MxNode.update_prop)
    nd_color4_out_out: FloatProperty(name="Out", description="", update=MxNode.update_prop)

    nd_vector2_in_in: FloatVectorProperty(name="In", description="", subtype="NONE", size=2, default=(0.0, 0.0), update=MxNode.update_prop)
    nd_vector2_in_index: IntProperty(name="Index", description="", min=0, max=1, default=0, update=MxNode.update_prop)
    nd_vector2_out_out: FloatProperty(name="Out", description="", update=MxNode.update_prop)

    nd_vector3_in_in: FloatVectorProperty(name="In", description="", subtype="XYZ", size=3, default=(0.0, 0.0, 0.0), update=MxNode.update_prop)
    nd_vector3_in_index: IntProperty(name="Index", description="", min=0, max=2, default=0, update=MxNode.update_prop)
    nd_vector3_out_out: FloatProperty(name="Out", description="", update=MxNode.update_prop)

    nd_vector4_in_in: FloatVectorProperty(name="In", description="", subtype="NONE", size=4, default=(0.0, 0.0, 0.0, 0.0), update=MxNode.update_prop)
    nd_vector4_in_index: IntProperty(name="Index", description="", min=0, max=3, default=0, update=MxNode.update_prop)
    nd_vector4_out_out: FloatProperty(name="Out", description="", update=MxNode.update_prop)


class MxNode_STD_separate2(MxNode):
    _file_path = FILE_PATH
    _data_types = {'vector2': {'nd_name': 'ND_separate2_vector2', 'nd': None}}

    bl_label = 'Separate2'
    bl_idname = 'usdhydra.MxNode_STD_separate2'
    bl_description = ""

    category = 'channel'

    data_type: EnumProperty(name="Type", description="Input Data Type", items=[('vector2', 'Vector2', 'Vector2')], default='vector2', update=MxNode.update_data_type)

    nd_vector2_in_in: FloatVectorProperty(name="In", description="", subtype="NONE", size=2, default=(0.0, 0.0), update=MxNode.update_prop)
    nd_vector2_out_outx: FloatProperty(name="Outx", description="", update=MxNode.update_prop)
    nd_vector2_out_outy: FloatProperty(name="Outy", description="", update=MxNode.update_prop)


class MxNode_STD_separate3(MxNode):
    _file_path = FILE_PATH
    _data_types = {'color3': {'nd_name': 'ND_separate3_color3', 'nd': None}, 'vector3': {'nd_name': 'ND_separate3_vector3', 'nd': None}}

    bl_label = 'Separate3'
    bl_idname = 'usdhydra.MxNode_STD_separate3'
    bl_description = ""

    category = 'channel'

    data_type: EnumProperty(name="Type", description="Input Data Type", items=[('color3', 'Color3', 'Color3'), ('vector3', 'Vector3', 'Vector3')], default='color3', update=MxNode.update_data_type)

    nd_color3_in_in: FloatVectorProperty(name="In", description="", subtype="COLOR", size=3, soft_min=0.0, soft_max=1.0, default=(0.0, 0.0, 0.0), update=MxNode.update_prop)
    nd_color3_out_outr: FloatProperty(name="Outr", description="", update=MxNode.update_prop)
    nd_color3_out_outg: FloatProperty(name="Outg", description="", update=MxNode.update_prop)
    nd_color3_out_outb: FloatProperty(name="Outb", description="", update=MxNode.update_prop)

    nd_vector3_in_in: FloatVectorProperty(name="In", description="", subtype="XYZ", size=3, default=(0.0, 0.0, 0.0), update=MxNode.update_prop)
    nd_vector3_out_outx: FloatProperty(name="Outx", description="", update=MxNode.update_prop)
    nd_vector3_out_outy: FloatProperty(name="Outy", description="", update=MxNode.update_prop)
    nd_vector3_out_outz: FloatProperty(name="Outz", description="", update=MxNode.update_prop)


class MxNode_STD_separate4(MxNode):
    _file_path = FILE_PATH
    _data_types = {'color4': {'nd_name': 'ND_separate4_color4', 'nd': None}, 'vector4': {'nd_name': 'ND_separate4_vector4', 'nd': None}}

    bl_label = 'Separate4'
    bl_idname = 'usdhydra.MxNode_STD_separate4'
    bl_description = ""

    category = 'channel'

    data_type: EnumProperty(name="Type", description="Input Data Type", items=[('color4', 'Color4', 'Color4'), ('vector4', 'Vector4', 'Vector4')], default='color4', update=MxNode.update_data_type)

    nd_color4_in_in: FloatVectorProperty(name="In", description="", subtype="COLOR", size=4, soft_min=0.0, soft_max=1.0, default=(0.0, 0.0, 0.0, 0.0), update=MxNode.update_prop)
    nd_color4_out_outr: FloatProperty(name="Outr", description="", update=MxNode.update_prop)
    nd_color4_out_outg: FloatProperty(name="Outg", description="", update=MxNode.update_prop)
    nd_color4_out_outb: FloatProperty(name="Outb", description="", update=MxNode.update_prop)
    nd_color4_out_outa: FloatProperty(name="Outa", description="", update=MxNode.update_prop)

    nd_vector4_in_in: FloatVectorProperty(name="In", description="", subtype="NONE", size=4, default=(0.0, 0.0, 0.0, 0.0), update=MxNode.update_prop)
    nd_vector4_out_outx: FloatProperty(name="Outx", description="", update=MxNode.update_prop)
    nd_vector4_out_outy: FloatProperty(name="Outy", description="", update=MxNode.update_prop)
    nd_vector4_out_outz: FloatProperty(name="Outz", description="", update=MxNode.update_prop)
    nd_vector4_out_outw: FloatProperty(name="Outw", description="", update=MxNode.update_prop)


class MxNode_STD_blur(MxNode):
    _file_path = FILE_PATH
    _data_types = {'float': {'nd_name': 'ND_blur_float', 'nd': None}, 'color3': {'nd_name': 'ND_blur_color3', 'nd': None}, 'color4': {'nd_name': 'ND_blur_color4', 'nd': None}, 'vector2': {'nd_name': 'ND_blur_vector2', 'nd': None}, 'vector3': {'nd_name': 'ND_blur_vector3', 'nd': None}, 'vector4': {'nd_name': 'ND_blur_vector4', 'nd': None}}

    bl_label = 'Blur'
    bl_idname = 'usdhydra.MxNode_STD_blur'
    bl_description = ""

    category = 'convolution2d'

    data_type: EnumProperty(name="Type", description="Input Data Type", items=[('float', 'Float', 'Float'), ('color3', 'Color3', 'Color3'), ('color4', 'Color4', 'Color4'), ('vector2', 'Vector2', 'Vector2'), ('vector3', 'Vector3', 'Vector3'), ('vector4', 'Vector4', 'Vector4')], default='color3', update=MxNode.update_data_type)

    nd_float_in_in: FloatProperty(name="In", description="", default=0.0, update=MxNode.update_prop)
    nd_float_in_size: FloatProperty(name="Size", description="", default=0.0, update=MxNode.update_prop)
    nd_float_in_filtertype: EnumProperty(name="Filtertype", description="", items=(('box', 'Box', 'Box'), ('gaussian', 'Gaussian', 'Gaussian')), default="box", update=MxNode.update_prop)
    nd_float_out_out: FloatProperty(name="Out", description="", update=MxNode.update_prop)

    nd_color3_in_in: FloatVectorProperty(name="In", description="", subtype="COLOR", size=3, soft_min=0.0, soft_max=1.0, default=(0.0, 0.0, 0.0), update=MxNode.update_prop)
    nd_color3_in_size: FloatProperty(name="Size", description="", default=0.0, update=MxNode.update_prop)
    nd_color3_in_filtertype: EnumProperty(name="Filtertype", description="", items=(('box', 'Box', 'Box'), ('gaussian', 'Gaussian', 'Gaussian')), default="box", update=MxNode.update_prop)
    nd_color3_out_out: FloatVectorProperty(name="Out", description="", subtype="COLOR", size=3, soft_min=0.0, soft_max=1.0, update=MxNode.update_prop)

    nd_color4_in_in: FloatVectorProperty(name="In", description="", subtype="COLOR", size=4, soft_min=0.0, soft_max=1.0, default=(0.0, 0.0, 0.0, 0.0), update=MxNode.update_prop)
    nd_color4_in_size: FloatProperty(name="Size", description="", default=0.0, update=MxNode.update_prop)
    nd_color4_in_filtertype: EnumProperty(name="Filtertype", description="", items=(('box', 'Box', 'Box'), ('gaussian', 'Gaussian', 'Gaussian')), default="box", update=MxNode.update_prop)
    nd_color4_out_out: FloatVectorProperty(name="Out", description="", subtype="COLOR", size=4, soft_min=0.0, soft_max=1.0, update=MxNode.update_prop)

    nd_vector2_in_in: FloatVectorProperty(name="In", description="", subtype="NONE", size=2, default=(0.0, 0.0), update=MxNode.update_prop)
    nd_vector2_in_size: FloatProperty(name="Size", description="", default=0.0, update=MxNode.update_prop)
    nd_vector2_in_filtertype: EnumProperty(name="Filtertype", description="", items=(('box', 'Box', 'Box'), ('gaussian', 'Gaussian', 'Gaussian')), default="box", update=MxNode.update_prop)
    nd_vector2_out_out: FloatVectorProperty(name="Out", description="", subtype="NONE", size=2, update=MxNode.update_prop)

    nd_vector3_in_in: FloatVectorProperty(name="In", description="", subtype="XYZ", size=3, default=(0.0, 0.0, 0.0), update=MxNode.update_prop)
    nd_vector3_in_size: FloatProperty(name="Size", description="", default=0.0, update=MxNode.update_prop)
    nd_vector3_in_filtertype: EnumProperty(name="Filtertype", description="", items=(('box', 'Box', 'Box'), ('gaussian', 'Gaussian', 'Gaussian')), default="box", update=MxNode.update_prop)
    nd_vector3_out_out: FloatVectorProperty(name="Out", description="", subtype="XYZ", size=3, update=MxNode.update_prop)

    nd_vector4_in_in: FloatVectorProperty(name="In", description="", subtype="NONE", size=4, default=(0.0, 0.0, 0.0, 0.0), update=MxNode.update_prop)
    nd_vector4_in_size: FloatProperty(name="Size", description="", default=0.0, update=MxNode.update_prop)
    nd_vector4_in_filtertype: EnumProperty(name="Filtertype", description="", items=(('box', 'Box', 'Box'), ('gaussian', 'Gaussian', 'Gaussian')), default="box", update=MxNode.update_prop)
    nd_vector4_out_out: FloatVectorProperty(name="Out", description="", subtype="NONE", size=4, update=MxNode.update_prop)


class MxNode_STD_heighttonormal(MxNode):
    _file_path = FILE_PATH
    _data_types = {'vector3': {'nd_name': 'ND_heighttonormal_vector3', 'nd': None}}

    bl_label = 'Heighttonormal'
    bl_idname = 'usdhydra.MxNode_STD_heighttonormal'
    bl_description = ""

    category = 'convolution2d'

    data_type: EnumProperty(name="Type", description="Input Data Type", items=[('vector3', 'Vector3', 'Vector3')], default='vector3', update=MxNode.update_data_type)

    nd_vector3_in_in: FloatProperty(name="In", description="", default=0.0, update=MxNode.update_prop)
    nd_vector3_in_scale: FloatProperty(name="Scale", description="", default=1.0, update=MxNode.update_prop)
    nd_vector3_out_out: FloatVectorProperty(name="Out", description="", subtype="XYZ", size=3, update=MxNode.update_prop)


class MxNode_STD_dot(MxNode):
    _file_path = FILE_PATH
    _data_types = {'float': {'nd_name': 'ND_dot_float', 'nd': None}, 'color3': {'nd_name': 'ND_dot_color3', 'nd': None}, 'color4': {'nd_name': 'ND_dot_color4', 'nd': None}, 'vector2': {'nd_name': 'ND_dot_vector2', 'nd': None}, 'vector3': {'nd_name': 'ND_dot_vector3', 'nd': None}, 'vector4': {'nd_name': 'ND_dot_vector4', 'nd': None}, 'boolean': {'nd_name': 'ND_dot_boolean', 'nd': None}, 'integer': {'nd_name': 'ND_dot_integer', 'nd': None}, 'string': {'nd_name': 'ND_dot_string', 'nd': None}, 'filename': {'nd_name': 'ND_dot_filename', 'nd': None}, 'surfaceshader': {'nd_name': 'ND_dot_surfaceshader', 'nd': None}, 'displacementshader': {'nd_name': 'ND_dot_displacementshader', 'nd': None}, 'volumeshader': {'nd_name': 'ND_dot_volumeshader', 'nd': None}, 'lightshader': {'nd_name': 'ND_dot_lightshader', 'nd': None}}

    bl_label = 'Dot'
    bl_idname = 'usdhydra.MxNode_STD_dot'
    bl_description = ""

    category = 'organization'

    data_type: EnumProperty(name="Type", description="Input Data Type", items=[('float', 'Float', 'Float'), ('color3', 'Color3', 'Color3'), ('color4', 'Color4', 'Color4'), ('vector2', 'Vector2', 'Vector2'), ('vector3', 'Vector3', 'Vector3'), ('vector4', 'Vector4', 'Vector4'), ('boolean', 'Boolean', 'Boolean'), ('integer', 'Integer', 'Integer'), ('string', 'String', 'String'), ('filename', 'Filename', 'Filename'), ('surfaceshader', 'Surfaceshader', 'Surfaceshader'), ('displacementshader', 'Displacementshader', 'Displacementshader'), ('volumeshader', 'Volumeshader', 'Volumeshader'), ('lightshader', 'Lightshader', 'Lightshader')], default='color3', update=MxNode.update_data_type)

    nd_float_in_in: FloatProperty(name="In", description="", default=0.0, update=MxNode.update_prop)
    nd_float_in_note: StringProperty(name="Note", description="", default="", update=MxNode.update_prop)
    nd_float_out_out: FloatProperty(name="Out", description="", update=MxNode.update_prop)

    nd_color3_in_in: FloatVectorProperty(name="In", description="", subtype="COLOR", size=3, soft_min=0.0, soft_max=1.0, default=(0.0, 0.0, 0.0), update=MxNode.update_prop)
    nd_color3_in_note: StringProperty(name="Note", description="", default="", update=MxNode.update_prop)
    nd_color3_out_out: FloatVectorProperty(name="Out", description="", subtype="COLOR", size=3, soft_min=0.0, soft_max=1.0, update=MxNode.update_prop)

    nd_color4_in_in: FloatVectorProperty(name="In", description="", subtype="COLOR", size=4, soft_min=0.0, soft_max=1.0, default=(0.0, 0.0, 0.0, 0.0), update=MxNode.update_prop)
    nd_color4_in_note: StringProperty(name="Note", description="", default="", update=MxNode.update_prop)
    nd_color4_out_out: FloatVectorProperty(name="Out", description="", subtype="COLOR", size=4, soft_min=0.0, soft_max=1.0, update=MxNode.update_prop)

    nd_vector2_in_in: FloatVectorProperty(name="In", description="", subtype="NONE", size=2, default=(0.0, 0.0), update=MxNode.update_prop)
    nd_vector2_in_note: StringProperty(name="Note", description="", default="", update=MxNode.update_prop)
    nd_vector2_out_out: FloatVectorProperty(name="Out", description="", subtype="NONE", size=2, update=MxNode.update_prop)

    nd_vector3_in_in: FloatVectorProperty(name="In", description="", subtype="XYZ", size=3, default=(0.0, 0.0, 0.0), update=MxNode.update_prop)
    nd_vector3_in_note: StringProperty(name="Note", description="", default="", update=MxNode.update_prop)
    nd_vector3_out_out: FloatVectorProperty(name="Out", description="", subtype="XYZ", size=3, update=MxNode.update_prop)

    nd_vector4_in_in: FloatVectorProperty(name="In", description="", subtype="NONE", size=4, default=(0.0, 0.0, 0.0, 0.0), update=MxNode.update_prop)
    nd_vector4_in_note: StringProperty(name="Note", description="", default="", update=MxNode.update_prop)
    nd_vector4_out_out: FloatVectorProperty(name="Out", description="", subtype="NONE", size=4, update=MxNode.update_prop)

    nd_boolean_in_in: BoolProperty(name="In", description="", default=False, update=MxNode.update_prop)
    nd_boolean_in_note: StringProperty(name="Note", description="", default="", update=MxNode.update_prop)
    nd_boolean_out_out: BoolProperty(name="Out", description="", update=MxNode.update_prop)

    nd_integer_in_in: IntProperty(name="In", description="", default=0, update=MxNode.update_prop)
    nd_integer_in_note: StringProperty(name="Note", description="", default="", update=MxNode.update_prop)
    nd_integer_out_out: IntProperty(name="Out", description="", update=MxNode.update_prop)

    nd_string_in_in: StringProperty(name="In", description="", default="", update=MxNode.update_prop)
    nd_string_in_note: StringProperty(name="Note", description="", default="", update=MxNode.update_prop)
    nd_string_out_out: StringProperty(name="Out", description="", update=MxNode.update_prop)

    nd_filename_in_in: StringProperty(name="In", description="", subtype="FILE_PATH", default="", update=MxNode.update_prop)
    nd_filename_in_note: StringProperty(name="Note", description="", default="", update=MxNode.update_prop)
    nd_filename_out_out: StringProperty(name="Out", description="", subtype="FILE_PATH", update=MxNode.update_prop)

    nd_surfaceshader_in_in: StringProperty(name="In", description="", default="", update=MxNode.update_prop)
    nd_surfaceshader_in_note: StringProperty(name="Note", description="", default="", update=MxNode.update_prop)
    nd_surfaceshader_out_out: StringProperty(name="Out", description="", update=MxNode.update_prop)

    nd_displacementshader_in_in: StringProperty(name="In", description="", default="", update=MxNode.update_prop)
    nd_displacementshader_in_note: StringProperty(name="Note", description="", default="", update=MxNode.update_prop)
    nd_displacementshader_out_out: StringProperty(name="Out", description="", update=MxNode.update_prop)

    nd_volumeshader_in_in: StringProperty(name="In", description="", default="", update=MxNode.update_prop)
    nd_volumeshader_in_note: StringProperty(name="Note", description="", default="", update=MxNode.update_prop)
    nd_volumeshader_out_out: StringProperty(name="Out", description="", update=MxNode.update_prop)

    nd_lightshader_in_in: StringProperty(name="In", description="", default="", update=MxNode.update_prop)
    nd_lightshader_in_note: StringProperty(name="Note", description="", default="", update=MxNode.update_prop)
    nd_lightshader_out_out: StringProperty(name="Out", description="", update=MxNode.update_prop)


mx_node_classes = [MxNode_STD_surfacematerial, MxNode_STD_volumematerial, MxNode_STD_surface_unlit, MxNode_STD_image, MxNode_STD_tiledimage, MxNode_STD_triplanarprojection, MxNode_STD_constant, MxNode_STD_ramplr, MxNode_STD_ramptb, MxNode_STD_ramp4, MxNode_STD_splitlr, MxNode_STD_splittb, MxNode_STD_noise2d, MxNode_STD_noise3d, MxNode_STD_fractal3d, MxNode_STD_cellnoise2d, MxNode_STD_cellnoise3d, MxNode_STD_worleynoise2d, MxNode_STD_worleynoise3d, MxNode_STD_position, MxNode_STD_normal, MxNode_STD_tangent, MxNode_STD_bitangent, MxNode_STD_texcoord, MxNode_STD_geomcolor, MxNode_STD_geompropvalue, MxNode_STD_ambientocclusion, MxNode_STD_frame, MxNode_STD_time, MxNode_STD_add, MxNode_STD_subtract, MxNode_STD_multiply, MxNode_STD_divide, MxNode_STD_modulo, MxNode_STD_invert, MxNode_STD_absval, MxNode_STD_floor, MxNode_STD_ceil, MxNode_STD_power, MxNode_STD_sin, MxNode_STD_cos, MxNode_STD_tan, MxNode_STD_asin, MxNode_STD_acos, MxNode_STD_atan2, MxNode_STD_sqrt, MxNode_STD_ln, MxNode_STD_exp, MxNode_STD_sign, MxNode_STD_clamp, MxNode_STD_min, MxNode_STD_max, MxNode_STD_normalize, MxNode_STD_magnitude, MxNode_STD_dotproduct, MxNode_STD_crossproduct, MxNode_STD_transformpoint, MxNode_STD_transformvector, MxNode_STD_transformnormal, MxNode_STD_transformmatrix, MxNode_STD_normalmap, MxNode_STD_rotate2d, MxNode_STD_rotate3d, MxNode_STD_place2d, MxNode_STD_arrayappend, MxNode_STD_remap, MxNode_STD_smoothstep, MxNode_STD_curveadjust, MxNode_STD_luminance, MxNode_STD_rgbtohsv, MxNode_STD_hsvtorgb, MxNode_STD_contrast, MxNode_STD_range, MxNode_STD_hsvadjust, MxNode_STD_saturate, MxNode_STD_premult, MxNode_STD_unpremult, MxNode_STD_plus, MxNode_STD_minus, MxNode_STD_difference, MxNode_STD_burn, MxNode_STD_dodge, MxNode_STD_screen, MxNode_STD_overlay, MxNode_STD_disjointover, MxNode_STD_in, MxNode_STD_mask, MxNode_STD_matte, MxNode_STD_out, MxNode_STD_over, MxNode_STD_inside, MxNode_STD_outside, MxNode_STD_mix, MxNode_STD_ifgreater, MxNode_STD_ifgreatereq, MxNode_STD_ifequal, MxNode_STD_switch, MxNode_STD_convert, MxNode_STD_swizzle, MxNode_STD_combine2, MxNode_STD_combine3, MxNode_STD_combine4, MxNode_STD_extract, MxNode_STD_separate2, MxNode_STD_separate3, MxNode_STD_separate4, MxNode_STD_blur, MxNode_STD_heighttonormal, MxNode_STD_dot]
