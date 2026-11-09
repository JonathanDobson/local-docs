---
sidebar_position: 1
---

# Job hooks

Job hooks are scripts you provide. They run in the job environment before its first step and after its last step. Use them for setup that applies to every job, such as registry logins, mirror configuration or masking secrets used by all jobs.

```yaml
runner:
  hooks:
    job_started: /hooks/started.sh
    job_completed: /hooks/completed.sh
```

`job_started` runs before any action is downloaded. `job_completed` runs after the last post step, including when the job fails or is cancelled. If these settings are unset, the runner reads GitHub's `ACTIONS_RUNNER_HOOK_JOB_STARTED` and `ACTIONS_RUNNER_HOOK_JOB_COMPLETED` from `runner.envs` or `runner.env_file`. The runner ignores workflow values for these hook variables.

A hook that exits with a non-zero status fails the job. Hooks block the job while they run and count against its timeout. Keep them fast.

## Where they run

Hooks run inside the job container, or on the host for host jobs. GitHub always runs hooks on the host. The script must exist in the job image or on the host where it runs. Job containers cannot access a path that exists only in the runner container. To make a host directory available to jobs, mount it with `container.options` and allow it in `container.valid_volumes`.

| Extension | Runs as |
| --- | --- |
| `.sh` | `bash -e <path>` |
| `.ps1` | `pwsh -command ". '<path>'"` |
| Anything else | The file itself |

The shell options of `run:` steps do not apply to hooks. Set `pipefail` and other shell options inside the script.

## Environment and output

A hook receives the job's environment, including `runner.envs`, the workflow's `env:` and the `GITHUB_*` variables. The runner includes hook output in the job log and masks secrets as it does for step output.

Use `$GITHUB_ENV` and `$GITHUB_PATH` to pass environment variables and paths to later steps. Mask values with `::add-mask::`:

```bash
#!/bin/bash
token="$(fetch-token)"
echo "::add-mask::$token"
echo "REGISTRY_TOKEN=$token" >> "$GITHUB_ENV"
echo "/opt/tooling/bin" >> "$GITHUB_PATH"
```

For cleanup on the host after the job environment is gone, use the [post-task script](post-task-script.md).
