# Command-line switches: `media/capture/capture_switches`

Generated from `media/capture/capture_switches.h` and `media/capture/capture_switches.cc` in the Chromium source. Each switch is passed to the browser as `--name` or `--name=value`. The description is the source comment verbatim; *Condition* is the build/platform `#if` it is defined under.

3 switches.

## `--video-capture-use-gpu-memory-buffer`

- Constant: `kVideoCaptureUseGpuMemoryBuffer`

Enables GpuMemoryBuffer-based buffer pool.

## `--video-capture-use-virtual-devices-only`

- Constant: `kVideoCaptureUseVirtualDevicesOnly`

Makes the video capture service ignore devices from the wrapped factory and expose only registered virtual devices.

## `--disable-video-capture-use-gpu-memory-buffer`

- Constant: `kDisableVideoCaptureUseGpuMemoryBuffer`

This is for the same feature controlled by kVideoCaptureUseGpuMemoryBuffer. kVideoCaptureUseGpuMemoryBuffer is settled by chromeos overlays. This flag is necessary to overwrite the settings via chrome:// flag. The behavior of chrome://flag#zero-copy-video-capture is as follows; Default  : Respect chromeos overlays settings. Enabled  : Force to enable kVideoCaptureUseGpuMemoryBuffer. Disabled : Force to disable kVideoCaptureUseGpuMemoryBuffer.
