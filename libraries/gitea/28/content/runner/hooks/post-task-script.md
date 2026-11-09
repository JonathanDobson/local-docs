---
sidebar_position: 2
---

# Post-task script

The post-task script runs on the runner's host after each job, once the runner has removed the job's containers. Use it for housekeeping such as pruning Docker images or freeing disk space.

```yaml
runner:
  post_task_script: /usr/local/bin/gitea-post-task.sh
  post_task_script_timeout: 2m
```

```sh
#!/bin/sh
docker image prune -f
docker builder prune -f --filter 'until=24h'
```

The job's slot stays busy until the script exits. With `capacity: 1`, the runner accepts no new jobs while the script runs. The runner kills the script if it runs longer than `post_task_script_timeout`, which defaults to `5m`. The runner also waits for the script during shutdown.

The runner writes the script's output to its own log, not to the job log. If the script exits with a non-zero status, the runner logs a warning without changing the job's result.

## Environment

The script receives variables from `runner.envs` and `runner.env_file`, but not from the runner's own environment. Set `PATH` in one of these settings if the script needs it. The runner also sets these variables:

| Variable | Value |
| --- | --- |
| `GITEA_TASK_ID` | The task ID |
| `GITEA_RUN_ID` | The workflow run ID |
| `GITEA_REPOSITORY` | The repository as `owner/name` |
| `GITEA_WORKSPACE` | The job's workspace path, which may already be deleted |
| `GITEA_JOB_RESULT` | `success`, `failure`, `cancelled`, `skipped` or `unknown` |

## Windows

The configured path must be an `.exe`, `.bat` or `.cmd` file. Wrap a PowerShell script in a batch file:

```bat
@echo off
powershell.exe -NoProfile -NonInteractive -ExecutionPolicy Bypass -File "%~dp0post-task.ps1"
```

For work inside the job environment, use [job hooks](job-hooks.md).
