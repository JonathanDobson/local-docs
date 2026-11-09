---
sidebar_position: 1
slug: /
---

# Gitea Runner

[Gitea Runner](https://gitea.com/gitea/runner) runs [Gitea Actions](/usage/actions/overview) jobs.
It asks a Gitea instance for jobs, runs them, and sends their logs and results back.

:::info
These pages describe the runner `5.x` series. Select another release, or the development version, in the **Runner Version** dropdown.
:::

## Requirements

- Gitea 1.21 or later with [Actions enabled](/administration/config-cheat-sheet#actions-actions), the default setting.
- Git 2.34.1 or later on the runner's `PATH`.
- Docker, or Podman with `podman.socket` enabled, for jobs in containers, Docker actions, and `docker://` steps.

Jobs need these tools wherever steps run, in the job image or on the host:

- `bash` or `sh` for `run` steps, or `pwsh` or `powershell` on Windows.
- `node` for JavaScript actions and `hashFiles()`.
- `git` 2.34.1 or later for [`builtin:checkout`](jobs.md#built-in-checkout), plus `git-lfs` for its `lfs` input and `ssh` for its `ssh-key` input.

## Where jobs run

The runner's [labels](labels.md) determine where each job runs. One runner can use a mix of these environments:

| Label | Where the job runs |
| --- | --- |
| `docker://<image>` | In a container |
| `kubernetes://<image>` | In a pod in a Kubernetes cluster |
| `host` | Directly on the runner's machine |

Host jobs run as the runner's user without isolation. Use them only for trusted repositories.

## Getting started

1. Install the runner [from a binary](installation/binary.md), [with Docker](installation/docker.md), or [on Kubernetes](installation/kubernetes.md).
2. [Register it](registration.md) with your Gitea instance.
3. Start it with `gitea-runner daemon`.

The runner works without a configuration file. [Configuration](configuration.md) explains when you need one.

The runner is released independently of Gitea. Read [Upgrading](upgrade.md) before moving to a new major version.
