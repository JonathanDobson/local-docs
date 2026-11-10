---
source: https://www.postgresql.org/docs/18/logicaldecoding-writer.html
title: "47.7. Logical Decoding Output Writers"
---


## 47.7. Logical Decoding Output Writers

It is possible to add more output methods for logical decoding. For details, see `src/backend/replication/logical/logicalfuncs.c`. Essentially, three functions need to be provided: one to read WAL, one to prepare writing output, and one to write the output (see [Section 47.6.5](logicaldecoding-output-plugin.html#LOGICALDECODING-OUTPUT-PLUGIN-OUTPUT "47.6.5. Functions for Producing Output")).
