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


FILE_PATH = r"libraries\pbrlib\pbrlib_defs.mtlx"


class MxNode_PBR_oren_nayar_diffuse_bsdf(MxNode):
    _file_path = FILE_PATH
    _data_types = {'BSDF': {'nd_name': 'ND_oren_nayar_diffuse_bsdf', 'nd': None}}

    bl_label = 'Oren nayar diffuse bsdf'
    bl_idname = 'usdhydra.MxNode_PBR_oren_nayar_diffuse_bsdf'
    bl_description = "A BSDF node for diffuse reflections."

    category = 'PBR'

    data_type: EnumProperty(name="Type", description="Input Data Type", items=[('BSDF', 'BSDF', 'BSDF')], default='BSDF', update=MxNode.update_data_type)

    nd_BSDF_in_weight: FloatProperty(name="Weight", description="", min=0.0, max=1.0, default=1.0, update=MxNode.update_prop)
    nd_BSDF_in_color: FloatVectorProperty(name="Color", description="", subtype="COLOR", size=3, soft_min=0.0, soft_max=1.0, default=(0.18, 0.18, 0.18), update=MxNode.update_prop)
    nd_BSDF_in_roughness: FloatProperty(name="Roughness", description="", default=0.0, update=MxNode.update_prop)
    nd_BSDF_in_normal: FloatVectorProperty(name="Normal", description="", subtype="XYZ", size=3, update=MxNode.update_prop)
    nd_BSDF_out_out: StringProperty(name="Out", description="", update=MxNode.update_prop)


class MxNode_PBR_burley_diffuse_bsdf(MxNode):
    _file_path = FILE_PATH
    _data_types = {'BSDF': {'nd_name': 'ND_burley_diffuse_bsdf', 'nd': None}}

    bl_label = 'Burley diffuse bsdf'
    bl_idname = 'usdhydra.MxNode_PBR_burley_diffuse_bsdf'
    bl_description = "A BSDF node for Burley diffuse reflections."

    category = 'PBR'

    data_type: EnumProperty(name="Type", description="Input Data Type", items=[('BSDF', 'BSDF', 'BSDF')], default='BSDF', update=MxNode.update_data_type)

    nd_BSDF_in_weight: FloatProperty(name="Weight", description="", min=0.0, max=1.0, default=1.0, update=MxNode.update_prop)
    nd_BSDF_in_color: FloatVectorProperty(name="Color", description="", subtype="COLOR", size=3, soft_min=0.0, soft_max=1.0, default=(0.18, 0.18, 0.18), update=MxNode.update_prop)
    nd_BSDF_in_roughness: FloatProperty(name="Roughness", description="", default=0.0, update=MxNode.update_prop)
    nd_BSDF_in_normal: FloatVectorProperty(name="Normal", description="", subtype="XYZ", size=3, update=MxNode.update_prop)
    nd_BSDF_out_out: StringProperty(name="Out", description="", update=MxNode.update_prop)


class MxNode_PBR_translucent_bsdf(MxNode):
    _file_path = FILE_PATH
    _data_types = {'BSDF': {'nd_name': 'ND_translucent_bsdf', 'nd': None}}

    bl_label = 'Translucent bsdf'
    bl_idname = 'usdhydra.MxNode_PBR_translucent_bsdf'
    bl_description = "A BSDF node for pure diffuse transmission."

    category = 'PBR'

    data_type: EnumProperty(name="Type", description="Input Data Type", items=[('BSDF', 'BSDF', 'BSDF')], default='BSDF', update=MxNode.update_data_type)

    nd_BSDF_in_weight: FloatProperty(name="Weight", description="", min=0.0, max=1.0, default=1.0, update=MxNode.update_prop)
    nd_BSDF_in_color: FloatVectorProperty(name="Color", description="", subtype="COLOR", size=3, soft_min=0.0, soft_max=1.0, default=(1.0, 1.0, 1.0), update=MxNode.update_prop)
    nd_BSDF_in_normal: FloatVectorProperty(name="Normal", description="", subtype="XYZ", size=3, update=MxNode.update_prop)
    nd_BSDF_out_out: StringProperty(name="Out", description="", update=MxNode.update_prop)


class MxNode_PBR_dielectric_bsdf(MxNode):
    _file_path = FILE_PATH
    _data_types = {'BSDF': {'nd_name': 'ND_dielectric_bsdf', 'nd': None}}

    bl_label = 'Dielectric bsdf'
    bl_idname = 'usdhydra.MxNode_PBR_dielectric_bsdf'
    bl_description = "A reflection/transmission BSDF node based on a microfacet model and a Fresnel curve for dielectrics."

    category = 'PBR'

    data_type: EnumProperty(name="Type", description="Input Data Type", items=[('BSDF', 'BSDF', 'BSDF')], default='BSDF', update=MxNode.update_data_type)

    nd_BSDF_in_weight: FloatProperty(name="Weight", description="", min=0.0, max=1.0, default=1.0, update=MxNode.update_prop)
    nd_BSDF_in_tint: FloatVectorProperty(name="Tint", description="", subtype="COLOR", size=3, soft_min=0.0, soft_max=1.0, default=(1.0, 1.0, 1.0), update=MxNode.update_prop)
    nd_BSDF_in_ior: FloatProperty(name="Ior", description="", default=1.5, update=MxNode.update_prop)
    nd_BSDF_in_roughness: FloatVectorProperty(name="Roughness", description="", subtype="NONE", size=2, default=(0.05, 0.05), update=MxNode.update_prop)
    nd_BSDF_in_normal: FloatVectorProperty(name="Normal", description="", subtype="XYZ", size=3, update=MxNode.update_prop)
    nd_BSDF_in_tangent: FloatVectorProperty(name="Tangent", description="", subtype="XYZ", size=3, update=MxNode.update_prop)
    nd_BSDF_in_distribution: EnumProperty(name="Distribution", description="", items=(('ggx', 'Ggx', 'Ggx'),), default="ggx", update=MxNode.update_prop)
    nd_BSDF_in_scatter_mode: EnumProperty(name="Scatter mode", description="", items=(('R', 'R', 'R'), ('T', 'T', 'T'), ('RT', 'RT', 'RT')), default="R", update=MxNode.update_prop)
    nd_BSDF_out_out: StringProperty(name="Out", description="", update=MxNode.update_prop)


