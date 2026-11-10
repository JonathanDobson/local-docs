---
source: https://www.postgresql.org/docs/18/catalog-pg-event-trigger.html
title: "52.21. pg_event_trigger"
---


## 52.21. `pg_event_trigger`

The catalog `pg_event_trigger` stores event triggers. See [Chapter 38](event-triggers.html "Chapter 38. Event Triggers") for more information.

**Table 52.21. `pg_event_trigger` Columns**

| Column Type  Description |
| --- |
| `oid` `oid`  Row identifier |
| `evtname` `name`  Trigger name (must be unique) |
| `evtevent` `name`  Identifies the event for which this trigger fires |
| `evtowner` `oid` (references [`pg_authid`](catalog-pg-authid.html "52.8. pg_authid").`oid`)  Owner of the event trigger |
| `evtfoid` `oid` (references [`pg_proc`](catalog-pg-proc.html "52.39. pg_proc").`oid`)  The function to be called |
| `evtenabled` `char`  Controls in which [session\_replication\_role](runtime-config-client.html#GUC-SESSION-REPLICATION-ROLE) modes the event trigger fires. `O` = trigger fires in “origin” and “local” modes, `D` = trigger is disabled, `R` = trigger fires in “replica” mode, `A` = trigger fires always. |
| `evttags` `text[]`  Command tags for which this trigger will fire. If NULL, the firing of this trigger is not restricted on the basis of the command tag. |
