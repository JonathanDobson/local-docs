---
source: https://www.postgresql.org/docs/18/monitoring.html
title: "Chapter 27. Monitoring Database Activity"
---


## Chapter 27. Monitoring Database Activity

A database administrator frequently wonders, “What is the system doing right now?” This chapter discusses how to find that out.

Several tools are available for monitoring database activity and analyzing performance. Most of this chapter is devoted to describing PostgreSQL's cumulative statistics system, but one should not neglect regular Unix monitoring programs such as `ps`, `top`, `iostat`, and `vmstat`. Also, once one has identified a poorly-performing query, further investigation might be needed using PostgreSQL's [`EXPLAIN`](sql-explain.html "EXPLAIN") command. [Section 14.1](using-explain.html "14.1. Using EXPLAIN") discusses `EXPLAIN` and other methods for understanding the behavior of an individual query.
