---
source: https://www.postgresql.org/docs/18/color-when.html
title: "N.1. When Color is Used"
---


## N.1. When Color is Used

To use colorized output, set the environment variable `PG_COLOR` as follows:

1. If the value is `always`, then color is used.
2. If the value is `auto` and the standard error stream is associated with a terminal device, then color is used.
3. Otherwise, color is not used.
