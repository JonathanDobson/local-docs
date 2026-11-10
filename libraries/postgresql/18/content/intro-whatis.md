---
source: https://www.postgresql.org/docs/18/intro-whatis.html
title: "1.  What Is PostgreSQL?"
---


## 1.  What Is PostgreSQL?

PostgreSQL is an object-relational database management system (ORDBMS) based on [POSTGRES, Version 4.2](https://dsf.berkeley.edu/postgres.html), developed at the University of California at Berkeley Computer Science Department. POSTGRES pioneered many concepts that only became available in some commercial database systems much later.

PostgreSQL is an open-source descendant of this original Berkeley code. It supports a large part of the SQL standard and offers many modern features:

- [complex queries](sql.html "Part II. The SQL Language")
- [foreign keys](ddl-constraints.html#DDL-CONSTRAINTS-FK "5.5.5. Foreign Keys")
- [triggers](triggers.html "Chapter 37. Triggers")
- [updatable views](sql-createview.html#SQL-CREATEVIEW-UPDATABLE-VIEWS "Updatable Views")
- [transactional integrity](transaction-iso.html "13.2. Transaction Isolation")
- [multiversion concurrency control](mvcc.html "Chapter 13. Concurrency Control")

Also, PostgreSQL can be extended by the user in many ways, for example by adding new

- [data types](datatype.html "Chapter 8. Data Types")
- [functions](functions.html "Chapter 9. Functions and Operators")
- [operators](functions.html "Chapter 9. Functions and Operators")
- [aggregate functions](functions-aggregate.html "9.21. Aggregate Functions")
- [index methods](indexes.html "Chapter 11. Indexes")
- [procedural languages](server-programming.html "Part V. Server Programming")

And because of the liberal license, PostgreSQL can be used, modified, and distributed by anyone free of charge for any purpose, be it private, commercial, or academic.
