# Command-line switches: `components/variations/variations_switches`

Generated from `components/variations/variations_switches.h` and `components/variations/variations_switches.cc` in the Chromium source. Each switch is passed to the browser as `--name` or `--name=value`. The description is the source comment verbatim; *Condition* is the build/platform `#if` it is defined under.

22 switches.

## `--disable-field-trial-config`

- Constant: `kDisableFieldTrialTestingConfig`

Disable field trial tests configured in fieldtrial_testing_config.json.

## `--disable-variations-safe-mode`

- Constant: `kDisableVariationsSafeMode`

Disable variations safe mode.

## `--disable-variations-seed-fetch`

- Constant: `kDisableVariationsSeedFetch`

Disable fetching of variations seed from the server for testing.

## `--disable-variations-seed-fetch-throttling`

- Constant: `kDisableVariationsSeedFetchThrottling`

Disables throttling for fetching the variations seed on mobile platforms. The seed will be fetched on startup and every time the app enters the foreground, regardless of the time passed in between the fetches. On Desktop, this switch has no effect (the seed is fetched periodically instead).

## `--enable-benchmarking-api`

- Constant: `kEnableBenchmarkingApi`

Enables the benchmarking JavaScript API.

## `--enable-field-trial-config`

- Constant: `kEnableFieldTrialTestingConfig`

Enable field trial tests configured in fieldtrial_testing_config.json. If the "disable_fieldtrial_testing_config" GN flag is set to true, then this switch is a no-op. Otherwise, for non-Chrome branded builds, the testing config is already applied by default, unless the "--disable-field-trial-config", "--force-fieldtrials", and/or "--variations-server-url" switches are passed. It is however possible to apply the testing config as well as specify additional field trials (using "--force-fieldtrials") by using this switch. For Chrome-branded builds, the testing config is not enabled by default, so this switch is required to enable it. If this switch is set to "benchmarking", it enables variations benchmarking mode, which skips experiments that are disabled for benchmarking.

## `--fake-variations-channel`

- Constant: `kFakeVariationsChannel`

Fakes the channel of the browser for purposes of Variations filtering. This is to be used for testing only. Possible values are "stable", "beta", "dev" and "canary". This works for official builds as well.

## `--fake-variations-platform`

- Constant: `kFakeVariationsPlatform`

Fakes the platform of the browser for variations seed fetching and field trial filtering. Possible values are as follows: "android", "android_webview", "chromeos", "fuchsia", "ios", "linux", "mac", and "win".  Intended only for testing.

## `--force-fieldtrial-params`

- Constant: `kForceFieldTrialParams`

This option can be used to force parameters of field trials when testing changes locally. The argument is a param list of (key, value) pairs prefixed by an associated (trial, group) pair. You specify the param list for multiple (trial, group) pairs with a comma separator. Example: "Trial1.Group1:k1/v1/k2/v2,Trial2.Group2:k3/v3/k4/v4" Trial names, groups names, parameter names, and value should all be URL escaped for all non-alphanumeric characters.

## `--force-variation-ids`

- Constant: `kForceVariationIds`

Forces additional Chrome Variation Ids that will be sent in X-Client-Data header, specified as a 64-bit encoded list of numeric experiment ids. Ids prefixed with the character "t" will be treated as Trigger Variation Ids.  IMPORTANT: You can use this switch for test purposes (e.g. a manual command line run or from a unit test), but NOT for production code in the browser, as the latter is not allowed for privacy reasons (except for the current use by about:flags code).

## `--force-disable-variation-ids`

- Constant: `kForceDisableVariationIds`

Forces to remove Chrome Variation Ids from being sent in X-Client-Data header, specified as a 64-bit encoded list of numeric experiment ids. Ids prefixed with the character "t" will be treated as Trigger Variation Ids.

## `--variations-seed-corpus`

- Constant: `kVariationsSeedCorpus`

Specifies the value of the variations seed corpus to use. When unspecified or unrecognized, the default corpus will be used.

## `--variations-seed-version`

- Constant: `kVariationsSeedVersion`

Used to share variations seed version with child processes.

## `--variations-override-country`

- Constant: `kVariationsOverrideCountry`

Allows overriding the country used for evaluating variations. This is similar to the "Override Variations Country" entry on chrome://translate-internals, but is exposed as a command-line flag to allow testing First Run scenarios. Additionally, unlike chrome://translate-internals, the value isn't persisted across sessions.

## `--variations-override-geo-level-1`

- Constant: `kVariationsOverrideGeoLevel1`

Allows overriding the administrative area code used for evaluating variations and regional eligibility features.

## `--variations-test-seed-path`

- Constant: `kVariationsTestSeedJsonPath`

Specifies the location of a seed file for Local State's seed to be populated from. The seed file must be in json format with the keys |kVariationsCompressedSeed| and |kVariationsSeedSignature|.

## `--variations-server-url`

- Constant: `kVariationsServerURL`

Specifies a custom URL for the server which reports variation data to the client. Specifying this switch enables the Variations service on unofficial builds. See variations_service.cc.

## `--variations-insecure-server-url`

- Constant: `kVariationsInsecureServerURL`

Specifies a custom URL for the server to use as an insecure fallback when requests to |kVariationsServerURL| fail. Requests to this URL will be encrypted.

## `--variations-seed-fetch-interval`

- Constant: `kVariationsSeedFetchInterval`

Override the time interval between each variation seed fetches. Unit is in minutes. The minimum is 1 minute. The default is 30 minutes.

## `--enable-finch-seed-delta-compression`

- Constant: `kEnableFinchSeedDeltaCompression`

Enables delta-compression when fetching a new seed via the "first run" code path on Android.

## `--accept-empty-variations-seed-signature`

- Constant: `kAcceptEmptySeedSignatureForTesting`

Accept an empty signature when loading a variations seed. This is for testing purposes.

## `--variations-state-file`

- Constant: `kVariationsStateFile`

Use features defined in the value. Use this flag to reproduce experiments related issues. Copy 'Command-line Variations' value from chrome://version page. Save it to a file and pass it via this flag. The value is a base64 encoded JSON format produced by `variations::VariationsCommandLine::WriteToString`.
