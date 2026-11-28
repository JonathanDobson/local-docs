# Command-line switches: `components/search_engines/search_engines_switches`

Generated from `components/search_engines/search_engines_switches.h` and `components/search_engines/search_engines_switches.cc` in the Chromium source. Each switch is passed to the browser as `--name` or `--name=value`. The description is the source comment verbatim; *Condition* is the build/platform `#if` it is defined under.

6 switches.

## `--extra-search-query-params`

- Constant: `kExtraSearchQueryParams`

Additional query params to insert in the search and instant URLs.  Useful for testing.

## `--ignore-no-first-run-for-search-engine-choice-screen`

- Constant: `kIgnoreNoFirstRunForSearchEngineChoiceScreen`

Override the --no-first-run dialog suppression for the search dialog for testing

## `--disable-search-engine-choice-screen`

- Constant: `kDisableSearchEngineChoiceScreen`

Disable the search engine choice screen for testing / autmation.

## `--force-search-engine-choice-screen`

- Constant: `kForceSearchEngineChoiceScreen`

Force-enable showing the search engine choice screen for testing regardless of region or choice already having been made.

## `--quicken-site-search-expiry-for-testing`

- Constant: `kQuickenSiteSearchExpiryForTesting`

_No description in the source._

## `--NO_REPROMPT`

- Constant: `kSearchEngineChoiceNoRepromptString`

The string that's passed to `switches::kSearchEngineChoiceTriggerRepromptParams` so that we don't reprompt users with the choice screen.
