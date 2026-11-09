---
sidebar_position: 2
---

# Registration

Register a runner once with a Gitea instance to get its identity and credentials.

## Registration token

Gitea issues registration tokens for the whole instance, an organization, a user, or a single repository. A runner accepts jobs within the token's scope. To find a token, see [Gitea Runner](/usage/actions/runner). A token can register any number of runners until it is reset.

## Registering

```bash
gitea-runner register --instance https://gitea.example.com --token <token>
```

The runner asks for its name. It also asks for its [labels](labels.md) unless you set `runner.labels`. To skip the prompts, use `--no-interactive` and pass the values as flags:

```bash
gitea-runner register --no-interactive \
  --instance https://gitea.example.com \
  --token <token> \
  --name my-runner \
  --labels ubuntu-latest:docker://docker.gitea.com/runner-images:ubuntu-latest
```

Set `--instance` to the instance's `ROOT_URL`. `localhost` does not work from job containers.

To keep the token out of shell history and the process list, pass it with `--token-file <path>` or through the `GITEA_RUNNER_REGISTRATION_TOKEN` environment variable.

## The registration file

Registration writes the runner's credentials to `.runner` in the working directory, or to the path in `runner.file`:

- Keep it on persistent storage. If the file is lost, register again as a new runner.
- Give each runner process its own registration file. A second process using the same file refuses to start.
- Treat it as a secret.

## Ephemeral runners

An ephemeral runner accepts exactly one job, then exits. Its credentials are revoked as soon as the job is assigned, so the job cannot use them to accept more work. Start each ephemeral runner in a fresh VM or container when running jobs from repositories you do not fully trust.

```bash
gitea-runner register --ephemeral --instance https://gitea.example.com --token <token>
```

With the Docker images, set `GITEA_RUNNER_EPHEMERAL=1`. To start a runner for each job, listen for Gitea's `workflow_job` [webhook](/usage/repository/webhooks), which fires when a job is queued.

`gitea-runner daemon --once` also exits after one job, but its credentials stay valid.

## Removing a runner

Delete the runner in Gitea's runner settings, then delete its registration file. The runner exits when it detects that Gitea has removed its registration.
