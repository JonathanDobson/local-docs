---
source: https://www.postgresql.org/docs/18/archive-modules.html
title: "Chapter 49. Archive Modules"
---


## Chapter 49. Archive Modules

PostgreSQL provides infrastructure to create custom modules for continuous archiving (see [Section 25.3](continuous-archiving.html "25.3. Continuous Archiving and Point-in-Time Recovery (PITR)")). While archiving via a shell command (i.e., [archive\_command](runtime-config-wal.html#GUC-ARCHIVE-COMMAND)) is much simpler, a custom archive module will often be considerably more robust and performant.

When a custom [archive\_library](runtime-config-wal.html#GUC-ARCHIVE-LIBRARY) is configured, PostgreSQL will submit completed WAL files to the module, and the server will avoid recycling or removing these WAL files until the module indicates that the files were successfully archived. It is ultimately up to the module to decide what to do with each WAL file, but many recommendations are listed at [Section 25.3.1](continuous-archiving.html#BACKUP-ARCHIVING-WAL "25.3.1. Setting Up WAL Archiving").

Archiving modules must at least consist of an initialization function (see [Section 49.1](archive-module-init.html "49.1. Initialization Functions")) and the required callbacks (see [Section 49.2](archive-module-callbacks.html "49.2. Archive Module Callbacks")). However, archive modules are also permitted to do much more (e.g., declare GUCs and register background workers).

The `contrib/basic_archive` module contains a working example, which demonstrates some useful techniques.
