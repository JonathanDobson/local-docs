---
sidebar_position: 3
---

# Configuration

The runner works without a configuration file. Create one to change a default:

```bash
gitea-runner config init
gitea-runner config set runner.capacity 4
gitea-runner -c config.yaml daemon
```

`config init` writes a minimal `config.yaml` in the working directory. Pass the file with `-c` when running `register`, `daemon` or `cache-server`. These commands do not find configuration files automatically. The runner reads its configuration only at startup. Restart it after each change.

## Editing

The `config` command edits the configuration file in place and preserves its comments:

```bash
gitea-runner config set runner.timeout 90m
gitea-runner config set runner.envs.MY_VAR value
gitea-runner config add container.valid_volumes '/data/**'
gitea-runner config remove container.valid_volumes '/data/**'
gitea-runner config get runner.capacity
```

A key is the path to a YAML value, with dots between levels. The command rejects unknown keys and values of the wrong type before changing the file. Without `-c`, these commands look for `config.yaml` or `config.yml` in the working directory, then in the directory containing the binary.

`gitea-runner config generate` prints every option with its default and a description. This matches the [example configuration](reference/config-example.md).

Use `${NAME}` in a value to read an environment variable from the runner's environment. The configuration fails to load if `NAME` is unset. Use `$${NAME}` for a literal `${NAME}`:

```yaml
runner:
  capacity: ${RUNNER_CAPACITY}
```

## Common options

| Option | Default | Description |
| --- | --- | --- |
| `runner.capacity` | `1` | Maximum number of jobs that can run at once. |
| `runner.timeout` | `3h` | Maximum job duration. Gitea's own job timeout may stop a job earlier. |
| `runner.shutdown_timeout` | `0s` | Time to let running jobs finish before canceling them during shutdown. |
| `runner.envs` | | Environment variables for every job. |
| `runner.env_file` | | File containing additional environment variables for every job. |
| `runner.labels` | | See [Labels](labels.md). |
| `runner.insecure` | `false` | Skip verification of Gitea's TLS certificate. |
| `runner.client_cert_file`, `runner.client_key_file` | | Client certificate and key for a Gitea instance that requires mutual TLS. |
| `runner.extra_headers` | | HTTP headers for requests to Gitea, for example for a reverse proxy. |
| `runner.github_mirror` | | URL to use instead of `https://github.com` when downloading actions from GitHub. |
| `container.network` | | Docker network for job containers. If empty, the runner creates a network for each job. |
| `container.options` | | Additional `docker run` options for every job container. |
| `container.privileged` | `false` | Run job containers in privileged mode. See [Jobs](jobs.md#volumes-and-privileges). |
| `container.valid_volumes` | | Volumes and host paths that workflows may mount. |
| `container.force_pull` | `false` | Pull job images even when they are already present. |
| `log.level` | `info` | Verbosity of the runner's log. |

See [Caching](cache.md), [hooks](hooks/job-hooks.md) and [monitoring](monitoring.md) for their configuration options.
