---
source: https://www.postgresql.org/docs/18/catalog-pg-operator.html
title: "52.34. pg_operator"
---


## 52.34. `pg_operator`

The catalog `pg_operator` stores information about operators. See [CREATE OPERATOR](sql-createoperator.html "CREATE OPERATOR") and [Section 36.14](xoper.html "36.14. User-Defined Operators") for more information.

**Table 52.34. `pg_operator` Columns**

| Column Type  Description |
| --- |
| `oid` `oid`  Row identifier |
| `oprname` `name`  Name of the operator |
| `oprnamespace` `oid` (references [`pg_namespace`](catalog-pg-namespace.html "52.32. pg_namespace").`oid`)  The OID of the namespace that contains this operator |
| `oprowner` `oid` (references [`pg_authid`](catalog-pg-authid.html "52.8. pg_authid").`oid`)  Owner of the operator |
| `oprkind` `char`  `b` = infix operator (“both”), or `l` = prefix operator (“left”) |
| `oprcanmerge` `bool`  This operator supports merge joins |
| `oprcanhash` `bool`  This operator supports hash joins |
| `oprleft` `oid` (references [`pg_type`](catalog-pg-type.html "52.64. pg_type").`oid`)  Type of the left operand (zero for a prefix operator) |
| `oprright` `oid` (references [`pg_type`](catalog-pg-type.html "52.64. pg_type").`oid`)  Type of the right operand |
| `oprresult` `oid` (references [`pg_type`](catalog-pg-type.html "52.64. pg_type").`oid`)  Type of the result (zero for a not-yet-defined “shell” operator) |
| `oprcom` `oid` (references [`pg_operator`](catalog-pg-operator.html "52.34. pg_operator").`oid`)  Commutator of this operator (zero if none) |
| `oprnegate` `oid` (references [`pg_operator`](catalog-pg-operator.html "52.34. pg_operator").`oid`)  Negator of this operator (zero if none) |
| `oprcode` `regproc` (references [`pg_proc`](catalog-pg-proc.html "52.39. pg_proc").`oid`)  Function that implements this operator (zero for a not-yet-defined “shell” operator) |
| `oprrest` `regproc` (references [`pg_proc`](catalog-pg-proc.html "52.39. pg_proc").`oid`)  Restriction selectivity estimation function for this operator (zero if none) |
| `oprjoin` `regproc` (references [`pg_proc`](catalog-pg-proc.html "52.39. pg_proc").`oid`)  Join selectivity estimation function for this operator (zero if none) |
