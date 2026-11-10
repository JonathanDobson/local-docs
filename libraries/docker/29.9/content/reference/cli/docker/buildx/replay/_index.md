---
title: "docker buildx replay"
source: https://docs.docker.com/reference/cli/docker/buildx/replay/
---

# docker buildx replay

**Description:** Replay a build from its provenance

**Usage:** `docker buildx replay`





> [!NOTE]
> **Experimental**
>
> This command is experimental. Experimental features are intended for testing and feedback as their functionality or design may change between releases without warning or can be removed entirely in a future release.





## Description

`buildx replay` reads the SLSA provenance attestation of an existing build and
reproduces the build with the recorded frontend, options, and source digests.
Replay runs on the selected builder and requires BuildKit v0.27 or later.

Subjects are accepted in three forms:

- `docker-image://<ref>` or a bare `<ref>` — resolve through the registry.
- `oci-layout://<path>[:<tag>]` — read from a local OCI layout.
- A local attestation file: an in-toto statement (`.intoto.jsonl`), an
  unsigned DSSE envelope, a Sigstore bundle, or a bare SLSA provenance
  predicate.

A build can be replayed when:

- its provenance was recorded with `mode=max`
  (`--provenance=mode=max` or `--attest=type=provenance,mode=max`). `mode=min`
  provenance omits the build arguments, secrets, and SSH needed for replay;
- its build context was a Git repository or an HTTP(S) URL. Builds that used
  local directories, stdin, OCI layouts, or other Bake targets as build
  contexts cannot be replayed;
- it did not use `--network=host`, unless a different `--network` is passed
  to replay;
- the recorded sources are still available.

Replay rebuilds one platform at a time. For a multi-platform image, select the
platform with `--platform`. By default, the only platform of the image or the
default platform of the builder is used.






## Subcommands

| Command | Description |
|---------|-------------|
| [`docker buildx replay build`](https://docs.docker.com/reference/cli/docker/buildx/replay/build/) | Rebuild an image from provenance and pinned materials |
