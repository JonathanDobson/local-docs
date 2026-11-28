# CacheStorage domain

Chrome DevTools Protocol, browser protocol (tip-of-tree) (protocol 1.3).

**Experimental**

Depends on: [Storage](Storage.md)

5 methods, 0 events, 6 types.

## Methods

### CacheStorage.deleteCache

Deletes a cache.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `cacheId` | [CacheStorage.CacheId](#type-cacheid) | Id of cache for deletion. |

### CacheStorage.deleteEntry

Deletes a cache entry.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `cacheId` | [CacheStorage.CacheId](#type-cacheid) | Id of cache where the entry will be deleted. |
| `request` | string | URL spec of the request. |

### CacheStorage.requestCacheNames

Requests cache names.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `securityOrigin` (optional) | string | At least and at most one of securityOrigin, storageKey, storageBucket must be specified. Security origin. |
| `storageKey` (optional) | string | Storage key. |
| `storageBucket` (optional) | [Storage.StorageBucket](Storage.md#type-storagebucket) | Storage bucket. If not specified, it uses the default bucket. |

**Return object**

| Name | Type | Description |
|---|---|---|
| `caches` | array of [CacheStorage.Cache](#type-cache) | Caches for the security origin. |

### CacheStorage.requestCachedResponse

Fetches cache entry.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `cacheId` | [CacheStorage.CacheId](#type-cacheid) | Id of cache that contains the entry. |
| `requestURL` | string | URL spec of the request. |
| `requestHeaders` | array of [CacheStorage.Header](#type-header) | headers of the request. |

**Return object**

| Name | Type | Description |
|---|---|---|
| `response` | [CacheStorage.CachedResponse](#type-cachedresponse) | Response read from the cache. |

### CacheStorage.requestEntries

Requests data from cache.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `cacheId` | [CacheStorage.CacheId](#type-cacheid) | ID of cache to get entries from. |
| `skipCount` (optional) | integer | Number of records to skip. |
| `pageSize` (optional) | integer | Number of records to fetch. |
| `pathFilter` (optional) | string | If present, only return the entries containing this substring in the path |

**Return object**

| Name | Type | Description |
|---|---|---|
| `cacheDataEntries` | array of [CacheStorage.DataEntry](#type-dataentry) | Array of object store data entries. |
| `returnCount` | number | Count of returned entries from this storage. If pathFilter is empty, it is the count of all entries from this storage. |

## Types

<a id="type-cacheid"></a>
### CacheStorage.CacheId

Unique identifier of the Cache object.

Type: string

<a id="type-cachedresponsetype"></a>
### CacheStorage.CachedResponseType

type of HTTP response cached

Type: string

Allowed values: `basic`, `cors`, `default`, `error`, `opaqueResponse`, `opaqueRedirect`

<a id="type-dataentry"></a>
### CacheStorage.DataEntry

Data entry.

Type: object

**Properties**

| Name | Type | Description |
|---|---|---|
| `requestURL` | string | Request URL. |
| `requestMethod` | string | Request method. |
| `requestHeaders` | array of [CacheStorage.Header](#type-header) | Request headers |
| `responseTime` | number | Number of seconds since epoch. |
| `responseStatus` | integer | HTTP response status code. |
| `responseStatusText` | string | HTTP response status text. |
| `responseType` | [CacheStorage.CachedResponseType](#type-cachedresponsetype) | HTTP response type |
| `responseHeaders` | array of [CacheStorage.Header](#type-header) | Response headers |

<a id="type-cache"></a>
### CacheStorage.Cache

Cache identifier.

Type: object

**Properties**

| Name | Type | Description |
|---|---|---|
| `cacheId` | [CacheStorage.CacheId](#type-cacheid) | An opaque unique id of the cache. |
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

Cached response

Type: object

**Properties**

| Name | Type | Description |
|---|---|---|
| `body` | string | Entry content, base64-encoded. (Encoded as a base64 string when passed over JSON) |
