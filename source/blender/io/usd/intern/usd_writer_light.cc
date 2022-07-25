/* SPDX-License-Identifier: GPL-2.0-or-later
 * Copyright 2019 Blender Foundation. All rights reserved. */
#include "usd_writer_light.h"
#include "usd_hierarchy_iterator.h"

#include <pxr/base/gf/math.h>
#include <pxr/usd/usdLux/diskLight.h>
#include <pxr/usd/usdLux/distantLight.h>
#include <pxr/usd/usdLux/rectLight.h>
#include <pxr/usd/usdLux/sphereLight.h>
#include <pxr/usd/usdLux/shapingAPI.h>

#include "BLI_assert.h"
#include "BLI_utildefines.h"

#include "DNA_light_types.h"
#include "DNA_object_types.h"

namespace blender::io::usd {

USDLightWriter::USDLightWriter(const USDExporterContext &ctx) : USDAbstractWriter(ctx)
{
}

bool USDLightWriter::is_supported(const HierarchyContext *context) const
{
  Light *light = static_cast<Light *>(context->object->data);
  return ELEM(light->type, LA_AREA, LA_LOCAL, LA_SUN, LA_SPOT);
}

void USDLightWriter::do_write(HierarchyContext &context)
{
  pxr::UsdStageRefPtr stage = usd_export_context_.stage;
  const pxr::SdfPath &usd_path = usd_export_context_.usd_path;
  pxr::UsdTimeCode timecode = get_export_time_code();

  Light *light = static_cast<Light *>(context.object->data);
#if PXR_VERSION >= 2111
  pxr::UsdLuxLightAPI usd_light_api;
#else
  pxr::UsdLuxLight usd_light_api;
#endif

  float usd_intensity = light->energy;

  switch (light->type) {
    case LA_AREA:
      switch (light->area_shape) {
        case LA_AREA_DISK: {
          pxr::UsdLuxDiskLight disk_light = pxr::UsdLuxDiskLight::Define(stage, usd_path);
          // light size is diameter
          disk_light.CreateRadiusAttr().Set(light->area_size / 2, timecode);

          // Coefficient approximated to follow Cycles results
          usd_intensity *= 30.0f;

#if PXR_VERSION >= 2111
          usd_light_api = disk_light.LightAPI();
#else
          usd_light_api = disk_light;
#endif
          break;
        }
        case LA_AREA_ELLIPSE: { /* An ellipse light will deteriorate into a disk light. */
          pxr::UsdLuxDiskLight disk_light = pxr::UsdLuxDiskLight::Define(stage, usd_path);
          // average of light size is diameter
          disk_light.CreateRadiusAttr().Set((light->area_size + light->area_sizey) / 4, timecode);

          // Coefficient approximated to follow Cycles results
          usd_intensity *= 30.0f;

#if PXR_VERSION >= 2111
          usd_light_api = disk_light.LightAPI();
#else
          usd_light_api = disk_light;
#endif
          break;
        }
        case LA_AREA_RECT: {
          pxr::UsdLuxRectLight rect_light = pxr::UsdLuxRectLight::Define(stage, usd_path);
          rect_light.CreateWidthAttr().Set(light->area_size, timecode);
          rect_light.CreateHeightAttr().Set(light->area_sizey, timecode);

          // Coefficient approximated to follow Cycles results
          usd_intensity *= 30.0f;

#if PXR_VERSION >= 2111
          usd_light_api = rect_light.LightAPI();
#else
          usd_light_api = rect_light;
#endif
          break;
        }
        case LA_AREA_SQUARE: {
          pxr::UsdLuxRectLight rect_light = pxr::UsdLuxRectLight::Define(stage, usd_path);
          rect_light.CreateWidthAttr().Set(light->area_size, timecode);
          rect_light.CreateHeightAttr().Set(light->area_size, timecode);

          // Coefficient approximated to follow Cycles results
          usd_intensity *= 30.0f;

#if PXR_VERSION >= 2111
          usd_light_api = rect_light.LightAPI();
#else
          usd_light_api = rect_light;
#endif
          break;
        }
      }
      break;
    case LA_LOCAL: {
      pxr::UsdLuxSphereLight sphere_light = pxr::UsdLuxSphereLight::Define(stage, usd_path);
      sphere_light.CreateRadiusAttr().Set(light->area_size, timecode);

      // Coefficient approximated to follow Cycles results
      usd_intensity *= 2.5f;

#if PXR_VERSION >= 2111
      usd_light_api = sphere_light.LightAPI();
#else
      usd_light_api = sphere_light;
#endif
      break;
    }
    case LA_SUN: {
      pxr::UsdLuxDistantLight distant_light = pxr::UsdLuxDistantLight::Define(stage, usd_path);
      distant_light.CreateAngleAttr().Set((float)pxr::GfRadiansToDegrees(light->sun_angle), timecode);

      // Coefficient approximated to follow Cycles results
      usd_intensity *= 35.0f;

#if PXR_VERSION >= 2111
      usd_light_api = distant_light.LightAPI();
#else
      usd_light_api = distant_light;
#endif
      break;
    }
    case LA_SPOT: {
      pxr::UsdLuxSphereLight spot_light = pxr::UsdLuxSphereLight::Define(stage, usd_path);
      pxr::UsdPrim spot_prim = stage->GetPrimAtPath(usd_path);

      spot_light.CreateTreatAsPointAttr(pxr::VtValue(true));

      float spot_size = (float)pxr::GfRadiansToDegrees(light->spotsize);

      pxr::UsdLuxShapingAPI usd_shaping_api = pxr::UsdLuxShapingAPI(spot_prim);
      usd_shaping_api.CreateShapingConeAngleAttr(pxr::VtValue(spot_size / 2));
      usd_shaping_api.CreateShapingConeSoftnessAttr(pxr::VtValue(light->spotblend));

      // Coefficient approximated to follow Cycles results
      usd_intensity /= 10.0f;

#if PXR_VERSION >= 2111
          usd_light_api = spot_light.LightAPI();
#else
          usd_light_api = spot_light;
#endif
      break;
    }
    default:
      BLI_assert_msg(0, "is_supported() returned true for unsupported light type");
  }

  usd_light_api.CreateIntensityAttr().Set(usd_intensity, timecode);

  usd_light_api.CreateColorAttr().Set(pxr::GfVec3f(light->r, light->g, light->b), timecode);
  usd_light_api.CreateSpecularAttr().Set(light->spec_fac, timecode);
}

}  // namespace blender::io::usd
