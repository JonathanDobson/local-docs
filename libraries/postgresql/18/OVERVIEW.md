# PostgreSQL 18 — overview

The official PostgreSQL manual for **version 18** (newest release **18.6** on
2026-11-10; PostgreSQL 19 was at release candidate), crawled from
postgresql.org/docs/18/, plus the official **postgres Docker image** docs. One
Markdown file per page of the manual; each file's front matter has its `source:` URL.

## Layout

Files keep the site's page names (`sql-createindex.md` is `…/docs/18/sql-createindex.html`),
so the folder is flat. Page-name prefixes tell you the area:

| Prefix | What it holds |
|---|---|
| `tutorial-*` | Tutorial |
| `sql-*.md` | **SQL command reference** — one page per command (`sql-createtable.md`, `sql-altertable.md`, `sql-select.md`, `sql-copy.md`, `sql-vacuum.md`…) |
| `datatype-*`, `functions-*` | Data types; functions and operators (`functions-json.md`, `functions-datetime.md`, `functions-uuid.md`…) |
| `indexes-*`, `gin*`, `gist*`, `brin*`, `btree*` | Indexes and index types |
| `ddl-*`, `dml-*`, `queries-*` | Defining tables, partitioning, constraints, inserting/updating, queries |
| `textsearch-*` | Full text search |
| `performance-tips`, `using-explain`, `planner-*`, `parallel-*` | Query performance and EXPLAIN |
| `runtime-config-*` | **Server configuration parameters** (`postgresql.conf`), one page per area |
| `auth-*`, `client-authentication`, `user-manag`, `ddl-priv` | `pg_hba.conf`, password/SCRAM/OAuth auth, roles and privileges |
| `backup-*`, `continuous-archiving`, `high-availability`, `warm-standby`, `logical-replication-*` | Backup, PITR, replication |
| `upgrading`, `pgupgrade` | Upgrading between major versions |
| `app-*` | Client and server programs: `app-psql.md`, `app-pgdump.md`, `app-pg-dumpall.md`, `app-pgrestore.md`, `app-initdb.md`, `app-postgres.md` |
| `monitoring-*`, `view-*`, `catalog-*` | Statistics views, system views and catalogs |
| `libpq-*`, `ecpg-*` | C client library (connection strings, env vars like `PGHOST`) |
| `plpgsql-*`, `xfunc-*`, `triggers`, `event-triggers` | Server-side programming |
| Contrib module pages (`pgstatstatements.md`, `pgtrgm.md`, `postgres-fdw.md`…) | Additional supplied modules (appendix F) |
| `release-notes/` | Release notes: `release-18.md` (18.0 incl. "Migration to Version 18"), `release-18-1.md` … `release-18-6.md` |
| `docker-image/README.md` | The postgres Docker Official Image: tags, env vars, `*_FILE` secrets, `/docker-entrypoint-initdb.d`, `PGDATA`, Alpine vs Debian |

## Where to look for…

- **A SQL command's syntax** — `sql-<command>.md` (no spaces: `sql-createindex.md`, `sql-altertable.md`).
- **A config parameter (`shared_buffers`, `max_connections`, `work_mem`…)** — `runtime-config-*.md`; how settings are set in `config-setting.md`.
- **Who can connect and how (`pg_hba.conf`)** — `auth-pg-hba-conf.md`, `auth-password.md`.
- **Backups** — `backup-dump.md` (pg_dump), `continuous-archiving.md` (WAL archiving, PITR), `app-pgbasebackup.md`.
- **Upgrading a major version** — `upgrading.md`, `pgupgrade.md`, and "Migration to Version 18" in `release-notes/release-18.md`.
- **psql meta-commands (`\d`, `\copy`…)** — `app-psql.md`.
- **JSON / JSONB** — `datatype-json.md`, `functions-json.md`.
- **EXPLAIN and slow queries** — `using-explain.md`, `performance-tips.md`, `pgstatstatements.md`.
- **Replication** — `high-availability.md`, `warm-standby.md`, `logical-replication.md`.
- **Running it in Docker (env vars, secrets, init scripts, data directory)** — `docker-image/README.md`.

## Version notes (from `release-notes/release-18.md`)

- **New in 18**: asynchronous I/O (AIO); `pg_upgrade` keeps optimizer statistics; B-tree "skip scan" for multicolumn indexes; `uuidv7()`; virtual generated columns (now the default for generated columns); OAuth authentication; `OLD`/`NEW` in `RETURNING`; temporal constraints (PRIMARY KEY, UNIQUE, FOREIGN KEY over ranges).
- **Incompatibilities**: `initdb` enables data checksums by default (`--no-data-checksums` to opt out; `pg_upgrade` needs matching settings); **MD5 password authentication is deprecated** (warnings on `CREATE/ALTER ROLE`); `VACUUM`/`ANALYZE` now process inheritance children (use `ONLY` for the old behaviour); `COPY FROM` no longer treats `\.` as end-of-file in CSV; unlogged partitioned tables are disallowed; `AFTER` triggers run as the role active when the event was queued; time-zone abbreviation lookup order changed.
- **Docker image**: from PostgreSQL 18 the image's `PGDATA` is version-specific, `/var/lib/postgresql/18/docker`, and the volume should be mounted at `/var/lib/postgresql`; for 17 and below mount at `/var/lib/postgresql/data`. Stacks that set `PGDATA` explicitly need their volume layout checked before upgrading (see the `PGDATA` section of `docker-image/README.md`).

## Search tips

- The docs say "role" for users and groups, "cluster" for one server's set of databases, "relation" for tables, views and indexes, and "GUC" (grand unified configuration) for config parameters.
- Section numbers appear in titles (`11.8. Partial Indexes`); `sql-*` and `app-*` pages are reference entries.
- Links between pages point at `<page>.html`; the matching file here is `<page>.md` (release notes are under `release-notes/`).
