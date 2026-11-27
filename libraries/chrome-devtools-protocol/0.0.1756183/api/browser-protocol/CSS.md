# CSS domain

Chrome DevTools Protocol, browser protocol (tip-of-tree) (protocol 1.3).

**Experimental**

This domain exposes CSS read/write operations. All CSS objects (stylesheets, rules, and styles)
have an associated `id` used in subsequent operations on the related object. Each object type has
a specific `id` structure, and those are not interchangeable between objects of different kinds.
CSS objects can be loaded using the `get*ForNode()` calls (which accept a DOM node id). A client
can also keep track of stylesheets via the `styleSheetAdded`/`styleSheetRemoved` events and
subsequently load the required stylesheet contents using the `getStyleSheet[Text]()` methods.

Depends on: [DOM](DOM.md), [Page](Page.md)

40 methods, 6 events, 46 types.

## Methods

### CSS.addRule

Inserts a new rule with the given `ruleText` in a stylesheet with given `styleSheetId`, at the
position specified by `location`.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `styleSheetId` | [DOM.StyleSheetId](DOM.md#type-stylesheetid) | The css style sheet identifier where a new rule should be inserted. |
| `ruleText` | string | The text of a new rule. |
| `location` | [CSS.SourceRange](#type-sourcerange) | Text position of a new rule in the target style sheet. |
| `nodeForPropertySyntaxValidation` (optional) | [DOM.NodeId](DOM.md#type-nodeid) | **Experimental** NodeId for the DOM node in whose context custom property declarations for registered properties should be validated. If omitted, declarations in the new rule text can only be validated statically, which may produce incorrect results if the declaration contains a var() for example. |

**Return object**

| Name | Type | Description |
|---|---|---|
| `rule` | [CSS.CSSRule](#type-cssrule) | The newly created rule. |

### CSS.collectClassNames

Returns all class names from specified stylesheet.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `styleSheetId` | [DOM.StyleSheetId](DOM.md#type-stylesheetid) |  |

**Return object**

| Name | Type | Description |
|---|---|---|
| `classNames` | array of string | Class name list. |

### CSS.createStyleSheet

Creates a new special "via-inspector" stylesheet in the frame with given `frameId`.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `frameId` | [Page.FrameId](Page.md#type-frameid) | Identifier of the frame where "via-inspector" stylesheet should be created. |
| `force` (optional) | boolean | If true, creates a new stylesheet for every call. If false, returns a stylesheet previously created by a call with force=false for the frame's document if it exists or creates a new stylesheet (default: false). |

**Return object**

| Name | Type | Description |
|---|---|---|
| `styleSheetId` | [DOM.StyleSheetId](DOM.md#type-stylesheetid) | Identifier of the created "via-inspector" stylesheet. |

### CSS.disable

Disables the CSS agent for the given page.

No parameters.

### CSS.enable

Enables the CSS agent for the given page. Clients should not assume that the CSS agent has been
enabled until the result of this command is received.

No parameters.

### CSS.forcePseudoState

Ensures that the given node will have specified pseudo-classes whenever its style is computed by
the browser.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `nodeId` | [DOM.NodeId](DOM.md#type-nodeid) | The element id for which to force the pseudo state. |
| `forcedPseudoClasses` | array of string | Element pseudo classes to force when computing the element's style. |

### CSS.forceStartingStyle

Ensures that the given node is in its starting-style state.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `nodeId` | [DOM.NodeId](DOM.md#type-nodeid) | The element id for which to force the starting-style state. |
| `forced` | boolean | Boolean indicating if this is on or off. |

### CSS.forcePositionTryOption

Forces a position-try option for the given node.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `nodeId` | [DOM.NodeId](DOM.md#type-nodeid) | The element id for which to force the position-try option. |
| `index` (optional) | integer | The 1-based index of the position-try fallback option, 0 for base position (no fallback), or omitted to clear the forced state. |

### CSS.getBackgroundColors

**Parameters**

| Name | Type | Description |
|---|---|---|
| `nodeId` | [DOM.NodeId](DOM.md#type-nodeid) | Id of the node to get background colors for. |

**Return object**

| Name | Type | Description |
|---|---|---|
| `backgroundColors` (optional) | array of string | The range of background colors behind this element, if it contains any visible text. If no visible text is present, this will be undefined. In the case of a flat background color, this will consist of simply that color. In the case of a gradient, this will consist of each of the color stops. For anything more complicated, this will be an empty array. Images will be ignored (as if the image had failed to load). |
| `computedFontSize` (optional) | string | The computed font size for this node, as a CSS computed value string (e.g. '12px'). |
| `computedFontWeight` (optional) | string | The computed font weight for this node, as a CSS computed value string (e.g. 'normal' or '100'). |

### CSS.getComputedStyleForNode

Returns the computed style for a DOM node identified by `nodeId`.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `nodeId` | [DOM.NodeId](DOM.md#type-nodeid) |  |

**Return object**

| Name | Type | Description |
|---|---|---|
| `computedStyle` | array of [CSS.CSSComputedStyleProperty](#type-csscomputedstyleproperty) | Computed style for the specified DOM node. |
| `extraFields` | [CSS.ComputedStyleExtraFields](#type-computedstyleextrafields) | **Experimental** A list of non-standard "extra fields" which blink stores alongside each computed style. |

### CSS.resolveValues

**Experimental**

Resolve the specified values in the context of the provided element.
For example, a value of '1em' is evaluated according to the computed
'font-size' of the element and a value 'calc(1px + 2px)' will be
resolved to '3px'.
If the `propertyName` was specified the `values` are resolved as if
they were property's declaration. If a value cannot be parsed according
to the provided property syntax, the value is parsed using combined
syntax as if null `propertyName` was provided. If the value cannot be
resolved even then, return the provided value without any changes.
Note: this function currently does not resolve CSS random() function,
it returns unmodified random() function parts.`

**Parameters**

| Name | Type | Description |
|---|---|---|
| `values` | array of string | Cascade-dependent keywords (revert/revert-layer) do not work. |
| `nodeId` | [DOM.NodeId](DOM.md#type-nodeid) | Id of the node in whose context the expression is evaluated |
| `propertyName` (optional) | string | Only longhands and custom property names are accepted. |
| `pseudoType` (optional) | [DOM.PseudoType](DOM.md#type-pseudotype) | Pseudo element type, only works for pseudo elements that generate elements in the tree, such as ::before and ::after. |
| `pseudoIdentifier` (optional) | string | Pseudo element custom ident. |

**Return object**

| Name | Type | Description |
|---|---|---|
| `results` | array of string |  |

### CSS.getLonghandProperties

**Experimental**

**Parameters**

| Name | Type | Description |
|---|---|---|
| `shorthandName` | string |  |
| `value` | string |  |

**Return object**

| Name | Type | Description |
|---|---|---|
| `longhandProperties` | array of [CSS.CSSProperty](#type-cssproperty) |  |

### CSS.getInlineStylesForNode

Returns the styles defined inline (explicitly in the "style" attribute and implicitly, using DOM
attributes) for a DOM node identified by `nodeId`.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `nodeId` | [DOM.NodeId](DOM.md#type-nodeid) |  |

**Return object**

| Name | Type | Description |
|---|---|---|
| `inlineStyle` (optional) | [CSS.CSSStyle](#type-cssstyle) | Inline style for the specified DOM node. |
| `attributesStyle` (optional) | [CSS.CSSStyle](#type-cssstyle) | Attribute-defined element style (e.g. resulting from "width=20 height=100%"). |

### CSS.getAnimatedStylesForNode

**Experimental**

Returns the styles coming from animations & transitions
including the animation & transition styles coming from inheritance chain.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `nodeId` | [DOM.NodeId](DOM.md#type-nodeid) |  |

**Return object**

| Name | Type | Description |
|---|---|---|
| `animationStyles` (optional) | array of [CSS.CSSAnimationStyle](#type-cssanimationstyle) | Styles coming from animations. |
| `transitionsStyle` (optional) | [CSS.CSSStyle](#type-cssstyle) | Style coming from transitions. |
| `inherited` (optional) | array of [CSS.InheritedAnimatedStyleEntry](#type-inheritedanimatedstyleentry) | Inherited style entries for animationsStyle and transitionsStyle from the inheritance chain of the element. |

### CSS.getMatchedStylesForNode

Returns requested styles for a DOM node identified by `nodeId`.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `nodeId` | [DOM.NodeId](DOM.md#type-nodeid) |  |

**Return object**

| Name | Type | Description |
|---|---|---|
| `inlineStyle` (optional) | [CSS.CSSStyle](#type-cssstyle) | Inline style for the specified DOM node. |
| `attributesStyle` (optional) | [CSS.CSSStyle](#type-cssstyle) | Attribute-defined element style (e.g. resulting from "width=20 height=100%"). |
| `matchedCSSRules` (optional) | array of [CSS.RuleMatch](#type-rulematch) | CSS rules matching this node, from all applicable stylesheets. |
| `pseudoElements` (optional) | array of [CSS.PseudoElementMatches](#type-pseudoelementmatches) | Pseudo style matches for this node. |
| `inherited` (optional) | array of [CSS.InheritedStyleEntry](#type-inheritedstyleentry) | A chain of inherited styles (from the immediate node parent up to the DOM tree root). |
| `inheritedPseudoElements` (optional) | array of [CSS.InheritedPseudoElementMatches](#type-inheritedpseudoelementmatches) | A chain of inherited pseudo element styles (from the immediate node parent up to the DOM tree root). |
| `cssKeyframesRules` (optional) | array of [CSS.CSSKeyframesRule](#type-csskeyframesrule) | A list of CSS keyframed animations matching this node. |
| `cssPositionTryRules` (optional) | array of [CSS.CSSPositionTryRule](#type-csspositiontryrule) | A list of CSS @position-try rules matching this node, based on the position-try-fallbacks property. |
| `activePositionFallbackIndex` (optional) | integer | Index of the active fallback in the applied position-try-fallback property, will not be set if there is no active position-try fallback. |
| `cssPropertyRules` (optional) | array of [CSS.CSSPropertyRule](#type-csspropertyrule) | A list of CSS at-property rules matching this node. |
| `cssPropertyRegistrations` (optional) | array of [CSS.CSSPropertyRegistration](#type-csspropertyregistration) | A list of CSS property registrations matching this node. |
| `cssAtRules` (optional) | array of [CSS.CSSAtRule](#type-cssatrule) | A list of simple @rules matching this node or its pseudo-elements. |
| `parentLayoutNodeId` (optional) | [DOM.NodeId](DOM.md#type-nodeid) | **Experimental** Id of the first parent element that does not have display: contents. |
| `cssFunctionRules` (optional) | array of [CSS.CSSFunctionRule](#type-cssfunctionrule) | **Experimental** A list of CSS at-function rules referenced by styles of this node. |

### CSS.getEnvironmentVariables

**Experimental**

Returns the values of the default UA-defined environment variables used in env()

No parameters.

**Return object**

| Name | Type | Description |
|---|---|---|
| `environmentVariables` | object |  |

### CSS.getMediaQueries

Returns all media queries parsed by the rendering engine.

No parameters.

**Return object**

| Name | Type | Description |
|---|---|---|
| `medias` | array of [CSS.CSSMedia](#type-cssmedia) |  |

### CSS.getPlatformFontsForNode

Requests information about platform fonts which we used to render child TextNodes in the given
node.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `nodeId` | [DOM.NodeId](DOM.md#type-nodeid) |  |

**Return object**

| Name | Type | Description |
|---|---|---|
| `fonts` | array of [CSS.PlatformFontUsage](#type-platformfontusage) | Usage statistics for every employed platform font. |

### CSS.getStyleSheetText

Returns the current textual content for a stylesheet.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `styleSheetId` | [DOM.StyleSheetId](DOM.md#type-stylesheetid) |  |

**Return object**

| Name | Type | Description |
|---|---|---|
| `text` | string | The stylesheet text. |

### CSS.getLayersForNode

**Experimental**

Returns all layers parsed by the rendering engine for the tree scope of a node.
Given a DOM element identified by nodeId, getLayersForNode returns the root
layer for the nearest ancestor document or shadow root. The layer root contains
the full layer tree for the tree scope and their ordering.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `nodeId` | [DOM.NodeId](DOM.md#type-nodeid) |  |

**Return object**

| Name | Type | Description |
|---|---|---|
| `rootLayer` | [CSS.CSSLayerData](#type-csslayerdata) |  |

### CSS.getLocationForSelector

**Experimental**

Given a CSS selector text and a style sheet ID, getLocationForSelector
returns an array of locations of the CSS selector in the style sheet.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `styleSheetId` | [DOM.StyleSheetId](DOM.md#type-stylesheetid) |  |
| `selectorText` | string |  |

**Return object**

| Name | Type | Description |
|---|---|---|
| `ranges` | array of [CSS.SourceRange](#type-sourcerange) |  |

### CSS.trackComputedStyleUpdatesForNode

**Experimental**

Starts tracking the given node for the computed style updates
and whenever the computed style is updated for node, it queues
a `computedStyleUpdated` event with throttling.
There can only be 1 node tracked for computed style updates
so passing a new node id removes tracking from the previous node.
Pass `undefined` to disable tracking.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `nodeId` (optional) | [DOM.NodeId](DOM.md#type-nodeid) |  |

### CSS.trackComputedStyleUpdates

**Experimental**

Starts tracking the given computed styles for updates. The specified array of properties
replaces the one previously specified. Pass empty array to disable tracking.
Use takeComputedStyleUpdates to retrieve the list of nodes that had properties modified.
The changes to computed style properties are only tracked for nodes pushed to the front-end
by the DOM agent. If no changes to the tracked properties occur after the node has been pushed
to the front-end, no updates will be issued for the node.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `propertiesToTrack` | array of [CSS.CSSComputedStyleProperty](#type-csscomputedstyleproperty) |  |

### CSS.takeComputedStyleUpdates

**Experimental**

Polls the next batch of computed style updates.

No parameters.

**Return object**

| Name | Type | Description |
|---|---|---|
| `nodeIds` | array of [DOM.NodeId](DOM.md#type-nodeid) | The list of node Ids that have their tracked computed styles updated. |

### CSS.setEffectivePropertyValueForNode

Find a rule with the given active property for the given node and set the new value for this
property

**Parameters**

| Name | Type | Description |
|---|---|---|
| `nodeId` | [DOM.NodeId](DOM.md#type-nodeid) | The element id for which to set property. |
| `propertyName` | string |  |
| `value` | string |  |

### CSS.setPropertyRulePropertyName

Modifies the property rule property name.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `styleSheetId` | [DOM.StyleSheetId](DOM.md#type-stylesheetid) |  |
| `range` | [CSS.SourceRange](#type-sourcerange) |  |
| `propertyName` | string |  |

**Return object**

| Name | Type | Description |
|---|---|---|
| `propertyName` | [CSS.Value](#type-value) | The resulting key text after modification. |

### CSS.setKeyframeKey

Modifies the keyframe rule key text.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `styleSheetId` | [DOM.StyleSheetId](DOM.md#type-stylesheetid) |  |
| `range` | [CSS.SourceRange](#type-sourcerange) |  |
| `keyText` | string |  |

**Return object**

| Name | Type | Description |
|---|---|---|
| `keyText` | [CSS.Value](#type-value) | The resulting key text after modification. |

### CSS.setMediaText

Modifies the rule selector.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `styleSheetId` | [DOM.StyleSheetId](DOM.md#type-stylesheetid) |  |
| `range` | [CSS.SourceRange](#type-sourcerange) |  |
| `text` | string |  |

**Return object**

| Name | Type | Description |
|---|---|---|
| `media` | [CSS.CSSMedia](#type-cssmedia) | The resulting CSS media rule after modification. |

### CSS.setContainerQueryText

**Experimental** · **Deprecated**

Modifies the expression of a container query.
Deprecated. Use setContainerQueryConditionText instead.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `styleSheetId` | [DOM.StyleSheetId](DOM.md#type-stylesheetid) |  |
| `range` | [CSS.SourceRange](#type-sourcerange) |  |
| `text` | string |  |

**Return object**

| Name | Type | Description |
|---|---|---|
| `containerQuery` | [CSS.CSSContainerQuery](#type-csscontainerquery) | The resulting CSS container query rule after modification. |

### CSS.setContainerQueryConditionText

**Experimental**

**Parameters**

| Name | Type | Description |
|---|---|---|
| `styleSheetId` | [DOM.StyleSheetId](DOM.md#type-stylesheetid) |  |
| `range` | [CSS.SourceRange](#type-sourcerange) |  |
| `text` | string |  |

**Return object**

| Name | Type | Description |
|---|---|---|
| `containerQuery` | [CSS.CSSContainerQuery](#type-csscontainerquery) | The resulting CSS container query rule after modification. |

### CSS.setSupportsText

**Experimental**

Modifies the expression of a supports at-rule.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `styleSheetId` | [DOM.StyleSheetId](DOM.md#type-stylesheetid) |  |
| `range` | [CSS.SourceRange](#type-sourcerange) |  |
| `text` | string |  |

**Return object**

| Name | Type | Description |
|---|---|---|
| `supports` | [CSS.CSSSupports](#type-csssupports) | The resulting CSS Supports rule after modification. |

### CSS.setNavigationText

**Experimental**

Modifies the expression of a navigation at-rule.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `styleSheetId` | [DOM.StyleSheetId](DOM.md#type-stylesheetid) |  |
| `range` | [CSS.SourceRange](#type-sourcerange) |  |
| `text` | string |  |

**Return object**

| Name | Type | Description |
|---|---|---|
| `navigation` | [CSS.CSSNavigation](#type-cssnavigation) | The resulting CSS Navigation rule after modification. |

### CSS.setScopeText

**Experimental**

Modifies the expression of a scope at-rule.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `styleSheetId` | [DOM.StyleSheetId](DOM.md#type-stylesheetid) |  |
| `range` | [CSS.SourceRange](#type-sourcerange) |  |
| `text` | string |  |

**Return object**

| Name | Type | Description |
|---|---|---|
| `scope` | [CSS.CSSScope](#type-cssscope) | The resulting CSS Scope rule after modification. |

### CSS.setRuleSelector

Modifies the rule selector.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `styleSheetId` | [DOM.StyleSheetId](DOM.md#type-stylesheetid) |  |
| `range` | [CSS.SourceRange](#type-sourcerange) |  |
| `selector` | string |  |

**Return object**

| Name | Type | Description |
|---|---|---|
| `selectorList` | [CSS.SelectorList](#type-selectorlist) | The resulting selector list after modification. |

### CSS.setStyleSheetText

Sets the new stylesheet text.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `styleSheetId` | [DOM.StyleSheetId](DOM.md#type-stylesheetid) |  |
| `text` | string |  |

**Return object**

| Name | Type | Description |
|---|---|---|
| `sourceMapURL` (optional) | string | URL of source map associated with script (if any). |

### CSS.setStyleTexts

Applies specified style edits one after another in the given order.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `edits` | array of [CSS.StyleDeclarationEdit](#type-styledeclarationedit) |  |
| `nodeForPropertySyntaxValidation` (optional) | [DOM.NodeId](DOM.md#type-nodeid) | **Experimental** NodeId for the DOM node in whose context custom property declarations for registered properties should be validated. If omitted, declarations in the new rule text can only be validated statically, which may produce incorrect results if the declaration contains a var() for example. |

**Return object**

| Name | Type | Description |
|---|---|---|
| `styles` | array of [CSS.CSSStyle](#type-cssstyle) | The resulting styles after modification. |

### CSS.startRuleUsageTracking

Enables the selector recording.

No parameters.

### CSS.stopRuleUsageTracking

Stop tracking rule usage and return the list of rules that were used since last call to
`takeCoverageDelta` (or since start of coverage instrumentation).

No parameters.

**Return object**

| Name | Type | Description |
|---|---|---|
| `ruleUsage` | array of [CSS.RuleUsage](#type-ruleusage) |  |

### CSS.takeCoverageDelta

Obtain list of rules that became used since last call to this method (or since start of coverage
instrumentation).

No parameters.

**Return object**

| Name | Type | Description |
|---|---|---|
| `coverage` | array of [CSS.RuleUsage](#type-ruleusage) |  |
| `timestamp` | number | Monotonically increasing time, in seconds. |

### CSS.setLocalFontsEnabled

**Experimental**

Enables/disables rendering of local CSS fonts (enabled by default).

**Parameters**

| Name | Type | Description |
|---|---|---|
| `enabled` | boolean | Whether rendering of local fonts is enabled. |

## Events

### CSS.fontsUpdated

Fires whenever a web font is updated.  A non-empty font parameter indicates a successfully loaded
web font.

**Event parameters**

| Name | Type | Description |
|---|---|---|
| `font` (optional) | [CSS.FontFace](#type-fontface) | The web font that has loaded. |

### CSS.mediaQueryResultChanged

Fires whenever a MediaQuery result changes (for example, after a browser window has been
resized.) The current implementation considers only viewport-dependent media features.

### CSS.styleSheetAdded

Fired whenever an active document stylesheet is added.

**Event parameters**

| Name | Type | Description |
|---|---|---|
| `header` | [CSS.CSSStyleSheetHeader](#type-cssstylesheetheader) | Added stylesheet metainfo. |

### CSS.styleSheetChanged

Fired whenever a stylesheet is changed as a result of the client operation.

**Event parameters**

| Name | Type | Description |
|---|---|---|
| `styleSheetId` | [DOM.StyleSheetId](DOM.md#type-stylesheetid) |  |

### CSS.styleSheetRemoved

Fired whenever an active document stylesheet is removed.

**Event parameters**

| Name | Type | Description |
|---|---|---|
| `styleSheetId` | [DOM.StyleSheetId](DOM.md#type-stylesheetid) | Identifier of the removed stylesheet. |

### CSS.computedStyleUpdated

**Experimental**

**Event parameters**

| Name | Type | Description |
|---|---|---|
| `nodeId` | [DOM.NodeId](DOM.md#type-nodeid) | The node id that has updated computed styles. |

## Types

<a id="type-stylesheetorigin"></a>
### CSS.StyleSheetOrigin

Stylesheet type: "injected" for stylesheets injected via extension, "user-agent" for user-agent
stylesheets, "inspector" for stylesheets created by the inspector (i.e. those holding the "via
inspector" rules), "regular" for regular stylesheets.

Type: string

Allowed values: `injected`, `user-agent`, `inspector`, `regular`

<a id="type-pseudoelementmatches"></a>
### CSS.PseudoElementMatches

CSS rule collection for a single pseudo style.

Type: object

**Properties**

| Name | Type | Description |
|---|---|---|
| `pseudoType` | [DOM.PseudoType](DOM.md#type-pseudotype) | Pseudo element type. |
| `pseudoIdentifier` (optional) | string | Pseudo element custom ident. |
| `matches` | array of [CSS.RuleMatch](#type-rulematch) | Matches of CSS rules applicable to the pseudo style. |

<a id="type-cssanimationstyle"></a>
### CSS.CSSAnimationStyle

CSS style coming from animations with the name of the animation.

Type: object

**Properties**

| Name | Type | Description |
|---|---|---|
| `name` (optional) | string | The name of the animation. |
| `style` | [CSS.CSSStyle](#type-cssstyle) | The style coming from the animation. |

<a id="type-inheritedstyleentry"></a>
### CSS.InheritedStyleEntry

Inherited CSS rule collection from ancestor node.

Type: object

**Properties**

| Name | Type | Description |
|---|---|---|
| `inlineStyle` (optional) | [CSS.CSSStyle](#type-cssstyle) | The ancestor node's inline style, if any, in the style inheritance chain. |
| `matchedCSSRules` | array of [CSS.RuleMatch](#type-rulematch) | Matches of CSS rules matching the ancestor node in the style inheritance chain. |

<a id="type-inheritedanimatedstyleentry"></a>
### CSS.InheritedAnimatedStyleEntry

Inherited CSS style collection for animated styles from ancestor node.

Type: object

**Properties**

| Name | Type | Description |
|---|---|---|
| `animationStyles` (optional) | array of [CSS.CSSAnimationStyle](#type-cssanimationstyle) | Styles coming from the animations of the ancestor, if any, in the style inheritance chain. |
| `transitionsStyle` (optional) | [CSS.CSSStyle](#type-cssstyle) | The style coming from the transitions of the ancestor, if any, in the style inheritance chain. |

<a id="type-inheritedpseudoelementmatches"></a>
### CSS.InheritedPseudoElementMatches

Inherited pseudo element matches from pseudos of an ancestor node.

Type: object

**Properties**

| Name | Type | Description |
|---|---|---|
| `pseudoElements` | array of [CSS.PseudoElementMatches](#type-pseudoelementmatches) | Matches of pseudo styles from the pseudos of an ancestor node. |

<a id="type-rulematch"></a>
### CSS.RuleMatch

Match data for a CSS rule.

Type: object

**Properties**

| Name | Type | Description |
|---|---|---|
| `rule` | [CSS.CSSRule](#type-cssrule) | CSS rule in the match. |
| `matchingSelectors` | array of integer | Matching selector indices in the rule's selectorList selectors (0-based). |

<a id="type-value"></a>
### CSS.Value

Data for a simple selector (these are delimited by commas in a selector list).

Type: object

**Properties**

| Name | Type | Description |
|---|---|---|
| `text` | string | Value text. |
| `range` (optional) | [CSS.SourceRange](#type-sourcerange) | Value range in the underlying resource (if available). |
| `specificity` (optional) | [CSS.Specificity](#type-specificity) | **Experimental** Specificity of the selector. |

<a id="type-specificitycomponent"></a>
### CSS.SpecificityComponent

**Experimental**

Contribution of an individual simple selector to specificity.

Type: object

**Properties**

| Name | Type | Description |
|---|---|---|
| `text` | string | The simple selector text that contributes to specificity. |
| `a` | integer | The a component contribution. |
| `b` | integer | The b component contribution. |
| `c` | integer | The c component contribution. |

<a id="type-specificity"></a>
### CSS.Specificity

**Experimental**

Specificity:
https://drafts.csswg.org/selectors/#specificity-rules

Type: object

**Properties**

| Name | Type | Description |
|---|---|---|
| `a` | integer | The a component, which represents the number of ID selectors. |
| `b` | integer | The b component, which represents the number of class selectors, attributes selectors, and pseudo-classes. |
| `c` | integer | The c component, which represents the number of type selectors and pseudo-elements. |
| `components` (optional) | array of [CSS.SpecificityComponent](#type-specificitycomponent) | **Experimental** Per-simple-selector contributions used to explain this specificity. |

<a id="type-selectorlist"></a>
### CSS.SelectorList

Selector list data.

Type: object

**Properties**

| Name | Type | Description |
|---|---|---|
| `selectors` | array of [CSS.Value](#type-value) | Selectors in the list. |
| `text` | string | Rule selector text. |

<a id="type-cssstylesheetheader"></a>
### CSS.CSSStyleSheetHeader

CSS stylesheet metainformation.

Type: object

**Properties**

| Name | Type | Description |
|---|---|---|
| `styleSheetId` | [DOM.StyleSheetId](DOM.md#type-stylesheetid) | The stylesheet identifier. |
| `frameId` | [Page.FrameId](Page.md#type-frameid) | Owner frame identifier. |
| `sourceURL` | string | Stylesheet resource URL. Empty if this is a constructed stylesheet created using new CSSStyleSheet() (but non-empty if this is a constructed stylesheet imported as a CSS module script). |
| `sourceMapURL` (optional) | string | URL of source map associated with the stylesheet (if any). |
| `origin` | [CSS.StyleSheetOrigin](#type-stylesheetorigin) | Stylesheet origin. |
| `title` | string | Stylesheet title. |
| `ownerNode` (optional) | [DOM.BackendNodeId](DOM.md#type-backendnodeid) | The backend id for the owner node of the stylesheet. |
| `disabled` | boolean | Denotes whether the stylesheet is disabled. |
| `hasSourceURL` (optional) | boolean | Whether the sourceURL field value comes from the sourceURL comment. |
| `isInline` | boolean | Whether this stylesheet is created for STYLE tag by parser. This flag is not set for document.written STYLE tags. |
| `isMutable` | boolean | Whether this stylesheet is mutable. Inline stylesheets become mutable after they have been modified via CSSOM API. `<link>` element's stylesheets become mutable only if DevTools modifies them. Constructed stylesheets (new CSSStyleSheet()) are mutable immediately after creation. |
| `isConstructed` | boolean | True if this stylesheet is created through new CSSStyleSheet() or imported as a CSS module script. |
| `startLine` | number | Line offset of the stylesheet within the resource (zero based). |
| `startColumn` | number | Column offset of the stylesheet within the resource (zero based). |
| `length` | number | Size of the content (in characters). |
| `endLine` | number | Line offset of the end of the stylesheet within the resource (zero based). |
| `endColumn` | number | Column offset of the end of the stylesheet within the resource (zero based). |
| `loadingFailed` (optional) | boolean | **Experimental** If the style sheet was loaded from a network resource, this indicates when the resource failed to load |

<a id="type-cssrule"></a>
### CSS.CSSRule

CSS rule representation.

Type: object

**Properties**

| Name | Type | Description |
|---|---|---|
| `styleSheetId` (optional) | [DOM.StyleSheetId](DOM.md#type-stylesheetid) | The css style sheet identifier (absent for user agent stylesheet and user-specified stylesheet rules) this rule came from. |
| `selectorList` | [CSS.SelectorList](#type-selectorlist) | Rule selector data. |
| `nestingSelectors` (optional) | array of string | **Experimental** Array of selectors from ancestor style rules, sorted by distance from the current rule. |
| `origin` | [CSS.StyleSheetOrigin](#type-stylesheetorigin) | Parent stylesheet's origin. |
| `style` | [CSS.CSSStyle](#type-cssstyle) | Associated style declaration. |
| `originTreeScopeNodeId` (optional) | [DOM.BackendNodeId](DOM.md#type-backendnodeid) | **Experimental** The BackendNodeId of the DOM node that constitutes the origin tree scope of this rule. |
| `media` (optional) | array of [CSS.CSSMedia](#type-cssmedia) | Media list array (for rules involving media queries). The array enumerates media queries starting with the innermost one, going outwards. |
| `containerQueries` (optional) | array of [CSS.CSSContainerQuery](#type-csscontainerquery) | **Experimental** Container query list array (for rules involving container queries). The array enumerates container queries starting with the innermost one, going outwards. |
| `supports` (optional) | array of [CSS.CSSSupports](#type-csssupports) | **Experimental** @supports CSS at-rule array. The array enumerates @supports at-rules starting with the innermost one, going outwards. |
| `layers` (optional) | array of [CSS.CSSLayer](#type-csslayer) | **Experimental** Cascade layer array. Contains the layer hierarchy that this rule belongs to starting with the innermost layer and going outwards. |
| `scopes` (optional) | array of [CSS.CSSScope](#type-cssscope) | **Experimental** @scope CSS at-rule array. The array enumerates @scope at-rules starting with the innermost one, going outwards. |
| `ruleTypes` (optional) | array of [CSS.CSSRuleType](#type-cssruletype) | **Experimental** The array keeps the types of ancestor CSSRules from the innermost going outwards. |
| `startingStyles` (optional) | array of [CSS.CSSStartingStyle](#type-cssstartingstyle) | **Experimental** @starting-style CSS at-rule array. The array enumerates @starting-style at-rules starting with the innermost one, going outwards. |
| `navigations` (optional) | array of [CSS.CSSNavigation](#type-cssnavigation) | **Experimental** @navigation CSS at-rule array. The array enumerates @navigation at-rules starting with the innermost one, going outwards. |

<a id="type-cssruletype"></a>
### CSS.CSSRuleType

**Experimental**

Enum indicating the type of a CSS rule, used to represent the order of a style rule's ancestors.
This list only contains rule types that are collected during the ancestor rule collection.

Type: string

Allowed values: `MediaRule`, `SupportsRule`, `ContainerRule`, `LayerRule`, `ScopeRule`, `StyleRule`, `StartingStyleRule`, `NavigationRule`

<a id="type-ruleusage"></a>
### CSS.RuleUsage

CSS coverage information.

Type: object

**Properties**

| Name | Type | Description |
|---|---|---|
| `styleSheetId` | [DOM.StyleSheetId](DOM.md#type-stylesheetid) | The css style sheet identifier (absent for user agent stylesheet and user-specified stylesheet rules) this rule came from. |
| `startOffset` | number | Offset of the start of the rule (including selector) from the beginning of the stylesheet. |
| `endOffset` | number | Offset of the end of the rule body from the beginning of the stylesheet. |
| `used` | boolean | Indicates whether the rule was actually used by some element in the page. |

<a id="type-sourcerange"></a>
### CSS.SourceRange

Text range within a resource. All numbers are zero-based.

Type: object

**Properties**

| Name | Type | Description |
|---|---|---|
| `startLine` | integer | Start line of range. |
| `startColumn` | integer | Start column of range (inclusive). |
| `endLine` | integer | End line of range |
| `endColumn` | integer | End column of range (exclusive). |

<a id="type-shorthandentry"></a>
### CSS.ShorthandEntry

Type: object

**Properties**

| Name | Type | Description |
|---|---|---|
| `name` | string | Shorthand name. |
| `value` | string | Shorthand value. |
| `important` (optional) | boolean | Whether the property has "!important" annotation (implies `false` if absent). |

<a id="type-csscomputedstyleproperty"></a>
### CSS.CSSComputedStyleProperty

Type: object

**Properties**

| Name | Type | Description |
|---|---|---|
| `name` | string | Computed style property name. |
| `value` | string | Computed style property value. |

<a id="type-computedstyleextrafields"></a>
### CSS.ComputedStyleExtraFields

**Experimental**

Type: object

**Properties**

| Name | Type | Description |
|---|---|---|
| `isAppearanceBase` | boolean | Returns whether or not this node is being rendered with base appearance, which happens when it has its appearance property set to base/base-select or it is in the subtree of an element being rendered with base appearance. |

<a id="type-cssstyle"></a>
### CSS.CSSStyle

CSS style representation.

Type: object

**Properties**

| Name | Type | Description |
|---|---|---|
| `styleSheetId` (optional) | [DOM.StyleSheetId](DOM.md#type-stylesheetid) | The css style sheet identifier (absent for user agent stylesheet and user-specified stylesheet rules) this rule came from. |
| `cssProperties` | array of [CSS.CSSProperty](#type-cssproperty) | CSS properties in the style. |
| `shorthandEntries` | array of [CSS.ShorthandEntry](#type-shorthandentry) | Computed values for all shorthands found in the style. |
| `cssText` (optional) | string | Style declaration text (if available). |
| `range` (optional) | [CSS.SourceRange](#type-sourcerange) | Style declaration range in the enclosing stylesheet (if available). |

<a id="type-cssproperty"></a>
### CSS.CSSProperty

CSS property declaration data.

Type: object

**Properties**

| Name | Type | Description |
|---|---|---|
| `name` | string | The property name. |
| `value` | string | The property value. |
| `important` (optional) | boolean | Whether the property has "!important" annotation (implies `false` if absent). |
| `implicit` (optional) | boolean | Whether the property is implicit (implies `false` if absent). |
| `text` (optional) | string | The full property text as specified in the style. |
| `parsedOk` (optional) | boolean | Whether the property is understood by the browser (implies `true` if absent). |
| `disabled` (optional) | boolean | Whether the property is disabled by the user (present for source-based properties only). |
| `range` (optional) | [CSS.SourceRange](#type-sourcerange) | The entire property range in the enclosing style declaration (if available). |
| `longhandProperties` (optional) | array of [CSS.CSSProperty](#type-cssproperty) | **Experimental** Parsed longhand components of this property if it is a shorthand. This field will be empty if the given property is not a shorthand. |

<a id="type-cssmedia"></a>
### CSS.CSSMedia

CSS media rule descriptor.

Type: object

**Properties**

| Name | Type | Description |
|---|---|---|
| `text` | string | Media query text. |
| `source` | string | Source of the media query: "mediaRule" if specified by a @media rule, "importRule" if specified by an @import rule, "linkedSheet" if specified by a "media" attribute in a linked stylesheet's LINK tag, "inlineSheet" if specified by a "media" attribute in an inline stylesheet's STYLE tag. Allowed values: `mediaRule`, `importRule`, `linkedSheet`, `inlineSheet` |
| `sourceURL` (optional) | string | URL of the document containing the media query description. |
| `range` (optional) | [CSS.SourceRange](#type-sourcerange) | The associated rule (@media or @import) header range in the enclosing stylesheet (if available). |
| `styleSheetId` (optional) | [DOM.StyleSheetId](DOM.md#type-stylesheetid) | Identifier of the stylesheet containing this object (if exists). |
| `mediaList` (optional) | array of [CSS.MediaQuery](#type-mediaquery) | Array of media queries. |

<a id="type-mediaquery"></a>
### CSS.MediaQuery

Media query descriptor.

Type: object

**Properties**

| Name | Type | Description |
|---|---|---|
| `expressions` | array of [CSS.MediaQueryExpression](#type-mediaqueryexpression) | Array of media query expressions. |
| `active` | boolean | Whether the media query condition is satisfied. |

<a id="type-mediaqueryexpression"></a>
### CSS.MediaQueryExpression

Media query expression descriptor.

Type: object

**Properties**

| Name | Type | Description |
|---|---|---|
| `value` | number | Media query expression value. |
| `unit` | string | Media query expression units. |
| `feature` | string | Media query expression feature. |
| `valueRange` (optional) | [CSS.SourceRange](#type-sourcerange) | The associated range of the value text in the enclosing stylesheet (if available). |
| `computedLength` (optional) | number | Computed length of media query expression (if applicable). |

<a id="type-csscontainerquery"></a>
### CSS.CSSContainerQuery

**Experimental**

CSS container query rule descriptor.

Type: object

**Properties**

| Name | Type | Description |
|---|---|---|
| `text` | string | **Deprecated** Container query text. Contains the query part without the container name for a single query. Deprecated in favor of conditionText which contains the full prelude after @container. |
| `range` (optional) | [CSS.SourceRange](#type-sourcerange) | The associated rule header range in the enclosing stylesheet (if available). |
| `styleSheetId` (optional) | [DOM.StyleSheetId](DOM.md#type-stylesheetid) | Identifier of the stylesheet containing this object (if exists). |
| `name` (optional) | string | Optional name for the container. |
| `physicalAxes` (optional) | [DOM.PhysicalAxes](DOM.md#type-physicalaxes) | Optional physical axes queried for the container. |
| `logicalAxes` (optional) | [DOM.LogicalAxes](DOM.md#type-logicalaxes) | Optional logical axes queried for the container. |
| `queriesScrollState` (optional) | boolean | true if the query contains scroll-state() queries. |
| `queriesAnchored` (optional) | boolean | true if the query contains anchored() queries. |
| `conditionText` | string | CSSContainerRule.conditionText |

<a id="type-csssupports"></a>
### CSS.CSSSupports

**Experimental**

CSS Supports at-rule descriptor.

Type: object

**Properties**

| Name | Type | Description |
|---|---|---|
| `text` | string | Supports rule text. |
| `active` | boolean | Whether the supports condition is satisfied. |
| `range` (optional) | [CSS.SourceRange](#type-sourcerange) | The associated rule header range in the enclosing stylesheet (if available). |
| `styleSheetId` (optional) | [DOM.StyleSheetId](DOM.md#type-stylesheetid) | Identifier of the stylesheet containing this object (if exists). |

<a id="type-cssnavigation"></a>
### CSS.CSSNavigation

**Experimental**

CSS Navigation at-rule descriptor.

Type: object

**Properties**

| Name | Type | Description |
|---|---|---|
| `text` | string | Navigation rule text. |
| `active` (optional) | boolean | Whether the navigation condition is satisfied. |
| `range` (optional) | [CSS.SourceRange](#type-sourcerange) | The associated rule header range in the enclosing stylesheet (if available). |
| `styleSheetId` (optional) | [DOM.StyleSheetId](DOM.md#type-stylesheetid) | Identifier of the stylesheet containing this object (if exists). |

<a id="type-cssscope"></a>
### CSS.CSSScope

**Experimental**

CSS Scope at-rule descriptor.

Type: object

**Properties**

| Name | Type | Description |
|---|---|---|
| `text` | string | Scope rule text. |
| `range` (optional) | [CSS.SourceRange](#type-sourcerange) | The associated rule header range in the enclosing stylesheet (if available). |
| `styleSheetId` (optional) | [DOM.StyleSheetId](DOM.md#type-stylesheetid) | Identifier of the stylesheet containing this object (if exists). |

<a id="type-csslayer"></a>
### CSS.CSSLayer

**Experimental**

CSS Layer at-rule descriptor.

Type: object

**Properties**

| Name | Type | Description |
|---|---|---|
| `text` | string | Layer name. |
| `range` (optional) | [CSS.SourceRange](#type-sourcerange) | The associated rule header range in the enclosing stylesheet (if available). |
| `styleSheetId` (optional) | [DOM.StyleSheetId](DOM.md#type-stylesheetid) | Identifier of the stylesheet containing this object (if exists). |

<a id="type-cssstartingstyle"></a>
### CSS.CSSStartingStyle

**Experimental**

CSS Starting Style at-rule descriptor.

Type: object

**Properties**

| Name | Type | Description |
|---|---|---|
| `range` (optional) | [CSS.SourceRange](#type-sourcerange) | The associated rule header range in the enclosing stylesheet (if available). |
| `styleSheetId` (optional) | [DOM.StyleSheetId](DOM.md#type-stylesheetid) | Identifier of the stylesheet containing this object (if exists). |

<a id="type-csslayerdata"></a>
### CSS.CSSLayerData

**Experimental**

CSS Layer data.

Type: object

**Properties**

| Name | Type | Description |
|---|---|---|
| `name` | string | Layer name. |
| `subLayers` (optional) | array of [CSS.CSSLayerData](#type-csslayerdata) | Direct sub-layers |
| `order` | number | Layer order. The order determines the order of the layer in the cascade order. A higher number has higher priority in the cascade order. |

<a id="type-platformfontusage"></a>
### CSS.PlatformFontUsage

Information about amount of glyphs that were rendered with given font.

Type: object

**Properties**

| Name | Type | Description |
|---|---|---|
| `familyName` | string | Font's family name reported by platform. |
| `postScriptName` | string | Font's PostScript name reported by platform. |
| `isCustomFont` | boolean | Indicates if the font was downloaded or resolved locally. |
| `glyphCount` | number | Amount of glyphs that were rendered with this font. |

<a id="type-fontvariationaxis"></a>
### CSS.FontVariationAxis

Information about font variation axes for variable fonts

Type: object

**Properties**

| Name | Type | Description |
|---|---|---|
| `tag` | string | The font-variation-setting tag (a.k.a. "axis tag"). |
| `name` | string | Human-readable variation name in the default language (normally, "en"). |
| `minValue` | number | The minimum value (inclusive) the font supports for this tag. |
| `maxValue` | number | The maximum value (inclusive) the font supports for this tag. |
| `defaultValue` | number | The default value. |

<a id="type-fontface"></a>
### CSS.FontFace

Properties of a web font: https://www.w3.org/TR/2008/REC-CSS2-20080411/fonts.html#font-descriptions
and additional information such as platformFontFamily and fontVariationAxes.

Type: object

**Properties**

| Name | Type | Description |
|---|---|---|
| `fontFamily` | string | The font-family. |
| `fontStyle` | string | The font-style. |
| `fontVariant` | string | The font-variant. |
| `fontWeight` | string | The font-weight. |
| `fontStretch` | string | The font-stretch. |
| `fontDisplay` | string | The font-display. |
| `unicodeRange` | string | The unicode-range. |
| `src` | string | The src. |
| `platformFontFamily` | string | The resolved platform font family |
| `fontVariationAxes` (optional) | array of [CSS.FontVariationAxis](#type-fontvariationaxis) | Available variation settings (a.k.a. "axes"). |

<a id="type-csstryrule"></a>
### CSS.CSSTryRule

CSS try rule representation.

Type: object

**Properties**

| Name | Type | Description |
|---|---|---|
| `styleSheetId` (optional) | [DOM.StyleSheetId](DOM.md#type-stylesheetid) | The css style sheet identifier (absent for user agent stylesheet and user-specified stylesheet rules) this rule came from. |
| `origin` | [CSS.StyleSheetOrigin](#type-stylesheetorigin) | Parent stylesheet's origin. |
| `style` | [CSS.CSSStyle](#type-cssstyle) | Associated style declaration. |

<a id="type-csspositiontryrule"></a>
### CSS.CSSPositionTryRule

CSS @position-try rule representation.

Type: object

**Properties**

| Name | Type | Description |
|---|---|---|
| `name` | [CSS.Value](#type-value) | The prelude dashed-ident name |
| `styleSheetId` (optional) | [DOM.StyleSheetId](DOM.md#type-stylesheetid) | The css style sheet identifier (absent for user agent stylesheet and user-specified stylesheet rules) this rule came from. |
| `origin` | [CSS.StyleSheetOrigin](#type-stylesheetorigin) | Parent stylesheet's origin. |
| `style` | [CSS.CSSStyle](#type-cssstyle) | Associated style declaration. |
| `active` | boolean |  |

<a id="type-csskeyframesrule"></a>
### CSS.CSSKeyframesRule

CSS keyframes rule representation.

Type: object

**Properties**

| Name | Type | Description |
|---|---|---|
| `animationName` | [CSS.Value](#type-value) | Animation name. |
| `keyframes` | array of [CSS.CSSKeyframeRule](#type-csskeyframerule) | List of keyframes. |

<a id="type-csspropertyregistration"></a>
### CSS.CSSPropertyRegistration

Representation of a custom property registration through CSS.registerProperty

Type: object

**Properties**

| Name | Type | Description |
|---|---|---|
| `propertyName` | string |  |
| `initialValue` (optional) | [CSS.Value](#type-value) |  |
| `inherits` | boolean |  |
| `syntax` | string |  |

<a id="type-cssatrule"></a>
### CSS.CSSAtRule

CSS generic @rule representation.

Type: object

**Properties**

| Name | Type | Description |
|---|---|---|
| `type` | string | Type of at-rule. Allowed values: `font-face`, `font-feature-values`, `font-palette-values`, `counter-style` |
| `subsection` (optional) | string | Subsection of font-feature-values, if this is a subsection. Allowed values: `swash`, `annotation`, `ornaments`, `stylistic`, `styleset`, `character-variant` |
| `name` (optional) | [CSS.Value](#type-value) | LINT.ThenChange(//third_party/blink/renderer/core/inspector/inspector_style_sheet.cc:FontVariantAlternatesFeatureType,//third_party/blink/renderer/core/inspector/inspector_css_agent.cc:FontVariantAlternatesFeatureType) Associated name, if applicable. |
| `styleSheetId` (optional) | [DOM.StyleSheetId](DOM.md#type-stylesheetid) | The css style sheet identifier (absent for user agent stylesheet and user-specified stylesheet rules) this rule came from. |
| `origin` | [CSS.StyleSheetOrigin](#type-stylesheetorigin) | Parent stylesheet's origin. |
| `style` | [CSS.CSSStyle](#type-cssstyle) | Associated style declaration. |

<a id="type-csspropertyrule"></a>
### CSS.CSSPropertyRule

CSS property at-rule representation.

Type: object

**Properties**

| Name | Type | Description |
|---|---|---|
| `styleSheetId` (optional) | [DOM.StyleSheetId](DOM.md#type-stylesheetid) | The css style sheet identifier (absent for user agent stylesheet and user-specified stylesheet rules) this rule came from. |
| `origin` | [CSS.StyleSheetOrigin](#type-stylesheetorigin) | Parent stylesheet's origin. |
| `propertyName` | [CSS.Value](#type-value) | Associated property name. |
| `style` | [CSS.CSSStyle](#type-cssstyle) | Associated style declaration. |

<a id="type-cssfunctionparameter"></a>
### CSS.CSSFunctionParameter

CSS function argument representation.

Type: object

**Properties**

| Name | Type | Description |
|---|---|---|
| `name` | string | The parameter name. |
| `type` | string | The parameter type. |

<a id="type-cssfunctionconditionnode"></a>
### CSS.CSSFunctionConditionNode

CSS function conditional block representation.

Type: object

**Properties**

| Name | Type | Description |
|---|---|---|
| `media` (optional) | [CSS.CSSMedia](#type-cssmedia) | Media query for this conditional block. Only one type of condition should be set. |
| `containerQueries` (optional) | [CSS.CSSContainerQuery](#type-csscontainerquery) | Container query for this conditional block. Only one type of condition should be set. |
| `supports` (optional) | [CSS.CSSSupports](#type-csssupports) | @supports CSS at-rule condition. Only one type of condition should be set. |
| `navigation` (optional) | [CSS.CSSNavigation](#type-cssnavigation) | @navigation condition. Only one type of condition should be set. |
| `children` | array of [CSS.CSSFunctionNode](#type-cssfunctionnode) | Block body. |
| `conditionText` | string | The condition text. |

<a id="type-cssfunctionnode"></a>
### CSS.CSSFunctionNode

Section of the body of a CSS function rule.

Type: object

**Properties**

| Name | Type | Description |
|---|---|---|
| `condition` (optional) | [CSS.CSSFunctionConditionNode](#type-cssfunctionconditionnode) | A conditional block. If set, style should not be set. |
| `style` (optional) | [CSS.CSSStyle](#type-cssstyle) | Values set by this node. If set, condition should not be set. |

<a id="type-cssfunctionrule"></a>
### CSS.CSSFunctionRule

CSS function at-rule representation.

Type: object

**Properties**

| Name | Type | Description |
|---|---|---|
| `name` | [CSS.Value](#type-value) | Name of the function. |
| `styleSheetId` (optional) | [DOM.StyleSheetId](DOM.md#type-stylesheetid) | The css style sheet identifier (absent for user agent stylesheet and user-specified stylesheet rules) this rule came from. |
| `origin` | [CSS.StyleSheetOrigin](#type-stylesheetorigin) | Parent stylesheet's origin. |
| `parameters` | array of [CSS.CSSFunctionParameter](#type-cssfunctionparameter) | List of parameters. |
| `children` | array of [CSS.CSSFunctionNode](#type-cssfunctionnode) | Function body. |
| `originTreeScopeNodeId` (optional) | [DOM.BackendNodeId](DOM.md#type-backendnodeid) | **Experimental** The BackendNodeId of the DOM node that constitutes the origin tree scope of this rule. |

<a id="type-csskeyframerule"></a>
### CSS.CSSKeyframeRule

CSS keyframe rule representation.

Type: object

**Properties**

| Name | Type | Description |
|---|---|---|
| `styleSheetId` (optional) | [DOM.StyleSheetId](DOM.md#type-stylesheetid) | The css style sheet identifier (absent for user agent stylesheet and user-specified stylesheet rules) this rule came from. |
| `origin` | [CSS.StyleSheetOrigin](#type-stylesheetorigin) | Parent stylesheet's origin. |
| `keyText` | [CSS.Value](#type-value) | Associated key text. |
| `style` | [CSS.CSSStyle](#type-cssstyle) | Associated style declaration. |

<a id="type-styledeclarationedit"></a>
### CSS.StyleDeclarationEdit

A descriptor of operation to mutate style declaration text.

Type: object

**Properties**

| Name | Type | Description |
|---|---|---|
| `styleSheetId` | [DOM.StyleSheetId](DOM.md#type-stylesheetid) | The css style sheet identifier. |
| `range` | [CSS.SourceRange](#type-sourcerange) | The range of the style text in the enclosing stylesheet. |
| `text` | string | New style text. |
