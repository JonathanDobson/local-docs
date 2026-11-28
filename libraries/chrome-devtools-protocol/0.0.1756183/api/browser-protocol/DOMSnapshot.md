# DOMSnapshot domain

Chrome DevTools Protocol, browser protocol (tip-of-tree) (protocol 1.3).

**Experimental**

This domain facilitates obtaining document snapshots with DOM, layout, and style information.

Depends on: [CSS](CSS.md), [DOM](DOM.md), [DOMDebugger](DOMDebugger.md), [Page](Page.md)

4 methods, 0 events, 15 types.

## Methods

### DOMSnapshot.disable

Disables DOM snapshot agent for the given page.

No parameters.

### DOMSnapshot.enable

Enables DOM snapshot agent for the given page.

No parameters.

### DOMSnapshot.getSnapshot

**Deprecated**

Returns a document snapshot, including the full DOM tree of the root node (including iframes,
template contents, and imported documents) in a flattened array, as well as layout and
white-listed computed style information for the nodes. Shadow DOM in the returned DOM tree is
flattened.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `computedStyleWhitelist` | array of string | Whitelist of computed styles to return. |
| `includeEventListeners` (optional) | boolean | Whether or not to retrieve details of DOM listeners (default false). |
| `includePaintOrder` (optional) | boolean | Whether to determine and include the paint order index of LayoutTreeNodes (default false). |
| `includeUserAgentShadowTree` (optional) | boolean | Whether to include UA shadow tree in the snapshot (default false). |

**Return object**

