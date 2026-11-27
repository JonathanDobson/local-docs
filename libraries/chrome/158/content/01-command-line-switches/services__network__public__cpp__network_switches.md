# Command-line switches: `services/network/public/cpp/network_switches`

Generated from `services/network/public/cpp/network_switches.h` and `services/network/public/cpp/network_switches.cc` in the Chromium source. Each switch is passed to the browser as `--name` or `--name=value`. The description is the source comment verbatim; *Condition* is the build/platform `#if` it is defined under.

17 switches.

## `--force-effective-connection-type`

- Constant: `kForceEffectiveConnectionType`

Forces Network Quality Estimator (NQE) to return a specific effective connection type.

## `--force-permission-policy-unload-default-enabled`

- Constant: `kForcePermissionPolicyUnloadDefaultEnabled`

If set, the unload event cannot be disabled by default by Permissions-Policy.

## `--host-resolver-rules`

- Constant: `kHostResolverRules`

These mappings only apply to the host resolver.

## `--host-rules`

- Constant: `kHostRules`

Deprecated alias for backwards compatibility, now does the same thing as --host-resolver-rules which should be used instead. TODO(crbug.com/40070729): consider removing in some future release.

## `--ignore-certificate-errors-spki-list`

- Constant: `kIgnoreCertificateErrorsSPKIList`

A set of public key hashes for which to ignore certificate-related errors.  If the certificate chain presented by the server does not validate, and one or more certificates have public key hashes that match a key from this list, the error is ignored.  The switch value must be a comma-separated list of Base64-encoded SHA-256 SPKI Fingerprints (RFC 7469, Section 2.4).  This switch has no effect unless --user-data-dir (as defined by the content embedder) is also present.

## `--net-log-capture-mode`

- Constant: `kNetLogCaptureMode`

Sets the granularity of events to capture in the network log. The mode can be set to one of the following values: "Default" "IncludeSensitive" "Everything"  See the enums of the corresponding name in net_log_capture_mode.h for a description of their meanings.

## `--net-log-file-format`

- Constant: `kNetLogFileFormat`

Sets the format used for the network log file. Supported values are: "json" "ndjson"

## `--net-log-duration`

- Constant: `kLogNetLogDuration`

Specifies the duration (in seconds) for network logging. When this flag is provided with a positive integer value X, Chrome will automatically stop collecting NetLog events after X seconds and flush the log to disk.

## `--net-log-max-size-mb`

- Constant: `kNetLogMaxSizeMb`

Sets the maximum size, in megabytes. The log file can grow to before older data is overwritten. Do not use this flag if you want an unlimited file size.

## `--ssl-key-log-file`

- Constant: `kSSLKeyLogFile`

Causes SSL key material to be logged to the specified file for debugging purposes. See https://developer.mozilla.org/en-US/docs/Mozilla/Projects/NSS/Key_Log_Format for the format.

## `--test-third-party-cookie-phaseout`

- Constant: `kTestThirdPartyCookiePhaseout`

_No description in the source._

## `--unsafely-treat-insecure-origin-as-secure`

- Constant: `kUnsafelyTreatInsecureOriginAsSecure`

Treat given (insecure) origins as secure origins. Multiple origins can be supplied as a comma-separated list. For the definition of secure contexts, see https://w3c.github.io/webappsec-secure-contexts/ and https://www.w3.org/TR/powerful-features/#is-origin-trustworthy  Example: --unsafely-treat-insecure-origin-as-secure=http://a.test,http://b.test

## `--additional-private-state-token-key-commitments`

- Constant: `kAdditionalTrustTokenKeyCommitments`

Manually sets additional Private State Tokens key commitments in the network service to the given value, which should be a JSON dictionary satisfying the requirements of TrustTokenKeyCommitmentParser::ParseMultipleIssuers.  These keys are available in addition to keys provided by the most recent call to TrustTokenKeyCommitments::Set.  For issuers with keys provided through both the command line and TrustTokenKeyCommitments::Set, the keys provided through the command line take precedence. This is because someone testing manually might want to pass additional keys via the command line to a real Chrome release with the component updater enabled, and it would be surprising if the manually-passed keys were overwritten some time after startup when the component updater runs.

## `--ip-address-space-overrides`

- Constant: `kIpAddressSpaceOverrides`

Specifies manual overrides to the IP endpoint -> IP address space mapping. This allows running local tests against "public" and "local" IP addresses.  This switch is specified as a comma-separated list of overrides. Each override is an equals-separated "<endpoint|ip-range>=<address space>" pair.  Grammar, in pseudo-BNF format:  switch := override-list override-list := override “,” override-list | <nil> override := (ip-endpoint | ip_range) “=” address-space address-space := “public” | “private” | “local” | "loopback" ip-endpoint := ip-address ":" port ip-address := see `net::ParseURLHostnameToAddress()` for details port := integer in the [0-65535] range ip-range := ip-address "/" bitmask bitmask := integer in the [0-128] range  Any invalid entries in the comma-separated list are ignored. If the port specified is 0, all ports for the given ip-address will be overridden.  See also the design doc: https://docs.google.com/document/d/1-umCGylIOuSG02k9KGDwKayt3bzBXtGwVlCQHHkIcnQ/edit#  And the Web Platform Test RFC #72 behind it: https://github.com/web-platform-tests/rfcs/blob/master/rfcs/address_space_overrides.md  Note that since the doc and the RFC were written, the address space names have changed slightly due to Local Network Access (LNA) replacing Private Network Access (PNA).

## `--local-network-access-permissions-policy-default-enabled`

- Constant: `kLocalNetworkAccessPermissionsPolicyDefaultEnabled`

If set, Local Network Access (LNA) permissions policy features will be default enabled in all frames, rather than requiring explicit delegation.

## `--disable-shared-dictionary-storage-cleanup-for-testing`

- Constant: `kDisableSharedDictionaryStorageCleanupForTesting`

The switch to disable the shared dictionary storage clean up task. Only for testing.

## `--ignore-bad-message-for-testing`

- Constant: `kIgnoreBadMessageForTesting`

The switch to ignore bad mojo message reports. Only for testing.
