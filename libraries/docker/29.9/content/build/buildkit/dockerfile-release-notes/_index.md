---
title: "Dockerfile release notes"
source: https://docs.docker.com/build/buildkit/dockerfile-release-notes/
---

# Dockerfile release notes

Dockerfile frontend (`docker/dockerfile`) releases 1.26 and later; the `-labs` variants are omitted. From the GitHub releases of [moby/buildkit](https://github.com/moby/buildkit/releases), which is where this page links on docs.docker.com.

## dockerfile/1.28.0

_2026-10-07 · tag `dockerfile/1.28.0`_

### Usage

```
# syntax=docker.io/docker/dockerfile-upstream:1.28.0
```

### Notable changes

- Allow "default group" syntax in `COPY --chown` instruction. #3555
- Add better detection for invalid combinations between `--chown` and `--link` in the `COPY` instruction. #7134

## dockerfile/1.27.1

_2026-09-30 · tag `dockerfile/1.27.1`_

### Usage

```
# syntax=docker.io/docker/dockerfile-upstream:1.27.1
```

### Notable changes

- Reject Dockerfiles and `.dockerignore` files larger than 16 MiB instead of loading them without a limit. GHSA-mgqf-486f-49vp
- Limit reads of HTTP archives to 16 MiB when inspecting them for `SOURCE_DATE_EPOCH` timestamps. GHSA-mgqf-486f-49vp

## dockerfile/1.27.0

_2026-09-02 · tag `dockerfile/1.27.0`_

### Usage

```
# syntax=docker.io/docker/dockerfile-upstream:1.27.0
```

### Notable changes

- Archives with zstd compression can now be used as build context and in `ADD` instructions. #7069
- `RUN --device` flag is now promoted from labs to stable. #6999

## dockerfile/1.26.0

_2026-07-29 · tag `dockerfile/1.26.0`_

### Usage

```
# syntax=docker.io/docker/dockerfile-upstream:1.26.0
```

### Notable changes

- Fix incorrect warning when matching dockerignore patterns to `COPY .` command #6930
