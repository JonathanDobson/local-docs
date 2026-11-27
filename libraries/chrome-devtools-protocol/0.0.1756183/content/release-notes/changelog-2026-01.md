# Chrome DevTools Protocol changelog — 2026-01

Protocol rolls (Chromium revision `rNNNNNNN`) published in 2026-01, newest first, with the PDL diff of each. From `changelog.md` in ChromeDevTools/devtools-protocol.

## Roll protocol to r1577676 — _2026-01-31T04:48:29.000Z_
######  Diff: [`ab28501...cd6a169`](https://github.com/ChromeDevTools/devtools-protocol/compare/ab28501...cd6a169)

```diff
@@ domains/Extensions.pdl:13 @@ experimental domain Extensions
       local
       sync
       managed
+
+  # Runs an extension default action.
+  # Available if the client is connected using the --remote-debugging-pipe
+  # flag and the --enable-unsafe-extension-debugging flag is set.
+  command triggerAction
+    parameters
+      # Extension id.
+      string id
+      # A tab target ID to trigger the default extension action on.
+      string targetId
+
   # Installs an unpacked extension from the filesystem similar to
   # --load-extension CLI flags. Returns extension ID once the extension
   # has been installed. Available if the client is connected using the
@@ -22,6 +33,8 @@ experimental domain Extensions
     parameters
       # Absolute file path.
       string path
+      # Enable the extension in incognito
+      optional boolean enableInIncognito
     returns
       # Extension id.
       string id
```

## Roll protocol to r1575685 — _2026-01-28T04:36:08.000Z_
######  Diff: [`19078ce...ab28501`](https://github.com/ChromeDevTools/devtools-protocol/compare/19078ce...ab28501)

```diff
@@ browser_protocol.pdl:48 @@ include domains/PerformanceTimeline.pdl
 include domains/Preload.pdl
 include domains/Security.pdl
 include domains/ServiceWorker.pdl
+include domains/SmartCardEmulation.pdl
 include domains/Storage.pdl
 include domains/SystemInfo.pdl
 include domains/Target.pdl
```

## Roll protocol to r1574117 — _2026-01-24T04:34:09.000Z_
######  Diff: [`878c563...19078ce`](https://github.com/ChromeDevTools/devtools-protocol/compare/878c563...19078ce)

```diff
@@ domains/CSS.pdl:708 @@ experimental domain CSS
   # to the provided property syntax, the value is parsed using combined
   # syntax as if null `propertyName` was provided. If the value cannot be
   # resolved even then, return the provided value without any changes.
+  # Note: this function currently does not resolve CSS random() function,
+  # it returns unmodified random() function parts.`
   experimental command resolveValues
     parameters
       # Cascade-dependent keywords (revert/revert-layer) do not work.
diff --git a/pdl/domains/Target.pdl b/pdl/domains/Target.pdl
index 8d8ead63..e8380799 100644
--- a/pdl/domains/Target.pdl
+++ b/pdl/domains/Target.pdl
@@ -167,6 +167,14 @@ domain Target
       # present in the tab UI strip. Cannot be created with `forTab: true`, `newWindow: true` or
       # `background: false`. The life-time of the tab is limited to the life-time of the session.
       experimental optional boolean hidden
+      # If specified, the option is used to determine if the new target should
+      # be focused or not. By default, the focus behavior depends on the
+      # value of the background field. For example, background=false and focus=false
+      # will result in the target tab being opened but the browser window remain
+      # unchanged (if it was in the background, it will remain in the background)
+      # and background=false with focus=undefined will result in the window being focused.
+      # Using background: true and focus: true is not supported and will result in an error.
+      experimental optional boolean focus
     returns
       # The id of the page opened.
       TargetID targetId
```

## Roll protocol to r1573491 — _2026-01-23T04:35:32.000Z_
######  Diff: [`9e24285...878c563`](https://github.com/ChromeDevTools/devtools-protocol/compare/9e24285...878c563)

```diff
@@ domains/Network.pdl:1812 @@ domain Network
       Headers headers
       # Connection timing information for the request.
       experimental ConnectTiming connectTiming
+      # How the request site's device bound sessions were used during this request.
+      optional array of DeviceBoundSessionWithUsage deviceBoundSessionUsages
       # The client security state set for the request.
       optional ClientSecurityState clientSecurityState
       # Whether the site has partitioned cookies stored in a partition different than the current one.
