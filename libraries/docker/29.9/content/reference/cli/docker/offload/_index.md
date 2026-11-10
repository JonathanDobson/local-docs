---
title: "docker offload"
source: https://docs.docker.com/reference/cli/docker/offload/
---

# docker offload

**Description:** Control Docker Offload from the CLI

**Usage:** `docker offload`










## Description

Control Docker Offload from the CLI.

There are two versions of Docker Offload, and some commands belong to only
one of them.

| Command | Docker Offload | Docker Offload v1 |
| --- | --- | --- |
| `docker offload create` | Yes | No |
| `docker offload rm` | Yes | No |
| `docker offload start` | No | Yes |
| `docker offload stop` | Yes | Yes |
| `docker offload status` | Yes | Yes |
| `docker offload diagnose` | No | Yes |
| `docker offload version` | Yes | Yes |

Running a command that belongs to the other version reports an error telling
you which setting to change. For more information, see [Docker
Offload](/offload/) and [Docker Offload
v1](/offload/v1/).






## Subcommands

| Command | Description |
|---------|-------------|
| [`docker offload create`](https://docs.docker.com/reference/cli/docker/offload/create/) | Create a Docker Offload cloud sandbox |
| [`docker offload diagnose`](https://docs.docker.com/reference/cli/docker/offload/diagnose/) | Print diagnostic information for Docker Offload |
| [`docker offload rm`](https://docs.docker.com/reference/cli/docker/offload/rm/) | Remove the Docker Offload cloud sandbox |
| [`docker offload start`](https://docs.docker.com/reference/cli/docker/offload/start/) | Start a Docker Offload v1 session |
| [`docker offload status`](https://docs.docker.com/reference/cli/docker/offload/status/) | Show the status of the Docker Offload connection |
| [`docker offload stop`](https://docs.docker.com/reference/cli/docker/offload/stop/) | Stop a Docker Offload session |
| [`docker offload version`](https://docs.docker.com/reference/cli/docker/offload/version/) | Prints the version |
