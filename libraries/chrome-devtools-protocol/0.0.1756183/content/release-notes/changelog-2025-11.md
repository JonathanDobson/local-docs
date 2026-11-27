# Chrome DevTools Protocol changelog — 2025-11

Protocol rolls (Chromium revision `rNNNNNNN`) published in 2025-11, newest first, with the PDL diff of each. From `changelog.md` in ChromeDevTools/devtools-protocol.

## Roll protocol to r1551306 — _2025-11-28T04:32:25.000Z_
######  Diff: [`f64a130...47b9187`](https://github.com/ChromeDevTools/devtools-protocol/compare/f64a130...47b9187)

```diff
@@ domains/Audits.pdl:632 @@ experimental domain Audits
       # Applies to NoisedCanvasReadback issue type.
       optional SourceCodeLocation sourceCodeLocation
 
+  type PermissionElementIssueType extends string
+    enum
+      InvalidType
+      FencedFrameDisallowed
+      CspFrameAncestorsMissing
+      PermissionsPolicyBlocked
+      PaddingRightUnsupported
+      PaddingBottomUnsupported
+      InsetBoxShadowUnsupported
+      RequestInProgress
+      UntrustedEvent
+      RegistrationFailed
+      TypeNotSupported
+      InvalidTypeActivation
+      SecurityChecksFailed
+      ActivationDisabled
+      GeolocationDeprecated
+      InvalidDisplayStyle
+      NonOpaqueColor
+      LowContrast
+      FontSizeTooSmall
+      FontSizeTooLarge
+      InvalidSizeValue
+
+  # This issue warns about improper usage of the <permission> element.
+  type PermissionElementIssueDetails extends object
+    properties
+      PermissionElementIssueType issueType
+      # The value of the type attribute.
+      optional string type
+      # The node ID of the <permission> element.
+      optional DOM.BackendNodeId nodeId
+      # True if the issue is a warning, false if it is an error.
+      optional boolean isWarning
+
+      # Fields for message construction:
+      # Used for messages that reference a specific permission name
+      optional string permissionName
+      # Used for messages about occlusion
+      optional string occluderNodeInfo
+      # Used for messages about occluder's parent
+      optional string occluderParentNodeInfo
+      # Used for messages about activation disabled reason
+      optional string disableReason
+
   # A unique identifier for the type of issue. Each type may use one of the
   # optional fields in InspectorIssueDetails to convey more specific
   # information about the kind of issue.
@@ -664,6 +709,7 @@ experimental domain Audits
       SRIMessageSignatureIssue
       UnencodedDigestIssue
       UserReidentificationIssue
+      PermissionElementIssue
 
   # This struct holds a list of optional fields with additional information
   # specific to the kind of issue. When adding a new issue code, please also
@@ -696,6 +742,7 @@ experimental domain Audits
       optional SRIMessageSignatureIssueDetails sriMessageSignatureIssueDetails
       optional UnencodedDigestIssueDetails unencodedDigestIssueDetails
       optional UserReidentificationIssueDetails userReidentificationIssueDetails
+      optional PermissionElementIssueDetails permissionElementIssueDetails
 
   # A unique id for a DevTools inspector issue. Allows other entities (e.g.
   # exceptions, CDP message, console messages, etc.) to reference an issue.
diff --git a/pdl/domains/CSS.pdl b/pdl/domains/CSS.pdl
index 1b67c49f..567e30f5 100644
--- a/pdl/domains/CSS.pdl
+++ b/pdl/domains/CSS.pdl
@@ -14,8 +14,6 @@ experimental domain CSS
   depends on DOM
   depends on Page
 
-  type StyleSheetId extends string
-
   # Stylesheet type: "injected" for stylesheets injected via extension, "user-agent" for user-agent
   # stylesheets, "inspector" for stylesheets created by the inspector (i.e. those holding the "via
   # inspector" rules), "regular" for regular stylesheets.
@@ -108,7 +106,7 @@ experimental domain CSS
   type CSSStyleSheetHeader extends object
     properties
       # The stylesheet identifier.
-      StyleSheetId styleSheetId
+      DOM.StyleSheetId styleSheetId
       # Owner frame identifier.
       Page.FrameId frameId
       # Stylesheet resource URL. Empty if this is a constructed stylesheet created using
@@ -156,7 +154,7 @@ experimental domain CSS
     properties
       # The css style sheet identifier (absent for user agent stylesheet and user-specified
       # stylesheet rules) this rule came from.
-      optional StyleSheetId styleSheetId
+      optional DOM.StyleSheetId styleSheetId
       # Rule selector data.
       SelectorList selectorList
       # Array of selectors from ancestor style rules, sorted by distance from the current rule.
@@ -205,7 +203,7 @@ experimental domain CSS
     properties
       # The css style sheet identifier (absent for user agent stylesheet and user-specified
       # stylesheet rules) this rule came from.
-      StyleSheetId styleSheetId
+      DOM.StyleSheetId styleSheetId
       # Offset of the start of the rule (including selector) from the beginning of the stylesheet.
       number startOffset
       # Offset of the end of the rule body from the beginning of the stylesheet.
@@ -253,7 +251,7 @@ experimental domain CSS
     properties
       # The css style sheet identifier (absent for user agent stylesheet and user-specified
       # stylesheet rules) this rule came from.
-      optional StyleSheetId styleSheetId
+      optional DOM.StyleSheetId styleSheetId
       # CSS properties in the style.
       array of CSSProperty cssProperties
       # Computed values for all shorthands found in the style.
@@ -306,7 +304,7 @@ experimental domain CSS
       # available).
       optional SourceRange range
       # Identifier of the stylesheet containing this object (if exists).
-      optional StyleSheetId styleSheetId
+      optional DOM.StyleSheetId styleSheetId
       # Array of media queries.
       optional array of MediaQuery mediaList
 
@@ -341,7 +339,7 @@ experimental domain CSS
       # available).
       optional SourceRange range
       # Identifier of the stylesheet containing this object (if exists).
-      optional StyleSheetId styleSheetId
+      optional DOM.StyleSheetId styleSheetId
       # Optional name for the container.
       optional string name
       # Optional physical axes queried for the container.
@@ -364,7 +362,7 @@ experimental domain CSS
       # available).
       optional SourceRange range
       # Identifier of the stylesheet containing this object (if exists).
-      optional StyleSheetId styleSheetId
+      optional DOM.StyleSheetId styleSheetId
 
   # CSS Scope at-rule descriptor.
   experimental type CSSScope extends object
@@ -375,7 +373,7 @@ experimental domain CSS
       # available).
       optional SourceRange range
       # Identifier of the stylesheet containing this object (if exists).
-      optional StyleSheetId styleSheetId
+      optional DOM.StyleSheetId styleSheetId
 
   # CSS Layer at-rule descriptor.
   experimental type CSSLayer extends object
@@ -386,7 +384,7 @@ experimental domain CSS
       # available).
       optional SourceRange range
       # Identifier of the stylesheet containing this object (if exists).
-      optional StyleSheetId styleSheetId
+      optional DOM.StyleSheetId styleSheetId
 
   # CSS Starting Style at-rule descriptor.
   experimental type CSSStartingStyle extends object
@@ -395,7 +393,7 @@ experimental domain CSS
       # available).
       optional SourceRange range
       # Identifier of the stylesheet containing this object (if exists).
-      optional StyleSheetId styleSheetId
+      optional DOM.StyleSheetId styleSheetId
 
   # CSS Layer data.
   experimental type CSSLayerData extends object
@@ -464,7 +462,7 @@ experimental domain CSS
     properties
       # The css style sheet identifier (absent for user agent stylesheet and user-specified
       # stylesheet rules) this rule came from.
-      optional StyleSheetId styleSheetId
+      optional DOM.StyleSheetId styleSheetId
       # Parent stylesheet's origin.
       StyleSheetOrigin origin
       # Associated style declaration.
@@ -477,7 +475,7 @@ experimental domain CSS
       Value name
       # The css style sheet identifier (absent for user agent stylesheet and user-specified
       # stylesheet rules) this rule came from.
-      optional StyleSheetId styleSheetId
+      optional DOM.StyleSheetId styleSheetId
       # Parent stylesheet's origin.
       StyleSheetOrigin origin
       # Associated style declaration.
@@ -522,7 +520,7 @@ experimental domain CSS
       optional Value name
       # The css style sheet identifier (absent for user agent stylesheet and user-specified
       # stylesheet rules) this rule came from.
-      optional StyleSheetId styleSheetId
+      optional DOM.StyleSheetId styleSheetId
       # Parent stylesheet's origin.
       StyleSheetOrigin origin
       # Associated style declaration.
@@ -533,7 +531,7 @@ experimental domain CSS
     properties
       # The css style sheet identifier (absent for user agent stylesheet and user-specified
       # stylesheet rules) this rule came from.
-      optional StyleSheetId styleSheetId
+      optional DOM.StyleSheetId styleSheetId
       # Parent stylesheet's origin.
       StyleSheetOrigin origin
       # Associated property name.
@@ -578,7 +576,7 @@ experimental domain CSS
       Value name
       # The css style sheet identifier (absent for user agent stylesheet and user-specified
       # stylesheet rules) this rule came from.
-      optional StyleSheetId styleSheetId
+      optional DOM.StyleSheetId styleSheetId
       # Parent stylesheet's origin.
       StyleSheetOrigin origin
       # List of parameters.
@@ -591,7 +589,7 @@ experimental domain CSS
     properties
       # The css style sheet identifier (absent for user agent stylesheet and user-specified
       # stylesheet rules) this rule came from.
-      optional StyleSheetId styleSheetId
+      optional DOM.StyleSheetId styleSheetId
       # Parent stylesheet's origin.
       StyleSheetOrigin origin
       # Associated key text.
@@ -603,7 +601,7 @@ experimental domain CSS
   type StyleDeclarationEdit extends object
     properties
       # The css style sheet identifier.
-      StyleSheetId styleSheetId
+      DOM.StyleSheetId styleSheetId
       # The range of the style text in the enclosing stylesheet.
       SourceRange range
       # New style text.
@@ -614,7 +612,7 @@ experimental domain CSS
   command addRule
     parameters
       # The css style sheet identifier where a new rule should be inserted.
-      StyleSheetId styleSheetId
+      DOM.StyleSheetId styleSheetId
       # The text of a new rule.
       string ruleText
       # Text position of a new rule in the target style sheet.
@@ -630,7 +628,7 @@ experimental domain CSS
   # Returns all class names from specified stylesheet.
   command collectClassNames
     parameters
-      StyleSheetId styleSheetId
+      DOM.StyleSheetId styleSheetId
     returns
       # Class name list.
       array of string classNames
@@ -647,7 +645,7 @@ experimental domain CSS
       optional boolean force
     returns
       # Identifier of the created "via-inspector" stylesheet.
-      StyleSheetId styleSheetId
+      DOM.StyleSheetId styleSheetId
 
   # Disables the CSS agent for the given page.
   command disable
@@ -815,7 +813,7 @@ experimental domain CSS
   # Returns the current textual content for a stylesheet.
   command getStyleSheetText
     parameters
-      StyleSheetId styleSheetId
+      DOM.StyleSheetId styleSheetId
     returns
       # The stylesheet text.
       string text
@@ -834,7 +832,7 @@ experimental domain CSS
   # returns an array of locations of the CSS selector in the style sheet.
   experimental command getLocationForSelector
     parameters
-      StyleSheetId styleSheetId
+      DOM.StyleSheetId styleSheetId
       string selectorText
     returns
       array of SourceRange ranges
@@ -877,7 +875,7 @@ experimental domain CSS
   # Modifies the property rule property name.
   command setPropertyRulePropertyName
     parameters
-      StyleSheetId styleSheetId
+      DOM.StyleSheetId styleSheetId
       SourceRange range
       string propertyName
     returns
@@ -887,7 +885,7 @@ experimental domain CSS
   # Modifies the keyframe rule key text.
   command setKeyframeKey
     parameters
-      StyleSheetId styleSheetId
+      DOM.StyleSheetId styleSheetId
       SourceRange range
       string keyText
     returns
@@ -897,7 +895,7 @@ experimental domain CSS
   # Modifies the rule selector.
   command setMediaText
     parameters
-      StyleSheetId styleSheetId
+      DOM.StyleSheetId styleSheetId
       SourceRange range
       string text
     returns
@@ -907,7 +905,7 @@ experimental domain CSS
   # Modifies the expression of a container query.
   experimental command setContainerQueryText
     parameters
-      StyleSheetId styleSheetId
+      DOM.StyleSheetId styleSheetId
       SourceRange range
       string text
     returns
@@ -917,7 +915,7 @@ experimental domain CSS
   # Modifies the expression of a supports at-rule.
   experimental command setSupportsText
     parameters
-      StyleSheetId styleSheetId
+      DOM.StyleSheetId styleSheetId
       SourceRange range
       string text
     returns
@@ -927,7 +925,7 @@ experimental domain CSS
   # Modifies the expression of a scope at-rule.
   experimental command setScopeText
     parameters
-      StyleSheetId styleSheetId
+      DOM.StyleSheetId styleSheetId
       SourceRange range
       string text
     returns
@@ -937,7 +935,7 @@ experimental domain CSS
   # Modifies the rule selector.
   command setRuleSelector
     parameters
-      StyleSheetId styleSheetId
+      DOM.StyleSheetId styleSheetId
       SourceRange range
       string selector
     returns
@@ -947,7 +945,7 @@ experimental domain CSS
   # Sets the new stylesheet text.
   command setStyleSheetText
     parameters
-      StyleSheetId styleSheetId
+      DOM.StyleSheetId styleSheetId
       string text
     returns
       # URL of source map associated with script (if any).
@@ -1008,13 +1006,13 @@ experimental domain CSS
   # Fired whenever a stylesheet is changed as a result of the client operation.
   event styleSheetChanged
     parameters
-      StyleSheetId styleSheetId
+      DOM.StyleSheetId styleSheetId
 
   # Fired whenever an active document stylesheet is removed.
   event styleSheetRemoved
     parameters
       # Identifier of the removed stylesheet.
-      StyleSheetId styleSheetId
+      DOM.StyleSheetId styleSheetId
 
   experimental event computedStyleUpdated
     parameters
diff --git a/pdl/domains/DOM.pdl b/pdl/domains/DOM.pdl
index 8ac853fa..06830b09 100644
--- a/pdl/domains/DOM.pdl
+++ b/pdl/domains/DOM.pdl
@@ -21,6 +21,9 @@ domain DOM
   # front-end.
   type BackendNodeId extends integer
 
+  # Unique identifier for a CSS stylesheet.
+  type StyleSheetId extends string
+
   # Backend node with a friendly name.
   type BackendNode extends object
     properties
@@ -180,6 +183,7 @@ domain DOM
       optional BackendNode assignedSlot
       experimental optional boolean isScrollable
       experimental optional boolean affectedByStartingStyles
+      experimental optional array of StyleSheetId adoptedStyleSheets
 
   # A structure to hold the top-level node of a detached tree and an array of its retained descendants.
   type DetachedElementInfo extends object
@@ -823,6 +827,14 @@ domain DOM
       # Attribute value.
       string value
 
+  # Fired when `Element`'s adoptedStyleSheets are modified.
+  experimental event adoptedStyleSheetsModified
+    parameters
+      # Id of the node that has changed.
+      NodeId nodeId
+      # New adoptedStyleSheets array.
+      experimental array of StyleSheetId adoptedStyleSheets
+
   # Fired when `Element`'s attribute is removed.
   event attributeRemoved
     parameters
diff --git a/pdl/domains/Target.pdl b/pdl/domains/Target.pdl
index 21c4e959..d61ab3ca 100644
--- a/pdl/domains/Target.pdl
+++ b/pdl/domains/Target.pdl
@@ -265,6 +265,16 @@ domain Target
       # List of remote locations.
       array of RemoteLocation locations
 
+  # Gets the targetId of the DevTools page target opened for the given target
+  # (if any).
+  experimental command getDevToolsTarget
+    parameters
+      # Page or tab target ID.
+      TargetID targetId
+    returns
+      # The targetId of DevTools page target if exists.
+      optional TargetID targetId
+
   # Issued when attached to target because of auto-attach or `attachToTarget` command.
   experimental event attachedToTarget
     parameters
```

