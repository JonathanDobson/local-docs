# SystemInfo domain *(experimental)*

Copyright 2017 The Chromium Authors Use of this source code is governed by a BSD-style license that can be found in the LICENSE file.  Contributing to Chrome DevTools Protocol: https://goo.gle/devtools-contribution-guide-cdp The SystemInfo domain defines methods and events for querying low-level system information.

Methods are called as `SystemInfo.<command>` and events arrive as `SystemInfo.<event>`.

## Commands

### SystemInfo.getInfo

Returns information about the system.

**Returns**

| Name | Type | Description |
|---|---|---|
| `gpu` | [GPUInfo](#type-gpuinfo) | Information about the GPUs on the system. |
| `modelName` | string | A platform-dependent description of the model of the machine. On Mac OS, this is, for example, 'MacBookPro'. Will be the empty string if not supported. |
| `modelVersion` | string | A platform-dependent description of the version of the machine. On Mac OS, this is, for example, '10.1'. Will be the empty string if not supported. |
| `commandLine` | string | The command line string used to launch the browser. Will be the empty string if not supported. |

### SystemInfo.getFeatureState

Returns information about the feature state.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `featureState` | string |  |

**Returns**

| Name | Type | Description |
|---|---|---|
| `featureEnabled` | boolean |  |

### SystemInfo.getProcessInfo

Returns information about all running processes.

**Returns**

| Name | Type | Description |
|---|---|---|
| `processInfo` | array of [ProcessInfo](#type-processinfo) | An array of process info blocks. |

## Types

<a id="type-gpudevice"></a>
### SystemInfo.GPUDevice

Type: object

Describes a single graphics processor (GPU).

**Properties**

| Name | Type | Description |
|---|---|---|
| `vendorId` | number | PCI ID of the GPU vendor, if available; 0 otherwise. |
| `deviceId` | number | PCI ID of the GPU device, if available; 0 otherwise. |
| `subSysId` (optional) | number | Sub sys ID of the GPU, only available on Windows. |
| `revision` (optional) | number | Revision of the GPU, only available on Windows. |
| `vendorString` | string | String description of the GPU vendor, if the PCI ID is not available. |
| `deviceString` | string | String description of the GPU device, if the PCI ID is not available. |
| `driverVendor` | string | String description of the GPU driver vendor. |
| `driverVersion` | string | String description of the GPU driver version. |

<a id="type-size"></a>
### SystemInfo.Size

Type: object

Describes the width and height dimensions of an entity.

**Properties**

| Name | Type | Description |
|---|---|---|
| `width` | integer | Width in pixels. |
| `height` | integer | Height in pixels. |

<a id="type-videodecodeacceleratorcapability"></a>
### SystemInfo.VideoDecodeAcceleratorCapability

Type: object

Describes a supported video decoding profile with its associated minimum and maximum resolutions.

**Properties**

| Name | Type | Description |
|---|---|---|
| `profile` | string | Video codec profile that is supported, e.g. VP9 Profile 2. |
| `maxResolution` | [Size](#type-size) | Maximum video dimensions in pixels supported for this \|profile\|. |
| `minResolution` | [Size](#type-size) | Minimum video dimensions in pixels supported for this \|profile\|. |

<a id="type-videoencodeacceleratorcapability"></a>
### SystemInfo.VideoEncodeAcceleratorCapability

Type: object

Describes a supported video encoding profile with its associated maximum resolution and maximum framerate.

**Properties**

| Name | Type | Description |
|---|---|---|
| `profile` | string | Video codec profile that is supported, e.g H264 Main. |
| `maxResolution` | [Size](#type-size) | Maximum video dimensions in pixels supported for this \|profile\|. |
| `maxFramerateNumerator` | integer | Maximum encoding framerate in frames per second supported for this \|profile\|, as fraction's numerator and denominator, e.g. 24/1 fps, 24000/1001 fps, etc. |
| `maxFramerateDenominator` | integer |  |

<a id="type-subsamplingformat"></a>
### SystemInfo.SubsamplingFormat

Type: string

YUV subsampling type of the pixels of a given image.

Allowed values: `yuv420`, `yuv422`, `yuv444`

<a id="type-imagetype"></a>
### SystemInfo.ImageType

Type: string

Image format of a given image.

Allowed values: `jpeg`, `webp`, `unknown`

<a id="type-gpuinfo"></a>
### SystemInfo.GPUInfo

Type: object

Provides information about the GPU(s) on the system.

**Properties**

| Name | Type | Description |
|---|---|---|
| `devices` | array of [GPUDevice](#type-gpudevice) | The graphics devices on the system. Element 0 is the primary GPU. |
| `auxAttributes` (optional) | object | An optional dictionary of additional GPU related attributes. |
| `featureStatus` (optional) | object | An optional dictionary of graphics features and their status. |
| `driverBugWorkarounds` | array of string | An optional array of GPU driver bug workarounds. |
| `videoDecoding` | array of [VideoDecodeAcceleratorCapability](#type-videodecodeacceleratorcapability) | Supported accelerated video decoding capabilities. |
| `videoEncoding` | array of [VideoEncodeAcceleratorCapability](#type-videoencodeacceleratorcapability) | Supported accelerated video encoding capabilities. |

<a id="type-processinfo"></a>
### SystemInfo.ProcessInfo

Type: object

Represents process info.

**Properties**

| Name | Type | Description |
|---|---|---|
| `type` | string | Specifies process type. |
| `id` | integer | Specifies process id. |
| `cpuTime` | number | Specifies cumulative CPU usage in seconds across all threads of the process since the process start. |

