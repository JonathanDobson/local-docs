# Command-line switches: `components/password_manager/core/browser/password_manager_switches`

Generated from `components/password_manager/core/browser/password_manager_switches.h` and `components/password_manager/core/browser/password_manager_switches.cc` in the Chromium source. Each switch is passed to the browser as `--name` or `--name=value`. The description is the source comment verbatim; *Condition* is the build/platform `#if` it is defined under.

5 switches.

## `--password-store`

- Constant: `kPasswordStore`
- Condition: `BUILDFLAG(IS_LINUX)`

Specifies which encryption storage backend to use. Possible values are kwallet, kwallet5, kwallet6, gnome-libsecret, basic. Any other value will lead to Chrome detecting the best backend automatically.

## `--enable-encryption-selection`

- Constant: `kEnableEncryptionSelection`
- Condition: `BUILDFLAG(IS_LINUX)`

Enables the feature of allowing the user to disable the backend via a setting.

## `--enable-share-button-unbranded`

- Constant: `kEnableShareButtonUnbranded`

Enables Password Sharing button in password details UI in settings when running unbranded builds.

## `--user-data-dir`

- Constant: `kUserDataDir`

Specifies the user data directory, which is where the browser will look for all of its state. Needs to be kept in sync with chrome/common/chrome_switches.h

## `--password-change-url`

- Constant: `kPasswordChangeUrl`

This switch allows testing password change feature on provided URL. Password change will be offered by submitting password form on any URL with matching eTLD+1.