class MxNode_PBR_conductor_bsdf(MxNode):
    _file_path = FILE_PATH
    _data_types = {'BSDF': {'nd_name': 'ND_conductor_bsdf', 'nd': None}}

    bl_label = 'Conductor bsdf'
    bl_idname = 'usdhydra.MxNode_PBR_conductor_bsdf'
    bl_description = "A reflection BSDF node based on a microfacet model and a Fresnel curve for conductors/metals."

    category = 'PBR'

    data_type: EnumProperty(name="Type", description="Input Data Type", items=[('BSDF', 'BSDF', 'BSDF')], default='BSDF', update=MxNode.update_data_type)

    nd_BSDF_in_weight: FloatProperty(name="Weight", description="", min=0.0, max=1.0, default=1.0, update=MxNode.update_prop)
    nd_BSDF_in_ior: FloatVectorProperty(name="Ior", description="", subtype="COLOR", size=3, soft_min=0.0, soft_max=1.0, default=(0.271, 0.677, 1.316), update=MxNode.update_prop)
    nd_BSDF_in_extinction: FloatVectorProperty(name="Extinction", description="", subtype="COLOR", size=3, soft_min=0.0, soft_max=1.0, default=(3.609, 2.625, 2.292), update=MxNode.update_prop)
    nd_BSDF_in_roughness: FloatVectorProperty(name="Roughness", description="", subtype="NONE", size=2, default=(0.05, 0.05), update=MxNode.update_prop)
    nd_BSDF_in_normal: FloatVectorProperty(name="Normal", description="", subtype="XYZ", size=3, update=MxNode.update_prop)
    nd_BSDF_in_tangent: FloatVectorProperty(name="Tangent", description="", subtype="XYZ", size=3, update=MxNode.update_prop)
    nd_BSDF_in_distribution: EnumProperty(name="Distribution", description="", items=(('ggx', 'Ggx', 'Ggx'),), default="ggx", update=MxNode.update_prop)
    nd_BSDF_out_out: StringProperty(name="Out", description="", update=MxNode.update_prop)


class MxNode_PBR_generalized_schlick_bsdf(MxNode):
    _file_path = FILE_PATH
    _data_types = {'BSDF': {'nd_name': 'ND_generalized_schlick_bsdf', 'nd': None}}

    bl_label = 'Generalized schlick bsdf'
    bl_idname = 'usdhydra.MxNode_PBR_generalized_schlick_bsdf'
    bl_description = "A reflection/transmission BSDF node based on a microfacet model and a generalized Schlick Fresnel curve."

    category = 'PBR'

    data_type: EnumProperty(name="Type", description="Input Data Type", items=[('BSDF', 'BSDF', 'BSDF')], default='BSDF', update=MxNode.update_data_type)

    nd_BSDF_in_weight: FloatProperty(name="Weight", description="", min=0.0, max=1.0, default=1.0, update=MxNode.update_prop)
    nd_BSDF_in_color0: FloatVectorProperty(name="Color0", description="", subtype="COLOR", size=3, soft_min=0.0, soft_max=1.0, default=(1.0, 1.0, 1.0), update=MxNode.update_prop)
    nd_BSDF_in_color90: FloatVectorProperty(name="Color90", description="", subtype="COLOR", size=3, soft_min=0.0, soft_max=1.0, default=(1.0, 1.0, 1.0), update=MxNode.update_prop)
    nd_BSDF_in_exponent: FloatProperty(name="Exponent", description="", default=5.0, update=MxNode.update_prop)
    nd_BSDF_in_roughness: FloatVectorProperty(name="Roughness", description="", subtype="NONE", size=2, default=(0.05, 0.05), update=MxNode.update_prop)
    nd_BSDF_in_normal: FloatVectorProperty(name="Normal", description="", subtype="XYZ", size=3, update=MxNode.update_prop)
    nd_BSDF_in_tangent: FloatVectorProperty(name="Tangent", description="", subtype="XYZ", size=3, update=MxNode.update_prop)
    nd_BSDF_in_distribution: EnumProperty(name="Distribution", description="", items=(('ggx', 'Ggx', 'Ggx'),), default="ggx", update=MxNode.update_prop)
    nd_BSDF_in_scatter_mode: EnumProperty(name="Scatter mode", description="", items=(('R', 'R', 'R'), ('T', 'T', 'T'), ('RT', 'RT', 'RT')), default="R", update=MxNode.update_prop)
    nd_BSDF_out_out: StringProperty(name="Out", description="", update=MxNode.update_prop)


