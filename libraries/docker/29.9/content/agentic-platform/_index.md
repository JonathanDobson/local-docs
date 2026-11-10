---
title: "Docker Agentic Platform"
source: https://docs.docker.com/agentic-platform/
---

# Docker Agentic Platform


> [!NOTE]
> Docker Agentic Platform is experimental. Features and behavior may change.

Docker Agentic Platform lets you run agents and tools in isolated cloud
sandboxes. Your agent keeps working when you close the Console, disconnect
your computer, or put it to sleep.

The `sbx` CLI supports both
[local sandboxes](/ai/sandboxes/get-started/) and
[cloud sandboxes](/ai/sandboxes/cloud/). These pages describe
the web Console experience. The Console and CLI use different secret names;
see [Cloud credentials](/ai/sandboxes/cloud/credentials/).

In the Console, choose a [kit](/agentic-platform/kits/) and configure
the sandbox's credentials, network access, tools, and compute size. Once it
starts, use its terminal to work with the agent. You can return to running or
paused sandboxes from **Sandboxes**.

You can reuse these settings across sandboxes:

- [MCP](/agentic-platform/mcp/) connects external tools.
- [Secrets](/agentic-platform/secrets/) provide credentials
  without placing their values inside a sandbox.
- [Network policies](/agentic-platform/policies/) control
  which hosts and services a sandbox can reach.

To begin, [activate your subscription](/agentic-platform/signup/#activate-cloud-access), then
[start a sandbox](/agentic-platform/get-started/). You pay for compute by the second while your
sandbox runs. See [Signup and billing](/agentic-platform/signup/) for account and payment
information.
