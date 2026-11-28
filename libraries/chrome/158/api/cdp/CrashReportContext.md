# CrashReportContext domain *(experimental)*

Copyright 2026 The Chromium Authors Use of this source code is governed by a BSD-style license that can be found in the LICENSE file. This domain exposes the current state of the CrashReportContext API.

Depends on: [Page](Page.md)

Methods are called as `CrashReportContext.<command>` and events arrive as `CrashReportContext.<event>`.

## Commands

### CrashReportContext.getEntries

Returns all entries in the CrashReportContext across all frames in the page.

**Returns**

| Name | Type | Description |
|---|---|---|
| `entries` | array of [CrashReportContextEntry](#type-crashreportcontextentry) |  |

## Types

<a id="type-crashreportcontextentry"></a>
### CrashReportContext.CrashReportContextEntry

Type: object

Key-value pair in CrashReportContext.

**Properties**

| Name | Type | Description |
|---|---|---|
| `key` | string |  |
| `value` | string |  |
| `frameId` | [Page.FrameId](Page.md#type-frameid) | The ID of the frame where the key-value pair was set. |

