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
#include "usd_writer_material.cc"


namespace usdtokens {
// Materials
static const pxr::TfToken color("color", pxr::TfToken::Immortal);
static const pxr::TfToken intensity("intensity", pxr::TfToken::Immortal);
static const pxr::TfToken transparency("inputs:transparency", pxr::TfToken::Immortal);
}  // namespace usdtokens


namespace blender::io::usd {

/* Map Blender socket names to USD Preview Surface InputSpec structs. */
using InputMap = std::map<std::string, InputSpec>;

template<typename T1, typename T2>
auto get_value(const void *value);

static InputMap &world_input_map();
static bNode *traverse_channel(bNodeSocket *input, short target_type);

template<typename T1, typename T2>
auto get_value(const void *value)
{
  const T1 *cast_value = static_cast<const T1 *>(value);
  return T2(cast_value->value);
}

void create_world(const pxr::UsdStageRefPtr stage, World *world)
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
//  pxr::UsdAttribute texattr = world_light.CreateTextureFileAttr();
//  texattr.ClearDefault();
//  texattr.Set("d:\\vasyl\\AMD\\Task_notes\\BLEN-43\\textures\\Untitled.hdr");

  const InputMap &input_map = world_input_map();

  LISTBASE_FOREACH (bNodeSocket *, sock, &node->inputs) {

    /* Check if this socket is mapped to a USD preview shader input. */
    printf("sock->name, %s, %s\n", node->name, sock->name);
    const InputMap::const_iterator it = input_map.find(sock->name);

    if (it == input_map.end()) {
      continue;
    }

    const InputSpec &input_spec = it->second;

    bNode *input_node;
    printf("Before Color, %s\n", sock->name);
    if (std::string(sock->name) == "Color"){
      world_light.CreateColorAttr().Set(get_value<bNodeSocketValueRGBA, pxr::GfVec3f>(sock->default_value));

      input_node = traverse_channel(sock, SH_NODE_TEX_IMAGE);
      if (!input_node){
        input_node = traverse_channel(sock, SH_NODE_TEX_ENVIRONMENT);
        }
      if (input_node) {
        printf("Color texture");
        /* Create connection. */
        //std::string imagePath = get_tex_image_asset_path(input_node, stage, export_params);
        std::string imagePath = "d:/vasyl/AMD/Task_notes/BLEN-64/Scenes/Inventor/Jet/_Jet Engine Model.usd_resources/SkyboxLibrary/Skyboxes/spiaggia_di_mondello_1k.hdr";
        //const char *imagePath = "d:/vasyl/AMD/Task_notes/BLEN-64/Scenes/Inventor/Jet/_Jet Engine Model.usd_resources/SkyboxLibrary/Skyboxes/spiaggia_di_mondello_1k.hdr";
        if (!imagePath.empty()) {
          world_light.OrientToStageUpAxis();
          pxr::UsdAttribute texattr = world_light.CreateTextureFileAttr(pxr::VtValue(pxr::SdfAssetPath(imagePath)));
          //texattr.ClearDefault();
          texattr.Set(pxr::VtValue(pxr::SdfAssetPath(imagePath)));
        }

        pxr::UsdGeomXformOp xOp = world_light.AddRotateXOp();
        pxr::UsdGeomXformOp yOp = world_light.AddRotateYOp();

        pxr::UsdVariantSet vset = world_prim.GetVariantSets().AddVariantSet(pxr::TfToken("delegate"));
        vset.AddVariant(pxr::TfToken("HdRprPlugin"));
        vset.SetVariantSelection(pxr::TfToken("HdRprPlugin"));
        {
        pxr::UsdEditContext ctx(vset.GetVariantEditContext());
        xOp.Set(180.0f);
        //yOp.Set(90.0f);
        }
        vset.ClearVariantSelection();
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
    else {
      world_light.CreateIntensityAttr().Set(get_value<bNodeSocketValueFloat, float>(sock->default_value));
    }

    world_light.GetPrim().CreateAttribute(usdtokens::transparency, pxr::SdfValueTypeNames->Float).Set(1.0f);
  }
}

/* Return USD Preview Surface input map singleton. */
static InputMap &world_input_map()
{
  static InputMap input_map = {
      {"Color", {usdtokens::color, pxr::SdfValueTypeNames->Float3, usdtokens::rgb, true}},
      {"Strength", {usdtokens::intensity, pxr::SdfValueTypeNames->Float, usdtokens::r, true}},

  };

  return input_map;
}

static bNode *find_background_node(World *world)
{
  LISTBASE_FOREACH (bNode *, node, &world->nodetree->nodes) {
    if (node->type == SH_NODE_BACKGROUND) {
      printf("Background node\n");
      return node;
    }
  }

  return nullptr;
}
}  // namespace blender::io::usd