## Roll protocol to r1550230 — _2025-11-26T04:32:55.000Z_
######  Diff: [`3507fa9...f64a130`](https://github.com/ChromeDevTools/devtools-protocol/compare/3507fa9...f64a130)

```diff
@@ domains/Page.pdl:100 @@ domain Page
       ambient-light-sensor
       aria-notify
       attribution-reporting
+      autofill
       autoplay
       bluetooth
       browsing-topics
@@ -165,6 +166,7 @@ domain Page
       local-fonts
       local-network-access
       magnetometer
+      manual-text
       media-playback-while-not-visible
       microphone
       midi
@@ -182,7 +184,6 @@ domain Page
       run-ad-auction
       screen-wake-lock
       serial
-      shared-autofill
       shared-storage
       shared-storage-select-url
       smart-card
```

## Roll protocol to r1548823 — _2025-11-22T04:31:34.000Z_
######  Diff: [`d9682c8...3507fa9`](https://github.com/ChromeDevTools/devtools-protocol/compare/d9682c8...3507fa9)

```diff
@@ domains/Page.pdl:1767 @@ domain Page
   experimental command setPrerenderingAllowed
     parameters
       boolean isAllowed
+
+  # Get the annotated page content for the main frame.
+  # This is an experimental command that is subject to change.
+  experimental command getAnnotatedPageContent
+    parameters
+      # Whether to include actionable information. Defaults to true.
+      optional boolean includeActionableInformation
+    returns
+      # The annotated page content as a base64 encoded protobuf.
+      # The format is defined by the `AnnotatedPageContent` message in
+      # components/optimization_guide/proto/features/common_quality_data.proto
+      binary content
```

