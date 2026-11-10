---
title: "Company accounts"
source: https://docs.docker.com/accounts/company/
---

# Company accounts




A company is where you configure sign-in and administration for multiple
Docker organizations.

> [!TIP]
>
> Organization owners with a Docker Business subscription can
> [create a company](/accounts/company/new-company/) in
> [Docker Home](https://app.docker.com/).

## Company structure

A company sits above its organizations, giving company owners full
administrative access across every organization in the company.

The following diagram shows that hierarchy:

```mermaid {title="Company structure" caption="Company owners manage a company that contains one or more organizations."}
flowchart TB
  co(("Company owners")) -.->|"manage"| C
  subgraph C["Company"]
    direction TB
    subgraph O1["Organization A"]
      direction TB
      m1(("Members"))
      r1[("Repositories")]
    end
    subgraph O2["Organization B"]
      direction TB
      m2(("Members"))
      r2[("Repositories")]
    end
    O1 ~~~ O2
  end
  style C fill:#3b82f622,stroke:#3b82f6
```

## What a company lets you do

When you create a company, you can:

- Administer every organization in the company from one place.
- Configure single sign-on (SSO) and System for Cross-domain Identity
  Management (SCIM) once for every organization in the company.
- Verify your domains once at the company level instead of in each
  organization. When you turn on auto-provisioning for a domain, you
  choose which organization new users join.
- View members and invitations from every organization in one list, and
  export that list as a CSV.

You can assign up to 10 company owners. Company owners occupy a purchased
seat only when they are also members of an organization. A company owner
who is not an organization member does not occupy a seat.

## Next steps

Learn how to create and manage a company in the following sections.
