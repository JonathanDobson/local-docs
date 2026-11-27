# Command-line switches: `components/translate/core/common/translate_switches`

Generated from `components/translate/core/common/translate_switches.h` and `components/translate/core/common/translate_switches.cc` in the Chromium source. Each switch is passed to the browser as `--name` or `--name=value`. The description is the source comment verbatim; *Condition* is the build/platform `#if` it is defined under.

4 switches.

## `--translate-script-url`

- Constant: `kTranslateScriptURL`

Overrides the default server used for Google Translate.

## `--translate-security-origin`

- Constant: `kTranslateSecurityOrigin`

Overrides security-origin with which Translate runs in an isolated world.

## `--translate-ranker-model-url`

- Constant: `kTranslateRankerModelURL`

Overrides the URL from which the translate ranker model is downloaded.

## `--forced-translate-language`

- Constant: `kForcedTranslateLanguage`

Overrides the target language for translation and forces translation of all pages to the new target language.