@@ -2033,6 +2035,20 @@ domain Network
       # The id of the session.
       string id
 
+  # How a device bound session was used during a request.
+  experimental type DeviceBoundSessionWithUsage extends object
+    properties
+      # The key for the session.
+      DeviceBoundSessionKey sessionKey
+      # How the session was used (or not used).
+      enum usage
+        NotInScope
+        InScopeRefreshNotYetNeeded
+        InScopeRefreshNotAllowed
+        ProactiveRefreshNotPossible
+        ProactiveRefreshAttempted
+        Deferred
+
   # A device bound session's cookie craving.
   experimental type DeviceBoundSessionCookieCraving extends object
     properties
```

## Roll protocol to r1572739 — _2026-01-22T04:38:20.000Z_
######  Diff: [`f44c6e0...9e24285`](https://github.com/ChromeDevTools/devtools-protocol/compare/f44c6e0...9e24285)

```diff
@@ domains/Network.pdl:333 @@ domain Network
       # TODO(https://crbug.com/1263483): Remove this once frontend code does
       # not reference it anymore.
       PreflightInvalidAllowExternal
-      PreflightMissingAllowPrivateNetwork
-      PreflightInvalidAllowPrivateNetwork
       InvalidAllowMethodsPreflightResponse
       InvalidAllowHeadersPreflightResponse
       MethodDisallowedByPreflightResponse
@@ -345,25 +343,7 @@ domain Network
       # Request carried a target IP address space property that did not match
       # the target resource's address space.
       InvalidPrivateNetworkAccess
-      # Request was a private network request yet did not carry a target IP
-      # address space.
-      UnexpectedPrivateNetworkAccess
       NoCorsRedirectModeNotFollow
-      # Request was a private network request and needed user permission yet did
-      # not carry `Private-Network-Access-Id` in the preflight response.
-      # https://github.com/WICG/private-network-access/blob/main/permission_prompt/explainer.md
-      PreflightMissingPrivateNetworkAccessId
-      # Request was a private network request and needed user permission yet did
-      # not carry `Private-Network-Access-Name` in the preflight response.
-      # https://github.com/WICG/private-network-access/blob/main/permission_prompt/explainer.md
-      PreflightMissingPrivateNetworkAccessName
-      # Request was a private network request and needed user permission yet not
-      # able to request for permission.
-      # https://github.com/WICG/private-network-access/blob/main/permission_prompt/explainer.md
-      PrivateNetworkAccessPermissionUnavailable
-      # Request was a private network request and is denied by user permission.
-      # https://github.com/WICG/private-network-access/blob/main/permission_prompt/explainer.md
-      PrivateNetworkAccessPermissionDenied
       # Request was a local network request and is denied by user permission.
       # https://wicg.github.io/local-network-access/
       LocalNetworkAccessPermissionDenied
```

## Roll protocol to r1568893 — _2026-01-14T04:37:57.000Z_
######  Diff: [`d0d2cf0...f44c6e0`](https://github.com/ChromeDevTools/devtools-protocol/compare/d0d2cf0...f44c6e0)

```diff
@@ domains/Audits.pdl:34 @@ experimental domain Audits
       ExcludeSameSiteNoneInsecure
       ExcludeSameSiteLax
       ExcludeSameSiteStrict
-      ExcludeInvalidSameParty
-      ExcludeSamePartyCrossPartyContext
       ExcludeDomainNonASCII
       ExcludeThirdPartyCookieBlockedInFirstPartySet
       ExcludeThirdPartyPhaseout
diff --git a/pdl/domains/Network.pdl b/pdl/domains/Network.pdl
index 030fc076..c2cd6c1f 100644
--- a/pdl/domains/Network.pdl
+++ b/pdl/domains/Network.pdl
@@ -622,8 +622,6 @@ domain Network
       optional CookieSameSite sameSite
       # Cookie Priority
       experimental CookiePriority priority
-      # True if cookie is SameParty.
-      experimental deprecated boolean sameParty
       # Cookie source scheme type.
       experimental CookieSourceScheme sourceScheme
       # Cookie source port. Valid values are {-1, [1, 65535]}, -1 indicates an unspecified port.
