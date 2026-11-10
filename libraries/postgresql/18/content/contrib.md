---
source: https://www.postgresql.org/docs/18/contrib.html
title: "Appendix F. Additional Supplied Modules and Extensions"
---


## Appendix F. Additional Supplied Modules and Extensions

This appendix and the next one contain information on the optional components found in the `contrib` directory of the PostgreSQL distribution. These include porting tools, analysis utilities, and plug-in features that are not part of the core PostgreSQL system. They are separate mainly because they address a limited audience or are too experimental to be part of the main source tree. This does not preclude their usefulness.

This appendix covers extensions and other server plug-in module libraries found in `contrib`. [Appendix G](contrib-prog.html "Appendix G. Additional Supplied Programs") covers utility programs.

When building from the source distribution, these optional components are not built automatically, unless you build the "world" target (see [Step 2](install-make.html#BUILD "Build")). You can build and install all of them by running:

```

make
make install
```

in the `contrib` directory of a configured source tree; or to build and install just one selected module, do the same in that module's subdirectory. Many of the modules have regression tests, which can be executed by running:

```

make check
```

before installation or

```

make installcheck
```

once you have a PostgreSQL server running.

If you are using a pre-packaged version of PostgreSQL, these components are typically made available as a separate subpackage, such as `postgresql-contrib`.

Many components supply new user-defined functions, operators, or types, packaged as *extensions*. To make use of one of these extensions, after you have installed the code you need to register the new SQL objects in the database system. This is done by executing a [CREATE EXTENSION](sql-createextension.html "CREATE EXTENSION") command. In a fresh database, you can simply do

```

CREATE EXTENSION extension_name;
```

This command registers the new SQL objects in the current database only, so you need to run it in every database in which you want the extension's facilities to be available. Alternatively, run it in database `template1` so that the extension will be copied into subsequently-created databases by default.

For all extensions, the `CREATE EXTENSION` command must be run by a database superuser, unless the extension is considered “trusted”. Trusted extensions can be run by any user who has `CREATE` privilege on the current database. Extensions that are trusted are identified as such in the sections that follow. Generally, trusted extensions are ones that cannot provide access to outside-the-database functionality.

The following extensions are trusted in a default installation:

|  |  |  |  |
| --- | --- | --- | --- |
| [btree\_gin](btree-gin.html "F.7. btree_gin — GIN operator classes with B-tree behavior") | [fuzzystrmatch](fuzzystrmatch.html "F.16. fuzzystrmatch — determine string similarities and distance") | [ltree](ltree.html "F.22. ltree — hierarchical tree-like data type") | [tcn](tcn.html "F.44. tcn — a trigger function to notify listeners of changes to table content") |
| [btree\_gist](btree-gist.html "F.8. btree_gist — GiST operator classes with B-tree behavior") | [hstore](hstore.html "F.17. hstore — hstore key/value datatype") | [pgcrypto](pgcrypto.html "F.26. pgcrypto — cryptographic functions") | [tsm\_system\_rows](tsm-system-rows.html "F.46. tsm_system_rows — the SYSTEM_ROWS sampling method for TABLESAMPLE") |
| [citext](citext.html "F.9. citext — a case-insensitive character string type") | [intarray](intarray.html "F.19. intarray — manipulate arrays of integers") | [pg\_trgm](pgtrgm.html "F.35. pg_trgm — support for similarity of text using trigram matching") | [tsm\_system\_time](tsm-system-time.html "F.47. tsm_system_time — the SYSTEM_TIME sampling method for TABLESAMPLE") |
| [cube](cube.html "F.10. cube — a multi-dimensional cube data type") | [isn](isn.html "F.20. isn — data types for international standard numbers (ISBN, EAN, UPC, etc.)") | [seg](seg.html "F.39. seg — a datatype for line segments or floating point intervals") | [unaccent](unaccent.html "F.48. unaccent — a text search dictionary which removes diacritics") |
| [dict\_int](dict-int.html "F.12. dict_int — example full-text search dictionary for integers") | [lo](lo.html "F.21. lo — manage large objects") | [tablefunc](tablefunc.html "F.43. tablefunc — functions that return tables (crosstab and others)") | [uuid-ossp](uuid-ossp.html "F.49. uuid-ossp — a UUID generator") |

Many extensions allow you to install their objects in a schema of your choice. To do that, add `SCHEMA schema_name` to the `CREATE EXTENSION` command. By default, the objects will be placed in your current creation target schema, which in turn defaults to `public`.

Note, however, that some of these components are not “extensions” in this sense, but are loaded into the server in some other way, for instance by way of [shared\_preload\_libraries](runtime-config-client.html#GUC-SHARED-PRELOAD-LIBRARIES). See the documentation of each component for details.
