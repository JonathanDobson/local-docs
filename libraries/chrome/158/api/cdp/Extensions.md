# Extensions domain *(experimental)*

Copyright 2017 The Chromium Authors Use of this source code is governed by a BSD-style license that can be found in the LICENSE file.  Contributing to Chrome DevTools Protocol: https://goo.gle/devtools-contribution-guide-cdp Defines commands and events for browser extensions.

Methods are called as `Extensions.<command>` and events arrive as `Extensions.<event>`.

## Commands

### Extensions.triggerAction

Runs an extension default action.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `id` | string | Extension id. |
| `targetId` | string | A tab target ID to trigger the default extension action on. |

### Extensions.loadUnpacked

Installs an unpacked extension from the filesystem similar to --load-extension CLI flags. Returns extension ID once the extension has been installed.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `path` | string | Absolute file path. |
| `enableInIncognito` (optional) | boolean | Enable the extension in incognito |

**Returns**

| Name | Type | Description |
|---|---|---|
| `id` | string | Extension id. |

### Extensions.getExtensions

Gets a list of all unpacked extensions.

**Returns**

| Name | Type | Description |
|---|---|---|
| `extensions` | array of [ExtensionInfo](#type-extensioninfo) |  |

### Extensions.uninstall

Uninstalls an unpacked extension (others not supported) from the profile.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `id` | string | Extension id. |

### Extensions.getStorageItems

Gets data from extension storage in the given `storageArea`. If `keys` is specified, these are used to filter the result.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `id` | string | ID of extension. |
| `storageArea` | [StorageArea](#type-storagearea) | StorageArea to retrieve data from. |
| `keys` (optional) | array of string | Keys to retrieve. |

**Returns**

| Name | Type | Description |
|---|---|---|
| `data` | object |  |

### Extensions.removeStorageItems

Removes `keys` from extension storage in the given `storageArea`.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `id` | string | ID of extension. |
| `storageArea` | [StorageArea](#type-storagearea) | StorageArea to remove data from. |
| `keys` | array of string | Keys to remove. |

### Extensions.clearStorageItems

Clears extension storage in the given `storageArea`.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `id` | string | ID of extension. |
| `storageArea` | [StorageArea](#type-storagearea) | StorageArea to remove data from. |

### Extensions.setStorageItems

Sets `values` in extension storage in the given `storageArea`. The provided `values` will be merged with existing values in the storage area.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `id` | string | ID of extension. |
| `storageArea` | [StorageArea](#type-storagearea) | StorageArea to set data in. |
| `values` | object | Values to set. |

## Types

<a id="type-storagearea"></a>
### Extensions.StorageArea

Type: string

Storage areas.

Allowed values: `session`, `local`, `sync`, `managed`

<a id="type-extensioninfo"></a>
### Extensions.ExtensionInfo

Type: object

Detailed information about an extension.

**Properties**

| Name | Type | Description |
|---|---|---|
| `id` | string | Extension id. |
| `name` | string | Extension name. |
| `version` | string | Extension version. |
| `path` | string | The path from which the extension was loaded. |
| `enabled` | boolean | Extension enabled status. |

