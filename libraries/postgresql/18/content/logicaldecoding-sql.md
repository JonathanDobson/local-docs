---
source: https://www.postgresql.org/docs/18/logicaldecoding-sql.html
title: "47.4. Logical Decoding SQL Interface"
---


## 47.4. Logical Decoding SQL Interface

See [Section 9.28.6](functions-admin.html#FUNCTIONS-REPLICATION "9.28.6. Replication Management Functions") for detailed documentation on the SQL-level API for interacting with logical decoding.

Synchronous replication (see [Section 26.2.8](warm-standby.html#SYNCHRONOUS-REPLICATION "26.2.8. Synchronous Replication")) is only supported on replication slots used over the streaming replication interface. The function interface and additional, non-core interfaces do not support synchronous replication.
