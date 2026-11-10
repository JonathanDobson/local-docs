---
source: https://www.postgresql.org/docs/18/catalog-pg-largeobject-metadata.html
title: "52.31. pg_largeobject_metadata"
---


## 52.31. `pg_largeobject_metadata`

The catalog `pg_largeobject_metadata` holds metadata associated with large objects. The actual large object data is stored in [`pg_largeobject`](catalog-pg-largeobject.html "52.30. pg_largeobject").

**Table 52.31. `pg_largeobject_metadata` Columns**

| Column Type  Description |
| --- |
| `oid` `oid`  Row identifier |
| `lomowner` `oid` (references [`pg_authid`](catalog-pg-authid.html "52.8. pg_authid").`oid`)  Owner of the large object |
| `lomacl` `aclitem[]`  Access privileges; see [Section 5.8](ddl-priv.html "5.8. Privileges") for details |
