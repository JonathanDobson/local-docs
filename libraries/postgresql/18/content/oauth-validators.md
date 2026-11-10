---
source: https://www.postgresql.org/docs/18/oauth-validators.html
title: "Chapter 50. OAuth Validator Modules"
---


## Chapter 50. OAuth Validator Modules

PostgreSQL provides infrastructure for creating custom modules to perform server-side validation of OAuth bearer tokens. Because OAuth implementations vary so wildly, and bearer token validation is heavily dependent on the issuing party, the server cannot check the token itself; validator modules provide the integration layer between the server and the OAuth provider in use.

OAuth validator modules must at least consist of an initialization function (see [Section 50.2](oauth-validator-init.html "50.2. Initialization Functions")) and the required callback for performing validation (see [Section 50.3.2](oauth-validator-callbacks.html#OAUTH-VALIDATOR-CALLBACK-VALIDATE "50.3.2. Validate Callback")).

### Warning

Since a misbehaving validator might let unauthorized users into the database, correct implementation is crucial for server safety. See [Section 50.1](oauth-validator-design.html "50.1. Safely Designing a Validator Module") for design considerations.
