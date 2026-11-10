---
title: "Secure Docker accounts and organizations"
source: https://docs.docker.com/security/
---

# Secure Docker accounts and organizations


Use these settings to protect your own sign-in, and to control who can join
an organization and what they can do. You configure them in
[Docker Home](https://app.docker.com/).

## Secure your account

Docker offers several methods to secure your account. You can choose how you sign in and what the CLI uses instead of your password.

- [Two-factor authentication](/security/authentication/2fa/)
  (2FA) requires a time-based one-time password (TOTP) from an authenticator
  app after you enter your password.
- A [personal access token](/security/access-tokens/personal-access-tokens/)
  (PAT) signs you in to the Docker CLI and other tools in place of your
  password. The CLI requires a PAT when two-factor authentication (2FA) is
  on or single sign-on (SSO) is enforced.
- [Connected accounts](/accounts/individual/manage-account/#manage-connected-accounts)
  let you sign in with Google or GitHub when the provider account uses the
  same email address as your Docker account.

## Secure your organization

Owners can choose how members sign in, how Docker adds them, and what they can do.

- [Single sign-on](/security/authentication/single-sign-on/)
  (SSO) allows members to sign-in through your identity provider.
- [Provisioning](/security/provisioning/) adds users with
  SCIM, Just-in-Time (JIT) provisioning, or auto-provisioning. Once an SSO connection exists, Docker enables JIT by default, or you can configure SCIM.
- An [organization access token](/security/access-tokens/organization-access-tokens/)
  (OAT) gives automation access on Docker Hub to selected repositories,
  organization settings, Docker Build Cloud, and Docker Governance. It
  belongs to the organization, so that access keeps working when people
  join or leave.
- [OIDC connections](/security/authentication/oidc-connections/)
  let GitHub Actions sign in with a short-lived token instead of a
  long-lived OAT. Organization owners and editors can create, update, and
  delete these connections.
- [Roles and permissions](/security/roles-and-permissions/)
  control what members can do after they join.

## Next steps

- [Choose a personal or organization access token](/security/access-tokens/).
- [Choose how to add users](/security/provisioning/).
- Compare what members can do in
  [Roles and permissions](/security/roles-and-permissions/core-roles/).
