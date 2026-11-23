---
title: google-auth-library 11.x changelog (11.0.0 – 11.3.4), for comparison
source: https://github.com/googleapis/google-cloud-node/blob/google-auth-library-v11.3.4/core/packages/google-auth-library-nodejs/CHANGELOG.md
---

# Changelog entries after 10.9.1 (11.0.0 – 11.3.4)

## [11.3.4](https://github.com/googleapis/google-cloud-node/compare/google-auth-library-v11.3.3...google-auth-library-v11.3.4) (2026-11-09)


### Bug Fixes

* **google-auth-library:** [cleanup] set iss from keyFile clientEmail ([#9808](https://github.com/googleapis/google-cloud-node/issues/9808)) ([d3897b9](https://github.com/googleapis/google-cloud-node/commit/d3897b97efc37ebaa2f3e7c248ad602e2f8e6373)), refs [#9469](https://github.com/googleapis/google-cloud-node/issues/9469)

## [11.3.3](https://github.com/googleapis/google-cloud-node/compare/google-auth-library-v11.3.2...google-auth-library-v11.3.3) (2026-11-02)


### Bug Fixes

* **google-auth-library:** Strip -fips suffix from AWS service name in SigV4 signing ([#9779](https://github.com/googleapis/google-cloud-node/issues/9779)) ([080f790](https://github.com/googleapis/google-cloud-node/commit/080f79057ce82351618c2032e73f2f722b0d3564))

## [11.3.2](https://github.com/googleapis/google-cloud-node/compare/google-auth-library-v11.3.1...google-auth-library-v11.3.2) (2026-10-28)


### Bug Fixes

* **core:** Log request/response payloads at DEBUG severity ([#9754](https://github.com/googleapis/google-cloud-node/issues/9754)) ([bf46818](https://github.com/googleapis/google-cloud-node/commit/bf468181b2c85ffd17cc820d2459d6b42213f016))
* **google-auth-library:** Add credential deprecation and validation warnings ([#9720](https://github.com/googleapis/google-cloud-node/issues/9720)) ([569678a](https://github.com/googleapis/google-cloud-node/commit/569678ac3f0917a6ac991548b83ae12819bf2715))

## [11.3.1](https://github.com/googleapis/google-cloud-node/compare/google-auth-library-v11.3.0...google-auth-library-v11.3.1) (2026-10-14)


### Bug Fixes

* **core:** Remove --fetch-shim and handle Bun fetch natively ([#9573](https://github.com/googleapis/google-cloud-node/issues/9573)) ([62559f1](https://github.com/googleapis/google-cloud-node/commit/62559f18d902330c546c787233dcaa7578774463))
* **core:** Remove --gaxios-shim and configure Bun Gaxios fetch ([#9569](https://github.com/googleapis/google-cloud-node/issues/9569)) ([640bf51](https://github.com/googleapis/google-cloud-node/commit/640bf5136c7e9002d65cb257af976c336110d33f))

## [11.3.0](https://github.com/googleapis/google-cloud-node/compare/google-auth-library-v11.2.0...google-auth-library-v11.3.0) (2026-10-08)


### Features

* Update API sources and regenerate ([#9554](https://github.com/googleapis/google-cloud-node/issues/9554)) ([8b6837a](https://github.com/googleapis/google-cloud-node/commit/8b6837a9757cc8bb281e0611b173cb19b58d4ac5))

## [11.2.0](https://github.com/googleapis/google-cloud-node/compare/google-auth-library-v11.1.0...google-auth-library-v11.2.0) (2026-10-07)


### Features

* **tools:** Add individual CLI flags for Bun monkey patches ([#9533](https://github.com/googleapis/google-cloud-node/issues/9533)) ([a5eec89](https://github.com/googleapis/google-cloud-node/commit/a5eec894b054e0605fd8e79591a88393bb2697c6))

## [11.1.0](https://github.com/googleapis/google-cloud-node/compare/google-auth-library-v11.0.2...google-auth-library-v11.1.0) (2026-09-15)


### Features

* PNPM workspace ([#8973](https://github.com/googleapis/google-cloud-node/issues/8973)) ([1ea27c9](https://github.com/googleapis/google-cloud-node/commit/1ea27c9c9bf4e4cbf79381321dcb9bce7951a76f))

## [11.0.2](https://github.com/googleapis/google-cloud-node/compare/google-auth-library-v11.0.1...google-auth-library-v11.0.2) (2026-08-12)


### Bug Fixes

* Ensure node 22 dependencies are up to date so they get the latest patches for core and handwritten libraries ([#9116](https://github.com/googleapis/google-cloud-node/issues/9116)) ([fad57ff](https://github.com/googleapis/google-cloud-node/commit/fad57ff4b9164712426a041fc61db035859f9043))

## [11.0.1](https://github.com/googleapis/google-cloud-node/compare/google-auth-library-v11.0.0...google-auth-library-v11.0.1) (2026-08-10)


### Bug Fixes

* Upgrade all node core library dependencies to their latest node 22 version ([#9084](https://github.com/googleapis/google-cloud-node/issues/9084)) ([af8074c](https://github.com/googleapis/google-cloud-node/commit/af8074c0281f4f8dc40570f580f4cdebf1d72cde))

## [11.0.0](https://github.com/googleapis/google-cloud-node/compare/google-auth-library-v10.9.1...google-auth-library-v11.0.0) (2026-07-29)


### ⚠ BREAKING CHANGES

* Update google-auth-library-nodejs to minimum Node version of 22. ([#8995](https://github.com/googleapis/google-cloud-node/issues/8995))

### Features

* Update google-auth-library-nodejs to minimum Node version of 22. ([#8995](https://github.com/googleapis/google-cloud-node/issues/8995)) ([152f686](https://github.com/googleapis/google-cloud-node/commit/152f68682850e30936597c732a62eca9c7a60eee)), refs [#8985](https://github.com/googleapis/google-cloud-node/issues/8985)