@@ -687,12 +685,6 @@ domain Network
       # value.
       # This is the "Schemeful Same-Site" version of the blocked reason.
       SchemefulSameSiteUnspecifiedTreatedAsLax
-      # The cookie had the "SameParty" attribute but came from a cross-party response.
-      SamePartyFromCrossPartyContext
-      # The cookie had the "SameParty" attribute but did not specify the "Secure" attribute
-      # (which is required in order to use "SameParty"); or specified the "SameSite=Strict"
-      # attribute (which is forbidden when using "SameParty").
-      SamePartyConflictsWithOtherAttributes
       # The cookie's name/value pair size exceeded the size limit defined in
       # RFC6265bis.
       NameValuePairExceedsMaxSize
@@ -749,8 +741,6 @@ domain Network
       # value.
       # This is the "Schemeful Same-Site" version of the blocked reason.
       SchemefulSameSiteUnspecifiedTreatedAsLax
-      # The cookie had the "SameParty" attribute and the request was made from a cross-party context.
-      SamePartyFromCrossPartyContext
       # The cookie's name/value pair size exceeded the size limit defined in
       # RFC6265bis.
       NameValuePairExceedsMaxSize
@@ -847,8 +837,6 @@ domain Network
       optional TimeSinceEpoch expires
       # Cookie Priority.
       experimental optional CookiePriority priority
-      # True if cookie is SameParty.
-      experimental optional boolean sameParty
       # Cookie source scheme type.
       experimental optional CookieSourceScheme sourceScheme
       # Cookie source port. Valid values are {-1, [1, 65535]}, -1 indicates an unspecified port.
@@ -1317,8 +1305,6 @@ domain Network
       optional TimeSinceEpoch expires
       # Cookie Priority type.
       experimental optional CookiePriority priority
-      # True if cookie is SameParty.
-      experimental optional boolean sameParty
       # Cookie source scheme type.
       experimental optional CookieSourceScheme sourceScheme
       # Cookie source port. Valid values are {-1, [1, 65535]}, -1 indicates an unspecified port.
```

## Roll protocol to r1568225 — _2026-01-13T04:34:57.000Z_
######  Diff: [`411079d...d0d2cf0`](https://github.com/ChromeDevTools/devtools-protocol/compare/411079d...d0d2cf0)

```diff
@@ domains/Network.pdl:1216 @@ domain Network
     returns
       # Request body string, omitting files from multipart requests
       string postData
+      # True, if content was sent as base64.
+      boolean base64Encoded
 
   # Returns content served for the given currently intercepted request.
   experimental command getResponseBodyForInterception
```

## Roll protocol to r1566079 — _2026-01-08T04:35:00.000Z_
######  Diff: [`2ab0ee0...411079d`](https://github.com/ChromeDevTools/devtools-protocol/compare/2ab0ee0...411079d)

```diff
@@ domains/Network.pdl:2123 @@ domain Network
       # See comments on `net::device_bound_sessions::Session::allowed_refresh_initiators_`.
       array of string allowedRefreshInitiators
 
