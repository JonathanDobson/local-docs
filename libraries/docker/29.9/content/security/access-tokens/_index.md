---
title: "Access tokens"
source: https://docs.docker.com/security/access-tokens/
---

# Access tokens


Access tokens authenticate to Docker Hub in place of a password. Docker
Hub offers two types: personal access tokens (PATs), tied to your
account, and organization access tokens (OATs), owned by an
organization. Both work with `docker login` and in automation, and you
can deactivate or delete a token at any time without changing a
password.

## Choose a token type

Pick a PAT for work that runs as you, or an OAT for organization-owned
automation.

## Personal access tokens (PATs) {#pats}

A PAT has
[one repository permission](/security/access-tokens/reference/#personal-access-token-permissions)
for every repository the account can access. A PAT can also grant
[Cloud Sandboxes access](/security/access-tokens/reference/#cloud-sandboxes-access),
which is a separate setting on the token.

Use a PAT for Docker Desktop, for environments governed by
[Image Access Management](/desktop/enterprise/hardened-desktop/image-access-management/),
and for other tools that run as you. A PAT is also required to sign in
to the CLI when two-factor authentication (2FA) is turned on or single
sign-on (SSO) is enforced, because the CLI doesn't accept your password
in those cases.

## Organization access tokens (OATs) {#oats}

Use an OAT for production systems that pull images during deployment,
monitoring or backup tools that check repository status or pull images,
third-party services that integrate with your repositories, and scripts
that call the
[Docker Hub API](/security/access-tokens/reference/#docker-hub-api).
OATs don't work with Docker Desktop or Image Access Management.

An OAT can be limited to specific repositories and operations, and it
has its own Docker Hub usage limits, separate from individual accounts.
To see scopes, see
[Access token reference](/security/access-tokens/reference/).

## OIDC connections

If your automation runs in GitHub Actions, you don't need to store a token.
An [OIDC connection](/security/authentication/oidc-connections/)
lets a workflow exchange GitHub's short-lived identity token for Docker
access on each run, so there is no long-lived credential to rotate,
scope, or leak. Organization owners set up OIDC connections, and they
require a Docker Team or Docker Business subscription.

Use an OAT instead when the automation runs outside GitHub Actions, or
when you need a credential that works with `docker login` from any
system.

## Next steps
