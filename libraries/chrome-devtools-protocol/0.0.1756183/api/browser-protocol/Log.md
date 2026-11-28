# Log domain

Chrome DevTools Protocol, browser protocol (tip-of-tree) (protocol 1.3).

Provides access to log entries.

Depends on: [Runtime](Runtime.md), [Network](Network.md)

5 methods, 1 events, 2 types.

## Methods

### Log.clear

Clears the log.

No parameters.

### Log.disable

Disables log domain, prevents further log entries from being reported to the client.

No parameters.

### Log.enable

Enables log domain, sends the entries collected so far to the client by means of the
`entryAdded` notification.

No parameters.

### Log.startViolationsReport

start violation reporting.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `config` | array of [Log.ViolationSetting](#type-violationsetting) | Configuration for violations. |

### Log.stopViolationsReport

Stop violation reporting.

No parameters.

## Events

### Log.entryAdded

Issued when new message was logged.

**Event parameters**

| Name | Type | Description |
|---|---|---|
| `entry` | [Log.LogEntry](#type-logentry) | The entry. |

## Types

<a id="type-logentry"></a>
### Log.LogEntry

Log entry.

Type: object

**Properties**

| Name | Type | Description |
|---|---|---|
| `source` | string | Log entry source. Allowed values: `xml`, `javascript`, `network`, `storage`, `appcache`, `rendering`, `security`, `deprecation`, `worker`, `violation`, `intervention`, `recommendation`, `other` |
| `level` | string | Log entry severity. Allowed values: `verbose`, `info`, `warning`, `error` |
| `text` | string | Logged text. |
| `category` (optional) | string | Allowed values: `cors` |
| `timestamp` | [Runtime.Timestamp](Runtime.md#type-timestamp) | Timestamp when this entry was added. |
| `url` (optional) | string | URL of the resource if known. |
| `lineNumber` (optional) | integer | Line number in the resource. |
| `stackTrace` (optional) | [Runtime.StackTrace](Runtime.md#type-stacktrace) | JavaScript stack trace. |
| `networkRequestId` (optional) | [Network.RequestId](Network.md#type-requestid) | Identifier of the network request associated with this entry. |
| `workerId` (optional) | string | Identifier of the worker associated with this entry. |
| `args` (optional) | array of [Runtime.RemoteObject](Runtime.md#type-remoteobject) | Call arguments. |

<a id="type-violationsetting"></a>
### Log.ViolationSetting

Violation configuration setting.

Type: object

**Properties**

| Name | Type | Description |
|---|---|---|
| `name` | string | Violation type. Allowed values: `longTask`, `longLayout`, `blockedEvent`, `blockedParser`, `discouragedAPIUse`, `handler`, `recurringHandler` |
| `threshold` | number | Time threshold to trigger upon. |
