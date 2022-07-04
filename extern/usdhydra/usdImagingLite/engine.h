/* SPDX-License-Identifier: Apache-2.0
 * Copyright 2011-2022 Blender Foundation */

#pragma once

#include <pxr/pxr.h>
#include <pxr/usd/usd/stage.h>

#include <pxr/imaging/hd/engine.h>
#include <pxr/imaging/hd/rendererPlugin.h>
#include <pxr/imaging/hd/pluginRenderDelegateUniqueHandle.h>
#include <pxr/usdImaging/usdImaging/delegate.h>

#include "renderParams.h"
#include "renderDataDelegate.h"
#include "renderTask.h"

namespace usdhydra {

/// \class UsdImagingLiteEngine
///
/// The UsdImagingLiteEngine is entry point API for rendering USD scenes for delegates
/// which don't require to use OpenGL. This is more lightweight engine comparing to
/// UsdImagingGLEngine.
///
class UsdImagingLiteEngine
{
public:
    // ---------------------------------------------------------------------
    /// \name Construction
    /// @{
    // ---------------------------------------------------------------------
    UsdImagingLiteEngine();

    // Disallow copies
    UsdImagingLiteEngine(const UsdImagingLiteEngine&) = delete;
    UsdImagingLiteEngine& operator=(const UsdImagingLiteEngine&) = delete;

    ~UsdImagingLiteEngine();

    /// @}

    // ---------------------------------------------------------------------
    /// \name Rendering
    /// @{
    // ---------------------------------------------------------------------

    /// Entry point for kicking off a render
    void Render(UsdPrim root, const UsdImagingLiteRenderParams &params);

    /// Returns true if the resulting image is fully converged.
    /// (otherwise, caller may need to call Render() again to refine the result)
    bool IsConverged() const;

    bool SetRendererAov(TfToken const &id);

    bool GetRendererAov(TfToken const &id, void *buf);

    void ClearRendererAovs();
    /// @}

    /// Gets a renderer setting's current value.
    VtValue GetRendererSetting(TfToken const& id) const;

    /// Sets a renderer setting's value.
    void SetRendererSetting(TfToken const& id, VtValue const& value);

    // ---------------------------------------------------------------------
    /// \name Camera State
    /// @{
    // ---------------------------------------------------------------------

    /// Set the viewport to use for rendering as (x,y,w,h), where (x,y)
    /// represents the lower left corner of the viewport rectangle, and (w,h)
    /// is the width and height of the viewport in pixels.
    void SetRenderViewport(GfVec4d const& viewport);

    /// Free camera API
    /// Set camera framing state directly (without pointing to a camera on the 
    /// USD stage). The projection matrix is expected to be pre-adjusted for the
    /// window policy.
    void SetCameraState(const GfMatrix4d& viewMatrix, const GfMatrix4d& projectionMatrix);

    /// @}

    // ---------------------------------------------------------------------
    /// \name Renderer Plugin Management
    /// @{
    // ---------------------------------------------------------------------

    /// Return the vector of available render-graph delegate plugins.
    static TfTokenVector GetRendererPlugins();

    /// Return the user-friendly description of a renderer plugin.
    static std::string GetRendererDisplayName(TfToken const &id);

    /// Set the current render-graph delegate to \p id.
    /// the plugin will be loaded if it's not yet.
    bool SetRendererPlugin(TfToken const &id);

    /// @}

    // ---------------------------------------------------------------------
    /// \name Control of background rendering threads.
    /// @{
    // ---------------------------------------------------------------------

    /// Query the renderer as to whether it supports pausing and resuming.
    bool IsPauseRendererSupported() const;

    /// Pause the renderer.
    ///
    /// Returns \c true if successful.
    bool PauseRenderer();

    /// Resume the renderer.
    ///
    /// Returns \c true if successful.
    bool ResumeRenderer();

    /// Stop the renderer.
    ///
    /// Returns \c true if successful.
    bool StopRenderer();

    /// Restart the renderer.
    ///
    /// Returns \c true if successful.
    bool RestartRenderer();

    /// @}

    // ---------------------------------------------------------------------
    /// \name Render Statistics
    /// @{
    // ---------------------------------------------------------------------

    /// Returns render statistics.
    ///
    /// The contents of the dictionary will depend on the current render
    /// delegate.
    ///
    VtDictionary GetRenderStats() const;

    /// @}

private:
    std::unique_ptr<HdRenderIndex> _renderIndex;
    HdPluginRenderDelegateUniqueHandle _renderDelegate;
    std::unique_ptr<UsdImagingDelegate> _sceneDelegate;
    std::unique_ptr<HdRenderDataDelegate> _renderDataDelegate;
    std::unique_ptr<HdEngine> _engine;

    HdRenderPassAovBindingVector _aovBindings;
    HdRenderTaskParams _renderTaskParams;

    bool _isPopulated;
    HdRprimCollection _renderCollection;

    // This function disposes of: the render index, the render plugin,
    // the task controller, and the usd imaging delegate.
    void _DeleteHydraResources();

    SdfPath _GetRendererAovPath(TfToken const &aov) const;
};

} // namespace usdhydra
