# Command-line switches: `components/autofill/core/common/autofill_switches`

Generated from `components/autofill/core/common/autofill_switches.h` and `components/autofill/core/common/autofill_switches.cc` in the Chromium source. Each switch is passed to the browser as `--name` or `--name=value`. The description is the source comment verbatim; *Condition* is the build/platform `#if` it is defined under.

8 switches.

## `--autofill-api-key`

- Constant: `kAutofillAPIKey`

All switches in alphabetical order. The switches should be documented alongside the definition of their values in the .cc file. Sets the API key that will be used when calling Autofill API instead of using Chrome's baked key by default. You can use this to test new versions of the API that are not linked to the Chrome baked key yet.

## `--autofill-server-url`

- Constant: `kAutofillServerURL`

Override the default autofill server URL with "scheme://host[:port]/prefix/".

## `--autofill-upload-throttling-period-in-days`

- Constant: `kAutofillUploadThrottlingPeriodInDays`

The number of days after which to reset the registry of autofill events for which an upload has been sent.

## `--auto-grant-email-verification-permission-for-testing`

- Constant: `kAutoGrantEmailVerificationPermissionForTesting`

Automatically grants permission prompts for email verification for testing.

## `--ignore-autocomplete-off-autofill`

- Constant: `kIgnoreAutocompleteOffForAutofill`

Ignores autocomplete="off" for Autofill data (profiles + credit cards).

## `--show-autofill-type-predictions`

- Constant: `kShowAutofillTypePredictions`

Annotates forms with Autofill field type predictions.

## `--show-autofill-signatures`

- Constant: `kShowAutofillSignatures`

Annotates forms and fields with Autofill signatures.

## `--wallet-service-use-sandbox`

- Constant: `kWalletServiceUseSandbox`

Use the sandbox Online Wallet service URL (for developer testing).
