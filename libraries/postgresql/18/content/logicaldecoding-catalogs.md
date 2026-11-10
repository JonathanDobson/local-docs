---
source: https://www.postgresql.org/docs/18/logicaldecoding-catalogs.html
title: "47.5. System Catalogs Related to Logical Decoding"
---


## 47.5. System Catalogs Related to Logical Decoding

The [`pg_replication_slots`](view-pg-replication-slots.html "53.20. pg_replication_slots") view and the [`pg_stat_replication`](monitoring-stats.html#MONITORING-PG-STAT-REPLICATION-VIEW "27.2.4. pg_stat_replication") view provide information about the current state of replication slots and streaming replication connections respectively. These views apply to both physical and logical replication. The [`pg_stat_replication_slots`](monitoring-stats.html#MONITORING-PG-STAT-REPLICATION-SLOTS-VIEW "27.2.5. pg_stat_replication_slots") view provides statistics information about the logical replication slots.
