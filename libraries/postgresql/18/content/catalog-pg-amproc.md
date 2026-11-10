---
source: https://www.postgresql.org/docs/18/catalog-pg-amproc.html
title: "52.5. pg_amproc"
---


## 52.5. `pg_amproc`

The catalog `pg_amproc` stores information about support functions associated with access method operator families. There is one row for each support function belonging to an operator family.

**Table 52.5. `pg_amproc` Columns**

| Column Type  Description |
| --- |
| `oid` `oid`  Row identifier |
| `amprocfamily` `oid` (references [`pg_opfamily`](catalog-pg-opfamily.html "52.35. pg_opfamily").`oid`)  The operator family this entry is for |
| `amproclefttype` `oid` (references [`pg_type`](catalog-pg-type.html "52.64. pg_type").`oid`)  Left-hand input data type of associated operator |
| `amprocrighttype` `oid` (references [`pg_type`](catalog-pg-type.html "52.64. pg_type").`oid`)  Right-hand input data type of associated operator |
| `amprocnum` `int2`  Support function number |
| `amproc` `regproc` (references [`pg_proc`](catalog-pg-proc.html "52.39. pg_proc").`oid`)  OID of the function |

  

The usual interpretation of the `amproclefttype` and `amprocrighttype` fields is that they identify the left and right input types of the operator(s) that a particular support function supports. For some access methods these match the input data type(s) of the support function itself, for others not. There is a notion of “default” support functions for an index, which are those with `amproclefttype` and `amprocrighttype` both equal to the index operator class's `opcintype`.
