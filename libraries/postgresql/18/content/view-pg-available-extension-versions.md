---
source: https://www.postgresql.org/docs/18/view-pg-available-extension-versions.html
title: "53.4. pg_available_extension_versions"
---


## 53.4. `pg_available_extension_versions`

The `pg_available_extension_versions` view lists the specific extension versions that are available for installation. See also the [`pg_extension`](catalog-pg-extension.html "52.22. pg_extension") catalog, which shows the extensions currently installed.

**Table 53.4. `pg_available_extension_versions` Columns**

| Column Type  Description |
| --- |
| `name` `name`  Extension name |
| `version` `text`  Version name |
| `installed` `bool`  True if this version of this extension is currently installed |
| `superuser` `bool`  True if only superusers are allowed to install this extension (but see `trusted`) |
| `trusted` `bool`  True if the extension can be installed by non-superusers with appropriate privileges |
| `relocatable` `bool`  True if extension can be relocated to another schema |
| `schema` `name`  Name of the schema that the extension must be installed into, or `NULL` if partially or fully relocatable |
| `requires` `name[]`  Names of prerequisite extensions, or `NULL` if none |
| `comment` `text`  Comment string from the extension's control file |

  

The `pg_available_extension_versions` view is read-only.
