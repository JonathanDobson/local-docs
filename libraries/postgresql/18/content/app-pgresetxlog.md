---
source: https://www.postgresql.org/docs/18/app-pgresetxlog.html
title: "O.4. pg_resetxlog renamed to pg_resetwal"
---


## O.4. `pg_resetxlog` renamed to `pg_resetwal`

PostgreSQL 9.6 and below provided a command named `pg_resetxlog`  to reset the write-ahead-log (WAL) files. This command was renamed to `pg_resetwal`, see [pg\_resetwal](app-pgresetwal.html "pg_resetwal") for documentation of `pg_resetwal` and see [the release notes for PostgreSQL 10](release-prior.html "E.7. Prior Releases") for details on this change.