class MxNode_PBR_subsurface_bsdf(MxNode):
    _file_path = FILE_PATH
    _data_types = {'BSDF': {'nd_name': 'ND_subsurface_bsdf', 'nd': None}}

    bl_label = 'Subsurface bsdf'
    bl_idname = 'usdhydra.MxNode_PBR_subsurface_bsdf'
    bl_description = "A subsurface scattering BSDF for true subsurface scattering."

    category = 'PBR'

    data_type: EnumProperty(name="Type", description="Input Data Type", items=[('BSDF', 'BSDF', 'BSDF')], default='BSDF', update=MxNode.update_data_type)

    nd_BSDF_in_weight: FloatProperty(name="Weight", description="", min=0.0, max=1.0, default=1.0, update=MxNode.update_prop)
    nd_BSDF_in_color: FloatVectorProperty(name="Color", description="", subtype="COLOR", size=3, soft_min=0.0, soft_max=1.0, default=(0.18, 0.18, 0.18), update=MxNode.update_prop)
    nd_BSDF_in_radius: FloatVectorProperty(name="Radius", description="", subtype="XYZ", size=3, default=(1.0, 1.0, 1.0), update=MxNode.update_prop)
    nd_BSDF_in_anisotropy: FloatProperty(name="Anisotropy", description="", default=0.0, update=MxNode.update_prop)
    nd_BSDF_in_normal: FloatVectorProperty(name="Normal", description="", subtype="XYZ", size=3, update=MxNode.update_prop)
    nd_BSDF_out_out: StringProperty(name="Out", description="", update=MxNode.update_prop)


class MxNode_PBR_sheen_bsdf(MxNode):
    _file_path = FILE_PATH
    _data_types = {'BSDF': {'nd_name': 'ND_sheen_bsdf', 'nd': None}}

    bl_label = 'Sheen bsdf'
    bl_idname = 'usdhydra.MxNode_PBR_sheen_bsdf'
    bl_description = "A microfacet BSDF for the back-scattering properties of cloth-like materials."

    category = 'PBR'

    data_type: EnumProperty(name="Type", description="Input Data Type", items=[('BSDF', 'BSDF', 'BSDF')], default='BSDF', update=MxNode.update_data_type)

    nd_BSDF_in_weight: FloatProperty(name="Weight", description="", min=0.0, max=1.0, default=1.0, update=MxNode.update_prop)
    nd_BSDF_in_color: FloatVectorProperty(name="Color", description="", subtype="COLOR", size=3, soft_min=0.0, soft_max=1.0, default=(1.0, 1.0, 1.0), update=MxNode.update_prop)
    nd_BSDF_in_roughness: FloatProperty(name="Roughness", description="", default=0.3, update=MxNode.update_prop)
    nd_BSDF_in_normal: FloatVectorProperty(name="Normal", description="", subtype="XYZ", size=3, update=MxNode.update_prop)
    nd_BSDF_out_out: StringProperty(name="Out", description="", update=MxNode.update_prop)


class MxNode_PBR_thin_film_bsdf(MxNode):
    _file_path = FILE_PATH
    _data_types = {'BSDF': {'nd_name': 'ND_thin_film_bsdf', 'nd': None}}

    bl_label = 'Thin film bsdf'
    bl_idname = 'usdhydra.MxNode_PBR_thin_film_bsdf'
    bl_description = "Adds an iridescent thin film layer over a microfacet base BSDF."

    category = 'PBR'

    data_type: EnumProperty(name="Type", description="Input Data Type", items=[('BSDF', 'BSDF', 'BSDF')], default='BSDF', update=MxNode.update_data_type)

    nd_BSDF_in_thickness: FloatProperty(name="Thickness", description="", default=550.0, update=MxNode.update_prop)
    nd_BSDF_in_ior: FloatProperty(name="Ior", description="", default=1.5, update=MxNode.update_prop)
    nd_BSDF_out_out: StringProperty(name="Out", description="", update=MxNode.update_prop)


class MxNode_PBR_uniform_edf(MxNode):
    _file_path = FILE_PATH
    _data_types = {'EDF': {'nd_name': 'ND_uniform_edf', 'nd': None}}

    bl_label = 'Uniform edf'
    bl_idname = 'usdhydra.MxNode_PBR_uniform_edf'
    bl_description = "An EDF node for uniform emission."

    category = 'PBR'

    data_type: EnumProperty(name="Type", description="Input Data Type", items=[('EDF', 'EDF', 'EDF')], default='EDF', update=MxNode.update_data_type)

    nd_EDF_in_color: FloatVectorProperty(name="Color", description="", subtype="COLOR", size=3, soft_min=0.0, soft_max=1.0, default=(1.0, 1.0, 1.0), update=MxNode.update_prop)
    nd_EDF_out_out: StringProperty(name="Out", description="", update=MxNode.update_prop)