+  # A unique identifier for a device bound session event.
+  experimental type DeviceBoundSessionEventId extends string
+
+  # A fetch result for a device bound session creation or refresh.
+  experimental type DeviceBoundSessionFetchResult extends string
+    enum
+      Success
+      KeyError
+      SigningError
+      ServerRequestedTermination
+      InvalidSessionId
+      InvalidChallenge
+      TooManyChallenges
+      InvalidFetcherUrl
+      InvalidRefreshUrl
+      TransientHttpError
+      ScopeOriginSameSiteMismatch
+      RefreshUrlSameSiteMismatch
+      MismatchedSessionId
+      MissingScope
+      NoCredentials
+      SubdomainRegistrationWellKnownUnavailable
+      SubdomainRegistrationUnauthorized
+      SubdomainRegistrationWellKnownMalformed
+      SessionProviderWellKnownUnavailable
+      RelyingPartyWellKnownUnavailable
+      FederatedKeyThumbprintMismatch
+      InvalidFederatedSessionUrl
+      InvalidFederatedKey
+      TooManyRelyingOriginLabels
+      BoundCookieSetForbidden
+      NetError
+      ProxyError
+      EmptySessionConfig
+      InvalidCredentialsConfig
+      InvalidCredentialsType
+      InvalidCredentialsEmptyName
+      InvalidCredentialsCookie
+      PersistentHttpError
+      RegistrationAttemptedChallenge
+      InvalidScopeOrigin
+      ScopeOriginContainsPath
+      RefreshInitiatorNotString
+      RefreshInitiatorInvalidHostPattern
+      InvalidScopeSpecification
+      MissingScopeSpecificationType
+      EmptyScopeSpecificationDomain
+      EmptyScopeSpecificationPath
+      InvalidScopeSpecificationType
+      InvalidScopeIncludeSite
+      MissingScopeIncludeSite
+      FederatedNotAuthorizedByProvider
+      FederatedNotAuthorizedByRelyingParty
+      SessionProviderWellKnownMalformed
+      SessionProviderWellKnownHasProviderOrigin
+      RelyingPartyWellKnownMalformed
+      RelyingPartyWellKnownHasRelyingOrigins
+      InvalidFederatedSessionProviderSessionMissing
+      InvalidFederatedSessionWrongProviderOrigin
+      InvalidCredentialsCookieCreationTime
+      InvalidCredentialsCookieName
+      InvalidCredentialsCookieParsing
+      InvalidCredentialsCookieUnpermittedAttribute
+      InvalidCredentialsCookieInvalidDomain
+      InvalidCredentialsCookiePrefix
+      InvalidScopeRulePath
+      InvalidScopeRuleHostPattern
+      ScopeRuleOriginScopedHostPatternMismatch
+      ScopeRuleSiteScopedHostPatternMismatch
+      SigningQuotaExceeded
+      InvalidConfigJson
+      InvalidFederatedSessionProviderFailedToRestoreKey
+      FailedToUnwrapKey
+      SessionDeletedDuringRefresh
+
+  # Session event details specific to creation.
+  experimental type CreationEventDetails extends object
+    properties
+      # The result of the fetch attempt.
+      DeviceBoundSessionFetchResult fetchResult
+      # The session if there was a newly created session. This is populated for
+      # all successful creation events.
+      optional DeviceBoundSession newSession
+
+  # Session event details specific to refresh.
+  experimental type RefreshEventDetails extends object
+    properties
+      # The result of a refresh.
+      enum refreshResult
+        Refreshed
+        InitializedService
+        Unreachable
+        ServerError
+        RefreshQuotaExceeded
+        FatalError
+        SigningQuotaExceeded
+      # If there was a fetch attempt, the result of that.
+      optional DeviceBoundSessionFetchResult fetchResult
+      # The session display if there was a newly created session. This is populated
+      # for any refresh event that modifies the session config.
+      optional DeviceBoundSession newSession
+      # See comments on `net::device_bound_sessions::RefreshEventResult::was_fully_proactive_refresh`.
+      boolean wasFullyProactiveRefresh
+
+  # Session event details specific to termination.
+  experimental type TerminationEventDetails extends object
+    properties
+      # The reason for a session being deleted.
+      enum deletionReason
+        Expired
+        FailedToRestoreKey
+        FailedToUnwrapKey
+        StoragePartitionCleared
+        ClearBrowsingData
+        ServerRequested
+        InvalidSessionParams
+        RefreshFatalError
+
+  # Session event details specific to challenges.
+  experimental type ChallengeEventDetails extends object
+    properties
+      # The result of a challenge.
+      enum challengeResult
+        Success
+        NoSessionId
+        NoSessionMatch
+        CantSetBoundCookie
+      # The challenge set.
+      string challenge
+
   # Triggered when the initial set of device bound sessions is added.
   experimental event deviceBoundSessionsAdded
     parameters
       # The device bound sessions.
       array of DeviceBoundSession sessions
 
+  # Triggered when a device bound session event occurs.
+  experimental event deviceBoundSessionEventOccurred
+    parameters
+      # A unique identifier for this session event.
+      DeviceBoundSessionEventId eventId
+      # The site this session event is associated with.
+      string site
+      # Whether this event was considered successful.
+      boolean succeeded
+      # The session ID this event is associated with. May not be populated for
+      # failed events.
+      optional string sessionId
+
+      # The below are the different session event type details. Exactly one is populated.
+      optional CreationEventDetails creationEventDetails
+      optional RefreshEventDetails refreshEventDetails
+      optional TerminationEventDetails terminationEventDetails
+      optional ChallengeEventDetails challengeEventDetails
+
   # Sets up tracking device bound sessions and fetching of initial set of sessions.
   experimental command enableDeviceBoundSessions
     parameters
