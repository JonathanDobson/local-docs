---
source: https://www.postgresql.org/docs/18/view-pg-available-extensions.html
title: "53.3. pg_available_extensions"
---


## 53.3. `pg_available_extensions`

The `pg_available_extensions` view lists the extensions that are available for installation. See also the [`pg_extension`](catalog-pg-extension.html "52.22. pg_extension") catalog, which shows the extensions currently installed.

**Table 53.3. `pg_available_extensions` Columns**

| Column Type  Description |
| --- |
| `name` `name`  Extension name |
| `default_version` `text`  Name of default version, or `NULL` if none is specified |
| `installed_version` `text`  Currently installed version of the extension, or `NULL` if not installed |
| `comment` `text`  Comment string from the extension's control file |

  

The `pg_available_extensions` view is read-only.
