# Headscale 0.29.7 — overview

Headscale is an open-source, self-hosted implementation of the Tailscale
**control server** (coordination server): official Tailscale clients connect to
it instead of Tailscale's SaaS to form a private network (a "tailnet"). This set is
the official documentation at release tag **v0.29.7** (newest stable on
2026-11-10) from `docs/` in github.com/juanfont/headscale, plus the example
configs, the REST API spec and the 0.29.x changelog.

## Layout

| Folder | What it holds |
|---|---|
| `content/setup/` | Requirements, install (official packages, container, community packages, from source), `upgrade.md` |
| `content/usage/` | `getting-started.md` (users, registering nodes, pre-auth keys), connecting Android, Apple and Windows clients |
| `content/ref/` | Reference: `configuration.md`, `policy.md` (ACLs, grants, autogroups, node attributes), `oidc.md`, `derp.md`, `dns.md`, `routes.md` (subnet routers, exit nodes), `tags.md`, `registration.md`, `tls.md`, `api.md`, `debug.md`, `integration/` (reverse proxy, web UIs, tools) |
| `content/ref/examples/` | `config-example.yaml` (every server setting, commented) and `derp-example.yaml` |
| `content/about/` | Features, supported clients, FAQ, releases |
| `api/` | `headscale.swagger.json` and generated pages: `endpoints/headscaleservice.md`, `schemas.md` |
| `content/release-notes/` | `CHANGELOG-0.29.md` |

## Where to look for…

- **Install** — `setup/install/official.md` (packages), `setup/install/container.md`.
- **Every config setting** — `ref/examples/config-example.yaml`; how config is loaded in `ref/configuration.md`.
- **ACL policy, grants, autogroups, tests** — `ref/policy.md`; new 0.29 features in the changelog.
- **Log in with an identity provider (Authelia, Authentik, Google, Kanidm, Keycloak, Entra ID)** — `ref/oidc.md`.
- **Register a node / pre-auth keys** — `usage/getting-started.md`, `ref/registration.md`.
- **Subnet routers and exit nodes** — `ref/routes.md`.
- **MagicDNS, extra DNS records** — `ref/dns.md`.
- **Embedded or custom DERP relays** — `ref/derp.md`.
- **Behind nginx / Caddy / Traefik** — `ref/integration/reverse-proxy.md`.
- **TLS / Let's Encrypt** — `ref/tls.md`.
- **REST API and API keys** — `ref/api.md`; endpoints in `api/endpoints/headscaleservice.md`.
- **Upgrading between versions** — `setup/upgrade.md` and the BREAKING section of 0.29.0 in the changelog.
- **Which client versions work** — `about/clients.md`; the changelog states the minimum.

## Version notes (from `release-notes/CHANGELOG-0.29.md`)

- Minimum supported Tailscale client: **v1.80.0**.
- **0.29.0 breaking**: upgrades must go one minor version at a time (0.27 → 0.29 is blocked) and downgrades to an earlier minor are blocked; `*` in ACLs now means the tailnet ranges (`100.64.0.0/10`, `fd7a:115c:a1e0::/48`), not all IPs (use `autogroup:danger-all` as a source for that); `proto:icmp` is ICMPv4 only; the `randomize_client_port` config key moved into the policy file as `randomizeClientPort` (Headscale won't start with the old key); hostname collisions get numeric suffixes (`laptop-1`); `headscale nodes register` is deprecated in favour of `headscale auth register --auth-id <id> --user <user>`.
- **0.29.0 new**: Tailscale **grants**, SSH `check` action with `headscale auth approve/reject`, policy `tests` and `sshTests` (beta), `nodeAttrs`, Taildrive, HA subnet-router health probing.
- The docs' configuration page links config examples for **0.29.5**: the site's build variable wasn't updated for 0.29.7. Use `ref/examples/config-example.yaml` here, taken from v0.29.7.

## Search tips

- The server config file is `config.yaml`, looked for in `/etc/headscale`, `$HOME/.headscale` and the working directory (or `-c` / `HEADSCALE_CONFIG`); check it with `headscale configtest`.
- The policy file is HuJSON, Tailscale's policy format; Headscale's docs say which parts are supported and link to tailscale.com for syntax.
- Tailscale terms used here: tailnet, node, pre-auth key, tag, exit node, subnet router, MagicDNS, DERP.
