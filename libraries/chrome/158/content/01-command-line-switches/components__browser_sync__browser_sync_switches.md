# Command-line switches: `components/browser_sync/browser_sync_switches`

Generated from `components/browser_sync/browser_sync_switches.h` and `components/browser_sync/browser_sync_switches.cc` in the Chromium source. Each switch is passed to the browser as `--name` or `--name=value`. The description is the source comment verbatim; *Condition* is the build/platform `#if` it is defined under.

3 switches.

## `--enable-local-sync-backend`

- Constant: `kEnableLocalSyncBackend`

Enabled the local sync backend implemented by the LoopbackServer.

## `--local-sync-backend-dir`

- Constant: `kLocalSyncBackendDir`

Specifies the local sync backend directory. The name is chosen to mimic user-data-dir etc. This flag only matters if the enable-local-sync-backend flag is present.

## `--disable-sync-invalidation-optimizations`

- Constant: `kDisableSyncInvalidationOptimizations`

Disables the optimizations flags in Commit requests for sync invalidations. This is useful for live tests to avoid flakiness.