## Roll protocol to r1548244 — _2025-11-21T04:32:14.000Z_
######  Diff: [`a07bc87...d9682c8`](https://github.com/ChromeDevTools/devtools-protocol/compare/a07bc87...d9682c8)

```diff
@@ domains/CSS.pdl:500 @@ experimental domain CSS
       boolean inherits
       string syntax
 
-
-  # CSS font-palette-values rule representation.
-  type CSSFontPaletteValuesRule extends object
-    properties
-      # The css style sheet identifier (absent for user agent stylesheet and user-specified
-      # stylesheet rules) this rule came from.
-      optional StyleSheetId styleSheetId
-      # Parent stylesheet's origin.
-      StyleSheetOrigin origin
-      # Associated font palette name.
-      Value fontPaletteName
-      # Associated style declaration.
-      CSSStyle style
-
   # CSS generic @rule representation.
   type CSSAtRule extends object
     properties
@@ -800,8 +786,6 @@ experimental domain CSS
       optional array of CSSPropertyRule cssPropertyRules
       # A list of CSS property registrations matching this node.
       optional array of CSSPropertyRegistration cssPropertyRegistrations
-      # A font-palette-values rule matching this node.
-      optional CSSFontPaletteValuesRule cssFontPaletteValuesRule
       # A list of simple @rules matching this node or its pseudo-elements.
       optional array of CSSAtRule cssAtRules
       # Id of the first parent element that does not have display: contents.
```

