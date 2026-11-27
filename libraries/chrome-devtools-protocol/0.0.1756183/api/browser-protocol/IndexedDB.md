# IndexedDB domain

Chrome DevTools Protocol, browser protocol (tip-of-tree) (protocol 1.3).

**Experimental**

Depends on: [Runtime](Runtime.md), [Storage](Storage.md)

9 methods, 0 events, 7 types.

## Methods

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
| `keyRange` | [IndexedDB.KeyRange](#type-keyrange) | Range of entry keys to delete |

### IndexedDB.disable

Disables events from backend.

No parameters.

### IndexedDB.enable

Enables events from backend.

No parameters.

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
| `keyRange` (optional) | [IndexedDB.KeyRange](#type-keyrange) | Key range. |

**Return object**

| Name | Type | Description |
|---|---|---|
| `objectStoreDataEntries` | array of [IndexedDB.DataEntry](#type-dataentry) | Array of object store data entries. |
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

**Return object**

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

**Return object**

| Name | Type | Description |
|---|---|---|
| `databaseWithObjectStores` | [IndexedDB.DatabaseWithObjectStores](#type-databasewithobjectstores) | Database with an array of object stores. |

### IndexedDB.requestDatabaseNames

Requests database names for given security origin.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `securityOrigin` (optional) | string | At least and at most one of securityOrigin, storageKey, or storageBucket must be specified. Security origin. |
| `storageKey` (optional) | string | Storage key. |
| `storageBucket` (optional) | [Storage.StorageBucket](Storage.md#type-storagebucket) | Storage bucket. If not specified, it uses the default bucket. |

**Return object**

| Name | Type | Description |
|---|---|---|
| `databaseNames` | array of string | Database names for origin. |

## Types

<a id="type-databasewithobjectstores"></a>
### IndexedDB.DatabaseWithObjectStores

Database with an array of object stores.

Type: object

**Properties**

| Name | Type | Description |
|---|---|---|
| `name` | string | Database name. |
| `version` | number | Database version (type is not 'integer', as the standard requires the version number to be 'unsigned long long') |
| `objectStores` | array of [IndexedDB.ObjectStore](#type-objectstore) | Object stores in this database. |

<a id="type-objectstore"></a>
### IndexedDB.ObjectStore

Object store.

Type: object

**Properties**

| Name | Type | Description |
|---|---|---|
| `name` | string | Object store name. |
| `keyPath` | [IndexedDB.KeyPath](#type-keypath) | Object store key path. |
| `autoIncrement` | boolean | If true, object store has auto increment flag set. |
| `indexes` | array of [IndexedDB.ObjectStoreIndex](#type-objectstoreindex) | Indexes in this object store. |

<a id="type-objectstoreindex"></a>
### IndexedDB.ObjectStoreIndex

Object store index.

Type: object

**Properties**

| Name | Type | Description |
|---|---|---|
| `name` | string | Index name. |
| `keyPath` | [IndexedDB.KeyPath](#type-keypath) | Index key path. |
| `unique` | boolean | If true, index is unique. |
| `multiEntry` | boolean | If true, index allows multiple entries for a key. |

<a id="type-key"></a>
### IndexedDB.Key

Key.

Type: object

**Properties**

| Name | Type | Description |
|---|---|---|
| `type` | string | Key type. Allowed values: `number`, `string`, `date`, `array` |
| `number` (optional) | number | Number value. |
| `string` (optional) | string | String value. |
| `date` (optional) | number | Date value. |
| `array` (optional) | array of [IndexedDB.Key](#type-key) | Array value. |

<a id="type-keyrange"></a>
### IndexedDB.KeyRange

Key range.

Type: object

**Properties**

| Name | Type | Description |
|---|---|---|
| `lower` (optional) | [IndexedDB.Key](#type-key) | Lower bound. |
| `upper` (optional) | [IndexedDB.Key](#type-key) | Upper bound. |
| `lowerOpen` | boolean | If true lower bound is open. |
| `upperOpen` | boolean | If true upper bound is open. |

<a id="type-dataentry"></a>
### IndexedDB.DataEntry

Data entry.

Type: object

**Properties**

| Name | Type | Description |
|---|---|---|
| `key` | [Runtime.RemoteObject](Runtime.md#type-remoteobject) | Key object. |
| `primaryKey` | [Runtime.RemoteObject](Runtime.md#type-remoteobject) | Primary key object. |
| `value` | [Runtime.RemoteObject](Runtime.md#type-remoteobject) | Value object. |

<a id="type-keypath"></a>
### IndexedDB.KeyPath

Key path.

Type: object

**Properties**

| Name | Type | Description |
|---|---|---|
| `type` | string | Key path type. Allowed values: `null`, `string`, `array` |
| `string` (optional) | string | String value. |
| `array` (optional) | array of string | Array value. |
