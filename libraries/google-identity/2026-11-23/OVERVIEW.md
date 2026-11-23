# Google Identity Services: Sign in with Google for Web (snapshot 2026-11-23)

Google's documentation for **Sign in with Google for Web**: the Google Identity
Services (GIS) JavaScript library loaded from `https://accounts.google.com/gsi/client`,
which shows the **Sign In With Google button** and the **One Tap** prompt and hands your
site a signed **ID token** (a JSON Web Token, JWT). Neither the site nor the library has
version numbers, so this set is a **dated snapshot fetched on 2026-11-23** from
developers.google.com, using the Markdown Google publishes for each page
(`<page URL>.md.txt`). It also holds the Sign in with Google branding guidelines and
Google's OpenID Connect page, which defines the ID token's claims. For the server-side
Node.js verifier, see the separate `google-auth-library` set.

## Layout

| Folder | What it holds |
|---|---|
| `content/gsi-web/guides/` | How-to guides: overview, setup (client ID, origins, CSP, COOP), button, One Tap, automatic sign-in/out, FedCM migration, server-side verification, migration from the old Google Sign-In platform library |
| `content/gsi-web/reference/` | `js-reference.md` (the `google.accounts.id.*` JavaScript API), `html-reference.md` (the `g_id_onload` / `g_id_signin` `data-*` attributes), `release-notes.md` |
| `content/gsi-web/amp/` | Accelerated Mobile Pages (AMP) and intermediate-iframe pages (AMP is not supported once FedCM is on) |
| `content/branding/index.md` | Sign in with Google branding guidelines (button text, colours, logo use, custom buttons) |
| `content/openid-connect/openid-connect.md` | Google's OpenID Connect: ID token claims (`sub`, `email_verified`, `hd`, `nonce`…), discovery document |

## Where to look for…

| Task | File |
|---|---|
| What Sign in with Google is, One Tap vs button | `gsi-web/guides/overview.md`, `gsi-web/guides/features.md` |
| Create the OAuth client ID, **authorized JavaScript origins** (add both `http://localhost` and `http://localhost:<port>`), `Referrer-Policy` for localhost | `gsi-web/guides/get-google-api-clientid.md` |
| **Content Security Policy** (`script-src https://accounts.google.com/gsi/client`, `frame-src`/`connect-src https://accounts.google.com/gsi/`, `style-src https://accounts.google.com/gsi/style`) and **COOP** (`same-origin-allow-popups` when FedCM is off) | `gsi-web/guides/get-google-api-clientid.md` (CSP and COOP sections) |
| `google.accounts.id.initialize`, `IdConfiguration` fields (`client_id`, `callback`, `login_uri`, `nonce`, `ux_mode`, `context`, `itp_support`, `use_fedcm_for_button`, `button_auto_select`, `hd`, `login_hint`…) | `gsi-web/reference/js-reference.md` |
| `renderButton` and `GsiButtonConfiguration` (type, theme, size, text, shape, logo_alignment, width, locale, state) | `gsi-web/reference/js-reference.md`, `gsi-web/guides/display-button.md`, `gsi-web/guides/personalized-button.md` |
| `prompt`, `cancel`, `PromptMomentNotification` | `gsi-web/reference/js-reference.md`, `gsi-web/guides/display-google-one-tap.md` |
| `CredentialResponse` (`credential`, `select_by`, `state`) | `gsi-web/reference/js-reference.md` ("Data type: CredentialResponse") |
| Doing it all in HTML (`data-client_id`, `data-login_uri`, `data-ux_mode`, `data-use_fedcm_for_button`…) | `gsi-web/reference/html-reference.md` |
| **Verify the ID token on the server**: `g_csrf_token` double-submit check (redirect mode), `aud`/`iss`/`exp`/`hd` checks, Node.js `verifyIdToken` example | `gsi-web/guides/verify-google-id-token.md` |
| Sign-out, `disableAutoSelect`, auto sign-in | `gsi-web/guides/automatic-sign-in-sign-out.md`, `js-reference.md` |
| Revoke consent (`google.accounts.id.revoke`) | `gsi-web/guides/revoke.md` |
| **FedCM** migration: what to remove, prompt position, browser support | `gsi-web/guides/fedcm-migration.md`, `gsi-web/guides/supported-browsers.md` |
| Migrating from the old Google Sign-In (`gapi.auth2`, platform.js) | `gsi-web/guides/migration.md` |
| Button branding rules / custom buttons | `branding/index.md` |
| What each ID token claim means | `openid-connect/openid-connect.md` |

## Version notes (as of 2026-11-23)

- **`use_fedcm_for_prompt` is deprecated and ignored** ("This attribute is deprecated
  and will be ignored if used", `js-reference.md`), so you can't use it to switch FedCM
  for One Tap on or off. See `supported-browsers.md` for which browsers use FedCM.
- **`use_fedcm_for_button`** opts the button into FedCM UX on Chrome (desktop M125+,
  Android M128+). Default `false`. **`button_auto_select`** (default `false`) turns on
  auto select for the FedCM button flow.
- FedCM migration says to **remove** `isDisplayMoment()`, `isDisplayed()`,
  `isNotDisplayed()`, `getNotDisplayedReason()` and `getSkippedReason()` from One Tap
  code, and not to rely on custom One Tap positions: the browser places the prompt.
- **COOP**: when FedCM is enabled no changes are needed. When it is disabled, set
  `Cross-Origin-Opener-Policy` to `same-origin` and include `same-origin-allow-popups`,
  or popups come up blank.
- Release notes (latest entry 2025-03-17): the button supports FedCM and follows
  Google Workspace admin policies. 2023-08-15: FedCM support added and AMP unsupported.
- `ux_mode` defaults to `popup` and only affects the button, not One Tap. With the JS API,
  One Tap and popup responses only reach the `callback` function. For an automatic POST
  to `login_uri`, use redirect mode or the HTML API. `select_by` is **not** included in
  the POST to `login_uri`.
- `login_uri` must exactly match an authorized redirect URI of the OAuth client.
- The verify page does not mention `nonce`. If you pass `nonce` to `initialize`, compare
  the token's `nonce` claim yourself (the OpenID Connect page says to present a nonce only
  once). `google-auth-library`'s `verifyIdToken` checks signature, `aud`, `iss` and the
  expiry/issue times, not the nonce.

## Search tips

- The JS namespace is `google.accounts.id`. The HTML API uses `<div id="g_id_onload">`
  and `<div class="g_id_signin">` with `data-` versions of the same field names
  (`data-client_id`, `data-login_uri`).
- The config object is called **`IdConfiguration`**; button options are
  **`GsiButtonConfiguration`**; the callback argument is **`CredentialResponse`**; its
  `credential` field is the ID token (a JWT).
- "One Tap" is the prompt; "personalized button" is the button showing the user's
  name/picture; "ITP" means Intelligent Tracking Prevention (browsers such as Safari and Chrome on iOS,
  where normal One Tap doesn't work; see `integrate.md`);
  "FedCM" means Federated Credential Management, the browser API that replaces
  third-party cookies.
- The CSRF cookie and form field in redirect mode are both named `g_csrf_token`.
- Links inside pages are absolute developers.google.com URLs, some ending in `.md.txt`.
  Find the local file by path (`.../guides/display-button` → `gsi-web/guides/display-button.md`).
