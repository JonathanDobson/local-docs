# Gitea 28 — overview

Gitea is a self-hosted Git service (repositories, pull requests, issues, package
registry, and CI/CD through Gitea Actions). This docs set covers the **Gitea 28**
release line; the newest release at ingest time is **v28.3.0** (2026-11-01). The
English user/admin docs come from the official docs-site source repository
`https://gitea.com/gitea/docs` (`versioned_docs/version-28`, which is what
docs.gitea.com serves for "28"); the Gitea Runner docs come from the same repo
(`runner-docs_versioned_docs/version-5`, runner 5.x, latest 5.2.0); the REST API
specs are copied unchanged from the `go-gitea/gitea` tag `v28.3.0`; and the
release notes for v28.0.0–v28.3.0 come from the GitHub releases. The docs
site's `@version@`-style placeholders were filled in with the 28 values the site
build uses (`28.3.0`, Go 1.27, Node 22, branch `release/v28`).

## Layout

- `content/docs/` — the main Gitea docs, same structure as docs.gitea.com:
  - `installation/` — binary, package, source, Docker (rootful and rootless),
    Podman quadlet, Kubernetes, Windows service, database preparation, upgrading.
  - `administration/` — the config reference (`config-cheat-sheet.md`), command
    line, authentication (LDAP, PAM, OAuth2/OIDC, reverse-proxy auth), email,
    HTTPS, reverse proxies, logging, backup/restore, customizing, signing, audit
    logging, indexers, LFS.
  - `usage/` — `actions/` (Gitea Actions CI/CD), `packages/` (one page per
    package registry type), `repository/` (webhooks, mirrors, migration, push
    options, templates, code owners), `issues-prs/` (PRs, AGit, templates,
    labels), `access-control/` (permissions, protected branches/tags, blocking),
    `user-setting/` (multi-factor authentication).
  - `development/` — API usage and tokens, OAuth2 provider, integrations,
    migrations.
  - `help/` — FAQ and support.
- `content/runner/` — Gitea Runner 5.x (the program that executes Actions jobs):
  installation, registration, configuration, labels, cache, proxy, job hooks,
  `reference/cli.md` and `reference/config-example.md`.
- `content/release-notes/` — official release notes for v28.0.0, v28.1.0,
  v28.2.0, v28.3.0 (breaking changes, security fixes, features).
- `api/` — `v1-swagger.generated.json` (Swagger 2.0) and
  `v1-openapi3.generated.json` (OpenAPI 3.0), unchanged from the v28.3.0 tag
  (they still contain the placeholders `0.0.0+GITEA-API-APP-VERSION` and
  `/GITEA-API-APP-SUBURL/api/v1`). `api/endpoints/<tag>.md` is one page per API
  tag (`repository`, `user`, `organization`, `issue`, `admin`, `package`,
  `notification`, `settings`, `miscellaneous`) and `api/schemas.md` lists every
  model; both were generated from the OpenAPI 3 spec with paths shown relative
  to the base path `/api/v1`.

## Where to look for…

| Task | File |
|---|---|
| Every `app.ini` setting and its default | `content/docs/administration/config-cheat-sheet.md` |
| Setting config through environment variables (`GITEA__section__KEY`) | `content/docs/administration/config-cheat-sheet.md` (section "Use environment variables to setup Gitea"), `content/docs/installation/with-docker.md` |
| Install with Docker / docker-compose | `content/docs/installation/with-docker.md`, `with-docker-rootless.md` |
| Install from binary, verify signatures | `content/docs/installation/from-binary.md` |
| Upgrade an existing instance | `content/docs/installation/upgrade-from-gitea.md` + `content/release-notes/` |
| `gitea` CLI (`admin user create`, `dump`, `doctor`, `actions generate-runner-token`) | `content/docs/administration/command-line.md` |
| API authentication and creating tokens | `content/docs/development/api-usage.md` |
| A specific REST endpoint | `api/endpoints/<tag>.md` (e.g. `rg -n "^## .* /repos/\{owner\}/\{repo\}/pulls" api/endpoints`) |
| A request/response model's fields | `api/schemas.md` |
| Actions workflows, secrets, variables, contexts | `content/docs/usage/actions/` (`overview.md`, `quickstart.md`, `secrets.md`, `variables.md`, `faq.md`, `comparison.md`) |
| Install, register and configure a runner | `content/runner/` (`installation/`, `registration.md`, `configuration.md`, `labels.md`) |
| Webhook payloads and events | `content/docs/usage/repository/webhooks.md` |
| LDAP / OAuth2 / OIDC / reverse-proxy login | `content/docs/administration/authentication.md` |
| Using Gitea as an OAuth2 provider | `content/docs/development/oauth2-provider.md` |
| Package registries (npm, container, Maven, PyPI…) | `content/docs/usage/packages/<type>.md`, `overview.md` |
| Reverse proxy (nginx, Apache, Caddy, Traefik) | `content/docs/administration/reverse-proxies.md` |
| Backup and restore | `content/docs/administration/backup-and-restore.md` |
| Branch protection | `content/docs/usage/access-control/protected-branches.md` |

## Version notes

- **Renumbering:** Gitea went from `1.27.x` straight to `28.0.0` (released
  2026-09-29). Read 28 as what would have been 1.28. Several docs pages still
  speak in `1.x` terms (e.g. `:1.x-nightly` Docker tags, the "a.b.x" upgrade
  compatibility table in `upgrade-from-gitea.md`); the docs do not say how the
  new numbering maps onto those rules.
- **Breaking in 28.0.0** (`content/release-notes/v28.0.0.md`): Git network
  operations now go through an internal proxy, with updated egress settings (see
  `[proxy]`, `[security]`, `[migrations]` in the config cheat sheet); and Actions
  gained `RUN_RETENTION_DAYS` (default 400) which **deletes completed runs** older
  than that, run by a cron job.
- New in 28.0.0 (selection): audit logging (`administration/audit-logging.md`,
  `[audit]`), deploy tokens, bot accounts, admin impersonation, regenerable
  personal access tokens, project APIs, force-cancel workflow run API, Actions
  `max-parallel` and dynamic matrices, `self:` prefix in `uses:`, scoped
  workflows (`usage/actions/scoped-workflows.md`), shared `[redis]` section,
  WebSocket instead of SSE for UI notifications.
- 28.1.0–28.3.0 are bug-fix/enhancement releases with no breaking section.
- Building from source needs Go 1.27+ and Node 22+.
- The API spec ships as both Swagger 2.0 and OpenAPI 3.0 (OpenAPI 3 exists since
  1.27); from 28 the spec is a pre-generated JSON file rather than a Go template.

## Search tips

- The config file is `app.ini` (default `custom/conf/app.ini`); sections are
  written `[server]`, `[database]`, `[actions]`, `[repository.pull-request]` etc.
  In the cheat sheet each section header looks like ``## Server (`server`)``.
  Env-var form is `GITEA__section__KEY`, e.g. `GITEA__database__DB_TYPE`.
- "Gitea Actions" is the CI system; "Gitea Runner" (repo
  `gitea.com/gitea/runner`) is the separate program that runs jobs. Workflows live in
  `.gitea/workflows/` (or `.github/workflows/`).
- "AGit" is Gitea's push-to-create-PR flow (`git push origin HEAD:refs/for/main`).
- API paths are under `/api/v1`; tokens go in `Authorization: token <t>`; token
  permissions are called "scopes" (`read:repository`, `write:issue`…).
- "Doctor" is the `gitea doctor` repair/check command; "dump" is the backup
  command.
- Admin web UI paths use `/-/admin/…`.
