---
sidebar_position: 4
---

# Labels

A runner's labels determine which jobs it accepts and where it runs them. Gitea sends a job to a runner that has the labels specified in the job's `runs-on`. The runner uses the environment of the first matching entry in `runs-on`.

| Label | Job environment |
| --- | --- |
| `ubuntu-latest:docker://docker.gitea.com/runner-images:ubuntu-latest` | Container using the specified image. |
| `ubuntu-latest:kubernetes://docker.gitea.com/runner-images:ubuntu-latest` | Pod using the specified image. See [job pods](installation/kubernetes.md#job-pods). |
| `macos:host`, or just `macos` | The runner's machine. |

The label name is the part before the first `:docker`, `:kubernetes` or `:host`. Workflows use this name in `runs-on`. For example:

```text
ubuntu-latest:docker://docker.gitea.com/runner-images:ubuntu-latest,macos:host
```

With these labels, `runs-on: ubuntu-latest` jobs run in a container. Jobs with `runs-on: macos` run on the runner's machine.

A job's `container:` image replaces the label's image. The job runs in a container even with a `host` label.

A job whose `runs-on` matches none of the runner's labels uses `runner.default_image`, which defaults to `docker.gitea.com/runner-images:ubuntu-latest`. It runs in a container, as a pod on runners with `kubernetes` but no `docker` labels, or on the host when no Docker daemon is reachable.

## Changing labels

Labels are set during registration and stored in the registration file. To change them, set them in the configuration file or on the command line, then restart the runner. The runner reports its labels to Gitea at startup:

```bash
gitea-runner config set runner.labels 'ubuntu-latest:docker://node:24' 'macos:host'
```

`daemon --labels` or the `GITEA_RUNNER_LABELS` environment variable takes precedence over `runner.labels`. The `runner.labels` setting takes precedence over labels in the registration file.

## Choosing images

- Use the [runner images](https://gitea.com/gitea/runner-images) for tools that common workflows need. To avoid installing a toolchain on every run, choose an image that already includes it.
- Pin images by tag or digest for reproducible jobs.
- Give host labels distinct names such as `macos-arm64` to prevent workflows written for GitHub's `ubuntu-latest` from running directly on your machine without a sandbox.
