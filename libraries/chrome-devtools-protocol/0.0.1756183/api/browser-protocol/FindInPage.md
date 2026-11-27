# FindInPage domain

Chrome DevTools Protocol, browser protocol (tip-of-tree) (protocol 1.3).

**Experimental**

This domain provides commands to trigger the "Find in page" feature.

4 methods, 0 events, 0 types.

## Methods

### FindInPage.findFirst

Forwards `query` to the find-in-page facility, starting a new find session.
Where exactly the search starts from is implementation-specific.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `query` | string |  |

### FindInPage.findNext

Moves to the next match for the query passed to the most recent
findFirst() call.

No parameters.

### FindInPage.findPrev

Moves to the previous match for the query passed to the most recent
findFirst() call.

No parameters.

### FindInPage.stop

Ends the current find session, if any, and clears its highlighting.

No parameters.
