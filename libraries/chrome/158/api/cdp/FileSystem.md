# FileSystem domain *(experimental)*

Copyright 2017 The Chromium Authors Use of this source code is governed by a BSD-style license that can be found in the LICENSE file.  Contributing to Chrome DevTools Protocol: https://goo.gle/devtools-contribution-guide-cdp

Depends on: [Network](Network.md), [Storage](Storage.md)

Methods are called as `FileSystem.<command>` and events arrive as `FileSystem.<event>`.

## Commands

### FileSystem.getDirectory

**Parameters**

| Name | Type | Description |
|---|---|---|
| `bucketFileSystemLocator` | [BucketFileSystemLocator](#type-bucketfilesystemlocator) |  |

**Returns**

| Name | Type | Description |
|---|---|---|
| `directory` | [Directory](#type-directory) | Returns the directory object at the path. |

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
| `nestedFiles` | array of [File](#type-file) | Files that are directly nested under this directory. |

<a id="type-bucketfilesystemlocator"></a>
### FileSystem.BucketFileSystemLocator

Type: object

**Properties**

| Name | Type | Description |
|---|---|---|
| `storageKey` | [Storage.SerializedStorageKey](Storage.md#type-serializedstoragekey) | Storage key |
| `bucketName` (optional) | string | Bucket name. Not passing a `bucketName` will retrieve the default Bucket. (https://developer.mozilla.org/en-US/docs/Web/API/Storage_API#storage_buckets) |
| `pathComponents` | array of string | Path to the directory using each path component as an array item. |

