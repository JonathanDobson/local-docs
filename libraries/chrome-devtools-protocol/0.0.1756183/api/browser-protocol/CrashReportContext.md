# CrashReportContext domain

Chrome DevTools Protocol, browser protocol (tip-of-tree) (protocol 1.3).

**Experimental**

This domain exposes the current state of the CrashReportContext API.

Depends on: [Page](Page.md)

1 methods, 0 events, 1 types.

## Methods

### CrashReportContext.getEntries

Returns all entries in the CrashReportContext across all frames in the page.

No parameters.

**Return object**

| Name | Type | Description |
|---|---|---|
| `entries` | array of [CrashReportContext.CrashReportContextEntry](#type-crashreportcontextentry) |  |

## Types

<a id="type-crashreportcontextentry"></a>
### CrashReportContext.CrashReportContextEntry

Key-value pair in CrashReportContext.

Type: object

**Properties**

| Name | Type | Description |
|---|---|---|
| `key` | string |  |
| `value` | string |  |
| `frameId` | [Page.FrameId](Page.md#type-frameid) | The ID of the frame where the key-value pair was set. |
