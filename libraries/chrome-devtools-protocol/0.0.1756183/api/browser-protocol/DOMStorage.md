# DOMStorage domain

Chrome DevTools Protocol, browser protocol (tip-of-tree) (protocol 1.3).

**Experimental**

Query and modify DOM storage.

6 methods, 4 events, 3 types.

## Methods

### DOMStorage.clear

**Parameters**

| Name | Type | Description |
|---|---|---|
| `storageId` | [DOMStorage.StorageId](#type-storageid) |  |

### DOMStorage.disable

Disables storage tracking, prevents storage events from being sent to the client.

No parameters.

### DOMStorage.enable

Enables storage tracking, storage events will now be delivered to the client.

No parameters.

### DOMStorage.getDOMStorageItems

**Parameters**

| Name | Type | Description |
|---|---|---|
| `storageId` | [DOMStorage.StorageId](#type-storageid) |  |

**Return object**

| Name | Type | Description |
|---|---|---|
| `entries` | array of [DOMStorage.Item](#type-item) |  |

### DOMStorage.removeDOMStorageItem

**Parameters**

| Name | Type | Description |
|---|---|---|
| `storageId` | [DOMStorage.StorageId](#type-storageid) |  |
| `key` | string |  |

### DOMStorage.setDOMStorageItem

**Parameters**

| Name | Type | Description |
|---|---|---|
| `storageId` | [DOMStorage.StorageId](#type-storageid) |  |
| `key` | string |  |
| `value` | string |  |

## Events

### DOMStorage.domStorageItemAdded

**Event parameters**

| Name | Type | Description |
|---|---|---|
| `storageId` | [DOMStorage.StorageId](#type-storageid) |  |
| `key` | string |  |
| `newValue` | string |  |

### DOMStorage.domStorageItemRemoved

**Event parameters**

| Name | Type | Description |
|---|---|---|
| `storageId` | [DOMStorage.StorageId](#type-storageid) |  |
| `key` | string |  |

### DOMStorage.domStorageItemUpdated

**Event parameters**

| Name | Type | Description |
|---|---|---|
| `storageId` | [DOMStorage.StorageId](#type-storageid) |  |
| `key` | string |  |
| `oldValue` | string |  |
| `newValue` | string |  |

### DOMStorage.domStorageItemsCleared

**Event parameters**

| Name | Type | Description |
|---|---|---|
| `storageId` | [DOMStorage.StorageId](#type-storageid) |  |

## Types

<a id="type-serializedstoragekey"></a>
### DOMStorage.SerializedStorageKey

Type: string

<a id="type-storageid"></a>
### DOMStorage.StorageId

DOM Storage identifier.

Type: object

**Properties**

| Name | Type | Description |
|---|---|---|
| `securityOrigin` (optional) | string | Security origin for the storage. |
| `storageKey` (optional) | [DOMStorage.SerializedStorageKey](#type-serializedstoragekey) | Represents a key by which DOM Storage keys its CachedStorageAreas |
| `isLocalStorage` | boolean | Whether the storage is local storage (not session storage). |

<a id="type-item"></a>
### DOMStorage.Item

DOM Storage item.

Type: array of string
