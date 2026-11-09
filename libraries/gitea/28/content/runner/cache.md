---
sidebar_position: 6
---

# Caching

By default, each runner runs a cache server for `actions/cache`, so caching works without setup.
The runner stores entries in `cache.dir`, which defaults to `$HOME/.cache/actcache`. It does not share entries with other runners.

## Sharing a cache between runners

Run one `gitea-runner cache-server` and configure each runner to use it. Use the same secret on the cache server and every runner. Generate the secret with `openssl rand -hex 32`.

On the cache server:

```yaml
cache:
  dir: /data/actcache
  port: 8088
  external_secret_file: /run/secrets/cache-secret
```

```bash
gitea-runner -c cache-server.yaml cache-server
```

On each runner:

```yaml
cache:
  external_server: "http://cache-host:8088/"
  external_secret_file: /run/secrets/cache-secret
```

Jobs send cache requests to their runner, which forwards them to the shared cache server. Only the runners need to reach the shared cache server. Set `external_secret` to supply the secret inline instead of from a file.

Runners can also share a `cache.dir` directory on a filesystem that supports file locks. This makes cache requests slower.

## S3-compatible storage

Use an S3-compatible bucket such as AWS S3, MinIO or RustFS to share the cache without a separate cache server:

```yaml
cache:
  s3:
    endpoint: "http://minio:9000"
    bucket: "runner-cache"
    access_key_file: "/run/secrets/cache-s3-access-key"
    secret_key_file: "/run/secrets/cache-s3-secret-key"
```

Runners with the same settings share the cache. An entry saved on one runner becomes available to the others within 30 seconds. The eviction settings below do not apply to the bucket. Add lifecycle rules to expire old entries and abort incomplete multipart uploads.

## Eviction

| Option | Default | Removes |
| --- | --- | --- |
| `cache.retention` | `168h` | Entries not read or written within this time |
| `cache.repo_size_limit` | `10GB` | Least recently used entries when a repository's cache exceeds this size |
| `cache.size_limit` | off | Least recently used entries when the whole cache exceeds this size |

The cache also keeps 1024 MiB free on its volume, or `health_check.min_free_disk_space_mb` when [health checks](monitoring.md#health-checks) are enabled. With a shared cache server, set these options on the server.

## Artifacts

The runner adapts `actions/cache`, `actions/upload-artifact` and `actions/download-artifact` while a job runs so these actions work with Gitea. With these changes, the cache uses the cache service v2 protocol.

Artifact uploads go through the runner's cache server, so jobs must be able to reach it. Set `cache.v2: false` to send artifact uploads directly to Gitea. Set `runner.patch_actions: false` to run every action exactly as published. This uses the cache service v1 protocol and causes the published artifact actions to fail.

## Jobs cannot reach the cache

If `actions/cache` fails with `connect ETIMEDOUT`, jobs cannot reach the runner's cache server.

A runner container connects itself to each job network when it uses the same Docker daemon as its jobs. For jobs on another Docker daemon, for example through a remote `DOCKER_HOST`, set `cache.host` and `cache.port` to an address and port the jobs can reach. Jobs using `container.network: bridge` cannot reach a runner container outside that network. Leave `container.network` empty or use a network that includes the runner container.

## Action cache

For each job, the runner checks action tags and branches for updates, so it picks up moved tags such as `v6`. With `cache.offline_mode: true`, the runner reuses its downloaded copy. This speeds up jobs on slow networks, but moved tags and updated branches stay at the cached commit.
