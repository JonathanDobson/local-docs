---
title: "docker offload stop"
source: https://docs.docker.com/reference/cli/docker/offload/stop/
---

# docker offload stop

**Description:** Stop a Docker Offload session

**Usage:** `docker offload stop [OPTIONS]`










## Description

Stop a Docker Offload session.

What stopping does, and which options apply, depends on which version of
Docker Offload your commands use. That's set by **Enable Docker Offload** in
Docker Desktop settings.

When the setting is off, or doesn't appear, you use the current version of
Docker Offload. Stopping pauses the sandbox and the next `docker offload
create` resumes it. Every machine on the account uses the same sandbox, so a
stop pauses it for all of them. To delete the sandbox instead, use `docker
offload rm`. The `--terminate` option isn't available.

When the setting is on, you use Docker Offload v1. Stopping ends the session,
and the cloud environment and everything in it is removed.


## Options

| Option | Default | Description |
|--------|---------|-------------|
| `--terminate` |  |  Terminate the remote lease. Docker Offload v1 only |
