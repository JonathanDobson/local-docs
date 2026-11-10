---
source: https://www.postgresql.org/docs/18/view-pg-replication-origin-status.html
title: "53.19. pg_replication_origin_status"
---


## 53.19. `pg_replication_origin_status`

The `pg_replication_origin_status` view contains information about how far replay for a certain origin has progressed. For more on replication origins see [Chapter 48](replication-origins.html "Chapter 48. Replication Progress Tracking").

**Table 53.19. `pg_replication_origin_status` Columns**

| Column Type  Description |
| --- |
| `local_id` `oid` (references [`pg_replication_origin`](catalog-pg-replication-origin.html "52.44. pg_replication_origin").`roident`)  internal node identifier |
| `external_id` `text` (references [`pg_replication_origin`](catalog-pg-replication-origin.html "52.44. pg_replication_origin").`roname`)  external node identifier |
| `remote_lsn` `pg_lsn`  The origin node's LSN up to which data has been replicated. |
| `local_lsn` `pg_lsn`  This node's LSN at which `remote_lsn` has been replicated. Used to flush commit records before persisting data to disk when using asynchronous commits. |
