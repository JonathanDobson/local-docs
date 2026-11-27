# PerformanceTimeline domain *(experimental)*

Copyright 2017 The Chromium Authors Use of this source code is governed by a BSD-style license that can be found in the LICENSE file.  Contributing to Chrome DevTools Protocol: https://goo.gle/devtools-contribution-guide-cdp Reporting of performance timeline events, as specified in https://w3c.github.io/performance-timeline/#dom-performanceobserver.

Depends on: [DOM](DOM.md), [Network](Network.md)

Methods are called as `PerformanceTimeline.<command>` and events arrive as `PerformanceTimeline.<event>`.

## Commands

### PerformanceTimeline.enable

Previously buffered events would be reported before method returns. See also: timelineEventAdded

**Parameters**

| Name | Type | Description |
|---|---|---|
| `eventTypes` | array of string | The types of event to report, as specified in https://w3c.github.io/performance-timeline/#dom-performanceentry-entrytype The specified filter overrides any previous filters, passing empty filter disables recording. Note that not all types exposed to the web platform are currently supported. |

## Events

### PerformanceTimeline.timelineEventAdded

Sent when a performance timeline event is added. See reportPerformanceTimeline method.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `event` | [TimelineEvent](#type-timelineevent) |  |

## Types

<a id="type-largestcontentfulpaint"></a>
### PerformanceTimeline.LargestContentfulPaint

Type: object

See https://github.com/WICG/LargestContentfulPaint and largest_contentful_paint.idl

**Properties**

| Name | Type | Description |
|---|---|---|
| `renderTime` | [Network.TimeSinceEpoch](Network.md#type-timesinceepoch) |  |
| `loadTime` | [Network.TimeSinceEpoch](Network.md#type-timesinceepoch) |  |
| `size` | number | The number of pixels being painted. |
| `elementId` (optional) | string | The id attribute of the element, if available. |
| `url` (optional) | string | The URL of the image (may be trimmed). |
| `nodeId` (optional) | [DOM.BackendNodeId](DOM.md#type-backendnodeid) |  |

<a id="type-layoutshiftattribution"></a>
### PerformanceTimeline.LayoutShiftAttribution

Type: object

**Properties**

| Name | Type | Description |
|---|---|---|
| `previousRect` | [DOM.Rect](DOM.md#type-rect) |  |
| `currentRect` | [DOM.Rect](DOM.md#type-rect) |  |
| `nodeId` (optional) | [DOM.BackendNodeId](DOM.md#type-backendnodeid) |  |

<a id="type-layoutshift"></a>
### PerformanceTimeline.LayoutShift

Type: object

See https://wicg.github.io/layout-instability/#sec-layout-shift and layout_shift.idl

**Properties**

| Name | Type | Description |
|---|---|---|
| `value` | number | Score increment produced by this event. |
| `hadRecentInput` | boolean |  |
| `lastInputTime` | [Network.TimeSinceEpoch](Network.md#type-timesinceepoch) |  |
| `sources` | array of [LayoutShiftAttribution](#type-layoutshiftattribution) |  |

<a id="type-timelineevent"></a>
### PerformanceTimeline.TimelineEvent

Type: object

**Properties**

| Name | Type | Description |
|---|---|---|
| `frameId` | [Page.FrameId](Page.md#type-frameid) | Identifies the frame that this event is related to. Empty for non-frame targets. |
| `type` | string | The event type, as specified in https://w3c.github.io/performance-timeline/#dom-performanceentry-entrytype This determines which of the optional "details" fields is present. |
| `name` | string | Name may be empty depending on the type. |
| `time` | [Network.TimeSinceEpoch](Network.md#type-timesinceepoch) | Time in seconds since Epoch, monotonically increasing within document lifetime. |
| `duration` (optional) | number | Event duration, if applicable. |
| `lcpDetails` (optional) | [LargestContentfulPaint](#type-largestcontentfulpaint) |  |
| `layoutShiftDetails` (optional) | [LayoutShift](#type-layoutshift) |  |

