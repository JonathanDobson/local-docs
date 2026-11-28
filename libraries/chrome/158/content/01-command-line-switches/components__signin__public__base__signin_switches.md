# Command-line switches: `components/signin/public/base/signin_switches`

Generated from `components/signin/public/base/signin_switches.h` and `components/signin/public/base/signin_switches.cc` in the Chromium source. Each switch is passed to the browser as `--name` or `--name=value`. The description is the source comment verbatim; *Condition* is the build/platform `#if` it is defined under.

5 switches.

## `--clear-token-service`

- Constant: `kClearTokenService`

Clears the token service before using it. This allows simulating the expiration of credentials during testing.

## `--disable-signin-promo-on-avatar-pill-for-testing`

- Constant: `kDisableSigninPromoOnAvatarPillForTesting`
- Condition: `BUILDFLAG(ENABLE_DICE_SUPPORT)`

Disables the sign-in promo on the avatar pill for tests by default, as it has impact on the startup behavior. Tests that need to test this specific behavior needs to explicitly enable it.

## `--force-fre-default-browser-step`

- Constant: `kForceFreDefaultBrowserStep`
- Condition: `BUILDFLAG(ENABLE_DICE_SUPPORT)`

Force enable the default browser step in the first run experience on Desktop.

## `--force-fre-feature-showcase-steps`

- Constant: `kForceFreFeatureShowcaseSteps`
- Condition: `BUILDFLAG(ENABLE_DICE_SUPPORT)`

Overrides the eligible steps in the Feature Showcase step of the first run experience. Step names should be valid values separated by commas.

## `--probability`

- Constant: `kHatsSurveyProbabilityName`
- Condition: `BUILDFLAG(IS_WIN) || BUILDFLAG(IS_MAC) || BUILDFLAG(IS_LINUX) || \`

Feature param to pass probability for identity surveys.
