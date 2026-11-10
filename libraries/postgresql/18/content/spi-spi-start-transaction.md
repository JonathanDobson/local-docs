---
source: https://www.postgresql.org/docs/18/spi-spi-start-transaction.html
title: "SPI_start_transaction"
---


## SPI\_start\_transaction

SPI\_start\_transaction — obsolete function

## Synopsis

```

void SPI_start_transaction(void)
```

## Description

`SPI_start_transaction` does nothing, and exists only for code compatibility with earlier PostgreSQL releases. It used to be required after calling `SPI_commit` or `SPI_rollback`, but now those functions start a new transaction automatically.
