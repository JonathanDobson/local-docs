---
source: https://www.postgresql.org/docs/18/catalog-pg-ts-parser.html
title: "52.62. pg_ts_parser"
---


## 52.62. `pg_ts_parser`

The `pg_ts_parser` catalog contains entries defining text search parsers. A parser is responsible for splitting input text into lexemes and assigning a token type to each lexeme. Since a parser must be implemented by C-language-level functions, creation of new parsers is restricted to database superusers.

PostgreSQL's text search features are described at length in [Chapter 12](textsearch.html "Chapter 12. Full Text Search").

**Table 52.62. `pg_ts_parser` Columns**

| Column Type  Description |
| --- |
| `oid` `oid`  Row identifier |
| `prsname` `name`  Text search parser name |
| `prsnamespace` `oid` (references [`pg_namespace`](catalog-pg-namespace.html "52.32. pg_namespace").`oid`)  The OID of the namespace that contains this parser |
| `prsstart` `regproc` (references [`pg_proc`](catalog-pg-proc.html "52.39. pg_proc").`oid`)  OID of the parser's startup function |
| `prstoken` `regproc` (references [`pg_proc`](catalog-pg-proc.html "52.39. pg_proc").`oid`)  OID of the parser's next-token function |
| `prsend` `regproc` (references [`pg_proc`](catalog-pg-proc.html "52.39. pg_proc").`oid`)  OID of the parser's shutdown function |
| `prsheadline` `regproc` (references [`pg_proc`](catalog-pg-proc.html "52.39. pg_proc").`oid`)  OID of the parser's headline function (zero if none) |
| `prslextype` `regproc` (references [`pg_proc`](catalog-pg-proc.html "52.39. pg_proc").`oid`)  OID of the parser's lextype function |
