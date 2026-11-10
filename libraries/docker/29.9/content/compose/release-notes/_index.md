---
title: "Release notes"
source: https://docs.docker.com/compose/release-notes/
---

# Release notes

Every Docker Compose v5 release. From the GitHub releases of [docker/compose](https://github.com/docker/compose/releases), which is where this page links on docs.docker.com.

## v5.7.0

_2026-11-02 · tag `v5.7.0`_

## What's Changed

> ℹ️ **Heads-up for users of Compose as a library:** `Up` now runs its Create and Start phases as **a single plan over a single daemon snapshot**, for `up -d` ([#14290](https://github.com/docker/compose/pull/14290)) and interactive `up` ([#14305](https://github.com/docker/compose/pull/14305)), as `scale`, watch rebuilds and `start` already do ([#14291](https://github.com/docker/compose/pull/14291), [#14296](https://github.com/docker/compose/pull/14296)). The CLI behaves as before. If you call `api.Compose.Up` from your own program:
>
> * `Up` now validates its options first, with the same rules as the CLI flags: `UpOptions.Validate()` returns an `*api.IncompatibleOptionsError` (`errors.Is(err, api.ErrIncompatibleOptions)`) for `Start.Wait` combined with `Start.Attach`, and for a detached `Up` (no `Start.Attach`) combined with `OnExit`, `ExitCodeFrom` or `Watch`. Those combinations used to be silently ignored ([#14306](https://github.com/docker/compose/pull/14306)).
> * `Up` works on the project it is given and ignores `StartOptions.Project`.
> * The daemon is not observed again between the two phases: a container that exits after the plan is built is not started again, and one removed in between makes its start fail instead of being skipped. A planning error of the Start phase now fails before any container is created.
> * A foreground `Up` now gives a `use_api_socket` service its `/run/secrets/docker/config.json`, as `up -d` does, and shows the output of `pre_start` hooks.
> * The keyboard menu of an interactive `up` is no longer built by the library: set `NavigationMenu: true` **and** pass an implementation with `compose.WithNavigationMenu(...)`, otherwise no menu is displayed and a warning says so ([#14324](https://github.com/docker/compose/pull/14324)).
>
> Other changes to the library surface in this release: `DownOptions.Images` is now an `api.ImagePruneMode` (untyped constants still compile, a `string` variable needs a conversion) and an invalid value is rejected before `Down` removes anything ([#14149](https://github.com/docker/compose/pull/14149)); `compose.ServiceHash`, `compose.NetworkHash` and `compose.VolumeHash` are no longer exported, the helpers having moved to an internal package ([#14405](https://github.com/docker/compose/pull/14405)); `api.Compose` is now assembled from six smaller interfaces, with the same method set ([#14322](https://github.com/docker/compose/pull/14322)); `PushOptions.IgnoreMissing` is added.

### ✨ Improvements

**Execution plan**
* Feat: detached up runs on a single plan by @ndeloof in https://github.com/docker/compose/pull/14290
* Feat(up): interactive up runs on a single plan by @ndeloof in https://github.com/docker/compose/pull/14305
* Feat: scale and watch rebuild use the unified plan by @ndeloof in https://github.com/docker/compose/pull/14291
* Feat: compose start builds a start-only plan by @ndeloof in https://github.com/docker/compose/pull/14296

**Commands**
* Feat(run): --no-recreate reuses existing dependencies as-is by @ndeloof in https://github.com/docker/compose/pull/14144
* Feat(push): add --ignore-missing to skip images not available locally by @glours in https://github.com/docker/compose/pull/14341
* Feat(push): deprecate --ignore-push-failures in favor of --ignore-missing by @glours in https://github.com/docker/compose/pull/14354
* Feat(stats): add --all-projects and --aggregate flags by @glours in https://github.com/docker/compose/pull/14337
* Feat(network): let a service opt out of its name as a network alias by @glours in https://github.com/docker/compose/pull/14342
* Pass --parallel limit to bake as --jobs by @maxproske in https://github.com/docker/compose/pull/14352

**Other**
* Feat: support the umask service attribute by @ndeloof in https://github.com/docker/compose/pull/14367
* Use the Docker Desktop Hub session for Docker Hub registry credentials by @Benehiko in https://github.com/docker/compose/pull/14295

### 🐛 Fixes
* Fix(bridge): reject --dry-run on bridge commands by @glours in https://github.com/docker/compose/pull/14307
* Fix(up): don't report a cancelled or expired wait on an optional dependency as skipped by @ndeloof in https://github.com/docker/compose/pull/14309
* Fix(logs): relay each line of a restarted container exactly once by @ndeloof in https://github.com/docker/compose/pull/14314
* Fix(bake): grant permissions for configured build inputs by @crazy-max in https://github.com/docker/compose/pull/14325
* Fix(watch): skip sync+exec triggers on bind-mounted paths by @glours in https://github.com/docker/compose/pull/14328
* Fix: pre_start hooks receive the service env_file and environment by @ndeloof in https://github.com/docker/compose/pull/14293
* Fix: keep the image pull of compose run inside the run progress block by @ndeloof in https://github.com/docker/compose/pull/14294
* Fix: do not execute providers and models in dry-run mode by @glours in https://github.com/docker/compose/pull/14334
* Fix(build): read bake's stderr to the end before waiting for it by @ndeloof in https://github.com/docker/compose/pull/14335
* Fix(executor): a wait node holds no --parallel slot while it polls by @ndeloof in https://github.com/docker/compose/pull/14303
* Fix(pre_start): capture a hook's output by opening its log stream once started by @ndeloof in https://github.com/docker/compose/pull/14353
* Fix(run): keep a recreated dependency's anonymous volumes by @htoyoda18 in https://github.com/docker/compose/pull/14358
* Fix(watch): ignore .git at any depth inside the watched path by @htoyoda18 in https://github.com/docker/compose/pull/14363
* Fix(executor): report the services a failed start interrupts by @ndeloof in https://github.com/docker/compose/pull/14376
* Fix(monitor): subscribe to events since before the initial listing by @ndeloof in https://github.com/docker/compose/pull/14304
* Fix(compose): skip the lowered-environment allocation in envResolverWithCase by @TDnorthgarden in https://github.com/docker/compose/pull/14390
* Fix(projectloader): unescape service names in unsupported attribute warnings by @Huang-404-Q in https://github.com/docker/compose/pull/14380
* Fix(down): keep a volume the project does not own on down -v by @htoyoda18 in https://github.com/docker/compose/pull/14374
* Fix(start): give a started use_api_socket service its config file by @ndeloof in https://github.com/docker/compose/pull/14393
* Fix(up): honor -t when an attached up stops the application by @htoyoda18 in https://github.com/docker/compose/pull/14395
* Fix(up): check a depends_on condition before the first poll tick by @htoyoda18 in https://github.com/docker/compose/pull/14385
* Fix(watch): recognize bind-mounted paths starting with two dots by @ahbaqdadi in https://github.com/docker/compose/pull/14425
* Fix(use_api_socket): harden the credentials handed to the service by @ndeloof in https://github.com/docker/compose/pull/14402

### 🔧  Internal
* Executor: run start-phase operations (epic #14081, lot 1) by @ndeloof in https://github.com/docker/compose/pull/14274
* Api: DownOptions.Images becomes a typed ImagePruneMode, validated upfront by @ndeloof in https://github.com/docker/compose/pull/14149
* Api: reject incompatible Up options with a typed error by @ndeloof in https://github.com/docker/compose/pull/14306
* Refactor: split create() into preparePlan + execute by @ndeloof in https://github.com/docker/compose/pull/14289
* Refactor(executor): let a caller drive the create and start phases itself by @ndeloof in https://github.com/docker/compose/pull/14302
* Refactor(api): split Compose into focused interfaces by @ndeloof in https://github.com/docker/compose/pull/14322
* Refactor(compose): move mutable package-level state into composeService by @ndeloof in https://github.com/docker/compose/pull/14323
* Refactor(up): inject the navigation menu instead of importing cmd/formatter by @ndeloof in https://github.com/docker/compose/pull/14324
* Refactor: extract inspect and projectloader from pkg/compose into internal packages by @ndeloof in https://github.com/docker/compose/pull/14331
* Refactor: move the provider relay and plugin execution to internal/relay and internal/provider by @ndeloof in https://github.com/docker/compose/pull/14333
* Refactor(executor): hand the hook-log listener to runStart only by @ndeloof in https://github.com/docker/compose/pull/14392
* Refactor: move exec, cp, export and commit to internal/containerops by @ndeloof in https://github.com/docker/compose/pull/14397
* Refactor: move the config-hash helpers to internal/confighash by @ndeloof in https://github.com/docker/compose/pull/14405
* Refactor: add internal/concurrency for the bounded errgroup helpers by @ndeloof in https://github.com/docker/compose/pull/14422
* Refactor: remove the helpers duplicated across pkg/compose and the internal packages by @ndeloof in https://github.com/docker/compose/pull/14424
* Docs(compose): drop the comments that still describe the deleted imperative start path by @ndeloof in https://github.com/docker/compose/pull/14398
* Docs(compose): correct what the startMx comment says about #12846 by @ndeloof in https://github.com/docker/compose/pull/14399
* Refactor(compose): drop the timeout parameter of waitDependencies by @ndeloof in https://github.com/docker/compose/pull/14400
* Refactor(compose): move the dependency wait helpers to their own file by @ndeloof in https://github.com/docker/compose/pull/14401
* Ci: run unit tests with -race, pin test tooling, add a ci-ok aggregate check by @ndeloof in https://github.com/docker/compose/pull/14321
* Go.mod: keep go patch version at lowest possible by @thaJeztah in https://github.com/docker/compose/pull/14347
* Build(lint): bump golangci-lint to v2.15.0 and fix its new findings by @ndeloof in https://github.com/docker/compose/pull/14418
* Test(e2e): lock the behavior of the foreground up by @ndeloof in https://github.com/docker/compose/pull/14300
* Test(formatter): keep escape sequences out of the go test output by @htoyoda18 in https://github.com/docker/compose/pull/14351
* Docs: remove broken CONTRIBUTING.md link by @DaneHarrison in https://github.com/docker/compose/pull/14251

### ⚙️ Dependencies
* Build(deps): golang.org/x/net v0.60.0 (security) by @thaJeztah in https://github.com/docker/compose/pull/14316
* Chore(deps): bump github.com/containerd/containerd/v2 v2.4.2 (security) by @thaJeztah in https://github.com/docker/compose/pull/14339
* Update to go1.26.9 (security) by @thaJeztah in https://github.com/docker/compose/pull/14315
* Update to go1.26.10 (security) by @thaJeztah in https://github.com/docker/compose/pull/14366
* Build(deps): bump github.com/mattn/go-shellwords from 1.0.15 to 1.0.16 by @dependabot[bot] in https://github.com/docker/compose/pull/14320
* Build(deps): bump github.com/docker/cli from 29.8.2+incompatible to 29.9.0+incompatible by @dependabot[bot] in https://github.com/docker/compose/pull/14319
* Build(deps): bump github.com/moby/moby/client from 0.6.1 to 0.6.2 by @dependabot[bot] in https://github.com/docker/compose/pull/14318
* Build(deps): bump github.com/docker/secrets-engine/x from 0.8.2 to 0.8.3 by @dependabot[bot] in https://github.com/docker/compose/pull/14301
* Build(deps): bump secrets-engine client to v0.2.0 by @Benehiko in https://github.com/docker/compose/pull/14327
* Build(deps): bump secrets-engine/client to v0.2.2 by @Benehiko in https://github.com/docker/compose/pull/14361
* Build(deps): bump github.com/Microsoft/go-winio from 0.6.3-0.20251027160822-ad3df93bed29 to 0.6.3 by @dependabot[bot] in https://github.com/docker/compose/pull/14330
* Build(deps): bump golang.org/x/sync from 0.23.0 to 0.24.0 by @dependabot[bot] in https://github.com/docker/compose/pull/14329
* Build(deps): bump github.com/mattn/go-runewidth from 0.0.30 to 0.0.31 by @dependabot[bot] in https://github.com/docker/compose/pull/14348
* Build(deps): bump github.com/docker/cli from 29.9.0+incompatible to 29.9.1+incompatible by @dependabot[bot] in https://github.com/docker/compose/pull/14349
* Build(deps): bump actions/upload-artifact from 7.0.1 to 7.0.2 by @dependabot[bot] in https://github.com/docker/compose/pull/14343
* Build(deps): bump actions/download-artifact from 8.0.1 to 8.0.2 by @dependabot[bot] in https://github.com/docker/compose/pull/14344
* Build(deps): bump github/codeql-action/upload-sarif from 4.38.2 to 4.38.3 by @dependabot[bot] in https://github.com/docker/compose/pull/14350
* Build(deps): bump golang.org/x/sys from 0.48.0 to 0.49.0 by @dependabot[bot] in https://github.com/docker/compose/pull/14338
* Build(deps): bump ossf/scorecard-action from 2.4.4 to 2.5.0 by @dependabot[bot] in https://github.com/docker/compose/pull/14360
* Build(deps): bump docker/bake-action from 7.4.0 to 7.5.0 in the docker-actions group by @dependabot[bot] in https://github.com/docker/compose/pull/14371
* Build(deps): bump github.com/docker/cli from 29.9.1+incompatible to 29.9.2+incompatible by @dependabot[bot] in https://github.com/docker/compose/pull/14369
* Build(deps): bump github.com/Microsoft/go-winio from 0.6.3 to 0.6.4 by @dependabot[bot] in https://github.com/docker/compose/pull/14368
* Build(deps): bump the docker-actions group with 2 updates by @dependabot[bot] in https://github.com/docker/compose/pull/14389
* Build(deps): bump github/codeql-action/upload-sarif from 4.38.3 to 4.39.0 by @dependabot[bot] in https://github.com/docker/compose/pull/14377
* Build(deps): bump docker/github-builder/.github/workflows/bake.yml from 1.18.0 to 1.18.1 in the docker-actions group by @dependabot[bot] in https://github.com/docker/compose/pull/14415
* Build(deps): bump github/codeql-action/upload-sarif from 4.39.0 to 4.39.1 by @dependabot[bot] in https://github.com/docker/compose/pull/14416

## New Contributors
* @Benehiko made their first contribution in https://github.com/docker/compose/pull/14295
* @DaneHarrison made their first contribution in https://github.com/docker/compose/pull/14251
* @TDnorthgarden made their first contribution in https://github.com/docker/compose/pull/14390
* @Huang-404-Q made their first contribution in https://github.com/docker/compose/pull/14380
* @ahbaqdadi made their first contribution in https://github.com/docker/compose/pull/14425

**Full Changelog**: https://github.com/docker/compose/compare/v5.6.1...v5.7.0

## v5.6.1

_2026-10-21 · tag `v5.6.1`_

update to go1.26.10
These releases include 1 security fix following the security policy:

- crypto/x509: mitigation for security concerns with a specific Certificate Authority

  We're blocking trust in a small set of intermediate certificates due to specific security concerns around their operation.

  Verify will now filter out chains which contain these intermediates, preventing them from being returned to the caller.

  We highly recommend immediately upgrading to this release.

  This is CVE-2026-111943 and Go issue https://go.dev/issue/82345.

**Full Changelog**: https://github.com/docker/compose/compare/v5.6.0...v5.6.1

## v5.6.0

_2026-10-02 · tag `v5.6.0`_

## What's Changed

> ℹ️ This release adds **partial support for jobs**: only manually-triggered jobs are supported for now, scheduled jobs are not yet available. Full job support will land once the corresponding Docker Engine support is merged.

### ✨ Improvements

**Jobs**
* Adopt compose-go jobs and container-spec layering by @ndeloof in https://github.com/docker/compose/pull/14093

**Provider services**
* Feat(provider): get-service-config provider request by @ndeloof in https://github.com/docker/compose/pull/14175
* Feat(provider): publish-endpoint deploys a network relay for provider services by @ndeloof in https://github.com/docker/compose/pull/14193
* Get-relay-info tells providers where to bind for the relay by @ndeloof in https://github.com/docker/compose/pull/14258
* Feat(compose): dedicated network for the provider relay link by @ndeloof in https://github.com/docker/compose/pull/14275
* Provider services take part in the image phase, with image distribution on demand by @ndeloof in https://github.com/docker/compose/pull/14252

**Other**
* Feat(compose): warn on unsupported compose-file attributes by @glours in https://github.com/docker/compose/pull/14196
* PRIVATE_PORT optional for `docker compose port` by @maxproske in https://github.com/docker/compose/pull/13577

### 🐛 Fixes
* Fix(build): hand unresolved 'auto' progress mode to bake by @ndeloof in https://github.com/docker/compose/pull/14194
* Fix(watch): coalesce rebuilds triggered during a burst of file changes by @glours in https://github.com/docker/compose/pull/14202
* Fix(port): preserve tie order for dual-stack port publishers by @glours in https://github.com/docker/compose/pull/14213
* Fix(publish): warn when push falls back from OCI 1.1 to OCI 1.0 by @htoyoda18 in https://github.com/docker/compose/pull/14146
* Fix: detect externally stopped and removed containers in up monitor by @glours in https://github.com/docker/compose/pull/13990
* Fix(dry-run): commit no longer creates a real image; the interception set becomes declarative by @ndeloof in https://github.com/docker/compose/pull/14150
* Fix(up): drop benign context.Canceled noise from the final report by @ndeloof in https://github.com/docker/compose/pull/14227
* Fix(relay): reconnect to new networks when routes are unchanged by @ndeloof in https://github.com/docker/compose/pull/14236
* Fix(provider): clean up stale relay and guard start/restart against it by @ndeloof in https://github.com/docker/compose/pull/14238
* Fix(hash): pin the service config-hash byte layout, decoupled from compose-go struct refactorings by @ndeloof in https://github.com/docker/compose/pull/14215
* Fix(hash): repair main after #14093/#14215 merged in reverse order by @ndeloof in https://github.com/docker/compose/pull/14253
* Fix(logs): restart re-attach loses a fast run's output — found by deflaking e2e by @ndeloof in https://github.com/docker/compose/pull/14140
* Fix: provider migration condemns the service's stale replicas by @ndeloof in https://github.com/docker/compose/pull/14264
* Fix/down rmi dangling images by @glours in https://github.com/docker/compose/pull/14266
* Fix/dry run service completed successfully 14269 by @glours in https://github.com/docker/compose/pull/14270
* Fix: honor --parallel across all bulk engine-call fan-outs by @glours in https://github.com/docker/compose/pull/14177
* Fix: adapt to compose-go v2.16.1 promoting x-initialSync silently by @glours in https://github.com/docker/compose/pull/14281

### 🔧  Internal
* Remove jonboulle/clockwork for testing/synctest by @thaJeztah in https://github.com/docker/compose/pull/14185
* Rebuild the TTY progress renderer on a model/layout/screen split by @ndeloof in https://github.com/docker/compose/pull/14051
* Golangci-lint: enable perfsprint linter by @thaJeztah in https://github.com/docker/compose/pull/14207
* Cmd/prompt: remove uses of github.com/AlecAivazis/survey/v2 by @thaJeztah in https://github.com/docker/compose/pull/14161
* Chore: update docker-agent-action to v2.0.8 by @docker-agent in https://github.com/docker/compose/pull/14197
* Chore: update docker-agent-action to v2.0.9 by @docker-agent in https://github.com/docker/compose/pull/14225
* Test(e2e): wait on state, not on an unsynchronized log line by @ndeloof in https://github.com/docker/compose/pull/14228
* E2e coverage for git and OCI remote stacks by @ndeloof in https://github.com/docker/compose/pull/14226
* Ci: lint, vet and test relay/ as its own module by @ndeloof in https://github.com/docker/compose/pull/14235
* Test(e2e): reproduce #14223 -- additional_contexts to a disabled service by @ndeloof in https://github.com/docker/compose/pull/14242
* Test(e2e): reproduce --project-directory ignored on an oci:// project (#14224) by @ndeloof in https://github.com/docker/compose/pull/14234
* Test(e2e): fix TestPullFailure's daemon-specific error assertion by @ricardobranco777 in https://github.com/docker/compose/pull/14245
* Plan engine: reconciler plans the start phase (epic #14081, lot 1) by @ndeloof in https://github.com/docker/compose/pull/14200
* Add AI Policy by @glours in https://github.com/docker/compose/pull/13550
* Pre_start hook runners become reconciliation-plan resources by @ndeloof in https://github.com/docker/compose/pull/14221
* Chore: remove duplicate 'publish' registration under 'alpha' by @glours in https://github.com/docker/compose/pull/14272
* Dependabot: disable cooldown for compose-spec, docker, moby modules by @thaJeztah in https://github.com/docker/compose/pull/14276

### ⚙️ Dependencies
* Fix(deps): github.com/containerd/containerd/v2 v2.3.5 by @thaJeztah in https://github.com/docker/compose/pull/14183
* Build(deps): bump softprops/action-gh-release from 3.0.2 to 3.0.3 by @dependabot[bot] in https://github.com/docker/compose/pull/14195
* Fix(deps): github.com/moby/sys/userns v0.2.1 by @thaJeztah in https://github.com/docker/compose/pull/14199
* Build(deps): bump golang.org/x/sys from 0.47.0 to 0.48.0 by @dependabot[bot] in https://github.com/docker/compose/pull/14205
* Build(deps): bump golang.org/x/sync from 0.22.0 to 0.23.0 by @dependabot[bot] in https://github.com/docker/compose/pull/14206
* Build(deps): bump github.com/mattn/go-runewidth from 0.0.23 to 0.0.29 by @dependabot[bot] in https://github.com/docker/compose/pull/14208
* Build(deps): bump tags.cncf.io/container-device-interface from 1.1.0 to 1.1.1 by @dependabot[bot] in https://github.com/docker/compose/pull/14218
* Build(deps): bump github.com/moby/moby/api from 1.55.0 to 1.56.0 by @dependabot[bot] in https://github.com/docker/compose/pull/14211
* Feat(deps): github.com/docker/cli v29.8.0 by @thaJeztah in https://github.com/docker/compose/pull/14138
* Build(deps): bump github.com/mattn/go-shellwords from 1.0.14 to 1.0.15 by @dependabot[bot] in https://github.com/docker/compose/pull/14246
* Build(deps): bump the docker-actions group across 1 directory with 3 updates by @dependabot[bot] in https://github.com/docker/compose/pull/14254
* Build(deps): github.com/DefangLabs/secret-detector 3e28d7ed64df by @thaJeztah in https://github.com/docker/compose/pull/14240
* Build(deps): bump codecov/codecov-action from 7.0.0 to 7.1.0 by @dependabot[bot] in https://github.com/docker/compose/pull/14247
* Build(deps): bump github/codeql-action/upload-sarif from 4.37.9 to 4.38.0 by @dependabot[bot] in https://github.com/docker/compose/pull/14231
* Build(deps): bump github.com/mattn/go-runewidth from 0.0.29 to 0.0.30 by @dependabot[bot] in https://github.com/docker/compose/pull/14239
* Build(deps): bump codecov/codecov-action from 7.1.0 to 7.1.1 by @dependabot[bot] in https://github.com/docker/compose/pull/14256
* Build(deps): bump github.com/docker/cli from 29.8.0+incompatible to 29.8.1+incompatible by @dependabot[bot] in https://github.com/docker/compose/pull/14255
* Build(deps): bump github.com/docker/cli from 29.8.1+incompatible to 29.8.2+incompatible by @dependabot[bot] in https://github.com/docker/compose/pull/14279
* Build(deps): bump github/codeql-action/upload-sarif from 4.38.0 to 4.38.2 by @dependabot[bot] in https://github.com/docker/compose/pull/14280
* Build(deps): bump github.com/moby/buildkit from 0.33.0 to 0.33.1 by @dependabot[bot] in https://github.com/docker/compose/pull/14277
* Build(deps): bump google.golang.org/grpc from 1.83.2 to 1.84.0 by @dependabot[bot] in https://github.com/docker/compose/pull/14262
* Build(deps): bump moby/moby and containerd/containerd/v2 by @ndeloof in https://github.com/docker/compose/pull/14282

**Full Changelog**: https://github.com/docker/compose/compare/v5.5.1...v5.6.0

## v5.5.1

_2026-09-03 · tag `v5.5.1`_

## What's Changed
### ✨ Improvements
* Feat(hooks): capture and surface lifecycle hook output by @glours in https://github.com/docker/compose/pull/14091
* Feat(tracing): surface otel shutdown errors via `--debug` by @htoyoda18 in https://github.com/docker/compose/pull/14152

### 🐛 Fixes
* Fix(events): validate service names before subscribing to events by @glours in https://github.com/docker/compose/pull/14076
* Fix: bake target names collision for services differing by `.` vs `_` by @ndeloof in https://github.com/docker/compose/pull/14058
* Fix(watch): sync into a symlinked directory instead of failing by @Endika in https://github.com/docker/compose/pull/14084
* Fix(hooks): include hook output in the error when a hook fails by @dennislapchenko in https://github.com/docker/compose/pull/14088
* Fix(build): TTY progress on Windows — hand the real stdout to buildkit by @ndeloof in https://github.com/docker/compose/pull/14090
* Fix(watch): sync all files on `initial_sync`, regardless of mtime by @glours in https://github.com/docker/compose/pull/14096
* Fix(network): pass IPAM options when creating networks by @glours in https://github.com/docker/compose/pull/14094
* Fix(ps): honor psFormat from Docker CLI config when no `--format` flag given by @glours in https://github.com/docker/compose/pull/14095
* Fix: dependency wait timeout surfaced only by luck by @ndeloof in https://github.com/docker/compose/pull/14105
* Fix: hold startMx on the start path actually exercised by @ndeloof in https://github.com/docker/compose/pull/14106
* Fix(watch): exclude Dockerfile and compose files from initial sync by @htoyoda18 in https://github.com/docker/compose/pull/14117
* Fix(display): stop ttyWriter.Done from hanging after context cancel by @glours in https://github.com/docker/compose/pull/14119
* Fix(build): honor provenance/sbom false in per-service bake attest by @glours in https://github.com/docker/compose/pull/14112
* Fix(compose): reject unknown subcommands under bridge/transformations by @glours in https://github.com/docker/compose/pull/14143
* Fix(plugins): honor PATHEXT for provider lookup on Windows by @ndeloof in https://github.com/docker/compose/pull/14159
* Fix(watch): stop swallowing SetRecursive errors via nolint by @glours in https://github.com/docker/compose/pull/14165
* Fix(bridge): confirm before wiping non-empty convert output dir by @glours in https://github.com/docker/compose/pull/14174
* Fix(down): spare dangling images of orphaned services, like their tagged image by @htoyoda18 in https://github.com/docker/compose/pull/14154

### 🔧  Internal
* CI: raise e2e go-test timeout to 20m by @ndeloof in https://github.com/docker/compose/pull/14072
* Lint: replace gocyclo with gocognit by @ndeloof in https://github.com/docker/compose/pull/14057
* Test(e2e): prepend provider bin dir to PATH in provider tests by @glours in https://github.com/docker/compose/pull/14079
* Refactor: dismantle the gocognit hotspots, one concern per function by @ndeloof in https://github.com/docker/compose/pull/14060
* Test(e2e): declarative Scenario layer, project files under testdata/<TestName>/ by @ndeloof in https://github.com/docker/compose/pull/14087
* Docs: document engine container event sequences in up monitor by @ndeloof in https://github.com/docker/compose/pull/14024
* E2E: fix test resource isolation and make standalone parallelism configurable by @glours in https://github.com/docker/compose/pull/14073
* API: ScaleOptions carries the replica counts by @ndeloof in https://github.com/docker/compose/pull/14077
* Chore: explicit, unique, greppable internal names by @ndeloof in https://github.com/docker/compose/pull/14049
* Docs: update CONTRIBUTING.md to reflect current tooling and practices by @glours in https://github.com/docker/compose/pull/14098
* API: option structs document what the implementation actually honors by @ndeloof in https://github.com/docker/compose/pull/14078
* Test: unit-lock the imperative start path by @ndeloof in https://github.com/docker/compose/pull/14104
* CLI: display.Mode always resolves to the mode actually rendered by @ndeloof in https://github.com/docker/compose/pull/14103
* CI: validate generated mocks are in sync by @ndeloof in https://github.com/docker/compose/pull/14102
* Docs(sdk): document the EventProcessor API that actually exists by @ndeloof in https://github.com/docker/compose/pull/14131
* Test(e2e): gate the e2e suite behind the build tag the docs already promise by @ndeloof in https://github.com/docker/compose/pull/14132
* Build: error messages name the real remedy, not a removed builder by @ndeloof in https://github.com/docker/compose/pull/14133
* Docs(contributing): legibility guidelines — comments state behavior, not history by @ndeloof in https://github.com/docker/compose/pull/14135
* Test(docs): compile the sdk.md examples by @ndeloof in https://github.com/docker/compose/pull/14136
* Chore(compose): rename convergence.go, whose convergence engine no longer exists by @ndeloof in https://github.com/docker/compose/pull/14129
* Chore(compose): comments state behavior, not history by @ndeloof in https://github.com/docker/compose/pull/14130
* Test(build): re-enable wrong ssh key id test by @htoyoda18 in https://github.com/docker/compose/pull/14120
* Chore(compose): orphan semantics stated where up and down diverge by @ndeloof in https://github.com/docker/compose/pull/14142
* Refactor: NewGraph stops mutating the project by @ndeloof in https://github.com/docker/compose/pull/14124
* Test(e2e): bump compose-bridge images to v0.0.7 by @ricardobranco777 in https://github.com/docker/compose/pull/14170

### ⚙️ Dependencies
* Build(deps): bump github/codeql-action/upload-sarif from 4.37.6 to 4.37.7 by @dependabot[bot] in https://github.com/docker/compose/pull/14101
* Remove buildx as a Go dependency by @ndeloof in https://github.com/docker/compose/pull/14123
* Chore(deps): github.com/sirupsen/logrus v1.10.2, google.golang.org/grpc v1.83.2 by @thaJeztah in https://github.com/docker/compose/pull/14137
* Build: bump golangci-lint to v2.13.2 by @ndeloof in https://github.com/docker/compose/pull/14164
* Build(deps): bump github/codeql-action/upload-sarif from 4.37.7 to 4.37.9 by @dependabot[bot] in https://github.com/docker/compose/pull/14167
* Update to go1.26.8 by @thaJeztah in https://github.com/docker/compose/pull/14172
* Feat(deps): github.com/moby/buildkit v0.33.0 by @thaJeztah in https://github.com/docker/compose/pull/14171
* Build(deps): golang.org/x/crypto v0.56.0 by @thaJeztah in https://github.com/docker/compose/pull/14173
* Bump compose-go to version v2.15.0 by @glours in https://github.com/docker/compose/pull/14178

## New Contributors
* @dennislapchenko made their first contribution in https://github.com/docker/compose/pull/14088

**Full Changelog**: https://github.com/docker/compose/compare/v5.5.0...v5.5.1

## v5.5.0

_2026-08-17 · tag `v5.5.0`_

## What's Changed

> ℹ️  This release overhauls image digest reconciliation to prevent unnecessary container recreation.                                                                                                                                                   
> Existing containers may be recreated the first time you run `compose up` after upgrading, as image digests are re-evaluated using the new logic.                                                                                                      
>                                                                                                                                                                                                                                                        
> `compose pull` now honors `pull_policy` refresh windows (`daily`, `weekly`, `every_N`).

### ✨ Improvements
* New image digest reconciliation process by @glours & @ndeloof https://github.com/docker/compose/pull/14011 https://github.com/docker/compose/pull/14041

### 🐛 Fixes
* Fix(bridge): skip pulling default image references for build-only ser… by @ericwyles in https://github.com/docker/compose/pull/14010
* Fix(watch): stop pruning every dangling image of the project by @glours in https://github.com/docker/compose/pull/14012
* Fix(config): resolve service environment when computing --hash by @glours in https://github.com/docker/compose/pull/14002
* Fix(watch): skip unreadable directories instead of failing the watch by @Endika in https://github.com/docker/compose/pull/13992
* Fix: ignore one-off container events in up monitor by @brano-osif in https://github.com/docker/compose/pull/14038
* Fix(bridge): validate arguments of bridge subcommands by @glours in https://github.com/docker/compose/pull/14003
* Fix(images): tolerate containers whose image record is gone by @ndeloof in https://github.com/docker/compose/pull/14028

### 🔧  Internal
* Test: Set stop_signal to SIGTERM in nginx-based services by @ricardobranco777 in https://github.com/docker/compose/pull/13881
* Chore: inline needlessly extracted single-use helpers by @ndeloof in https://github.com/docker/compose/pull/14048
* Add ENGINE column driven by label by @nicksieger in https://github.com/docker/compose/pull/13959

### ⚙️ Dependencies
* Build(deps): bump github.com/moby/moby/client from 0.5.0 to 0.5.1 by @dependabot[bot] in https://github.com/docker/compose/pull/13999
* Build(deps): bump github/codeql-action/upload-sarif from 4.37.3 to 4.37.4 by @dependabot[bot] in https://github.com/docker/compose/pull/14009
* Build(deps): bump github/codeql-action/upload-sarif from 4.37.4 to 4.37.5 by @dependabot[bot] in https://github.com/docker/compose/pull/14019
* Build(deps): bump github.com/moby/buildkit from 0.32.1 to 0.32.2 by @dependabot[bot] in https://github.com/docker/compose/pull/14033
* Build(deps): bump github.com/docker/buildx from 0.36.0 to 0.36.1 by @dependabot[bot] in https://github.com/docker/compose/pull/14034
* Build(deps): bump docker/github-builder/.github/workflows/bake.yml from 1.15.0 to 1.16.0 in the docker-actions group by @dependabot[bot] in https://github.com/docker/compose/pull/14035
* Build(deps): bump github.com/moby/go-archive from 0.3.2 to 0.3.3 by @dependabot[bot] in https://github.com/docker/compose/pull/14043
* Build(deps): bump github/codeql-action/upload-sarif from 4.37.5 to 4.37.6 by @dependabot[bot] in https://github.com/docker/compose/pull/14022
* Build(deps): bump github.com/docker/cli from 29.6.2+incompatible to 29.7.2+incompatible by @dependabot[bot] in https://github.com/docker/compose/pull/14042
* Build(deps): bump google.golang.org/grpc from 1.82.1 to 1.83.0 by @dependabot[bot] in https://github.com/docker/compose/pull/14008
* Bump golang to version 1.26.6 by @glours in https://github.com/docker/compose/pull/14045


## New Contributors
* @ericwyles made their first contribution in https://github.com/docker/compose/pull/14010
* @Endika made their first contribution in https://github.com/docker/compose/pull/13992
* @brano-osif made their first contribution in https://github.com/docker/compose/pull/14038

**Full Changelog**: https://github.com/docker/compose/compare/v5.4.0...v5.5.0

## v5.4.0

_2026-08-03 · tag `v5.4.0`_

## What's Changed

> ℹ️ This release introduces a new way to reconcile resources such as volumes and networks

### ✨ Improvements
* Feat(reconcile): model volume recreation in the plan by @ndeloof in https://github.com/docker/compose/pull/13962
* Feat(reconcile): model network lifecycle in the plan by @ndeloof in https://github.com/docker/compose/pull/13966

### 🐛 Fixes
* Fix(reconcile): preserve zero-replica services during hashing by @junhaoliao in https://github.com/docker/compose/pull/13931
* Fix(config): warn when service selection is silently ignored by @glours in https://github.com/docker/compose/pull/13950
* Fix(build): use platform image-manifest digest, not attested index by @glours in https://github.com/docker/compose/pull/13949
* Fix(oci): honor --insecure-registry when `up` re-loads the model by @ptrdom in https://github.com/docker/compose/pull/13894
* Fix(config): pin type:image volume sources and pre_start hook images by @glours in https://github.com/docker/compose/pull/13956
* Tolerate missing env file on more runtime commands by @maxproske in https://github.com/docker/compose/pull/13603
* Resolve `pre_start` hook images alongside service images by @ndeloof in https://github.com/docker/compose/pull/13937
* Fix(cp): return non-nil Content from dry-run CopyFromContainer by @glours in https://github.com/docker/compose/pull/13982
* Fix(config): apply config flags to `--services`/`--volumes`/`--networks`/`--models`/`--hash` by @glours in https://github.com/docker/compose/pull/13979
* Fix: tolerate missing env file on scale, watch and shell completion by @glours in https://github.com/docker/compose/pull/13973

### 🔧  Internal
* README: remove Go Report Card badge by @thaJeztah in https://github.com/docker/compose/pull/13926
* Docs: adopt `AGENTS.md` standard, symlink `CLAUDE.md` to it by @glours in https://github.com/docker/compose/pull/13871
* Dockerfile: update golang image to alpine `3.23` by @thaJeztah in https://github.com/docker/compose/pull/13921
* Docs: require dated `AI_AGENT_DISCLOSURE.md`, drop committed copy by @glours in https://github.com/docker/compose/pull/13976
* CI: publish images to Docker Hub using OIDC by @glours in https://github.com/docker/compose/pull/13994

### ⚙️ Dependencies
* Build(deps): bump github/codeql-action/upload-sarif from `4.36.2` to `4.37.0` by @dependabot[bot] in https://github.com/docker/compose/pull/13942
* Build(deps): bump the docker-actions group across 1 directory with 4 updates by @dependabot[bot] in https://github.com/docker/compose/pull/13941
* Build(deps): bump actions/stale from `10.3.0` to `10.4.0` by @dependabot[bot] in https://github.com/docker/compose/pull/13943
* Build(deps): bump github.com/mattn/go-shellwords from `1.0.13` to `1.0.14` by @dependabot[bot] in https://github.com/docker/compose/pull/13948
* Build(deps): bump golang.org/x/sync from `0.21.0` to `0.22.0` by @dependabot[bot] in https://github.com/docker/compose/pull/13927
* Build(deps): bump golang.org/x/sys from `0.46.0` to `0.47.0` by @dependabot[bot] in https://github.com/docker/compose/pull/13928
* Build(deps): bump docker/github-builder/.github/workflows/bake.yml from `1.13.0` to `1.14.0` in the docker-actions group by @dependabot[bot] in https://github.com/docker/compose/pull/13953
* Build(deps): bump google.golang.org/grpc from `1.81.1` to `1.82.0` by @dependabot[bot] in https://github.com/docker/compose/pull/13922
* Build(deps): bump softprops/action-gh-release from `3.0.1` to `3.0.2` by @dependabot[bot] in https://github.com/docker/compose/pull/13955
* Build(deps): bump actions/setup-go from `6.5.0` to `7.0.0` by @dependabot[bot] in https://github.com/docker/compose/pull/13960
* Build(deps): bump google.golang.org/grpc from `1.82.0` to `1.82.1` in the go_modules group across 1 directory by @dependabot[bot] in https://github.com/docker/compose/pull/13961
* Build(deps): bump github.com/docker/cli from `29.6.1+incompatible` to `29.6.2+incompatible` by @dependabot[bot] in https://github.com/docker/compose/pull/13968
* Build(deps): bump github/codeql-action/upload-sarif from `4.37.0` to `4.37.3` by @dependabot[bot] in https://github.com/docker/compose/pull/13981
* Build(deps): bump actions/checkout from `7.0.0` to `7.0.1` by @dependabot[bot] in https://github.com/docker/compose/pull/13970
* Build(deps): bump github.com/moby/buildkit from `0.31.1` to `0.31.2` by @dependabot[bot] in https://github.com/docker/compose/pull/13969
* Bump compose-go to version `v2.14.0` by @glours in https://github.com/docker/compose/pull/13983
* Bump go-archive to version `v0.3.0` by @glours in https://github.com/docker/compose/pull/13986
* Build(deps): bump docker/github-builder/.github/workflows/bake.yml from `1.14.0` to `1.15.0` in the docker-actions group by @dependabot[bot] in https://github.com/docker/compose/pull/13989
* Chore(deps): bump github.com/moby/go-archive `v0.3.2` by @thaJeztah in https://github.com/docker/compose/pull/13991
* Update to `go1.26.5` by @thaJeztah in https://github.com/docker/compose/pull/13920
* Build(deps): bump actions/stale from `10.4.0` to `11.0.0` by @dependabot[bot] in https://github.com/docker/compose/pull/13996
* Build(deps): bump docker/docker-agent-action/.github/workflows/review-pr.yml from `2.0.2` to `2.0.3` in the docker-actions group by @dependabot[bot] in https://github.com/docker/compose/pull/13995
* Build(deps): bump ossf/scorecard-action from `2.4.3` to `2.4.4` by @dependabot[bot] in https://github.com/docker/compose/pull/13984
* Chore(deps): github.com/docker/buildx `v0.36.0`, buildkit `v0.32.0` by @glours in https://github.com/docker/compose/pull/13975
* Bump buildkit `v0.32.1` by @glours in https://github.com/docker/compose/pull/13997

## New Contributors
* @junhaoliao made their first contribution in https://github.com/docker/compose/pull/13931

**Full Changelog**: https://github.com/docker/compose/compare/v5.3.1...v5.4.0

## v5.3.1

_2026-07-07 · tag `v5.3.1`_

## What's Changed

### 🔧  Internal
* Ci: add concurrency group to pr-review-trigger to prevent duplicate reviews by @derekmisler in https://github.com/docker/compose/pull/13890
* Fix grammar in Attestations field comment by @blackflytech in https://github.com/docker/compose/pull/13891
* Ci: remove unused desktop-edge-test workflow by @thaJeztah in https://github.com/docker/compose/pull/13897
* Ci: zizmor workflow by @crazy-max in https://github.com/docker/compose/pull/13901
* Ci: fix docs-upstream workflow by @crazy-max in https://github.com/docker/compose/pull/13912
* CODEOWNERS: add compose-reviewers by @thaJeztah in https://github.com/docker/compose/pull/13913
* Ci: harden GitHub Actions workflows by @glours in https://github.com/docker/compose/pull/13896
* GHA: dependabot: group docker/* actions updates by @thaJeztah in https://github.com/docker/compose/pull/13914

### ⚙️ Dependencies

* Build(deps): bump github.com/moby/buildkit from `0.31.0` to `0.31.1` by @dependabot[bot] in https://github.com/docker/compose/pull/13892
* Build(deps): bump github.com/moby/sys/user to `v0.4.1` by @thaJeztah in https://github.com/docker/compose/pull/13893
* Build(deps): bump go.yaml.in/yaml/v4 from `4.0.0-rc.4` to `4.0.0-rc.6` by @dependabot[bot] in https://github.com/docker/compose/pull/13876
* Build(deps): bump github.com/docker/cli from `29.6.0+incompatible` to `29.6.1+incompatible` by @dependabot[bot] in https://github.com/docker/compose/pull/13895
* Build(deps): bump actions/stale from `10.2.0` to `10.3.0` by @dependabot[bot] in https://github.com/docker/compose/pull/13902
* Build(deps): bump the docker-actions group with 3 updates by @dependabot[bot] in https://github.com/docker/compose/pull/13916
* Build(deps): bump actions/upload-artifact from `7.0.0` to `7.0.1` by @dependabot[bot] in https://github.com/docker/compose/pull/13908
* Build(deps): bump actions/setup-go from `6.3.0` to `6.5.0` by @dependabot[bot] in https://github.com/docker/compose/pull/13907
* Build(deps): bump test-summary/action from `2.4` to `2.6` by @dependabot[bot] in https://github.com/docker/compose/pull/13903
* Build(deps): bump mxschmitt/action-tmate from `3.23` to `3.24` by @dependabot[bot] in https://github.com/docker/compose/pull/13910
* Build(deps): bump codecov/codecov-action from `5.5.3` to `7.0.0` by @dependabot[bot] in https://github.com/docker/compose/pull/13904
* Build(deps): bump github/codeql-action/upload-sarif from `3.36.3` to `4.36.2` by @dependabot[bot] in https://github.com/docker/compose/pull/13917
* Build(deps): bump actions/checkout from `6.0.2` to `7.0.0` by @dependabot[bot] in https://github.com/docker/compose/pull/13911

## New Contributors
* @blackflytech made their first contribution in https://github.com/docker/compose/pull/13891

**Full Changelog**: https://github.com/docker/compose/compare/v5.3.0...v5.3.1

## v5.3.0

_2026-07-02 · tag `v5.3.0`_

## What's Changed

> ℹ️ This release introduces native support for init containers.

### ✨ Improvements
* Pre start init containers by @glours in https://github.com/docker/compose/pull/13862

### 🐛 Fixes
* Fix(oci): route authorizer token fetches through provided transport by @glours in https://github.com/docker/compose/pull/13873
* Fix(run): scope Running events to project.Services by @glours in https://github.com/docker/compose/pull/13883

### 🔧  Internal
* Chore: migrate cagent-action to docker-agent-action (v2.0.0) by @docker-agent in https://github.com/docker/compose/pull/13869
* Chore: migrate to docker-agent-action v2.0.1 by @docker-agent in https://github.com/docker/compose/pull/13872
* Fix(reconcile): hash resolved service refs to match executor by @glours in https://github.com/docker/compose/pull/13880
* Fix(compose/port): show private port in portNotFoundError message by @vmphase in https://github.com/docker/compose/pull/13875
* Fix(run): normalize --no-TTY flag to --no-tty by @nickjj in https://github.com/docker/compose/pull/13885

### ⚙️ Dependencies
* Bump compose-go to version v2.13.0 by @glours in https://github.com/docker/compose/pull/13886





## New Contributors
* @docker-agent made their first contribution in https://github.com/docker/compose/pull/13869
* @vmphase made their first contribution in https://github.com/docker/compose/pull/13875
* @nickjj made their first contribution in https://github.com/docker/compose/pull/13885

**Full Changelog**: https://github.com/docker/compose/compare/v5.2.0...v5.3.0

## v5.2.0

_2026-06-23 · tag `v5.2.0`_

## What's Changed

> ℹ️ This version introduces a new reconciliation algorithm between the observed state and the expected state.
> 
> If you experience any issues with a Compose workload that was previously working, please open an issue.

### ✨ Improvements
* Reconciliation plan by @ndeloof & @glours in https://github.com/docker/compose/pull/13830
* Add `rawsetenv` message type for provider plugins by @rajyan in https://github.com/docker/compose/pull/13742

### 🐛 Fixes
* Fix(build): skip remote URL contexts from bake fs.read allowlist by @ndeloof in https://github.com/docker/compose/pull/13816
* Skip validation when extracting config variables by @scarab-systems in https://github.com/docker/compose/pull/13831
* Fix(progress): probe stderr (not stdout) for TTY auto-detection by @glours in https://github.com/docker/compose/pull/13837
* Fix(publish): honor env_file required: false for missing files by @Ijtihed in https://github.com/docker/compose/pull/13848

### 🔧  Internal
* Docs: compose logs: add links for since/until flag descriptions by @thaJeztah in https://github.com/docker/compose/pull/13806
* Ci: add Dependabot cooldown (20260603-170456) by @securityeng-bot[bot] in https://github.com/docker/compose/pull/13820
* Docs(CLAUDE.md): note that commits must be signed off (DCO) by @ndeloof in https://github.com/docker/compose/pull/13817
* Refactor: replace Split in loops with more efficient SplitSeq and replace HasPrefix+TrimPrefix with CutPrefix by @caltechustc in https://github.com/docker/compose/pull/13810
* Chore: fix some comments to improve readability by @solunolab in https://github.com/docker/compose/pull/13823
* GHA: update docs-upstream to pin workflows by sha by @thaJeztah in https://github.com/docker/compose/pull/13834
* Docs: compose logs: add more links for flag descriptions by @thaJeztah in https://github.com/docker/compose/pull/13833
* Fix/progress tty line overflow 13595 by @glours in https://github.com/docker/compose/pull/13840
* Fix(publish): bypass Docker Desktop proxy for loopback registries by @ptrdom in https://github.com/docker/compose/pull/13825
* Watch: do not rebuild depends_on services on file change by @ndeloof in https://github.com/docker/compose/pull/13856
* pkg/e2e: fix malformed JWT in fixtures by @thaJeztah in https://github.com/docker/compose/pull/13857
* pkg/e2e: drop unused run param from getEnv by @glours in https://github.com/docker/compose/pull/13867
* Docs: `ps --format json` outputs JSON Lines, not a JSON array by @glours in https://github.com/docker/compose/pull/13868

### ⚙️ Dependencies
* Build(deps): bump github.com/docker/cli from `29.5.1+incompatible` to `29.5.2+incompatible` by @dependabot[bot] in https://github.com/docker/compose/pull/13802
* Update to go `1.26.4` by @thaJeztah in https://github.com/docker/compose/pull/13828
* Chore(deps): github.com/containerd/typeurl/v2 `v2.3.0` by @thaJeztah in https://github.com/docker/compose/pull/13829
* Build(deps): bump golang.org/x/sync from `0.20.0` to `0.21.0` by @dependabot[bot] in https://github.com/docker/compose/pull/13838
* Chore(deps): github.com/docker/cli `v29.5.3`, github.com/docker/buildx `v0.34.1`, buildkit `v0.30.0` by @thaJeztah in https://github.com/docker/compose/pull/13841
* Build(deps): bump golang.org/x/sys from `0.45.0` to `0.46.0` by @dependabot[bot] in https://github.com/docker/compose/pull/13832
* Chore(deps): golang.org/x/crypto `v0.53.0` by @thaJeztah in https://github.com/docker/compose/pull/13844
* Build(deps): bump github.com/containerd/containerd/v2 from `2.2.3` to `2.2.4` in the go_modules group across 1 directory by @dependabot[bot] in https://github.com/docker/compose/pull/13804
* Chore(deps): bump github.com/containerd/containerd/v2 to `v2.2.5` by @thaJeztah in https://github.com/docker/compose/pull/13855
* Chore(deps): bump github.com/golang-jwt/jwt/v5 to `v5.3.1` by @thaJeztah in https://github.com/docker/compose/pull/13847
* Chore(deps): github.com/docker/cli `v29.6.0`, github.com/docker/buildx `v0.35.0`, buildkit `v0.31.0` by @thaJeztah in https://github.com/docker/compose/pull/13842
* Bump compose-go to version `v2.12.1` by @glours in https://github.com/docker/compose/pull/13865


## New Contributors
* @securityeng-bot[bot] made their first contribution in https://github.com/docker/compose/pull/13820
* @caltechustc made their first contribution in https://github.com/docker/compose/pull/13810
* @solunolab made their first contribution in https://github.com/docker/compose/pull/13823
* @scarab-systems made their first contribution in https://github.com/docker/compose/pull/13831
* @ptrdom made their first contribution in https://github.com/docker/compose/pull/13825
* @rajyan made their first contribution in https://github.com/docker/compose/pull/13742
* @Ijtihed made their first contribution in https://github.com/docker/compose/pull/13848

**Full Changelog**: https://github.com/docker/compose/compare/v5.1.4...v5.2.0

## v5.1.4

_2026-05-20 · tag `v5.1.4`_

## What's Changed

### ✨ Improvements
* feat: add stop lifecycle hook for external providers by @glours in https://github.com/docker/compose/pull/13779

### 🐛 Fixes
* fix: route OCI artifact pulls through Docker Desktop HTTP proxy by @glours in https://github.com/docker/compose/pull/13770
* fix: restore stoppingEvent/stoppedEvent helpers for plugin stop hook by @glours in https://github.com/docker/compose/pull/13794
* fix(publish): flag literal inline environment values by @glours in https://github.com/docker/compose/pull/13760

### 🔧  Internal
* ci: remove unused e2e job from merge workflow by @glours in https://github.com/docker/compose/pull/13740
* chore: update cagent-action to `v1.4.4` by @derekmisler in https://github.com/docker/compose/pull/13745
* Change verb tense in Docker Compose reference documentation by @ryanjbonnell in https://github.com/docker/compose/pull/13773
* pkg/compose: go fix by @thaJeztah in https://github.com/docker/compose/pull/13782
* refactor: code deduplication and simplification by @ndeloof in https://github.com/docker/compose/pull/13759
* fix: make e2e tests pass reliably locally with Docker Desktop by @glours in https://github.com/docker/compose/pull/13741
* refactor: drop Desktop beta-settings check; gate hint on LogsTab flag by @glours in https://github.com/docker/compose/pull/13755

### ⚙️ Dependencies


* build(deps): bump github.com/mattn/go-shellwords from `1.0.12` to `1.0.13` by @dependabot[bot] in https://github.com/docker/compose/pull/13731
* build(deps): bump github.com/docker/cli from `29.4.0+incompatible` to `29.4.2+incompatible` by @dependabot[bot] in https://github.com/docker/compose/pull/13768
* build(deps): bump github.com/moby/moby/client from `0.4.0` to `0.4.1` by @dependabot[bot] in https://github.com/docker/compose/pull/13752
* build(deps): bump github.com/docker/cli from `29.4.2+incompatible` to `29.4.3+incompatible` by @dependabot[bot] in https://github.com/docker/compose/pull/13776
* build(deps): bump google.golang.org/grpc from `1.80.0` to `1.81.0` by @dependabot[bot] in https://github.com/docker/compose/pull/13775
* build(deps):  update to `go 1.26.3` by @thaJeztah in https://github.com/docker/compose/pull/13783
* build(deps): bump google.golang.org/grpc from `1.81.0` to `1.81.1` by @dependabot[bot] in https://github.com/docker/compose/pull/13791
* build(deps): bump github.com/compose-spec/compose-go/v2 from `2.10.2` to `2.11.0` by @dependabot[bot] in https://github.com/docker/compose/pull/13798
* build(deps): bump github.com/docker/cli from `29.4.3+incompatible` to `29.5.1+incompatible` by @dependabot[bot] in https://github.com/docker/compose/pull/13796
* build(deps): bump golang.org/x/sys from `0.42.0` to `0.44.0` by @dependabot[bot] in https://github.com/docker/compose/pull/13788

## New Contributors
* @ryanjbonnell made their first contribution in https://github.com/docker/compose/pull/13773

**Full Changelog**: https://github.com/docker/compose/compare/v5.1.3...v5.1.4

## v5.1.3

_2026-04-15 · tag `v5.1.3`_

## What's Changed
### 🐛 Fixes
* fix: provider output handling and watch rebuild re-invocation by @glours in https://github.com/docker/compose/pull/13732

### 🔧  Internal
* Add Docker Desktop Logs view hints and navigation shortcut by @glours in https://github.com/docker/compose/pull/13721
* Build and push Docker Desktop module image on release by @glours in https://github.com/docker/compose/pull/13726
* Fix typo in SECURITY.md by @glours in https://github.com/docker/compose/pull/13730
* Make hook hint deep links clickable using OSC 8 terminal hyperlinks by @glours in https://github.com/docker/compose/pull/13734
* Remove 'provenance' attribute' by @glours in https://github.com/docker/compose/pull/13738

### ⚙️ Dependencies
* build(deps): bump github.com/containerd/containerd/v2 from 2.2.2 to 2.2.3 by @dependabot[bot] in https://github.com/docker/compose/pull/13737



**Full Changelog**: https://github.com/docker/compose/compare/v5.1.2...v5.1.3

## v5.1.2

_2026-04-09 · tag `v5.1.2`_

## What's Changed
### 🐛 Fixes
* Fix TTY timer rendering when duration length changes by @MaybeSam05 in https://github.com/docker/compose/pull/13634
* Fix up attach filtering by @false200 in https://github.com/docker/compose/pull/13664
* Preserve ssh:// URL scheme when resolving Dockerfile path by @ssam18 in https://github.com/docker/compose/pull/13669
* Initialize and pass envFiles map in processExtends by @Mohamed-Moumni in https://github.com/docker/compose/pull/13678
* Fix TestRunHook_ConsoleSize on macOS by @thaJeztah in https://github.com/docker/compose/pull/13686
* Restore post-connect fallback for multi-network stacks on API < 1.44 by @jotka in https://github.com/docker/compose/pull/13629
* Publish: return api.ErrCanceled when user declines interactive prompts by @ishwar170695 in https://github.com/docker/compose/pull/13674
* Return error on non-ErrNotExist stat failures in Tar.Sync() by @Lidang-Jiang in https://github.com/docker/compose/pull/13684

### 🔧  Internal
* Refactor: thread context through publish sensitive data check by @ishwar170695 in https://github.com/docker/compose/pull/13653
* Add AI-powered PR review workflow via `docker/cagent-action` by @glours in https://github.com/docker/compose/pull/13659
* Update `cagent-action` to latest (with better permissions) by @derekmisler in https://github.com/docker/compose/pull/13665
* Pin GitHub Actions to commit SHA, remove pr-review workflow by @glours in https://github.com/docker/compose/pull/13662
* Exclude hook_test.go from Windows builds and propagate ExecStart error in runWaitExec by @pawannn in https://github.com/docker/compose/pull/13683
* Skip PR review workflow for Dependabot PRs by @glours in https://github.com/docker/compose/pull/13679
* Use negotiated API version for network setup by @glours in https://github.com/docker/compose/pull/13690
* Fix mixed assertion libraries in tests by @thaJeztah in https://github.com/docker/compose/pull/13689
* Test: use random host port for dind TLS build test by @ricardobranco777 in https://github.com/docker/compose/pull/13630
* Remove direct dependency on `docker/docker` by @glours in https://github.com/docker/compose/pull/13706

### ⚙️ Dependencies
* Bump github.com/containerd/platforms from `1.0.0-rc.2` to `1.0.0-rc.3` by @dependabot[bot] in https://github.com/docker/compose/pull/13657
* Bump golangci-lint to `v2.11.3` and configure CLAUDE to use it on change by @ndeloof in https://github.com/docker/compose/pull/13656
* Bump google.golang.org/grpc from `1.78.0` to `1.79.3` by @dependabot[bot] in https://github.com/docker/compose/pull/13642
* Bump github.com/moby/patternmatcher from `0.6.0` to `0.6.1` by @dependabot[bot] in https://github.com/docker/compose/pull/13667
* Bump go.opentelemetry.io/otel/sdk from `1.39.0` to `1.42.0` by @glours in https://github.com/docker/compose/pull/13663
* Bump github.com/docker/cli from `29.2.1+incompatible` to `29.3.1+incompatible` by @dependabot[bot] in https://github.com/docker/compose/pull/13670
* Bump github.com/hashicorp/go-version from `1.8.0` to `1.9.0` by @dependabot[bot] in https://github.com/docker/compose/pull/13692
* Bump github.com/docker/buildx `v0.33.0`, buildkit `v0.29.0` by @thaJeztah in https://github.com/docker/compose/pull/13693
* Bump google.golang.org/grpc from `1.79.3` to `1.80.0` by @dependabot[bot] in https://github.com/docker/compose/pull/13697
* Bump github.com/containerd/platforms from `1.0.0-rc.3` to `1.0.0-rc.4` by @dependabot[bot] in https://github.com/docker/compose/pull/13696
* Bump github.com/moby/moby/client `v0.4.0`, moby/api `v1.54.1` by @thaJeztah in https://github.com/docker/compose/pull/13708
* Bump github.com/docker/cli `v29.4.0` by @thaJeztah in https://github.com/docker/compose/pull/13707
* Bump compose-go to version `v2.10.2` by @glours in https://github.com/docker/compose/pull/13705
* Bump to Go `1.25.9` by @thaJeztah in https://github.com/docker/compose/pull/13720

## New Contributors
* @MaybeSam05 made their first contribution in https://github.com/docker/compose/pull/13634
* @ishwar170695 made their first contribution in https://github.com/docker/compose/pull/13653
* @derekmisler made their first contribution in https://github.com/docker/compose/pull/13665
* @false200 made their first contribution in https://github.com/docker/compose/pull/13664
* @ssam18 made their first contribution in https://github.com/docker/compose/pull/13669
* @Mohamed-Moumni made their first contribution in https://github.com/docker/compose/pull/13678
* @pawannn made their first contribution in https://github.com/docker/compose/pull/13683
* @jotka made their first contribution in https://github.com/docker/compose/pull/13629
* @Lidang-Jiang made their first contribution in https://github.com/docker/compose/pull/13684

**Full Changelog**: https://github.com/docker/compose/compare/v5.1.1...v5.1.2

## v5.1.1

_2026-03-20 · tag `v5.1.1`_

## What's Changed

### 🐛 Fixes
* Only pass ConsoleSize to ExecAttach when TTY is enabled by @mikesir87 in https://github.com/docker/compose/pull/13616
* Fix deadlock in ttyWriter.Done() by @maks2134 in https://github.com/docker/compose/pull/13640

### ⚙️ Dependencies
* update to go1.25.8 by @thaJeztah in https://github.com/docker/compose/pull/13622
* bump github.com/moby/moby/api from 1.53.0 to 1.54.0 by @dependabot[bot] in https://github.com/docker/compose/pull/13619
* bump golang.org/x/sys from 0.41.0 to 0.42.0 by @dependabot[bot] in https://github.com/docker/compose/pull/13626
* bump github.com/containerd/containerd/v2 from 2.2.1 to 2.2.2 by @dependabot[bot] in https://github.com/docker/compose/pull/13631
* bump golang.org/x/sync from 0.19.0 to 0.20.0 by @dependabot[bot] in https://github.com/docker/compose/pull/13627
* bump github.com/moby/moby/client from 0.2.2 to 0.3.0 by @dependabot[bot] in https://github.com/docker/compose/pull/13621

## New Contributors
* @maks2134 made their first contribution in https://github.com/docker/compose/pull/13640

**Full Changelog**: https://github.com/docker/compose/compare/v5.1.0...v5.1.1

## v5.1.0

_2026-02-24 · tag `v5.1.0`_

## What's Changed

### 🐛 Fixes
* emit container status events after network reconnection (fixes #13524) by @MaheshThakur9152 in https://github.com/docker/compose/pull/13529
* Fix potential nil pointer dereference in container event monitoring by @Nepomuk5665 in https://github.com/docker/compose/pull/13551
* compose: recreate container when mounted image digest changes by @ibrahimypr in https://github.com/docker/compose/pull/13549
* fix panic by @ndeloof in https://github.com/docker/compose/pull/13562
* Fix invalid path error when using OCI artifacts on Windows by @mikesir87 in https://github.com/docker/compose/pull/13574
* fix: execute post_start hooks in docker compose run by @veeceey in https://github.com/docker/compose/pull/13607
* Fix panic when watch rebuilds without up by @maxproske in https://github.com/docker/compose/pull/13610

### 🔧  Internal
* fsnotify is set in Dockerfile by @ndeloof in https://github.com/docker/compose/pull/13533
* Dockerfile: update golangci-lint to v2.8.0 by @thaJeztah in https://github.com/docker/compose/pull/13535
* replace some uses of strings.Split(N) for strings.Cut by @thaJeztah in https://github.com/docker/compose/pull/13542
* Upgrade GitHub Actions to latest versions by @salmanmkc in https://github.com/docker/compose/pull/13546
* pkg/compose: remove dependency on github.com/docker/buildx/driver by @thaJeztah in https://github.com/docker/compose/pull/13563
* use Docker GitHub Builder to build and sign binaries and bin image by @crazy-max in https://github.com/docker/compose/pull/13568
* ci: fix bin-image job by @crazy-max in https://github.com/docker/compose/pull/13569
* pkg/compose: defaultNetworkSettings: refactor by @thaJeztah in https://github.com/docker/compose/pull/13580
* pkg/compose: un-export consts by @thaJeztah in https://github.com/docker/compose/pull/13584
* modernize some code by @thaJeztah in https://github.com/docker/compose/pull/13588

### ⚙️ Dependencies
* update to go1.25.7 by @thaJeztah in https://github.com/docker/compose/pull/13573
* build(deps): bump golang.org/x/sys from 0.40.0 to 0.41.0 by @dependabot[bot] in https://github.com/docker/compose/pull/13578
* build(deps): bump go.yaml.in/yaml/v4 from 4.0.0-rc.3 to 4.0.0-rc.4 by @dependabot[bot] in https://github.com/docker/compose/pull/13541
* migrate to moby modules by @thaJeztah in https://github.com/docker/compose/pull/13078

## New Contributors
* @MaheshThakur9152 made their first contribution in https://github.com/docker/compose/pull/13529
* @salmanmkc made their first contribution in https://github.com/docker/compose/pull/13546
* @Nepomuk5665 made their first contribution in https://github.com/docker/compose/pull/13551
* @ibrahimypr made their first contribution in https://github.com/docker/compose/pull/13549
* @veeceey made their first contribution in https://github.com/docker/compose/pull/13607

**Full Changelog**: https://github.com/docker/compose/compare/v5.0.2...v5.1.0

## v5.0.2

_2026-01-21 · tag `v5.0.2`_

## What's Changed

### 🐛 Fixes
* Fixed progress UI to adapt to terminal width by @ndeloof in https://github.com/docker/compose/pull/13519
* Removed warning when no explicit build has been requested. by @ndeloof in https://github.com/docker/compose/pull/13493
* Restored `runtime_flags` support in `models` by @ilopezluna in https://github.com/docker/compose/pull/13460
* Added service name completion to `down` command by @bmo-at in https://github.com/docker/compose/pull/13470
* Fixed tilde in `--env-file` paths expanded to user home directory by @tensorworkerr in https://github.com/docker/compose/pull/13510
* Handle `healthcheck.disable: true` by @stavros-k in https://github.com/docker/compose/pull/13494
* Fixed shutdown and error handling for large file change batches in `watch` by @amyssnippet in https://github.com/docker/compose/pull/13525


### 🔧  Internal
* Added unit test for upOptions.OnExit method by @htoyoda18 in https://github.com/docker/compose/pull/13489
* clean up temporary compose files after conversion by @htoyoda18 in https://github.com/docker/compose/pull/13483
* Fixed typo in isSwarmEnabled method name by @htoyoda18 in https://github.com/docker/compose/pull/13481
* Fixed incorrect usage of errgroup.WithContext by @htoyoda18 in https://github.com/docker/compose/pull/13480
* Fixed timeout initialization when waitTimeout is zero by @htoyoda18 in https://github.com/docker/compose/pull/13471
* Extracted API version constants to dedicated file by @htoyoda18 in https://github.com/docker/compose/pull/13503
* Replace tabbed indentation in sdk.md by @pkqk in https://github.com/docker/compose/pull/13505
* Improved attach error handling and cleanup by @htoyoda18 in https://github.com/docker/compose/pull/13488
* Modernize tests by @dgageot in https://github.com/docker/compose/pull/13531
* set fsnotify build tag when building for OSX by @ndeloof in https://github.com/docker/compose/pull/13532

### ⚙️ Dependencies
* build(deps): bump github.com/klauspost/compress to v1.18.2 by @thaJeztah in https://github.com/docker/compose/pull/13499
* go.mod: remove exclude rules by @thaJeztah in https://github.com/docker/compose/pull/13498
* build(deps): bump github.com/containerd/containerd/v2 to v2.2.1 by @thaJeztah in https://github.com/docker/compose/pull/13497
* build(deps): bump golang.org/x/sys from 0.39.0 to 0.40.0 by @dependabot[bot] in https://github.com/docker/compose/pull/13502
* build(deps): bump google.golang.org/grpc from 1.77.0 to 1.78.0 by @dependabot[bot] in https://github.com/docker/compose/pull/13475
* build(deps): bump github.com/go-viper/mapstructure/v2 from 2.4.0 to 2.5.0 by @dependabot[bot] in https://github.com/docker/compose/pull/13506
* build(deps): bump github.com/sirupsen/logrus v1.9.4 by @thaJeztah in https://github.com/docker/compose/pull/13518
* Bump compose to v2.10.1 by @ndeloof in https://github.com/docker/compose/pull/13528

## New Contributors
* @bmo-at made their first contribution in https://github.com/docker/compose/pull/13470
* @pkqk made their first contribution in https://github.com/docker/compose/pull/13505
* @tensorworkerr made their first contribution in https://github.com/docker/compose/pull/13510
* @stavros-k made their first contribution in https://github.com/docker/compose/pull/13494
* @amyssnippet made their first contribution in https://github.com/docker/compose/pull/13525
* @dgageot made their first contribution in https://github.com/docker/compose/pull/13531

**Full Changelog**: https://github.com/docker/compose/compare/v5.0.1...v5.0.2

## v5.0.1

_2025-12-18 · tag `v5.0.1`_

## What's Changed

### 🐛 Fixes
* Restored support for `COMPOSE_COMPATIBILITY` by @ndeloof in https://github.com/docker/compose/pull/13424
* Fixed grammatical errors and improve clarity in code. by @xiaolinny in https://github.com/docker/compose/pull/13429
* Fixed broken `run --quiet`. by @ndeloof in https://github.com/docker/compose/pull/13430
* Fixed SDK example by @ndeloof in https://github.com/docker/compose/pull/13416
* Added a check buildx version is set before comparing it. by @yangfeiyu20102011 in https://github.com/docker/compose/pull/13415
* Fixed grammar: pluralize 'service' and remove apostrophes in lets. by @rashmivagha in https://github.com/docker/compose/pull/13423
* Fixed progress UI not restoring terminal once operation completes. by @ndeloof in https://github.com/docker/compose/pull/13439
* Fixed status alignment in progress UI. by @ndeloof in https://github.com/docker/compose/pull/13438
* Restored image layer download progress details on pull. by @ndeloof in https://github.com/docker/compose/pull/13445
* Added 'configured' event at the end of model configuration phase. by @glours in https://github.com/docker/compose/pull/13446
* Introduced a build tag to select watcher implementation. by @ndeloof in https://github.com/docker/compose/pull/13452
* Removed mention for `v2` on README. by @alexislefebvre in https://github.com/docker/compose/pull/13451
* Fixed missing error handling in `setEnvWithDotEnv`. by @htoyoda18 in https://github.com/docker/compose/pull/13450
* Adopted morikuni/aec library over raw ANSI sequences. by @ndeloof in https://github.com/docker/compose/pull/13440
* Prevented incorrect progress metrics to break compose display. by @ndeloof in https://github.com/docker/compose/pull/13457
* Restored support for BUILDKIT_PROGRESS. by @ndeloof in https://github.com/docker/compose/pull/13455
* Added check model plugin is successfully loaded. by @ndeloof in https://github.com/docker/compose/pull/13464
* Added a warning when no service has been selected to build. by @ndeloof in https://github.com/docker/compose/pull/13467

### ⚙️ Dependencies
* Drop Go min patch version by @austinvazquez in https://github.com/docker/compose/pull/13418
* bump golang 1.24.11 by @austinvazquez in https://github.com/docker/compose/pull/13417
* bump osxcross by @ndeloof in https://github.com/docker/compose/pull/13425
* bump golang.org/x/sys from 0.38.0 to 0.39.0 by @dependabot[bot] in https://github.com/docker/compose/pull/13433
* bump github.com/docker/cli-docs-tool from 0.10.0 to 0.11.0 by @dependabot[bot] in https://github.com/docker/compose/pull/13437
* bump golang.org/x/sync from 0.18.0 to 0.19.0 by @dependabot[bot] in https://github.com/docker/compose/pull/13434
* bump tags.cncf.io/container-device-interface from 1.0.1 to 1.1.0 by @dependabot[bot] in https://github.com/docker/compose/pull/13441
* bump github.com/moby/buildkit from 0.26.2 to 0.26.3 by @dependabot[bot] in https://github.com/docker/compose/pull/13462

## New Contributors
* @yangfeiyu20102011 made their first contribution in https://github.com/docker/compose/pull/13415
* @xiaolinny made their first contribution in https://github.com/docker/compose/pull/13429
* @alexislefebvre made their first contribution in https://github.com/docker/compose/pull/13451
* @htoyoda18 made their first contribution in https://github.com/docker/compose/pull/13450

**Full Changelog**: https://github.com/docker/compose/compare/v5.0.0...v5.0.1

## v5.0.0 "Mont Blanc"

_2025-12-02 · tag `v5.0.0`_

![mont blanc](https://github.com/user-attachments/assets/1e6b938e-e67a-4063-b1d0-0f225da01521)

Major changes in this release:
* Compose can now officially be used as a SDK to be integrated into third-party softwares
* Internal builder has been removed, build is delegated to Docker Bake (same as `docker build` command) 

## Why "v5" ?
We decided to skip `3.0.0` for next major release after docker Compose v2 to prevent (more) confusion with the obsolete docker-compose file versions `2.x` and `3.x` inherited from Docker Compose v1. We also skipped `4.0.0` to have a clear separation with this legacy.

## What's Changed

### ✨ Improvements
* drop support for internal buildkit builder by @ndeloof in https://github.com/docker/compose/pull/13056
* Setup Compose service using functional parameters by @ndeloof in https://github.com/docker/compose/pull/13312
* Introduce abstractions to support SDK usage without requiring Docker CLI by @glours in https://github.com/docker/compose/pull/13313
* configure Compose service with io.Reader and io.Writer by @glours in https://github.com/docker/compose/pull/13322
* Make progress Writer a CLI component by @ndeloof in https://github.com/docker/compose/pull/13316
* SDK docs by @ndeloof in https://github.com/docker/compose/pull/13350
* document support for OCI and Git remote resources by @ndeloof in https://github.com/docker/compose/pull/13362
* run hooks on restart by @ndeloof in https://github.com/docker/compose/pull/13321
* fix(run): Ensure images exist only for the target service in run command by @idsulik in https://github.com/docker/compose/pull/13325
* Add load project to api definition by @glours in https://github.com/docker/compose/pull/13329
* introduce --insecure-registry, reserved for testing purpose by @ndeloof in https://github.com/docker/compose/pull/13355
* Move progress package to cmd as a command line component by @ndeloof in https://github.com/docker/compose/pull/13357
* Added support for `build.no_cache_filter` by @ndeloof in https://github.com/docker/compose/pull/13377
* add --wait option to start command by @ndeloof in https://github.com/docker/compose/pull/13409

### 🐛 Fixes
* fix OCI compose override support by @ndeloof in https://github.com/docker/compose/pull/13311
* Fix help output for "exec --no-tty" option by @tonyo in https://github.com/docker/compose/pull/13314
* fix typo in error message by @stasadev in https://github.com/docker/compose/pull/13328
* disable progress UI when build is ran with --print by @ndeloof in https://github.com/docker/compose/pull/13351
* add (restore) support for detach keys by @ndeloof in https://github.com/docker/compose/pull/13369
* images command should display image Created time or N/A if not available by @ndeloof in https://github.com/docker/compose/pull/13376
* Fix support for port range by @ndeloof in https://github.com/docker/compose/pull/13381
* skip includes preparing publish by @ndeloof in https://github.com/docker/compose/pull/13400
* feat(model): ignore runtime flags in model configuration by @ilopezluna in https://github.com/docker/compose/pull/13404

### 🔧  Internal
* Next release will be major version v5.x by @ndeloof in https://github.com/docker/compose/pull/13375
* Test to check writeComposeFile detects invalid OCI artifact by @ndeloof in https://github.com/docker/compose/pull/13309
* Code Cleanup by @ndeloof in https://github.com/docker/compose/pull/13315
* fix various linting issues by @thaJeztah in https://github.com/docker/compose/pull/13326
* Making the American/British spellings consistent to the error messages by @JLesDev in https://github.com/docker/compose/pull/13366
* gha: test against docker v29, v28, and rename checks to use `stable`, `oldstable` by @thaJeztah in https://github.com/docker/compose/pull/13380
* refactor: replace Split in loops with more efficient SplitSeq by @vicerace in https://github.com/docker/compose/pull/13393
* refactor: use strings.Builder to improve performance by @liuyueyangxmu in https://github.com/docker/compose/pull/13398
* Fix grammar: change 'adopted' to 'adopt' in Docker Swarm note by @rashmivagha in https://github.com/docker/compose/pull/13407
* golangci-lint: use gci formatter instead of goimports by @thaJeztah in https://github.com/docker/compose/pull/13406
* refactor: replace interface{} with any for clarity and modernization by @zjumathcode in https://github.com/docker/compose/pull/13411

### ⚙️ Dependencies
* Bump compose go to v2.10.0 by @ndeloof in https://github.com/docker/compose/pull/13410
* build(deps): bump github.com/containerd/platforms from 1.0.0-rc.1 to 1.0.0-rc.2 by @dependabot[bot] in https://github.com/docker/compose/pull/13353
* build(deps): bump github.com/docker/docker from 28.5.1+incompatible to 28.5.2+incompatible by @dependabot[bot] in https://github.com/docker/compose/pull/13361
* build(deps): bump github.com/containerd/containerd/v2 from 2.1.4 to 2.2.0 by @dependabot[bot] in https://github.com/docker/compose/pull/13358
* build(deps): bump github.com/docker/cli from 28.5.1+incompatible to 28.5.2+incompatible by @dependabot[bot] in https://github.com/docker/compose/pull/13360
* build(deps): bump golang.org/x/sys from 0.37.0 to 0.38.0 by @dependabot[bot] in https://github.com/docker/compose/pull/13367
* build(deps): bump golang.org/x/sync from 0.17.0 to 0.18.0 by @dependabot[bot] in https://github.com/docker/compose/pull/13368
* Dockerfile: update golangci-lint to v2.6.2 by @thaJeztah in https://github.com/docker/compose/pull/13370
* build(deps): bump buildx v0.30.0, buildkit v0.26.0, otel v1.38.0, otel/contrib v0.63.0 by @thaJeztah in https://github.com/docker/compose/pull/13379
* bump dependencies by @ndeloof in https://github.com/docker/compose/pull/13392
* build(deps): bump github.com/hashicorp/go-version from 1.7.0 to 1.8.0 by @dependabot[bot] in https://github.com/docker/compose/pull/13403
* build(deps): bump golang.org/x/crypto v0.45.0 by @thaJeztah in https://github.com/docker/compose/pull/13405

## New Contributors
* @tonyo made their first contribution in https://github.com/docker/compose/pull/13314
* @stasadev made their first contribution in https://github.com/docker/compose/pull/13328
* @JLesDev made their first contribution in https://github.com/docker/compose/pull/13366
* @vicerace made their first contribution in https://github.com/docker/compose/pull/13393
* @liuyueyangxmu made their first contribution in https://github.com/docker/compose/pull/13398
* @ilopezluna made their first contribution in https://github.com/docker/compose/pull/13404
* @rashmivagha made their first contribution in https://github.com/docker/compose/pull/13407
* @zjumathcode made their first contribution in https://github.com/docker/compose/pull/13411

**Full Changelog**: https://github.com/docker/compose/compare/v2.40.2...v5.0.0
