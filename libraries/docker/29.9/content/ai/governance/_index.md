---
title: "AI governance"
source: https://docs.docker.com/ai/governance/
---

# AI governance


Agents in [Docker Sandboxes](/ai/sandboxes/) work on their own. They
install packages, call APIs, and use tools without asking you first.
Governance lets an agent work freely within rules that limit what it can
access. The rules are enforced outside the sandbox, so the agent can't change or
bypass them. They come from three sources: your local policy, the kits your
sandboxes use, and your organization.

> [!NOTE]
> This section covers sandboxes that run on your machine. Cloud sandboxes use
> the same kinds of allow and deny rules, but they don't use local policy or
> organization policy. They use
> [cloud network policy](/ai/sandboxes/cloud/network-policy/), which is stored in your
> Docker account and managed with `sbx --cloud policy` or in the Docker Agentic
> Platform [Console](/agentic-platform/policies/).

## Where the rules come from

You set your local policy and choose which kits your sandboxes use. Your
organization's administrators set its organization policies.

### Local policy and kits

With [local policy](/ai/governance/local/), you decide which network destinations
your sandboxes can reach. You start from a preset, then use `sbx policy` to
allow what your work needs and block what sandboxes shouldn't reach.

[Kits](/ai/sandboxes/customize/use-kits/), including the built-in agent kits,
bring rules of their own. Whoever authors a kit defines the rules its agent
needs, such as access to the agent's API, and the rules come with the kit
whether you build it yourself or pull it from a registry or Git repository.
They apply only to the sandboxes that use the kit.

### Organization governance

If your organization has an
[AI Governance plan](/subscription-billing/plans/ai-governance/),
administrators set rules centrally with
[organization governance](/ai/governance/organization/). Their policies apply to the
sandboxes of licensed members and go beyond the network, controlling which
host paths sandboxes can mount and which MCP servers they can use.
Administrators then review the decisions those policies make in audit logs.

## Get started

If you're a developer, start with
[Try out local policy](/ai/governance/local/try-it-out/), an example that allows and blocks
destinations for one sandbox.

If you're an administrator, start with
[Get started with organization governance](/ai/governance/organization/get-started/) to set
up policies, audit logs, licenses, sign-in enforcement, and Docker Sandboxes
for your organization.
