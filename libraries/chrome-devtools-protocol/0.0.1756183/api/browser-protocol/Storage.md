# Storage domain

Chrome DevTools Protocol, browser protocol (tip-of-tree) (protocol 1.3).

**Experimental**

Depends on: [Browser](Browser.md), [Network](Network.md)

27 methods, 7 events, 9 types.

## Methods

### Storage.getStorageKeyForFrame

**Deprecated**

Returns a storage key given a frame id.
Deprecated. Please use Storage.getStorageKey instead.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `frameId` | [Page.FrameId](Page.md#type-frameid) |  |

**Return object**

| Name | Type | Description |
|---|---|---|
| `storageKey` | [Storage.SerializedStorageKey](#type-serializedstoragekey) |  |

### Storage.getStorageKey

**Experimental**

Returns storage key for the given frame. If no frame ID is provided,
the storage key of the target executing this command is returned.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `frameId` (optional) | [Page.FrameId](Page.md#type-frameid) |  |

**Return object**

| Name | Type | Description |
|---|---|---|
| `storageKey` | [Storage.SerializedStorageKey](#type-serializedstoragekey) |  |

### Storage.clearDataForOrigin

Clears storage for origin.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `origin` | string | Security origin. |
| `storageTypes` | string | Comma separated list of StorageType to clear. |

### Storage.clearDataForStorageKey

Clears storage for storage key.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `storageKey` | string | Storage key. |
| `storageTypes` | string | Comma separated list of StorageType to clear. |

### Storage.getCookies

Returns all browser cookies.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `browserContextId` (optional) | [Browser.BrowserContextID](Browser.md#type-browsercontextid) | Browser context to use when called on the browser endpoint. |

**Return object**

| Name | Type | Description |
|---|---|---|
| `cookies` | array of [Network.Cookie](Network.md#type-cookie) | Array of cookie objects. |

### Storage.setCookies

Sets given cookies.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `cookies` | array of [Network.CookieParam](Network.md#type-cookieparam) | Cookies to be set. |
| `browserContextId` (optional) | [Browser.BrowserContextID](Browser.md#type-browsercontextid) | Browser context to use when called on the browser endpoint. |

### Storage.clearCookies

Clears cookies.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `browserContextId` (optional) | [Browser.BrowserContextID](Browser.md#type-browsercontextid) | Browser context to use when called on the browser endpoint. |

### Storage.getUsageAndQuota

Returns usage and quota in bytes.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `origin` | string | Security origin. |

**Return object**

| Name | Type | Description |
|---|---|---|
| `usage` | number | Storage usage (bytes). |
| `quota` | number | Storage quota (bytes). |
| `overrideActive` | boolean | Whether or not the origin has an active storage quota override |
| `usageBreakdown` | array of [Storage.UsageForType](#type-usagefortype) | Storage usage per type (bytes). |

### Storage.overrideQuotaForOrigin

**Experimental**

Override quota for the specified origin

**Parameters**

| Name | Type | Description |
|---|---|---|
| `origin` | string | Security origin. |
| `quotaSize` (optional) | number | The quota size (in bytes) to override the original quota with. If this is called multiple times, the overridden quota will be equal to the quotaSize provided in the final call. If this is called without specifying a quotaSize, the quota will be reset to the default value for the specified origin. If this is called multiple times with different origins, the override will be maintained for each origin until it is disabled (called without a quotaSize). |

### Storage.trackCacheStorageForOrigin

Registers origin to be notified when an update occurs to its cache storage list.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `origin` | string | Security origin. |

### Storage.trackCacheStorageForStorageKey

Registers storage key to be notified when an update occurs to its cache storage list.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `storageKey` | string | Storage key. |

### Storage.trackIndexedDBForOrigin

Registers origin to be notified when an update occurs to its IndexedDB.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `origin` | string | Security origin. |

### Storage.trackIndexedDBForStorageKey

Registers storage key to be notified when an update occurs to its IndexedDB.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `storageKey` | string | Storage key. |

### Storage.untrackCacheStorageForOrigin

Unregisters origin from receiving notifications for cache storage.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `origin` | string | Security origin. |

### Storage.untrackCacheStorageForStorageKey

Unregisters storage key from receiving notifications for cache storage.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `storageKey` | string | Storage key. |

### Storage.untrackIndexedDBForOrigin

Unregisters origin from receiving notifications for IndexedDB.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `origin` | string | Security origin. |

### Storage.untrackIndexedDBForStorageKey

Unregisters storage key from receiving notifications for IndexedDB.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `storageKey` | string | Storage key. |

### Storage.getTrustTokens

**Experimental**

Returns the number of stored Trust Tokens per issuer for the
current browsing context.

No parameters.

**Return object**

| Name | Type | Description |
|---|---|---|
| `tokens` | array of [Storage.TrustTokens](#type-trusttokens) |  |

### Storage.clearTrustTokens

**Experimental**

Removes all Trust Tokens issued by the provided issuerOrigin.
Leaves other stored data, including the issuer's Redemption Records, intact.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `issuerOrigin` | string |  |

**Return object**

| Name | Type | Description |
|---|---|---|
| `didDeleteTokens` | boolean | True if any tokens were deleted, false otherwise. |

### Storage.getPrivateVerificationTokens

**Experimental**

Returns all stored Private Verification Tokens for the current browsing
context.

No parameters.

**Return object**

| Name | Type | Description |
|---|---|---|
| `tokens` | array of [Storage.PrivateVerificationToken](#type-privateverificationtoken) |  |

### Storage.getPrivateVerificationTokensIssuerConfigs

**Experimental**

Returns the configured Private Verification Tokens issuers and their redeemer
origins.

No parameters.

**Return object**

| Name | Type | Description |
|---|---|---|
| `configs` | array of [Storage.PrivateVerificationTokensIssuerConfig](#type-privateverificationtokensissuerconfig) |  |

### Storage.clearPrivateVerificationTokens

**Experimental**

Removes all Private Verification Tokens issued by the provided issuerOrigin.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `issuerOrigin` | string |  |

### Storage.deletePrivateVerificationToken

**Experimental**

Removes a specific Private Verification Token by its ID.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `tokenId` | string |  |

### Storage.setPrivateVerificationTokensTracking

**Experimental**

Set tracking for Private Verification Tokens.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `enable` | boolean |  |

### Storage.setStorageBucketTracking

**Experimental**

Set tracking for a storage key's buckets.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `storageKey` | string |  |
| `enable` | boolean |  |

### Storage.deleteStorageBucket

**Experimental**

Deletes the Storage Bucket with the given storage key and bucket name.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `bucket` | [Storage.StorageBucket](#type-storagebucket) |  |

### Storage.runBounceTrackingMitigations

**Experimental**

Deletes state for sites identified as potential bounce trackers, immediately.

No parameters.

**Return object**

| Name | Type | Description |
|---|---|---|
| `deletedSites` | array of string |  |

## Events

### Storage.cacheStorageContentUpdated

A cache's contents have been modified.

**Event parameters**

| Name | Type | Description |
|---|---|---|
| `origin` | string | Origin to update. |
| `storageKey` | string | Storage key to update. |
| `bucketId` | string | Storage bucket to update. |
| `cacheName` | string | Name of cache in origin. |

### Storage.cacheStorageListUpdated

A cache has been added/deleted.

**Event parameters**

| Name | Type | Description |
|---|---|---|
| `origin` | string | Origin to update. |
| `storageKey` | string | Storage key to update. |
| `bucketId` | string | Storage bucket to update. |

### Storage.indexedDBContentUpdated

The origin's IndexedDB object store has been modified.

**Event parameters**

| Name | Type | Description |
|---|---|---|
| `origin` | string | Origin to update. |
| `storageKey` | string | Storage key to update. |
| `bucketId` | string | Storage bucket to update. |
| `databaseName` | string | Database to update. |
| `objectStoreName` | string | ObjectStore to update. |

### Storage.indexedDBListUpdated

The origin's IndexedDB database list has been modified.

**Event parameters**

| Name | Type | Description |
|---|---|---|
| `origin` | string | Origin to update. |
| `storageKey` | string | Storage key to update. |
| `bucketId` | string | Storage bucket to update. |

### Storage.storageBucketCreatedOrUpdated

**Event parameters**

| Name | Type | Description |
|---|---|---|
| `bucketInfo` | [Storage.StorageBucketInfo](#type-storagebucketinfo) |  |

### Storage.storageBucketDeleted

**Event parameters**

| Name | Type | Description |
|---|---|---|
| `bucketId` | string |  |

### Storage.privateVerificationTokensUpdated

**Experimental**

Private Verification Tokens have been stored or deleted.

## Types

<a id="type-serializedstoragekey"></a>
### Storage.SerializedStorageKey

Type: string

<a id="type-storagetype"></a>
### Storage.StorageType

Enum of possible storage types.

Type: string

Allowed values: `cookies`, `file_systems`, `indexeddb`, `local_storage`, `shader_cache`, `websql`, `service_workers`, `cache_storage`, `storage_buckets`, `all`, `other`

<a id="type-usagefortype"></a>
### Storage.UsageForType

Usage for a storage type.

Type: object

**Properties**

| Name | Type | Description |
|---|---|---|
| `storageType` | [Storage.StorageType](#type-storagetype) | Name of storage type. |
| `usage` | number | Storage usage (bytes). |

<a id="type-trusttokens"></a>
### Storage.TrustTokens

**Experimental**

Pair of issuer origin and number of available (signed, but not used) Trust
Tokens from that issuer.

Type: object

**Properties**

| Name | Type | Description |
|---|---|---|
| `issuerOrigin` | string |  |
| `count` | number |  |

<a id="type-privateverificationtoken"></a>
### Storage.PrivateVerificationToken

**Experimental**

Details of a stored Private Verification Token.

Type: object

**Properties**

| Name | Type | Description |
|---|---|---|
| `id` | string | Unique identifier of the token in the database. |
| `issuerOrigin` | string | Origin of the token issuer. |
| `keyId` | integer | Public key ID used to issue the token. |
| `expiration` | [Network.TimeSinceEpoch](Network.md#type-timesinceepoch) | Expiration timestamp in seconds since the epoch. |
| `creationTime` | [Network.TimeSinceEpoch](Network.md#type-timesinceepoch) | Token creation timestamp in seconds since the epoch. |
| `version` | integer | Token protocol version. |
| `token` | string | Base64-encoded serialized token. |

<a id="type-privateverificationtokensissuerconfig"></a>
### Storage.PrivateVerificationTokensIssuerConfig

**Experimental**

Configuration for a Private Verification Tokens issuer.

Type: object

**Properties**

| Name | Type | Description |
|---|---|---|
| `issuerOrigin` | string | Origin of the token issuer. |
| `redeemerOrigins` | array of string | Origins authorized to redeem tokens from this issuer. |

<a id="type-storagebucketsdurability"></a>
### Storage.StorageBucketsDurability

Type: string

Allowed values: `relaxed`, `strict`

<a id="type-storagebucket"></a>
### Storage.StorageBucket

Type: object

**Properties**

| Name | Type | Description |
|---|---|---|
| `storageKey` | [Storage.SerializedStorageKey](#type-serializedstoragekey) |  |
| `name` (optional) | string | If not specified, it is the default bucket of the storageKey. |

<a id="type-storagebucketinfo"></a>
### Storage.StorageBucketInfo

Type: object

**Properties**

| Name | Type | Description |
|---|---|---|
| `bucket` | [Storage.StorageBucket](#type-storagebucket) |  |
| `id` | string |  |
| `expiration` | [Network.TimeSinceEpoch](Network.md#type-timesinceepoch) |  |
| `quota` | number | Storage quota (bytes). |
| `persistent` | boolean |  |
| `durability` | [Storage.StorageBucketsDurability](#type-storagebucketsdurability) |  |
