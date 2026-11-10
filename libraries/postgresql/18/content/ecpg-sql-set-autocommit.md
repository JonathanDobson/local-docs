---
source: https://www.postgresql.org/docs/18/ecpg-sql-set-autocommit.html
title: "SET AUTOCOMMIT"
---


## SET AUTOCOMMIT

SET AUTOCOMMIT — set the autocommit behavior of the current session

## Synopsis

```

SET AUTOCOMMIT { = | TO } { ON | OFF }
```

## Description

`SET AUTOCOMMIT` sets the autocommit behavior of the current database session. By default, embedded SQL programs are *not* in autocommit mode, so `COMMIT` needs to be issued explicitly when desired. This command can change the session to autocommit mode, where each individual statement is committed implicitly.

## Compatibility

`SET AUTOCOMMIT` is an extension of PostgreSQL ECPG.
