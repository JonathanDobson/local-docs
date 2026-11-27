# LayerTree domain *(experimental)*

Copyright 2017 The Chromium Authors Use of this source code is governed by a BSD-style license that can be found in the LICENSE file.  Contributing to Chrome DevTools Protocol: https://goo.gle/devtools-contribution-guide-cdp

Depends on: [DOM](DOM.md)

Methods are called as `LayerTree.<command>` and events arrive as `LayerTree.<event>`.

## Commands

### LayerTree.compositingReasons

Provides the reasons why the given layer was composited.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `layerId` | [LayerId](#type-layerid) | The id of the layer for which we want to get the reasons it was composited. |

**Returns**

| Name | Type | Description |
|---|---|---|
| `compositingReasons` | array of string | A list of strings specifying reasons for the given layer to become composited. |
| `compositingReasonIds` | array of string | A list of strings specifying reason IDs for the given layer to become composited. |

### LayerTree.disable

Disables compositing tree inspection.

### LayerTree.enable

Enables compositing tree inspection.

### LayerTree.loadSnapshot

Returns the snapshot identifier.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `tiles` | array of [PictureTile](#type-picturetile) | An array of tiles composing the snapshot. |

**Returns**

| Name | Type | Description |
|---|---|---|
| `snapshotId` | [SnapshotId](#type-snapshotid) | The id of the snapshot. |

### LayerTree.makeSnapshot

Returns the layer snapshot identifier.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `layerId` | [LayerId](#type-layerid) | The id of the layer. |

**Returns**

| Name | Type | Description |
|---|---|---|
| `snapshotId` | [SnapshotId](#type-snapshotid) | The id of the layer snapshot. |

### LayerTree.profileSnapshot

**Parameters**

| Name | Type | Description |
|---|---|---|
| `snapshotId` | [SnapshotId](#type-snapshotid) | The id of the layer snapshot. |
| `minRepeatCount` (optional) | integer | The maximum number of times to replay the snapshot (1, if not specified). |
| `minDuration` (optional) | number | The minimum duration (in seconds) to replay the snapshot. |
| `clipRect` (optional) | [DOM.Rect](DOM.md#type-rect) | The clip rectangle to apply when replaying the snapshot. |

**Returns**

| Name | Type | Description |
|---|---|---|
| `timings` | array of [PaintProfile](#type-paintprofile) | The array of paint profiles, one per run. |

### LayerTree.releaseSnapshot

Releases layer snapshot captured by the back-end.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `snapshotId` | [SnapshotId](#type-snapshotid) | The id of the layer snapshot. |

### LayerTree.replaySnapshot

Replays the layer snapshot and returns the resulting bitmap.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `snapshotId` | [SnapshotId](#type-snapshotid) | The id of the layer snapshot. |
| `fromStep` (optional) | integer | The first step to replay from (replay from the very start if not specified). |
| `toStep` (optional) | integer | The last step to replay to (replay till the end if not specified). |
| `scale` (optional) | number | The scale to apply while replaying (defaults to 1). |

**Returns**

| Name | Type | Description |
|---|---|---|
| `dataURL` | string | A data: URL for resulting image. |

### LayerTree.snapshotCommandLog

Replays the layer snapshot and returns canvas log.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `snapshotId` | [SnapshotId](#type-snapshotid) | The id of the layer snapshot. |

**Returns**

| Name | Type | Description |
|---|---|---|
| `commandLog` | array of object | The array of canvas function calls. |

## Events

### LayerTree.layerPainted

**Parameters**

| Name | Type | Description |
|---|---|---|
| `layerId` | [LayerId](#type-layerid) | The id of the painted layer. |
| `clip` | [DOM.Rect](DOM.md#type-rect) | Clip rectangle. |

### LayerTree.layerTreeDidChange

**Parameters**

| Name | Type | Description |
|---|---|---|
| `layers` (optional) | array of [Layer](#type-layer) | Layer tree, absent if not in the compositing mode. |

## Types

<a id="type-layerid"></a>
### LayerTree.LayerId

Type: string

Unique Layer identifier.

<a id="type-snapshotid"></a>
### LayerTree.SnapshotId

Type: string

Unique snapshot identifier.

<a id="type-scrollrect"></a>
### LayerTree.ScrollRect

Type: object

Rectangle where scrolling happens on the main thread.

**Properties**

| Name | Type | Description |
|---|---|---|
| `rect` | [DOM.Rect](DOM.md#type-rect) | Rectangle itself. |
| `type` | enum: `RepaintsOnScroll`, `TouchEventHandler`, `WheelEventHandler` | Reason for rectangle to force scrolling on the main thread |

<a id="type-stickypositionconstraint"></a>
### LayerTree.StickyPositionConstraint

Type: object

Sticky position constraints.

**Properties**

| Name | Type | Description |
|---|---|---|
| `stickyBoxRect` | [DOM.Rect](DOM.md#type-rect) | Layout rectangle of the sticky element before being shifted |
| `containingBlockRect` | [DOM.Rect](DOM.md#type-rect) | Layout rectangle of the containing block of the sticky element |
| `nearestLayerShiftingStickyBox` (optional) | [LayerId](#type-layerid) | The nearest sticky layer that shifts the sticky box |
| `nearestLayerShiftingContainingBlock` (optional) | [LayerId](#type-layerid) | The nearest sticky layer that shifts the containing block |

<a id="type-picturetile"></a>
### LayerTree.PictureTile

Type: object

Serialized fragment of layer picture along with its offset within the layer.

**Properties**

| Name | Type | Description |
|---|---|---|
| `x` | number | Offset from owning layer left boundary |
| `y` | number | Offset from owning layer top boundary |
| `picture` | binary | Base64-encoded snapshot data. |

<a id="type-layer"></a>
### LayerTree.Layer

Type: object

Information about a compositing layer.

**Properties**

| Name | Type | Description |
|---|---|---|
| `layerId` | [LayerId](#type-layerid) | The unique id for this layer. |
| `parentLayerId` (optional) | [LayerId](#type-layerid) | The id of parent (not present for root). |
| `backendNodeId` (optional) | [DOM.BackendNodeId](DOM.md#type-backendnodeid) | The backend id for the node associated with this layer. |
| `offsetX` | number | Offset from parent layer, X coordinate. |
| `offsetY` | number | Offset from parent layer, Y coordinate. |
| `width` | number | Layer width. |
| `height` | number | Layer height. |
| `transform` (optional) | array of number | Transformation matrix for layer, default is identity matrix |
| `anchorX` (optional) | number | Transform anchor point X, absent if no transform specified |
| `anchorY` (optional) | number | Transform anchor point Y, absent if no transform specified |
| `anchorZ` (optional) | number | Transform anchor point Z, absent if no transform specified |
| `paintCount` | integer | Indicates how many time this layer has painted. |
| `drawsContent` | boolean | Indicates whether this layer hosts any content, rather than being used for transform/scrolling purposes only. |
| `invisible` (optional) | boolean | Set if layer is not visible. |
| `scrollRects` (optional) | array of [ScrollRect](#type-scrollrect) | Rectangles scrolling on main thread only. |
| `stickyPositionConstraint` (optional) | [StickyPositionConstraint](#type-stickypositionconstraint) | Sticky position constraint information |

<a id="type-paintprofile"></a>
### LayerTree.PaintProfile

Type: array of number

Array of timings, one per paint step.