class MxNode_PBR_conical_edf(MxNode):
    _file_path = FILE_PATH
    _data_types = {'EDF': {'nd_name': 'ND_conical_edf', 'nd': None}}

    bl_label = 'Conical edf'
    bl_idname = 'usdhydra.MxNode_PBR_conical_edf'
    bl_description = "Constructs an EDF emitting light inside a cone around the normal direction."

    category = 'PBR'

    data_type: EnumProperty(name="Type", description="Input Data Type", items=[('EDF', 'EDF', 'EDF')], default='EDF', update=MxNode.update_data_type)

    nd_EDF_in_color: FloatVectorProperty(name="Color", description="", subtype="COLOR", size=3, soft_min=0.0, soft_max=1.0, default=(1.0, 1.0, 1.0), update=MxNode.update_prop)
    nd_EDF_in_normal: FloatVectorProperty(name="Normal", description="", subtype="XYZ", size=3, update=MxNode.update_prop)
    nd_EDF_in_inner_angle: FloatProperty(name="Inner angle", description="", default=60.0, update=MxNode.update_prop)
    nd_EDF_in_outer_angle: FloatProperty(name="Outer angle", description="", default=0.0, update=MxNode.update_prop)
    nd_EDF_out_out: StringProperty(name="Out", description="", update=MxNode.update_prop)


class MxNode_PBR_measured_edf(MxNode):
    _file_path = FILE_PATH
    _data_types = {'EDF': {'nd_name': 'ND_measured_edf', 'nd': None}}

    bl_label = 'Measured edf'
    bl_idname = 'usdhydra.MxNode_PBR_measured_edf'
    bl_description = "Constructs an EDF emitting light according to a measured IES light profile."

    category = 'PBR'

    data_type: EnumProperty(name="Type", description="Input Data Type", items=[('EDF', 'EDF', 'EDF')], default='EDF', update=MxNode.update_data_type)

    nd_EDF_in_color: FloatVectorProperty(name="Color", description="", subtype="COLOR", size=3, soft_min=0.0, soft_max=1.0, default=(1.0, 1.0, 1.0), update=MxNode.update_prop)
    nd_EDF_in_normal: FloatVectorProperty(name="Normal", description="", subtype="XYZ", size=3, update=MxNode.update_prop)
    nd_EDF_in_file: StringProperty(name="File", description="", subtype="FILE_PATH", default="", update=MxNode.update_prop)
    nd_EDF_out_out: StringProperty(name="Out", description="", update=MxNode.update_prop)


class MxNode_PBR_absorption_vdf(MxNode):
    _file_path = FILE_PATH
    _data_types = {'VDF': {'nd_name': 'ND_absorption_vdf', 'nd': None}}

    bl_label = 'Absorption vdf'
    bl_idname = 'usdhydra.MxNode_PBR_absorption_vdf'
    bl_description = "Constructs a VDF for pure light absorption."

    category = 'PBR'

    data_type: EnumProperty(name="Type", description="Input Data Type", items=[('VDF', 'VDF', 'VDF')], default='VDF', update=MxNode.update_data_type)

    nd_VDF_in_absorption: FloatVectorProperty(name="Absorption", description="", subtype="XYZ", size=3, default=(0.0, 0.0, 0.0), update=MxNode.update_prop)
    nd_VDF_out_out: StringProperty(name="Out", description="", update=MxNode.update_prop)


class MxNode_PBR_anisotropic_vdf(MxNode):
    _file_path = FILE_PATH
    _data_types = {'VDF': {'nd_name': 'ND_anisotropic_vdf', 'nd': None}}

    bl_label = 'Anisotropic vdf'
    bl_idname = 'usdhydra.MxNode_PBR_anisotropic_vdf'
    bl_description = "Constructs a VDF scattering light for a participating medium, based on the Henyey-Greenstein phase function."

    category = 'PBR'

    data_type: EnumProperty(name="Type", description="Input Data Type", items=[('VDF', 'VDF', 'VDF')], default='VDF', update=MxNode.update_data_type)

    nd_VDF_in_absorption: FloatVectorProperty(name="Absorption", description="", subtype="XYZ", size=3, default=(0.0, 0.0, 0.0), update=MxNode.update_prop)
    nd_VDF_in_scattering: FloatVectorProperty(name="Scattering", description="", subtype="XYZ", size=3, default=(0.0, 0.0, 0.0), update=MxNode.update_prop)
    nd_VDF_in_anisotropy: FloatProperty(name="Anisotropy", description="", default=0.0, update=MxNode.update_prop)
    nd_VDF_out_out: StringProperty(name="Out", description="", update=MxNode.update_prop)


class MxNode_PBR_surface(MxNode):
    _file_path = FILE_PATH
    _data_types = {'surfaceshader': {'nd_name': 'ND_surface', 'nd': None}}

    bl_label = 'Surface'
    bl_idname = 'usdhydra.MxNode_PBR_surface'
    bl_description = "A constructor node for the surfaceshader type."

    category = 'PBR'

    data_type: EnumProperty(name="Type", description="Input Data Type", items=[('surfaceshader', 'Surfaceshader', 'Surfaceshader')], default='surfaceshader', update=MxNode.update_data_type)

    nd_surfaceshader_in_bsdf: StringProperty(name="Bsdf", description="Distribution function for surface scattering.", default="", update=MxNode.update_prop)
    nd_surfaceshader_in_edf: StringProperty(name="Edf", description="Distribution function for surface emission.", default="", update=MxNode.update_prop)
    nd_surfaceshader_in_opacity: FloatProperty(name="Opacity", description="Surface cutout opacity", default=1.0, update=MxNode.update_prop)
    nd_surfaceshader_out_out: StringProperty(name="Out", description="", update=MxNode.update_prop)


