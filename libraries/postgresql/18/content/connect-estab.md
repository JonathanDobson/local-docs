---
source: https://www.postgresql.org/docs/18/connect-estab.html
title: "51.2. How Connections Are Established"
---


## 51.2. How Connections Are Established

PostgreSQL implements a “process per user” client/server model. In this model, every [client process](glossary.html#GLOSSARY-CLIENT "Client (process)") connects to exactly one [backend process](glossary.html#GLOSSARY-BACKEND "Backend (process)"). As we do not know ahead of time how many connections will be made, we have to use a “supervisor process” that spawns a new backend process every time a connection is requested. This supervisor process is called [postmaster](glossary.html#GLOSSARY-POSTMASTER "Postmaster (process)") and listens at a specified TCP/IP port for incoming connections. Whenever it detects a request for a connection, it spawns a new backend process. Those backend processes communicate with each other and with other processes of the [instance](glossary.html#GLOSSARY-INSTANCE "Instance") using *semaphores* and [shared memory](glossary.html#GLOSSARY-SHARED-MEMORY "Shared memory") to ensure data integrity throughout concurrent data access.

The client process can be any program that understands the PostgreSQL protocol described in [Chapter 54](protocol.html "Chapter 54. Frontend/Backend Protocol"). Many clients are based on the C-language library libpq, but several independent implementations of the protocol exist, such as the Java JDBC driver.

Once a connection is established, the client process can send a query to the backend process it's connected to. The query is transmitted using plain text, i.e., there is no parsing done in the client. The backend process parses the query, creates an *execution plan*, executes the plan, and returns the retrieved rows to the client by transmitting them over the established connection.
