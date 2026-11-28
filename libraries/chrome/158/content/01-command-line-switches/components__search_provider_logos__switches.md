# Command-line switches: `components/search_provider_logos/switches`

Generated from `components/search_provider_logos/switches.h` and `components/search_provider_logos/switches.cc` in the Chromium source. Each switch is passed to the browser as `--name` or `--name=value`. The description is the source comment verbatim; *Condition* is the build/platform `#if` it is defined under.

3 switches.

## `--google-doodle-url`

- Constant: `kGoogleDoodleUrl`

Overrides the URL used to fetch the current Google Doodle. Example: https://www.google.com/async/ddljson Testing? Try: https://www.gstatic.com/chrome/ntp/doodle_test/ddljson_android0.json https://www.gstatic.com/chrome/ntp/doodle_test/ddljson_android1.json https://www.gstatic.com/chrome/ntp/doodle_test/ddljson_android2.json https://www.gstatic.com/chrome/ntp/doodle_test/ddljson_android3.json https://www.gstatic.com/chrome/ntp/doodle_test/ddljson_android4.json

## `--search-provider-logo-url`

- Constant: `kSearchProviderLogoURL`

Use a static URL for the logo of the default search engine. Example: https://www.google.com/branding/logo.png

## `--third-party-doodle-url`

- Constant: `kThirdPartyDoodleURL`

Overrides the Doodle URL to use for third-party search engines. Testing? Try: https://www.gstatic.com/chrome/ntp/doodle_test/third_party_simple.json https://www.gstatic.com/chrome/ntp/doodle_test/third_party_animated.json
