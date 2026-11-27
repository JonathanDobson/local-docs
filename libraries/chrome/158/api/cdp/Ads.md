# Ads domain *(experimental)*

Copyright 2026 The Chromium Authors Use of this source code is governed by a BSD-style license that can be found in the LICENSE file. A domain for ad-related metrics and data.

Depends on: [Network](Network.md), [Page](Page.md), [Runtime](Runtime.md)

Methods are called as `Ads.<command>` and events arrive as `Ads.<event>`.

## Commands

### Ads.getAdMetrics

Retrieves ad metrics for the current page.

**Returns**

| Name | Type | Description |
|---|---|---|
| `metrics` | [AdMetrics](#type-admetrics) |  |

### Ads.getAdScripts

Retrieves ad scripts for the current page. To minimize payload size, this only returns the newly tracked ad scripts since the last call to getAdScripts (i.e., the delta).

**Returns**

| Name | Type | Description |
|---|---|---|
| `newScripts` | array of [AdScript](#type-adscript) |  |

## Types

<a id="type-adframedata"></a>
### Ads.AdFrameData

Type: object

Ad frame data.

**Properties**

| Name | Type | Description |
|---|---|---|
| `frameId` | [Page.FrameId](Page.md#type-frameid) | The DevTools frame token. |
| `initialOrigin` (optional) | string | The initial origin of the frame. To minimize the payload size, this is only sent once per frame. |
| `networkBytes` | number | The network bytes of the frame. |
| `cpuTime` | number | The CPU time of the frame, in milliseconds. |

<a id="type-admetrics"></a>
### Ads.AdMetrics

Type: object

Ad metrics for a page.

**Properties**

| Name | Type | Description |
|---|---|---|
| `viewportAdDensityByArea` | integer | The viewport ad density by area, represented as a percentage (an integer between 0 and 100). |
| `averageViewportAdDensityByArea` | number | The time-weighted average of the viewport ad density by area, measured across the duration of the page. |
| `viewportAdCount` | integer | The number of ads currently visible within the viewport. |
| `averageViewportAdCount` | number | The time-weighted average of the viewport ad count, measured across the duration of the page. |
| `totalAdCpuTime` | number | The total ad CPU usage, in milliseconds. |
| `totalAdNetworkBytes` | number | The total ad network bytes. |
| `updateAdFrames` | array of [AdFrameData](#type-adframedata) | The list of ad frames that have been updated since the last event. |
| `removeAdFrames` | array of [Page.FrameId](Page.md#type-frameid) | The list of ad frame IDs that have been removed since the last event. |

<a id="type-adscript"></a>
### Ads.AdScript

Type: object

An ad script. Note: when the script is a transitive ad script, we only fill in the immediate ancestor script in the provenance's adScriptAncestry field (as its first entry), rather than filling in the full ancestry. This saves work for the backend, and the frontend can reconstruct the full ancestry if necessary.

**Properties**

| Name | Type | Description |
|---|---|---|
| `scriptId` | [Runtime.ScriptId](Runtime.md#type-scriptid) | The script ID. |
| `provenance` | [Network.AdProvenance](Network.md#type-adprovenance) | The ad provenance. |

