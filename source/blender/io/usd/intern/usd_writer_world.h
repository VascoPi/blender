/* SPDX-License-Identifier: GPL-2.0-or-later
 * Copyright 2019 Blender Foundation. All rights reserved. */
#pragma once

#include "usd_writer_abstract.h"
#include "DNA_world_types.h"
#include "BKE_node.h"

namespace blender::io::usd {

void create_world(const pxr::UsdStageRefPtr stage, World *world, const char *render_delegate);
static bNode *find_background_node(World *world);

}  // namespace blender::io::usd
