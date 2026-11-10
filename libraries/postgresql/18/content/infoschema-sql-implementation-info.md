---
source: https://www.postgresql.org/docs/18/infoschema-sql-implementation-info.html
title: "35.49. sql_implementation_info"
---


## 35.49. `sql_implementation_info`

The table `sql_implementation_info` contains information about various aspects that are left implementation-defined by the SQL standard. This information is primarily intended for use in the context of the ODBC interface; users of other interfaces will probably find this information to be of little use. For this reason, the individual implementation information items are not described here; you will find them in the description of the ODBC interface.

**Table 35.47. `sql_implementation_info` Columns**

| Column Type  Description |
| --- |
| `implementation_info_id` `character_data`  Identifier string of the implementation information item |
| `implementation_info_name` `character_data`  Descriptive name of the implementation information item |
| `integer_value` `cardinal_number`  Value of the implementation information item, or null if the value is contained in the column `character_value` |
| `character_value` `character_data`  Value of the implementation information item, or null if the value is contained in the column `integer_value` |
| `comments` `character_data`  Possibly a comment pertaining to the implementation information item |
