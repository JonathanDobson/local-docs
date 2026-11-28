# Extensions domain

Chrome DevTools Protocol, browser protocol (tip-of-tree) (protocol 1.3).

**Experimental**

Defines commands and events for browser extensions.

8 methods, 0 events, 2 types.

## Methods

### Extensions.triggerAction

Runs an extension default action.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `id` | string | Extension id. |
| `targetId` | string | A tab target ID to trigger the default extension action on. |

### Extensions.loadUnpacked

Installs an unpacked extension from the filesystem similar to
--load-extension CLI flags. Returns extension ID once the extension
has been installed.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `path` | string | Absolute file path. |
| `enableInIncognito` (optional) | boolean | Enable the extension in incognito |

**Return object**

| Name | Type | Description |
|---|---|---|
| `id` | string | Extension id. |

### Extensions.getExtensions

Gets a list of all unpacked extensions.

No parameters.

**Return object**

| Name | Type | Description |
|---|---|---|
| `extensions` | array of [Extensions.ExtensionInfo](#type-extensioninfo) |  |

### Extensions.uninstall

Uninstalls an unpacked extension (others not supported) from the profile.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `id` | string | Extension id. |

### Extensions.getStorageItems

Gets data from extension storage in the given `storageArea`. If `keys` is
specified, these are used to filter the result.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `id` | string | ID of extension. |
| `storageArea` | [Extensions.StorageArea](#type-storagearea) | StorageArea to retrieve data from. |
| `keys` (optional) | array of string | Keys to retrieve. |

**Return object**

| Name | Type | Description |
|---|---|---|
| `data` | object |  |

### Extensions.removeStorageItems

Removes `keys` from extension storage in the given `storageArea`.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `id` | string | ID of extension. |
| `storageArea` | [Extensions.StorageArea](#type-storagearea) | StorageArea to remove data from. |
| `keys` | array of string | Keys to remove. |

### Extensions.clearStorageItems

Clears extension storage in the given `storageArea`.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `id` | string | ID of extension. |
| `storageArea` | [Extensions.StorageArea](#type-storagearea) | StorageArea to remove data from. |

### Extensions.setStorageItems

Sets `values` in extension storage in the given `storageArea`. The provided `values`
will be merged with existing values in the storage area.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `id` | string | ID of extension. |
| `storageArea` | [Extensions.StorageArea](#type-storagearea) | StorageArea to set data in. |
| `values` | object | Values to set. |

## Types

<a id="type-storagearea"></a>
### Extensions.StorageArea

Storage areas.

Type: string

Allowed values: `session`, `local`, `sync`, `managed`

<a id="type-extensioninfo"></a>
### Extensions.ExtensionInfo

Detailed information about an extension.

Type: object

**Properties**

| Name | Type | Description |
|---|---|---|
| `id` | string | Extension id. |
| `name` | string | Extension name. |
| `version` | string | Extension version. |
| `path` | string | The path from which the extension was loaded. |
| `enabled` | boolean | Extension enabled status. |
