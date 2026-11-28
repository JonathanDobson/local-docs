# Command-line switches: `components/viz/common/switches`

Generated from `components/viz/common/switches.h` and `components/viz/common/switches.cc` in the Chromium source. Each switch is passed to the browser as `--name` or `--name=value`. The description is the source comment verbatim; *Condition* is the build/platform `#if` it is defined under.

10 switches.

## `--deadline-to-synchronize-surfaces`

- Constant: `kDeadlineToSynchronizeSurfaces`

Keep list in alphabetical order. The default number of the BeginFrames to wait to activate a surface with dependencies.

## `--delegated-ink-renderer`

- Constant: `kDelegatedInkRenderer`

Force the use of a Delegated Ink renderer as specified by the command line argument, rather than using system details. Acceptable values are: skia, system, none. Default to skia.

## `--disable-adpf`

- Constant: `kDisableAdpf`

Disables reporting of frame timing via ADPF, even if supported on the device.

## `--disable-frame-rate-limit`

- Constant: `kDisableFrameRateLimit`

Disables begin frame limiting in both cc scheduler and display scheduler. Also implies --disable-gpu-vsync (see //ui/gl/gl_switches.h). TODO(ananta/jonross/sunnyps) http://crbug.com/346931323 We should remove or change this once VRR support is implemented for Windows and other platforms potentially.

## `--double-buffer-compositing`

- Constant: `kDoubleBufferCompositing`

Sets the number of max pending frames in the GL buffer queue to 1.

## `--enable-hardware-overlays`

- Constant: `kEnableHardwareOverlays`

Enable compositing individual elements via hardware overlays when permitted by device. Setting the flag to "single-fullscreen" will try to promote a single fullscreen overlay and use it as main framebuffer where possible.

## `--run-all-compositor-stages-before-draw`

- Constant: `kRunAllCompositorStagesBeforeDraw`

Effectively disables pipelining of compositor frame production stages by waiting for each stage to finish before completing a frame.

## `--show-aggregated-damage`

- Constant: `kShowAggregatedDamage`

Adds a DebugBorderDrawQuad to the top of the root RenderPass showing the damage rect after surface aggregation. Note that when enabled this feature sets the entire output rect as damaged after adding the quad to highlight the real damage rect, which could hide damage rect problems.

## `--tint-composited-content-modulate`

- Constant: `kTintCompositedContentModulate`

Modulates the debug compositor tint color so that damage and page flip updates are made clearly visible. This feature was useful in determining the root cause of https://b.corp.google.com/issues/183260320 . The tinting flag "tint-composited-content" must also be enabled for this flag to used.

## `--show-dc-layer-debug-borders`

- Constant: `kShowDCLayerDebugBorders`

kShowDCLayerDebugBorders shows the debug borders of the overlays and the damage rect after using overlays on Windows. Do not use kShowDCLayerDebugBorders and kShowAggregatedDamage together because kShowAggregatedDamage sets the entire frame as damaged and this causes incorrect damage rect borders after using overlays. Show debug borders for DC layers - red for overlays and blue for underlays. The debug borders are offset from the layer rect by a few pixels for clarity.
