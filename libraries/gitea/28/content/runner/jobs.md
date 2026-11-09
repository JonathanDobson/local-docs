---
sidebar_position: 5
---

# Jobs

## Service containers

A job's `services` start before its steps. If a service defines a health check in its image or `options`, the runner waits until the service is healthy:

```yaml
services:
  postgres:
    image: postgres:18
    options: >-
      --health-cmd pg_isready
      --health-interval 5s
      --health-retries 10
```

If a service is unhealthy, the runner fails the job and shows the service's container log. If a service never becomes healthy, the runner fails the job after `container.service_ready_timeout`, which defaults to `5m`.

Connect to a service from a step using its ID and listening port, for example `psql -h postgres -p 5432`.

A job with a `host` label does not start services. Set `container:` on the job if it needs services.

## Docker inside jobs

Container jobs can access the runner's Docker daemon, usually through a proxy. Containers started by the job can bind-mount the workspace using its path:

```bash
docker run -v "$PWD:/src" alpine ls /src
```

When the job ends, the proxy removes the containers, networks and volumes the job created, including `docker compose` services. Set `container.sweep: false` when jobs deploy services that should keep running.

Without the proxy, for example with a remote `DOCKER_HOST`, prefix workspace bind mounts with `GITEA_DOCKER_WORKSPACE`. This variable contains the workspace path as the Docker daemon sees it:

```yaml
volumes:
  - ${GITEA_DOCKER_WORKSPACE:-.}/data:/app/data
```

To keep the Docker socket out of job containers, set `container.docker_host: "-"`.

## Volumes and privileges

Workflows can mount only the volumes and host paths allowed by `container.valid_volumes`. The list is empty by default:

```yaml
container:
  valid_volumes:
    - data             # the volume named data
    - /src/*.json      # * stays within one path segment, ** crosses them
    - /etc/ssl/certs:ro  # read-only mounts only
```

Unless you enable `container.privileged`, the runner drops options in a workflow's `container.options` that could allow the job to escape the container. Examples include `--privileged`, `--cap-add`, `--device` and `--security-opt`. The runner writes a warning in the job log when it drops an option. The runner's own `container.options` always apply.

## Tool cache

Setup actions such as `actions/setup-go` install tools in `/opt/hostedtoolcache`. `runner.tool_cache_mode` determines how the runner stores this cache:

| Mode | Tool cache |
| --- | --- |
| `none` (default) | Tools included in the job image. Tools installed by a job are removed when it ends. |
| `shared` | One volume reused by every job. Use only with `runner.capacity: 1`. Two jobs installing the same tool version at once corrupt the cache. |

With `none`, include tools in the job image at `/opt/hostedtoolcache/<tool>/<version>/<arch>`. Place an empty `<arch>.complete` file next to the directory. The `-full` variant of the [runner images](https://gitea.com/gitea/runner-images) includes its tools this way.

## Built-in checkout

`uses: builtin:checkout` checks out the repository like `actions/checkout`. It does not download an action or require Node in the job image. It runs `git` in the job. See [Requirements](index.md#requirements) and the inputs listed in [builtin-actions.md](https://gitea.com/gitea/runner/src/branch/main/docs/builtin-actions.md).

## Secrets

The runner masks secrets and `::add-mask::` values in job logs, job summaries, and the names of containers it creates. The runner does not send job outputs that contain a secret. A `needs.<job>.outputs.<name>` expression that reads such an output is empty.
