# Command-line switches: `components/os_crypt/common/os_crypt_switches`

Generated from `components/os_crypt/common/os_crypt_switches.h` in the Chromium source. Each switch is passed to the browser as `--name` or `--name=value`. The description is the source comment verbatim; *Condition* is the build/platform `#if` it is defined under.

1 switches.

## `--use-mock-keychain`

- Constant: `kUseMockKeychain`
- Condition: `BUILDFLAG(IS_APPLE)`

Uses mock keychain for testing purposes, which prevents blocking dialogs from causing timeouts.
