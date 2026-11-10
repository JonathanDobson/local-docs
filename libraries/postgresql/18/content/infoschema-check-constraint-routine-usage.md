---
source: https://www.postgresql.org/docs/18/infoschema-check-constraint-routine-usage.html
title: "35.8. check_constraint_routine_usage"
---


## 35.8. `check_constraint_routine_usage`

The view `check_constraint_routine_usage` identifies routines (functions and procedures) that are used by a check constraint. Only those routines are shown that are owned by a currently enabled role.

**Table 35.6. `check_constraint_routine_usage` Columns**

| Column Type  Description |
| --- |
| `constraint_catalog` `sql_identifier`  Name of the database containing the constraint (always the current database) |
| `constraint_schema` `sql_identifier`  Name of the schema containing the constraint |
| `constraint_name` `sql_identifier`  Name of the constraint |
| `specific_catalog` `sql_identifier`  Name of the database containing the function (always the current database) |
| `specific_schema` `sql_identifier`  Name of the schema containing the function |
| `specific_name` `sql_identifier`  The “specific name” of the function. See [Section 35.45](infoschema-routines.html "35.45. routines") for more information. |
