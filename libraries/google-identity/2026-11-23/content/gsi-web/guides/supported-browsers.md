---
source: https://developers.google.com/identity/gsi/web/guides/supported-browsers
markdown_source: https://developers.google.com/identity/gsi/web/guides/supported-browsers.md.txt
title: "Supported browsers and platforms  |  Web guides  |  Google for Developers"
fetched: 2026-11-23
---

> [!IMPORTANT]
> **Important:** For apps running on devices that don't support a system browser or that have limited input capabilities, such as TVs, game consoles, cameras, or printers, see [Sign-In on TVs and Limited Input Devices](https://developers.google.com/identity/gsi/web/guides/devices).  
>
> This library does not support Chrome extensions. When adding user sign-in to a Chrome extension refer to this [guide](https://developer.chrome.com/docs/extensions/how-to/integrate/oauth) instead.

> [!NOTE]
> **Note:** Android and iOS webviews are not supported for user sign-in. We recommend using [Chrome Custom Tabs](https://developer.chrome.com/docs/android/custom-tabs/) on Android and [SFSafariViewController](https://developer.apple.com/documentation/safariservices/sfsafariviewcontroller) on iOS instead. For more information on security best practices, see [Use secure browsers](https://developers.google.com/identity/protocols/oauth2/resources/best-practices#use-secure-browsers).

The JavaScript client library for Sign In With Google and Google One Tap is
designed to be compatible with most common browsers and platforms. It is
not guaranteed to work on all browsers or platforms.

Due to security risks the JavaScript client library is only supported
on the latest two versions of each browser.

## Compatibility

Support for the Sign In With Google button and One Tap sign-in flows varies
across browser and platform combinations.

The user experience may differ between browsers based upon availability of
these features:

- [Intelligent Tracking Prevention](https://webkit.org/blog/9521/intelligent-tracking-prevention-2-3/) (ITP)
- [Federated Credentials Management API](https://developers.google.com/privacy-sandbox/3pcd/fedcm) (FedCM)

Supported sign-in flows and features are shown in the following tables. Not all
browsers are available on all platforms, N/A means a supported browser is not
available on the platform.

### Sign In With Google

| Browser / Platform | Android | iOS ^\*^ | macOS | Linux | Windows 10 |
| Chrome | Yes | Yes | Yes | Yes | Yes |
| Edge | Yes | Yes | Yes | Yes | Yes |
| Firefox | Yes | Yes | Yes | Yes | Yes |
| Safari | N/A | Yes | Yes | N/A | N/A |
|---|---|---|---|---|---|

^\*^ Due to ITP [redirect mode](https://developers.google.com/identity/gsi/web/guides/display-button#redirect_mode) is required for iOS.

### One Tap

| Browser / Platform | Android | iOS | macOS | Linux | Windows 10 |
| Chrome | Yes | Yes | Yes | Yes | Yes |
| Edge | Yes | Yes | Yes | Yes | Yes |
| Firefox | Yes | No | Yes | Yes | Yes |
| Safari | N/A | Yes | Yes | N/A | N/A |
|---|---|---|---|---|---|

> [!NOTE]
> **Note:** [Check the latest supported browsers for FedCM.](https://caniuse.com/?search=fedcm) Consider [enabling
> ITP](https://developers.google.com/identity/gsi/web/reference/js-reference#itp_support) support to ensure users receive the [upgraded One Tap UX](https://developers.google.com/identity/gsi/web/guides/features#upgraded_ux_on_itp_browsers).

## Third-party cookies

As a participant in the W3C [FedID](https://www.w3.org/community/fed-id/) community group working on [FedCM](https://developers.google.com/privacy-sandbox/3pcd/fedcm),
Google Identity Services has been working to increase user privacy and security
while also minimizing the changes to existing websites and preserving ease of
use for our users. The GIS JavaScript library now supports the proposed FedCM
API.

As of August 2023, Google Identity Services fully supports FedCM and recommends
its use. Changes to [adopt FedCM](https://developers.google.com/identity/gsi/web/guides/fedcm-migration) may be required for some existing web apps.

> [!IMPORTANT]
> **Important:** When testing sign-in and third-party cookie blocking, you should start by updating to the latest stable version of Chrome.

Recommended

- [Enable FedCM](https://developers.google.com/identity/gsi/web/reference/js-reference#use_fedcm_for_button) for new web apps and [migrate](https://developers.google.com/identity/gsi/web/guides/fedcm-migration) existing apps.

Not Recommended

- Disabling FedCM.

As of August 2022, Google Identity Services has conducted a limited
[FedCM origin trial](https://developer.chrome.com/blog/fedcm-origin-trial/). Approximately 20 websites and 300K users successfully
signed in using FedCM APIs and GIS.

We're pleased to say early feedback has demonstrated that for most websites,
switching to a more private and secure sign-in process without third-party
cookies can occur transparently through backward compatible updates to the
existing GIS library. **Minimal to no changes to existing user flows and
websites was required.** This is a critical point as widespread adoption of
FedCM APIs relies on a trouble-free migration by existing websites.

Based upon this preliminary feedback, GIS plans to expand participation in
testing GIS with FedCM.

During trials these issues were discovered and may require some web sites to
take action when FedCM is adopted by GIS:

- Browser rendered dialogs eliminate the existing ability for sites to use style attributes or intermediate iframes to control sign-in dialog positioning. This may obscure existing site content, some of which may be helpful or critical for users to see before signing in.
- Although not yet widely deployed, some sites may use CSP and COOP. In these cases, sites may have to make [changes](https://developers.google.com/identity/gsi/web/guides/get-google-api-clientid#content_security_policy) to direct browsers to allow popups and to load cross-site resources.