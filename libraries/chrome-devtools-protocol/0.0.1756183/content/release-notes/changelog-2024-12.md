# Chrome DevTools Protocol changelog — 2024-12

Protocol rolls (Chromium revision `rNNNNNNN`) published in 2024-12, newest first, with the PDL diff of each. From `changelog.md` in ChromeDevTools/devtools-protocol.

## Roll protocol to r1400418 — _2024-12-27T04:28:57.000Z_
######  Diff: [`6abdabb...1f97d3a`](https://github.com/ChromeDevTools/devtools-protocol/compare/6abdabb...1f97d3a)

```diff
@@ browser_protocol.pdl:984 @@ experimental domain Audits
       string failureMessage
       optional Network.RequestId requestId
 
+  type SelectElementAccessibilityIssueReason extends string
+    enum
+      DisallowedSelectChild
+      DisallowedOptGroupChild
+      NonPhrasingContentOptionChild
+      InteractiveContentOptionChild
+      InteractiveContentLegendChild
+
+  # This isue warns about errors in the select element content model.
+  type SelectElementAccessibilityIssueDetails extends object
+    properties
+      DOM.BackendNodeId nodeId
+      SelectElementAccessibilityIssueReason selectElementAccessibilityIssueReason
+      boolean hasDisallowedAttributes
+
+
   type StyleSheetLoadingIssueReason extends string
     enum
       LateImportRule
@@ -1044,6 +1060,7 @@ experimental domain Audits
       FederatedAuthUserInfoRequestIssue
       PropertyRuleIssue
       SharedDictionaryIssue
+      SelectElementAccessibilityIssue
 
   # This struct holds a list of optional fields with additional information
   # specific to the kind of issue. When adding a new issue code, please also
@@ -1071,6 +1088,7 @@ experimental domain Audits
       optional PropertyRuleIssueDetails propertyRuleIssueDetails
       optional FederatedAuthUserInfoRequestIssueDetails federatedAuthUserInfoRequestIssueDetails
       optional SharedDictionaryIssueDetails sharedDictionaryIssueDetails
+      optional SelectElementAccessibilityIssueDetails selectElementAccessibilityIssueDetails
 
   # A unique id for a DevTools inspector issue. Allows other entities (e.g.
   # exceptions, CDP message, console messages, etc.) to reference an issue.
@@ -11258,6 +11276,10 @@ domain Target
     parameters
       # The initial URL the page will be navigated to. An empty string indicates about:blank.
       string url
+      # Frame left origin in DIP (headless chrome only).
+      experimental optional integer left
+      # Frame top origin in DIP (headless chrome only).
+      experimental optional integer top
       # Frame width in DIP (headless chrome only).
       optional integer width
       # Frame height in DIP (headless chrome only).
```

## Roll protocol to r1399977 — _2024-12-24T04:29:08.000Z_
######  Diff: [`17f0c33...6abdabb`](https://github.com/ChromeDevTools/devtools-protocol/compare/17f0c33...6abdabb)

```diff
@@ browser_protocol.pdl:499 @@ experimental domain Audits
   type AffectedRequest extends object
     properties
       # The unique request id.
-      Network.RequestId requestId
-      optional string url
+      optional Network.RequestId requestId
+      string url
 
   # Information about the frame affected by an inspector issue.
   type AffectedFrame extends object
```

## Roll protocol to r1396320 — _2024-12-14T04:29:52.000Z_
######  Diff: [`e61f211...17f0c33`](https://github.com/ChromeDevTools/devtools-protocol/compare/e61f211...17f0c33)

```diff
@@ browser_protocol.pdl:2255 @@ experimental domain CSS
       # Element pseudo classes to force when computing the element's style.
       array of string forcedPseudoClasses
 
+  # Ensures that the given node is in its starting-style state.
+  command forceStartingStyle
+    parameters
+      # The element id for which to force the starting-style state.
+      DOM.NodeId nodeId
+      # Boolean indicating if this is on or off.
+      boolean forced
+
   command getBackgroundColors
     parameters
       # Id of the node to get background colors for.
```

