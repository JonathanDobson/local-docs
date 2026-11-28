# DOM domain

Copyright 2017 The Chromium Authors Use of this source code is governed by a BSD-style license that can be found in the LICENSE file.  Contributing to Chrome DevTools Protocol: https://goo.gle/devtools-contribution-guide-cdp This domain exposes DOM read/write operations. Each DOM Node is represented with its mirror object that has an `id`. This `id` can be used to get additional information on the Node, resolve it into the JavaScript object wrapper, etc. It is important that client receives DOM events only for the nodes that are known to the client. Backend keeps track of the nodes that were sent to the client and never sends the same node twice. It is client's responsibility to collect information about the nodes that were sent to the client. Note that `iframe` owner elements will return corresponding document elements as their child nodes.

Depends on: [Runtime](Runtime.md), [Network](Network.md)

Methods are called as `DOM.<command>` and events arrive as `DOM.<event>`.

## Commands

### DOM.collectClassNamesFromSubtree *(experimental)*

Collects class names for the node with given id and all of it's child nodes.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `nodeId` | [NodeId](#type-nodeid) | Id of the node to collect class names. |

**Returns**

| Name | Type | Description |
|---|---|---|
| `classNames` | array of string | Class name list. |

### DOM.copyTo *(experimental)*

Creates a deep copy of the specified node and places it into the target container before the given anchor.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `nodeId` | [NodeId](#type-nodeid) | Id of the node to copy. |
| `targetNodeId` | [NodeId](#type-nodeid) | Id of the element to drop the copy into. |
| `insertBeforeNodeId` (optional) | [NodeId](#type-nodeid) | Drop the copy before this node (if absent, the copy becomes the last child of `targetNodeId`). |

**Returns**

| Name | Type | Description |
|---|---|---|
| `nodeId` | [NodeId](#type-nodeid) | Id of the node clone. |

### DOM.describeNode

Describes node given its id, does not require domain to be enabled. Does not start tracking any objects, can be used for automation.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `nodeId` (optional) | [NodeId](#type-nodeid) | Identifier of the node. |
| `backendNodeId` (optional) | [BackendNodeId](#type-backendnodeid) | Identifier of the backend node. |
| `objectId` (optional) | [Runtime.RemoteObjectId](Runtime.md#type-remoteobjectid) | JavaScript object id of the node wrapper. |
| `depth` (optional) | integer | The maximum depth at which children should be retrieved, defaults to 1. Use -1 for the entire subtree or provide an integer larger than 0. |
| `pierce` (optional) | boolean | Whether or not iframes and shadow roots should be traversed when returning the subtree (default is false). |

**Returns**

| Name | Type | Description |
|---|---|---|
| `node` | [Node](#type-node) | Node description. |

### DOM.scrollIntoViewIfNeeded

Scrolls the specified rect of the given node into view if not already visible. Note: exactly one between nodeId, backendNodeId and objectId should be passed to identify the node.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `nodeId` (optional) | [NodeId](#type-nodeid) | Identifier of the node. |
| `backendNodeId` (optional) | [BackendNodeId](#type-backendnodeid) | Identifier of the backend node. |
| `objectId` (optional) | [Runtime.RemoteObjectId](Runtime.md#type-remoteobjectid) | JavaScript object id of the node wrapper. |
| `rect` (optional) | [Rect](#type-rect) | The rect to be scrolled into view, relative to the node's border box, in CSS pixels. When omitted, center of the node will be used, similar to Element.scrollIntoView. |

### DOM.disable

Disables DOM agent for the given page.

### DOM.discardSearchResults *(experimental)*

Discards search results from the session with the given id. `getSearchResults` should no longer be called for that search.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `searchId` | string | Unique search session identifier. |

### DOM.enable

Enables DOM agent for the given page.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `includeWhitespace` (optional) *(experimental)* | enum: `none`, `all` | Whether to include whitespaces in the children array of returned Nodes. |

### DOM.focus

Focuses the given element.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `nodeId` (optional) | [NodeId](#type-nodeid) | Identifier of the node. |
| `backendNodeId` (optional) | [BackendNodeId](#type-backendnodeid) | Identifier of the backend node. |
| `objectId` (optional) | [Runtime.RemoteObjectId](Runtime.md#type-remoteobjectid) | JavaScript object id of the node wrapper. |

### DOM.getAttributes

Returns attributes for the specified node.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `nodeId` | [NodeId](#type-nodeid) | Id of the node to retrieve attributes for. |

**Returns**

| Name | Type | Description |
|---|---|---|
| `attributes` | array of string | An interleaved array of node attribute names and values. |

### DOM.getBoxModel

Returns boxes for the given node.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `nodeId` (optional) | [NodeId](#type-nodeid) | Identifier of the node. |
| `backendNodeId` (optional) | [BackendNodeId](#type-backendnodeid) | Identifier of the backend node. |
| `objectId` (optional) | [Runtime.RemoteObjectId](Runtime.md#type-remoteobjectid) | JavaScript object id of the node wrapper. |

**Returns**

| Name | Type | Description |
|---|---|---|
| `model` | [BoxModel](#type-boxmodel) | Box model for the node. |

### DOM.getContentQuads *(experimental)*

Returns quads that describe node position on the page. This method might return multiple quads for inline nodes.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `nodeId` (optional) | [NodeId](#type-nodeid) | Identifier of the node. |
| `backendNodeId` (optional) | [BackendNodeId](#type-backendnodeid) | Identifier of the backend node. |
| `objectId` (optional) | [Runtime.RemoteObjectId](Runtime.md#type-remoteobjectid) | JavaScript object id of the node wrapper. |

**Returns**

| Name | Type | Description |
|---|---|---|
| `quads` | array of [Quad](#type-quad) | Quads that describe node layout relative to viewport. |

### DOM.getDocument

Returns the root DOM node (and optionally the subtree) to the caller. Implicitly enables the DOM domain events for the current target.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `depth` (optional) | integer | The maximum depth at which children should be retrieved, defaults to 1. Use -1 for the entire subtree or provide an integer larger than 0. |
| `pierce` (optional) | boolean | Whether or not iframes and shadow roots should be traversed when returning the subtree (default is false). |

**Returns**

| Name | Type | Description |
|---|---|---|
| `root` | [Node](#type-node) | Resulting node. |

### DOM.getFlattenedDocument *(deprecated)*

Returns the root DOM node (and optionally the subtree) to the caller. Deprecated, as it is not designed to work well with the rest of the DOM agent. Use DOMSnapshot.captureSnapshot instead.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `depth` (optional) | integer | The maximum depth at which children should be retrieved, defaults to 1. Use -1 for the entire subtree or provide an integer larger than 0. |
| `pierce` (optional) | boolean | Whether or not iframes and shadow roots should be traversed when returning the subtree (default is false). |

**Returns**

| Name | Type | Description |
|---|---|---|
| `nodes` | array of [Node](#type-node) | Resulting node. |

### DOM.getNodesForSubtreeByStyle *(experimental)*

Finds nodes with a given computed style in a subtree.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `nodeId` | [NodeId](#type-nodeid) | Node ID pointing to the root of a subtree. |
| `computedStyles` | array of [CSSComputedStyleProperty](#type-csscomputedstyleproperty) | The style to filter nodes by (includes nodes if any of properties matches). |
| `pierce` (optional) | boolean | Whether or not iframes and shadow roots in the same target should be traversed when returning the results (default is false). |

**Returns**

| Name | Type | Description |
|---|---|---|
| `nodeIds` | array of [NodeId](#type-nodeid) | Resulting nodes. |

### DOM.getNodeForLocation

Returns node id at given location. Depending on whether DOM domain is enabled, nodeId is either returned or not.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `x` | integer | X coordinate. |
| `y` | integer | Y coordinate. |
| `includeUserAgentShadowDOM` (optional) | boolean | False to skip to the nearest non-UA shadow root ancestor (default: false). |
| `ignorePointerEventsNone` (optional) | boolean | Whether to ignore pointer-events: none on elements and hit test them. |

**Returns**

| Name | Type | Description |
|---|---|---|
| `backendNodeId` | [BackendNodeId](#type-backendnodeid) | Resulting node. |
| `frameId` | [Page.FrameId](Page.md#type-frameid) | Frame this node belongs to. |
| `nodeId` (optional) | [NodeId](#type-nodeid) | Id of the node at given coordinates, only when enabled and requested document. |

### DOM.getOuterHTML

Returns node's HTML markup.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `nodeId` (optional) | [NodeId](#type-nodeid) | Identifier of the node. |
| `backendNodeId` (optional) | [BackendNodeId](#type-backendnodeid) | Identifier of the backend node. |
| `objectId` (optional) | [Runtime.RemoteObjectId](Runtime.md#type-remoteobjectid) | JavaScript object id of the node wrapper. |
| `includeShadowDOM` (optional) *(experimental)* | boolean | Include all shadow roots. Equals to false if not specified. |

**Returns**

| Name | Type | Description |
|---|---|---|
| `outerHTML` | string | Outer HTML markup. |

### DOM.getRelayoutBoundary *(experimental)*

Returns the id of the nearest ancestor that is a relayout boundary.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `nodeId` | [NodeId](#type-nodeid) | Id of the node. |

**Returns**

| Name | Type | Description |
|---|---|---|
| `nodeId` | [NodeId](#type-nodeid) | Relayout boundary node id for the given node. |

### DOM.getSearchResults *(experimental)*

Returns search results from given `fromIndex` to given `toIndex` from the search with the given identifier.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `searchId` | string | Unique search session identifier. |
| `fromIndex` | integer | Start index of the search result to be returned. |
| `toIndex` | integer | End index of the search result to be returned. |

**Returns**

| Name | Type | Description |
|---|---|---|
| `nodeIds` | array of [NodeId](#type-nodeid) | Ids of the search result nodes. |

### DOM.hideHighlight

Hides any highlight.

Redirects to `Overlay`.

### DOM.highlightNode

Highlights DOM node.

Redirects to `Overlay`.

### DOM.highlightRect

Highlights given rectangle.

Redirects to `Overlay`.

### DOM.markUndoableState *(experimental)*

Marks last undoable state.

### DOM.moveTo

Moves node into the new container, places it before the given anchor.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `nodeId` | [NodeId](#type-nodeid) | Id of the node to move. |
| `targetNodeId` | [NodeId](#type-nodeid) | Id of the element to drop the moved node into. |
| `insertBeforeNodeId` (optional) | [NodeId](#type-nodeid) | Drop node before this one (if absent, the moved node becomes the last child of `targetNodeId`). |

**Returns**

| Name | Type | Description |
|---|---|---|
| `nodeId` | [NodeId](#type-nodeid) | New id of the moved node. |

### DOM.performSearch *(experimental)*

Searches for a given string in the DOM tree. Use `getSearchResults` to access search results or `cancelSearch` to end this search session.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `query` | string | Plain text or query selector or XPath search query. |
| `includeUserAgentShadowDOM` (optional) | boolean | True to search in user agent shadow DOM. |

**Returns**

| Name | Type | Description |
|---|---|---|
| `searchId` | string | Unique search session identifier. |
| `resultCount` | integer | Number of search results. |

### DOM.pushNodeByPathToFrontend *(experimental)*

Requests that the node is sent to the caller given its path. // FIXME, use XPath

**Parameters**

| Name | Type | Description |
|---|---|---|
| `path` | string | Path to node in the proprietary format. |

**Returns**

| Name | Type | Description |
|---|---|---|
| `nodeId` | [NodeId](#type-nodeid) | Id of the node for given path. |

### DOM.pushNodesByBackendIdsToFrontend *(experimental)*

Requests that a batch of nodes is sent to the caller given their backend node ids.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `backendNodeIds` | array of [BackendNodeId](#type-backendnodeid) | The array of backend node ids. |

**Returns**

| Name | Type | Description |
|---|---|---|
| `nodeIds` | array of [NodeId](#type-nodeid) | The array of ids of pushed nodes that correspond to the backend ids specified in backendNodeIds. |

### DOM.querySelector

Executes `querySelector` on a given node.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `nodeId` | [NodeId](#type-nodeid) | Id of the node to query upon. |
| `selector` | string | Selector string. |

**Returns**

| Name | Type | Description |
|---|---|---|
| `nodeId` | [NodeId](#type-nodeid) | Query selector result. |

### DOM.querySelectorAll

Executes `querySelectorAll` on a given node.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `nodeId` | [NodeId](#type-nodeid) | Id of the node to query upon. |
| `selector` | string | Selector string. |

**Returns**

| Name | Type | Description |
|---|---|---|
| `nodeIds` | array of [NodeId](#type-nodeid) | Query selector result. |

### DOM.getTopLayerElements *(experimental)*

Returns NodeIds of current top layer elements. Top layer is rendered closest to the user within a viewport, therefore its elements always appear on top of all other content.

**Returns**

| Name | Type | Description |
|---|---|---|
| `nodeIds` | array of [NodeId](#type-nodeid) | NodeIds of top layer elements |

### DOM.getElementByRelation *(experimental)*

Returns the NodeId of the matched element according to certain relations.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `nodeId` | [NodeId](#type-nodeid) | Id of the node from which to query the relation. |
| `relation` | enum: `PopoverTarget`, `InterestTarget`, `CommandFor` | Type of relation to get. |

**Returns**

| Name | Type | Description |
|---|---|---|
| `nodeId` | [NodeId](#type-nodeid) | NodeId of the element matching the queried relation. |

### DOM.redo *(experimental)*

Re-does the last undone action.

### DOM.removeAttribute

Removes attribute with given name from an element with given id.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `nodeId` | [NodeId](#type-nodeid) | Id of the element to remove attribute from. |
| `name` | string | Name of the attribute to remove. |

### DOM.removeNode

Removes node with given id.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `nodeId` | [NodeId](#type-nodeid) | Id of the node to remove. |

### DOM.requestChildNodes

Requests that children of the node with given id are returned to the caller in form of `setChildNodes` events where not only immediate children are retrieved, but all children down to the specified depth.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `nodeId` | [NodeId](#type-nodeid) | Id of the node to get children for. |
| `depth` (optional) | integer | The maximum depth at which children should be retrieved, defaults to 1. Use -1 for the entire subtree or provide an integer larger than 0. |
| `pierce` (optional) | boolean | Whether or not iframes and shadow roots should be traversed when returning the sub-tree (default is false). |

### DOM.requestNode

Requests that the node is sent to the caller given the JavaScript node object reference. All nodes that form the path from the node to the root are also sent to the client as a series of `setChildNodes` notifications.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `objectId` | [Runtime.RemoteObjectId](Runtime.md#type-remoteobjectid) | JavaScript object id to convert into node. |

**Returns**

| Name | Type | Description |
|---|---|---|
| `nodeId` | [NodeId](#type-nodeid) | Node id for given object. |

### DOM.resolveNode

Resolves the JavaScript node object for a given NodeId or BackendNodeId.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `nodeId` (optional) | [NodeId](#type-nodeid) | Id of the node to resolve. |
| `backendNodeId` (optional) | [DOM.BackendNodeId](DOM.md#type-backendnodeid) | Backend identifier of the node to resolve. |
| `objectGroup` (optional) | string | Symbolic group name that can be used to release multiple objects. |
| `executionContextId` (optional) | [Runtime.ExecutionContextId](Runtime.md#type-executioncontextid) | Execution context in which to resolve the node. |

**Returns**

| Name | Type | Description |
|---|---|---|
| `object` | [Runtime.RemoteObject](Runtime.md#type-remoteobject) | JavaScript object wrapper for given node. |

### DOM.setAttributeValue

Sets attribute for an element with given id.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `nodeId` | [NodeId](#type-nodeid) | Id of the element to set attribute for. |
| `name` | string | Attribute name. |
| `value` | string | Attribute value. |

### DOM.setAttributesAsText

Sets attributes on element with given id. This method is useful when user edits some existing attribute value and types in several attribute name/value pairs.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `nodeId` | [NodeId](#type-nodeid) | Id of the element to set attributes for. |
| `text` | string | Text with a number of attributes. Will parse this text using HTML parser. |
| `name` (optional) | string | Attribute name to replace with new attributes derived from text in case text parsed successfully. |

### DOM.setFileInputFiles

Sets files for the given file input element.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `files` | array of string | Array of file paths to set. |
| `nodeId` (optional) | [NodeId](#type-nodeid) | Identifier of the node. |
| `backendNodeId` (optional) | [BackendNodeId](#type-backendnodeid) | Identifier of the backend node. |
| `objectId` (optional) | [Runtime.RemoteObjectId](Runtime.md#type-remoteobjectid) | JavaScript object id of the node wrapper. |

### DOM.setNodeStackTracesEnabled *(experimental)*

Sets if stack traces should be captured for Nodes. See `Node.getNodeStackTraces`. Default is disabled.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `enable` | boolean | Enable or disable. |

### DOM.getNodeStackTraces *(experimental)*

Gets stack traces associated with a Node. As of now, only provides stack trace for Node creation.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `nodeId` | [NodeId](#type-nodeid) | Id of the node to get stack traces for. |

**Returns**

| Name | Type | Description |
|---|---|---|
| `creation` (optional) | [Runtime.StackTrace](Runtime.md#type-stacktrace) | Creation stack trace, if available. |

### DOM.getFileInfo *(experimental)*

Returns file information for the given File wrapper.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `objectId` | [Runtime.RemoteObjectId](Runtime.md#type-remoteobjectid) | JavaScript object id of the node wrapper. |

**Returns**

| Name | Type | Description |
|---|---|---|
| `path` | string |  |

### DOM.getDetachedDomNodes *(experimental)*

Returns list of detached nodes

**Returns**

| Name | Type | Description |
|---|---|---|
| `detachedNodes` | array of [DetachedElementInfo](#type-detachedelementinfo) | The list of detached nodes |

### DOM.setInspectedNode *(experimental)*

Enables console to refer to the node with given id via $x (see Command Line API for more details $x functions).

**Parameters**

| Name | Type | Description |
|---|---|---|
| `nodeId` | [NodeId](#type-nodeid) | DOM node id to be accessible by means of $x command line API. |

### DOM.setNodeName

Sets node name for a node with given id.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `nodeId` | [NodeId](#type-nodeid) | Id of the node to set name for. |
| `name` | string | New node's name. |

**Returns**

| Name | Type | Description |
|---|---|---|
| `nodeId` | [NodeId](#type-nodeid) | New node's id. |

### DOM.setNodeValue

Sets node value for a node with given id.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `nodeId` | [NodeId](#type-nodeid) | Id of the node to set value for. |
| `value` | string | New node's value. |

### DOM.setOuterHTML

Sets node HTML markup, returns new node id.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `nodeId` | [NodeId](#type-nodeid) | Id of the node to set markup for. |
| `outerHTML` | string | Outer HTML markup to set. |

### DOM.undo *(experimental)*

Undoes the last performed action.

### DOM.getFrameOwner *(experimental)*

Returns iframe node that owns iframe with the given domain.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `frameId` | [Page.FrameId](Page.md#type-frameid) |  |

**Returns**

| Name | Type | Description |
|---|---|---|
| `backendNodeId` | [BackendNodeId](#type-backendnodeid) | Resulting node. |
| `nodeId` (optional) | [NodeId](#type-nodeid) | Id of the node at given coordinates, only when enabled and requested document. |

### DOM.getContainerForNode *(experimental)*

Returns the query container of the given node based on container query conditions: containerName, physical and logical axes, and whether it queries scroll-state or anchored elements. If no axes are provided and queriesScrollState is false, the style container is returned, which is the direct parent or the closest element with a matching container-name.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `nodeId` | [NodeId](#type-nodeid) |  |
| `containerName` (optional) | string |  |
| `physicalAxes` (optional) | [PhysicalAxes](#type-physicalaxes) |  |
| `logicalAxes` (optional) | [LogicalAxes](#type-logicalaxes) |  |
| `queriesScrollState` (optional) | boolean |  |
| `queriesAnchored` (optional) | boolean |  |

**Returns**

| Name | Type | Description |
|---|---|---|
| `nodeId` (optional) | [NodeId](#type-nodeid) | The container node for the given node, or null if not found. |

### DOM.getQueryingDescendantsForContainer *(experimental)*

Returns the descendants of a container query container that have container queries against this container.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `nodeId` | [NodeId](#type-nodeid) | Id of the container node to find querying descendants from. |

**Returns**

| Name | Type | Description |
|---|---|---|
| `nodeIds` | array of [NodeId](#type-nodeid) | Descendant nodes with container queries against the given container. |

### DOM.getAnchorElement *(experimental)*

Returns the target anchor element of the given anchor query according to https://www.w3.org/TR/css-anchor-position-1/#target.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `nodeId` | [NodeId](#type-nodeid) | Id of the positioned element from which to find the anchor. |
| `anchorSpecifier` (optional) | string | An optional anchor specifier, as defined in https://www.w3.org/TR/css-anchor-position-1/#anchor-specifier. If not provided, it will return the implicit anchor element for the given positioned element. |

**Returns**

| Name | Type | Description |
|---|---|---|
| `nodeId` | [NodeId](#type-nodeid) | The anchor element of the given anchor query. |

### DOM.forceShowPopover *(experimental)*

When enabling, this API force-opens the popover identified by nodeId and keeps it open until disabled.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `nodeId` | [NodeId](#type-nodeid) | Id of the popover HTMLElement |
| `enable` | boolean | If true, opens the popover and keeps it open. If false, closes the popover if it was previously force-opened. |
| `invokerNodeId` (optional) | [BackendNodeId](#type-backendnodeid) | Optional ID of the element invoking this popover, used to establish the implicit anchor. If not provided, it will fall back to the first invoker in the document, preferring elements with a popovertarget attribute over those with a commandfor attribute. Note that if there are multiple invokers, this is just an estimate. |

**Returns**

| Name | Type | Description |
|---|---|---|
| `nodeIds` | array of [NodeId](#type-nodeid) | List of popovers that were closed in order to respect popover stacking order. |

### DOM.getImplicitAnchorCandidates *(experimental)*

Returns candidate nodes that are configured as triggers for the given popover.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `nodeId` | [NodeId](#type-nodeid) | Id of the popover HTMLElement. |

**Returns**

| Name | Type | Description |
|---|---|---|
| `backendNodeIds` | array of [BackendNodeId](#type-backendnodeid) | Candidate elements that can invoke this popover. |

### DOM.forceShowInterest *(experimental)*

When enabling, this API forces an element to gain interest in its target, keeping interest active until disabled.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `nodeId` | [NodeId](#type-nodeid) | Id of the interest invoker HTMLElement. |
| `enable` | boolean | If true, opens and holds interest. If false, releases forced interest. |

### DOM.setTextMarker *(experimental)*

Sets a spelling or grammar error marker on the given range of text. See https://github.com/Igalia/explainers/blob/main/force-spelling-grammar-markers/README.md Note: exactly one between nodeId, backendNodeId and objectId should be passed to identify the node.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `nodeId` (optional) | [NodeId](#type-nodeid) | Identifier of the node. |
| `backendNodeId` (optional) | [BackendNodeId](#type-backendnodeid) | Identifier of the backend node. |
| `objectId` (optional) | [Runtime.RemoteObjectId](Runtime.md#type-remoteobjectid) | JavaScript object id of the node wrapper. |
| `type` | enum: `spelling`, `grammar` | The type of marker to set on the given range of text. |
| `start` | integer | Start offset into the element's rendered text in UTF-16 code units. For a text control, an offset into the control's value. Offsets count text in DOM order and do not enter shadow trees. To mark text inside a shadow tree, pass the element inside the shadow tree. |
| `end` | integer | End offset (exclusive) in the same units and space as start. |

### DOM.clearTextMarkers *(experimental)*

Clears the spelling and grammar error text markers overlapping the ranges set by setTextMarker in this session. These markers are also removed when the DOM domain is disabled or the session ends.

## Events

### DOM.attributeModified

Fired when `Element`'s attribute is modified.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `nodeId` | [NodeId](#type-nodeid) | Id of the node that has changed. |
| `name` | string | Attribute name. |
| `value` | string | Attribute value. |

### DOM.adoptedStyleSheetsModified *(experimental)*

Fired when `Element`'s adoptedStyleSheets are modified.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `nodeId` | [NodeId](#type-nodeid) | Id of the node that has changed. |
| `adoptedStyleSheets` *(experimental)* | array of [StyleSheetId](#type-stylesheetid) | New adoptedStyleSheets array. |

### DOM.attributeRemoved

Fired when `Element`'s attribute is removed.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `nodeId` | [NodeId](#type-nodeid) | Id of the node that has changed. |
| `name` | string | A ttribute name. |

### DOM.characterDataModified

Mirrors `DOMCharacterDataModified` event.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `nodeId` | [NodeId](#type-nodeid) | Id of the node that has changed. |
| `characterData` | string | New text value. |

### DOM.childNodeCountUpdated

Fired when `Container`'s child node count has changed.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `nodeId` | [NodeId](#type-nodeid) | Id of the node that has changed. |
| `childNodeCount` | integer | New node count. |

### DOM.childNodeInserted

Mirrors `DOMNodeInserted` event.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `parentNodeId` | [NodeId](#type-nodeid) | Id of the node that has changed. |
| `previousNodeId` | [NodeId](#type-nodeid) | Id of the previous sibling. |
| `node` | [Node](#type-node) | Inserted node data. |

### DOM.childNodeRemoved

Mirrors `DOMNodeRemoved` event.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `parentNodeId` | [NodeId](#type-nodeid) | Parent id. |
| `nodeId` | [NodeId](#type-nodeid) | Id of the node that has been removed. |

### DOM.distributedNodesUpdated *(experimental)*

Called when distribution is changed.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `insertionPointId` | [NodeId](#type-nodeid) | Insertion point where distributed nodes were updated. |
| `distributedNodes` | array of [BackendNode](#type-backendnode) | Distributed nodes for given insertion point. |

### DOM.documentUpdated

Fired when `Document` has been totally updated. Node ids are no longer valid.

### DOM.inlineStyleInvalidated *(experimental)*

Fired when `Element`'s inline style is modified via a CSS property modification.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `nodeIds` | array of [NodeId](#type-nodeid) | Ids of the nodes for which the inline styles have been invalidated. |

### DOM.pseudoElementAdded *(experimental)*

Called when a pseudo element is added to an element.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `parentId` | [NodeId](#type-nodeid) | Pseudo element's parent element id. |
| `pseudoElement` | [Node](#type-node) | The added pseudo element. |

### DOM.topLayerElementsUpdated *(experimental)*

Called when top layer elements are changed.

### DOM.scrollableFlagUpdated *(experimental)*

Fired when a node's scrollability state changes.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `nodeId` | [DOM.NodeId](DOM.md#type-nodeid) | The id of the node. |
| `isScrollable` | boolean | If the node is scrollable. |

### DOM.adRelatedStateUpdated *(experimental)*

Fired when a node's ad related state changes.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `nodeId` | [DOM.NodeId](DOM.md#type-nodeid) | The id of the node. |
| `adProvenance` (optional) | [Network.AdProvenance](Network.md#type-adprovenance) | The provenance of the ad related node, if it is ad related. |

### DOM.affectedByStartingStylesFlagUpdated *(experimental)*

Fired when a node's starting styles changes.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `nodeId` | [DOM.NodeId](DOM.md#type-nodeid) | The id of the node. |
| `affectedByStartingStyles` | boolean | If the node has starting styles. |

### DOM.pseudoElementRemoved *(experimental)*

Called when a pseudo element is removed from an element.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `parentId` | [NodeId](#type-nodeid) | Pseudo element's parent element id. |
| `pseudoElementId` | [NodeId](#type-nodeid) | The removed pseudo element id. |

### DOM.setChildNodes

Fired when backend wants to provide client with the missing DOM structure. This happens upon most of the calls requesting node ids.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `parentId` | [NodeId](#type-nodeid) | Parent node id to populate with children. |
| `nodes` | array of [Node](#type-node) | Child nodes array. |

### DOM.shadowRootPopped *(experimental)*

Called when shadow root is popped from the element.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `hostId` | [NodeId](#type-nodeid) | Host element id. |
| `rootId` | [NodeId](#type-nodeid) | Shadow root id. |

### DOM.shadowRootPushed *(experimental)*

Called when shadow root is pushed into the element.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `hostId` | [NodeId](#type-nodeid) | Host element id. |
| `root` | [Node](#type-node) | Shadow root. |

## Types

<a id="type-nodeid"></a>
### DOM.NodeId

Type: integer

Unique DOM node identifier.

<a id="type-backendnodeid"></a>
### DOM.BackendNodeId

Type: integer

Unique DOM node identifier used to reference a node that may not have been pushed to the front-end.

<a id="type-stylesheetid"></a>
### DOM.StyleSheetId

Type: string

Unique identifier for a CSS stylesheet.

<a id="type-backendnode"></a>
### DOM.BackendNode

Type: object

Backend node with a friendly name.

**Properties**

| Name | Type | Description |
|---|---|---|
| `nodeType` | integer | `Node`'s nodeType. |
| `nodeName` | string | `Node`'s nodeName. |
| `backendNodeId` | [BackendNodeId](#type-backendnodeid) |  |

<a id="type-pseudotype"></a>
### DOM.PseudoType

Type: string

Pseudo element type.

Allowed values: `first-line`, `first-letter`, `checkmark`, `before`, `after`, `expand-icon`, `picker-icon`, `interest-button`, `marker`, `backdrop`, `column`, `selection`, `search-text`, `target-text`, `spelling-error`, `grammar-error`, `highlight`, `first-line-inherited`, `scroll-marker`, `scroll-marker-group`, `scroll-button`, `scrollbar`, `scrollbar-thumb`, `scrollbar-button`, `scrollbar-track`, `scrollbar-track-piece`, `scrollbar-corner`, `resizer`, `input-list-button`, `view-transition`, `view-transition-group`, `view-transition-image-pair`, `view-transition-group-children`, `view-transition-old`, `view-transition-new`, `placeholder`, `file-selector-button`, `details-content`, `picker`, `select-listbox`, `permission-icon`, `overscroll-area-parent`, `overscroll-backdrop`, `skeleton`

<a id="type-shadowroottype"></a>
### DOM.ShadowRootType

Type: string

Shadow root type.

Allowed values: `user-agent`, `open`, `closed`

<a id="type-compatibilitymode"></a>
### DOM.CompatibilityMode

Type: string

Document compatibility mode.

Allowed values: `QuirksMode`, `LimitedQuirksMode`, `NoQuirksMode`

<a id="type-physicalaxes"></a>
### DOM.PhysicalAxes

Type: string

ContainerSelector physical axes

Allowed values: `Horizontal`, `Vertical`, `Both`

<a id="type-logicalaxes"></a>
### DOM.LogicalAxes

Type: string

ContainerSelector logical axes

Allowed values: `Inline`, `Block`, `Both`

<a id="type-scrollorientation"></a>
### DOM.ScrollOrientation

Type: string

Physical scroll orientation

Allowed values: `horizontal`, `vertical`

<a id="type-node"></a>
### DOM.Node

Type: object

DOM interaction is implemented in terms of mirror objects that represent the actual DOM nodes. DOMNode is a base node mirror type.

**Properties**

| Name | Type | Description |
|---|---|---|
| `nodeId` | [NodeId](#type-nodeid) | Node identifier that is passed into the rest of the DOM messages as the `nodeId`. Backend will only push node with given `id` once. It is aware of all requested nodes and will only fire DOM events for nodes known to the client. |
| `parentId` (optional) | [NodeId](#type-nodeid) | The id of the parent node if any. |
| `backendNodeId` | [BackendNodeId](#type-backendnodeid) | The BackendNodeId for this node. |
| `nodeType` | integer | `Node`'s nodeType. |
| `nodeName` | string | `Node`'s nodeName. |
| `localName` | string | `Node`'s localName. |
| `nodeValue` | string | `Node`'s nodeValue. |
| `childNodeCount` (optional) | integer | Child count for `Container` nodes. |
| `children` (optional) | array of [Node](#type-node) | Child nodes of this node when requested with children. |
| `attributes` (optional) | array of string | Attributes of the `Element` node in the form of flat array `[name1, value1, name2, value2]`. |
| `documentURL` (optional) | string | Document URL that `Document` or `FrameOwner` node points to. |
| `baseURL` (optional) | string | Base URL that `Document` or `FrameOwner` node uses for URL completion. |
| `publicId` (optional) | string | `DocumentType`'s publicId. |
| `systemId` (optional) | string | `DocumentType`'s systemId. |
| `internalSubset` (optional) | string | `DocumentType`'s internalSubset. |
| `xmlVersion` (optional) | string | `Document`'s XML version in case of XML documents. |
| `name` (optional) | string | `Attr`'s name. |
| `value` (optional) | string | `Attr`'s value. |
| `pseudoType` (optional) | [PseudoType](#type-pseudotype) | Pseudo element type for this node. |
| `pseudoIdentifier` (optional) | string | Pseudo element identifier for this node. Only present if there is a valid pseudoType. |
| `shadowRootType` (optional) | [ShadowRootType](#type-shadowroottype) | Shadow root type. |
| `frameId` (optional) | [Page.FrameId](Page.md#type-frameid) | Frame ID for frame owner elements. |
| `contentDocument` (optional) | [Node](#type-node) | Content document for frame owner elements. |
| `shadowRoots` (optional) | array of [Node](#type-node) | Shadow root list for given element host. |
| `templateContent` (optional) | [Node](#type-node) | Content document fragment for template elements. |
| `pseudoElements` (optional) | array of [Node](#type-node) | Pseudo elements associated with this node. |
| `importedDocument` (optional) *(deprecated)* | [Node](#type-node) | Deprecated, as the HTML Imports API has been removed (crbug.com/937746). This property used to return the imported document for the HTMLImport links. The property is always undefined now. |
| `distributedNodes` (optional) | array of [BackendNode](#type-backendnode) | Distributed nodes for given insertion point. |
| `isSVG` (optional) | boolean | Whether the node is SVG. |
| `compatibilityMode` (optional) | [CompatibilityMode](#type-compatibilitymode) |  |
| `assignedSlot` (optional) | [BackendNode](#type-backendnode) |  |
| `isScrollable` (optional) *(experimental)* | boolean |  |
| `affectedByStartingStyles` (optional) *(experimental)* | boolean |  |
| `adoptedStyleSheets` (optional) *(experimental)* | array of [StyleSheetId](#type-stylesheetid) |  |
| `adProvenance` (optional) *(experimental)* | [Network.AdProvenance](Network.md#type-adprovenance) |  |

<a id="type-detachedelementinfo"></a>
### DOM.DetachedElementInfo

Type: object

A structure to hold the top-level node of a detached tree and an array of its retained descendants.

**Properties**

| Name | Type | Description |
|---|---|---|
| `treeNode` | [Node](#type-node) |  |
| `retainedNodeIds` | array of [NodeId](#type-nodeid) |  |

<a id="type-rgba"></a>
### DOM.RGBA

Type: object

A structure holding an RGBA color.

**Properties**

| Name | Type | Description |
|---|---|---|
| `r` | integer | The red component, in the [0-255] range. |
| `g` | integer | The green component, in the [0-255] range. |
| `b` | integer | The blue component, in the [0-255] range. |
| `a` (optional) | number | The alpha component, in the [0-1] range (default: 1). |

<a id="type-quad"></a>
### DOM.Quad

Type: array of number

An array of quad vertices, x immediately followed by y for each point, points clock-wise.

<a id="type-boxmodel"></a>
### DOM.BoxModel

Type: object

Box model.

**Properties**

| Name | Type | Description |
|---|---|---|
| `content` | [Quad](#type-quad) | Content box |
| `padding` | [Quad](#type-quad) | Padding box |
| `border` | [Quad](#type-quad) | Border box |
| `margin` | [Quad](#type-quad) | Margin box |
| `width` | integer | Node width |
| `height` | integer | Node height |
| `shapeOutside` (optional) | [ShapeOutsideInfo](#type-shapeoutsideinfo) | Shape outside coordinates |

<a id="type-shapeoutsideinfo"></a>
### DOM.ShapeOutsideInfo

Type: object

CSS Shape Outside details.

**Properties**

| Name | Type | Description |
|---|---|---|
| `bounds` | [Quad](#type-quad) | Shape bounds |
| `shape` | array of any | Shape coordinate details |
| `marginShape` | array of any | Margin shape bounds |

<a id="type-rect"></a>
### DOM.Rect

Type: object

Rectangle.

**Properties**

| Name | Type | Description |
|---|---|---|
| `x` | number | X coordinate |
| `y` | number | Y coordinate |
| `width` | number | Rectangle width |
| `height` | number | Rectangle height |

<a id="type-csscomputedstyleproperty"></a>
### DOM.CSSComputedStyleProperty

Type: object

**Properties**

| Name | Type | Description |
|---|---|---|
| `name` | string | Computed style property name. |
| `value` | string | Computed style property value. |

