# Command-line switches: `cc/base/switches`

Generated from `cc/base/switches.h` and `cc/base/switches.cc` in the Chromium source. Each switch is passed to the browser as `--name` or `--name=value`. The description is the source comment verbatim; *Condition* is the build/platform `#if` it is defined under.

33 switches.

## `--disable-threaded-animation`

- Constant: `kDisableThreadedAnimation`

Switches for the renderer compositor only.

## `--disable-composited-antialiasing`

- Constant: `kDisableCompositedAntialiasing`

Disables layer-edge anti-aliasing in the compositor.

## `--disable-main-frame-before-activation`

- Constant: `kDisableMainFrameBeforeActivation`

Disables sending the next BeginMainFrame before the previous commit activates. Overrides the kEnableMainFrameBeforeActivation flag.

## `--enable-main-frame-before-activation`

- Constant: `kEnableMainFrameBeforeActivation`

Enables sending the next BeginMainFrame before the previous commit activates.

## `--disable-checker-imaging`

- Constant: `kDisableCheckerImaging`

Disabled defering all image decodes to the image decode service, ignoring DecodingMode preferences specified on PaintImage.

## `--top-controls-hide-threshold`

- Constant: `kBrowserControlsHideThreshold`

Percentage of the browser controls need to be hidden before they will auto hide.

## `--top-controls-show-threshold`

- Constant: `kBrowserControlsShowThreshold`

Percentage of the browser controls need to be shown before they will auto show.

## `--slow-down-raster-scale-factor`

- Constant: `kSlowDownRasterScaleFactor`

Re-rasters everything multiple times to simulate a much slower machine. Give a scale factor to cause raster to take that many times longer to complete, such as --slow-down-raster-scale-factor=25.

## `--check-damage-early`

- Constant: `kCheckDamageEarly`

Checks damage early and aborts the frame if no damage, so that clients like Android WebView don't invalidate unnecessarily.

## `--enable-gpu-benchmarking`

- Constant: `kEnableGpuBenchmarking`

Switches for both the renderer and ui compositors. Enables the GPU benchmarking extension

## `--disable-layer-tree-host-memory-pressure`

- Constant: `kDisableLayerTreeHostMemoryPressure`

Switches for LayerTreeHost. Disables LayerTreeHost::OnMemoryPressure

## `--num-raster-threads`

- Constant: `kNumRasterThreads`

Switches for raster. Controls the number of threads to use for raster tasks.

## `--show-composited-layer-borders`

- Constant: `kShowCompositedLayerBorders`

Debug visualizations. Renders a border around compositor layers to help debug and study layer compositing.

## `--ui-show-composited-layer-borders`

- Constant: `kUIShowCompositedLayerBorders`

_No description in the source._

## `--show-fps-counter`

- Constant: `kShowFPSCounter`

Draws a heads-up-display showing Frames Per Second as well as GPU memory usage. If you also use --enable-logging=stderr --vmodule="head*=1" then FPS will also be output to the console log.

## `--ui-show-fps-counter`

- Constant: `kUIShowFPSCounter`

_No description in the source._

## `--show-layer-animation-bounds`

- Constant: `kShowLayerAnimationBounds`

Renders a border that represents the bounding box for the layer's animation.

## `--ui-show-layer-animation-bounds`

- Constant: `kUIShowLayerAnimationBounds`

_No description in the source._

## `--show-property-changed-rects`

- Constant: `kShowPropertyChangedRects`

Show rects in the HUD around layers whose properties have changed.

## `--ui-show-property-changed-rects`

- Constant: `kUIShowPropertyChangedRects`

_No description in the source._

## `--show-surface-damage-rects`

- Constant: `kShowSurfaceDamageRects`

Show rects in the HUD around damage as it is recorded into each render surface.

## `--ui-show-surface-damage-rects`

- Constant: `kUIShowSurfaceDamageRects`

_No description in the source._

## `--show-screenspace-rects`

- Constant: `kShowScreenSpaceRects`

Show rects in the HUD around the screen-space transformed bounds of every layer.

## `--ui-show-screenspace-rects`

- Constant: `kUIShowScreenSpaceRects`

_No description in the source._

## `--log-on-ui-double-background-blur`

- Constant: `kLogOnUIDoubleBackgroundBlur`
- Condition: `DCHECK_IS_ON()`

Checks and logs double background blur as an error if any.

## `--dump-compositor-frame`

- Constant: `kDumpCompositorFrame`

Debug data dump. Save CompositorFrame data in both renderer and gpu process for TreesInViz and TreeAnimationsInViz. This doesn't work without --no-sandbox. If no parameters are specified, by default, it records frame 1 - 10. If --dump-compositor-frame=begin,end is specified, it records frame [begin, end] inclusive.

## `--renderpass`

- Constant: `kCompositedRenderPassBorders`

Parameters for kUIShowCompositedLayerBorders.

## `--surface`

- Constant: `kCompositedSurfaceBorders`

_No description in the source._

## `--layer`

- Constant: `kCompositedLayerBorders`

_No description in the source._

## `--enable-scaling-clipped-images`

- Constant: `kEnableClippedImageScaling`

Allows scaling clipped images in GpuImageDecodeCache. Note that this may cause color-bleeding. TODO(crbug.com/40160880): Remove this workaround flag once the underlying cache problems are solved.

## `--cc-layer-tree-test-no-timeout`

- Constant: `kCCLayerTreeTestNoTimeout`

Test related. Prevents the layer tree unit tests from timing out.

## `--cc-layer-tree-test-long-timeout`

- Constant: `kCCLayerTreeTestLongTimeout`

Increases timeout for memory checkers.

## `--cc-scroll-animation-duration-in-seconds`

- Constant: `kCCScrollAnimationDurationForTesting`

Controls the duration of the scroll animation curve.
