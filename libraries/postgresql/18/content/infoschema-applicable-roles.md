---
source: https://www.postgresql.org/docs/18/infoschema-applicable-roles.html
title: "35.5. applicable_roles"
---


## 35.5. `applicable_roles`

The view `applicable_roles` identifies all roles whose privileges the current user can use. This means there is some chain of role grants from the current user to the role in question. The current user itself is also an applicable role. The set of applicable roles is generally used for permission checking.

**Table 35.3. `applicable_roles` Columns**

| Column Type  Description |
| --- |
| `grantee` `sql_identifier`  Name of the role to which this role membership was granted (can be the current user, or a different role in case of nested role memberships) |
| `role_name` `sql_identifier`  Name of a role |
| `is_grantable` `yes_or_no`  `YES` if the grantee has the admin option on the role, `NO` if not |
