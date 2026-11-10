---
title: "docker offload rm"
source: https://docs.docker.com/reference/cli/docker/offload/rm/
---

# docker offload rm

**Description:** Remove the Docker Offload cloud sandbox

**Usage:** `docker offload rm [OPTIONS]`










## Description

The cloud sandbox is deleted with everything in it, running or paused. Every
machine on the account uses the same sandbox, so `rm` deletes it for all of
them. To keep the sandbox for later, use `docker offload stop` instead.


## Options

| Option | Default | Description |
|--------|---------|-------------|
| `-f`, `--force` |  |  Remove without asking for confirmation |



## Examples

### Remove the sandbox

Asks for confirmation first:

```console
$ docker offload rm
```

### Remove the sandbox without confirmation

```console
$ docker offload rm --force
```
