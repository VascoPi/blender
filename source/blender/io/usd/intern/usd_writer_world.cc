/* SPDX-License-Identifier: GPL-2.0-or-later
 * Copyright 2019 Blender Foundation. All rights reserved. */
#include "usd_writer_world.h"

#include <pxr/pxr.h>
#include <pxr/usd/usdLux/domeLight.h>
#include <pxr/usd/usdLux/shapingAPI.h>
#include <pxr/usd/usd/variantSets.h>
#include <pxr/usd/usd/editContext.h>
#include "BKE_node.h"
#include "DNA_world_types.h"
#include "usd_writer_material.h"
#include "usd_exporter_context.h"


namespace blender::io::usd {

template<typename T1, typename T2>
auto get_value(const void *value)
{
  const T1 *cast_value = static_cast<const T1 *>(value);
  return T2(cast_value->value);
}
void create_world(const pxr::UsdStageRefPtr stage, World *world, const char *render_delegate)
{
  if (!world) {
    return;
  }
  bNode *node = find_background_node(world);
  if (!node) {
    return;
  }
  pxr::UsdPrim world_prim = stage->DefinePrim(pxr::SdfPath("/World"));
  pxr::UsdLuxDomeLight world_light = pxr::UsdLuxDomeLight::Define(stage, world_prim.GetPath().AppendChild(pxr::TfToken(pxr::TfMakeValidIdentifier("World"))));
  USDExportParams export_params;
  export_params.export_textures = true;
  export_params.overwrite_textures = true;

  LISTBASE_FOREACH (bNodeSocket *, sock, &node->inputs) {

    bNode *input_node;
    if (std::string(sock->name) == "Color"){
      world_light.CreateColorAttr().Set(get_value<bNodeSocketValueRGBA, pxr::GfVec3f>(sock->default_value));

      input_node = blender::io::usd::traverse_channel(sock, SH_NODE_TEX_IMAGE);
      if (!input_node){
        input_node = blender::io::usd::traverse_channel(sock, SH_NODE_TEX_ENVIRONMENT);
        }
      if (input_node) {
        std::string imagePath = blender::io::usd::get_tex_image_asset_path(input_node, stage, export_params);
        if (export_params.export_textures) {
          blender::io::usd::export_texture(input_node, stage, export_params.overwrite_textures);
        }
//        std::string imagePath = "d:/vasyl/AMD/Task_notes/BLEN-64/Scenes/Inventor/Jet/_Jet Engine Model.usd_resources/SkyboxLibrary/Skyboxes/spiaggia_di_mondello_1k.hdr";
        if (!imagePath.empty()) {
          world_light.OrientToStageUpAxis();
          pxr::UsdAttribute texattr = world_light.CreateTextureFileAttr(pxr::VtValue(pxr::SdfAssetPath(imagePath)));
          //texattr.ClearDefault();
          texattr.Set(pxr::VtValue(pxr::SdfAssetPath(imagePath)));
        }

        pxr::UsdGeomXformOp xOp = world_light.AddRotateXOp();
        pxr::UsdGeomXformOp yOp = world_light.AddRotateYOp();

        if (strcmp(render_delegate, "HdStormRendererPlugin") == 0){
          yOp.Set(90.0f);
        }
        else if (strcmp(render_delegate, "HdRprPlugin") == 0){
          xOp.Set(180.0f);
          yOp.Set(-90.0f);
        }
//
//        pxr::UsdVariantSet vset = world_prim.GetVariantSets().AddVariantSet(pxr::TfToken("delegate"));
//        vset.AddVariant(pxr::TfToken("HdRprPlugin"));
//        vset.SetVariantSelection(pxr::TfToken("HdRprPlugin"));
//        {
//        pxr::UsdEditContext ctx(vset.GetVariantEditContext());
//        xOp.Set(180.0f);
//        yOp.Set(90.0f);
//        }
//        vset.ClearVariantSelection();
//        vset.AddVariant("HdStormRendererPlugin");
//        vset.SetVariantSelection("HdStormRendererPlugin");
//        {
//        pxr::UsdEditContext ctx(vset.GetVariantEditContext());
//        yOp.Set(-90.0f);
//        }
//        vset.ClearVariantSelection();

//        // set correct Dome light x rotation
//        usd_utils.add_delegate_variants(obj_prim, {
//          'RPR': lambda: xOp.Set(180.0f)
//        })
//
//        // set correct Dome light y rotation
//        usd_utils.add_delegate_variants(obj_prim, {
//          'GL': lambda: yOp.Set(90.0f),
//          'RPR': lambda: yOp.Set(-90.0f)
//        })
    }
    }
    else if (std::string(sock->name) == "Strength"){
      world_light.CreateIntensityAttr().Set(get_value<bNodeSocketValueFloat, float>(sock->default_value));
    }

    world_light.GetPrim().CreateAttribute(pxr::TfToken("inputs:transparency"), pxr::SdfValueTypeNames->Float).Set(1.0f);
  }
}
static bNode *find_background_node(World *world)
{
  LISTBASE_FOREACH (bNode *, node, &world->nodetree->nodes) {
    if (node->type == SH_NODE_BACKGROUND) {
      return node;
    }
  }
  return nullptr;
}
}  // namespace blender::io::usd
