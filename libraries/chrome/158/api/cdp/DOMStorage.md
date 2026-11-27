# DOMStorage domain *(experimental)*

Copyright 2017 The Chromium Authors Use of this source code is governed by a BSD-style license that can be found in the LICENSE file.  Contributing to Chrome DevTools Protocol: https://goo.gle/devtools-contribution-guide-cdp Query and modify DOM storage.

Methods are called as `DOMStorage.<command>` and events arrive as `DOMStorage.<event>`.

## Commands

### DOMStorage.clear

**Parameters**

| Name | Type | Description |
|---|---|---|
| `storageId` | [StorageId](#type-storageid) |  |

### DOMStorage.disable

Disables storage tracking, prevents storage events from being sent to the client.

### DOMStorage.enable

Enables storage tracking, storage events will now be delivered to the client.

### DOMStorage.getDOMStorageItems

**Parameters**

| Name | Type | Description |
|---|---|---|
| `storageId` | [StorageId](#type-storageid) |  |

**Returns**

| Name | Type | Description |
|---|---|---|
| `entries` | array of [Item](#type-item) |  |

### DOMStorage.removeDOMStorageItem

**Parameters**

| Name | Type | Description |
|---|---|---|
| `storageId` | [StorageId](#type-storageid) |  |
| `key` | string |  |

### DOMStorage.setDOMStorageItem

**Parameters**

| Name | Type | Description |
|---|---|---|
| `storageId` | [StorageId](#type-storageid) |  |
| `key` | string |  |
| `value` | string |  |

## Events

### DOMStorage.domStorageItemAdded

**Parameters**

| Name | Type | Description |
|---|---|---|
| `storageId` | [StorageId](#type-storageid) |  |
| `key` | string |  |
| `newValue` | string |  |

### DOMStorage.domStorageItemRemoved

**Parameters**

| Name | Type | Description |
|---|---|---|
| `storageId` | [StorageId](#type-storageid) |  |
| `key` | string |  |

### DOMStorage.domStorageItemUpdated

**Parameters**

| Name | Type | Description |
|---|---|---|
| `storageId` | [StorageId](#type-storageid) |  |
| `key` | string |  |
| `oldValue` | string |  |
| `newValue` | string |  |

### DOMStorage.domStorageItemsCleared

**Parameters**

| Name | Type | Description |
|---|---|---|
| `storageId` | [StorageId](#type-storageid) |  |

## Types

<a id="type-serializedstoragekey"></a>
### DOMStorage.SerializedStorageKey

Type: string

<a id="type-storageid"></a>
### DOMStorage.StorageId

Type: object

DOM Storage identifier.

**Properties**

| Name | Type | Description |
|---|---|---|
| `securityOrigin` (optional) | string | Security origin for the storage. |
| `storageKey` (optional) | [SerializedStorageKey](#type-serializedstoragekey) | Represents a key by which DOM Storage keys its CachedStorageAreas |
| `isLocalStorage` | boolean | Whether the storage is local storage (not session storage). |

<a id="type-item"></a>
### DOMStorage.Item

Type: array of string

DOM Storage item.

