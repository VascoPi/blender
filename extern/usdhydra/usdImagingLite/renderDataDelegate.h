/* SPDX-License-Identifier: Apache-2.0
 * Copyright 2011-2022 Blender Foundation */

#pragma once

#include <pxr/pxr.h>
#include <pxr/imaging/hd/camera.h>
#include <pxr/imaging/hd/sceneDelegate.h>
#include <pxr/imaging/hd/renderIndex.h>
#include <pxr/usd/usd/stage.h>

using namespace pxr;

namespace usdhydra {

TF_DEFINE_PRIVATE_TOKENS(_tokens,
    (renderBufferDescriptor)
    (renderTags));

class HdRenderDataDelegate : public HdSceneDelegate {
public:
    HdRenderDataDelegate(HdRenderIndex* parentIndex, SdfPath const& delegateID);
    ~HdRenderDataDelegate() override = default;

    template <typename T>
    void SetParameter(SdfPath const& id, TfToken const& key, T const& value)
    {
        _valueCacheMap[id][key] = value;
    }

    template <typename T>
    T const& GetParameter(SdfPath const& id, TfToken const& key) const
    {
        VtValue vParams;
        ValueCache vCache;
        TF_VERIFY(
            TfMapLookup(_valueCacheMap, id, &vCache) &&
            TfMapLookup(vCache, key, &vParams) &&
            vParams.IsHolding<T>());
        return vParams.Get<T>();
    }

    bool HasParameter(SdfPath const& id, TfToken const& key) const;
    VtValue Get(SdfPath const& id, TfToken const& key) override;
    VtValue GetCameraParamValue(SdfPath const& id, TfToken const& key) override;
    VtValue GetLightParamValue(SdfPath const& id, TfToken const& paramName) override;
    HdRenderBufferDescriptor GetRenderBufferDescriptor(SdfPath const& id) override;
    TfTokenVector GetTaskRenderTags(SdfPath const& taskId) override;

private:
    typedef TfHashMap<TfToken, VtValue, TfToken::HashFunctor> ValueCache;
    typedef TfHashMap<SdfPath, ValueCache, SdfPath::Hash> ValueCacheMap;
    ValueCacheMap _valueCacheMap;
};

} // namespace usdhydra
