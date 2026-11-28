# Command-line switches: `components/safe_browsing/core/common/safebrowsing_switches`

Generated from `components/safe_browsing/core/common/safebrowsing_switches.h` and `components/safe_browsing/core/common/safebrowsing_switches.cc` in the Chromium source. Each switch is passed to the browser as `--name` or `--name=value`. The description is the source comment verbatim; *Condition* is the build/platform `#if` it is defined under.

22 switches.

## `--mark_as_phishing`

- Constant: `kMarkAsPhishing`

List of comma-separated URLs to mark as phishing for local database checks.

## `--mark_as_malware`

- Constant: `kMarkAsMalware`

List of comma-separated URLs to mark as malware for local database checks.

## `--mark_as_uws`

- Constant: `kMarkAsUws`

List of comma-separated URLs to mark as unwanted software for local database checks.

## `--mark_as_allowlisted_for_real_time`

- Constant: `kMarkAsHighConfidenceAllowlisted`

List of comma-separated URLs to mark as present on the high-confidence allowlist.

## `--mark_as_real_time_phishing`

- Constant: `kArtificialCachedUrlRealTimeVerdictFlag`

Command-line flag for caching an artificial phishing verdict for URL real-time lookups.

## `--mark_as_v5_search_hashes_phishing`

- Constant: `kArtificialCachedV5SearchHashesVerdictFlag`

Command-line flag for caching an artificial phishing verdict for V5 SearchHashes.

## `--mark_as_enterprise_blocked`

- Constant: `kArtificialCachedEnterpriseBlockedVerdictFlag`

Command-line flag for caching an artificial blocked enterprise lookup verdict.

## `--mark_as_enterprise_warned`

- Constant: `kArtificialCachedEnterpriseWarnedVerdictFlag`

Command-line flag for caching an artificial flagged enterprise lookup verdict.

## `--safe-browsing-skip-high-confidence-allowlist`

- Constant: `kSkipHighConfidenceAllowlist`

If the switch is present, any high-confidence allowlist check will return that it does not match the allowlist.

## `--url-filtering-endpoint`

- Constant: `kUrlFilteringEndpointFlag`

Alternate URL to use for ChromeEnterpriseRealTimeUrlLookupService real-time lookups.

## `--csd-debug-feature-directory`

- Constant: `kCsdDebugFeatureDirectoryFlag`

Command-line flag that can be used to write extracted CSD features to disk. This is also enables a few other behaviors that are useful for debugging.

## `--safe-browsing-skip-csd-allowlist`

- Constant: `kSkipCSDAllowlistOnPreclassification`

If present, indicates that the client-side detection allowlist check should be skipped (it is treated as no match).

## `--csd-model-override-path`

- Constant: `kOverrideCsdModelFlag`

Command-line flag that can be used to override the current CSD model. Must be provided with an absolute path.

## `--mark_as_phish_guard_phishing`

- Constant: `kArtificialCachedPhishGuardVerdictFlag`

Command-line flag for caching an artificial PhishGuard unsafe verdict.

## `--mark_as_allowlisted_for_phish_guard`

- Constant: `kMarkAsPasswordProtectionAllowlisted`

List of comma-separated URLs to mark as present on the password protection allowlist. Note this uses the client-side detection allowlist.

## `--wp-max-file-opening-threads`

- Constant: `kWpMaxFileOpeningThreads`

_No description in the source._

## `--binary-upload-service-url`

- Constant: `kCloudBinaryUploadServiceUrlFlag`

_No description in the source._

## `--safebrowsing-manual-download-blacklist`

- Constant: `kSbManualDownloadBlocklist`

List of comma-separated sha256 hashes of executable files which the download-protection service should treat as "dangerous."  For a file to show a warning, it also must be considered a dangerous filetype and not be allowlisted otherwise (by signature or URL) and must be on a supported OS. Hashes are in hex. This is used for manual testing when looking for ways to by-pass download protection.

## `--safebrowsing-enable-enhanced-protection`

- Constant: `kSbEnableEnhancedProtection`

Enable Safe Browsing Enhanced Protection.

## `--safe-browsing-treat-user-as-advanced-protection`

- Constant: `kForceTreatUserAsAdvancedProtection`

_No description in the source._

## `--safebrowsing-fast-initial-lists-update`

- Constant: `kSbFastInitialListsUpdate`

Command-line flag that reduces the initial delay for Safe Browsing database updates for manual testing purposes.

## `--safe-browsing-no-protection-duration-seconds`

- Constant: `kSafeBrowsingNoProtectionDurationSeconds`

Command-line override for the temporary No Protection duration in seconds.
