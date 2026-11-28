# Command-line switches: `google_apis/gaia/gaia_switches`

Generated from `google_apis/gaia/gaia_switches.h` and `google_apis/gaia/gaia_switches.cc` in the Chromium source. Each switch is passed to the browser as `--name` or `--name=value`. The description is the source comment verbatim; *Condition* is the build/platform `#if` it is defined under.

9 switches.

## `--gaia-config`

- Constant: `kGaiaConfigPath`

Specifies the path to a config file containing GAIA urls. See "google_apis/test/data/gaia/all_urls.json" for a format example.

## `--gaia-config-contents`

- Constant: `kGaiaConfigContents`

Specifies a string containing the JSON config for GAIA urls. This is equivalent to pointing to a file with the same content via kGaiaConfigPath. See "google_apis/test/data/gaia/all_urls.json" for a format example.

## `--google-url`

- Constant: `kGoogleUrl`

Specifies the domain of the SAPISID cookie. The default value is "http://.google.com".

## `--gaia-url`

- Constant: `kGaiaUrl`

Specifies the path for GAIA authentication URL. The default value is "https://accounts.google.com".

## `--google-apis-url`

- Constant: `kGoogleApisUrl`

Specifies the backend server used for Google API calls. "https://www.googleapis.com".

## `--lso-url`

- Constant: `kLsoUrl`

Specifies the backend server used for lso authentication calls. "https://accounts.google.com".

## `--oauth-account-manager-url`

- Constant: `kOAuthAccountManagerUrl`

Specifies the backend server used for OAuth issue token calls. "https://oauthaccountmanager.googleapis.com".

## `--oauth2-client-id`

- Constant: `kOAuth2ClientID`

Specifies custom OAuth2 client id for testing purposes.

## `--oauth2-client-secret`

- Constant: `kOAuth2ClientSecret`

Specifies custom OAuth2 client secret for testing purposes.
