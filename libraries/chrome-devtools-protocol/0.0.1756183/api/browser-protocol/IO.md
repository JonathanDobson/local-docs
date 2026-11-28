# IO domain

Chrome DevTools Protocol, browser protocol (tip-of-tree) (protocol 1.3).

Input/Output operations for streams produced by DevTools.

3 methods, 0 events, 1 types.

## Methods

### IO.close

Close the stream, discard any temporary backing storage.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `handle` | [IO.StreamHandle](#type-streamhandle) | Handle of the stream to close. |

### IO.read

Read a chunk of the stream

**Parameters**

| Name | Type | Description |
|---|---|---|
| `handle` | [IO.StreamHandle](#type-streamhandle) | Handle of the stream to read. |
| `offset` (optional) | integer | Seek to the specified offset before reading (if not specified, proceed with offset following the last read). Some types of streams may only support sequential reads. |
| `size` (optional) | integer | Maximum number of bytes to read (left upon the agent discretion if not specified). |

**Return object**

| Name | Type | Description |
|---|---|---|
| `base64Encoded` (optional) | boolean | Set if the data is base64-encoded |
| `data` | string | Data that were read. |
| `eof` | boolean | Set if the end-of-file condition occurred while reading. |

### IO.resolveBlob

**Deprecated**

Return UUID of Blob object specified by a remote object id.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `objectId` | [Runtime.RemoteObjectId](Runtime.md#type-remoteobjectid) | Object id of a Blob object wrapper. |

**Return object**

| Name | Type | Description |
|---|---|---|
| `uuid` | string | UUID of the specified Blob. |

## Types

<a id="type-streamhandle"></a>
### IO.StreamHandle

This is either obtained from another method or specified as `blob:<uuid>` where
`<uuid>` is an UUID of a Blob.

Type: string
