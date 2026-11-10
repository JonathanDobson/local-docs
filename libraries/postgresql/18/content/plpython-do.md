---
source: https://www.postgresql.org/docs/18/plpython-do.html
title: "44.4. Anonymous Code Blocks"
---


## 44.4. Anonymous Code Blocks

PL/Python also supports anonymous code blocks called with the [DO](sql-do.html "DO") statement:

```

DO $$
    # PL/Python code
$$ LANGUAGE plpython3u;
```

An anonymous code block receives no arguments, and whatever value it might return is discarded. Otherwise it behaves just like a function.