## Roll protocol to r1547617 — _2025-11-20T04:31:52.000Z_
######  Diff: [`672dae3...a07bc87`](https://github.com/ChromeDevTools/devtools-protocol/compare/672dae3...a07bc87)

```diff
@@ domains/Network.pdl:1706 @@ domain Network
       optional number sendBufferSize
       # Expected to be unsigned integer.
       optional number receiveBufferSize
+      optional boolean multicastLoopback
+      # Unsigned int 8.
+      optional integer multicastTimeToLive
+      optional boolean multicastAllowAddressSharing
+
+  experimental event directUDPSocketJoinedMulticastGroup
+    parameters
+      RequestId identifier
+      string IPAddress
+
+  experimental event directUDPSocketLeftMulticastGroup
+    parameters
+      RequestId identifier
+      string IPAddress
 
 
   # Fired upon direct_socket.UDPSocket creation.
```

## Roll protocol to r1546284 — _2025-11-18T04:32:28.000Z_
######  Diff: [`1f03df6...672dae3`](https://github.com/ChromeDevTools/devtools-protocol/compare/1f03df6...672dae3)

```diff
@@ domains/Audits.pdl:405 @@ experimental domain Audits
       FormInputWithNoLabelError
       FormAutocompleteAttributeEmptyError
       FormEmptyIdAndNameAttributesForInputError
-      FormAriaLabelledByToNonExistingId
+      FormAriaLabelledByToNonExistingIdError
       FormInputAssignedAutocompleteValueToIdOrNameAttributeError
-      FormLabelHasNeitherForNorNestedInput
+      FormLabelHasNeitherForNorNestedInputError
       FormLabelForMatchesNonExistingIdError
       FormInputHasWrongButWellIntendedAutocompleteValueError
       ResponseWasBlockedByORB
+      NavigationEntryMarkedSkippable
 
   # Depending on the concrete errorType, different properties are set.
   type GenericIssueDetails extends object
```

