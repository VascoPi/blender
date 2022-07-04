/* SPDX-License-Identifier: Apache-2.0
 * Copyright 2011-2022 Blender Foundation */

#pragma once

#include <pxr/pxr.h>
#include <pxr/usd/usd/timeCode.h>
#include <pxr/base/gf/vec2i.h>
#include <pxr/base/gf/vec4d.h>
#include <pxr/base/gf/vec4f.h>
#include <pxr/base/gf/matrix4d.h>
#include <pxr/base/tf/token.h>

using namespace pxr;

namespace usdhydra {

/// \class UsdImagingLiteRenderParams
///
/// Used as an arguments class for various methods in UsdImagingLiteEngine.
///
class UsdImagingLiteRenderParams 
{
public:
    TfToken renderPluginId;
    UsdTimeCode frame;
    int samples;
    GfVec4f clearColor;
    TfToken colorCorrectionMode;
    GfVec2i renderResolution;
    GfMatrix4d viewMatrix;
    GfMatrix4d projMatrix;
    TfTokenVector aovs;
    std::vector<int64_t> aovBuffers;

    inline UsdImagingLiteRenderParams();

    inline bool operator==(const UsdImagingLiteRenderParams &other) const;

    inline bool operator!=(const UsdImagingLiteRenderParams &other) const {
        return !(*this == other);
    }
};

UsdImagingLiteRenderParams::UsdImagingLiteRenderParams()
    : renderPluginId("HdRprPlugin")
    , frame(UsdTimeCode::Default())
    , samples(64)
    , clearColor(0, 0, 0, 1)
    , renderResolution(100, 100)
{
}

bool UsdImagingLiteRenderParams::operator==(const UsdImagingLiteRenderParams &other) const {
    return renderPluginId == other.renderPluginId
        && frame == other.frame
        && clearColor == other.clearColor
        && colorCorrectionMode == other.colorCorrectionMode
        && renderResolution == other.renderResolution
        && viewMatrix == other.viewMatrix
        && projMatrix == other.projMatrix
        && aovs == other.aovs
        && aovBuffers == other.aovBuffers;
}

} // namespace usdhydra
