---
source: https://www.postgresql.org/docs/18/view-pg-wait-events.html
title: "53.38. pg_wait_events"
---


## 53.38. `pg_wait_events`

The view `pg_wait_events` provides description about the wait events.

**Table 53.38. `pg_wait_events` Columns**

| Column Type  Description |
| --- |
| `type` `text`  Wait event type |
| `name` `text`  Wait event name |
| `description` `text`  Wait event description |
