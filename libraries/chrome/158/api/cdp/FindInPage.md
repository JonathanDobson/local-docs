# FindInPage domain *(experimental)*

Copyright 2026 The Chromium Authors Use of this source code is governed by a BSD-style license that can be found in the LICENSE file. This domain provides commands to trigger the "Find in page" feature.

Methods are called as `FindInPage.<command>` and events arrive as `FindInPage.<event>`.

## Commands

### FindInPage.findFirst

Forwards `query` to the find-in-page facility, starting a new find session. Where exactly the search starts from is implementation-specific.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `query` | string |  |

### FindInPage.findNext

Moves to the next match for the query passed to the most recent findFirst() call.

### FindInPage.findPrev

Moves to the previous match for the query passed to the most recent findFirst() call.

### FindInPage.stop

Ends the current find session, if any, and clears its highlighting.

