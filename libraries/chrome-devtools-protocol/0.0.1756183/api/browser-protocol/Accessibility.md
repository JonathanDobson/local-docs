# Accessibility domain

Chrome DevTools Protocol, browser protocol (tip-of-tree) (protocol 1.3).

**Experimental**

Depends on: [DOM](DOM.md)

8 methods, 2 events, 10 types.

## Methods

### Accessibility.disable

Disables the accessibility domain.

No parameters.

### Accessibility.enable

Enables the accessibility domain which causes `AXNodeId`s to remain consistent between method calls.
This turns on accessibility for the page, which can impact performance until accessibility is disabled.

No parameters.

### Accessibility.getPartialAXTree

**Experimental**

Fetches the accessibility node and partial accessibility tree for this DOM node, if it exists.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `nodeId` (optional) | [DOM.NodeId](DOM.md#type-nodeid) | Identifier of the node to get the partial accessibility tree for. |
| `backendNodeId` (optional) | [DOM.BackendNodeId](DOM.md#type-backendnodeid) | Identifier of the backend node to get the partial accessibility tree for. |
| `objectId` (optional) | [Runtime.RemoteObjectId](Runtime.md#type-remoteobjectid) | JavaScript object id of the node wrapper to get the partial accessibility tree for. |
| `fetchRelatives` (optional) | boolean | Whether to fetch this node's ancestors, siblings and children. Defaults to true. |

**Return object**

| Name | Type | Description |
|---|---|---|
| `nodes` | array of [Accessibility.AXNode](#type-axnode) | The `Accessibility.AXNode` for this DOM node, if it exists, plus its ancestors, siblings and children, if requested. |

### Accessibility.getFullAXTree

**Experimental**

Fetches the entire accessibility tree for the root Document

**Parameters**

| Name | Type | Description |
|---|---|---|
| `depth` (optional) | integer | The maximum depth at which descendants of the root node should be retrieved. If omitted, the full tree is returned. |
| `frameId` (optional) | [Page.FrameId](Page.md#type-frameid) | The frame for whose document the AX tree should be retrieved. If omitted, the root frame is used. |

**Return object**

| Name | Type | Description |
|---|---|---|
| `nodes` | array of [Accessibility.AXNode](#type-axnode) |  |

### Accessibility.getRootAXNode

**Experimental**

Fetches the root node.
Requires `enable()` to have been called previously.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `frameId` (optional) | [Page.FrameId](Page.md#type-frameid) | The frame in whose document the node resides. If omitted, the root frame is used. |

**Return object**

| Name | Type | Description |
|---|---|---|
| `node` | [Accessibility.AXNode](#type-axnode) |  |

### Accessibility.getAXNodeAndAncestors

**Experimental**

Fetches a node and all ancestors up to and including the root.
Requires `enable()` to have been called previously.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `nodeId` (optional) | [DOM.NodeId](DOM.md#type-nodeid) | Identifier of the node to get. |
| `backendNodeId` (optional) | [DOM.BackendNodeId](DOM.md#type-backendnodeid) | Identifier of the backend node to get. |
| `objectId` (optional) | [Runtime.RemoteObjectId](Runtime.md#type-remoteobjectid) | JavaScript object id of the node wrapper to get. |

**Return object**

| Name | Type | Description |
|---|---|---|
| `nodes` | array of [Accessibility.AXNode](#type-axnode) |  |

### Accessibility.getChildAXNodes

**Experimental**

Fetches a particular accessibility node by AXNodeId.
Requires `enable()` to have been called previously.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `id` | [Accessibility.AXNodeId](#type-axnodeid) |  |
| `frameId` (optional) | [Page.FrameId](Page.md#type-frameid) | The frame in whose document the node resides. If omitted, the root frame is used. |

**Return object**

| Name | Type | Description |
|---|---|---|
| `nodes` | array of [Accessibility.AXNode](#type-axnode) |  |

### Accessibility.queryAXTree

**Experimental**

Query a DOM node's accessibility subtree for accessible name and role.
This command computes the name and role for all nodes in the subtree, including those that are
ignored for accessibility, and returns those that match the specified name and role. If no DOM
node is specified, or the DOM node does not exist, the command returns an error. If neither
`accessibleName` or `role` is specified, it returns all the accessibility nodes in the subtree.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `nodeId` (optional) | [DOM.NodeId](DOM.md#type-nodeid) | Identifier of the node for the root to query. |
| `backendNodeId` (optional) | [DOM.BackendNodeId](DOM.md#type-backendnodeid) | Identifier of the backend node for the root to query. |
| `objectId` (optional) | [Runtime.RemoteObjectId](Runtime.md#type-remoteobjectid) | JavaScript object id of the node wrapper for the root to query. |
| `accessibleName` (optional) | string | Find nodes with this computed name. |
| `role` (optional) | string | Find nodes with this computed role. |

**Return object**

| Name | Type | Description |
|---|---|---|
| `nodes` | array of [Accessibility.AXNode](#type-axnode) | A list of `Accessibility.AXNode` matching the specified attributes, including nodes that are ignored for accessibility. |

## Events

### Accessibility.loadComplete

**Experimental**

The loadComplete event mirrors the load complete event sent by the browser to assistive
technology when the web page has finished loading.

**Event parameters**

| Name | Type | Description |
|---|---|---|
| `root` | [Accessibility.AXNode](#type-axnode) | New document root node. |

### Accessibility.nodesUpdated

**Experimental**

The nodesUpdated event is sent every time a previously requested node has changed the in tree.

**Event parameters**

| Name | Type | Description |
|---|---|---|
| `nodes` | array of [Accessibility.AXNode](#type-axnode) | Updated node data. |

## Types

<a id="type-axnodeid"></a>
### Accessibility.AXNodeId

Unique accessibility node identifier.

Type: string

<a id="type-axvaluetype"></a>
### Accessibility.AXValueType

Enum of possible property types.

Type: string

Allowed values: `boolean`, `tristate`, `booleanOrUndefined`, `idref`, `idrefList`, `integer`, `node`, `nodeList`, `number`, `string`, `computedString`, `token`, `tokenList`, `domRelation`, `role`, `internalRole`, `valueUndefined`

<a id="type-axvaluesourcetype"></a>
### Accessibility.AXValueSourceType

Enum of possible property sources.

Type: string

Allowed values: `attribute`, `implicit`, `style`, `contents`, `placeholder`, `relatedElement`

<a id="type-axvaluenativesourcetype"></a>
### Accessibility.AXValueNativeSourceType

Enum of possible native property sources (as a subtype of a particular AXValueSourceType).

Type: string

Allowed values: `description`, `figcaption`, `label`, `labelfor`, `labelwrapped`, `legend`, `rubyannotation`, `tablecaption`, `title`, `other`

<a id="type-axvaluesource"></a>
### Accessibility.AXValueSource

A single source for a computed AX property.

Type: object

**Properties**

| Name | Type | Description |
|---|---|---|
| `type` | [Accessibility.AXValueSourceType](#type-axvaluesourcetype) | What type of source this is. |
| `value` (optional) | [Accessibility.AXValue](#type-axvalue) | The value of this property source. |
| `attribute` (optional) | string | The name of the relevant attribute, if any. |
| `attributeValue` (optional) | [Accessibility.AXValue](#type-axvalue) | The value of the relevant attribute, if any. |
| `superseded` (optional) | boolean | Whether this source is superseded by a higher priority source. |
| `nativeSource` (optional) | [Accessibility.AXValueNativeSourceType](#type-axvaluenativesourcetype) | The native markup source for this value, e.g. a `<label>` element. |
| `nativeSourceValue` (optional) | [Accessibility.AXValue](#type-axvalue) | The value, such as a node or node list, of the native source. |
| `invalid` (optional) | boolean | Whether the value for this property is invalid. |
| `invalidReason` (optional) | string | Reason for the value being invalid, if it is. |

<a id="type-axrelatednode"></a>
### Accessibility.AXRelatedNode

Type: object

**Properties**

| Name | Type | Description |
|---|---|---|
| `backendDOMNodeId` | [DOM.BackendNodeId](DOM.md#type-backendnodeid) | The BackendNodeId of the related DOM node. |
| `idref` (optional) | string | The IDRef value provided, if any. |
| `text` (optional) | string | The text alternative of this node in the current context. |

<a id="type-axproperty"></a>
### Accessibility.AXProperty

Type: object

**Properties**

| Name | Type | Description |
|---|---|---|
| `name` | [Accessibility.AXPropertyName](#type-axpropertyname) | The name of this property. |
| `value` | [Accessibility.AXValue](#type-axvalue) | The value of this property. |

<a id="type-axvalue"></a>
### Accessibility.AXValue

A single computed AX property.

Type: object

**Properties**

| Name | Type | Description |
|---|---|---|
| `type` | [Accessibility.AXValueType](#type-axvaluetype) | The type of this value. |
| `value` (optional) | any | The computed value of this property. |
| `relatedNodes` (optional) | array of [Accessibility.AXRelatedNode](#type-axrelatednode) | One or more related nodes, if applicable. |
| `sources` (optional) | array of [Accessibility.AXValueSource](#type-axvaluesource) | The sources which contributed to the computation of this property. |

<a id="type-axpropertyname"></a>
### Accessibility.AXPropertyName

Values of AXProperty name:
- from 'busy' to 'roledescription': states which apply to every AX node
- from 'live' to 'root': attributes which apply to nodes in live regions
- from 'autocomplete' to 'valuetext': attributes which apply to widgets
- from 'checked' to 'selected': states which apply to widgets
- from 'activedescendant' to 'owns': relationships between elements other than parent/child/sibling
- from 'activeFullscreenElement' to 'uninteresting': reasons why this noode is hidden

Type: string

Allowed values: `actions`, `busy`, `disabled`, `editable`, `focusable`, `focused`, `hidden`, `hiddenRoot`, `invalid`, `keyshortcuts`, `settable`, `roledescription`, `live`, `atomic`, `relevant`, `root`, `autocomplete`, `hasPopup`, `level`, `multiselectable`, `orientation`, `multiline`, `readonly`, `required`, `valuemin`, `valuemax`, `valuetext`, `checked`, `expanded`, `modal`, `pressed`, `selected`, `activedescendant`, `controls`, `describedby`, `details`, `errormessage`, `flowto`, `labelledby`, `owns`, `url`, `activeFullscreenElement`, `activeModalDialog`, `activeAriaModalDialog`, `ariaHiddenElement`, `ariaHiddenSubtree`, `emptyAlt`, `emptyText`, `inertElement`, `inertSubtree`, `labelContainer`, `labelFor`, `notRendered`, `notVisible`, `presentationalRole`, `probablyPresentational`, `inactiveCarouselTabContent`, `uninteresting`

<a id="type-axnode"></a>
### Accessibility.AXNode

A node in the accessibility tree.

Type: object

**Properties**

| Name | Type | Description |
|---|---|---|
| `nodeId` | [Accessibility.AXNodeId](#type-axnodeid) | Unique identifier for this node. |
| `ignored` | boolean | Whether this node is ignored for accessibility |
| `ignoredReasons` (optional) | array of [Accessibility.AXProperty](#type-axproperty) | Collection of reasons why this node is hidden. |
| `role` (optional) | [Accessibility.AXValue](#type-axvalue) | This `Node`'s role, whether explicit or implicit. |
| `chromeRole` (optional) | [Accessibility.AXValue](#type-axvalue) | This `Node`'s Chrome raw role. |
| `name` (optional) | [Accessibility.AXValue](#type-axvalue) | The accessible name for this `Node`. |
| `description` (optional) | [Accessibility.AXValue](#type-axvalue) | The accessible description for this `Node`. |
| `value` (optional) | [Accessibility.AXValue](#type-axvalue) | The value for this `Node`. |
| `properties` (optional) | array of [Accessibility.AXProperty](#type-axproperty) | All other properties |
| `parentId` (optional) | [Accessibility.AXNodeId](#type-axnodeid) | ID for this node's parent. |
| `childIds` (optional) | array of [Accessibility.AXNodeId](#type-axnodeid) | IDs for each of this node's child nodes. |
| `backendDOMNodeId` (optional) | [DOM.BackendNodeId](DOM.md#type-backendnodeid) | The backend ID for the associated DOM node, if any. |
| `frameId` (optional) | [Page.FrameId](Page.md#type-frameid) | The frame ID for the frame associated with this nodes document. |
