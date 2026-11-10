---
source: https://www.postgresql.org/docs/18/view-pg-config.html
title: "53.6. pg_config"
---


## 53.6. `pg_config`

The view `pg_config` describes the compile-time configuration parameters of the currently installed version of PostgreSQL. It is intended, for example, to be used by software packages that want to interface to PostgreSQL to facilitate finding the required header files and libraries. It provides the same basic information as the [pg\_config](app-pgconfig.html "pg_config") PostgreSQL client application.

By default, the `pg_config` view can be read only by superusers.

**Table 53.6. `pg_config` Columns**

| Column Type  Description |
| --- |
| `name` `text`  The parameter name |
| `setting` `text`  The parameter value |
