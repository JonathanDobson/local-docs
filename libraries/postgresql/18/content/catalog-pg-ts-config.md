---
source: https://www.postgresql.org/docs/18/catalog-pg-ts-config.html
title: "52.59. pg_ts_config"
---


## 52.59. `pg_ts_config`

The `pg_ts_config` catalog contains entries representing text search configurations. A configuration specifies a particular text search parser and a list of dictionaries to use for each of the parser's output token types. The parser is shown in the `pg_ts_config` entry, but the token-to-dictionary mapping is defined by subsidiary entries in [`pg_ts_config_map`](catalog-pg-ts-config-map.html "52.60. pg_ts_config_map").

PostgreSQL's text search features are described at length in [Chapter 12](textsearch.html "Chapter 12. Full Text Search").

**Table 52.59. `pg_ts_config` Columns**

| Column Type  Description |
| --- |
| `oid` `oid`  Row identifier |
| `cfgname` `name`  Text search configuration name |
| `cfgnamespace` `oid` (references [`pg_namespace`](catalog-pg-namespace.html "52.32. pg_namespace").`oid`)  The OID of the namespace that contains this configuration |
| `cfgowner` `oid` (references [`pg_authid`](catalog-pg-authid.html "52.8. pg_authid").`oid`)  Owner of the configuration |
| `cfgparser` `oid` (references [`pg_ts_parser`](catalog-pg-ts-parser.html "52.62. pg_ts_parser").`oid`)  The OID of the text search parser for this configuration |
