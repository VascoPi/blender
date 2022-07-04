# SPDX-License-Identifier: Apache-2.0
# Copyright 2011-2022 Blender Foundation

# <pep8 compliant>

from . import USDHydra_Panel


#
# FINAL RENDER SETTINGS
#
class USDHYDRA_RENDER_PT_hdrpr_settings_final(USDHydra_Panel):
    bl_label = "RPR Settings"
    bl_parent_id = 'USDHYDRA_RENDER_PT_render_settings_final'

    @classmethod
    def poll(cls, context):
        return super().poll(context) and context.scene.usdhydra.final.delegate == 'HdRprPlugin'

    def draw(self, context):
        hdrpr = context.scene.usdhydra.final.hdrpr

        layout = self.layout
        layout.use_property_split = True
        layout.use_property_decorate = False

        col = layout.column()
        # col.prop(hdrpr, "device")
        col.prop(hdrpr, "render_quality")
        col.prop(hdrpr, "render_mode")


class USDHYDRA_RENDER_PT_hdrpr_settings_samples_final(USDHydra_Panel):
    bl_label = "Samples"
    bl_parent_id = 'USDHYDRA_RENDER_PT_hdrpr_settings_final'
    bl_options = {'DEFAULT_CLOSED'}

    def draw(self, context):
        hdrpr = context.scene.usdhydra.final.hdrpr

        layout = self.layout
        layout.use_property_split = True
        layout.use_property_decorate = False

        layout.prop(hdrpr, "max_samples")

        col = layout.column(align=True)
        col.prop(hdrpr, "variance_threshold")
        row = col.row()
        row.enabled = hdrpr.variance_threshold > 0.0
        row.prop(hdrpr, "min_adaptive_samples")


class USDHYDRA_RENDER_PT_hdrpr_settings_quality_final(USDHydra_Panel):
    bl_label = "Quality"
    bl_parent_id = 'USDHYDRA_RENDER_PT_hdrpr_settings_final'
    bl_space_type = 'PROPERTIES'
    bl_options = {'DEFAULT_CLOSED'}

    def draw(self, context):
        hdrpr = context.scene.usdhydra.final.hdrpr
        quality = hdrpr.quality

        layout = self.layout
        layout.use_property_split = True
        layout.use_property_decorate = False

        col = layout.column(align=True)
        col.prop(quality, "max_ray_depth")
        col.prop(quality, "max_ray_depth_diffuse")
        col.prop(quality, "max_ray_depth_glossy")
        col.prop(quality, "max_ray_depth_refraction")
        col.prop(quality, "max_ray_depth_glossy_refraction")

        layout.prop(quality, "raycast_epsilon")
        layout.prop(quality, "radiance_clamping")


class USDHYDRA_RENDER_PT_hdrpr_settings_denoise_final(USDHydra_Panel):
    bl_label = ""
    bl_parent_id = 'USDHYDRA_RENDER_PT_hdrpr_settings_final'
    bl_options = {'DEFAULT_CLOSED'}

    def draw_header(self, context):
        denoise = context.scene.usdhydra.final.hdrpr.denoise
        self.layout.prop(denoise, "enable")

    def draw(self, context):
        denoise = context.scene.usdhydra.final.hdrpr.denoise

        layout = self.layout
        layout.use_property_split = True
        layout.use_property_decorate = False

        layout.enabled = denoise.enable
        layout.prop(denoise, "min_iter")
        layout.prop(denoise, "iter_step")


class USDHYDRA_RENDER_PT_hdrpr_settings_film_final(USDHydra_Panel):
    bl_label = "Film"
    bl_parent_id = 'USDHYDRA_RENDER_PT_hdrpr_settings_final'
    bl_options = {'DEFAULT_CLOSED'}

    def draw(self, context):
        layout = self.layout
        layout.use_property_split = True
        layout.use_property_decorate = False

        hdrpr = context.scene.usdhydra.final.hdrpr

        layout.prop(hdrpr, "enable_alpha", text="Transparent Background")


#
# VIEWPORT RENDER SETTINGS
#
class USDHYDRA_RENDER_PT_hdrpr_settings_viewport(USDHydra_Panel):
    bl_label = "RPR Settings"
    bl_parent_id = 'USDHYDRA_RENDER_PT_render_settings_viewport'

    @classmethod
    def poll(cls, context):
        return super().poll(context) and context.scene.usdhydra.viewport.delegate == 'HdRprPlugin'

    def draw(self, context):
        hdrpr = context.scene.usdhydra.viewport.hdrpr

        layout = self.layout
        layout.use_property_split = True
        layout.use_property_decorate = False

        layout = layout.column()
        # layout.prop(hdrpr, "device")
        layout.prop(hdrpr, "render_quality")
        layout.prop(hdrpr, "render_mode")


class USDHYDRA_RENDER_PT_hdrpr_settings_samples_viewport(USDHydra_Panel):
    bl_label = "Samples"
    bl_parent_id = 'USDHYDRA_RENDER_PT_hdrpr_settings_viewport'
    bl_options = {'DEFAULT_CLOSED'}

    def draw(self, context):
        hdrpr = context.scene.usdhydra.viewport.hdrpr

        layout = self.layout
        layout.use_property_split = True
        layout.use_property_decorate = False

        layout.prop(hdrpr, "max_samples")

        col = layout.column(align=True)
        col.prop(hdrpr, "variance_threshold")
        row = col.row()
        row.enabled = hdrpr.variance_threshold > 0.0
        row.prop(hdrpr, "min_adaptive_samples")


class USDHYDRA_RENDER_PT_hdrpr_settings_quality_viewport(USDHydra_Panel):
    bl_label = "Quality"
    bl_parent_id = 'USDHYDRA_RENDER_PT_hdrpr_settings_viewport'
    bl_space_type = 'PROPERTIES'
    bl_options = {'DEFAULT_CLOSED'}

    def draw(self, context):
        hdrpr = context.scene.usdhydra.viewport.hdrpr
        quality = hdrpr.interactive_quality

        layout = self.layout
        layout.use_property_split = True
        layout.use_property_decorate = False

        layout.prop(quality, "max_ray_depth")
        # layout.prop(quality, "enable_downscale")
        # layout.prop(quality, "resolution_downscale")


class USDHYDRA_RENDER_PT_hdrpr_settings_denoise_viewport(USDHydra_Panel):
    bl_label = ""
    bl_parent_id = 'USDHYDRA_RENDER_PT_hdrpr_settings_viewport'
    bl_options = {'DEFAULT_CLOSED'}

    def draw_header(self, context):
        denoise = context.scene.usdhydra.viewport.hdrpr.denoise
        self.layout.prop(denoise, "enable")

    def draw(self, context):
        denoise = context.scene.usdhydra.viewport.hdrpr.denoise

        layout = self.layout
        layout.use_property_split = True
        layout.use_property_decorate = False

        layout.enabled = denoise.enable
        layout.prop(denoise, "min_iter")
        layout.prop(denoise, "iter_step")
