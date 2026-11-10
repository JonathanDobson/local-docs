---
source: https://www.postgresql.org/docs/18/catalog-pg-ts-config-map.html
title: "52.60. pg_ts_config_map"
---


## 52.60. `pg_ts_config_map`

The `pg_ts_config_map` catalog contains entries showing which text search dictionaries should be consulted, and in what order, for each output token type of each text search configuration's parser.

PostgreSQL's text search features are described at length in [Chapter 12](textsearch.html "Chapter 12. Full Text Search").

**Table 52.60. `pg_ts_config_map` Columns**

| Column Type  Description |
| --- |
| `mapcfg` `oid` (references [`pg_ts_config`](catalog-pg-ts-config.html "52.59. pg_ts_config").`oid`)  The OID of the [`pg_ts_config`](catalog-pg-ts-config.html "52.59. pg_ts_config") entry owning this map entry |
| `maptokentype` `int4`  A token type emitted by the configuration's parser |
| `mapseqno` `int4`  Order in which to consult this entry (lower `mapseqno`s first) |
| `mapdict` `oid` (references [`pg_ts_dict`](catalog-pg-ts-dict.html "52.61. pg_ts_dict").`oid`)  The OID of the text search dictionary to consult |
