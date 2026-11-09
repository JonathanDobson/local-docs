---
sidebar_position: 2
---

# Install with Docker

Runner images are available on [Docker Hub](https://hub.docker.com/r/gitea/runner/tags) as `docker.io/gitea/runner`. On its first start, the container registers and starts the runner:

```bash
docker run -d --name gitea-runner --restart always --privileged \
  -e GITEA_INSTANCE_URL=https://gitea.example.com \
  -e GITEA_RUNNER_REGISTRATION_TOKEN=<token> \
  -v ./data:/data \
  -v runner-docker:/var/lib/docker \
  docker.io/gitea/runner:5-dind
```

The `-dind` image runs its own Docker daemon for jobs. Jobs never get access to the host's Docker daemon socket, which grants the equivalent of root access on the host. The two volumes preserve registration and job images when you replace the container:

- `/data` holds the `.runner` registration file. Without it, a new container registers as another runner.
- `/var/lib/docker` holds the images pulled for jobs. Without it, a new container pulls them again.

## Image flavours

| Tag | Docker daemon for jobs |
| --- | --- |
| `5-dind` (recommended) | Bundled. Requires `--privileged`. |
| `5-dind-rootless` | Bundled. Runs as UID 1000. Requires `--privileged` and [rootless Docker](https://docs.docker.com/engine/security/rootless/) support on the host. Stores its images in `/home/rootless/.local/share/docker`. |
| `5` | None. Mount the host's Docker daemon socket with `-v /var/run/docker.sock:/var/run/docker.sock`, or set `DOCKER_HOST`. |

The `5` tags follow the newest `5.x` release. The `latest` and exact version tags such as `5.2.0` use the same suffixes. The `-dind` flavours are available for amd64 and arm64. The basic image also supports riscv64 and s390x. The images are designed for Docker, not Podman.

When the basic image uses the host's Docker daemon, jobs share that daemon. Use this setup only for trusted repositories.

## Environment variables

| Variable | Meaning |
| --- | --- |
| `GITEA_INSTANCE_URL` | Gitea instance to register with. |
| `GITEA_RUNNER_REGISTRATION_TOKEN` | Registration token, needed only until registration completes. |
| `GITEA_RUNNER_REGISTRATION_TOKEN_FILE` | File to read the registration token from, such as a Docker secret. |
| `GITEA_RUNNER_NAME` | Runner name. Defaults to the container's hostname. |
| `GITEA_RUNNER_LABELS` | Comma-separated [labels](../labels.md), applied on every start. |
| `GITEA_RUNNER_EPHEMERAL` | Any nonempty value registers an [ephemeral runner](../registration.md#ephemeral-runners). |
| `GITEA_RUNNER_ONCE` | Any nonempty value makes the runner exit after one job. |
| `GITEA_MAX_REG_ATTEMPTS` | Maximum number of registration attempts. Unlimited by default, with 5 seconds between attempts. |
| `CONFIG_FILE` | Path to a [configuration file](../configuration.md) inside the container. |

To use a configuration file, mount it and set `CONFIG_FILE` to its path:

```bash
docker run ... -v ./config.yaml:/config.yaml -e CONFIG_FILE=/config.yaml docker.io/gitea/runner:5-dind
```

## Docker Compose

```yaml
services:
  runner:
    image: docker.io/gitea/runner:5-dind
    restart: always
    privileged: true
    environment:
      GITEA_INSTANCE_URL: https://gitea.example.com
      GITEA_RUNNER_REGISTRATION_TOKEN: <token>
    volumes:
      - ./data:/data
      - runner-docker:/var/lib/docker

volumes:
  runner-docker:
```

The rootless flavour needs these additional settings:

```yaml
services:
  runner:
    image: docker.io/gitea/runner:5-dind-rootless
    restart: always
    privileged: true
    security_opt:
      - apparmor=rootlesskit
    environment:
      GITEA_INSTANCE_URL: https://gitea.example.com
      GITEA_RUNNER_REGISTRATION_TOKEN: <token>
      DOCKERD_ROOTLESS_ROOTLESSKIT_NET: slirp4netns
      DOCKERD_ROOTLESS_ROOTLESSKIT_MTU: 65520
    volumes:
      - runner-data:/data

volumes:
  runner-data:
```

- Set `security_opt` on AppArmor hosts such as Ubuntu and Debian. Docker's `docker-ce-rootless-extras` package provides the `rootlesskit` profile.
- Use `slirp4netns` for better job network throughput than the default.
- Make `/data` writable by UID 1000. Use a named volume or a bind-mounted host directory owned by that UID.

See the runner repository's [examples](https://gitea.com/gitea/runner/src/branch/main/examples) for more deployments.
