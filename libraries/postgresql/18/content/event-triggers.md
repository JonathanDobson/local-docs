---
source: https://www.postgresql.org/docs/18/event-triggers.html
title: "Chapter 38. Event Triggers"
---


## Chapter 38. Event Triggers

To supplement the trigger mechanism discussed in [Chapter 37](triggers.html "Chapter 37. Triggers"), PostgreSQL also provides event triggers. Unlike regular triggers, which are attached to a single table and capture only DML events, event triggers are global to a particular database and are capable of capturing DDL events.

Like regular triggers, event triggers can be written in any procedural language that includes event trigger support, or in C, but not in plain SQL.
