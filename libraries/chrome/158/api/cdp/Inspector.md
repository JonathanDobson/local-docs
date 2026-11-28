# Inspector domain *(experimental)*

Copyright 2017 The Chromium Authors Use of this source code is governed by a BSD-style license that can be found in the LICENSE file.  Contributing to Chrome DevTools Protocol: https://goo.gle/devtools-contribution-guide-cdp

Methods are called as `Inspector.<command>` and events arrive as `Inspector.<event>`.

## Commands

### Inspector.disable

Disables inspector domain notifications.

### Inspector.enable

Enables inspector domain notifications.

## Events

### Inspector.detached

Fired when remote debugging connection is about to be terminated. Contains detach reason.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `reason` | string | The reason why connection has been terminated. |

### Inspector.targetCrashed

Fired when debugging target has crashed

### Inspector.targetReloadedAfterCrash

Fired when debugging target has reloaded after crash

### Inspector.workerScriptLoaded *(experimental)*

Fired on worker targets when main worker script and any imported scripts have been evaluated.

