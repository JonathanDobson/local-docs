# FileSystem domain

Chrome DevTools Protocol, browser protocol (tip-of-tree) (protocol 1.3).

**Experimental**

Depends on: [Network](Network.md), [Storage](Storage.md)

1 methods, 0 events, 3 types.

## Methods

### FileSystem.getDirectory

**Parameters**

| Name | Type | Description |
|---|---|---|
| `bucketFileSystemLocator` | [FileSystem.BucketFileSystemLocator](#type-bucketfilesystemlocator) |  |

**Return object**

| Name | Type | Description |
|---|---|---|
| `directory` | [FileSystem.Directory](#type-directory) | Returns the directory object at the path. |

## Types

<a id="type-file"></a>
### FileSystem.File

Type: object

**Properties**

| Name | Type | Description |
|---|---|---|
| `name` | string |  |
| `lastModified` | [Network.TimeSinceEpoch](Network.md#type-timesinceepoch) | Timestamp |
| `size` | number | Size in bytes |
| `type` | string |  |

<a id="type-directory"></a>
### FileSystem.Directory

Type: object

**Properties**

| Name | Type | Description |
|---|---|---|
| `name` | string |  |
| `nestedDirectories` | array of string |  |
| `nestedFiles` | array of [FileSystem.File](#type-file) | Files that are directly nested under this directory. |

<a id="type-bucketfilesystemlocator"></a>
### FileSystem.BucketFileSystemLocator

Type: object

**Properties**

| Name | Type | Description |
|---|---|---|
| `storageKey` | [Storage.SerializedStorageKey](Storage.md#type-serializedstoragekey) | Storage key |
| `bucketName` (optional) | string | Bucket name. Not passing a `bucketName` will retrieve the default Bucket. (https://developer.mozilla.org/en-US/docs/Web/API/Storage_API#storage_buckets) |
| `pathComponents` | array of string | Path to the directory using each path component as an array item. |
