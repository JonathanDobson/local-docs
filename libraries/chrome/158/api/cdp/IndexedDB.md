# IndexedDB domain *(experimental)*

Copyright 2017 The Chromium Authors Use of this source code is governed by a BSD-style license that can be found in the LICENSE file.  Contributing to Chrome DevTools Protocol: https://goo.gle/devtools-contribution-guide-cdp

Depends on: [Runtime](Runtime.md), [Storage](Storage.md)

Methods are called as `IndexedDB.<command>` and events arrive as `IndexedDB.<event>`.

## Commands

### IndexedDB.clearObjectStore

Clears all entries from an object store.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `securityOrigin` (optional) | string | At least and at most one of securityOrigin, storageKey, or storageBucket must be specified. Security origin. |
| `storageKey` (optional) | string | Storage key. |
| `storageBucket` (optional) | [Storage.StorageBucket](Storage.md#type-storagebucket) | Storage bucket. If not specified, it uses the default bucket. |
| `databaseName` | string | Database name. |
| `objectStoreName` | string | Object store name. |

### IndexedDB.deleteDatabase

Deletes a database.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `securityOrigin` (optional) | string | At least and at most one of securityOrigin, storageKey, or storageBucket must be specified. Security origin. |
| `storageKey` (optional) | string | Storage key. |
| `storageBucket` (optional) | [Storage.StorageBucket](Storage.md#type-storagebucket) | Storage bucket. If not specified, it uses the default bucket. |
| `databaseName` | string | Database name. |

### IndexedDB.deleteObjectStoreEntries

Delete a range of entries from an object store

**Parameters**

| Name | Type | Description |
|---|---|---|
| `securityOrigin` (optional) | string | At least and at most one of securityOrigin, storageKey, or storageBucket must be specified. Security origin. |
| `storageKey` (optional) | string | Storage key. |
| `storageBucket` (optional) | [Storage.StorageBucket](Storage.md#type-storagebucket) | Storage bucket. If not specified, it uses the default bucket. |
| `databaseName` | string |  |
| `objectStoreName` | string |  |
| `keyRange` | [KeyRange](#type-keyrange) | Range of entry keys to delete |

### IndexedDB.disable

Disables events from backend.

### IndexedDB.enable

Enables events from backend.

### IndexedDB.requestData

Requests data from object store or index.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `securityOrigin` (optional) | string | At least and at most one of securityOrigin, storageKey, or storageBucket must be specified. Security origin. |
| `storageKey` (optional) | string | Storage key. |
| `storageBucket` (optional) | [Storage.StorageBucket](Storage.md#type-storagebucket) | Storage bucket. If not specified, it uses the default bucket. |
| `databaseName` | string | Database name. |
| `objectStoreName` | string | Object store name. |
| `indexName` (optional) | string | Index name. If not specified, it performs an object store data request. |
| `skipCount` | integer | Number of records to skip. |
| `pageSize` | integer | Number of records to fetch. |
| `keyRange` (optional) | [KeyRange](#type-keyrange) | Key range. |

**Returns**

| Name | Type | Description |
|---|---|---|
| `objectStoreDataEntries` | array of [DataEntry](#type-dataentry) | Array of object store data entries. |
| `hasMore` | boolean | If true, there are more entries to fetch in the given range. |

### IndexedDB.getMetadata

Gets metadata of an object store.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `securityOrigin` (optional) | string | At least and at most one of securityOrigin, storageKey, or storageBucket must be specified. Security origin. |
| `storageKey` (optional) | string | Storage key. |
| `storageBucket` (optional) | [Storage.StorageBucket](Storage.md#type-storagebucket) | Storage bucket. If not specified, it uses the default bucket. |
| `databaseName` | string | Database name. |
| `objectStoreName` | string | Object store name. |

**Returns**

| Name | Type | Description |
|---|---|---|
| `entriesCount` | number | the entries count |
| `keyGeneratorValue` | number | the current value of key generator, to become the next inserted key into the object store. Valid if objectStore.autoIncrement is true. |

### IndexedDB.requestDatabase

Requests database with given name in given frame.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `securityOrigin` (optional) | string | At least and at most one of securityOrigin, storageKey, or storageBucket must be specified. Security origin. |
| `storageKey` (optional) | string | Storage key. |
| `storageBucket` (optional) | [Storage.StorageBucket](Storage.md#type-storagebucket) | Storage bucket. If not specified, it uses the default bucket. |
| `databaseName` | string | Database name. |

**Returns**

| Name | Type | Description |
|---|---|---|
| `databaseWithObjectStores` | [DatabaseWithObjectStores](#type-databasewithobjectstores) | Database with an array of object stores. |

### IndexedDB.requestDatabaseNames

Requests database names for given security origin.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `securityOrigin` (optional) | string | At least and at most one of securityOrigin, storageKey, or storageBucket must be specified. Security origin. |
| `storageKey` (optional) | string | Storage key. |
| `storageBucket` (optional) | [Storage.StorageBucket](Storage.md#type-storagebucket) | Storage bucket. If not specified, it uses the default bucket. |

**Returns**

| Name | Type | Description |
|---|---|---|
| `databaseNames` | array of string | Database names for origin. |

## Types

<a id="type-databasewithobjectstores"></a>
### IndexedDB.DatabaseWithObjectStores

Type: object

Database with an array of object stores.

**Properties**

| Name | Type | Description |
|---|---|---|
| `name` | string | Database name. |
| `version` | number | Database version (type is not 'integer', as the standard requires the version number to be 'unsigned long long') |
| `objectStores` | array of [ObjectStore](#type-objectstore) | Object stores in this database. |

<a id="type-objectstore"></a>
### IndexedDB.ObjectStore

Type: object

Object store.

**Properties**

| Name | Type | Description |
|---|---|---|
| `name` | string | Object store name. |
| `keyPath` | [KeyPath](#type-keypath) | Object store key path. |
| `autoIncrement` | boolean | If true, object store has auto increment flag set. |
| `indexes` | array of [ObjectStoreIndex](#type-objectstoreindex) | Indexes in this object store. |

<a id="type-objectstoreindex"></a>
### IndexedDB.ObjectStoreIndex

Type: object

Object store index.

**Properties**

| Name | Type | Description |
|---|---|---|
| `name` | string | Index name. |
| `keyPath` | [KeyPath](#type-keypath) | Index key path. |
| `unique` | boolean | If true, index is unique. |
| `multiEntry` | boolean | If true, index allows multiple entries for a key. |

<a id="type-key"></a>
### IndexedDB.Key

Type: object

Key.

**Properties**

| Name | Type | Description |
|---|---|---|
| `type` | enum: `number`, `string`, `date`, `array` | Key type. |
| `number` (optional) | number | Number value. |
| `string` (optional) | string | String value. |
| `date` (optional) | number | Date value. |
| `array` (optional) | array of [Key](#type-key) | Array value. |

<a id="type-keyrange"></a>
### IndexedDB.KeyRange

Type: object

Key range.

**Properties**

| Name | Type | Description |
|---|---|---|
| `lower` (optional) | [Key](#type-key) | Lower bound. |
| `upper` (optional) | [Key](#type-key) | Upper bound. |
| `lowerOpen` | boolean | If true lower bound is open. |
| `upperOpen` | boolean | If true upper bound is open. |

<a id="type-dataentry"></a>
### IndexedDB.DataEntry

Type: object

Data entry.

**Properties**

| Name | Type | Description |
|---|---|---|
| `key` | [Runtime.RemoteObject](Runtime.md#type-remoteobject) | Key object. |
| `primaryKey` | [Runtime.RemoteObject](Runtime.md#type-remoteobject) | Primary key object. |
| `value` | [Runtime.RemoteObject](Runtime.md#type-remoteobject) | Value object. |

<a id="type-keypath"></a>
### IndexedDB.KeyPath

Type: object

Key path.

**Properties**

| Name | Type | Description |
|---|---|---|
| `type` | enum: `null`, `string`, `array` | Key path type. |
| `string` (optional) | string | String value. |
| `array` (optional) | array of string | Array value. |

