---
source: https://www.postgresql.org/docs/18/dblink.html
title: "F.11. dblink — connect to other PostgreSQL databases"
---


## F.11. dblink — connect to other PostgreSQL databases

`dblink` is a module that supports connections to other PostgreSQL databases from within a database session.

`dblink` can report the following wait events under the wait event type `Extension`.

`DblinkConnect`
:   Waiting to establish a connection to a remote server.

`DblinkGetConnect`
:   Waiting to establish a connection to a remote server when it could not be found in the list of already-opened connections.

`DblinkGetResult`
:   Waiting to receive the results of a query from a remote server.

See also [postgres\_fdw](postgres-fdw.html "F.38. postgres_fdw — access data stored in external PostgreSQL servers"), which provides roughly the same functionality using a more modern and standards-compliant infrastructure.
