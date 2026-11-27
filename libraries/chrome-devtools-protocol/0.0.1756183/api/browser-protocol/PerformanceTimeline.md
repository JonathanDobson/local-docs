# PerformanceTimeline domain

Chrome DevTools Protocol, browser protocol (tip-of-tree) (protocol 1.3).

**Experimental**

Reporting of performance timeline events, as specified in
https://w3c.github.io/performance-timeline/#dom-performanceobserver.

Depends on: [DOM](DOM.md), [Network](Network.md)

1 methods, 1 events, 4 types.

## Methods

### PerformanceTimeline.enable

Previously buffered events would be reported before method returns.
See also: timelineEventAdded

**Parameters**

| Name | Type | Description |
|---|---|---|
| `eventTypes` | array of string | The types of event to report, as specified in https://w3c.github.io/performance-timeline/#dom-performanceentry-entrytype The specified filter overrides any previous filters, passing empty filter disables recording. Note that not all types exposed to the web platform are currently supported. |

## Events

### PerformanceTimeline.timelineEventAdded

Sent when a performance timeline event is added. See reportPerformanceTimeline method.

**Event parameters**

| Name | Type | Description |
|---|---|---|
| `event` | [PerformanceTimeline.TimelineEvent](#type-timelineevent) |  |

## Types

<a id="type-largestcontentfulpaint"></a>
### PerformanceTimeline.LargestContentfulPaint

See https://github.com/WICG/LargestContentfulPaint and largest_contentful_paint.idl

Type: object

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

See https://wicg.github.io/layout-instability/#sec-layout-shift and layout_shift.idl

Type: object

**Properties**

| Name | Type | Description |
|---|---|---|
| `value` | number | Score increment produced by this event. |
| `hadRecentInput` | boolean |  |
| `lastInputTime` | [Network.TimeSinceEpoch](Network.md#type-timesinceepoch) |  |
| `sources` | array of [PerformanceTimeline.LayoutShiftAttribution](#type-layoutshiftattribution) |  |

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
| `lcpDetails` (optional) | [PerformanceTimeline.LargestContentfulPaint](#type-largestcontentfulpaint) |  |
| `layoutShiftDetails` (optional) | [PerformanceTimeline.LayoutShift](#type-layoutshift) |  |
