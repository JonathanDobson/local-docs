# Command-line switches: `components/client_hints/common/switches`

Generated from `components/client_hints/common/switches.h` and `components/client_hints/common/switches.cc` in the Chromium source. Each switch is passed to the browser as `--name` or `--name=value`. The description is the source comment verbatim; *Condition* is the build/platform `#if` it is defined under.

1 switches.

## `--initialize-client-hints-storage`

- Constant: `kInitializeClientHintsStorage`

Pre-load the client hint storage. Takes a JSON dict, with each key being an origin (RFC 6454 Section 6.2) and each value a comma-separated list of client hint tokens (RFC 8942 Section 3.1, client-hints-infrastructure Section 7.1).  Each origin/token-list entry will be parsed and persisted to the Client Hints storage as though the token-list had come through an Accept-CH response header from a navigation from the origin.  The initialization will only apply to non-OffTheRecord profiles, meaning incognito or guest profiles will not have the storage applied.