class MxNode_PBR_thin_surface(MxNode):
    _file_path = FILE_PATH
    _data_types = {'surfaceshader': {'nd_name': 'ND_thin_surface', 'nd': None}}

    bl_label = 'Thin surface'
    bl_idname = 'usdhydra.MxNode_PBR_thin_surface'
    bl_description = "A constructor node for the surfaceshader type for non-closed 'thin' objects."

    category = 'PBR'

    data_type: EnumProperty(name="Type", description="Input Data Type", items=[('surfaceshader', 'Surfaceshader', 'Surfaceshader')], default='surfaceshader', update=MxNode.update_data_type)

    nd_surfaceshader_in_front_bsdf: StringProperty(name="Front bsdf", description="Distribution function for front-side surface scattering.", default="", update=MxNode.update_prop)
    nd_surfaceshader_in_front_edf: StringProperty(name="Front edf", description="Distribution function for front-side surface emission.", default="", update=MxNode.update_prop)
    nd_surfaceshader_in_back_bsdf: StringProperty(name="Back bsdf", description="Distribution function for back-side surface scattering.", default="", update=MxNode.update_prop)
    nd_surfaceshader_in_back_edf: StringProperty(name="Back edf", description="Distribution function for back-side surface emission.", default="", update=MxNode.update_prop)
    nd_surfaceshader_in_opacity: FloatProperty(name="Opacity", description="Surface cutout opacity", default=1.0, update=MxNode.update_prop)
    nd_surfaceshader_out_out: StringProperty(name="Out", description="", update=MxNode.update_prop)


class MxNode_PBR_volume(MxNode):
    _file_path = FILE_PATH
    _data_types = {'volumeshader': {'nd_name': 'ND_volume', 'nd': None}}

    bl_label = 'Volume'
    bl_idname = 'usdhydra.MxNode_PBR_volume'
    bl_description = "A constructor node for the volumeshader type."

    category = 'PBR'

    data_type: EnumProperty(name="Type", description="Input Data Type", items=[('volumeshader', 'Volumeshader', 'Volumeshader')], default='volumeshader', update=MxNode.update_data_type)

    nd_volumeshader_in_vdf: StringProperty(name="Vdf", description="Volume distribution function for the medium.", default="", update=MxNode.update_prop)
    nd_volumeshader_in_edf: StringProperty(name="Edf", description="Emission distribution function for the medium.", default="", update=MxNode.update_prop)
    nd_volumeshader_out_out: StringProperty(name="Out", description="", update=MxNode.update_prop)


class MxNode_PBR_light(MxNode):
    _file_path = FILE_PATH
    _data_types = {'lightshader': {'nd_name': 'ND_light', 'nd': None}}

    bl_label = 'Light'
    bl_idname = 'usdhydra.MxNode_PBR_light'
    bl_description = "A constructor node for the lightshader type."

    category = 'PBR'

    data_type: EnumProperty(name="Type", description="Input Data Type", items=[('lightshader', 'Lightshader', 'Lightshader')], default='lightshader', update=MxNode.update_data_type)

    nd_lightshader_in_edf: StringProperty(name="Edf", description="Distribution function for light emission.", default="", update=MxNode.update_prop)
    nd_lightshader_in_intensity: FloatProperty(name="Intensity", description="Multiplier for the light intensity", default=1.0, update=MxNode.update_prop)
    nd_lightshader_in_exposure: FloatProperty(name="Exposure", description="Exposure control for the light intensity", default=0.0, update=MxNode.update_prop)
    nd_lightshader_out_out: StringProperty(name="Out", description="", update=MxNode.update_prop)


class MxNode_PBR_displacement(MxNode):
    _file_path = FILE_PATH
    _data_types = {'float': {'nd_name': 'ND_displacement_float', 'nd': None}, 'vector3': {'nd_name': 'ND_displacement_vector3', 'nd': None}}

    bl_label = 'Displacement'
    bl_idname = 'usdhydra.MxNode_PBR_displacement'
    bl_description = "A constructor node for the displacementshader type."

    category = 'PBR'

    data_type: EnumProperty(name="Type", description="Input Data Type", items=[('float', 'Float', 'Float'), ('vector3', 'Vector3', 'Vector3')], default='float', update=MxNode.update_data_type)

    nd_float_in_displacement: FloatProperty(name="Displacement", description="Scalar displacement amount along the surface normal direction.", default=0.0, update=MxNode.update_prop)
    nd_float_in_scale: FloatProperty(name="Scale", description="Scale factor for the displacement vector", default=1.0, update=MxNode.update_prop)
    nd_float_out_out: StringProperty(name="Out", description="", update=MxNode.update_prop)

    nd_vector3_in_displacement: FloatVectorProperty(name="Displacement", description="Vector displacement in (dPdu, dPdv, N) tangent/normal space.", subtype="XYZ", size=3, default=(0.0, 0.0, 0.0), update=MxNode.update_prop)
    nd_vector3_in_scale: FloatProperty(name="Scale", description="Scale factor for the displacement vector", default=1.0, update=MxNode.update_prop)
    nd_vector3_out_out: StringProperty(name="Out", description="", update=MxNode.update_prop)