## Roll protocol to r1395251 — _2024-12-12T04:30:26.000Z_
######  Diff: [`dff3f42...e61f211`](https://github.com/ChromeDevTools/devtools-protocol/compare/dff3f42...e61f211)

```diff
@@ browser_protocol.pdl:1701 @@ experimental domain CSS
       # Matches of CSS rules applicable to the pseudo style.
       array of RuleMatch matches
 
+  # CSS style coming from animations with the name of the animation.
+  type CSSAnimationStyle extends object
+    properties
+      # The name of the animation.
+      optional string name
+      # The style coming from the animation.
+      CSSStyle style
+
   # Inherited CSS rule collection from ancestor node.
   type InheritedStyleEntry extends object
     properties
@@ -1709,6 +1717,14 @@ experimental domain CSS
       # Matches of CSS rules matching the ancestor node in the style inheritance chain.
       array of RuleMatch matchedCSSRules
 
+  # Inherited CSS style collection for animated styles from ancestor node.
+  type InheritedAnimatedStyleEntry extends object
+    properties
+      # Styles coming from the animations of the ancestor, if any, in the style inheritance chain.
+      optional array of CSSAnimationStyle animationStyles
+      # The style coming from the transitions of the ancestor, if any, in the style inheritance chain.
+      optional CSSStyle transitionsStyle
+
   # Inherited pseudo element matches from pseudos of an ancestor node.
   type InheritedPseudoElementMatches extends object
     properties
@@ -2296,6 +2312,20 @@ experimental domain CSS
       # Attribute-defined element style (e.g. resulting from "width=20 height=100%").
       optional CSSStyle attributesStyle
 
+  # Returns the styles coming from animations & transitions
+  # including the animation & transition styles coming from inheritance chain.
+  experimental command getAnimatedStylesForNode
+    parameters
+      DOM.NodeId nodeId
+    returns
+      # Styles coming from animations.
+      optional array of CSSAnimationStyle animationStyles
+      # Style coming from transitions.
+      optional CSSStyle transitionsStyle
+      # Inherited style entries for animationsStyle and transitionsStyle from
+      # the inheritance chain of the element.
+      optional array of InheritedAnimatedStyleEntry inherited
+
   # Returns requested styles for a DOM node identified by `nodeId`.
   command getMatchedStylesForNode
     parameters
```

## Roll protocol to r1393284 — _2024-12-07T04:30:05.000Z_
######  Diff: [`d2f3487...dff3f42`](https://github.com/ChromeDevTools/devtools-protocol/compare/d2f3487...dff3f42)

```diff
@@ js_protocol.pdl:641 @@ domain Debugger
       Runtime.ExecutionContextId executionContextId
       # Content hash of the script, SHA-256.
       string hash
+      # For Wasm modules, the content of the `build_id` custom section.
+      string buildId
       # Embedder-specific auxiliary data likely matching {isDefault: boolean, type: 'default'|'isolated'|'worker', frameId: string}
       optional object executionContextAuxData
       # URL of source map associated with script (if any).
@@ -680,6 +682,8 @@ domain Debugger
       Runtime.ExecutionContextId executionContextId
       # Content hash of the script, SHA-256.
       string hash
+      # For Wasm modules, the content of the `build_id` custom section.
+      string buildId
       # Embedder-specific auxiliary data likely matching {isDefault: boolean, type: 'default'|'isolated'|'worker', frameId: string}
       optional object executionContextAuxData
       # True, if this script is generated as a result of the live edit operation.
```

## Roll protocol to r1392711 — _2024-12-06T04:30:32.000Z_
######  Diff: [`4f13107...d2f3487`](https://github.com/ChromeDevTools/devtools-protocol/compare/4f13107...d2f3487)

