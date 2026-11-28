# Command-line switches: `components/regional_capabilities/regional_capabilities_switches`

Generated from `components/regional_capabilities/regional_capabilities_switches.h` and `components/regional_capabilities/regional_capabilities_switches.cc` in the Chromium source. Each switch is passed to the browser as `--name` or `--name=value`. The description is the source comment verbatim; *Condition* is the build/platform `#if` it is defined under.

4 switches.

## `--search-engine-choice-country`

- Constant: `kSearchEngineChoiceCountry`

Overrides the profile country (which is among other things used for search engine choice region checks for example). Intended for testing. Parameter can be one of 3 things: - 2-letter country codes => Will override the profile country - A program name => Will override the country and the program - A specific list override => Will override the program, but instead of overriding the country, will use special values to force the search engine list to some preset testing ones.

## `--TAIYAKI`

- Constant: `kTaiyakiProgramOverride`

Special value for the `kSearchEngineChoiceCountry` command-line flag. Enables the Taiyaki program. On unsupported platform / build types, will fall back to default program / unknown country.

## `--DEFAULT_EEA`

- Constant: `kDefaultListCountryOverride`

Special value for the `kSearchEngineChoiceCountry` command-line flag. Enables the Waffle program and overrides the list of search engines to display the default set.

## `--EEA_ALL`

- Constant: `kEeaListCountryOverride`

Special value for the `kSearchEngineChoiceCountry` command-line flag. Enables the Waffle program and overrides the list of search engines to display the list of all EEA engines.
