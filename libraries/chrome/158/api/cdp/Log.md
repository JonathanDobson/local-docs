# Log domain

Copyright 2017 The Chromium Authors Use of this source code is governed by a BSD-style license that can be found in the LICENSE file.  Contributing to Chrome DevTools Protocol: https://goo.gle/devtools-contribution-guide-cdp Provides access to log entries.

Depends on: [Runtime](Runtime.md), [Network](Network.md)

Methods are called as `Log.<command>` and events arrive as `Log.<event>`.

## Commands

### Log.clear

Clears the log.

### Log.disable

Disables log domain, prevents further log entries from being reported to the client.

### Log.enable

Enables log domain, sends the entries collected so far to the client by means of the `entryAdded` notification.

### Log.startViolationsReport

start violation reporting.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `config` | array of [ViolationSetting](#type-violationsetting) | Configuration for violations. |

### Log.stopViolationsReport

Stop violation reporting.

## Events

### Log.entryAdded

Issued when new message was logged.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `entry` | [LogEntry](#type-logentry) | The entry. |

## Types

<a id="type-logentry"></a>
### Log.LogEntry

Type: object

Log entry.

**Properties**

| Name | Type | Description |
|---|---|---|
| `source` | enum: `xml`, `javascript`, `network`, `storage`, `appcache`, `rendering`, `security`, `deprecation`, `worker`, `violation`, `intervention`, `recommendation`, `other` | Log entry source. |
| `level` | enum: `verbose`, `info`, `warning`, `error` | Log entry severity. |
| `text` | string | Logged text. |
| `category` (optional) | enum: `cors` |  |
| `timestamp` | [Runtime.Timestamp](Runtime.md#type-timestamp) | Timestamp when this entry was added. |
| `url` (optional) | string | URL of the resource if known. |
| `lineNumber` (optional) | integer | Line number in the resource. |
| `stackTrace` (optional) | [Runtime.StackTrace](Runtime.md#type-stacktrace) | JavaScript stack trace. |
| `networkRequestId` (optional) | [Network.RequestId](Network.md#type-requestid) | Identifier of the network request associated with this entry. |
| `workerId` (optional) | string | Identifier of the worker associated with this entry. |
| `args` (optional) | array of [Runtime.RemoteObject](Runtime.md#type-remoteobject) | Call arguments. |

<a id="type-violationsetting"></a>
### Log.ViolationSetting

Type: object

Violation configuration setting.

**Properties**

| Name | Type | Description |
|---|---|---|
| `name` | enum: `longTask`, `longLayout`, `blockedEvent`, `blockedParser`, `discouragedAPIUse`, `handler`, `recurringHandler` | Violation type. |
| `threshold` | number | Time threshold to trigger upon. |