```diff
@@ browser_protocol.pdl:2264 @@ experimental domain CSS
       # Computed style for the specified DOM node.
       array of CSSComputedStyleProperty computedStyle
 
+  # Resolve the specified values in the context of the provided element.
+  # For example, a value of '1em' is evaluated according to the computed
+  # 'font-size' of the element and a value 'calc(1px + 2px)' will be
+  # resolved to '3px'.
+  command resolveValues
+    parameters
+      # Substitution functions (var()/env()/attr()) and cascade-dependent
+      # keywords (revert/revert-layer) do not work.
+      array of string values
+      # Id of the node in whose context the expression is evaluated
+      DOM.NodeId nodeId
+      # Only longhands and custom property names are accepted.
+      optional string propertyName
+      # Pseudo element type, only works for pseudo elements that generate
+      # elements in the tree, such as ::before and ::after.
+      experimental optional DOM.PseudoType pseudoType
+      # Pseudo element custom ident.
+      experimental optional string pseudoIdentifier
+    returns
+      array of string results
+
   # Returns the styles defined inline (explicitly in the "style" attribute and implicitly, using DOM
   # attributes) for a DOM node identified by `nodeId`.
   command getInlineStylesForNode
@@ -7293,6 +7314,9 @@ domain Network
       # are represented by the invalid cookie line string instead of a proper cookie.
       array of BlockedSetCookieWithReason blockedCookies
       # Raw response headers as they were received over the wire.
+      # Duplicate headers in the response are represented as a single key with their values
+      # concatentated using `\n` as the separator.
+      # See also `headersText` that contains verbatim text for HTTP/1.*.
       Headers headers
       # The IP address space of the resource. The address space can only be determined once the transport
       # established the connection, so we can't send it in `requestWillBeSentExtraInfo`.
@@ -7321,6 +7345,9 @@ domain Network
       # Request identifier. Used to match this information to another responseReceived event.
       RequestId requestId
       # Raw response headers as they were received over the wire.
+      # Duplicate headers in the response are represented as a single key with their values
+      # concatentated using `\n` as the separator.
+      # See also `headersText` that contains verbatim text for HTTP/1.*.
       Headers headers
 
   # Fired exactly once for each Trust Token operation. Depending on
```

## Roll protocol to r1392070 — _2024-12-05T04:30:37.000Z_
######  Diff: [`49fd69e...4f13107`](https://github.com/ChromeDevTools/devtools-protocol/compare/49fd69e...4f13107)

```diff
@@ browser_protocol.pdl:12424 @@ experimental domain Preload
       array of RuleSetId ruleSetIds
       array of DOM.BackendNodeId nodeIds
 
+  # Chrome manages different types of preloads together using a
+  # concept of preloading pipeline. For example, if a site uses a
+  # SpeculationRules for prerender, Chrome first starts a prefetch and
+  # then upgrades it to prerender.
+  #
+  # CDP events for them are emitted separately but they share
+  # `PreloadPipelineId`.
+  type PreloadPipelineId extends string
+
   command enable
 
   command disable
@@ -12580,6 +12589,7 @@ experimental domain Preload
   event prefetchStatusUpdated
     parameters
       PreloadingAttemptKey key
+      PreloadPipelineId pipelineId
       # The frame id of the frame initiating prefetch.
       Page.FrameId initiatingFrameId
       string prefetchUrl
@@ -12598,6 +12608,7 @@ experimental domain Preload
   event prerenderStatusUpdated
     parameters
       PreloadingAttemptKey key
+      PreloadPipelineId pipelineId
       PreloadingStatus status
       optional PrerenderFinalStatus prerenderStatus
       # This is used to give users more information about the name of Mojo interface
```

## Roll protocol to r1391447 — _2024-12-04T04:30:22.000Z_
######  Diff: [`33ab53c...49fd69e`](https://github.com/ChromeDevTools/devtools-protocol/compare/33ab53c...49fd69e)

```diff
@@ browser_protocol.pdl:2743 @@ domain DOM
       checkmark
       before
       after
-      select-arrow
+      picker-icon
       marker
       backdrop
       column
```