## Roll protocol to r1545402 — _2025-11-15T04:31:18.000Z_
######  Diff: [`a134eaa...1f03df6`](https://github.com/ChromeDevTools/devtools-protocol/compare/a134eaa...1f03df6)

```diff
@@ domains/Network.pdl:298 @@ domain Network
       corp-not-same-site
       sri-message-signature-mismatch
 
-  # Sets Controls for IP Proxy of requests.
-  # Page reload is required before the new behavior will be observed.
-  experimental type IpProxyStatus extends string
-    enum
-      Available
-      FeatureNotEnabled
-      MaskedDomainListNotEnabled
-      MaskedDomainListNotPopulated
-      AuthTokensUnavailable
-      Unavailable
-      BypassedByDevTools
-
-  # Returns enum representing if IP Proxy of requests is available
-  # or reason it is not active.
-  experimental command getIPProtectionProxyStatus
-    returns
-      # Whether IP proxy is available
-      IpProxyStatus status
-
-  # Sets bypass IP Protection Proxy boolean.
-  experimental command setIPProtectionProxyBypassEnabled
-    parameters
-      # Whether IP Proxy is being bypassed by devtools; false by default.
-      boolean enabled
-
   # The reason why request was blocked.
   type CorsError extends string
     enum
@@ -527,9 +502,6 @@ domain Network
       Security.SecurityState securityState
       # Security details for the request.
       optional SecurityDetails securityDetails
-      # Indicates whether the request was sent through IP Protection proxies. If
-      # set to true, the request used the IP Protection privacy feature.
-      experimental optional boolean isIpProtectionUsed
 
   # WebSocket request data.
   type WebSocketRequest extends object
diff --git a/pdl/domains/Target.pdl b/pdl/domains/Target.pdl
index abe66920..21c4e959 100644
--- a/pdl/domains/Target.pdl
+++ b/pdl/domains/Target.pdl
@@ -323,7 +323,8 @@ domain Target
       # This can be the page or tab target ID.
       TargetID targetId
       # The id of the panel we want DevTools to open initially. Currently
-      # supported panels are elements, console, network, sources and resources.
+      # supported panels are elements, console, network, sources, resources
+      # and performance.
       optional string panelId
     returns
       # The targetId of DevTools page target.
```

