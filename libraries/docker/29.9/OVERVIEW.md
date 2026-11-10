# Docker documentation (Engine 29.9) — overview

The official documentation from **docs.docker.com**, captured on 2026-11-10. The
site isn't versioned, so this is a snapshot: it describes **Docker Engine 29.9**
(newest release 29.9.3), Docker CLI 29.9.2, Engine API v1.56, Compose 5.7.0,
Buildx 0.38.2 and BuildKit 0.34.2, plus Docker Desktop, Docker Hub, Scout,
Docker Hardened Images and Docker's AI tools as they stood that day. Each page is
the Markdown the site itself publishes (`<page>.md`), so includes, tabs and the
generated CLI reference read exactly as on the website. API references come from
the OpenAPI specs in the docker/docs repo.

## Layout

Folders mirror the site's URLs (`content/engine/install/ubuntu.md` is
`https://docs.docker.com/engine/install/ubuntu/`); every page's front matter has
its `source:` URL. A page with sub-pages is `<folder>/_index.md`.

| Folder | What it holds |
|---|---|
| `content/get-started/` | Concepts (images, containers, registries, Compose), workshop, tutorials |
| `content/guides/` | Language and use-case guides (Python, Go, Node, databases, CI…) |
| `content/engine/` | Docker Engine: install per distro, daemon config, networking, storage and volumes, logging, security (rootless, userns), Swarm, `deprecated.md`, release notes |
| `content/build/` | Docker Build: BuildKit, builders and drivers, cache, exporters, Bake, multi-platform, CI, attestations, build checks |
| `content/compose/` | Docker Compose: install, how-tos (profiles, env vars, networking, GPUs…), Compose SDK, release notes |
| `content/desktop/` | Docker Desktop: install, settings, features, enterprise deployment, troubleshooting, release notes |
| `content/docker-hub/`, `content/scout/`, `content/dhi/`, `content/build-cloud/`, `content/offload/` | Docker Hub, Docker Scout, Docker Hardened Images, Build Cloud, Offload |
| `content/ai/` | Model Runner, MCP Catalog and Toolkit, Docker Agent, Gordon, Sandboxes, AI governance |
| `content/security/`, `content/accounts/`, `content/subscription-billing/` | Org security (SSO, SCIM), accounts, billing |
| `content/reference/cli/docker/` | **CLI reference**: one page per command (`container/run.md` = `docker container run`); also `dockerd.md` and the `sbx` CLI |
| `content/reference/dockerfile.md` | **Dockerfile reference** (every instruction); build-check rules in `reference/build-checks/` |
| `content/reference/compose-file/` | **Compose file reference**: `services.md`, `networks.md`, `volumes.md`, `build.md`, `deploy.md`, `develop.md`, `interpolation.md`, `merge.md`, `include.md`, `profiles.md`, `secrets.md`, `configs.md`, `models.md` |
| `content/reference/api/` | API landing pages: Engine SDKs and version history, Hub/DVP changelogs, registry auth, Extensions SDK |
| `api/` | OpenAPI specs (unchanged) and generated pages: `engine-v1.56/` (Engine API), `hub/`, `dvp/`, `registry/`, `ai-governance/`, `ai-governance-audit-logs/`, `sandboxes/` |
| `*/release-notes/` | Release notes: Engine (`engine/release-notes/29.md` …), Desktop, Compose, Build, Hub, Scout, DHI, and `platform-release-notes/` |

## Where to look for…

- **Install Docker Engine on Linux** — `engine/install/<distro>.md` (`ubuntu.md`, `debian.md`, `fedora.md`, …); post-install steps in `engine/install/linux-postinstall.md`.
- **Daemon configuration (`daemon.json`)** — `engine/daemon/` and the `dockerd` reference `reference/cli/dockerd.md`.
- **A CLI command's flags** — `reference/cli/docker/<group>/<command>.md`, e.g. `container/run.md`, `image/build.md` → `buildx/build.md`, `compose/up.md`.
- **Dockerfile instructions** — `reference/dockerfile.md`; best practices in `build/building/best-practices.md`.
- **Compose file keys** — `reference/compose-file/services.md` and siblings.
- **Networking (bridge, host, overlay, port publishing, firewalls)** — `engine/network/`.
- **Volumes, bind mounts, storage drivers, containerd image store** — `engine/storage/`.
- **Logging drivers** — `engine/logging/`.
- **Rootless mode and security** — `engine/security/`.
- **Multi-platform builds, cache, Bake** — `build/building/multi-platform.md`, `build/cache/`, `build/bake/`.
- **Engine REST API** — `api/engine-v1.56/endpoints/<tag>.md` (container, image, network, volume, exec, system, swarm…) and `api/engine-v1.56/schemas.md`; changes by API version in `reference/api/engine/version-history.md`.
- **Docker Hub API (repositories, tags, access tokens, org members, SCIM)** — `api/hub/`.
- **What's deprecated** — `engine/deprecated.md`.
- **What changed in a release** — `engine/release-notes/29.md` (newest first), `desktop/release-notes/_index.md`, `compose/release-notes/_index.md`.

## Version notes (from `engine/release-notes/29.md`)

- **29.0.0** (breaking): the daemon requires API version v1.44 or later (Docker 25.0+); the Go module `github.com/docker/docker` is deprecated in favour of `github.com/moby/moby/client` and `github.com/moby/moby/api`, and releases are tagged `docker-v29.x.y`; Docker Content Trust was removed from the CLI; cgroup v1 is deprecated (supported until at least May 2029); the **containerd image store is the default for fresh installs** (not with `userns-remap`).
- **29.9.0**: the `lazy-pull` daemon feature for the containerd image store; BuildKit v0.34.0; containerd v2.4.1 in the static binaries; Go 1.26.9 with HTTP/2 security fixes.
- **29.9.1 – 29.9.3**: security and bug-fix releases; read the top of `29.md`.
- Compose is v5: `compose/release-notes/_index.md` has every v5 release (from GitHub) up to 5.7.0, the version the CLI reference documents.

## Search tips

- Commands have long and short forms: `docker run` is documented at `docker container run`, `docker build` at `docker buildx build`, `docker ps` at `docker container ls`.
- The daemon's config file is `daemon.json` (`/etc/docker/daemon.json` on Linux); daemon flags are under `dockerd`.
- "Compose file" pages describe `compose.yaml`; "Compose" CLI pages are under `reference/cli/docker/compose/`.
- Callouts appear as `> [!NOTE]`, `> [!WARNING]`, `> [!IMPORTANT]`.
- Engine API paths in the generated pages start with `/v1.56/`.
