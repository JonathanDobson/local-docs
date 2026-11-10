---
source: https://www.postgresql.org/docs/18/views.html
title: "Chapter 53. System Views"
---


## Chapter 53. System Views

In addition to the system catalogs, PostgreSQL provides a number of built-in views. Some system views provide convenient access to some commonly used queries on the system catalogs. Other views provide access to internal server state.

The information schema ([Chapter 35](information-schema.html "Chapter 35. The Information Schema")) provides an alternative set of views which overlap the functionality of the system views. Since the information schema is SQL-standard whereas the views described here are PostgreSQL-specific, it's usually better to use the information schema if it provides all the information you need.

[Table 53.1](views-overview.html#VIEW-TABLE "Table 53.1. System Views") lists the system views described here. More detailed documentation of each view follows below. There are some additional views that provide access to accumulated statistics; they are described in [Table 27.2](monitoring-stats.html#MONITORING-STATS-VIEWS-TABLE "Table 27.2. Collected Statistics Views").
