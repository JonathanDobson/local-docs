---
title: "docker offload start"
source: https://docs.docker.com/reference/cli/docker/offload/start/
---

# docker offload start

**Description:** Start a Docker Offload v1 session

**Usage:** `docker offload start`










## Description

Start a Docker Offload v1 session.

This command belongs to Docker Offload v1, and works when **Enable Docker
Offload** is turned on in Docker Desktop settings. If the setting is off, or
doesn't appear, your Docker commands use the current version of Docker
Offload, which uses `docker offload create` instead.


## Options

| Option | Default | Description |
|--------|---------|-------------|
| `-a`, `--account` |  |  The Docker account to use |
| `--timeout` | `10s` |  How long to wait for the engine to be ready |
