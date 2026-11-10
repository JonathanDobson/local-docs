---
source: https://www.postgresql.org/docs/18/view-pg-shadow.html
title: "53.26. pg_shadow"
---


## 53.26. `pg_shadow`

The view `pg_shadow` exists for backwards compatibility: it emulates a catalog that existed in PostgreSQL before version 8.1. It shows properties of all roles that are marked as `rolcanlogin` in [`pg_authid`](catalog-pg-authid.html "52.8. pg_authid").

The name stems from the fact that this table should not be readable by the public since it contains passwords. [`pg_user`](view-pg-user.html "53.35. pg_user") is a publicly readable view on `pg_shadow` that blanks out the password field.

**Table 53.26. `pg_shadow` Columns**

| Column Type  Description |
| --- |
| `usename` `name` (references [`pg_authid`](catalog-pg-authid.html "52.8. pg_authid").`rolname`)  User name |
| `usesysid` `oid` (references [`pg_authid`](catalog-pg-authid.html "52.8. pg_authid").`oid`)  ID of this user |
| `usecreatedb` `bool`  User can create databases |
| `usesuper` `bool`  User is a superuser |
| `userepl` `bool`  User can initiate streaming replication and put the system in and out of backup mode. |
| `usebypassrls` `bool`  User bypasses every row-level security policy, see [Section 5.9](ddl-rowsecurity.html "5.9. Row Security Policies") for more information. |
| `passwd` `text`  Encrypted password; null if none. See [`pg_authid`](catalog-pg-authid.html "52.8. pg_authid") for details of how encrypted passwords are stored. |
| `valuntil` `timestamptz`  Password expiry time (only used for password authentication) |
| `useconfig` `text[]`  Session defaults for run-time configuration variables |