class MxNode_PBR_layer(MxNode):
    _file_path = FILE_PATH
    _data_types = {'bsdf': {'nd_name': 'ND_layer_bsdf', 'nd': None}, 'vdf': {'nd_name': 'ND_layer_vdf', 'nd': None}}

    bl_label = 'Layer'
    bl_idname = 'usdhydra.MxNode_PBR_layer'
    bl_description = "Layer two BSDF's with vertical layering."

    category = 'PBR'

    data_type: EnumProperty(name="Type", description="Input Data Type", items=[('bsdf', 'Bsdf', 'Bsdf'), ('vdf', 'Vdf', 'Vdf')], default='bsdf', update=MxNode.update_data_type)

    nd_bsdf_in_top: StringProperty(name="Top", description="", default="", update=MxNode.update_prop)
    nd_bsdf_in_base: StringProperty(name="Base", description="", default="", update=MxNode.update_prop)
    nd_bsdf_out_out: StringProperty(name="Out", description="", update=MxNode.update_prop)

    nd_vdf_in_top: StringProperty(name="Top", description="", default="", update=MxNode.update_prop)
    nd_vdf_in_base: StringProperty(name="Base", description="", default="", update=MxNode.update_prop)
    nd_vdf_out_out: StringProperty(name="Out", description="", update=MxNode.update_prop)


class MxNode_PBR_mix(MxNode):
    _file_path = FILE_PATH
    _data_types = {'bsdf': {'nd_name': 'ND_mix_bsdf', 'nd': None}, 'edf': {'nd_name': 'ND_mix_edf', 'nd': None}, 'vdf': {'nd_name': 'ND_mix_vdf', 'nd': None}}

    bl_label = 'Mix'
    bl_idname = 'usdhydra.MxNode_PBR_mix'
    bl_description = "Mix two BSDF's according to an input mix amount."

    category = 'PBR'

    data_type: EnumProperty(name="Type", description="Input Data Type", items=[('bsdf', 'Bsdf', 'Bsdf'), ('edf', 'Edf', 'Edf'), ('vdf', 'Vdf', 'Vdf')], default='bsdf', update=MxNode.update_data_type)

    nd_bsdf_in_fg: StringProperty(name="Fg", description="", default="", update=MxNode.update_prop)
    nd_bsdf_in_bg: StringProperty(name="Bg", description="", default="", update=MxNode.update_prop)
    nd_bsdf_in_mix: FloatProperty(name="Mix", description="Mixing weight, range [0, 1].", min=0.0, max=1.0, default=0.0, update=MxNode.update_prop)
    nd_bsdf_out_out: StringProperty(name="Out", description="", update=MxNode.update_prop)

    nd_edf_in_fg: StringProperty(name="Fg", description="", default="", update=MxNode.update_prop)
    nd_edf_in_bg: StringProperty(name="Bg", description="", default="", update=MxNode.update_prop)
    nd_edf_in_mix: FloatProperty(name="Mix", description="Mixing weight, range [0, 1].", min=0.0, max=1.0, default=0.0, update=MxNode.update_prop)
    nd_edf_out_out: StringProperty(name="Out", description="", update=MxNode.update_prop)

    nd_vdf_in_fg: StringProperty(name="Fg", description="", default="", update=MxNode.update_prop)
    nd_vdf_in_bg: StringProperty(name="Bg", description="", default="", update=MxNode.update_prop)
    nd_vdf_in_mix: FloatProperty(name="Mix", description="Mixing weight, range [0, 1].", min=0.0, max=1.0, default=0.0, update=MxNode.update_prop)
    nd_vdf_out_out: StringProperty(name="Out", description="", update=MxNode.update_prop)


class MxNode_PBR_add(MxNode):
    _file_path = FILE_PATH
    _data_types = {'bsdf': {'nd_name': 'ND_add_bsdf', 'nd': None}, 'edf': {'nd_name': 'ND_add_edf', 'nd': None}, 'vdf': {'nd_name': 'ND_add_vdf', 'nd': None}}

    bl_label = 'Add'
    bl_idname = 'usdhydra.MxNode_PBR_add'
    bl_description = "A node for additive blending of BSDF's."

    category = 'PBR'

    data_type: EnumProperty(name="Type", description="Input Data Type", items=[('bsdf', 'Bsdf', 'Bsdf'), ('edf', 'Edf', 'Edf'), ('vdf', 'Vdf', 'Vdf')], default='bsdf', update=MxNode.update_data_type)

    nd_bsdf_in_in1: StringProperty(name="In1", description="First BSDF.", default="", update=MxNode.update_prop)
    nd_bsdf_in_in2: StringProperty(name="In2", description="Second BSDF.", default="", update=MxNode.update_prop)
    nd_bsdf_out_out: StringProperty(name="Out", description="", update=MxNode.update_prop)

    nd_edf_in_in1: StringProperty(name="In1", description="First EDF.", default="", update=MxNode.update_prop)
    nd_edf_in_in2: StringProperty(name="In2", description="Second EDF.", default="", update=MxNode.update_prop)
    nd_edf_out_out: StringProperty(name="Out", description="", update=MxNode.update_prop)

    nd_vdf_in_in1: StringProperty(name="In1", description="First VDF.", default="", update=MxNode.update_prop)
    nd_vdf_in_in2: StringProperty(name="In2", description="Second VDF.", default="", update=MxNode.update_prop)
    nd_vdf_out_out: StringProperty(name="Out", description="", update=MxNode.update_prop)


