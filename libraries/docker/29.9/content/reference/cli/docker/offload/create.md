---
title: "docker offload create"
source: https://docs.docker.com/reference/cli/docker/offload/create/
---

# docker offload create

**Description:** Create a Docker Offload cloud sandbox

**Usage:** `docker offload create [OPTIONS]`










## Description

Create a Docker Offload cloud sandbox.

This command is available when **Enable Docker Offload** is turned off in
Docker Desktop settings, or doesn't appear. If the setting is on, you'll be asked to 
switch it off before continuing.

If a sandbox already exists for your account, `create` connects to it instead
of creating a second one, and resumes it if it's paused.

A sandbox pauses once it has been idle for its idle timeout, which is 5m
unless you set it: nothing working inside it, and no command, build or pull
in flight. Pausing keeps its containers, and a docker command that needs the
sandbox, such as `run`, `start` or `attach`, resumes it. Attached sessions
are cut off by a pause; reattach with `docker attach`. Exec sessions have to
be started again.

Set the idle timeout with `--idle-timeout`, at least 1m, or turn pausing off
with `--keep-alive`. Either applies at once to a sandbox that's already
running, and is kept for that sandbox on this machine; a new sandbox starts
from 5m. A kept-alive sandbox runs until you stop it, but still pauses if
this machine sleeps past its `--ttl`, and after 24h.

`--cpus`, `--memory` and `--ttl` apply only when a sandbox is created. If a
sandbox is already running, they aren't applied and `create` tells you so.
To resize, create again with `--recreate`, which deletes the sandbox and
everything on it.


## Options

| Option | Default | Description |
|--------|---------|-------------|
| `--cpus` |  |  The number of CPUs for a new sandbox: 1, 2, 4, 8 or 16 |
| `--idle-timeout` |  |  How long the sandbox may be idle before it pauses, as a duration like 30m (default 5m, minimum 1m, 0 is --keep-alive)<br> |
| `--keep-alive` |  |  Never pause the sandbox for being idle |
| `--memory` |  |  Memory for a new sandbox, as a size like 16g |
| `--recreate` |  |  Recreate the sandbox if it is a different size than asked for. Deletes the old sandbox and everything on it.<br> |
| `--timeout` | `15m0s` |  How long to wait for the sandbox to be ready |
| `--ttl` |  |  How long the sandbox keeps running after the daemon stops renewing it, for example if this machine sleeps or goes offline, as a duration like 4h<br> |



## Examples

### Create a sandbox and connect to it

```console
$ docker offload create
```

### Create a sandbox with a chosen size and lifetime

```console
$ docker offload create --cpus 8 --memory 16g --ttl 4h
```

### Change the idle timeout

Applies at once to a sandbox that's already running:

```console
$ docker offload create --idle-timeout 30m
```

### Keep a sandbox awake

The sandbox runs, and bills, until you stop it:

```console
$ docker offload create --keep-alive
```
