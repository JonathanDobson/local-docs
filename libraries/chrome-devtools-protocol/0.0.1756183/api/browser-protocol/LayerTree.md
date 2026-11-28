# LayerTree domain

Chrome DevTools Protocol, browser protocol (tip-of-tree) (protocol 1.3).

**Experimental**

Depends on: [DOM](DOM.md)

9 methods, 2 events, 7 types.

## Methods

### LayerTree.compositingReasons

Provides the reasons why the given layer was composited.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `layerId` | [LayerTree.LayerId](#type-layerid) | The id of the layer for which we want to get the reasons it was composited. |

**Return object**

| Name | Type | Description |
|---|---|---|
| `compositingReasons` | array of string | A list of strings specifying reasons for the given layer to become composited. |
| `compositingReasonIds` | array of string | A list of strings specifying reason IDs for the given layer to become composited. |

### LayerTree.disable

Disables compositing tree inspection.

No parameters.

### LayerTree.enable

Enables compositing tree inspection.

No parameters.

### LayerTree.loadSnapshot

Returns the snapshot identifier.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `tiles` | array of [LayerTree.PictureTile](#type-picturetile) | An array of tiles composing the snapshot. |

**Return object**

| Name | Type | Description |
|---|---|---|
| `snapshotId` | [LayerTree.SnapshotId](#type-snapshotid) | The id of the snapshot. |

### LayerTree.makeSnapshot

Returns the layer snapshot identifier.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `layerId` | [LayerTree.LayerId](#type-layerid) | The id of the layer. |

**Return object**

| Name | Type | Description |
|---|---|---|
| `snapshotId` | [LayerTree.SnapshotId](#type-snapshotid) | The id of the layer snapshot. |

### LayerTree.profileSnapshot

**Parameters**

| Name | Type | Description |
|---|---|---|
| `snapshotId` | [LayerTree.SnapshotId](#type-snapshotid) | The id of the layer snapshot. |
| `minRepeatCount` (optional) | integer | The maximum number of times to replay the snapshot (1, if not specified). |
| `minDuration` (optional) | number | The minimum duration (in seconds) to replay the snapshot. |
| `clipRect` (optional) | [DOM.Rect](DOM.md#type-rect) | The clip rectangle to apply when replaying the snapshot. |

**Return object**

| Name | Type | Description |
|---|---|---|
| `timings` | array of [LayerTree.PaintProfile](#type-paintprofile) | The array of paint profiles, one per run. |

### LayerTree.releaseSnapshot

Releases layer snapshot captured by the back-end.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `snapshotId` | [LayerTree.SnapshotId](#type-snapshotid) | The id of the layer snapshot. |

### LayerTree.replaySnapshot

Replays the layer snapshot and returns the resulting bitmap.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `snapshotId` | [LayerTree.SnapshotId](#type-snapshotid) | The id of the layer snapshot. |
| `fromStep` (optional) | integer | The first step to replay from (replay from the very start if not specified). |
| `toStep` (optional) | integer | The last step to replay to (replay till the end if not specified). |
| `scale` (optional) | number | The scale to apply while replaying (defaults to 1). |

**Return object**

| Name | Type | Description |
|---|---|---|
| `dataURL` | string | A data: URL for resulting image. |

### LayerTree.snapshotCommandLog

Replays the layer snapshot and returns canvas log.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `snapshotId` | [LayerTree.SnapshotId](#type-snapshotid) | The id of the layer snapshot. |

**Return object**

| Name | Type | Description |
|---|---|---|
| `commandLog` | array of object | The array of canvas function calls. |

## Events

### LayerTree.layerPainted

**Event parameters**

| Name | Type | Description |
|---|---|---|
| `layerId` | [LayerTree.LayerId](#type-layerid) | The id of the painted layer. |
| `clip` | [DOM.Rect](DOM.md#type-rect) | Clip rectangle. |

### LayerTree.layerTreeDidChange

**Event parameters**

| Name | Type | Description |
|---|---|---|
| `layers` (optional) | array of [LayerTree.Layer](#type-layer) | Layer tree, absent if not in the compositing mode. |

## Types

<a id="type-layerid"></a>
### LayerTree.LayerId

Unique Layer identifier.

Type: string

<a id="type-snapshotid"></a>
### LayerTree.SnapshotId

Unique snapshot identifier.

Type: string

<a id="type-scrollrect"></a>
### LayerTree.ScrollRect

Rectangle where scrolling happens on the main thread.

Type: object

**Properties**

| Name | Type | Description |
|---|---|---|
| `rect` | [DOM.Rect](DOM.md#type-rect) | Rectangle itself. |
| `type` | string | Reason for rectangle to force scrolling on the main thread Allowed values: `RepaintsOnScroll`, `TouchEventHandler`, `WheelEventHandler` |

<a id="type-stickypositionconstraint"></a>
### LayerTree.StickyPositionConstraint

Sticky position constraints.

Type: object

**Properties**

| Name | Type | Description |
|---|---|---|
| `stickyBoxRect` | [DOM.Rect](DOM.md#type-rect) | Layout rectangle of the sticky element before being shifted |
| `containingBlockRect` | [DOM.Rect](DOM.md#type-rect) | Layout rectangle of the containing block of the sticky element |
| `nearestLayerShiftingStickyBox` (optional) | [LayerTree.LayerId](#type-layerid) | The nearest sticky layer that shifts the sticky box |
| `nearestLayerShiftingContainingBlock` (optional) | [LayerTree.LayerId](#type-layerid) | The nearest sticky layer that shifts the containing block |

<a id="type-picturetile"></a>
### LayerTree.PictureTile

Serialized fragment of layer picture along with its offset within the layer.

Type: object

**Properties**

| Name | Type | Description |
|---|---|---|
| `x` | number | Offset from owning layer left boundary |
| `y` | number | Offset from owning layer top boundary |
| `picture` | string | Base64-encoded snapshot data. (Encoded as a base64 string when passed over JSON) |

<a id="type-layer"></a>
### LayerTree.Layer

Information about a compositing layer.

Type: object

**Properties**

| Name | Type | Description |
|---|---|---|
| `layerId` | [LayerTree.LayerId](#type-layerid) | The unique id for this layer. |
| `parentLayerId` (optional) | [LayerTree.LayerId](#type-layerid) | The id of parent (not present for root). |
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
| `scrollRects` (optional) | array of [LayerTree.ScrollRect](#type-scrollrect) | Rectangles scrolling on main thread only. |
| `stickyPositionConstraint` (optional) | [LayerTree.StickyPositionConstraint](#type-stickypositionconstraint) | Sticky position constraint information |

<a id="type-paintprofile"></a>
### LayerTree.PaintProfile

Array of timings, one per paint step.

Type: array of number