## Roll protocol to r1543509 — _2025-11-12T04:32:18.000Z_
######  Diff: [`c40015d...a134eaa`](https://github.com/ChromeDevTools/devtools-protocol/compare/c40015d...a134eaa)

```diff
@@ domains/Page.pdl:172 @@ domain Page
       otp-credentials
       payment
       picture-in-picture
-      popins
       private-aggregation
       private-state-token-issuance
       private-state-token-redemption
```

## Roll protocol to r1541592 — _2025-11-07T04:32:19.000Z_
######  Diff: [`b8b14fd...c40015d`](https://github.com/ChromeDevTools/devtools-protocol/compare/b8b14fd...c40015d)

```diff
@@ domains/CSS.pdl:514 @@ experimental domain CSS
       # Associated style declaration.
       CSSStyle style
 
+  # CSS generic @rule representation.
+  type CSSAtRule extends object
+    properties
+      # Type of at-rule.
+      enum type
+        font-face
+        font-feature-values
+        font-palette-values
+      # Subsection of font-feature-values, if this is a subsection.
+      optional enum subsection
+        # LINT.IfChange(FontVariantAlternatesFeatureType)
+        swash
+        annotation
+        ornaments
+        stylistic
+        styleset
+        character-variant
+        # LINT.ThenChange(//third_party/blink/renderer/core/inspector/inspector_style_sheet.cc:FontVariantAlternatesFeatureType,//third_party/blink/renderer/core/inspector/inspector_css_agent.cc:FontVariantAlternatesFeatureType)
+      # Associated name, if applicable.
+      optional Value name
+      # The css style sheet identifier (absent for user agent stylesheet and user-specified
+      # stylesheet rules) this rule came from.
+      optional StyleSheetId styleSheetId
+      # Parent stylesheet's origin.
+      StyleSheetOrigin origin
+      # Associated style declaration.
+      CSSStyle style
+
   # CSS property at-rule representation.
   type CSSPropertyRule extends object
     properties
@@ -774,6 +802,8 @@ experimental domain CSS
       optional array of CSSPropertyRegistration cssPropertyRegistrations
       # A font-palette-values rule matching this node.
       optional CSSFontPaletteValuesRule cssFontPaletteValuesRule
+      # A list of simple @rules matching this node or its pseudo-elements.
+      optional array of CSSAtRule cssAtRules
       # Id of the first parent element that does not have display: contents.
       experimental optional DOM.NodeId parentLayoutNodeId
       # A list of CSS at-function rules referenced by styles of this node.
diff --git a/pdl/domains/Target.pdl b/pdl/domains/Target.pdl
index 8c7f510d..abe66920 100644
--- a/pdl/domains/Target.pdl
+++ b/pdl/domains/Target.pdl
@@ -322,6 +322,9 @@ domain Target
     parameters
       # This can be the page or tab target ID.
       TargetID targetId
+      # The id of the panel we want DevTools to open initially. Currently
+      # supported panels are elements, console, network, sources and resources.
+      optional string panelId
     returns
       # The targetId of DevTools page target.
       TargetID targetId
```

