---
source: https://www.postgresql.org/docs/18/infoschema-administrable-role-authorizations.html
title: "35.4. administrable_role_​authorizations"
---


## 35.4. `administrable_role_​authorizations`

The view `administrable_role_authorizations` identifies all roles that the current user has the admin option for.

**Table 35.2. `administrable_role_authorizations` Columns**

| Column Type  Description |
| --- |
| `grantee` `sql_identifier`  Name of the role to which this role membership was granted (can be the current user, or a different role in case of nested role memberships) |
| `role_name` `sql_identifier`  Name of a role |
| `is_grantable` `yes_or_no`  Always `YES` |
