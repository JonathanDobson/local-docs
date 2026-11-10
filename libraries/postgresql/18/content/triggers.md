---
source: https://www.postgresql.org/docs/18/triggers.html
title: "Chapter 37. Triggers"
---


## Chapter 37. Triggers

This chapter provides general information about writing trigger functions. Trigger functions can be written in most of the available procedural languages, including PL/pgSQL ([Chapter 41](plpgsql.html "Chapter 41. PL/pgSQL — SQL Procedural Language")), PL/Tcl ([Chapter 42](pltcl.html "Chapter 42. PL/Tcl — Tcl Procedural Language")), PL/Perl ([Chapter 43](plperl.html "Chapter 43. PL/Perl — Perl Procedural Language")), and PL/Python ([Chapter 44](plpython.html "Chapter 44. PL/Python — Python Procedural Language")). After reading this chapter, you should consult the chapter for your favorite procedural language to find out the language-specific details of writing a trigger in it.

It is also possible to write a trigger function in C, although most people find it easier to use one of the procedural languages. It is not currently possible to write a trigger function in the plain SQL function language.