## Roll protocol to r1541017 — _2025-11-06T04:32:31.000Z_
######  Diff: [`0e79e39...b8b14fd`](https://github.com/ChromeDevTools/devtools-protocol/compare/0e79e39...b8b14fd)

```diff
@@ domains/Animation.pdl:68 @@ experimental domain Animation
       number endDelay
       # `AnimationEffect`'s iteration start.
       number iterationStart
-      # `AnimationEffect`'s iterations.
-      number iterations
+      # `AnimationEffect`'s iterations. Omitted if the value is infinite.
+      optional number iterations
       # `AnimationEffect`'s iteration duration.
       # Milliseconds for time based animations and
       # percentage [0 - 100] for scroll driven animations
diff --git a/pdl/domains/DOM.pdl b/pdl/domains/DOM.pdl
index 71a50b6f..8ac853fa 100644
--- a/pdl/domains/DOM.pdl
+++ b/pdl/domains/DOM.pdl
@@ -72,6 +72,8 @@ domain DOM
       details-content
       picker
       permission-icon
+      overscroll-area-parent
+      overscroll-client-area
 
   # Shadow root type.
   type ShadowRootType extends string
```

## Roll protocol to r1538951 — _2025-11-01T04:30:31.000Z_
######  Diff: [`b8a7fa7...0e79e39`](https://github.com/ChromeDevTools/devtools-protocol/compare/b8a7fa7...0e79e39)

```diff
@@ domains/Network.pdl:1797 @@ domain Network
       Allow
       BlockFromInsecureToMorePrivate
       WarnFromInsecureToMorePrivate
-      PreflightBlock
-      PreflightWarn
       PermissionBlock
       PermissionWarn
```
