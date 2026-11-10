---
title: "OIDC connections overview"
source: https://docs.docker.com/security/authentication/oidc-connections/
---

# OIDC connections overview




OIDC connections create a trust relationship between Docker and a trusted
third party so you don't have to maintain long-lived credentials. When you
create an OIDC connection, Docker exchanges short-lived tokens with another
vendor that can grant fine-grained access to your Docker resources.

## How OIDC connections work

OIDC connections follow the OpenID Connect (OIDC) standard. Establishing a
trust relationship involves creating the connection, configuring a
workflow, and testing. A connection, then, is the named trust relationship
in Docker Home that workflows point to. For example, a trust relationship
between Docker and GitHub follows these steps:

- GitHub issues a JWT ID token for the workflow run.
- During authentication, Docker:
  - Verifies the token against GitHub's public key registry
  - Matches subject claims against rulesets created in
    [Docker Home](https://app.docker.com/)
- Docker returns an access token so the GitHub Action can sign in to Docker
  and access resources.

All tokens created and exchanged during an OIDC workflow are short-lived
and issued on a per-workflow basis.

For how OIDC connections compare to organization access tokens, see
[Access tokens](/security/access-tokens/).

## Connection limits

The number of OIDC connections an organization can have depends on its
subscription:

| Subscription | Maximum OIDC connections |
| :----------- | :----------------------- |
| Team         | 10                       |
| [Docker-Sponsored Open Source](/docker-hub/repos/manage/trusted-content/dsos-program/) | 10 |
| Business     | 100                      |

Active and deactivated connections count toward the limit, but deleted
connections don't. When your organization reaches the limit, the
**Create OIDC connection** button is disabled. To create another
connection, delete one you no longer need.

Each connection can have up to five rulesets. See
[Rulesets](/security/authentication/oidc-connections/rulesets-claims/#rulesets).

## Next steps

- [Create an OIDC connection](/security/authentication/oidc-connections/create-manage/)
- [OIDC rulesets and subject claims](/security/authentication/oidc-connections/rulesets-claims/)
- [Troubleshoot OIDC connections](/security/authentication/oidc-connections/troubleshoot/)
