# CSS domain *(experimental)*

Copyright 2017 The Chromium Authors Use of this source code is governed by a BSD-style license that can be found in the LICENSE file.  Contributing to Chrome DevTools Protocol: https://goo.gle/devtools-contribution-guide-cdp This domain exposes CSS read/write operations. All CSS objects (stylesheets, rules, and styles) have an associated `id` used in subsequent operations on the related object. Each object type has a specific `id` structure, and those are not interchangeable between objects of different kinds. CSS objects can be loaded using the `get*ForNode()` calls (which accept a DOM node id). A client can also keep track of stylesheets via the `styleSheetAdded`/`styleSheetRemoved` events and subsequently load the required stylesheet contents using the `getStyleSheet[Text]()` methods.

Depends on: [DOM](DOM.md), [Page](Page.md)

Methods are called as `CSS.<command>` and events arrive as `CSS.<event>`.

## Commands

### CSS.addRule

Inserts a new rule with the given `ruleText` in a stylesheet with given `styleSheetId`, at the position specified by `location`.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `styleSheetId` | [DOM.StyleSheetId](DOM.md#type-stylesheetid) | The css style sheet identifier where a new rule should be inserted. |
| `ruleText` | string | The text of a new rule. |
| `location` | [SourceRange](#type-sourcerange) | Text position of a new rule in the target style sheet. |
| `nodeForPropertySyntaxValidation` (optional) *(experimental)* | [DOM.NodeId](DOM.md#type-nodeid) | NodeId for the DOM node in whose context custom property declarations for registered properties should be validated. If omitted, declarations in the new rule text can only be validated statically, which may produce incorrect results if the declaration contains a var() for example. |

**Returns**

| Name | Type | Description |
|---|---|---|
| `rule` | [CSSRule](#type-cssrule) | The newly created rule. |

### CSS.collectClassNames

Returns all class names from specified stylesheet.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `styleSheetId` | [DOM.StyleSheetId](DOM.md#type-stylesheetid) |  |

**Returns**

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

**Returns**

| Name | Type | Description |
|---|---|---|
| `styleSheetId` | [DOM.StyleSheetId](DOM.md#type-stylesheetid) | Identifier of the created "via-inspector" stylesheet. |

### CSS.disable

Disables the CSS agent for the given page.

### CSS.enable

Enables the CSS agent for the given page. Clients should not assume that the CSS agent has been enabled until the result of this command is received.

### CSS.forcePseudoState

Ensures that the given node will have specified pseudo-classes whenever its style is computed by the browser.

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

**Returns**

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

**Returns**

| Name | Type | Description |
|---|---|---|
| `computedStyle` | array of [CSSComputedStyleProperty](#type-csscomputedstyleproperty) | Computed style for the specified DOM node. |
| `extraFields` *(experimental)* | [ComputedStyleExtraFields](#type-computedstyleextrafields) | A list of non-standard "extra fields" which blink stores alongside each computed style. |

### CSS.resolveValues *(experimental)*

Resolve the specified values in the context of the provided element. For example, a value of '1em' is evaluated according to the computed 'font-size' of the element and a value 'calc(1px + 2px)' will be resolved to '3px'. If the `propertyName` was specified the `values` are resolved as if they were property's declaration. If a value cannot be parsed according to the provided property syntax, the value is parsed using combined syntax as if null `propertyName` was provided. If the value cannot be resolved even then, return the provided value without any changes. Note: this function currently does not resolve CSS random() function, it returns unmodified random() function parts.`

**Parameters**

| Name | Type | Description |
|---|---|---|
| `values` | array of string | Cascade-dependent keywords (revert/revert-layer) do not work. |
| `nodeId` | [DOM.NodeId](DOM.md#type-nodeid) | Id of the node in whose context the expression is evaluated |
| `propertyName` (optional) | string | Only longhands and custom property names are accepted. |
| `pseudoType` (optional) | [DOM.PseudoType](DOM.md#type-pseudotype) | Pseudo element type, only works for pseudo elements that generate elements in the tree, such as ::before and ::after. |
| `pseudoIdentifier` (optional) | string | Pseudo element custom ident. |

**Returns**

| Name | Type | Description |
|---|---|---|
| `results` | array of string |  |

### CSS.getLonghandProperties *(experimental)*

**Parameters**

| Name | Type | Description |
|---|---|---|
| `shorthandName` | string |  |
| `value` | string |  |

**Returns**

| Name | Type | Description |
|---|---|---|
| `longhandProperties` | array of [CSSProperty](#type-cssproperty) |  |

### CSS.getInlineStylesForNode

Returns the styles defined inline (explicitly in the "style" attribute and implicitly, using DOM attributes) for a DOM node identified by `nodeId`.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `nodeId` | [DOM.NodeId](DOM.md#type-nodeid) |  |

**Returns**

| Name | Type | Description |
|---|---|---|
| `inlineStyle` (optional) | [CSSStyle](#type-cssstyle) | Inline style for the specified DOM node. |
| `attributesStyle` (optional) | [CSSStyle](#type-cssstyle) | Attribute-defined element style (e.g. resulting from "width=20 height=100%"). |

### CSS.getAnimatedStylesForNode *(experimental)*

Returns the styles coming from animations & transitions including the animation & transition styles coming from inheritance chain.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `nodeId` | [DOM.NodeId](DOM.md#type-nodeid) |  |

**Returns**

| Name | Type | Description |
|---|---|---|
| `animationStyles` (optional) | array of [CSSAnimationStyle](#type-cssanimationstyle) | Styles coming from animations. |
| `transitionsStyle` (optional) | [CSSStyle](#type-cssstyle) | Style coming from transitions. |
| `inherited` (optional) | array of [InheritedAnimatedStyleEntry](#type-inheritedanimatedstyleentry) | Inherited style entries for animationsStyle and transitionsStyle from the inheritance chain of the element. |

### CSS.getMatchedStylesForNode

Returns requested styles for a DOM node identified by `nodeId`.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `nodeId` | [DOM.NodeId](DOM.md#type-nodeid) |  |

**Returns**

| Name | Type | Description |
|---|---|---|
| `inlineStyle` (optional) | [CSSStyle](#type-cssstyle) | Inline style for the specified DOM node. |
| `attributesStyle` (optional) | [CSSStyle](#type-cssstyle) | Attribute-defined element style (e.g. resulting from "width=20 height=100%"). |
| `matchedCSSRules` (optional) | array of [RuleMatch](#type-rulematch) | CSS rules matching this node, from all applicable stylesheets. |
| `pseudoElements` (optional) | array of [PseudoElementMatches](#type-pseudoelementmatches) | Pseudo style matches for this node. |
| `inherited` (optional) | array of [InheritedStyleEntry](#type-inheritedstyleentry) | A chain of inherited styles (from the immediate node parent up to the DOM tree root). |
| `inheritedPseudoElements` (optional) | array of [InheritedPseudoElementMatches](#type-inheritedpseudoelementmatches) | A chain of inherited pseudo element styles (from the immediate node parent up to the DOM tree root). |
| `cssKeyframesRules` (optional) | array of [CSSKeyframesRule](#type-csskeyframesrule) | A list of CSS keyframed animations matching this node. |
| `cssPositionTryRules` (optional) | array of [CSSPositionTryRule](#type-csspositiontryrule) | A list of CSS @position-try rules matching this node, based on the position-try-fallbacks property. |
| `activePositionFallbackIndex` (optional) | integer | Index of the active fallback in the applied position-try-fallback property, will not be set if there is no active position-try fallback. |
| `cssPropertyRules` (optional) | array of [CSSPropertyRule](#type-csspropertyrule) | A list of CSS at-property rules matching this node. |
| `cssPropertyRegistrations` (optional) | array of [CSSPropertyRegistration](#type-csspropertyregistration) | A list of CSS property registrations matching this node. |
| `cssAtRules` (optional) | array of [CSSAtRule](#type-cssatrule) | A list of simple @rules matching this node or its pseudo-elements. |
| `parentLayoutNodeId` (optional) *(experimental)* | [DOM.NodeId](DOM.md#type-nodeid) | Id of the first parent element that does not have display: contents. |
| `cssFunctionRules` (optional) *(experimental)* | array of [CSSFunctionRule](#type-cssfunctionrule) | A list of CSS at-function rules referenced by styles of this node. |

### CSS.getEnvironmentVariables *(experimental)*

Returns the values of the default UA-defined environment variables used in env()

**Returns**

| Name | Type | Description |
|---|---|---|
| `environmentVariables` | object |  |

### CSS.getMediaQueries

Returns all media queries parsed by the rendering engine.

**Returns**

| Name | Type | Description |
|---|---|---|
| `medias` | array of [CSSMedia](#type-cssmedia) |  |

### CSS.getPlatformFontsForNode

Requests information about platform fonts which we used to render child TextNodes in the given node.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `nodeId` | [DOM.NodeId](DOM.md#type-nodeid) |  |

**Returns**

| Name | Type | Description |
|---|---|---|
| `fonts` | array of [PlatformFontUsage](#type-platformfontusage) | Usage statistics for every employed platform font. |

### CSS.getStyleSheetText

Returns the current textual content for a stylesheet.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `styleSheetId` | [DOM.StyleSheetId](DOM.md#type-stylesheetid) |  |

**Returns**

| Name | Type | Description |
|---|---|---|
| `text` | string | The stylesheet text. |

### CSS.getLayersForNode *(experimental)*

Returns all layers parsed by the rendering engine for the tree scope of a node. Given a DOM element identified by nodeId, getLayersForNode returns the root layer for the nearest ancestor document or shadow root. The layer root contains the full layer tree for the tree scope and their ordering.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `nodeId` | [DOM.NodeId](DOM.md#type-nodeid) |  |

**Returns**

| Name | Type | Description |
|---|---|---|
| `rootLayer` | [CSSLayerData](#type-csslayerdata) |  |

### CSS.getLocationForSelector *(experimental)*

Given a CSS selector text and a style sheet ID, getLocationForSelector returns an array of locations of the CSS selector in the style sheet.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `styleSheetId` | [DOM.StyleSheetId](DOM.md#type-stylesheetid) |  |
| `selectorText` | string |  |

**Returns**

| Name | Type | Description |
|---|---|---|
| `ranges` | array of [SourceRange](#type-sourcerange) |  |

### CSS.trackComputedStyleUpdatesForNode *(experimental)*

Starts tracking the given node for the computed style updates and whenever the computed style is updated for node, it queues a `computedStyleUpdated` event with throttling. There can only be 1 node tracked for computed style updates so passing a new node id removes tracking from the previous node. Pass `undefined` to disable tracking.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `nodeId` (optional) | [DOM.NodeId](DOM.md#type-nodeid) |  |

### CSS.trackComputedStyleUpdates *(experimental)*

Starts tracking the given computed styles for updates. The specified array of properties replaces the one previously specified. Pass empty array to disable tracking. Use takeComputedStyleUpdates to retrieve the list of nodes that had properties modified. The changes to computed style properties are only tracked for nodes pushed to the front-end by the DOM agent. If no changes to the tracked properties occur after the node has been pushed to the front-end, no updates will be issued for the node.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `propertiesToTrack` | array of [CSSComputedStyleProperty](#type-csscomputedstyleproperty) |  |

### CSS.takeComputedStyleUpdates *(experimental)*

Polls the next batch of computed style updates.

**Returns**

| Name | Type | Description |
|---|---|---|
| `nodeIds` | array of [DOM.NodeId](DOM.md#type-nodeid) | The list of node Ids that have their tracked computed styles updated. |

### CSS.setEffectivePropertyValueForNode

Find a rule with the given active property for the given node and set the new value for this property

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
| `range` | [SourceRange](#type-sourcerange) |  |
| `propertyName` | string |  |

**Returns**

| Name | Type | Description |
|---|---|---|
| `propertyName` | [Value](#type-value) | The resulting key text after modification. |

### CSS.setKeyframeKey

Modifies the keyframe rule key text.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `styleSheetId` | [DOM.StyleSheetId](DOM.md#type-stylesheetid) |  |
| `range` | [SourceRange](#type-sourcerange) |  |
| `keyText` | string |  |

**Returns**

| Name | Type | Description |
|---|---|---|
| `keyText` | [Value](#type-value) | The resulting key text after modification. |

### CSS.setMediaText

Modifies the rule selector.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `styleSheetId` | [DOM.StyleSheetId](DOM.md#type-stylesheetid) |  |
| `range` | [SourceRange](#type-sourcerange) |  |
| `text` | string |  |

**Returns**

| Name | Type | Description |
|---|---|---|
| `media` | [CSSMedia](#type-cssmedia) | The resulting CSS media rule after modification. |

### CSS.setContainerQueryText *(experimental)* *(deprecated)*

Modifies the expression of a container query. Deprecated. Use setContainerQueryConditionText instead.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `styleSheetId` | [DOM.StyleSheetId](DOM.md#type-stylesheetid) |  |
| `range` | [SourceRange](#type-sourcerange) |  |
| `text` | string |  |

**Returns**

| Name | Type | Description |
|---|---|---|
| `containerQuery` | [CSSContainerQuery](#type-csscontainerquery) | The resulting CSS container query rule after modification. |

### CSS.setContainerQueryConditionText *(experimental)*

**Parameters**

| Name | Type | Description |
|---|---|---|
| `styleSheetId` | [DOM.StyleSheetId](DOM.md#type-stylesheetid) |  |
| `range` | [SourceRange](#type-sourcerange) |  |
| `text` | string |  |

**Returns**

| Name | Type | Description |
|---|---|---|
| `containerQuery` | [CSSContainerQuery](#type-csscontainerquery) | The resulting CSS container query rule after modification. |

### CSS.setSupportsText *(experimental)*

Modifies the expression of a supports at-rule.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `styleSheetId` | [DOM.StyleSheetId](DOM.md#type-stylesheetid) |  |
| `range` | [SourceRange](#type-sourcerange) |  |
| `text` | string |  |

**Returns**

| Name | Type | Description |
|---|---|---|
| `supports` | [CSSSupports](#type-csssupports) | The resulting CSS Supports rule after modification. |

### CSS.setNavigationText *(experimental)*

Modifies the expression of a navigation at-rule.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `styleSheetId` | [DOM.StyleSheetId](DOM.md#type-stylesheetid) |  |
| `range` | [SourceRange](#type-sourcerange) |  |
| `text` | string |  |

**Returns**

| Name | Type | Description |
|---|---|---|
| `navigation` | [CSSNavigation](#type-cssnavigation) | The resulting CSS Navigation rule after modification. |

### CSS.setScopeText *(experimental)*

Modifies the expression of a scope at-rule.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `styleSheetId` | [DOM.StyleSheetId](DOM.md#type-stylesheetid) |  |
| `range` | [SourceRange](#type-sourcerange) |  |
| `text` | string |  |

**Returns**

| Name | Type | Description |
|---|---|---|
| `scope` | [CSSScope](#type-cssscope) | The resulting CSS Scope rule after modification. |

### CSS.setRuleSelector

Modifies the rule selector.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `styleSheetId` | [DOM.StyleSheetId](DOM.md#type-stylesheetid) |  |
| `range` | [SourceRange](#type-sourcerange) |  |
| `selector` | string |  |

**Returns**

| Name | Type | Description |
|---|---|---|
| `selectorList` | [SelectorList](#type-selectorlist) | The resulting selector list after modification. |

### CSS.setStyleSheetText

Sets the new stylesheet text.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `styleSheetId` | [DOM.StyleSheetId](DOM.md#type-stylesheetid) |  |
| `text` | string |  |

**Returns**

| Name | Type | Description |
|---|---|---|
| `sourceMapURL` (optional) | string | URL of source map associated with script (if any). |

### CSS.setStyleTexts

Applies specified style edits one after another in the given order.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `edits` | array of [StyleDeclarationEdit](#type-styledeclarationedit) |  |
| `nodeForPropertySyntaxValidation` (optional) *(experimental)* | [DOM.NodeId](DOM.md#type-nodeid) | NodeId for the DOM node in whose context custom property declarations for registered properties should be validated. If omitted, declarations in the new rule text can only be validated statically, which may produce incorrect results if the declaration contains a var() for example. |

**Returns**

| Name | Type | Description |
|---|---|---|
| `styles` | array of [CSSStyle](#type-cssstyle) | The resulting styles after modification. |

### CSS.startRuleUsageTracking

Enables the selector recording.

### CSS.stopRuleUsageTracking

Stop tracking rule usage and return the list of rules that were used since last call to `takeCoverageDelta` (or since start of coverage instrumentation).

**Returns**

| Name | Type | Description |
|---|---|---|
| `ruleUsage` | array of [RuleUsage](#type-ruleusage) |  |

### CSS.takeCoverageDelta

Obtain list of rules that became used since last call to this method (or since start of coverage instrumentation).

**Returns**

| Name | Type | Description |
|---|---|---|
| `coverage` | array of [RuleUsage](#type-ruleusage) |  |
| `timestamp` | number | Monotonically increasing time, in seconds. |

### CSS.setLocalFontsEnabled *(experimental)*

Enables/disables rendering of local CSS fonts (enabled by default).

**Parameters**

| Name | Type | Description |
|---|---|---|
| `enabled` | boolean | Whether rendering of local fonts is enabled. |

## Events

### CSS.fontsUpdated

Fires whenever a web font is updated.  A non-empty font parameter indicates a successfully loaded web font.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `font` (optional) | [FontFace](#type-fontface) | The web font that has loaded. |

### CSS.mediaQueryResultChanged

Fires whenever a MediaQuery result changes (for example, after a browser window has been resized.) The current implementation considers only viewport-dependent media features.

### CSS.styleSheetAdded

Fired whenever an active document stylesheet is added.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `header` | [CSSStyleSheetHeader](#type-cssstylesheetheader) | Added stylesheet metainfo. |

### CSS.styleSheetChanged

Fired whenever a stylesheet is changed as a result of the client operation.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `styleSheetId` | [DOM.StyleSheetId](DOM.md#type-stylesheetid) |  |

### CSS.styleSheetRemoved

Fired whenever an active document stylesheet is removed.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `styleSheetId` | [DOM.StyleSheetId](DOM.md#type-stylesheetid) | Identifier of the removed stylesheet. |

### CSS.computedStyleUpdated *(experimental)*

**Parameters**

| Name | Type | Description |
|---|---|---|
| `nodeId` | [DOM.NodeId](DOM.md#type-nodeid) | The node id that has updated computed styles. |

## Types

<a id="type-stylesheetorigin"></a>
### CSS.StyleSheetOrigin

Type: string

Stylesheet type: "injected" for stylesheets injected via extension, "user-agent" for user-agent stylesheets, "inspector" for stylesheets created by the inspector (i.e. those holding the "via inspector" rules), "regular" for regular stylesheets.

Allowed values: `injected`, `user-agent`, `inspector`, `regular`

<a id="type-pseudoelementmatches"></a>
### CSS.PseudoElementMatches

Type: object

CSS rule collection for a single pseudo style.

**Properties**

| Name | Type | Description |
|---|---|---|
| `pseudoType` | [DOM.PseudoType](DOM.md#type-pseudotype) | Pseudo element type. |
| `pseudoIdentifier` (optional) | string | Pseudo element custom ident. |
| `matches` | array of [RuleMatch](#type-rulematch) | Matches of CSS rules applicable to the pseudo style. |

<a id="type-cssanimationstyle"></a>
### CSS.CSSAnimationStyle

Type: object

CSS style coming from animations with the name of the animation.

**Properties**

| Name | Type | Description |
|---|---|---|
| `name` (optional) | string | The name of the animation. |
| `style` | [CSSStyle](#type-cssstyle) | The style coming from the animation. |

<a id="type-inheritedstyleentry"></a>
### CSS.InheritedStyleEntry

Type: object

Inherited CSS rule collection from ancestor node.

**Properties**

| Name | Type | Description |
|---|---|---|
| `inlineStyle` (optional) | [CSSStyle](#type-cssstyle) | The ancestor node's inline style, if any, in the style inheritance chain. |
| `matchedCSSRules` | array of [RuleMatch](#type-rulematch) | Matches of CSS rules matching the ancestor node in the style inheritance chain. |

<a id="type-inheritedanimatedstyleentry"></a>
### CSS.InheritedAnimatedStyleEntry

Type: object

Inherited CSS style collection for animated styles from ancestor node.

**Properties**

| Name | Type | Description |
|---|---|---|
| `animationStyles` (optional) | array of [CSSAnimationStyle](#type-cssanimationstyle) | Styles coming from the animations of the ancestor, if any, in the style inheritance chain. |
| `transitionsStyle` (optional) | [CSSStyle](#type-cssstyle) | The style coming from the transitions of the ancestor, if any, in the style inheritance chain. |

<a id="type-inheritedpseudoelementmatches"></a>
### CSS.InheritedPseudoElementMatches

Type: object

Inherited pseudo element matches from pseudos of an ancestor node.

**Properties**

| Name | Type | Description |
|---|---|---|
| `pseudoElements` | array of [PseudoElementMatches](#type-pseudoelementmatches) | Matches of pseudo styles from the pseudos of an ancestor node. |

<a id="type-rulematch"></a>
### CSS.RuleMatch

Type: object

Match data for a CSS rule.

**Properties**

| Name | Type | Description |
|---|---|---|
| `rule` | [CSSRule](#type-cssrule) | CSS rule in the match. |
| `matchingSelectors` | array of integer | Matching selector indices in the rule's selectorList selectors (0-based). |

<a id="type-value"></a>
### CSS.Value

Type: object

Data for a simple selector (these are delimited by commas in a selector list).

**Properties**

| Name | Type | Description |
|---|---|---|
| `text` | string | Value text. |
| `range` (optional) | [SourceRange](#type-sourcerange) | Value range in the underlying resource (if available). |
| `specificity` (optional) *(experimental)* | [Specificity](#type-specificity) | Specificity of the selector. |

<a id="type-specificitycomponent"></a>
### CSS.SpecificityComponent *(experimental)*

Type: object

Contribution of an individual simple selector to specificity.

**Properties**

| Name | Type | Description |
|---|---|---|
| `text` | string | The simple selector text that contributes to specificity. |
| `a` | integer | The a component contribution. |
| `b` | integer | The b component contribution. |
| `c` | integer | The c component contribution. |

<a id="type-specificity"></a>
### CSS.Specificity *(experimental)*

Type: object

Specificity: https://drafts.csswg.org/selectors/#specificity-rules

**Properties**

| Name | Type | Description |
|---|---|---|
| `a` | integer | The a component, which represents the number of ID selectors. |
| `b` | integer | The b component, which represents the number of class selectors, attributes selectors, and pseudo-classes. |
| `c` | integer | The c component, which represents the number of type selectors and pseudo-elements. |
| `components` (optional) *(experimental)* | array of [SpecificityComponent](#type-specificitycomponent) | Per-simple-selector contributions used to explain this specificity. |

<a id="type-selectorlist"></a>
### CSS.SelectorList

Type: object

Selector list data.

**Properties**

| Name | Type | Description |
|---|---|---|
| `selectors` | array of [Value](#type-value) | Selectors in the list. |
| `text` | string | Rule selector text. |

<a id="type-cssstylesheetheader"></a>
### CSS.CSSStyleSheetHeader

Type: object

CSS stylesheet metainformation.

**Properties**

| Name | Type | Description |
|---|---|---|
| `styleSheetId` | [DOM.StyleSheetId](DOM.md#type-stylesheetid) | The stylesheet identifier. |
| `frameId` | [Page.FrameId](Page.md#type-frameid) | Owner frame identifier. |
| `sourceURL` | string | Stylesheet resource URL. Empty if this is a constructed stylesheet created using new CSSStyleSheet() (but non-empty if this is a constructed stylesheet imported as a CSS module script). |
| `sourceMapURL` (optional) | string | URL of source map associated with the stylesheet (if any). |
| `origin` | [StyleSheetOrigin](#type-stylesheetorigin) | Stylesheet origin. |
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
| `loadingFailed` (optional) *(experimental)* | boolean | If the style sheet was loaded from a network resource, this indicates when the resource failed to load |

<a id="type-cssrule"></a>
### CSS.CSSRule

Type: object

CSS rule representation.

**Properties**

| Name | Type | Description |
|---|---|---|
| `styleSheetId` (optional) | [DOM.StyleSheetId](DOM.md#type-stylesheetid) | The css style sheet identifier (absent for user agent stylesheet and user-specified stylesheet rules) this rule came from. |
| `selectorList` | [SelectorList](#type-selectorlist) | Rule selector data. |
| `nestingSelectors` (optional) *(experimental)* | array of string | Array of selectors from ancestor style rules, sorted by distance from the current rule. |
| `origin` | [StyleSheetOrigin](#type-stylesheetorigin) | Parent stylesheet's origin. |
| `style` | [CSSStyle](#type-cssstyle) | Associated style declaration. |
| `originTreeScopeNodeId` (optional) *(experimental)* | [DOM.BackendNodeId](DOM.md#type-backendnodeid) | The BackendNodeId of the DOM node that constitutes the origin tree scope of this rule. |
| `media` (optional) | array of [CSSMedia](#type-cssmedia) | Media list array (for rules involving media queries). The array enumerates media queries starting with the innermost one, going outwards. |
| `containerQueries` (optional) *(experimental)* | array of [CSSContainerQuery](#type-csscontainerquery) | Container query list array (for rules involving container queries). The array enumerates container queries starting with the innermost one, going outwards. |
| `supports` (optional) *(experimental)* | array of [CSSSupports](#type-csssupports) | @supports CSS at-rule array. The array enumerates @supports at-rules starting with the innermost one, going outwards. |
| `layers` (optional) *(experimental)* | array of [CSSLayer](#type-csslayer) | Cascade layer array. Contains the layer hierarchy that this rule belongs to starting with the innermost layer and going outwards. |
| `scopes` (optional) *(experimental)* | array of [CSSScope](#type-cssscope) | @scope CSS at-rule array. The array enumerates @scope at-rules starting with the innermost one, going outwards. |
| `ruleTypes` (optional) *(experimental)* | array of [CSSRuleType](#type-cssruletype) | The array keeps the types of ancestor CSSRules from the innermost going outwards. |
| `startingStyles` (optional) *(experimental)* | array of [CSSStartingStyle](#type-cssstartingstyle) | @starting-style CSS at-rule array. The array enumerates @starting-style at-rules starting with the innermost one, going outwards. |
| `navigations` (optional) *(experimental)* | array of [CSSNavigation](#type-cssnavigation) | @navigation CSS at-rule array. The array enumerates @navigation at-rules starting with the innermost one, going outwards. |

<a id="type-cssruletype"></a>
### CSS.CSSRuleType *(experimental)*

Type: string

Enum indicating the type of a CSS rule, used to represent the order of a style rule's ancestors. This list only contains rule types that are collected during the ancestor rule collection.

Allowed values: `MediaRule`, `SupportsRule`, `ContainerRule`, `LayerRule`, `ScopeRule`, `StyleRule`, `StartingStyleRule`, `NavigationRule`

<a id="type-ruleusage"></a>
### CSS.RuleUsage

Type: object

CSS coverage information.

**Properties**

| Name | Type | Description |
|---|---|---|
| `styleSheetId` | [DOM.StyleSheetId](DOM.md#type-stylesheetid) | The css style sheet identifier (absent for user agent stylesheet and user-specified stylesheet rules) this rule came from. |
| `startOffset` | number | Offset of the start of the rule (including selector) from the beginning of the stylesheet. |
| `endOffset` | number | Offset of the end of the rule body from the beginning of the stylesheet. |
| `used` | boolean | Indicates whether the rule was actually used by some element in the page. |

<a id="type-sourcerange"></a>
### CSS.SourceRange

Type: object

Text range within a resource. All numbers are zero-based.

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
### CSS.ComputedStyleExtraFields *(experimental)*

Type: object

**Properties**

| Name | Type | Description |
|---|---|---|
| `isAppearanceBase` | boolean | Returns whether or not this node is being rendered with base appearance, which happens when it has its appearance property set to base/base-select or it is in the subtree of an element being rendered with base appearance. |

<a id="type-cssstyle"></a>
### CSS.CSSStyle

Type: object

CSS style representation.

**Properties**

| Name | Type | Description |
|---|---|---|
| `styleSheetId` (optional) | [DOM.StyleSheetId](DOM.md#type-stylesheetid) | The css style sheet identifier (absent for user agent stylesheet and user-specified stylesheet rules) this rule came from. |
| `cssProperties` | array of [CSSProperty](#type-cssproperty) | CSS properties in the style. |
| `shorthandEntries` | array of [ShorthandEntry](#type-shorthandentry) | Computed values for all shorthands found in the style. |
| `cssText` (optional) | string | Style declaration text (if available). |
| `range` (optional) | [SourceRange](#type-sourcerange) | Style declaration range in the enclosing stylesheet (if available). |

<a id="type-cssproperty"></a>
### CSS.CSSProperty

Type: object

CSS property declaration data.

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
| `range` (optional) | [SourceRange](#type-sourcerange) | The entire property range in the enclosing style declaration (if available). |
| `longhandProperties` (optional) *(experimental)* | array of [CSSProperty](#type-cssproperty) | Parsed longhand components of this property if it is a shorthand. This field will be empty if the given property is not a shorthand. |

<a id="type-cssmedia"></a>
### CSS.CSSMedia

Type: object

CSS media rule descriptor.

**Properties**

| Name | Type | Description |
|---|---|---|
| `text` | string | Media query text. |
| `source` | enum: `mediaRule`, `importRule`, `linkedSheet`, `inlineSheet` | Source of the media query: "mediaRule" if specified by a @media rule, "importRule" if specified by an @import rule, "linkedSheet" if specified by a "media" attribute in a linked stylesheet's LINK tag, "inlineSheet" if specified by a "media" attribute in an inline stylesheet's STYLE tag. |
| `sourceURL` (optional) | string | URL of the document containing the media query description. |
| `range` (optional) | [SourceRange](#type-sourcerange) | The associated rule (@media or @import) header range in the enclosing stylesheet (if available). |
| `styleSheetId` (optional) | [DOM.StyleSheetId](DOM.md#type-stylesheetid) | Identifier of the stylesheet containing this object (if exists). |
| `mediaList` (optional) | array of [MediaQuery](#type-mediaquery) | Array of media queries. |

<a id="type-mediaquery"></a>
### CSS.MediaQuery

Type: object

Media query descriptor.

**Properties**

| Name | Type | Description |
|---|---|---|
| `expressions` | array of [MediaQueryExpression](#type-mediaqueryexpression) | Array of media query expressions. |
| `active` | boolean | Whether the media query condition is satisfied. |

<a id="type-mediaqueryexpression"></a>
### CSS.MediaQueryExpression

Type: object

Media query expression descriptor.

**Properties**

| Name | Type | Description |
|---|---|---|
| `value` | number | Media query expression value. |
| `unit` | string | Media query expression units. |
| `feature` | string | Media query expression feature. |
| `valueRange` (optional) | [SourceRange](#type-sourcerange) | The associated range of the value text in the enclosing stylesheet (if available). |
| `computedLength` (optional) | number | Computed length of media query expression (if applicable). |

<a id="type-csscontainerquery"></a>
### CSS.CSSContainerQuery *(experimental)*

Type: object

CSS container query rule descriptor.

**Properties**

| Name | Type | Description |
|---|---|---|
| `text` *(deprecated)* | string | Container query text. Contains the query part without the container name for a single query. Deprecated in favor of conditionText which contains the full prelude after @container. |
| `range` (optional) | [SourceRange](#type-sourcerange) | The associated rule header range in the enclosing stylesheet (if available). |
| `styleSheetId` (optional) | [DOM.StyleSheetId](DOM.md#type-stylesheetid) | Identifier of the stylesheet containing this object (if exists). |
| `name` (optional) | string | Optional name for the container. |
| `physicalAxes` (optional) | [DOM.PhysicalAxes](DOM.md#type-physicalaxes) | Optional physical axes queried for the container. |
| `logicalAxes` (optional) | [DOM.LogicalAxes](DOM.md#type-logicalaxes) | Optional logical axes queried for the container. |
| `queriesScrollState` (optional) | boolean | true if the query contains scroll-state() queries. |
| `queriesAnchored` (optional) | boolean | true if the query contains anchored() queries. |
| `conditionText` | string | CSSContainerRule.conditionText |

<a id="type-csssupports"></a>
### CSS.CSSSupports *(experimental)*

Type: object

CSS Supports at-rule descriptor.

**Properties**

| Name | Type | Description |
|---|---|---|
| `text` | string | Supports rule text. |
| `active` | boolean | Whether the supports condition is satisfied. |
| `range` (optional) | [SourceRange](#type-sourcerange) | The associated rule header range in the enclosing stylesheet (if available). |
| `styleSheetId` (optional) | [DOM.StyleSheetId](DOM.md#type-stylesheetid) | Identifier of the stylesheet containing this object (if exists). |

<a id="type-cssnavigation"></a>
### CSS.CSSNavigation *(experimental)*

Type: object

CSS Navigation at-rule descriptor.

**Properties**

| Name | Type | Description |
|---|---|---|
| `text` | string | Navigation rule text. |
| `active` (optional) | boolean | Whether the navigation condition is satisfied. |
| `range` (optional) | [SourceRange](#type-sourcerange) | The associated rule header range in the enclosing stylesheet (if available). |
| `styleSheetId` (optional) | [DOM.StyleSheetId](DOM.md#type-stylesheetid) | Identifier of the stylesheet containing this object (if exists). |

<a id="type-cssscope"></a>
### CSS.CSSScope *(experimental)*

Type: object

CSS Scope at-rule descriptor.

**Properties**

| Name | Type | Description |
|---|---|---|
| `text` | string | Scope rule text. |
| `range` (optional) | [SourceRange](#type-sourcerange) | The associated rule header range in the enclosing stylesheet (if available). |
| `styleSheetId` (optional) | [DOM.StyleSheetId](DOM.md#type-stylesheetid) | Identifier of the stylesheet containing this object (if exists). |

<a id="type-csslayer"></a>
### CSS.CSSLayer *(experimental)*

Type: object

CSS Layer at-rule descriptor.

**Properties**

| Name | Type | Description |
|---|---|---|
| `text` | string | Layer name. |
| `range` (optional) | [SourceRange](#type-sourcerange) | The associated rule header range in the enclosing stylesheet (if available). |
| `styleSheetId` (optional) | [DOM.StyleSheetId](DOM.md#type-stylesheetid) | Identifier of the stylesheet containing this object (if exists). |

<a id="type-cssstartingstyle"></a>
### CSS.CSSStartingStyle *(experimental)*

Type: object

CSS Starting Style at-rule descriptor.

**Properties**

| Name | Type | Description |
|---|---|---|
| `range` (optional) | [SourceRange](#type-sourcerange) | The associated rule header range in the enclosing stylesheet (if available). |
| `styleSheetId` (optional) | [DOM.StyleSheetId](DOM.md#type-stylesheetid) | Identifier of the stylesheet containing this object (if exists). |

<a id="type-csslayerdata"></a>
### CSS.CSSLayerData *(experimental)*

Type: object

CSS Layer data.

**Properties**

| Name | Type | Description |
|---|---|---|
| `name` | string | Layer name. |
| `subLayers` (optional) | array of [CSSLayerData](#type-csslayerdata) | Direct sub-layers |
| `order` | number | Layer order. The order determines the order of the layer in the cascade order. A higher number has higher priority in the cascade order. |

<a id="type-platformfontusage"></a>
### CSS.PlatformFontUsage

Type: object

Information about amount of glyphs that were rendered with given font.

**Properties**

| Name | Type | Description |
|---|---|---|
| `familyName` | string | Font's family name reported by platform. |
| `postScriptName` | string | Font's PostScript name reported by platform. |
| `isCustomFont` | boolean | Indicates if the font was downloaded or resolved locally. |
| `glyphCount` | number | Amount of glyphs that were rendered with this font. |

<a id="type-fontvariationaxis"></a>
### CSS.FontVariationAxis

Type: object

Information about font variation axes for variable fonts

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

Type: object

Properties of a web font: https://www.w3.org/TR/2008/REC-CSS2-20080411/fonts.html#font-descriptions and additional information such as platformFontFamily and fontVariationAxes.

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
| `fontVariationAxes` (optional) | array of [FontVariationAxis](#type-fontvariationaxis) | Available variation settings (a.k.a. "axes"). |

<a id="type-csstryrule"></a>
### CSS.CSSTryRule

Type: object

CSS try rule representation.

**Properties**

| Name | Type | Description |
|---|---|---|
| `styleSheetId` (optional) | [DOM.StyleSheetId](DOM.md#type-stylesheetid) | The css style sheet identifier (absent for user agent stylesheet and user-specified stylesheet rules) this rule came from. |
| `origin` | [StyleSheetOrigin](#type-stylesheetorigin) | Parent stylesheet's origin. |
| `style` | [CSSStyle](#type-cssstyle) | Associated style declaration. |

<a id="type-csspositiontryrule"></a>
### CSS.CSSPositionTryRule

Type: object

CSS @position-try rule representation.

**Properties**

| Name | Type | Description |
|---|---|---|
| `name` | [Value](#type-value) | The prelude dashed-ident name |
| `styleSheetId` (optional) | [DOM.StyleSheetId](DOM.md#type-stylesheetid) | The css style sheet identifier (absent for user agent stylesheet and user-specified stylesheet rules) this rule came from. |
| `origin` | [StyleSheetOrigin](#type-stylesheetorigin) | Parent stylesheet's origin. |
| `style` | [CSSStyle](#type-cssstyle) | Associated style declaration. |
| `active` | boolean |  |

<a id="type-csskeyframesrule"></a>
### CSS.CSSKeyframesRule

Type: object

CSS keyframes rule representation.

**Properties**

| Name | Type | Description |
|---|---|---|
| `animationName` | [Value](#type-value) | Animation name. |
| `keyframes` | array of [CSSKeyframeRule](#type-csskeyframerule) | List of keyframes. |

<a id="type-csspropertyregistration"></a>
### CSS.CSSPropertyRegistration

Type: object

Representation of a custom property registration through CSS.registerProperty

**Properties**

| Name | Type | Description |
|---|---|---|
| `propertyName` | string |  |
| `initialValue` (optional) | [Value](#type-value) |  |
| `inherits` | boolean |  |
| `syntax` | string |  |

<a id="type-cssatrule"></a>
### CSS.CSSAtRule

Type: object

CSS generic @rule representation.

**Properties**

| Name | Type | Description |
|---|---|---|
| `type` | enum: `font-face`, `font-feature-values`, `font-palette-values`, `counter-style` | Type of at-rule. |
| `subsection` (optional) | enum: `swash`, `annotation`, `ornaments`, `stylistic`, `styleset`, `character-variant` | Subsection of font-feature-values, if this is a subsection. |
| `name` (optional) | [Value](#type-value) | LINT.ThenChange(//third_party/blink/renderer/core/inspector/inspector_style_sheet.cc:FontVariantAlternatesFeatureType,//third_party/blink/renderer/core/inspector/inspector_css_agent.cc:FontVariantAlternatesFeatureType) Associated name, if applicable. |
| `styleSheetId` (optional) | [DOM.StyleSheetId](DOM.md#type-stylesheetid) | The css style sheet identifier (absent for user agent stylesheet and user-specified stylesheet rules) this rule came from. |
| `origin` | [StyleSheetOrigin](#type-stylesheetorigin) | Parent stylesheet's origin. |
| `style` | [CSSStyle](#type-cssstyle) | Associated style declaration. |

<a id="type-csspropertyrule"></a>
### CSS.CSSPropertyRule

Type: object

CSS property at-rule representation.

**Properties**

| Name | Type | Description |
|---|---|---|
| `styleSheetId` (optional) | [DOM.StyleSheetId](DOM.md#type-stylesheetid) | The css style sheet identifier (absent for user agent stylesheet and user-specified stylesheet rules) this rule came from. |
| `origin` | [StyleSheetOrigin](#type-stylesheetorigin) | Parent stylesheet's origin. |
| `propertyName` | [Value](#type-value) | Associated property name. |
| `style` | [CSSStyle](#type-cssstyle) | Associated style declaration. |

<a id="type-cssfunctionparameter"></a>
### CSS.CSSFunctionParameter

Type: object

CSS function argument representation.

**Properties**

| Name | Type | Description |
|---|---|---|
| `name` | string | The parameter name. |
| `type` | string | The parameter type. |

<a id="type-cssfunctionconditionnode"></a>
### CSS.CSSFunctionConditionNode

Type: object

CSS function conditional block representation.

**Properties**

| Name | Type | Description |
|---|---|---|
| `media` (optional) | [CSSMedia](#type-cssmedia) | Media query for this conditional block. Only one type of condition should be set. |
| `containerQueries` (optional) | [CSSContainerQuery](#type-csscontainerquery) | Container query for this conditional block. Only one type of condition should be set. |
| `supports` (optional) | [CSSSupports](#type-csssupports) | @supports CSS at-rule condition. Only one type of condition should be set. |
| `navigation` (optional) | [CSSNavigation](#type-cssnavigation) | @navigation condition. Only one type of condition should be set. |
| `children` | array of [CSSFunctionNode](#type-cssfunctionnode) | Block body. |
| `conditionText` | string | The condition text. |

<a id="type-cssfunctionnode"></a>
### CSS.CSSFunctionNode

Type: object

Section of the body of a CSS function rule.

**Properties**

| Name | Type | Description |
|---|---|---|
| `condition` (optional) | [CSSFunctionConditionNode](#type-cssfunctionconditionnode) | A conditional block. If set, style should not be set. |
| `style` (optional) | [CSSStyle](#type-cssstyle) | Values set by this node. If set, condition should not be set. |

<a id="type-cssfunctionrule"></a>
### CSS.CSSFunctionRule

Type: object

CSS function at-rule representation.

**Properties**

| Name | Type | Description |
|---|---|---|
| `name` | [Value](#type-value) | Name of the function. |
| `styleSheetId` (optional) | [DOM.StyleSheetId](DOM.md#type-stylesheetid) | The css style sheet identifier (absent for user agent stylesheet and user-specified stylesheet rules) this rule came from. |
| `origin` | [StyleSheetOrigin](#type-stylesheetorigin) | Parent stylesheet's origin. |
| `parameters` | array of [CSSFunctionParameter](#type-cssfunctionparameter) | List of parameters. |
| `children` | array of [CSSFunctionNode](#type-cssfunctionnode) | Function body. |
| `originTreeScopeNodeId` (optional) *(experimental)* | [DOM.BackendNodeId](DOM.md#type-backendnodeid) | The BackendNodeId of the DOM node that constitutes the origin tree scope of this rule. |

<a id="type-csskeyframerule"></a>
### CSS.CSSKeyframeRule

Type: object

CSS keyframe rule representation.

**Properties**

| Name | Type | Description |
|---|---|---|
| `styleSheetId` (optional) | [DOM.StyleSheetId](DOM.md#type-stylesheetid) | The css style sheet identifier (absent for user agent stylesheet and user-specified stylesheet rules) this rule came from. |
| `origin` | [StyleSheetOrigin](#type-stylesheetorigin) | Parent stylesheet's origin. |
| `keyText` | [Value](#type-value) | Associated key text. |
| `style` | [CSSStyle](#type-cssstyle) | Associated style declaration. |

<a id="type-styledeclarationedit"></a>
### CSS.StyleDeclarationEdit

Type: object

A descriptor of operation to mutate style declaration text.

**Properties**

| Name | Type | Description |
|---|---|---|
| `styleSheetId` | [DOM.StyleSheetId](DOM.md#type-stylesheetid) | The css style sheet identifier. |
| `range` | [SourceRange](#type-sourcerange) | The range of the style text in the enclosing stylesheet. |
| `text` | string | New style text. |

