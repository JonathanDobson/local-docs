---
sidebar_position: 9
---

# Upgrading

Stop the runner, replace the binary or image, and start it again. The registration file stays valid, so you do not need to register the runner again.

```bash
sudo systemctl stop gitea-runner
sudo install -m 0755 gitea-runner-<version>-linux-amd64 /usr/local/bin/gitea-runner
sudo systemctl start gitea-runner
```

Stopping the runner cancels running jobs unless `runner.shutdown_timeout` gives them time to finish. The runner logs a warning for unknown configuration keys and ignores them. Run `gitea-runner config generate` to list all configuration options.

## Breaking changes in 5.0

- **Git 2.34.1 or later is required** on the runner and in job images that use `builtin:checkout`.
- **`builtin:checkout` works like `actions/checkout`.** It removes untracked and ignored files unless `clean: false` is set. It fails if the triggering tag moved after the workflow started.
- **Configuration values expand `${NAME}`** from the runner's environment. The configuration fails to load if `NAME` is unset. Write `$${NAME}` for a literal `${NAME}`, for example in a shell command in a Kubernetes `pod_template`.
- **Jobs require `runs-on`.** A job without `runs-on` fails, as it does on GitHub. Jobs that call a reusable workflow are exempt.
- **OpenTelemetry metrics follow the semantic conventions**, which changed their names, units and attributes. See [telemetry.md](https://gitea.com/gitea/runner/src/branch/main/docs/telemetry.md#metrics). On `/metrics`, `gitea_runner_client_errors_total` gained a `code` label, and `gitea_runner_job_total` counts jobs stopped by `runner.timeout` as `timeout`.
- **Unprivileged runners drop more workflow options.** Unless `container.privileged` is set, `--log-driver`, `--log-opt`, `--oom-score-adj` and `--oom-kill-disable` are removed from a job's `container.options` with a warning.

Release notes for every version are on the [release page](https://gitea.com/gitea/runner/releases).
