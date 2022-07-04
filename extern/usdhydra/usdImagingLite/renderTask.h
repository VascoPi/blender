/* SPDX-License-Identifier: Apache-2.0
 * Copyright 2011-2022 Blender Foundation */

#pragma once

#include <pxr/imaging/hd/task.h>
#include <pxr/imaging/hd/renderPass.h>
#include <pxr/imaging/hd/renderPassState.h>

using namespace pxr;

namespace usdhydra {

class HdRenderTask : public HdTask
{
public:
    HdRenderTask(HdSceneDelegate* delegate, SdfPath const& id);

    HdRenderTask() = delete;
    HdRenderTask(HdRenderTask const&) = delete;
    HdRenderTask &operator=(HdRenderTask const&) = delete;

    ~HdRenderTask() override;

    bool IsConverged() const;

    /// Sync the render pass resources
    void Sync(HdSceneDelegate* delegate,
              HdTaskContext* ctx,
              HdDirtyBits* dirtyBits) override;

    /// Prepare the tasks resources
    void Prepare(HdTaskContext* ctx,
                 HdRenderIndex* renderIndex) override;

    /// Execute render pass task
    void Execute(HdTaskContext* ctx) override;

    /// Collect Render Tags used by the task.
    TfTokenVector const& GetRenderTags() const override;

private:
    HdRenderPassSharedPtr _pass;
    HdRenderPassStateSharedPtr _passState;

    TfTokenVector _renderTags;
    GfVec4d _viewport;
    SdfPath _cameraId;
    HdRenderPassAovBindingVector _aovBindings;
};

struct HdRenderTaskParams
{
    // Should not be empty.
    HdRenderPassAovBindingVector aovBindings;

    SdfPath camera;
    GfVec4d viewport = GfVec4d(0.0);
};

// VtValue requirements
std::ostream& operator<<(std::ostream& out, const HdRenderTaskParams& pv);
bool operator==(const HdRenderTaskParams& lhs, const HdRenderTaskParams& rhs);
bool operator!=(const HdRenderTaskParams& lhs, const HdRenderTaskParams& rhs);

} // namespace usdhydra
