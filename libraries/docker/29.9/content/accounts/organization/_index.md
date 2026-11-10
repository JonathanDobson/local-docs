---
title: "Organization accounts"
source: https://docs.docker.com/accounts/organization/
---

# Organization accounts


A Docker organization is a shared workspace for members and repositories
under one namespace.
Organization owners administer membership, access, and security.

## Organization structure

Organization owners manage organizations that contain members,
repositories, and teams, which group members within an
organization.

The following diagram shows that hierarchy:

```mermaid {title="Organization structure" caption="Organization owners manage an organization that contains members, repositories, and optional teams."}
flowchart TB
  oo(("Organization owners")) -.->|"manage"| org
  subgraph org["Organization"]
    direction TB
    m(("Members"))
    subgraph t["Teams (optional)"]
      tm(("Members"))
    end
    r[("Repositories")]
  end
  style org fill:#3b82f622,stroke:#3b82f6
  style t stroke-dasharray: 5 5
```

### Owners

Organization owners administer the organization. They invite members, assign
roles, and manage teams and repositories.

An organization can have multiple owners. All owners share the same
predefined permissions. For other roles and their permissions, see
[Roles and permissions](/security/roles-and-permissions/).

### Members

A member is a Docker user invited to the organization. Organization owners
assign a role to each member, and that role sets organization-wide access.

### Teams

Teams are optional. They group members so you can grant repository
access to many people at once. Use a team when several members need the
same repositories. Members can belong to the organization without joining
a team.

For a deployment across your organization, start with
[Plan and roll out Docker](/accounts/organization/setup/rollout/).
For ongoing membership and permissions decisions, use
[Plan and maintain user access](/accounts/organization/manage/user-access/).

## Next steps

Learn how to manage organizations in the following sections.