class MxNode_PBR_multiply(MxNode):
    _file_path = FILE_PATH
    _data_types = {'bsdfC': {'nd_name': 'ND_multiply_bsdfC', 'nd': None}, 'bsdfF': {'nd_name': 'ND_multiply_bsdfF', 'nd': None}, 'edfC': {'nd_name': 'ND_multiply_edfC', 'nd': None}, 'edfF': {'nd_name': 'ND_multiply_edfF', 'nd': None}, 'vdfC': {'nd_name': 'ND_multiply_vdfC', 'nd': None}, 'vdfF': {'nd_name': 'ND_multiply_vdfF', 'nd': None}}

    bl_label = 'Multiply'
    bl_idname = 'usdhydra.MxNode_PBR_multiply'
    bl_description = "A node for adjusting the contribution of a BSDF with a weight."

    category = 'PBR'

    data_type: EnumProperty(name="Type", description="Input Data Type", items=[('bsdfC', 'BsdfC', 'BsdfC'), ('bsdfF', 'BsdfF', 'BsdfF'), ('edfC', 'EdfC', 'EdfC'), ('edfF', 'EdfF', 'EdfF'), ('vdfC', 'VdfC', 'VdfC'), ('vdfF', 'VdfF', 'VdfF')], default='bsdfC', update=MxNode.update_data_type)

    nd_bsdfC_in_in1: StringProperty(name="In1", description="The BSDF to scale.", default="", update=MxNode.update_prop)
    nd_bsdfC_in_in2: FloatVectorProperty(name="In2", description="Scaling weight.", subtype="COLOR", size=3, soft_min=0.0, soft_max=1.0, default=(1.0, 1.0, 1.0), update=MxNode.update_prop)
    nd_bsdfC_out_out: StringProperty(name="Out", description="", update=MxNode.update_prop)

    nd_bsdfF_in_in1: StringProperty(name="In1", description="The BSDF to scale.", default="", update=MxNode.update_prop)
    nd_bsdfF_in_in2: FloatProperty(name="In2", description="Scaling weight.", default=1.0, update=MxNode.update_prop)
    nd_bsdfF_out_out: StringProperty(name="Out", description="", update=MxNode.update_prop)

    nd_edfC_in_in1: StringProperty(name="In1", description="The EDF to scale.", default="", update=MxNode.update_prop)
    nd_edfC_in_in2: FloatVectorProperty(name="In2", description="Scaling weight.", subtype="COLOR", size=3, soft_min=0.0, soft_max=1.0, default=(1.0, 1.0, 1.0), update=MxNode.update_prop)
    nd_edfC_out_out: StringProperty(name="Out", description="", update=MxNode.update_prop)

    nd_edfF_in_in1: StringProperty(name="In1", description="The EDF to scale.", default="", update=MxNode.update_prop)
    nd_edfF_in_in2: FloatProperty(name="In2", description="Scaling weight.", default=1.0, update=MxNode.update_prop)
    nd_edfF_out_out: StringProperty(name="Out", description="", update=MxNode.update_prop)

    nd_vdfC_in_in1: StringProperty(name="In1", description="The VDF to scale.", default="", update=MxNode.update_prop)
    nd_vdfC_in_in2: FloatVectorProperty(name="In2", description="Scaling weight.", subtype="COLOR", size=3, soft_min=0.0, soft_max=1.0, default=(1.0, 1.0, 1.0), update=MxNode.update_prop)
    nd_vdfC_out_out: StringProperty(name="Out", description="", update=MxNode.update_prop)

    nd_vdfF_in_in1: StringProperty(name="In1", description="The VDF to scale.", default="", update=MxNode.update_prop)
    nd_vdfF_in_in2: FloatProperty(name="In2", description="Scaling weight.", default=1.0, update=MxNode.update_prop)
    nd_vdfF_out_out: StringProperty(name="Out", description="", update=MxNode.update_prop)


class MxNode_PBR_roughness_anisotropy(MxNode):
    _file_path = FILE_PATH
    _data_types = {'vector2': {'nd_name': 'ND_roughness_anisotropy', 'nd': None}}

    bl_label = 'Roughness anisotropy'
    bl_idname = 'usdhydra.MxNode_PBR_roughness_anisotropy'
    bl_description = "Calculates anisotropic surface roughness from a scalar roughness/anisotropy parameterization."

    category = 'PBR'

    data_type: EnumProperty(name="Type", description="Input Data Type", items=[('vector2', 'Vector2', 'Vector2')], default='vector2', update=MxNode.update_data_type)

    nd_vector2_in_roughness: FloatProperty(name="Roughness", description="", default=0.0, update=MxNode.update_prop)
    nd_vector2_in_anisotropy: FloatProperty(name="Anisotropy", description="", default=0.0, update=MxNode.update_prop)
    nd_vector2_out_out: FloatVectorProperty(name="Out", description="", subtype="NONE", size=2, update=MxNode.update_prop)


