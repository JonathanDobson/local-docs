# ServiceWorker domain

Chrome DevTools Protocol, browser protocol (tip-of-tree) (protocol 1.3).

**Experimental**

Depends on: [Target](Target.md)

12 methods, 3 events, 11 types.

## Methods

### ServiceWorker.deliverPushMessage

**Parameters**

| Name | Type | Description |
|---|---|---|
| `origin` | string |  |
| `registrationId` | [ServiceWorker.RegistrationID](#type-registrationid) |  |
| `data` | string |  |

### ServiceWorker.disable

No parameters.

### ServiceWorker.dispatchSyncEvent

**Parameters**

| Name | Type | Description |
|---|---|---|
| `origin` | string |  |
| `registrationId` | [ServiceWorker.RegistrationID](#type-registrationid) |  |
| `tag` | string |  |
| `lastChance` | boolean |  |

### ServiceWorker.dispatchPeriodicSyncEvent

**Parameters**

| Name | Type | Description |
|---|---|---|
| `origin` | string |  |
| `registrationId` | [ServiceWorker.RegistrationID](#type-registrationid) |  |
| `tag` | string |  |

### ServiceWorker.enable

No parameters.

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

No parameters.

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

**Event parameters**

| Name | Type | Description |
|---|---|---|
| `errorMessage` | [ServiceWorker.ServiceWorkerErrorMessage](#type-serviceworkererrormessage) |  |

### ServiceWorker.workerRegistrationUpdated

**Event parameters**

| Name | Type | Description |
|---|---|---|
| `registrations` | array of [ServiceWorker.ServiceWorkerRegistration](#type-serviceworkerregistration) |  |

### ServiceWorker.workerVersionUpdated

**Event parameters**

| Name | Type | Description |
|---|---|---|
| `versions` | array of [ServiceWorker.ServiceWorkerVersion](#type-serviceworkerversion) |  |

## Types

<a id="type-registrationid"></a>
### ServiceWorker.RegistrationID

Type: string

<a id="type-serviceworkerregistration"></a>
### ServiceWorker.ServiceWorkerRegistration

ServiceWorker registration.

Type: object

**Properties**

| Name | Type | Description |
|---|---|---|
| `registrationId` | [ServiceWorker.RegistrationID](#type-registrationid) |  |
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

Mostly corresponds to `RouterCondition` in ServiceWorker spec
(https://www.w3.org/TR/service-workers/#dictdef-routercondition)

Type: object

**Properties**

| Name | Type | Description |
|---|---|---|
| `urlPattern` (optional) | string | Plain text, or JSON serialization of URLPatternInit or URLPattern |
| `requestMethod` (optional) | string |  |
| `requestMode` (optional) | string |  |
| `requestDestination` (optional) | string |  |
| `runningStatus` (optional) | [ServiceWorker.ServiceWorkerVersionRunningStatus](#type-serviceworkerversionrunningstatus) |  |
| `or` (optional) | array of [ServiceWorker.ServiceWorkerRouterCondition](#type-serviceworkerroutercondition) |  |
| `not` (optional) | [ServiceWorker.ServiceWorkerRouterCondition](#type-serviceworkerroutercondition) |  |

<a id="type-serviceworkerroutersourcetype"></a>
### ServiceWorker.ServiceWorkerRouterSourceType

Type: string

Allowed values: `cache`, `fetchEvent`, `network`, `raceNetworkAndFetchHandler`, `raceNetworkAndCache`, `sourceDict`

<a id="type-serviceworkerroutersourcedict"></a>
### ServiceWorker.ServiceWorkerRouterSourceDict

https://www.w3.org/TR/service-workers/#dictdef-routersourcedict

Type: object

**Properties**

| Name | Type | Description |
|---|---|---|
| `cacheName` | string |  |

<a id="type-serviceworkerroutersource"></a>
### ServiceWorker.ServiceWorkerRouterSource

Corresponds to `RouterSource` in the spec while the representation is different as follows.
(https://www.w3.org/TR/service-workers/#typedefdef-routersource)
- `RouterSourceEnum`: `type` equals `cache`, `sourceDict` is null.
- `RouterSourceDict`: `type` equals `sourceDict`, `sourceDict` has valid value.

Type: object

**Properties**

| Name | Type | Description |
|---|---|---|
| `type` | [ServiceWorker.ServiceWorkerRouterSourceType](#type-serviceworkerroutersourcetype) |  |
| `sourceDict` (optional) | [ServiceWorker.ServiceWorkerRouterSourceDict](#type-serviceworkerroutersourcedict) | Non-empty iff `type` equals "sourceDict". |

<a id="type-serviceworkerrouterrule"></a>
### ServiceWorker.ServiceWorkerRouterRule

Type: object

**Properties**

| Name | Type | Description |
|---|---|---|
| `condition` | [ServiceWorker.ServiceWorkerRouterCondition](#type-serviceworkerroutercondition) |  |
| `source` | [ServiceWorker.ServiceWorkerRouterSource](#type-serviceworkerroutersource) |  |
| `id` | integer | Rule ID assigned by the browser. Unique within each ServiceWorkerVersion. |

<a id="type-serviceworkerversion"></a>
### ServiceWorker.ServiceWorkerVersion

ServiceWorker version.

Type: object

**Properties**

| Name | Type | Description |
|---|---|---|
| `versionId` | string |  |
| `registrationId` | [ServiceWorker.RegistrationID](#type-registrationid) |  |
| `scriptURL` | string |  |
| `runningStatus` | [ServiceWorker.ServiceWorkerVersionRunningStatus](#type-serviceworkerversionrunningstatus) |  |
| `status` | [ServiceWorker.ServiceWorkerVersionStatus](#type-serviceworkerversionstatus) |  |
| `scriptLastModified` (optional) | number | The Last-Modified header value of the main script. |
| `scriptResponseTime` (optional) | number | The time at which the response headers of the main script were received from the server. For cached script it is the last time the cache entry was validated. |
| `controlledClients` (optional) | array of [Target.TargetID](Target.md#type-targetid) |  |
| `targetId` (optional) | [Target.TargetID](Target.md#type-targetid) |  |
| `routerRules` (optional) | string | Migration to `typedRouterRules` is in progress. The browser sends either `routerRules` or `typedRouterRules`. TODO(crbug.com/540469610): Remove `routerRules` after the migration. |
| `typedRouterRules` (optional) | array of [ServiceWorker.ServiceWorkerRouterRule](#type-serviceworkerrouterrule) |  |

<a id="type-serviceworkererrormessage"></a>
### ServiceWorker.ServiceWorkerErrorMessage

ServiceWorker error message.

Type: object

**Properties**

| Name | Type | Description |
|---|---|---|
| `errorMessage` | string |  |
| `registrationId` | [ServiceWorker.RegistrationID](#type-registrationid) |  |
| `versionId` | string |  |
| `sourceURL` | string |  |
| `lineNumber` | integer |  |
| `columnNumber` | integer |  |
