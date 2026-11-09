---
sidebar_position: 8
---

# Monitoring

## Metrics

```yaml
metrics:
  enabled: true
  addr: "127.0.0.1:9101"
```

With metrics enabled, the runner serves these endpoints:

| Endpoint | Purpose |
| --- | --- |
| `/metrics` | Prometheus metrics |
| `/healthz` | Liveness, always `200` while the process runs |
| `/readyz` | Readiness, `503` when a [health check](#health-checks) fails, the runner cannot reach Gitea for longer than `metrics.readiness_grace` (`30s`), or the runner is shutting down |

The listener has no authentication. If you expose it beyond localhost, for example with `addr: ":9101"`, protect it with a firewall.

The runner exports these metrics in addition to the standard Go and process metrics:

| Metric | Meaning |
| --- | --- |
| `gitea_runner_state` | `1` for the current `state`: `busy`, `idle` or `unavailable` |
| `gitea_runner_job_running`, `gitea_runner_capacity` | Running jobs and configured capacity |
| `gitea_runner_job_capacity_utilization_ratio` | Running jobs divided by capacity |
| `gitea_runner_job_total` | Finished jobs by `status`: `success`, `failure`, `cancelled`, `skipped`, `timeout` or `unknown` |
| `gitea_runner_job_duration_seconds` | Job duration histogram |
| `gitea_runner_poll_fetch_total` | Job fetches by `result`: `task`, `empty` or `error` |
| `gitea_runner_client_errors_total` | Failed requests to Gitea by `method` and `code` |

Consider alerts for `gitea_runner_state{state="unavailable"}`, a rising `gitea_runner_poll_fetch_total{result="error"}`, and a utilization ratio that stays at `1`, which means jobs may be waiting for a free slot.

## OpenTelemetry

Set `OTEL_EXPORTER_OTLP_ENDPOINT` in the runner's environment to send traces and the metrics above to an OpenTelemetry collector. Each job has a trace with a span for each step:

```sh
OTEL_EXPORTER_OTLP_ENDPOINT=http://localhost:4318
```

Jobs receive `TRACEPARENT`, so instrumented tools can add spans to the job's trace. See [telemetry.md](https://gitea.com/gitea/runner/src/branch/main/docs/telemetry.md) for all variables and security notes.

## Health checks

Health checks stop a runner from accepting new jobs while its machine has a problem, such as a full disk:

```yaml
health_check:
  enabled: true
  min_free_disk_space_mb: 1024
  script: /usr/local/bin/check-runner.sh
```

- The disk check measures free space on the filesystem containing `host.workdir_parent`, or `container.workdir_parent` when `container.bind_workdir` is enabled.
- `script` is optional. The runner becomes unavailable if the script exits with a non-zero status, fails to start, or runs longer than `health_check.timeout` (`10s`). The runner reuses the script's result for `health_check.interval` (`30s`).
- Checks only run while the runner is idle. Running jobs are never interrupted.
- The runner resumes accepting jobs once the checks pass again.

## Logs

The runner writes logs to stderr. View them in the systemd journal or with `docker logs` for a runner container. Set `log.level` to control verbosity, from `trace` to `error`.

The runner streams step output to Gitea without including it in its own log. To also keep a local copy of every job log, set a directory:

```yaml
log:
  job:
    dir: /var/log/gitea-runner
```

The runner writes each job log to `<start time>-task-<id>.log` in this directory and masks secrets. It keeps the files for `log.job.retention` (`168h`). Only the user running the runner can read them.

## Reporting a problem

`gitea-runner bug-report` prints the runner version, Go version, platform and CPU count. Include its output when you open an issue at [gitea/runner](https://gitea.com/gitea/runner/issues).
