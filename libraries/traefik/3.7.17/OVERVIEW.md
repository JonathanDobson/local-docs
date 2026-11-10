# Traefik Proxy 3.7.17 — overview

Traefik Proxy is an open-source reverse proxy and load balancer that discovers
services from Docker, Swarm, Kubernetes, files, key-value stores and other
"providers", and routes HTTP, TCP and UDP traffic to them. This set is the
official documentation at release tag **v3.7.17** (newest stable on 2026-11-10),
taken from `docs/content` in github.com/traefik/traefik, plus the v3.7.x
changelog.

## Layout

| Folder | What it holds |
|---|---|
| `content/getting-started/` | Concepts, quick starts for Docker and Kubernetes, configuration introduction, FAQ |
| `content/setup/` | Installing Traefik on Docker, Swarm, Kubernetes |
| `content/expose/` | Exposing services on Docker, Swarm and Kubernetes (basic and advanced) |
| `content/secure/`, `content/security/` | Securing APIs (JWT, OIDC, WAF — Hub features) and hardening notes (request path, header aliases, content length) |
| `content/observe/` | Logs and access logs, metrics, tracing — task guides |
| `content/reference/install-configuration/` | **Install (static) configuration**: entry points, providers, TLS certificate resolvers (ACME), API and dashboard, observability, and `configuration-options.md` — every option in one table |
| `content/reference/routing-configuration/` | **Routing (dynamic) configuration**: HTTP/TCP/UDP routers, rules and priority, services and load balancing, middlewares, TLS; Kubernetes CRD, Gateway API and Ingress; Docker labels and other providers |
| `content/reference/dynamic-configuration/` | Raw files: full Docker label list, file-provider TOML/YAML, Kubernetes CRD definitions and RBAC |
| `content/reference/static-configuration/` | Full static configuration examples (`file.toml`, `file.yaml`) |
| `content/migrate/` | Upgrade notes: `v3.md` (per-release changes within v3), `v2-to-v3.md` and details, `v1-to-v2.md`, NGINX → Traefik |
| `content/user-guides/` | Docker Compose recipes: basic example and ACME HTTP, TLS and DNS challenges |
| `content/deprecation/`, `content/release-notes/` | Deprecation notices; `CHANGELOG-v3.7.md` |

## Where to look for…

- **Static vs dynamic configuration** — `getting-started/configuration-overview.md` ("install configuration" vs "routing configuration").
- **Any install option, its default, CLI flag or env var** — `reference/install-configuration/configuration-options.md`.
- **Entry points (ports, HTTP→HTTPS redirect)** — `reference/install-configuration/entrypoints.md`.
- **Docker labels** — `reference/routing-configuration/other-providers/docker.md`; full list in `reference/dynamic-configuration/docker-labels.yml`; provider options in `reference/install-configuration/providers/docker.md`.
- **Router rules (`Host`, `PathPrefix`, `HostSNI`…) and priority** — `reference/routing-configuration/http/routing/rules-and-priority.md`.
- **A specific middleware** — `reference/routing-configuration/http/middlewares/<name>.md` (TCP: `.../tcp/middlewares/`).
- **Let's Encrypt / ACME** — `reference/install-configuration/tls/certificate-resolvers/`; Compose recipes in `user-guides/docker-compose/acme-*`.
- **Kubernetes** — providers in `reference/install-configuration/providers/kubernetes/` (CRD, Gateway API, Ingress, Ingress NGINX, Knative); routing in `reference/routing-configuration/kubernetes/`.
- **Dashboard and API** — `reference/install-configuration/api-dashboard.md`.
- **Metrics, tracing, access logs** — `reference/install-configuration/observability/` and `observe/`.
- **Upgrading** — `migrate/v3.md` (newest first) and `migrate/v2-to-v3.md`.
- **What changed in a patch release** — `release-notes/CHANGELOG-v3.7.md`.

## Version notes (from `migrate/v3.md` and the changelog)

- **v3.7.0**: `Host` and `HostSNI` matchers accept a single-level wildcard (`*.example.com`); the Kubernetes Gateway API provider supports Gateway API v1.5.1 (update the CRDs) and `TLSRoute` no longer needs `experimentalChannel`; the Ingress NGINX provider supports the `nginx.ingress.kubernetes.io/custom-headers` annotation and needs the `configmaps` RBAC right; the CRD provider needs updated CRDs for new `retry` options and `ingressClassName`.
- **v3.7.1** onward: Kubernetes providers' `crossProviderNamespaces`.
- Later 3.7.x patches add behaviour notes (CONNECT requests, h2c upgrades, GODEBUG TLS settings, header value limits, generated names in the Ingress NGINX provider); read `migrate/v3.md` from the top.
- Traefik **Hub** (commercial) features are documented alongside OSS ones and marked "Traefik Hub Feature" — they don't work in Traefik Proxy.

## Search tips

- Traefik's own words: **install configuration** (formerly "static") and **routing configuration** (formerly "dynamic"); **entry points**, **routers**, **services**, **middlewares**, **providers**, **certificate resolvers**.
- The config file is `traefik.yml` / `traefik.yaml` / `traefik.toml`, looked for in `/etc/traefik/`, `$XDG_CONFIG_HOME/`, `$HOME/.config/` and the working directory.
- Docker labels look like `traefik.http.routers.<name>.rule`; `providers.docker.exposedByDefault` controls whether containers need `traefik.enable=true`.
- The options table lists keys in dotted form (`providers.docker.exposedByDefault`).
