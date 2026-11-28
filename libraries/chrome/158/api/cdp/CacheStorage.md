# CacheStorage domain *(experimental)*

Copyright 2017 The Chromium Authors Use of this source code is governed by a BSD-style license that can be found in the LICENSE file.  Contributing to Chrome DevTools Protocol: https://goo.gle/devtools-contribution-guide-cdp

Depends on: [Storage](Storage.md)

Methods are called as `CacheStorage.<command>` and events arrive as `CacheStorage.<event>`.

## Commands

### CacheStorage.deleteCache

Deletes a cache.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `cacheId` | [CacheId](#type-cacheid) | Id of cache for deletion. |

### CacheStorage.deleteEntry

Deletes a cache entry.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `cacheId` | [CacheId](#type-cacheid) | Id of cache where the entry will be deleted. |
| `request` | string | URL spec of the request. |

### CacheStorage.requestCacheNames

Requests cache names.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `securityOrigin` (optional) | string | At least and at most one of securityOrigin, storageKey, storageBucket must be specified. Security origin. |
| `storageKey` (optional) | string | Storage key. |
| `storageBucket` (optional) | [Storage.StorageBucket](Storage.md#type-storagebucket) | Storage bucket. If not specified, it uses the default bucket. |

**Returns**

| Name | Type | Description |
|---|---|---|
| `caches` | array of [Cache](#type-cache) | Caches for the security origin. |

### CacheStorage.requestCachedResponse

Fetches cache entry.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `cacheId` | [CacheId](#type-cacheid) | Id of cache that contains the entry. |
| `requestURL` | string | URL spec of the request. |
| `requestHeaders` | array of [Header](#type-header) | headers of the request. |

**Returns**

| Name | Type | Description |
|---|---|---|
| `response` | [CachedResponse](#type-cachedresponse) | Response read from the cache. |

### CacheStorage.requestEntries

Requests data from cache.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `cacheId` | [CacheId](#type-cacheid) | ID of cache to get entries from. |
| `skipCount` (optional) | integer | Number of records to skip. |
| `pageSize` (optional) | integer | Number of records to fetch. |
| `pathFilter` (optional) | string | If present, only return the entries containing this substring in the path |

**Returns**

| Name | Type | Description |
|---|---|---|
| `cacheDataEntries` | array of [DataEntry](#type-dataentry) | Array of object store data entries. |
| `returnCount` | number | Count of returned entries from this storage. If pathFilter is empty, it is the count of all entries from this storage. |

## Types

<a id="type-cacheid"></a>
### CacheStorage.CacheId

Type: string

Unique identifier of the Cache object.

<a id="type-cachedresponsetype"></a>
### CacheStorage.CachedResponseType

Type: string

type of HTTP response cached

Allowed values: `basic`, `cors`, `default`, `error`, `opaqueResponse`, `opaqueRedirect`

<a id="type-dataentry"></a>
### CacheStorage.DataEntry

Type: object

Data entry.

**Properties**

| Name | Type | Description |
|---|---|---|
| `requestURL` | string | Request URL. |
| `requestMethod` | string | Request method. |
| `requestHeaders` | array of [Header](#type-header) | Request headers |
| `responseTime` | number | Number of seconds since epoch. |
| `responseStatus` | integer | HTTP response status code. |
| `responseStatusText` | string | HTTP response status text. |
| `responseType` | [CachedResponseType](#type-cachedresponsetype) | HTTP response type |
| `responseHeaders` | array of [Header](#type-header) | Response headers |

<a id="type-cache"></a>
### CacheStorage.Cache

Type: object

Cache identifier.

**Properties**

| Name | Type | Description |
|---|---|---|
| `cacheId` | [CacheId](#type-cacheid) | An opaque unique id of the cache. |
| `securityOrigin` | string | Security origin of the cache. |
| `storageKey` | string | Storage key of the cache. |
| `storageBucket` (optional) | [Storage.StorageBucket](Storage.md#type-storagebucket) | Storage bucket of the cache. |
| `cacheName` | string | The name of the cache. |

<a id="type-header"></a>
### CacheStorage.Header

Type: object

**Properties**

| Name | Type | Description |
|---|---|---|
| `name` | string |  |
| `value` | string |  |

<a id="type-cachedresponse"></a>
### CacheStorage.CachedResponse

Type: object

Cached response

**Properties**

| Name | Type | Description |
|---|---|---|
| `body` | binary | Entry content, base64-encoded. |

