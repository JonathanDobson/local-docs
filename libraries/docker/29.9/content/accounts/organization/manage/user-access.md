---
title: "Plan and maintain user access"
source: https://docs.docker.com/accounts/organization/manage/user-access/
---

# Plan and maintain user access


Use this workflow to decide who needs access to your Docker organization,
assign appropriate permissions, and keep membership aligned with changing
responsibilities. It links to the procedures for onboarding, provisioning,
and monitoring so you can apply those decisions.

## Setting up roles and permissions in Docker

### Identify your Docker users and accounts

Inventory the people who need Docker access, the projects they work on, and
the resources they need. Use device management records or ask development
teams to identify existing Docker Desktop users. Ask users to use their
business email for their Docker accounts.

Follow [organization onboarding](/accounts/organization/setup/onboard/)
for the identification procedure and seat planning. Keep this inventory as
the starting point for access reviews.

### Assign roles strategically

Choose the minimum permissions each person needs. Compare the built-in
Member, Editor, and Owner roles with
[Roles and permissions](/security/roles-and-permissions/).
If you need a combination of permissions that the built-in roles don't
provide, consider custom roles, which require Docker Business.

#### Enhance with teams

Group members by project, department, or shared repository needs. A member's
role determines organization-wide access, while team permissions apply to
specific repositories. Avoid granting an administrative role solely because
a developer needs access to a project's repositories.

Use [Create and manage a team](/accounts/organization/manage/manage-a-team/)
to apply repository permissions to groups of members. Review team membership
when projects or responsibilities change.

## Onboarding and managing roles and permissions in Docker

### Invite owners

Decide who needs to administer membership, settings, and billing. Additional
owners can share these responsibilities and provide continuity when another
owner is unavailable. Review the permissions before assigning the role.

### Invite members and assign roles

Use your access inventory to assign roles and teams. Follow
[Onboard a Docker organization](/accounts/organization/setup/onboard/)
for initial setup and
[Manage organization members](/accounts/organization/manage/members/)
for invitations and membership changes.

### Choose a provisioning method {#future-proof-user-management}

Decide who will maintain membership as people join, move between teams, or
leave. Manual invitations can suit a small organization. For Docker Business
organizations using an identity provider, compare the
[provisioning methods](/security/provisioning/) before
choosing how to automate membership.

#### Secure user authentication with single sign-on (SSO)

[SSO](/security/authentication/single-sign-on/) authenticates
users through your identity provider. Plan it together with provisioning,
which controls account creation, updates, and removal.

#### Automate onboarding with SCIM and JIT provisioning

Choose a method based on the user lifecycle you need to manage:

- [Just-in-Time (JIT) provisioning](/security/provisioning/just-in-time/)
  creates and updates accounts during SSO sign-in. It doesn't deprovision users,
  so plan how to remove access when users leave.
- [SCIM](/security/provisioning/scim/) synchronizes users
  with your identity provider and supports deprovisioning. If you enable SCIM,
  choose how it will work with JIT so the intended source manages user attributes.

Test adding a user, changing their team, and removing access before relying
on automated provisioning for the whole organization.

#### Simplify access with group mapping

Use [group mapping](/security/provisioning/scim/group-mapping/)
to assign identity provider groups to Docker organizations and teams.
Group mapping works with SAML SSO or SCIM. For Microsoft Entra ID OIDC
connections, use SCIM to synchronize groups. Review the mappings when your
identity provider groups change.

## Monitoring and insights

Schedule access reviews with organization owners and team leads. Compare
membership with your access inventory, remove users who no longer need
access, and adjust roles and teams when responsibilities change.

### Activity logs

Use [activity logs](/accounts/organization/activity-logs/) to review
organization and repository changes, including repository privacy changes
and subscription seat changes. Check who made an unexpected change and when
it happened. Docker Home retains logs for 90 days; plan exports if your audit
process needs a longer history.

### Insights

If your organization meets the subscription and configuration requirements,
use [Insights](/accounts/organization/insights/) to review Docker
Desktop adoption, versions, builds, and container usage. Active user counts
include only users who send analytics. Compare usage with your membership
inventory before deciding whether to change access or subscription seats.

### Next steps

- Review [members](/accounts/organization/manage/members/) and
  [teams](/accounts/organization/manage/manage-a-team/) on a regular schedule.
- Use [rollout planning](/accounts/organization/setup/rollout/)
  before deploying changes to Docker Desktop settings or sign-in requirements.