```

## Roll protocol to r1565416 — _2026-01-07T04:35:12.000Z_
######  Diff: [`c67e6af...2ab0ee0`](https://github.com/ChromeDevTools/devtools-protocol/compare/c67e6af...2ab0ee0)

```diff
@@ domains/Network.pdl:2057 @@ domain Network
       string origin
       array of ReportingApiEndpoint endpoints
 
+  # Unique identifier for a device bound session.
+  experimental type DeviceBoundSessionKey extends object
+    properties
+      # The site the session is set up for.
+      string site
+      # The id of the session.
+      string id
+
+  # A device bound session's cookie craving.
+  experimental type DeviceBoundSessionCookieCraving extends object
+    properties
+      # The name of the craving.
+      string name
+      # The domain of the craving.
+      string domain
+      # The path of the craving.
+      string path
+      # The `Secure` attribute of the craving attributes.
+      boolean secure
+      # The `HttpOnly` attribute of the craving attributes.
+      boolean httpOnly
+      # The `SameSite` attribute of the craving attributes.
+      optional CookieSameSite sameSite
+
+  # A device bound session's inclusion URL rule.
+  experimental type DeviceBoundSessionUrlRule extends object
+    properties
+      # See comments on `net::device_bound_sessions::SessionInclusionRules::UrlRule::rule_type`.
+      enum ruleType
+        Exclude
+        Include
+      # See comments on `net::device_bound_sessions::SessionInclusionRules::UrlRule::host_pattern`.
+      string hostPattern
+      # See comments on `net::device_bound_sessions::SessionInclusionRules::UrlRule::path_prefix`.
+      string pathPrefix
+
+  # A device bound session's inclusion rules.
+  experimental type DeviceBoundSessionInclusionRules extends object
+    properties
+      # See comments on `net::device_bound_sessions::SessionInclusionRules::origin_`.
+      string origin
+      # Whether the whole site is included. See comments on
+      # `net::device_bound_sessions::SessionInclusionRules::include_site_` for more
+      # details; this boolean is true if that value is populated.
+      boolean includeSite
+      # See comments on `net::device_bound_sessions::SessionInclusionRules::url_rules_`.
+      array of DeviceBoundSessionUrlRule urlRules
+
+  # A device bound session.
+  experimental type DeviceBoundSession extends object
+    properties
+      # The site and session ID of the session.
+      DeviceBoundSessionKey key
+      # See comments on `net::device_bound_sessions::Session::refresh_url_`.
+      string refreshUrl
+      # See comments on `net::device_bound_sessions::Session::inclusion_rules_`.
+      DeviceBoundSessionInclusionRules inclusionRules
+      # See comments on `net::device_bound_sessions::Session::cookie_cravings_`.
+      array of DeviceBoundSessionCookieCraving cookieCravings
+      # See comments on `net::device_bound_sessions::Session::expiry_date_`.
+      Network.TimeSinceEpoch expiryDate
+      # See comments on `net::device_bound_sessions::Session::cached_challenge__`.
+      optional string cachedChallenge
+      # See comments on `net::device_bound_sessions::Session::allowed_refresh_initiators_`.
+      array of string allowedRefreshInitiators
+
+  # Triggered when the initial set of device bound sessions is added.
+  experimental event deviceBoundSessionsAdded
+    parameters
+      # The device bound sessions.
+      array of DeviceBoundSession sessions
+
+  # Sets up tracking device bound sessions and fetching of initial set of sessions.
+  experimental command enableDeviceBoundSessions
+    parameters
+      # Whether to enable or disable events.
+      boolean enable
+
+  # Fetches the schemeful site for a specific origin.
+  experimental command fetchSchemefulSite
+    parameters
+      # The URL origin.
+      string origin
+    returns
+      # The corresponding schemeful site.
+      string schemefulSite
+
   # An object providing the result of a network resource load.
   experimental type LoadNetworkResourcePageResult extends object
     properties
```
