# Overlay domain *(experimental)*

Copyright 2017 The Chromium Authors Use of this source code is governed by a BSD-style license that can be found in the LICENSE file.  Contributing to Chrome DevTools Protocol: https://goo.gle/devtools-contribution-guide-cdp This domain provides various functionality related to drawing atop the inspected page.

Depends on: [DOM](DOM.md), [Page](Page.md), [Runtime](Runtime.md)

Methods are called as `Overlay.<command>` and events arrive as `Overlay.<event>`.

## Commands

### Overlay.disable

Disables domain notifications.

### Overlay.enable

Enables domain notifications.

### Overlay.getHighlightObjectForTest

For testing.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `nodeId` | [DOM.NodeId](DOM.md#type-nodeid) | Id of the node to get highlight object for. |
| `includeDistance` (optional) | boolean | Whether to include distance info. |
| `includeStyle` (optional) | boolean | Whether to include style info. |
| `colorFormat` (optional) | [ColorFormat](#type-colorformat) | The color format to get config with (default: hex). |
| `showAccessibilityInfo` (optional) | boolean | Whether to show accessibility info (default: true). |

**Returns**

| Name | Type | Description |
|---|---|---|
| `highlight` | object | Highlight data for the node. |

### Overlay.getGridHighlightObjectsForTest

For Persistent Grid testing.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `nodeIds` | array of [DOM.NodeId](DOM.md#type-nodeid) | Ids of the node to get highlight object for. |

**Returns**

| Name | Type | Description |
|---|---|---|
| `highlights` | object | Grid Highlight data for the node ids provided. |

### Overlay.getSourceOrderHighlightObjectForTest

For Source Order Viewer testing.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `nodeId` | [DOM.NodeId](DOM.md#type-nodeid) | Id of the node to highlight. |

**Returns**

| Name | Type | Description |
|---|---|---|
| `highlight` | object | Source order highlight data for the node id provided. |

### Overlay.hideHighlight

Hides any highlight.

### Overlay.highlightFrame *(deprecated)*

Highlights owner element of the frame with given id. Deprecated: Doesn't work reliably and cannot be fixed due to process separation (the owner node might be in a different process). Determine the owner node in the client and use highlightNode.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `frameId` | [Page.FrameId](Page.md#type-frameid) | Identifier of the frame to highlight. |
| `contentColor` (optional) | [DOM.RGBA](DOM.md#type-rgba) | The content box highlight fill color (default: transparent). |
| `contentOutlineColor` (optional) | [DOM.RGBA](DOM.md#type-rgba) | The content box highlight outline color (default: transparent). |

### Overlay.highlightNode

Highlights DOM node with given id or with the given JavaScript object wrapper. Either nodeId or objectId must be specified.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `highlightConfig` | [HighlightConfig](#type-highlightconfig) | A descriptor for the highlight appearance. |
| `nodeId` (optional) | [DOM.NodeId](DOM.md#type-nodeid) | Identifier of the node to highlight. |
| `backendNodeId` (optional) | [DOM.BackendNodeId](DOM.md#type-backendnodeid) | Identifier of the backend node to highlight. |
| `objectId` (optional) | [Runtime.RemoteObjectId](Runtime.md#type-remoteobjectid) | JavaScript object id of the node to be highlighted. |
| `selector` (optional) | string | Selectors to highlight relevant nodes. |

### Overlay.highlightQuad

Highlights given quad. Coordinates are absolute with respect to the main frame viewport.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `quad` | [DOM.Quad](DOM.md#type-quad) | Quad to highlight |
| `color` (optional) | [DOM.RGBA](DOM.md#type-rgba) | The highlight fill color (default: transparent). |
| `outlineColor` (optional) | [DOM.RGBA](DOM.md#type-rgba) | The highlight outline color (default: transparent). |

### Overlay.highlightRect

Highlights given rectangle. Coordinates are absolute with respect to the main frame viewport. Issue: the method does not handle device pixel ratio (DPR) correctly. The coordinates currently have to be adjusted by the client if DPR is not 1 (see crbug.com/437807128).

**Parameters**

| Name | Type | Description |
|---|---|---|
| `x` | integer | X coordinate |
| `y` | integer | Y coordinate |
| `width` | integer | Rectangle width |
| `height` | integer | Rectangle height |
| `color` (optional) | [DOM.RGBA](DOM.md#type-rgba) | The highlight fill color (default: transparent). |
| `outlineColor` (optional) | [DOM.RGBA](DOM.md#type-rgba) | The highlight outline color (default: transparent). |

### Overlay.highlightSourceOrder

Highlights the source order of the children of the DOM node with given id or with the given JavaScript object wrapper. Either nodeId or objectId must be specified.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `sourceOrderConfig` | [SourceOrderConfig](#type-sourceorderconfig) | A descriptor for the appearance of the overlay drawing. |
| `nodeId` (optional) | [DOM.NodeId](DOM.md#type-nodeid) | Identifier of the node to highlight. |
| `backendNodeId` (optional) | [DOM.BackendNodeId](DOM.md#type-backendnodeid) | Identifier of the backend node to highlight. |
| `objectId` (optional) | [Runtime.RemoteObjectId](Runtime.md#type-remoteobjectid) | JavaScript object id of the node to be highlighted. |

### Overlay.setInspectMode

Enters the 'inspect' mode. In this mode, elements that user is hovering over are highlighted. Backend then generates 'inspectNodeRequested' event upon element selection.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `mode` | [InspectMode](#type-inspectmode) | Set an inspection mode. |
| `highlightConfig` (optional) | [HighlightConfig](#type-highlightconfig) | A descriptor for the highlight appearance of hovered-over nodes. May be omitted if `enabled == false`. |

### Overlay.setShowAdHighlights

Highlights owner element of all frames detected to be ads.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `show` | boolean | True for showing ad highlights |

### Overlay.setPausedInDebuggerMessage

**Parameters**

| Name | Type | Description |
|---|---|---|
| `message` (optional) | string | The message to display, also triggers resume and step over controls. |

### Overlay.setShowDebugBorders

Requests that backend shows debug borders on layers

**Parameters**

| Name | Type | Description |
|---|---|---|
| `show` | boolean | True for showing debug borders |

### Overlay.setShowFPSCounter

Requests that backend shows the FPS counter

**Parameters**

| Name | Type | Description |
|---|---|---|
| `show` | boolean | True for showing the FPS counter |

### Overlay.setShowGridOverlays

Highlight multiple elements with the CSS Grid overlay.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `gridNodeHighlightConfigs` | array of [GridNodeHighlightConfig](#type-gridnodehighlightconfig) | An array of node identifiers and descriptors for the highlight appearance. |

### Overlay.setShowFlexOverlays

**Parameters**

| Name | Type | Description |
|---|---|---|
| `flexNodeHighlightConfigs` | array of [FlexNodeHighlightConfig](#type-flexnodehighlightconfig) | An array of node identifiers and descriptors for the highlight appearance. |

### Overlay.setShowScrollSnapOverlays

**Parameters**

| Name | Type | Description |
|---|---|---|
| `scrollSnapHighlightConfigs` | array of [ScrollSnapHighlightConfig](#type-scrollsnaphighlightconfig) | An array of node identifiers and descriptors for the highlight appearance. |

### Overlay.setShowContainerQueryOverlays

**Parameters**

| Name | Type | Description |
|---|---|---|
| `containerQueryHighlightConfigs` | array of [ContainerQueryHighlightConfig](#type-containerqueryhighlightconfig) | An array of node identifiers and descriptors for the highlight appearance. |

### Overlay.setShowInspectedElementAnchor

**Parameters**

| Name | Type | Description |
|---|---|---|
| `inspectedElementAnchorConfig` | [InspectedElementAnchorConfig](#type-inspectedelementanchorconfig) | Node identifier for which to show an anchor for. |

### Overlay.setShowPaintRects

Requests that backend shows paint rectangles

**Parameters**

| Name | Type | Description |
|---|---|---|
| `result` | boolean | True for showing paint rectangles |

### Overlay.setShowLayoutShiftRegions

Requests that backend shows layout shift regions

**Parameters**

| Name | Type | Description |
|---|---|---|
| `result` | boolean | True for showing layout shift regions |

### Overlay.setShowScrollBottleneckRects

Requests that backend shows scroll bottleneck rects

**Parameters**

| Name | Type | Description |
|---|---|---|
| `show` | boolean | True for showing scroll bottleneck rects |

### Overlay.setShowHitTestBorders *(deprecated)*

Deprecated, no longer has any effect.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `show` | boolean | True for showing hit-test borders |

### Overlay.setShowWebVitals *(deprecated)*

Deprecated, no longer has any effect.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `show` | boolean |  |

### Overlay.setShowViewportSizeOnResize

Paints viewport size upon main frame resize.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `show` | boolean | Whether to paint size or not. |

### Overlay.setShowHinge

Add a dual screen device hinge

**Parameters**

| Name | Type | Description |
|---|---|---|
| `hingeConfig` (optional) | [HingeConfig](#type-hingeconfig) | hinge data, null means hideHinge |

### Overlay.setShowDisplayCutout

Add a display cutout overlay.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `displayCutoutConfig` (optional) | [DisplayCutoutConfig](#type-displaycutoutconfig) | display cutout data, null means hide display cutout |

### Overlay.setShowIsolatedElements

Show elements in isolation mode with overlays.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `isolatedElementHighlightConfigs` | array of [IsolatedElementHighlightConfig](#type-isolatedelementhighlightconfig) | An array of node identifiers and descriptors for the highlight appearance. |

### Overlay.setShowWindowControlsOverlay

Show Window Controls Overlay for PWA

**Parameters**

| Name | Type | Description |
|---|---|---|
| `windowControlsOverlayConfig` (optional) | [WindowControlsOverlayConfig](#type-windowcontrolsoverlayconfig) | Window Controls Overlay data, null means hide Window Controls Overlay |

## Events

### Overlay.inspectNodeRequested

Fired when the node should be inspected. This happens after call to `setInspectMode` or when user manually inspects an element.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `backendNodeId` | [DOM.BackendNodeId](DOM.md#type-backendnodeid) | Id of the node to inspect. |

### Overlay.nodeHighlightRequested

Fired when the node should be highlighted. This happens after call to `setInspectMode`.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `nodeId` | [DOM.NodeId](DOM.md#type-nodeid) |  |

### Overlay.screenshotRequested

Fired when user asks to capture screenshot of some area on the page.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `viewport` | [Page.Viewport](Page.md#type-viewport) | Viewport to capture, in device independent pixels (dip). |

### Overlay.inspectPanelShowRequested

Fired when user asks to show the Inspect panel.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `backendNodeId` | [DOM.BackendNodeId](DOM.md#type-backendnodeid) | Id of the node to show in the panel. |

### Overlay.inspectedElementWindowRestored

Fired when user asks to restore the Inspected Element floating window.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `backendNodeId` | [DOM.BackendNodeId](DOM.md#type-backendnodeid) | Id of the node to restore the floating window for. |

### Overlay.inspectModeCanceled

Fired when user cancels the inspect mode.

## Types

<a id="type-sourceorderconfig"></a>
### Overlay.SourceOrderConfig

Type: object

Configuration data for drawing the source order of an elements children.

**Properties**

| Name | Type | Description |
|---|---|---|
| `parentOutlineColor` | [DOM.RGBA](DOM.md#type-rgba) | the color to outline the given element in. |
| `childOutlineColor` | [DOM.RGBA](DOM.md#type-rgba) | the color to outline the child elements in. |

<a id="type-gridhighlightconfig"></a>
### Overlay.GridHighlightConfig

Type: object

Configuration data for the highlighting of Grid elements.

**Properties**

| Name | Type | Description |
|---|---|---|
| `showGridExtensionLines` (optional) | boolean | Whether the extension lines from grid cells to the rulers should be shown (default: false). |
| `showPositiveLineNumbers` (optional) | boolean | Show Positive line number labels (default: false). |
| `showNegativeLineNumbers` (optional) | boolean | Show Negative line number labels (default: false). |
| `showAreaNames` (optional) | boolean | Show area name labels (default: false). |
| `showLineNames` (optional) | boolean | Show line name labels (default: false). |
| `showTrackSizes` (optional) | boolean | Show track size labels (default: false). |
| `gridBorderColor` (optional) | [DOM.RGBA](DOM.md#type-rgba) | The grid container border highlight color (default: transparent). |
| `cellBorderColor` (optional) *(deprecated)* | [DOM.RGBA](DOM.md#type-rgba) | The cell border color (default: transparent). Deprecated, please use rowLineColor and columnLineColor instead. |
| `rowLineColor` (optional) | [DOM.RGBA](DOM.md#type-rgba) | The row line color (default: transparent). |
| `columnLineColor` (optional) | [DOM.RGBA](DOM.md#type-rgba) | The column line color (default: transparent). |
| `gridBorderDash` (optional) | boolean | Whether the grid border is dashed (default: false). |
| `cellBorderDash` (optional) *(deprecated)* | boolean | Whether the cell border is dashed (default: false). Deprecated, please us rowLineDash and columnLineDash instead. |
| `rowLineDash` (optional) | boolean | Whether row lines are dashed (default: false). |
| `columnLineDash` (optional) | boolean | Whether column lines are dashed (default: false). |
| `rowGapColor` (optional) | [DOM.RGBA](DOM.md#type-rgba) | The row gap highlight fill color (default: transparent). |
| `rowHatchColor` (optional) | [DOM.RGBA](DOM.md#type-rgba) | The row gap hatching fill color (default: transparent). |
| `columnGapColor` (optional) | [DOM.RGBA](DOM.md#type-rgba) | The column gap highlight fill color (default: transparent). |
| `columnHatchColor` (optional) | [DOM.RGBA](DOM.md#type-rgba) | The column gap hatching fill color (default: transparent). |
| `areaBorderColor` (optional) | [DOM.RGBA](DOM.md#type-rgba) | The named grid areas border color (Default: transparent). |
| `gridBackgroundColor` (optional) | [DOM.RGBA](DOM.md#type-rgba) | The grid container background color (Default: transparent). |

<a id="type-flexcontainerhighlightconfig"></a>
### Overlay.FlexContainerHighlightConfig

Type: object

Configuration data for the highlighting of Flex container elements.

**Properties**

| Name | Type | Description |
|---|---|---|
| `containerBorder` (optional) | [LineStyle](#type-linestyle) | The style of the container border |
| `lineSeparator` (optional) | [LineStyle](#type-linestyle) | The style of the separator between lines |
| `itemSeparator` (optional) | [LineStyle](#type-linestyle) | The style of the separator between items |
| `mainDistributedSpace` (optional) | [BoxStyle](#type-boxstyle) | Style of content-distribution space on the main axis (justify-content). |
| `crossDistributedSpace` (optional) | [BoxStyle](#type-boxstyle) | Style of content-distribution space on the cross axis (align-content). |
| `rowGapSpace` (optional) | [BoxStyle](#type-boxstyle) | Style of empty space caused by row gaps (gap/row-gap). |
| `columnGapSpace` (optional) | [BoxStyle](#type-boxstyle) | Style of empty space caused by columns gaps (gap/column-gap). |
| `crossAlignment` (optional) | [LineStyle](#type-linestyle) | Style of the self-alignment line (align-items). |

<a id="type-flexitemhighlightconfig"></a>
### Overlay.FlexItemHighlightConfig

Type: object

Configuration data for the highlighting of Flex item elements.

**Properties**

| Name | Type | Description |
|---|---|---|
| `baseSizeBox` (optional) | [BoxStyle](#type-boxstyle) | Style of the box representing the item's base size |
| `baseSizeBorder` (optional) | [LineStyle](#type-linestyle) | Style of the border around the box representing the item's base size |
| `flexibilityArrow` (optional) | [LineStyle](#type-linestyle) | Style of the arrow representing if the item grew or shrank |

<a id="type-linestyle"></a>
### Overlay.LineStyle

Type: object

Style information for drawing a line.

**Properties**

| Name | Type | Description |
|---|---|---|
| `color` (optional) | [DOM.RGBA](DOM.md#type-rgba) | The color of the line (default: transparent) |
| `pattern` (optional) | enum: `dashed`, `dotted` | The line pattern (default: solid) |

<a id="type-boxstyle"></a>
### Overlay.BoxStyle

Type: object

Style information for drawing a box.

**Properties**

| Name | Type | Description |
|---|---|---|
| `fillColor` (optional) | [DOM.RGBA](DOM.md#type-rgba) | The background color for the box (default: transparent) |
| `hatchColor` (optional) | [DOM.RGBA](DOM.md#type-rgba) | The hatching color for the box (default: transparent) |

<a id="type-contrastalgorithm"></a>
### Overlay.ContrastAlgorithm

Type: string

Allowed values: `aa`, `aaa`, `apca`

<a id="type-imcbhighlightconfig"></a>
### Overlay.ImcbHighlightConfig

Type: object

Configuration for Inset-Modified Containing Block (IMCB) and CSS Anchor Positioning highlight.

**Properties**

| Name | Type | Description |
|---|---|---|
| `imcbBorderColor` (optional) | [DOM.RGBA](DOM.md#type-rgba) | Border color for the Inset-Modified Containing Block (default: transparent). |
| `imcbBackgroundColor` (optional) | [DOM.RGBA](DOM.md#type-rgba) | Background fill color for the Inset-Modified Containing Block (default: transparent). |
| `insetsBackgroundColor` (optional) | [DOM.RGBA](DOM.md#type-rgba) | Fill color for the inset modifiers area (difference between CB and IMCB). |
| `insetsHatchColor` (optional) | [DOM.RGBA](DOM.md#type-rgba) | Hatch color for the inset modifiers area. |
| `anchorBorderColor` (optional) | [DOM.RGBA](DOM.md#type-rgba) | Border color for the referenced target anchor element(s) (when element is anchor-positioned). |
| `anchorBackgroundColor` (optional) | [DOM.RGBA](DOM.md#type-rgba) | Background fill color for the referenced target anchor element(s) (when element is anchor-positioned). |
| `showPositionAreaGrid` (optional) | boolean | Whether to render the 3x3 position-area grid lines when position-area is used. |
| `positionAreaGridLineColor` (optional) | [DOM.RGBA](DOM.md#type-rgba) | Line color for the 3x3 position-area grid lines. |
| `positionAreaActiveRegionColor` (optional) | [DOM.RGBA](DOM.md#type-rgba) | Fill color for the active region within the position-area grid. |

<a id="type-highlightconfig"></a>
### Overlay.HighlightConfig

Type: object

Configuration data for the highlighting of page elements.

**Properties**

| Name | Type | Description |
|---|---|---|
| `showInfo` (optional) | boolean | Whether the node info tooltip should be shown (default: false). |
| `showStyles` (optional) | boolean | Whether the node styles in the tooltip (default: false). |
| `showRulers` (optional) | boolean | Whether the rulers should be shown (default: false). |
| `showAccessibilityInfo` (optional) | boolean | Whether the a11y info should be shown (default: true). |
| `showExtensionLines` (optional) | boolean | Whether the extension lines from node to the rulers should be shown (default: false). |
| `contentColor` (optional) | [DOM.RGBA](DOM.md#type-rgba) | The content box highlight fill color (default: transparent). |
| `paddingColor` (optional) | [DOM.RGBA](DOM.md#type-rgba) | The padding highlight fill color (default: transparent). |
| `borderColor` (optional) | [DOM.RGBA](DOM.md#type-rgba) | The border highlight fill color (default: transparent). |
| `marginColor` (optional) | [DOM.RGBA](DOM.md#type-rgba) | The margin highlight fill color (default: transparent). |
| `eventTargetColor` (optional) | [DOM.RGBA](DOM.md#type-rgba) | The event target element highlight fill color (default: transparent). |
| `shapeColor` (optional) | [DOM.RGBA](DOM.md#type-rgba) | The shape outside fill color (default: transparent). |
| `shapeMarginColor` (optional) | [DOM.RGBA](DOM.md#type-rgba) | The shape margin fill color (default: transparent). |
| `cssGridColor` (optional) | [DOM.RGBA](DOM.md#type-rgba) | The grid layout color (default: transparent). |
| `colorFormat` (optional) | [ColorFormat](#type-colorformat) | The color format used to format color styles (default: hex). |
| `gridHighlightConfig` (optional) | [GridHighlightConfig](#type-gridhighlightconfig) | The grid layout highlight configuration (default: all transparent). |
| `flexContainerHighlightConfig` (optional) | [FlexContainerHighlightConfig](#type-flexcontainerhighlightconfig) | The flex container highlight configuration (default: all transparent). |
| `flexItemHighlightConfig` (optional) | [FlexItemHighlightConfig](#type-flexitemhighlightconfig) | The flex item highlight configuration (default: all transparent). |
| `contrastAlgorithm` (optional) | [ContrastAlgorithm](#type-contrastalgorithm) | The contrast algorithm to use for the contrast ratio (default: aa). |
| `containerQueryContainerHighlightConfig` (optional) | [ContainerQueryContainerHighlightConfig](#type-containerquerycontainerhighlightconfig) | The container query container highlight configuration (default: all transparent). |
| `imcbHighlightConfig` (optional) | [ImcbHighlightConfig](#type-imcbhighlightconfig) | The IMCB highlight configuration (default: all transparent). |

<a id="type-colorformat"></a>
### Overlay.ColorFormat

Type: string

Allowed values: `rgb`, `hsl`, `hwb`, `hex`

<a id="type-gridnodehighlightconfig"></a>
### Overlay.GridNodeHighlightConfig

Type: object

Configurations for Persistent Grid Highlight

**Properties**

| Name | Type | Description |
|---|---|---|
| `gridHighlightConfig` | [GridHighlightConfig](#type-gridhighlightconfig) | A descriptor for the highlight appearance. |
| `nodeId` | [DOM.NodeId](DOM.md#type-nodeid) | Identifier of the node to highlight. |

<a id="type-flexnodehighlightconfig"></a>
### Overlay.FlexNodeHighlightConfig

Type: object

**Properties**

| Name | Type | Description |
|---|---|---|
| `flexContainerHighlightConfig` | [FlexContainerHighlightConfig](#type-flexcontainerhighlightconfig) | A descriptor for the highlight appearance of flex containers. |
| `nodeId` | [DOM.NodeId](DOM.md#type-nodeid) | Identifier of the node to highlight. |

<a id="type-scrollsnapcontainerhighlightconfig"></a>
### Overlay.ScrollSnapContainerHighlightConfig

Type: object

**Properties**

| Name | Type | Description |
|---|---|---|
| `snapportBorder` (optional) | [LineStyle](#type-linestyle) | The style of the snapport border (default: transparent) |
| `snapAreaBorder` (optional) | [LineStyle](#type-linestyle) | The style of the snap area border (default: transparent) |
| `scrollMarginColor` (optional) | [DOM.RGBA](DOM.md#type-rgba) | The margin highlight fill color (default: transparent). |
| `scrollPaddingColor` (optional) | [DOM.RGBA](DOM.md#type-rgba) | The padding highlight fill color (default: transparent). |

<a id="type-scrollsnaphighlightconfig"></a>
### Overlay.ScrollSnapHighlightConfig

Type: object

**Properties**

| Name | Type | Description |
|---|---|---|
| `scrollSnapContainerHighlightConfig` | [ScrollSnapContainerHighlightConfig](#type-scrollsnapcontainerhighlightconfig) | A descriptor for the highlight appearance of scroll snap containers. |
| `nodeId` | [DOM.NodeId](DOM.md#type-nodeid) | Identifier of the node to highlight. |

<a id="type-hingeconfig"></a>
### Overlay.HingeConfig

Type: object

Configuration for dual screen hinge

**Properties**

| Name | Type | Description |
|---|---|---|
| `rect` | [DOM.Rect](DOM.md#type-rect) | A rectangle represent hinge |
| `contentColor` (optional) | [DOM.RGBA](DOM.md#type-rgba) | The content box highlight fill color (default: a dark color). |
| `outlineColor` (optional) | [DOM.RGBA](DOM.md#type-rgba) | The content box highlight outline color (default: transparent). |

<a id="type-displaycutoutshape"></a>
### Overlay.DisplayCutoutShape

Type: string

Supported display cutout shapes.

Allowed values: `pill`, `notch`, `circle`, `rectangle`

<a id="type-displaycutoutconfig"></a>
### Overlay.DisplayCutoutConfig

Type: object

Configuration for a display cutout.

**Properties**

| Name | Type | Description |
|---|---|---|
| `rect` | [DOM.Rect](DOM.md#type-rect) | A rectangle representing the cutout bounds. |
| `shape` | [DisplayCutoutShape](#type-displaycutoutshape) | Shape used to draw the cutout. |
| `borderRadius` (optional) | integer | Border radius for rounded cutout shapes. |
| `upperRadius` (optional) | integer | Upper shoulder radius for notch cutout shapes. |
| `lowerRadius` (optional) | integer | Lower transition radius for notch cutout shapes. |
| `cx` (optional) | integer | Center x coordinate for circle cutout shapes. |
| `cy` (optional) | integer | Center y coordinate for circle cutout shapes. |
| `radius` (optional) | integer | Radius for circle cutout shapes. |
| `contentColor` (optional) | [DOM.RGBA](DOM.md#type-rgba) | The cutout fill color (default: black). |

<a id="type-windowcontrolsoverlayconfig"></a>
### Overlay.WindowControlsOverlayConfig

Type: object

Configuration for Window Controls Overlay

**Properties**

| Name | Type | Description |
|---|---|---|
| `showCSS` | boolean | Whether the title bar CSS should be shown when emulating the Window Controls Overlay. |
| `selectedPlatform` | string | Selected platforms to show the overlay. |
| `themeColor` | string | The theme color defined in app manifest. |

<a id="type-containerqueryhighlightconfig"></a>
### Overlay.ContainerQueryHighlightConfig

Type: object

**Properties**

| Name | Type | Description |
|---|---|---|
| `containerQueryContainerHighlightConfig` | [ContainerQueryContainerHighlightConfig](#type-containerquerycontainerhighlightconfig) | A descriptor for the highlight appearance of container query containers. |
| `nodeId` | [DOM.NodeId](DOM.md#type-nodeid) | Identifier of the container node to highlight. |

<a id="type-containerquerycontainerhighlightconfig"></a>
### Overlay.ContainerQueryContainerHighlightConfig

Type: object

**Properties**

| Name | Type | Description |
|---|---|---|
| `containerBorder` (optional) | [LineStyle](#type-linestyle) | The style of the container border. |
| `descendantBorder` (optional) | [LineStyle](#type-linestyle) | The style of the descendants' borders. |

<a id="type-isolatedelementhighlightconfig"></a>
### Overlay.IsolatedElementHighlightConfig

Type: object

**Properties**

| Name | Type | Description |
|---|---|---|
| `isolationModeHighlightConfig` | [IsolationModeHighlightConfig](#type-isolationmodehighlightconfig) | A descriptor for the highlight appearance of an element in isolation mode. |
| `nodeId` | [DOM.NodeId](DOM.md#type-nodeid) | Identifier of the isolated element to highlight. |

<a id="type-isolationmodehighlightconfig"></a>
### Overlay.IsolationModeHighlightConfig

Type: object

**Properties**

| Name | Type | Description |
|---|---|---|
| `resizerColor` (optional) | [DOM.RGBA](DOM.md#type-rgba) | The fill color of the resizers (default: transparent). |
| `resizerHandleColor` (optional) | [DOM.RGBA](DOM.md#type-rgba) | The fill color for resizer handles (default: transparent). |
| `maskColor` (optional) | [DOM.RGBA](DOM.md#type-rgba) | The fill color for the mask covering non-isolated elements (default: transparent). |

<a id="type-inspectmode"></a>
### Overlay.InspectMode

Type: string

Allowed values: `searchForNode`, `searchForUAShadowDOM`, `captureAreaScreenshot`, `none`

<a id="type-inspectedelementanchorconfig"></a>
### Overlay.InspectedElementAnchorConfig

Type: object

**Properties**

| Name | Type | Description |
|---|---|---|
| `nodeId` (optional) | [DOM.NodeId](DOM.md#type-nodeid) | Identifier of the node to highlight. |
| `backendNodeId` (optional) | [DOM.BackendNodeId](DOM.md#type-backendnodeid) | Identifier of the backend node to highlight. |

