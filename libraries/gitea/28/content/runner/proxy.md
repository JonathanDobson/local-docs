---
sidebar_position: 7
---

# Proxies

Set proxy variables in the runner's environment. Use `Environment=` in a systemd unit, `docker run -e`, or `env:` in Kubernetes:

```sh
http_proxy=http://proxy.example:3128
https_proxy=http://proxy.example:3128
no_proxy=gitea.internal,.example.local
```

The runner uses these variables for its own requests. It passes them to every job and service container in lowercase and uppercase. Dockerfile actions receive them as build arguments.

The runner adds the following to `no_proxy` so jobs reach them directly:

- The runner's cache server
- `localhost`, `127.0.0.1` and `::1`
- The job's service containers
- The Docker daemon, when reached over `tcp://`

Add Gitea to `no_proxy` if jobs should reach it directly. The runner does not add it automatically.

## Changing the proxy for jobs

| Scope | Where to set it |
| --- | --- |
| One step | Set the step's `env:`. |
| The rest of a job | Write lowercase and uppercase variable names to `$GITHUB_ENV`. |
| Every job | Set `runner.envs`. Values in `no_proxy` are added to the list above. |

Proxy values set at the workflow or job level, or in `container.env`, cannot replace the runner's proxy values.

## Docker daemon

The Docker daemon pulls images and needs its own proxy settings. See [the Docker documentation](https://docs.docker.com/engine/daemon/proxy/). The Docker daemon bundled with the `dind` images reads the runner's proxy variables. The runner warns at startup if it has a proxy but the Docker daemon does not.

## Credentials

The runner masks passwords in proxy URLs in job logs, but every step can read them from its environment. Prefer a proxy that authenticates by source address.