class MxNode_PBR_roughness_dual(MxNode):
    _file_path = FILE_PATH
    _data_types = {'vector2': {'nd_name': 'ND_roughness_dual', 'nd': None}}

    bl_label = 'Roughness dual'
    bl_idname = 'usdhydra.MxNode_PBR_roughness_dual'
    bl_description = "Calculates anisotropic surface roughness from a dual surface roughness parameterization."

    category = 'PBR'

    data_type: EnumProperty(name="Type", description="Input Data Type", items=[('vector2', 'Vector2', 'Vector2')], default='vector2', update=MxNode.update_data_type)

    nd_vector2_in_roughness: FloatVectorProperty(name="Roughness", description="", subtype="NONE", size=2, default=(0.0, 0.0), update=MxNode.update_prop)
    nd_vector2_out_out: FloatVectorProperty(name="Out", description="", subtype="NONE", size=2, update=MxNode.update_prop)


class MxNode_PBR_glossiness_anisotropy(MxNode):
    _file_path = FILE_PATH
    _data_types = {'vector2': {'nd_name': 'ND_glossiness_anisotropy', 'nd': None}}

    bl_label = 'Glossiness anisotropy'
    bl_idname = 'usdhydra.MxNode_PBR_glossiness_anisotropy'
    bl_description = "Calculates anisotropic surface roughness from a scalar glossiness/anisotropy parameterization."

    category = 'PBR'

    data_type: EnumProperty(name="Type", description="Input Data Type", items=[('vector2', 'Vector2', 'Vector2')], default='vector2', update=MxNode.update_data_type)

    nd_vector2_in_glossiness: FloatProperty(name="Glossiness", description="", min=0.0, max=1.0, default=1.0, update=MxNode.update_prop)
    nd_vector2_in_anisotropy: FloatProperty(name="Anisotropy", description="", min=0.0, max=1.0, default=0.0, update=MxNode.update_prop)
    nd_vector2_out_out: FloatVectorProperty(name="Out", description="", subtype="NONE", size=2, update=MxNode.update_prop)


class MxNode_PBR_blackbody(MxNode):
    _file_path = FILE_PATH
    _data_types = {'color3': {'nd_name': 'ND_blackbody', 'nd': None}}

    bl_label = 'Blackbody'
    bl_idname = 'usdhydra.MxNode_PBR_blackbody'
    bl_description = "Returns the radiant emittance of a blackbody radiator with the given temperature."

    category = 'PBR'

    data_type: EnumProperty(name="Type", description="Input Data Type", items=[('color3', 'Color3', 'Color3')], default='color3', update=MxNode.update_data_type)

    nd_color3_in_temperature: FloatProperty(name="Temperature", description="", default=5000.0, update=MxNode.update_prop)
    nd_color3_out_out: FloatVectorProperty(name="Out", description="", subtype="COLOR", size=3, soft_min=0.0, soft_max=1.0, update=MxNode.update_prop)


class MxNode_PBR_artistic_ior(MxNode):
    _file_path = FILE_PATH
    _data_types = {'color3': {'nd_name': 'ND_artistic_ior', 'nd': None}}

    bl_label = 'Artistic ior'
    bl_idname = 'usdhydra.MxNode_PBR_artistic_ior'
    bl_description = "Converts the artistic parameterization reflectivity and edge_color to  complex IOR values."

    category = 'PBR'

    data_type: EnumProperty(name="Type", description="Input Data Type", items=[('color3', 'Color3', 'Color3')], default='color3', update=MxNode.update_data_type)

    nd_color3_in_reflectivity: FloatVectorProperty(name="Reflectivity", description="", subtype="COLOR", size=3, soft_min=0.0, soft_max=1.0, default=(0.944, 0.776, 0.373), update=MxNode.update_prop)
    nd_color3_in_edge_color: FloatVectorProperty(name="Edge color", description="", subtype="COLOR", size=3, soft_min=0.0, soft_max=1.0, default=(0.998, 0.981, 0.751), update=MxNode.update_prop)
    nd_color3_out_ior: FloatVectorProperty(name="Ior", description="", subtype="COLOR", size=3, soft_min=0.0, soft_max=1.0, update=MxNode.update_prop)
    nd_color3_out_extinction: FloatVectorProperty(name="Extinction", description="", subtype="COLOR", size=3, soft_min=0.0, soft_max=1.0, update=MxNode.update_prop)


mx_node_classes = [MxNode_PBR_oren_nayar_diffuse_bsdf, MxNode_PBR_burley_diffuse_bsdf, MxNode_PBR_translucent_bsdf, MxNode_PBR_dielectric_bsdf, MxNode_PBR_conductor_bsdf, MxNode_PBR_generalized_schlick_bsdf, MxNode_PBR_subsurface_bsdf, MxNode_PBR_sheen_bsdf, MxNode_PBR_thin_film_bsdf, MxNode_PBR_uniform_edf, MxNode_PBR_conical_edf, MxNode_PBR_measured_edf, MxNode_PBR_absorption_vdf, MxNode_PBR_anisotropic_vdf, MxNode_PBR_surface, MxNode_PBR_thin_surface, MxNode_PBR_volume, MxNode_PBR_light, MxNode_PBR_displacement, MxNode_PBR_layer, MxNode_PBR_mix, MxNode_PBR_add, MxNode_PBR_multiply, MxNode_PBR_roughness_anisotropy, MxNode_PBR_roughness_dual, MxNode_PBR_glossiness_anisotropy, MxNode_PBR_blackbody, MxNode_PBR_artistic_ior]
