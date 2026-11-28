# ServiceWorker domain *(experimental)*

Copyright 2017 The Chromium Authors Use of this source code is governed by a BSD-style license that can be found in the LICENSE file.  Contributing to Chrome DevTools Protocol: https://goo.gle/devtools-contribution-guide-cdp

Depends on: [Target](Target.md)

Methods are called as `ServiceWorker.<command>` and events arrive as `ServiceWorker.<event>`.

## Commands

### ServiceWorker.deliverPushMessage

**Parameters**

| Name | Type | Description |
|---|---|---|
| `origin` | string |  |
| `registrationId` | [RegistrationID](#type-registrationid) |  |
| `data` | string |  |

### ServiceWorker.disable

### ServiceWorker.dispatchSyncEvent

**Parameters**

| Name | Type | Description |
|---|---|---|
| `origin` | string |  |
| `registrationId` | [RegistrationID](#type-registrationid) |  |
| `tag` | string |  |
| `lastChance` | boolean |  |

### ServiceWorker.dispatchPeriodicSyncEvent

**Parameters**

| Name | Type | Description |
|---|---|---|
| `origin` | string |  |
| `registrationId` | [RegistrationID](#type-registrationid) |  |
| `tag` | string |  |

### ServiceWorker.enable

### ServiceWorker.setForceUpdateOnPageLoad

**Parameters**

| Name | Type | Description |
|---|---|---|
| `forceUpdateOnPageLoad` | boolean |  |

### ServiceWorker.skipWaiting

**Parameters**

| Name | Type | Description |
|---|---|---|
| `scopeURL` | string |  |

### ServiceWorker.startWorker

**Parameters**

| Name | Type | Description |
|---|---|---|
| `scopeURL` | string |  |

### ServiceWorker.stopAllWorkers

### ServiceWorker.stopWorker

**Parameters**

| Name | Type | Description |
|---|---|---|
| `versionId` | string |  |

### ServiceWorker.unregister

**Parameters**

| Name | Type | Description |
|---|---|---|
| `scopeURL` | string |  |

### ServiceWorker.updateRegistration

**Parameters**

| Name | Type | Description |
|---|---|---|
| `scopeURL` | string |  |

## Events

### ServiceWorker.workerErrorReported

**Parameters**

| Name | Type | Description |
|---|---|---|
| `errorMessage` | [ServiceWorkerErrorMessage](#type-serviceworkererrormessage) |  |

### ServiceWorker.workerRegistrationUpdated

**Parameters**

| Name | Type | Description |
|---|---|---|
| `registrations` | array of [ServiceWorkerRegistration](#type-serviceworkerregistration) |  |

### ServiceWorker.workerVersionUpdated

**Parameters**

| Name | Type | Description |
|---|---|---|
| `versions` | array of [ServiceWorkerVersion](#type-serviceworkerversion) |  |

## Types

<a id="type-registrationid"></a>
### ServiceWorker.RegistrationID

Type: string

<a id="type-serviceworkerregistration"></a>
### ServiceWorker.ServiceWorkerRegistration

Type: object

ServiceWorker registration.

**Properties**

| Name | Type | Description |
|---|---|---|
| `registrationId` | [RegistrationID](#type-registrationid) |  |
| `scopeURL` | string |  |
| `isDeleted` | boolean |  |

<a id="type-serviceworkerversionrunningstatus"></a>
### ServiceWorker.ServiceWorkerVersionRunningStatus

Type: string

Allowed values: `stopped`, `starting`, `running`, `stopping`

<a id="type-serviceworkerversionstatus"></a>
### ServiceWorker.ServiceWorkerVersionStatus

Type: string

Allowed values: `new`, `installing`, `installed`, `activating`, `activated`, `redundant`

<a id="type-serviceworkerroutercondition"></a>
### ServiceWorker.ServiceWorkerRouterCondition

Type: object

Mostly corresponds to `RouterCondition` in ServiceWorker spec (https://www.w3.org/TR/service-workers/#dictdef-routercondition)

**Properties**

| Name | Type | Description |
|---|---|---|
| `urlPattern` (optional) | string | Plain text, or JSON serialization of URLPatternInit or URLPattern |
| `requestMethod` (optional) | string |  |
| `requestMode` (optional) | string |  |
| `requestDestination` (optional) | string |  |
| `runningStatus` (optional) | [ServiceWorkerVersionRunningStatus](#type-serviceworkerversionrunningstatus) |  |
| `or` (optional) | array of [ServiceWorkerRouterCondition](#type-serviceworkerroutercondition) |  |
| `not` (optional) | [ServiceWorkerRouterCondition](#type-serviceworkerroutercondition) |  |

<a id="type-serviceworkerroutersourcetype"></a>
### ServiceWorker.ServiceWorkerRouterSourceType

Type: string

Allowed values: `cache`, `fetchEvent`, `network`, `raceNetworkAndFetchHandler`, `raceNetworkAndCache`, `sourceDict`

<a id="type-serviceworkerroutersourcedict"></a>
### ServiceWorker.ServiceWorkerRouterSourceDict

Type: object

https://www.w3.org/TR/service-workers/#dictdef-routersourcedict

**Properties**

| Name | Type | Description |
|---|---|---|
| `cacheName` | string |  |

<a id="type-serviceworkerroutersource"></a>
### ServiceWorker.ServiceWorkerRouterSource

Type: object

Corresponds to `RouterSource` in the spec while the representation is different as follows. (https://www.w3.org/TR/service-workers/#typedefdef-routersource) - `RouterSourceEnum`: `type` equals `cache`, `sourceDict` is null. - `RouterSourceDict`: `type` equals `sourceDict`, `sourceDict` has valid value.

**Properties**

| Name | Type | Description |
|---|---|---|
| `type` | [ServiceWorkerRouterSourceType](#type-serviceworkerroutersourcetype) |  |
| `sourceDict` (optional) | [ServiceWorkerRouterSourceDict](#type-serviceworkerroutersourcedict) | Non-empty iff `type` equals "sourceDict". |

<a id="type-serviceworkerrouterrule"></a>
### ServiceWorker.ServiceWorkerRouterRule

Type: object

**Properties**

| Name | Type | Description |
|---|---|---|
| `condition` | [ServiceWorkerRouterCondition](#type-serviceworkerroutercondition) |  |
| `source` | [ServiceWorkerRouterSource](#type-serviceworkerroutersource) |  |
| `id` | integer | Rule ID assigned by the browser. Unique within each ServiceWorkerVersion. |

<a id="type-serviceworkerversion"></a>
### ServiceWorker.ServiceWorkerVersion

Type: object

ServiceWorker version.

**Properties**

| Name | Type | Description |
|---|---|---|
| `versionId` | string |  |
| `registrationId` | [RegistrationID](#type-registrationid) |  |
| `scriptURL` | string |  |
| `runningStatus` | [ServiceWorkerVersionRunningStatus](#type-serviceworkerversionrunningstatus) |  |
| `status` | [ServiceWorkerVersionStatus](#type-serviceworkerversionstatus) |  |
| `scriptLastModified` (optional) | number | The Last-Modified header value of the main script. |
| `scriptResponseTime` (optional) | number | The time at which the response headers of the main script were received from the server. For cached script it is the last time the cache entry was validated. |
| `controlledClients` (optional) | array of [Target.TargetID](Target.md#type-targetid) |  |
| `targetId` (optional) | [Target.TargetID](Target.md#type-targetid) |  |
| `routerRules` (optional) | string | Migration to `typedRouterRules` is in progress. The browser sends either `routerRules` or `typedRouterRules`. TODO(crbug.com/540469610): Remove `routerRules` after the migration. |
| `typedRouterRules` (optional) | array of [ServiceWorkerRouterRule](#type-serviceworkerrouterrule) |  |

<a id="type-serviceworkererrormessage"></a>
### ServiceWorker.ServiceWorkerErrorMessage

Type: object

ServiceWorker error message.

**Properties**

| Name | Type | Description |
|---|---|---|
| `errorMessage` | string |  |
| `registrationId` | [RegistrationID](#type-registrationid) |  |
| `versionId` | string |  |
| `sourceURL` | string |  |
| `lineNumber` | integer |  |
| `columnNumber` | integer |  |