| Name | Type | Description |
|---|---|---|
| `domNodes` | array of [DOMSnapshot.DOMNode](#type-domnode) | The nodes in the DOM tree. The DOMNode at index 0 corresponds to the root document. |
| `layoutTreeNodes` | array of [DOMSnapshot.LayoutTreeNode](#type-layouttreenode) | The nodes in the layout tree. |
| `computedStyles` | array of [DOMSnapshot.ComputedStyle](#type-computedstyle) | Whitelisted ComputedStyle properties for each node in the layout tree. |

### DOMSnapshot.captureSnapshot

Returns a document snapshot, including the full DOM tree of the root node (including iframes,
template contents, and imported documents) in a flattened array, as well as layout and
white-listed computed style information for the nodes. Shadow DOM in the returned DOM tree is
flattened.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `computedStyles` | array of string | Whitelist of computed styles to return. |
| `includePaintOrder` (optional) | boolean | Whether to include layout object paint orders into the snapshot. |
| `includeDOMRects` (optional) | boolean | Whether to include DOM rectangles (offsetRects, clientRects, scrollRects) into the snapshot |
| `includeBlendedBackgroundColors` (optional) | boolean | **Experimental** Whether to include blended background colors in the snapshot (default: false). Blended background color is achieved by blending background colors of all elements that overlap with the current element. |
| `includeTextColorOpacities` (optional) | boolean | **Experimental** Whether to include text color opacity in the snapshot (default: false). An element might have the opacity property set that affects the text color of the element. The final text color opacity is computed based on the opacity of all overlapping elements. |

**Return object**

| Name | Type | Description |
|---|---|---|
| `documents` | array of [DOMSnapshot.DocumentSnapshot](#type-documentsnapshot) | The nodes in the DOM tree. The DOMNode at index 0 corresponds to the root document. |
| `strings` | array of string | Shared string table that all string properties refer to with indexes. |

## Types

<a id="type-domnode"></a>
### DOMSnapshot.DOMNode

A Node in the DOM tree.

Type: object

**Properties**

| Name | Type | Description |
|---|---|---|
| `nodeType` | integer | `Node`'s nodeType. |
| `nodeName` | string | `Node`'s nodeName. |
| `nodeValue` | string | `Node`'s nodeValue. |
| `textValue` (optional) | string | Only set for textarea elements, contains the text value. |
| `inputValue` (optional) | string | Only set for input elements, contains the input's associated text value. |
| `inputChecked` (optional) | boolean | Only set for radio and checkbox input elements, indicates if the element has been checked |
| `optionSelected` (optional) | boolean | Only set for option elements, indicates if the element has been selected |
| `backendNodeId` | [DOM.BackendNodeId](DOM.md#type-backendnodeid) | `Node`'s id, corresponds to DOM.Node.backendNodeId. |
| `childNodeIndexes` (optional) | array of integer | The indexes of the node's child nodes in the `domNodes` array returned by `getSnapshot`, if any. |
| `attributes` (optional) | array of [DOMSnapshot.NameValue](#type-namevalue) | Attributes of an `Element` node. |
| `pseudoElementIndexes` (optional) | array of integer | Indexes of pseudo elements associated with this node in the `domNodes` array returned by `getSnapshot`, if any. |
| `layoutNodeIndex` (optional) | integer | The index of the node's related layout tree node in the `layoutTreeNodes` array returned by `getSnapshot`, if any. |
| `documentURL` (optional) | string | Document URL that `Document` or `FrameOwner` node points to. |
| `baseURL` (optional) | string | Base URL that `Document` or `FrameOwner` node uses for URL completion. |
| `contentLanguage` (optional) | string | Only set for documents, contains the document's content language. |
| `documentEncoding` (optional) | string | Only set for documents, contains the document's character set encoding. |
| `publicId` (optional) | string | `DocumentType` node's publicId. |
| `systemId` (optional) | string | `DocumentType` node's systemId. |
| `frameId` (optional) | [Page.FrameId](Page.md#type-frameid) | Frame ID for frame owner elements and also for the document node. |
| `contentDocumentIndex` (optional) | integer | The index of a frame owner element's content document in the `domNodes` array returned by `getSnapshot`, if any. |
| `pseudoType` (optional) | [DOM.PseudoType](DOM.md#type-pseudotype) | Type of a pseudo element node. |
| `shadowRootType` (optional) | [DOM.ShadowRootType](DOM.md#type-shadowroottype) | Shadow root type. |
| `isClickable` (optional) | boolean | Whether this DOM node responds to mouse clicks. This includes nodes that have had click event listeners attached via JavaScript as well as anchor tags that naturally navigate when clicked. |
| `eventListeners` (optional) | array of [DOMDebugger.EventListener](DOMDebugger.md#type-eventlistener) | Details of the node's event listeners, if any. |
| `currentSourceURL` (optional) | string | The selected url for nodes with a srcset attribute. |
| `originURL` (optional) | string | The url of the script (if any) that generates this node. |
| `scrollOffsetX` (optional) | number | Scroll offsets, set when this node is a Document. |
| `scrollOffsetY` (optional) | number |  |

<a id="type-inlinetextbox"></a>
### DOMSnapshot.InlineTextBox

Details of post layout rendered text positions. The exact layout should not be regarded as
stable and may change between versions.

Type: object

**Properties**

| Name | Type | Description |
|---|---|---|
| `boundingBox` | [DOM.Rect](DOM.md#type-rect) | The bounding box in document coordinates. Note that scroll offset of the document is ignored. |
| `startCharacterIndex` | integer | The starting index in characters, for this post layout textbox substring. Characters that would be represented as a surrogate pair in UTF-16 have length 2. |
| `numCharacters` | integer | The number of characters in this post layout textbox substring. Characters that would be represented as a surrogate pair in UTF-16 have length 2. |

<a id="type-layouttreenode"></a>
### DOMSnapshot.LayoutTreeNode

Details of an element in the DOM tree with a LayoutObject.

Type: object

**Properties**

| Name | Type | Description |
|---|---|---|
| `domNodeIndex` | integer | The index of the related DOM node in the `domNodes` array returned by `getSnapshot`. |
| `boundingBox` | [DOM.Rect](DOM.md#type-rect) | The bounding box in document coordinates. Note that scroll offset of the document is ignored. |
| `layoutText` (optional) | string | Contents of the LayoutText, if any. |
| `inlineTextNodes` (optional) | array of [DOMSnapshot.InlineTextBox](#type-inlinetextbox) | The post-layout inline text nodes, if any. |
| `styleIndex` (optional) | integer | Index into the `computedStyles` array returned by `getSnapshot`. |
| `paintOrder` (optional) | integer | Global paint order index, which is determined by the stacking order of the nodes. Nodes that are painted together will have the same index. Only provided if includePaintOrder in getSnapshot was true. |
| `isStackingContext` (optional) | boolean | Set to true to indicate the element begins a new stacking context. |

<a id="type-computedstyle"></a>
### DOMSnapshot.ComputedStyle

A subset of the full ComputedStyle as defined by the request whitelist.

Type: object

**Properties**

| Name | Type | Description |
|---|---|---|
| `properties` | array of [DOMSnapshot.NameValue](#type-namevalue) | Name/value pairs of computed style properties. |

<a id="type-namevalue"></a>
### DOMSnapshot.NameValue

A name/value pair.

Type: object

**Properties**

| Name | Type | Description |
|---|---|---|
| `name` | string | Attribute/property name. |
| `value` | string | Attribute/property value. |

<a id="type-stringindex"></a>
### DOMSnapshot.StringIndex

Index of the string in the strings table.

Type: integer

<a id="type-arrayofstrings"></a>
### DOMSnapshot.ArrayOfStrings

Index of the string in the strings table.

Type: array of [DOMSnapshot.StringIndex](#type-stringindex)

<a id="type-rarestringdata"></a>
### DOMSnapshot.RareStringData

Data that is only present on rare nodes.

Type: object

**Properties**

| Name | Type | Description |
|---|---|---|
| `index` | array of integer |  |
| `value` | array of [DOMSnapshot.StringIndex](#type-stringindex) |  |

<a id="type-rarebooleandata"></a>
### DOMSnapshot.RareBooleanData

Type: object

**Properties**

| Name | Type | Description |
|---|---|---|
| `index` | array of integer |  |

<a id="type-rareintegerdata"></a>
### DOMSnapshot.RareIntegerData

Type: object

**Properties**

| Name | Type | Description |
|---|---|---|
| `index` | array of integer |  |
| `value` | array of integer |  |

<a id="type-rectangle"></a>
### DOMSnapshot.Rectangle

Type: array of number

<a id="type-documentsnapshot"></a>
### DOMSnapshot.DocumentSnapshot

Document snapshot.

Type: object

**Properties**

| Name | Type | Description |
|---|---|---|
| `documentURL` | [DOMSnapshot.StringIndex](#type-stringindex) | Document URL that `Document` or `FrameOwner` node points to. |
| `title` | [DOMSnapshot.StringIndex](#type-stringindex) | Document title. |
| `baseURL` | [DOMSnapshot.StringIndex](#type-stringindex) | Base URL that `Document` or `FrameOwner` node uses for URL completion. |
| `contentLanguage` | [DOMSnapshot.StringIndex](#type-stringindex) | Contains the document's content language. |
| `encodingName` | [DOMSnapshot.StringIndex](#type-stringindex) | Contains the document's character set encoding. |
| `publicId` | [DOMSnapshot.StringIndex](#type-stringindex) | `DocumentType` node's publicId. |
| `systemId` | [DOMSnapshot.StringIndex](#type-stringindex) | `DocumentType` node's systemId. |
| `frameId` | [DOMSnapshot.StringIndex](#type-stringindex) | Frame ID for frame owner elements and also for the document node. |
| `nodes` | [DOMSnapshot.NodeTreeSnapshot](#type-nodetreesnapshot) | A table with dom nodes. |
| `layout` | [DOMSnapshot.LayoutTreeSnapshot](#type-layouttreesnapshot) | The nodes in the layout tree. |
| `textBoxes` | [DOMSnapshot.TextBoxSnapshot](#type-textboxsnapshot) | The post-layout inline text nodes. |
| `scrollOffsetX` (optional) | number | Horizontal scroll offset. |
| `scrollOffsetY` (optional) | number | Vertical scroll offset. |
| `contentWidth` (optional) | number | Document content width. |
| `contentHeight` (optional) | number | Document content height. |

<a id="type-nodetreesnapshot"></a>
### DOMSnapshot.NodeTreeSnapshot

Table containing nodes.

Type: object

**Properties**

| Name | Type | Description |
|---|---|---|
| `parentIndex` (optional) | array of integer | Parent node index. |
| `nodeType` (optional) | array of integer | `Node`'s nodeType. |
| `shadowRootType` (optional) | [DOMSnapshot.RareStringData](#type-rarestringdata) | Type of the shadow root the `Node` is in. String values are equal to the `ShadowRootType` enum. |
| `nodeName` (optional) | array of [DOMSnapshot.StringIndex](#type-stringindex) | `Node`'s nodeName. |
| `nodeValue` (optional) | array of [DOMSnapshot.StringIndex](#type-stringindex) | `Node`'s nodeValue. |
| `backendNodeId` (optional) | array of [DOM.BackendNodeId](DOM.md#type-backendnodeid) | `Node`'s id, corresponds to DOM.Node.backendNodeId. |
| `attributes` (optional) | array of [DOMSnapshot.ArrayOfStrings](#type-arrayofstrings) | Attributes of an `Element` node. Flatten name, value pairs. |
| `textValue` (optional) | [DOMSnapshot.RareStringData](#type-rarestringdata) | Only set for textarea elements, contains the text value. |
| `inputValue` (optional) | [DOMSnapshot.RareStringData](#type-rarestringdata) | Only set for input elements, contains the input's associated text value. |
| `inputChecked` (optional) | [DOMSnapshot.RareBooleanData](#type-rarebooleandata) | Only set for radio and checkbox input elements, indicates if the element has been checked |
| `optionSelected` (optional) | [DOMSnapshot.RareBooleanData](#type-rarebooleandata) | Only set for option elements, indicates if the element has been selected |
| `contentDocumentIndex` (optional) | [DOMSnapshot.RareIntegerData](#type-rareintegerdata) | The index of the document in the list of the snapshot documents. |
| `pseudoType` (optional) | [DOMSnapshot.RareStringData](#type-rarestringdata) | Type of a pseudo element node. |
| `pseudoIdentifier` (optional) | [DOMSnapshot.RareStringData](#type-rarestringdata) | Pseudo element identifier for this node. Only present if there is a valid pseudoType. |
| `isClickable` (optional) | [DOMSnapshot.RareBooleanData](#type-rarebooleandata) | Whether this DOM node responds to mouse clicks. This includes nodes that have had click event listeners attached via JavaScript as well as anchor tags that naturally navigate when clicked. |
| `currentSourceURL` (optional) | [DOMSnapshot.RareStringData](#type-rarestringdata) | The selected url for nodes with a srcset attribute. |
| `originURL` (optional) | [DOMSnapshot.RareStringData](#type-rarestringdata) | The url of the script (if any) that generates this node. |

<a id="type-layouttreesnapshot"></a>
### DOMSnapshot.LayoutTreeSnapshot

Table of details of an element in the DOM tree with a LayoutObject.

Type: object

**Properties**

| Name | Type | Description |
|---|---|---|
| `nodeIndex` | array of integer | Index of the corresponding node in the `NodeTreeSnapshot` array returned by `captureSnapshot`. |
| `styles` | array of [DOMSnapshot.ArrayOfStrings](#type-arrayofstrings) | Array of indexes specifying computed style strings, filtered according to the `computedStyles` parameter passed to `captureSnapshot`. |
| `bounds` | array of [DOMSnapshot.Rectangle](#type-rectangle) | The absolute position bounding box. |
| `text` | array of [DOMSnapshot.StringIndex](#type-stringindex) | Contents of the LayoutText, if any. |
| `stackingContexts` | [DOMSnapshot.RareBooleanData](#type-rarebooleandata) | Stacking context information. |
| `paintOrders` (optional) | array of integer | Global paint order index, which is determined by the stacking order of the nodes. Nodes that are painted together will have the same index. Only provided if includePaintOrder in captureSnapshot was true. |
| `offsetRects` (optional) | array of [DOMSnapshot.Rectangle](#type-rectangle) | The offset rect of nodes. Only available when includeDOMRects is set to true |
| `scrollRects` (optional) | array of [DOMSnapshot.Rectangle](#type-rectangle) | The scroll rect of nodes. Only available when includeDOMRects is set to true |
| `clientRects` (optional) | array of [DOMSnapshot.Rectangle](#type-rectangle) | The client rect of nodes. Only available when includeDOMRects is set to true |
| `blendedBackgroundColors` (optional) | array of [DOMSnapshot.StringIndex](#type-stringindex) | **Experimental** The list of background colors that are blended with colors of overlapping elements. |
| `textColorOpacities` (optional) | array of number | **Experimental** The list of computed text opacities. |

<a id="type-textboxsnapshot"></a>
### DOMSnapshot.TextBoxSnapshot

Table of details of the post layout rendered text positions. The exact layout should not be regarded as
stable and may change between versions.

Type: object

**Properties**

| Name | Type | Description |
|---|---|---|
| `layoutIndex` | array of integer | Index of the layout tree node that owns this box collection. |
| `bounds` | array of [DOMSnapshot.Rectangle](#type-rectangle) | The absolute position bounding box. |
| `start` | array of integer | The starting index in characters, for this post layout textbox substring. Characters that would be represented as a surrogate pair in UTF-16 have length 2. |
| `length` | array of integer | The number of characters in this post layout textbox substring. Characters that would be represented as a surrogate pair in UTF-16 have length 2. |
