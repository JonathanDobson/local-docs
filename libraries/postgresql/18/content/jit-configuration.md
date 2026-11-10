---
source: https://www.postgresql.org/docs/18/jit-configuration.html
title: "30.3. Configuration"
---


## 30.3. Configuration

The configuration variable [jit](runtime-config-query.html#GUC-JIT) determines whether JIT compilation is enabled or disabled. If it is enabled, the configuration variables [jit\_above\_cost](runtime-config-query.html#GUC-JIT-ABOVE-COST), [jit\_inline\_above\_cost](runtime-config-query.html#GUC-JIT-INLINE-ABOVE-COST), and [jit\_optimize\_above\_cost](runtime-config-query.html#GUC-JIT-OPTIMIZE-ABOVE-COST) determine whether JIT compilation is performed for a query, and how much effort is spent doing so.

[jit\_provider](runtime-config-client.html#GUC-JIT-PROVIDER) determines which JIT implementation is used. It is rarely required to be changed. See [Section 30.4.2](jit-extensibility.html#JIT-PLUGGABLE "30.4.2. Pluggable JIT Providers").

For development and debugging purposes a few additional configuration parameters exist, as described in [Section 19.17](runtime-config-developer.html "19.17. Developer Options").
