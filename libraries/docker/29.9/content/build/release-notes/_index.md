---
title: "Build release notes"
source: https://docs.docker.com/build/release-notes/
---

# Build release notes

Buildx releases v0.36 and later. From the GitHub releases of [docker/buildx](https://github.com/docker/buildx/releases), which is where this page links on docs.docker.com.

## v0.38.2

_2026-11-03 · tag `v0.38.2`_

Welcome to the v0.38.2 release of buildx!



Please try out the release binaries and report any issues at
https://github.com/docker/buildx/issues.

### Contributors

* CrazyMax
* Tõnis Tiigi
* Sebastiaan van Stijn

### Notable Changes

- Fix Bake filesystem entitlement checks when building multiple targets together so paths from every target are checked against the approved entitlements. https://github.com/docker/buildx/security/advisories/GHSA-xg6v-cv2h-2w5h
- Fix Bake filesystem entitlement path boundaries so paths under the same parent directory that share the current working directory's basename prefix cannot bypass `fs.read` approval. https://github.com/docker/buildx/security/advisories/GHSA-rghq-x9hf-hc3r

### Dependency Changes

* **github.com/containerd/containerd/v2**  v2.4.1 -> v2.4.2
* **github.com/klauspost/compress**        v1.20.1 -> v1.20.2
* **github.com/moby/buildkit**             v0.34.0 -> v0.34.2
* **github.com/tonistiigi/fsutil**         83cac42c1c52 -> a72de9dcf763
* **go.yaml.in/yaml/v3**                   v3.0.5 -> v3.0.6

Previous release can be found at [v0.38.1](https://github.com/docker/buildx/releases/tag/v0.38.1)

## v0.38.1

_2026-10-20 · tag `v0.38.1`_

buildx 0.38.1

Welcome to the v0.38.1 release of buildx!



Please try out the release binaries and report any issues at
https://github.com/docker/buildx/issues.

### Security

This release has been built with updated Go runtime 1.26.10 to address [CVE-2026-111943](https://go.dev/issue/82345) by rejecting certificate chains that include eight revoked eMudhra intermediate certificates.
Image pulls and pushes fail TLS certificate verification if a registry's certificate chain relies on one of the affected TLS intermediates.
Affected registries need a replacement certificate chain that does not use these intermediates.

The blocked intermediates are:

- Domain-validated TLS: `EM DV TLS CA - G3B` and `EM DV TLS CA - G3C`
- Organization-validated TLS: `EM OV TLS CA - G3B` and `EM OV TLS CA - G3C`
- Extended-validation TLS: `EM EV TLS CA - G3B` and `EM EV TLS CA - G3C`
- Code signing: `EM OV CS CA - G3B` and `EM OV CS CA - G3C`

The G3B intermediates belong to eMudhra BV, and the G3C intermediates belong to eMudhra Inc.
The keys for these intermediates were compromised.

[Read more about the eMudhra Intermediate CA Compromise](https://emudhra.we-have-a-problem.com/)

There are no functional changes in Buildx itself compared to the previous release.



Previous release can be found at [v0.38.0](https://github.com/docker/buildx/releases/tag/v0.38.0)

## v0.38.0

_2026-10-07 · tag `v0.38.0`_

buildx 0.38.0

Welcome to the v0.38.0 release of buildx!



Please try out the release binaries and report any issues at
https://github.com/docker/buildx/issues.

### Contributors

* CrazyMax
* Tõnis Tiigi
* Sebastiaan van Stijn
* Akihiro Suda
* Tomas Perez Molina
* Dean Chen
* MohammadHasan Akbari
* Nicolas De Loof
* Ricardo Branco
* Ryan Bonnell

### Notable Changes

- Bake now supports configuring job execution modes and parallelization limits with `--jobs/-j` flag. New execution modes include `defer-error` to delay cancellation of failed jobs and `defer-output` to wait for all jobs to complete before exporting results. #4044
- New experiment command `docker buildx replay build` allows rebuilding historical builds based on recorded provenance of a distributed artifact or Docker image. This subcommand is expected to be updated with additional features and improvements in future releases. #4122 #3818
- HTTP hosts passed to build policies are now normalized to assist writing accurate policy rules. #4068
- Bake `--set` overrides have now been updated to use singular keys for better consistency and clarity. #4089
- Bake `--set` overrides now support clearing array values with an empty parameter. #4107
- Git advice output can now be controlled with `BUILDKIT_GIT_ADVICE` and `BUILDX_BAKE_GIT_ADVICE`. #4103
- Compose support has been updated to v2.16.1 #4118
- Zstd compressed archives can now be passed as build context. #4104
- Update Kubernetes driver to handle AppArmor profile correctly. #4083
- Improve Kubernetes driver dial retry backoff logic. #4039
- Fix possible issues with builder feature detection using stale cached data. #4085 #4082
- Fix possible panic from result image loading and progress race. #4064
- Fix possible stale node status printed by `inspect --bootstrap` command. #4048
- Fix confusing error messages when encountering undefined variables in bake targets. #4086
- Fix possible incorrect parsing of bake target overrides. #4088
- Fix possible build error with Kubernetes driver and linked targets. #4073
- Fix issue with Kubernetes driver waiting for connection readiness. #4077


### Dependency Changes

* **github.com/aws/aws-sdk-go-v2**                                                  v1.43.8 -> v1.47.0
* **github.com/aws/aws-sdk-go-v2/config**                                           v1.32.39 -> v1.33.4
* **github.com/aws/aws-sdk-go-v2/credentials**                                      v1.19.38 -> v1.20.4
* **github.com/aws/aws-sdk-go-v2/feature/ec2/imds**                                 v1.18.39 -> v1.20.0
* **github.com/aws/aws-sdk-go-v2/internal/configsources**                           v1.4.39 -> v1.5.3
* **github.com/aws/aws-sdk-go-v2/internal/endpoints/v2**                            v2.7.39 -> v2.8.3
* **github.com/aws/aws-sdk-go-v2/internal/v4a**                                     v1.4.40 -> v1.5.3
* **github.com/aws/aws-sdk-go-v2/service/internal/accept-encoding**                 v1.13.18 -> v1.13.19
* **github.com/aws/aws-sdk-go-v2/service/internal/presigned-url**                   v1.13.39 -> v1.14.3
* **github.com/aws/aws-sdk-go-v2/service/signin**                                   v1.5.8 -> v1.10.0
* **github.com/aws/aws-sdk-go-v2/service/sso**                                      v1.33.8 -> v1.38.0
* **github.com/aws/aws-sdk-go-v2/service/ssooidc**                                  v1.38.8 -> v1.43.0
* **github.com/aws/aws-sdk-go-v2/service/sts**                                      v1.45.8 -> v1.50.0
* **github.com/aws/smithy-go**                                                      v1.27.10 -> v1.28.2
* **github.com/clipperhouse/uax29/v2**                                              v2.2.0 -> v2.6.0
* **github.com/compose-spec/compose-go/v2**                                         v2.14.0 -> v2.16.1
* **github.com/containerd/containerd/api**                                          v1.11.1 -> v1.12.0
* **github.com/containerd/containerd/v2**                                           v2.3.6 -> v2.4.1
* **github.com/containerd/log/otel**                                                v0.1.0 **_new_**
* **github.com/containerd/ttrpc**                                                   v1.2.9 -> v1.2.10
* **github.com/decred/dcrd/dcrec/secp256k1/v4**                                     v4.4.0 -> v4.4.1
* **github.com/docker/cli**                                                         v29.7.2 -> v29.8.2
* **github.com/docker/docker-credential-helpers**                                   v0.9.8 -> v0.9.9
* **github.com/docker/go-connections**                                              v0.7.0 -> v0.8.1
* **github.com/fvbommel/sortorder**                                                 v1.1.0 -> v1.2.0
* **github.com/fxamacker/cbor/v2**                                                  v2.9.0 -> v2.9.4
* **github.com/go-openapi/analysis**                                                v0.25.2 -> v0.25.5
* **github.com/go-openapi/jsonpointer**                                             v0.23.1 -> v1.0.0
* **github.com/go-openapi/jsonreference**                                           v0.21.6 -> v1.0.0
* **github.com/go-openapi/loads**                                                   v0.24.0 -> v0.25.0
* **github.com/go-openapi/runtime**                                                 v0.32.4 -> v0.33.0
* **github.com/go-openapi/spec**                                                    v0.22.6 -> v0.22.9
* **github.com/go-openapi/strfmt**                                                  v0.26.4 -> v0.27.0
* **github.com/go-openapi/swag**                                                    v0.26.1 -> v0.28.0
* **github.com/go-openapi/swag/cmdutils**                                           v0.26.1 -> v0.28.0
* **github.com/go-openapi/swag/conv**                                               v0.27.0 -> v0.28.0
* **github.com/go-openapi/swag/fileutils**                                          v0.26.1 -> v0.28.0
* **github.com/go-openapi/swag/jsonutils**                                          v0.26.1 -> v0.28.0
* **github.com/go-openapi/swag/loading**                                            v0.26.1 -> v0.28.0
* **github.com/go-openapi/swag/mangling**                                           v0.26.1 -> v0.28.0
* **github.com/go-openapi/swag/netutils**                                           v0.26.1 -> v0.28.0
* **github.com/go-openapi/swag/pools**                                              v0.28.0 **_new_**
* **github.com/go-openapi/swag/stringutils**                                        v0.26.1 -> v0.28.0
* **github.com/go-openapi/swag/typeutils**                                          v0.27.0 -> v0.28.0
* **github.com/go-openapi/swag/yamlutils**                                          v0.26.1 -> v0.28.0
* **github.com/go-openapi/validate**                                                v0.26.0 -> v0.26.1
* **github.com/goccy/go-json**                                                      v0.10.5 -> v0.10.6
* **github.com/gofrs/flock**                                                        v0.13.0 -> v0.13.1
* **github.com/grpc-ecosystem/grpc-gateway/v2**                                     v2.29.0 -> v2.30.0
* **github.com/klauspost/compress**                                                 v1.19.2 -> v1.20.1
* **github.com/lestrrat-go/dsig**                                                   v1.0.0 -> v1.2.1
* **github.com/lestrrat-go/httprc/v3**                                              v3.0.2 -> v3.0.5
* **github.com/lestrrat-go/jwx/v3**                                                 v3.0.13 -> v3.1.1
* **github.com/mattn/go-runewidth**                                                 v0.0.23 -> v0.0.29
* **github.com/mattn/go-shellwords**                                                v1.0.12 -> v1.0.13
* **github.com/moby/buildkit**                                                      v0.33.1 -> v0.34.0
* **github.com/moby/moby/api**                                                      v1.55.0 -> v1.56.0
* **github.com/moby/moby/client**                                                   v0.5.0 -> v0.6.0
* **github.com/moby/policy-helpers**                                                dd6c5499c491 -> bd98f4747414
* **github.com/open-policy-agent/opa**                                              v1.14.1 -> v1.19.0
* **github.com/package-url/packageurl-go**                                          v0.1.1 -> v0.1.7
* **github.com/santhosh-tekuri/jsonschema/v6**                                      v6.0.1 -> v6.0.3
* **github.com/valyala/fastjson**                                                   v1.6.7 -> v1.6.10
* **github.com/vektah/gqlparser/v2**                                                v2.5.32 -> v2.5.36
* **go.etcd.io/bbolt**                                                              v1.5.0 **_new_**
* **go.opentelemetry.io/contrib/instrumentation/google.golang.org/grpc/otelgrpc**   v0.70.0 -> v0.71.0
* **go.opentelemetry.io/contrib/instrumentation/net/http/httptrace/otelhttptrace**  v0.70.0 -> v0.71.0
* **go.opentelemetry.io/contrib/instrumentation/net/http/otelhttp**                 v0.70.0 -> v0.71.0
* **go.opentelemetry.io/otel**                                                      v1.45.0 -> v1.46.0
* **go.opentelemetry.io/otel/exporters/otlp/otlpmetric/otlpmetricgrpc**             v1.45.0 -> v1.46.0
* **go.opentelemetry.io/otel/exporters/otlp/otlpmetric/otlpmetrichttp**             v1.45.0 -> v1.46.0
* **go.opentelemetry.io/otel/exporters/otlp/otlptrace**                             v1.45.0 -> v1.46.0
* **go.opentelemetry.io/otel/exporters/otlp/otlptrace/otlptracegrpc**               v1.45.0 -> v1.46.0
* **go.opentelemetry.io/otel/exporters/otlp/otlptrace/otlptracehttp**               v1.45.0 -> v1.46.0
* **go.opentelemetry.io/otel/exporters/stdout/stdouttrace**                         v1.44.0 -> v1.46.0
* **go.opentelemetry.io/otel/metric**                                               v1.45.0 -> v1.46.0
* **go.opentelemetry.io/otel/sdk**                                                  v1.45.0 -> v1.46.0
* **go.opentelemetry.io/otel/sdk/metric**                                           v1.45.0 -> v1.46.0
* **go.opentelemetry.io/otel/trace**                                                v1.45.0 -> v1.46.0
* **google.golang.org/genproto/googleapis/api**                                     6ac0973c030d -> da73d73af1c5
* **google.golang.org/genproto/googleapis/rpc**                                     6ac0973c030d -> da73d73af1c5
* **google.golang.org/grpc**                                                        v1.83.2 -> v1.84.0
* **k8s.io/api**                                                                    v0.36.3 -> v0.37.0
* **k8s.io/apimachinery**                                                           v0.36.3 -> v0.37.0
* **k8s.io/client-go**                                                              v0.36.3 -> v0.37.0
* **k8s.io/kube-openapi**                                                           5883c5ee87b9 -> d427ff9ee9ad
* **k8s.io/streaming**                                                              v0.36.3 -> v0.37.0
* **k8s.io/utils**                                                                  28399d86e0b5 -> be93311217bd
* **sigs.k8s.io/structured-merge-diff/v6**                                          v6.3.3 -> v6.4.2

Previous release can be found at [v0.37.2](https://github.com/docker/buildx/releases/tag/v0.37.2)

## v0.37.2

_2026-09-30 · tag `v0.37.2`_

Welcome to the v0.37.2 release of buildx!



Please try out the release binaries and report any issues at
https://github.com/docker/buildx/issues.

### Contributors

* CrazyMax
* Sebastiaan van Stijn
* Tõnis Tiigi

### Notable Changes

- Bake with `--progress=rawjson` now rejects ungranted entitlements instead of skipping the consent check. Grant the requested privileges explicitly with `--allow`. https://github.com/docker/buildx/security/advisories/GHSA-gwr2-q96m-6682
- Bake now requires `fs.read` approval for secret files selected by an implicit `id` fallback and for local OCI layout named contexts. https://github.com/docker/buildx/security/advisories/GHSA-p54p-jq4x-rc28

### Dependency Changes

* **github.com/containerd/containerd/v2**  v2.3.4 -> v2.3.6
* **github.com/moby/buildkit**             v0.33.0 -> v0.33.1
* **golang.org/x/crypto**                  v0.55.0 -> v0.56.0

Previous release can be found at [v0.37.1](https://github.com/docker/buildx/releases/tag/v0.37.1)

## v0.37.1

_2026-09-11 · tag `v0.37.1`_

Welcome to the v0.37.1 release of buildx!



Please try out the release binaries and report any issues at
https://github.com/docker/buildx/issues.

### Contributors

* CrazyMax
* Tomas Perez Molina
* Tõnis Tiigi

### Notable Changes

- Fix failed multi-node image pushes leaving the requested tag pointing to a partial image. #4058
- Fix newly started container builders not getting a full readiness timeout before first use. #4050
- Fix builder removal cleanup being tied to the status timeout. #4072
- Fix linked Bake targets using the Kubernetes driver losing shared clients before the build completes. #4073

### Dependency Changes

This release has no dependency changes

Previous release can be found at [v0.37.0](https://github.com/docker/buildx/releases/tag/v0.37.0)

## v0.37.0

_2026-09-02 · tag `v0.37.0`_

Welcome to the v0.37.0 release of buildx!



Please try out the release binaries and report any issues at
https://github.com/docker/buildx/issues.

### Contributors

* CrazyMax
* Tõnis Tiigi
* Sebastiaan van Stijn
* Alberto Garcia Hierro
* Brad Davidson
* Guilhem Charles
* Guillaume Lours

### Notable Changes

- Buildx now supports `cloud` driver builder instances to run builds with [Docker Build Cloud](https://docs.docker.com/build-cloud/usage/) service. No custom version of Buildx binary is needed anymore. #4017
- Newly started container builders now wait for BuildKit readiness before first use. #4027
- Policy evaluation now uses Docker CLI registry auth for image metadata. #4046
- Several consistency issues with handling Windows platform identifiers with OS version have been fixed. #4035 #4034 #4008
- Using the Kubernetes driver now skips terminating pods when choosing a pod. #3997
- Avoid creating temporary files on the host to send builder configuration to remote containers. #3996
- Fix issue where Bake builds could sometimes drop sending build secrets when using linked targets. #4014
- Fix cases where empty source policy sessions were created for some builds, possibly causing confusing progress output. #4028

### Dependency Changes

* **github.com/aws/aws-sdk-go-v2**                                                  v1.43.0 -> v1.43.8
* **github.com/aws/aws-sdk-go-v2/config**                                           v1.32.31 -> v1.32.39
* **github.com/aws/aws-sdk-go-v2/credentials**                                      v1.19.30 -> v1.19.38
* **github.com/aws/aws-sdk-go-v2/feature/ec2/imds**                                 v1.18.31 -> v1.18.39
* **github.com/aws/aws-sdk-go-v2/internal/configsources**                           v1.4.31 -> v1.4.39
* **github.com/aws/aws-sdk-go-v2/internal/endpoints/v2**                            v2.7.31 -> v2.7.39
* **github.com/aws/aws-sdk-go-v2/internal/v4a**                                     v1.4.32 -> v1.4.40
* **github.com/aws/aws-sdk-go-v2/service/internal/accept-encoding**                 v1.13.13 -> v1.13.18
* **github.com/aws/aws-sdk-go-v2/service/internal/presigned-url**                   v1.13.31 -> v1.13.39
* **github.com/aws/aws-sdk-go-v2/service/signin**                                   v1.5.0 -> v1.5.8
* **github.com/aws/aws-sdk-go-v2/service/sso**                                      v1.33.0 -> v1.33.8
* **github.com/aws/aws-sdk-go-v2/service/ssooidc**                                  v1.38.0 -> v1.38.8
* **github.com/aws/aws-sdk-go-v2/service/sts**                                      v1.45.0 -> v1.45.8
* **github.com/aws/smithy-go**                                                      v1.27.4 -> v1.27.10
* **github.com/compose-spec/compose-go/v2**                                         v2.13.0 -> v2.14.0
* **github.com/containerd/containerd/v2**                                           v2.3.3 -> v2.3.4
* **github.com/containerd/platforms**                                               v1.0.0-rc.4 -> v1.0.0-rc.5
* **github.com/docker/cli**                                                         v29.6.2 -> v29.7.2
* **github.com/felixge/httpsnoop**                                                  v1.0.4 -> v1.1.0
* **github.com/go-logr/logr**                                                       v1.4.3 -> v1.4.4
* **github.com/klauspost/compress**                                                 v1.19.1 -> v1.19.2
* **github.com/moby/buildkit**                                                      v0.32.2 -> v0.33.0
* **github.com/moby/go-archive**                                                    v0.2.1 -> v0.2.0
* **github.com/moby/policy-helpers**                                                856be88baec4 -> dd6c5499c491
* **github.com/pelletier/go-toml/v2**                                               v2.3.1 -> v2.4.3
* **github.com/sirupsen/logrus**                                                    v1.9.4 -> v1.10.2
* **github.com/stretchr/testify**                                                   v1.11.1 -> v1.12.1
* **github.com/tonistiigi/fsutil**                                                  6d9dc2ebad62 -> 83cac42c1c52
* **go.opentelemetry.io/contrib/instrumentation/google.golang.org/grpc/otelgrpc**   v0.69.0 -> v0.70.0
* **go.opentelemetry.io/contrib/instrumentation/net/http/httptrace/otelhttptrace**  v0.69.0 -> v0.70.0
* **go.opentelemetry.io/contrib/instrumentation/net/http/otelhttp**                 v0.69.0 -> v0.70.0
* **go.opentelemetry.io/otel**                                                      v1.44.0 -> v1.45.0
* **go.opentelemetry.io/otel/exporters/otlp/otlpmetric/otlpmetricgrpc**             v1.44.0 -> v1.45.0
* **go.opentelemetry.io/otel/exporters/otlp/otlpmetric/otlpmetrichttp**             v1.44.0 -> v1.45.0
* **go.opentelemetry.io/otel/exporters/otlp/otlptrace**                             v1.44.0 -> v1.45.0
* **go.opentelemetry.io/otel/exporters/otlp/otlptrace/otlptracegrpc**               v1.44.0 -> v1.45.0
* **go.opentelemetry.io/otel/exporters/otlp/otlptrace/otlptracehttp**               v1.44.0 -> v1.45.0
* **go.opentelemetry.io/otel/metric**                                               v1.44.0 -> v1.45.0
* **go.opentelemetry.io/otel/sdk**                                                  v1.44.0 -> v1.45.0
* **go.opentelemetry.io/otel/sdk/metric**                                           v1.44.0 -> v1.45.0
* **go.opentelemetry.io/otel/trace**                                                v1.44.0 -> v1.45.0
* **go.opentelemetry.io/proto/otlp**                                                v1.10.0 -> v1.11.0
* **go.yaml.in/yaml/v3**                                                            v3.0.4 -> v3.0.5
* **golang.org/x/crypto**                                                           v0.54.0 -> v0.55.0
* **golang.org/x/mod**                                                              v0.38.0 -> v0.40.0
* **golang.org/x/net**                                                              v0.57.0 -> v0.58.0
* **golang.org/x/text**                                                             v0.40.0 -> v0.41.0
* **golang.org/x/tools**                                                            v0.47.0 -> v0.49.0
* **google.golang.org/genproto/googleapis/api**                                     3dc84a4a5aaa -> 6ac0973c030d
* **google.golang.org/genproto/googleapis/rpc**                                     3dc84a4a5aaa -> 6ac0973c030d
* **google.golang.org/grpc**                                                        v1.82.1 -> v1.83.2
* **google.golang.org/grpc/cmd/protoc-gen-go-grpc**                                 v1.6.1 -> v1.6.2
* **google.golang.org/protobuf**                                                    f2248ac996af -> v1.36.12
* **k8s.io/api**                                                                    v0.36.0 -> v0.36.3
* **k8s.io/apimachinery**                                                           v0.36.0 -> v0.36.3
* **k8s.io/client-go**                                                              v0.36.0 -> v0.36.3
* **sigs.k8s.io/structured-merge-diff/v6**                                          v6.3.2 -> v6.3.3

Previous release can be found at [v0.36.1](https://github.com/docker/buildx/releases/tag/v0.36.1)

## v0.36.1

_2026-08-04 · tag `v0.36.1`_

Welcome to the v0.36.1 release of buildx!



Please try out the release binaries and report any issues at
https://github.com/docker/buildx/issues.

### Contributors

* CrazyMax

### Notable Changes

- Add `BUILDX_NO_DEFAULT_OCI_ARTIFACT` as alternative to `oci-artifact=false` when users have not set it explicitly. #3991

### Dependency Changes

* **github.com/moby/buildkit**  v0.32.0 -> v0.32.2

Previous release can be found at [v0.36.0](https://github.com/docker/buildx/releases/tag/v0.36.0)

## v0.36.0

_2026-07-29 · tag `v0.36.0`_

Welcome to the v0.36.0 release of buildx!



Please try out the release binaries and report any issues at
https://github.com/docker/buildx/issues.

### Contributors

* CrazyMax
* Tõnis Tiigi
* Sebastiaan van Stijn
* MohammadHasan Akbari
* Matt Van Horn
* amarkdotdev
* Areeb Ahmed
* Guillaume Lours
* Paweł Gronowski
* Pierre Gimalac
* s3onghyun

### Notables Changes

- Default source policy can now validate the authenticity of BuildKit release images when creating docker-container builder with `docker buildx create` command. #3961
- Bake command now supports overriding declared secret sources. #3962
- Broken builder instances are now correctly handled on removal. #3934
- Bake now supports resolving files relative to the bake file location instead of the current working directory with `BUILDX_BAKE_FILE_RELATIVE_PATHS=true`. #3935
- Source policies now support new `array.flatten` builtin and OPA template strings. #3913
- Imagetools commands now do extra validation of the descriptor inputs from files. #3933
- Windows release binaries are now code-signed, matching the signing coverage already provided for macOS release artifacts. #3978
- Compose compatibility has been updated to v2.13.0. #3929
- Fix source policy support on Windows when loading local files inside policy. #3944
- Fix Kubernetes driver random load balancer support. #3861
- Fix Kubernetes driver builds hanging indefinitely when the remote exec stream ends. #3966
- Fix iidfile for containerd-backed Docker driver. #3952
- Fix authority pseudo-header when using remote driver. #3928
- Fix possible FD leak when using source policies. #3943

### Dependency Changes

* **github.com/Microsoft/go-winio**                                  v0.6.2 -> ad3df93bed29
* **github.com/ProtonMail/go-crypto**                                v1.3.0 -> v1.4.1
* **github.com/aws/aws-sdk-go-v2**                                   v1.42.0 -> v1.43.0
* **github.com/aws/aws-sdk-go-v2/config**                            v1.32.24 -> v1.32.31
* **github.com/aws/aws-sdk-go-v2/credentials**                       v1.19.23 -> v1.19.30
* **github.com/aws/aws-sdk-go-v2/feature/ec2/imds**                  v1.18.29 -> v1.18.31
* **github.com/aws/aws-sdk-go-v2/internal/configsources**            v1.4.29 -> v1.4.31
* **github.com/aws/aws-sdk-go-v2/internal/endpoints/v2**             v2.7.29 -> v2.7.31
* **github.com/aws/aws-sdk-go-v2/internal/v4a**                      v1.4.30 -> v1.4.32
* **github.com/aws/aws-sdk-go-v2/service/internal/accept-encoding**  v1.13.12 -> v1.13.13
* **github.com/aws/aws-sdk-go-v2/service/internal/presigned-url**    v1.13.29 -> v1.13.31
* **github.com/aws/aws-sdk-go-v2/service/signin**                    v1.1.5 -> v1.5.0
* **github.com/aws/aws-sdk-go-v2/service/sso**                       v1.31.3 -> v1.33.0
* **github.com/aws/aws-sdk-go-v2/service/ssooidc**                   v1.36.6 -> v1.38.0
* **github.com/aws/aws-sdk-go-v2/service/sts**                       v1.43.3 -> v1.45.0
* **github.com/aws/smithy-go**                                       v1.27.2 -> v1.27.4
* **github.com/compose-spec/compose-go/v2**                          v2.10.2 -> v2.13.0
* **github.com/containerd/containerd/api**                           v1.10.0 -> v1.11.1
* **github.com/containerd/containerd/v2**                            v2.2.4 -> v2.3.3
* **github.com/containerd/ttrpc**                                    v1.2.8 -> v1.2.9
* **github.com/docker/cli**                                          v29.5.3 -> v29.6.2
* **github.com/go-openapi/errors**                                   v0.22.7 -> v0.22.8
* **github.com/go-openapi/loads**                                    v0.23.3 -> v0.24.0
* **github.com/go-openapi/runtime**                                  v0.32.3 -> v0.32.4
* **github.com/go-openapi/spec**                                     v0.22.5 -> v0.22.6
* **github.com/go-openapi/strfmt**                                   v0.26.3 -> v0.26.4
* **github.com/go-openapi/swag**                                     v0.26.0 -> v0.26.1
* **github.com/go-openapi/swag/cmdutils**                            v0.26.0 -> v0.26.1
* **github.com/go-openapi/swag/conv**                                v0.26.0 -> v0.27.0
* **github.com/go-openapi/swag/fileutils**                           v0.26.0 -> v0.26.1
* **github.com/go-openapi/swag/jsonname**                            v0.26.0 -> v0.26.1
* **github.com/go-openapi/swag/jsonutils**                           v0.26.0 -> v0.26.1
* **github.com/go-openapi/swag/loading**                             v0.26.0 -> v0.26.1
* **github.com/go-openapi/swag/mangling**                            v0.26.0 -> v0.26.1
* **github.com/go-openapi/swag/netutils**                            v0.26.0 -> v0.26.1
* **github.com/go-openapi/swag/stringutils**                         v0.26.0 -> v0.26.1
* **github.com/go-openapi/swag/typeutils**                           v0.26.0 -> v0.27.0
* **github.com/go-openapi/swag/yamlutils**                           v0.26.0 -> v0.26.1
* **github.com/go-openapi/validate**                                 v0.25.3 -> v0.26.0
* **github.com/google/go-containerregistry**                         v0.21.6 -> v0.21.7
* **github.com/klauspost/compress**                                  v1.18.6 -> v1.19.1
* **github.com/lestrrat-go/httprc/v3**                               v3.0.1 -> v3.0.2
* **github.com/lestrrat-go/jwx/v3**                                  v3.0.11 -> v3.0.13
* **github.com/moby/buildkit**                                       v0.31.0 -> v0.32.0
* **github.com/moby/go-archive**                                     v0.2.0 -> v0.2.1
* **github.com/moby/moby/api**                                       v1.54.2 -> v1.55.0
* **github.com/moby/moby/client**                                    v0.4.1 -> v0.5.0
* **github.com/moby/policy-helpers**                                 d5411a945cfc -> 856be88baec4
* **github.com/moby/sys/user**                                       v0.4.0 -> v0.4.1
* **github.com/open-policy-agent/opa**                               v1.10.1 -> v1.14.1
* **github.com/segmentio/asm**                                       v1.2.0 -> v1.2.1
* **github.com/sigstore/rekor**                                      v1.5.2 -> v1.5.3
* **github.com/sigstore/rekor-tiles/v2**                             5d098a2b6443 -> v2.3.0
* **github.com/sigstore/sigstore-go**                                v1.2.1 -> v1.2.2
* **github.com/tonistiigi/fsutil**                                   0257b3308df4 -> 6d9dc2ebad62
* **github.com/valyala/fastjson**                                    v1.6.4 -> v1.6.7
* **github.com/vektah/gqlparser/v2**                                 v2.5.30 -> v2.5.32
* **golang.org/x/crypto**                                            v0.52.0 -> v0.54.0
* **golang.org/x/mod**                                               v0.36.0 -> v0.38.0
* **golang.org/x/net**                                               v0.55.0 -> v0.57.0
* **golang.org/x/sync**                                              v0.20.0 -> v0.22.0
* **golang.org/x/sys**                                               v0.45.0 -> v0.47.0
* **golang.org/x/term**                                              v0.43.0 -> v0.45.0
* **golang.org/x/text**                                              v0.37.0 -> v0.40.0
* **golang.org/x/tools**                                             v0.45.0 -> v0.47.0
* **google.golang.org/grpc**                                         v1.81.1 -> v1.82.1
* **google.golang.org/protobuf**                                     v1.36.11 -> f2248ac996af
* **k8s.io/api**                                                     v0.35.4 -> v0.36.0
* **k8s.io/apimachinery**                                            v0.35.4 -> v0.36.0
* **k8s.io/client-go**                                               v0.35.4 -> v0.36.0
* **k8s.io/kube-openapi**                                            589584f1c912 -> 5883c5ee87b9
* **k8s.io/streaming**                                               v0.36.0 **_new_**
* **k8s.io/utils**                                                   bc988d571ff4 -> 28399d86e0b5
* **sigs.k8s.io/structured-merge-diff/v6**                           v6.3.0 -> v6.3.2

Previous release can be found at [v0.35.0](https://github.com/docker/buildx/releases/tag/v0.35.0)
