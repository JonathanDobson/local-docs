---
source: https://www.postgresql.org/docs/18/catalog-pg-replication-origin.html
title: "52.44. pg_replication_origin"
---


## 52.44. `pg_replication_origin`

The `pg_replication_origin` catalog contains all replication origins created. For more on replication origins see [Chapter 48](replication-origins.html "Chapter 48. Replication Progress Tracking").

Unlike most system catalogs, `pg_replication_origin` is shared across all databases of a cluster: there is only one copy of `pg_replication_origin` per cluster, not one per database.

**Table 52.44. `pg_replication_origin` Columns**

| Column Type  Description |
| --- |
| `roident` `oid`  A unique, cluster-wide identifier for the replication origin. Should never leave the system. |
| `roname` `text`  The external, user defined, name of a replication origin. |
