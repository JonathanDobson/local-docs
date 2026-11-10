---
source: https://www.postgresql.org/docs/18/view-pg-user.html
title: "53.35. pg_user"
---


## 53.35. `pg_user`

The view `pg_user` provides access to information about database users. This is simply a publicly readable view of [`pg_shadow`](view-pg-shadow.html "53.26. pg_shadow") that blanks out the password field.

**Table 53.35. `pg_user` Columns**

| Column Type  Description |
| --- |
| `usename` `name`  User name |
| `usesysid` `oid`  ID of this user |
| `usecreatedb` `bool`  User can create databases |
| `usesuper` `bool`  User is a superuser |
| `userepl` `bool`  User can initiate streaming replication and put the system in and out of backup mode. |
| `usebypassrls` `bool`  User bypasses every row-level security policy, see [Section 5.9](ddl-rowsecurity.html "5.9. Row Security Policies") for more information. |
| `passwd` `text`  Not the password (always reads as `********`) |
| `valuntil` `timestamptz`  Password expiry time (only used for password authentication) |
| `useconfig` `text[]`  Session defaults for run-time configuration variables |
