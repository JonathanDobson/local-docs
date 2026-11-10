---
title: "Docker Sandboxes API and SDK"
source: https://docs.docker.com/ai/sandboxes-api/
---

# Docker Sandboxes API and SDK


Use the Docker Sandboxes API to create cloud sandboxes, run commands, and
transfer files from your applications and automated workflows. You can also
manage related resources, including images, snapshots, volumes, and secrets.

To try it, [run your first cloud sandbox](/ai/sandboxes-api/get-started/) with the TypeScript
SDK. The tutorial uses a bundled kit that supplies a shell environment for
running commands.

## Activate cloud access

To use the API or SDK, [activate a Docker Agentic Platform subscription](/agentic-platform/signup/#activate-cloud-access).
Use the same Docker account to [authenticate your application](/ai/sandboxes-api/authentication/).

Cloud compute is billed separately from your Docker subscription. See
[Billing](/agentic-platform/signup/#billing) for details.

## Choose an interface

Use the TypeScript SDK in your JavaScript or TypeScript application. The SDK
provides typed requests and responses, waits for sandboxes to start or stop,
and handles file transfers and interactive processes.
See [Install the SDK](/ai/sandboxes-api/install/) for installation instructions.

You can also call the REST API directly from any language or HTTP tool.
See the [API reference](/reference/api/sandboxes/latest/) for operations,
request fields, responses, and the downloadable OpenAPI specification.

To run agents from your terminal, see [Docker Sandboxes](/ai/sandboxes/).

## Develop your application

- [SDK cookbook](/ai/sandboxes-api/cookbook/): follow examples for processes, files,
  storage, networking, and other sandbox operations.
- [API concepts](/ai/sandboxes-api/concepts/): choose a kit or image, identify resources, and
  wait for actions to finish.
- [Authentication and authorization](/ai/sandboxes-api/authentication/): authenticate requests
  and understand which permissions your application needs.
- [Errors and retries](/ai/sandboxes-api/errors/): handle failures and retry requests without
  duplicating work.
- [Compute sizes and limits](/ai/sandboxes-api/limits/): choose resources and handle account
  quotas and request rate limits.
