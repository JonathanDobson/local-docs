---
source: https://www.postgresql.org/docs/18/spi-spi-freetuple.html
title: "SPI_freetuple"
---


## SPI\_freetuple

SPI\_freetuple — free a row allocated in the upper executor context

## Synopsis

```

void SPI_freetuple(HeapTuple row)
```

## Description

`SPI_freetuple` frees a row previously allocated in the upper executor context.

This function is no longer different from plain `heap_freetuple`. It's kept just for backward compatibility of existing code.

## Arguments

`HeapTuple row`
:   row to free
