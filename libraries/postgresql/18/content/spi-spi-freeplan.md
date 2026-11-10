---
source: https://www.postgresql.org/docs/18/spi-spi-freeplan.html
title: "SPI_freeplan"
---


## SPI\_freeplan

SPI\_freeplan — free a previously saved prepared statement

## Synopsis

```

int SPI_freeplan(SPIPlanPtr plan)
```

## Description

`SPI_freeplan` releases a prepared statement previously returned by `SPI_prepare` or saved by `SPI_keepplan` or `SPI_saveplan`.

## Arguments

`SPIPlanPtr plan`
:   pointer to statement to free

## Return Value

0 on success; `SPI_ERROR_ARGUMENT` if *`plan`* is `NULL` or invalid
