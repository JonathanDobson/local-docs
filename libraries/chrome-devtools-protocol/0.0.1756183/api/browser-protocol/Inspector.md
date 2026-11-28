# Inspector domain

Chrome DevTools Protocol, browser protocol (tip-of-tree) (protocol 1.3).

**Experimental**

2 methods, 4 events, 0 types.

## Methods

### Inspector.disable

Disables inspector domain notifications.

No parameters.

### Inspector.enable

Enables inspector domain notifications.

No parameters.

## Events

### Inspector.detached

Fired when remote debugging connection is about to be terminated. Contains detach reason.

**Event parameters**

| Name | Type | Description |
|---|---|---|
| `reason` | string | The reason why connection has been terminated. |

### Inspector.targetCrashed

Fired when debugging target has crashed

### Inspector.targetReloadedAfterCrash

Fired when debugging target has reloaded after crash

### Inspector.workerScriptLoaded

**Experimental**

Fired on worker targets when main worker script and any imported scripts have been evaluated.
