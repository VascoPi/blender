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


FILE_PATH = r"libraries\bxdf\standard_surface.mtlx"


class MxNode_PBR_standard_surface(MxNode):
    _file_path = FILE_PATH
    _data_types = {'surfaceshader': {'nd_name': 'ND_standard_surface_surfaceshader', 'nd': None}}

    bl_label = 'Standard surface'
    bl_idname = 'usdhydra.MxNode_PBR_standard_surface'
    bl_description = "Autodesk standard surface shader"

    category = 'PBR'

    bl_width_default = 250

    _ui_folders = ('Base', 'Specular', 'Transmission', 'Subsurface', 'Sheen', 'Coat', 'Thin Film', 'Emission', 'Geometry')
    data_type: EnumProperty(name="Type", description="Input Data Type", items=[('surfaceshader', 'Surfaceshader', 'Surfaceshader')], default='surfaceshader', update=MxNode.update_data_type)

    f_base: BoolProperty(name="Base", description="Enable Base", default=True, update=MxNode.update_ui_folders)
    f_specular: BoolProperty(name="Specular", description="Enable Specular", default=False, update=MxNode.update_ui_folders)
    f_transmission: BoolProperty(name="Transmission", description="Enable Transmission", default=False, update=MxNode.update_ui_folders)
    f_subsurface: BoolProperty(name="Subsurface", description="Enable Subsurface", default=False, update=MxNode.update_ui_folders)
    f_sheen: BoolProperty(name="Sheen", description="Enable Sheen", default=False, update=MxNode.update_ui_folders)
    f_coat: BoolProperty(name="Coat", description="Enable Coat", default=False, update=MxNode.update_ui_folders)
    f_thin_film: BoolProperty(name="Thin Film", description="Enable Thin Film", default=False, update=MxNode.update_ui_folders)
    f_emission: BoolProperty(name="Emission", description="Enable Emission", default=False, update=MxNode.update_ui_folders)
    f_geometry: BoolProperty(name="Geometry", description="Enable Geometry", default=False, update=MxNode.update_ui_folders)

    nd_surfaceshader_in_base: FloatProperty(name="Base", description="Multiplier on the intensity of the diffuse reflection.", min=0.0, max=1.0, default=1.0, update=MxNode.update_prop)
    nd_surfaceshader_in_base_color: FloatVectorProperty(name="Base Color", description="Color of the diffuse reflection.", subtype="COLOR", size=3, soft_min=0.0, soft_max=1.0, min=0.0, max=1.0, default=(0.8, 0.8, 0.8), update=MxNode.update_prop)
    nd_surfaceshader_in_diffuse_roughness: FloatProperty(name="Diffuse Roughness", description="Roughness of the diffuse reflection. Higher values cause the surface to appear flatter and darker.", min=0.0, max=1.0, default=0.0, update=MxNode.update_prop)
    nd_surfaceshader_in_metalness: FloatProperty(name="Metalness", description="Specifies how metallic the material appears. At its maximum, the surface behaves like a metal, using fully specular reflection and complex fresnel.", min=0.0, max=1.0, default=0.0, update=MxNode.update_prop)
    nd_surfaceshader_in_specular: FloatProperty(name="Specular", description="Multiplier on the intensity of the specular reflection.", min=0.0, max=1.0, default=1.0, update=MxNode.update_prop)
    nd_surfaceshader_in_specular_color: FloatVectorProperty(name="Specular Color", description="Color tint on the specular reflection.", subtype="COLOR", size=3, soft_min=0.0, soft_max=1.0, min=0.0, max=1.0, default=(1.0, 1.0, 1.0), update=MxNode.update_prop)
    nd_surfaceshader_in_specular_roughness: FloatProperty(name="Specular Roughness", description="The roughness of the specular reflection. Lower numbers produce sharper reflections, higher numbers produce blurrier reflections.", min=0.0, max=1.0, default=0.2, update=MxNode.update_prop)
    nd_surfaceshader_in_specular_IOR: FloatProperty(name="Index of Refraction", description="Index of refraction for specular reflection.", min=0.0, soft_max=3.0, default=1.5, update=MxNode.update_prop)
    nd_surfaceshader_in_specular_anisotropy: FloatProperty(name="Specular Anisotropy", description="The directional bias of reflected and transmitted light resulting in materials appearing rougher or glossier in certain directions.", min=0.0, max=1.0, default=0.0, update=MxNode.update_prop)
    nd_surfaceshader_in_specular_rotation: FloatProperty(name="Specular Rotation", description="Rotation of the axis of specular anisotropy around the surface normal.", min=0.0, max=1.0, default=0.0, update=MxNode.update_prop)
    nd_surfaceshader_in_transmission: FloatProperty(name="Transmission", description="Transmission of light through the surface for materials such as glass or water. The greater the value the more transparent the material.", min=0.0, max=1.0, default=0.0, update=MxNode.update_prop)
    nd_surfaceshader_in_transmission_color: FloatVectorProperty(name="Transmission Color", description="Color tint on the transmitted light.", subtype="COLOR", size=3, soft_min=0.0, soft_max=1.0, min=0.0, max=1.0, default=(1.0, 1.0, 1.0), update=MxNode.update_prop)
    nd_surfaceshader_in_transmission_depth: FloatProperty(name="Transmission Depth", description="Specifies the distance light travels inside the material before its becomes exactly the transmission color according to Beer's law.", min=0.0, soft_max=100.0, default=0.0, update=MxNode.update_prop)
    nd_surfaceshader_in_transmission_scatter: FloatVectorProperty(name="Transmission Scatter", description="Scattering coefficient of the interior medium. Suitable for a large body of liquid or one that is fairly thick, such as an ocean, honey, ice, or frosted glass.", subtype="COLOR", size=3, soft_min=0.0, soft_max=1.0, min=0.0, max=1.0, default=(0.0, 0.0, 0.0), update=MxNode.update_prop)
    nd_surfaceshader_in_transmission_scatter_anisotropy: FloatProperty(name="Transmission Anisotropy", description="The amount of directional bias, or anisotropy, of the scattering.", min=0.0, max=1.0, default=0.0, update=MxNode.update_prop)
    nd_surfaceshader_in_transmission_dispersion: FloatProperty(name="Transmission Dispersion", description="Dispersion amount, describing how much the index of refraction varies across wavelengths.", min=0.0, soft_max=100.0, default=0.0, update=MxNode.update_prop)
    nd_surfaceshader_in_transmission_extra_roughness: FloatProperty(name="Transmission Roughness", description="Additional roughness on top of specular roughness. Positive values blur refractions more than reflections, and negative values blur refractions less.", min=-1.0, max=1.0, soft_min=0.0, default=0.0, update=MxNode.update_prop)
    nd_surfaceshader_in_subsurface: FloatProperty(name="Subsurface", description="The blend between diffuse reflection and subsurface scattering. A value of 1.0 indicates full subsurface scattering and a value 0 for diffuse reflection only.", min=0.0, max=1.0, default=0.0, update=MxNode.update_prop)
    nd_surfaceshader_in_subsurface_color: FloatVectorProperty(name="Subsurface Color", description="The color of the subsurface scattering effect.", subtype="COLOR", size=3, soft_min=0.0, soft_max=1.0, min=0.0, max=1.0, default=(1.0, 1.0, 1.0), update=MxNode.update_prop)
    nd_surfaceshader_in_subsurface_radius: FloatVectorProperty(name="Subsurface Radius", description="The mean free path. The distance which light can travel before being scattered inside the surface.", subtype="COLOR", size=3, soft_min=0.0, soft_max=1.0, min=0.0, max=1.0, default=(1.0, 1.0, 1.0), update=MxNode.update_prop)
    nd_surfaceshader_in_subsurface_scale: FloatProperty(name="Subsurface Scale", description="Scalar weight for the subsurface radius value.", min=0.0, soft_max=10.0, default=1.0, update=MxNode.update_prop)
    nd_surfaceshader_in_subsurface_anisotropy: FloatProperty(name="Subsurface Anisotropy", description="The direction of subsurface scattering. 0 scatters light evenly, positive values scatter forward and negative values scatter backward.", min=0.0, max=1.0, default=0.0, update=MxNode.update_prop)
    nd_surfaceshader_in_sheen: FloatProperty(name="Sheen", description="The weight of a sheen layer that can be used to approximate microfibers or fabrics such as velvet and satin.", min=0.0, max=1.0, default=0.0, update=MxNode.update_prop)
    nd_surfaceshader_in_sheen_color: FloatVectorProperty(name="Sheen Color", description="The color of the sheen layer.", subtype="COLOR", size=3, soft_min=0.0, soft_max=1.0, min=0.0, max=1.0, default=(1.0, 1.0, 1.0), update=MxNode.update_prop)
    nd_surfaceshader_in_sheen_roughness: FloatProperty(name="Sheen Roughness", description="The roughness of the sheen layer.", min=0.0, max=1.0, default=0.3, update=MxNode.update_prop)
    nd_surfaceshader_in_coat: FloatProperty(name="Coat", description="The weight of a reflective clear-coat layer on top of the material. Use for materials such as car paint or an oily layer.", min=0.0, max=1.0, default=0.0, update=MxNode.update_prop)
    nd_surfaceshader_in_coat_color: FloatVectorProperty(name="Coat Color", description="The color of the clear-coat layer's transparency.", subtype="COLOR", size=3, soft_min=0.0, soft_max=1.0, min=0.0, max=1.0, default=(1.0, 1.0, 1.0), update=MxNode.update_prop)
    nd_surfaceshader_in_coat_roughness: FloatProperty(name="Coat Roughness", description="The roughness of the clear-coat reflections. The lower the value, the sharper the reflection.", min=0.0, max=1.0, default=0.1, update=MxNode.update_prop)
    nd_surfaceshader_in_coat_anisotropy: FloatProperty(name="Coat Anisotropy", description="The amount of directional bias, or anisotropy, of the clear-coat layer.", min=0.0, max=1.0, default=0.0, update=MxNode.update_prop)
    nd_surfaceshader_in_coat_rotation: FloatProperty(name="Coat Rotation", description="The rotation of the anisotropic effect of the clear-coat layer.", min=0.0, max=1.0, default=0.0, update=MxNode.update_prop)
    nd_surfaceshader_in_coat_IOR: FloatProperty(name="Coat Index of Refraction", description="The index of refraction of the clear-coat layer.", min=0.0, soft_max=3.0, default=1.5, update=MxNode.update_prop)
    nd_surfaceshader_in_coat_normal: FloatVectorProperty(name="Coat normal", description="Input normal for clear-coat layer", subtype="XYZ", size=3, update=MxNode.update_prop)
    nd_surfaceshader_in_coat_affect_color: FloatProperty(name="Coat Affect Color", description="Controls the saturation of diffuse reflection and subsurface scattering below the clear-coat.", min=0.0, max=1.0, default=0.0, update=MxNode.update_prop)
    nd_surfaceshader_in_coat_affect_roughness: FloatProperty(name="Coat Affect Roughness", description="Controls the roughness of the specular reflection in the layers below the clear-coat.", min=0.0, max=1.0, default=0.0, update=MxNode.update_prop)
    nd_surfaceshader_in_thin_film_thickness: FloatProperty(name="Thin Film Thickness", description="The thickness of the thin film layer on a surface. Use for materials such as multitone car paint or soap bubbles.", min=0.0, soft_max=2000.0, default=0.0, update=MxNode.update_prop)
    nd_surfaceshader_in_thin_film_IOR: FloatProperty(name="Thin Film Index of Refraction", description="The index of refraction of the medium surrounding the material.", min=0.0, soft_max=3.0, default=1.5, update=MxNode.update_prop)
    nd_surfaceshader_in_emission: FloatProperty(name="Emission", description="The amount of emitted incandescent light.", min=0.0, soft_max=1.0, default=0.0, update=MxNode.update_prop)
    nd_surfaceshader_in_emission_color: FloatVectorProperty(name="Emission Color", description="The color of the emitted light.", subtype="COLOR", size=3, soft_min=0.0, soft_max=1.0, min=0.0, max=1.0, default=(1.0, 1.0, 1.0), update=MxNode.update_prop)
    nd_surfaceshader_in_opacity: FloatVectorProperty(name="Opacity", description="The opacity of the entire material.", subtype="COLOR", size=3, soft_min=0.0, soft_max=1.0, min=0.0, max=1.0, default=(1.0, 1.0, 1.0), update=MxNode.update_prop)
    nd_surfaceshader_in_thin_walled: BoolProperty(name="Thin Walled", description="If true the surface is double-sided and represents an infinitely thin shell. Suiteable for thin objects such as tree leafs or paper", default=False, update=MxNode.update_prop)
    nd_surfaceshader_in_normal: FloatVectorProperty(name="Normal", description="Input geometric normal", subtype="XYZ", size=3, update=MxNode.update_prop)
    nd_surfaceshader_in_tangent: FloatVectorProperty(name="Tangent Input", description="Input geometric tangent", subtype="XYZ", size=3, update=MxNode.update_prop)
    nd_surfaceshader_out_out: StringProperty(name="Out", description="", update=MxNode.update_prop)


mx_node_classes = [MxNode_PBR_standard_surface]
