---
title: "CLI release notes"
source: https://docs.docker.com/scout/release-notes/cli/
---

# CLI release notes

The latest Docker Scout CLI releases. From the GitHub releases of [docker/scout-cli](https://github.com/docker/scout-cli/releases), which is where this page links on docs.docker.com.

## v1.29.0

_2026-10-28 · tag `v1.29.0`_

## What's Changed

- Fixes duplicate or inconsistent Debian, Alpine, and Docker Hardened Images package identities when installed package records and embedded SBOMs describe the same package, while preserving package and file evidence. [@brianru](https://github.com/brianru)
- Fixes local policy evaluation ignoring Docker Desktop and `HTTP_PROXY`/`HTTPS_PROXY` settings for registry requests, which could cause policies to report "No data" on networks that require a proxy. [@flyingmachine](https://github.com/flyingmachine)
- Preserves provenance and SBOM attestations for local images when an older cached SBOM lacks those attestations, including entries created by Docker Desktop's background image indexer. [@flyingmachine](https://github.com/flyingmachine)
- Fixes a crash when exporting OpenVEX with `docker scout vex get` or `docker scout attest get` for an image referenced by digest without a tag. [@andrestylianos](https://github.com/andrestylianos)
- Fixes SBOM generation failures caused by Maven Central rate limits when scanning images or directories containing `pom.xml` files. Scout no longer resolves those files against remote Maven repositories during indexing. [@astokes-docker](https://github.com/astokes-docker)
- Updates the compression dependency to version 1.18.7 to address CVE-2026-63209. [@brianru](https://github.com/brianru)

### SBOM compatibility

Generated Debian and Alpine binary package URLs now retain architecture and source-package qualifiers, including when no embedded SBOM is present. Existing generated SBOM caches are refreshed automatically. No new flag is required. Imported SBOMs and SBOM attestations retain their producer's identities.

## v1.28.0

_2026-10-27 · tag `v1.28.0`_

## What's Changed

- Updates the Brotli decoder to 1.2.7 to incorporate security fixes. [@brianru](https://github.com/brianru)
- Updates HTTP/2 dependencies to incorporate security fixes. [@brianru](https://github.com/brianru)
- Fixes missing Debian vulnerability findings in Distroless images by correctly identifying their operating system version. [@brianru](https://github.com/brianru)

## v1.27.0

_2026-10-21 · tag `v1.27.0`_

## What's Changed

- Updates the Go toolchain to 1.26.10 to incorporate security fixes. [@thaJeztah](https://github.com/thaJeztah)

## v1.26.0

_2026-09-30 · tag `v1.26.0`_

## What's Changed

- Fixes `docker scout watch` failing with `401 Unauthorized` about 15 minutes after it starts. The Docker token is now refreshed before it expires, and an image that fails to process no longer stops the watcher; it is retried on the next check. [@aubm](https://github.com/aubm)
- Fixes `docker scout attest list` and `docker scout attest get` so they find attestations attached as OCI referrers on Docker Hub and other registries. Previously only attestations served by the Scout registry were listed. [@benja-M-1](https://github.com/benja-M-1)
- Fixes `docker scout quickview` showing VEX-suppressed CVEs in the Target row when VEX suppresses every CVE in the image. [@whostolebenfrog](https://github.com/whostolebenfrog)
- Fixes DHI base-image VEX statements not being applied to multistage builds that use a mirrored DHI base image (`<org>/dhi-<name>` naming). [@flyingmachine](https://github.com/flyingmachine)
- Fixes CycloneDX SBOM output to keep the original creation timestamp and generator tool names and versions. [@brianru](https://github.com/brianru)
- Updates the embedded Trivy (0.72.0) and Syft (1.46.0) scanning engines. [@brianru](https://github.com/brianru)

## v1.25.0

_2026-09-30 · tag `v1.25.0`_

## What's Changed

- Adds discovery of software inside Debian and Alpine package archives, preserving package containment and separate package occurrences in SPDX SBOMs. Archive scanning is enabled by default and can be disabled with `SCOUT_SBOM_EXPAND_ARCHIVES=false`. [@brianru](https://github.com/brianru)
- Fixes manual vulnerability exception handling so image scans correctly mark suppressed vulnerabilities and filter them with `--ignore-suppressed`, while reducing network requests. [@whostolebenfrog](https://github.com/whostolebenfrog)
- Moves exception details in `--format sbom` output from the top-level inventory to each vulnerability’s `exceptions` array. Consumers counting manual suppressions must filter for `MANUAL_EXCEPTION`. [@whostolebenfrog](https://github.com/whostolebenfrog)
- Adds warnings when manual exceptions cannot be applied in local mode or when loading older native SBOMs with legacy exception inventories. Older SBOMs require rescanning to restore manual-exception suppression. [@whostolebenfrog](https://github.com/whostolebenfrog)
- Updates the native Scout SBOM format to version 12 to support the expanded package inventory and SPDX relationships. [@brianru](https://github.com/brianru)

## v1.24.0

_2026-07-30 · tag `v1.24.0`_

## What's Changed

- Adds local Scout Health Scores to `docker scout policy`, `quickview`, and `compare`. [@cdupuis](https://github.com/cdupuis)
- Fixes `docker scout cves --only-base` and `--ignore-base` to correctly classify packages from provenance-identified base images. [@andrestylianos](https://github.com/andrestylianos)
- Updates dependencies, including ORAS, Sigstore, OpenTelemetry, go-git, and pgx.

## v1.23.1

_2026-07-04 · tag `v1.23.1`_

## What's Changed

- Fixes policy evaluation when using custom Rego policies without details metadata [@whostolebenfrog](https://github.com/whostolebenfrog)

## v1.23.0

_2026-07-02 · tag `v1.23.0`_

## What's Changed

- Prevents empty VEX documents from breaking scanning [@flyingmachine](https://github.com/flyingmachine)
- Rego policy sources can be served via http(s) through --policy-file [@cdupuis](https://github.com/cdupuis)
- Performance improvements on SBOM fetching and policies evaluation [@cdupuis](https://github.com/cdupuis)
