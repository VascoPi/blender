/* SPDX-License-Identifier: Apache-2.0
 * Copyright 2011-2022 Blender Foundation */

#include <pxr/imaging/hd/camera.h>
#include <pxr/imaging/hd/renderIndex.h>
#include <pxr/imaging/hd/renderBuffer.h>
#include <pxr/imaging/hd/renderDelegate.h>

#include "renderTask.h"

namespace usdhydra {

HdRenderTask::HdRenderTask(HdSceneDelegate* delegate, SdfPath const& id)
    : HdTask(id)
{
}

HdRenderTask::~HdRenderTask()
{
}

bool HdRenderTask::IsConverged() const
{
    return _pass ? _pass->IsConverged() : true;
}

void HdRenderTask::Sync(HdSceneDelegate* delegate,
                        HdTaskContext* ctx,
                        HdDirtyBits* dirtyBits)
{
    auto renderIndex = &delegate->GetRenderIndex();

    if ((*dirtyBits) & HdChangeTracker::DirtyCollection) {
        VtValue val = delegate->Get(GetId(), HdTokens->collection);
        auto collection = val.Get<HdRprimCollection>();

        // Check for cases where the collection is empty (i.e. default
        // constructed).  To do this, the code looks at the root paths,
        // if it is empty, the collection doesn't refer to any prims at
        // all.
        if (collection.GetName().IsEmpty()) {
            _pass.reset();
        } else {
            if (!_pass) {
                auto renderDelegate = renderIndex->GetRenderDelegate();
                _pass = renderDelegate->CreateRenderPass(renderIndex, collection);
            } else {
                _pass->SetRprimCollection(collection);
            }
        }
    }

    if ((*dirtyBits) & HdChangeTracker::DirtyParams) {
        HdRenderTaskParams params;

        auto value = delegate->Get(GetId(), HdTokens->params);
        if (TF_VERIFY(value.IsHolding<HdRenderTaskParams>())) {
            params = value.UncheckedGet<HdRenderTaskParams>();
        }

        _aovBindings = params.aovBindings;
        _viewport = params.viewport;
        _cameraId = params.camera;
    }

    if ((*dirtyBits) & HdChangeTracker::DirtyRenderTags) {
        _renderTags = _GetTaskRenderTags(delegate);
    }

    if (_pass) {
        _pass->Sync();
    }

    *dirtyBits = HdChangeTracker::Clean;
}

void HdRenderTask::Prepare(HdTaskContext* ctx,
                           HdRenderIndex* renderIndex)
{
    if (!_passState) {
        _passState = renderIndex->GetRenderDelegate()->CreateRenderPassState();
    }

    // Prepare AOVS
    {
        // Walk the aov bindings, resolving the render index references as they're
        // encountered.
        for (size_t i = 0; i < _aovBindings.size(); ++i) {
            if (_aovBindings[i].renderBuffer == nullptr) {
                _aovBindings[i].renderBuffer = static_cast<HdRenderBuffer*>(renderIndex->GetBprim(HdPrimTypeTokens->renderBuffer, _aovBindings[i].renderBufferId));
            }
        }
        _passState->SetAovBindings(_aovBindings);

        // XXX Tasks that are not RenderTasks (OIT, ColorCorrection etc) also need
        // access to AOVs, but cannot access SetupTask or RenderPassState.
        //(*ctx)[HdxTokens->aovBindings] = VtValue(_aovBindings);
    }

    // Prepare Camera
    {
        auto camera = static_cast<const HdCamera*>(renderIndex->GetSprim(HdPrimTypeTokens->camera, _cameraId));
        TF_VERIFY(camera);
        _passState->SetCameraAndViewport(camera, _viewport);
    }

    _passState->Prepare(renderIndex->GetResourceRegistry());
}

void HdRenderTask::Execute(HdTaskContext* ctx)
{
    // Bind the render state and render geometry with the rendertags (if any)
    if (_pass) {
        _pass->Execute(_passState, GetRenderTags());
    }
}

TfTokenVector const& HdRenderTask::GetRenderTags() const
{
    return _renderTags;
}

// --------------------------------------------------------------------------- //
// VtValue Requirements
// --------------------------------------------------------------------------- //

std::ostream& operator<<(std::ostream& out, const HdRenderTaskParams& pv)
{
    out << "RenderTask Params:\n";
    out << "camera: " << pv.camera << '\n';
    out << "viewport: " << pv.viewport << '\n';
    out << "aovBindings: ";
    for (auto const& a : pv.aovBindings) {
        out << a << " ";
    }
    out << '\n';
    return out;
}

bool operator==(const HdRenderTaskParams& lhs, const HdRenderTaskParams& rhs)
{
    return lhs.aovBindings == rhs.aovBindings &&
           lhs.camera == rhs.camera &&
           lhs.viewport == rhs.viewport;
}

bool operator!=(const HdRenderTaskParams& lhs, const HdRenderTaskParams& rhs)
{
    return !(lhs == rhs);
}

} // namespace usdhydra
