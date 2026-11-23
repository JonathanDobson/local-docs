---
source: https://developers.google.com/identity/gsi/web/guides/personalized-button
markdown_source: https://developers.google.com/identity/gsi/web/guides/personalized-button.md.txt
title: "Sign in with Google button UX  |  Web guides  |  Google for Developers"
fetched: 2026-11-23
---

This page describes the user experience (UX) of the Sign in with Google button.

## Button rendering

A personalized button displays profile information for the first Google session
that approves your website. An approved Google session has a corresponding
account on your website who has signed in using Sign In With Google before.

If a personalized button is displayed, the user knows the following:

- There's at least one active Google session.
- There's a corresponding account on your website.

A personalized button gives users a quick indication of the session status, both
on Google's side and on your website, before they click the button. This is
especially helpful to end users who visit your website only occasionally. They
may forget whether an account has been created or not, and in which way. A
personalized button reminds them that Sign In With Google has been used before.
Thus, it helps to prevent unnecessary duplicate account creation on your
website.

To indicate the session status, the personalized button is displayed in the
following ways:

- **One session:** There's only one session on Google's side. That session
  approves the client, and there's a corresponding account on your website.

  ![A personalized button that displays the name of a single Google Account.](https://developers.google.com/static/identity/gsi/web/images/personalized-button-single.png)
- **Multiple sessions:** There are multiple sessions on Google's side. Those
  sessions approve the client. The approval is indicated by the list arrow
  next to the displayed account. At least one session has a corresponding
  account on your website.

  ![A personalized button with a list arrow.](https://developers.google.com/static/identity/gsi/web/images/personalized-button-multiple.png)
- **No session:** There's no session on Google's side, or none of the sessions
  have approved the client yet.

  ![A button that says 'Sign in with Google' without personalized information.](https://developers.google.com/static/identity/gsi/web/images/standard-button-white.png)

The personalized button is automatically displayed when the session status
is suitable, unless your button settings don't allow the personalized button to
be displayed. The personalized button is not displayed if:

- The `data-type` attribute is `icon`.
- The `data-size` attribute is set to `medium` or `small`.
- The `data-width` attribute is set to a number smaller than 200px.
- Third-party cookie is blocked, and [FedCM version](https://developers.google.com/identity/gsi/web/guides/personalized-button#federated_credential_manager_fedcm) of button is not enabled.

The name or email address is ellipsized when they are too long to be displayed
inside the button.

![A personalized button with ellipsized name and email.](https://developers.google.com/static/identity/gsi/web/images/personalized-button-ellipsized.png)

> [!IMPORTANT]
> **Key Point:** The [Code Generator](https://developers.google.com/identity/gsi/web/tools/configurator) developer tool can help you design the Sign In With Google button interactively and generate the code.

## Federated Credential Manager (FedCM)

[Privacy Sandbox for the Web](https://privacysandbox.com/intl/en_us/open-web/#how-works-on-web-hero) introduces significant changes to Google
Identity Services and user sign in. It impacts the Sign in with Google
personalized button. While sign-in flow is unaffected with the
button, with 3rd-party cookies blocked, your returning users wouldn't see
the personalized button.

With [Federated Credentials Management](https://developer.chrome.com/en/docs/privacy-sandbox/fedcm/) API (FedCM) button flow, users
would be able to see the personalized Sign in with Google button on your site.
By default, FedCM is disabled, but you can enable FedCM by changing one
attribute ([HTML](https://developers.google.com/identity/gsi/web/reference/html-reference#data-use_fedcm_for_button)/[JavaScript](https://developers.google.com/identity/gsi/web/reference/js-reference#use_fedcm_for_button)). The benefits of the FedCM
button include:

- **Improved Returning User Experience** : The returning user sign-in process is
  streamlined because users can recognize their existing accounts. This
  improved recognition is proven to lead to a higher click-through rate (CTR).
  Furthermore, unlike the button flow without having FedCM enabled, the FedCM
  button flow supports the [automatic select](https://developers.google.com/identity/gsi/web/guides/personalized-button#auto-select) feature - returning
  users with an active Google session will be automatically signed in after
  clicking the button, bypassing the Account Chooser prompt.

- **Enhanced Feature Integration**: We've integrated One Tap and Auto Sign-in
  functionalities, enabling all Federated Credential Management (FedCM) Sign-in
  with Google features from a single Relying Party (RP) to work in concert. The
  user gestures in the FedCM button flow will be recorded and honored by Chrome
  to fulfill the one-time reconfirmation for One Tap auto sign-in flow. This
  ensures a seamless experience across all features.

## Key user journeys

> [!IMPORTANT]
> **Key Point:** Whether a personalized button or a generic text button displays has no impact on the UX flows after the button is clicked. The account displayed in the personalized button is not automatically selected.

> [!IMPORTANT]
> **Key Point:** The Sign in with Google button flow doesn't support automatic sign-in. A user action is required to select the right session, even when there is only one active Google session.

The user journeys vary based on the following statuses.

- Session status on Google websites. The following terms are used to indicate
  different Google session status when the user journey starts.

  - **Has-Google-session**: There is at least one active session on Google websites.
  - **No-Google-session**: There is no active session on Google websites.
- Whether the selected Google Account has approved your website when the user
  journey starts. The following terms are used to indicate different approval
  status.

  - **New user**: The selected account hasn't approved your website.
  - **Returning user**: The selected account has approved your website before.

### Has-Google-session new user journey

### Button without FedCM

1. The Sign in with Google button.

   ![A button that says 'Sign in with Google' without personalized information.](https://developers.google.com/static/identity/gsi/web/images/standard-button-white.png)
2. The account chooser page.

   ![Has-Initial-Session Account Chooser Page.](https://developers.google.com/static/identity/gsi/web/images/account-chooser-oauth.png)
3. The new user consent page.

   ![Sign In With Google button consent and sign-in.](https://developers.google.com/static/identity/gsi/web/images/sign-in-dialog-box-oauth.png)
4. After the user confirms, an ID token is shared with your website.

Users can add a new Google session by clicking the **Use another account**
button, refer to the **No-Google-session** user journeys section.

### Button using FedCM

[![With FedCM enabled - Has-Google-session new user journey](https://developers.google.com/static/identity/gsi/web/images/fedcm-button/Has-Google-session-new-user-journey.png)](https://developers.google.com/static/identity/gsi/web/images/fedcm-button/Has-Google-session-new-user-journey.png)

The second last screen in the flow is the loading screen, which
automatically redirects users to your [login endpoint](https://developers.google.com/identity/gsi/web/guides/display-button#your_login_endpoint_uri) without
action from users.

### Has-Google-session returning user journey

### Button without FedCM

1. The Sign in with Google button.

   ![A personalized button that displays the name of a single Google Account.](https://developers.google.com/static/identity/gsi/web/images/personalized-button-single.png)
2. The account chooser page.

   ![Google Account chooser](https://developers.google.com/static/identity/gsi/web/images/account-chooser-oauth.png)
3. After the user chooses a returning account, an ID token is shared with
   your website.

Users can add a new Google session by clicking the **Use another account**
button, refer to the 'No-Google-session' user journeys section.

### Button using FedCM

[![With FedCM enabled - Has-Google-session returning user journey](https://developers.google.com/static/identity/gsi/web/images/fedcm-button/Has-Google-session-returning-user-journey.png)](https://developers.google.com/static/identity/gsi/web/images/fedcm-button/Has-Google-session-returning-user-journey.png)

The second last screen in the flow is the loading screen, which
automatically redirects users to your [login endpoint](https://developers.google.com/identity/gsi/web/guides/display-button#your_login_endpoint_uri) without
action from users.

### Has-Google-session with auto select returning user journey

### Button without FedCM

Sign in with Google button without FedCM doesn't have automatic select
feature.

### Button using FedCM

Returning users with an active Google session will be automatically selected
after clicking the button, bypassing the Account Chooser prompt. Set
the `auto select` attribute to true ([HTML](https://developers.google.com/identity/gsi/web/reference/html-reference#data-button_auto_select)/[JavaScript](https://developers.google.com/identity/gsi/web/reference/js-reference#button_auto_select)).

[![With FedCM and auto sign-in enabled - Has-Google-session with auto sign-in returning user journey](https://developers.google.com/static/identity/gsi/web/images/fedcm-button/Has-Google-session-with-auto-sign-in-returning-user-journey.png)](https://developers.google.com/static/identity/gsi/web/images/fedcm-button/Has-Google-session-with-auto-sign-in-returning-user-journey.png)

### No-Google-session new user journey

### Button without FedCM

1. The Sign in with Google button.

   ![A button that says 'Sign in with Google' without personalized information.](https://developers.google.com/static/identity/gsi/web/images/standard-button-white.png)
2. The first page to add a new Google session.

   ![Google Account Email](https://developers.google.com/static/identity/gsi/web/images/google-account-id-oauth.png)
3. The second page to add a new Google session.

   ![Google Account sign-in](https://developers.google.com/static/identity/gsi/web/images/google-account-signin-oauth.png)
4. The new user consent page.

   ![Sign In With Google button consent and sign-in.](https://developers.google.com/static/identity/gsi/web/images/sign-in-dialog-box-oauth.png)
5. After the user confirms, an ID token is shared with your website.

### Button using FedCM

[![With FedCM enabled - Has-Google-session returning user journey](https://developers.google.com/static/identity/gsi/web/images/fedcm-button/No-Google-session-new-user-journey.png)](https://developers.google.com/static/identity/gsi/web/images/fedcm-button/No-Google-session-new-user-journey.png)

The second last screen in the flow is the loading screen, which
automatically redirects users to your [login endpoint](https://developers.google.com/identity/gsi/web/guides/display-button#your_login_endpoint_uri) without
action from users.

### No-Google-session returning user journey

### Button without FedCM

1. The Sign in with Google button.

   ![A button that says 'Sign in with Google' without personalized information.](https://developers.google.com/static/identity/gsi/web/images/standard-button-white.png)
2. The first page to add a new Google session.

   ![Google Account Email](https://developers.google.com/static/identity/gsi/web/images/google-account-id-oauth.png)
3. The second page to add a new Google session.

   ![Google Account sign-in](https://developers.google.com/static/identity/gsi/web/images/google-account-signin-oauth.png)
4. After the user clicks the **Next** button, an ID token is shared with
   your website.

### Button using FedCM

[![With FedCM enabled - Has-Google-session returning user journey](https://developers.google.com/static/identity/gsi/web/images/fedcm-button/No-Google-session-returning-user-journey.png)](https://developers.google.com/static/identity/gsi/web/images/fedcm-button/No-Google-session-returning-user-journey.png)

## Family Link account key user journeys

The general key user journeys from the previous section still apply. The
following shows the additional flow would be presented for child's
Google Account when signing in.

### Button without FedCM

### No-Google-session

1. The Sign in with Google button.

   ![A button that says 'Sign in with Google' without personalized information.](https://developers.google.com/static/identity/gsi/web/images/standard-button-white.png)
2. The first page to add a new child Google session (child Google Account email).

   ![Child Google Account email](https://developers.google.com/static/identity/gsi/web/images/familylink/has-no-session/child-account-id.png)
3. The second page to add a new child Google session (child Google Account password).

   ![Child Google Account password](https://developers.google.com/static/identity/gsi/web/images/familylink/has-no-session/child-password.png)
4. The first page to get approval from parent to add a new child Google session.

   ![Parent's approval selection page](https://developers.google.com/static/identity/gsi/web/images/familylink/has-no-session/choose-a-parent.png)
5. The second page to get approval from parent to add a new child Google session.

   ![Parent's approval password page](https://developers.google.com/static/identity/gsi/web/images/familylink/has-no-session/parent-password.png)
6. The third page to get approval from parent to add a new child Google session.

   ![Parent's approval page](https://developers.google.com/static/identity/gsi/web/images/familylink/has-no-session/sign-in-child-device.png)
7. The first page to get approval from parent to sign in a child Google Account to the application.

   ![Get parent to approve sign in page](https://developers.google.com/static/identity/gsi/web/images/familylink/has-no-session/get-your-parent.png)
8. The second page to get approval from parent to sign in a child Google Account to the application.

   ![Choose a parent to approve sign in page](https://developers.google.com/static/identity/gsi/web/images/familylink/has-no-session/parent-account-chooser.png)
9. The third page to get approval from parent to sign in a child Google Account to the application.

   ![Password for the parent Google Account to approve sign in page](https://developers.google.com/static/identity/gsi/web/images/familylink/has-no-session/parent-password-consent.png)
10. The final page to get approval from parent to sign in a child Google Account to the application.

    ![Parental approval for child to sign in page](https://developers.google.com/static/identity/gsi/web/images/familylink/has-no-session/parent-consent.png)
11. After the parent clicks the **Continue** button, an ID token is shared with your website.

### Has-Google-session

1. The Sign in with Google button.

   ![A button that says 'Sign in with Google' without personalized information.](https://developers.google.com/static/identity/gsi/web/images/standard-button-white.png)
2. The account chooser page.

   ![Choose the child account page.](https://developers.google.com/static/identity/gsi/web/images/familylink/has-session/child-account-chooser.png)
3. The first page to get approval from parent to sign in a child Google Account to the application.

   ![Get parent to approve sign in page](https://developers.google.com/static/identity/gsi/web/images/familylink/has-session/get-your-parent.png)
4. The second page to get approval from parent to sign in a child Google Account to the application.

   ![Choose a parent to approve sign in page](https://developers.google.com/static/identity/gsi/web/images/familylink/has-session/parent-account-chooser.png)
5. The third page to get approval from parent to sign in a child Google Account to the application.

   ![Password for the parent Google Account to approve sign in page](https://developers.google.com/static/identity/gsi/web/images/familylink/has-session/parent-password.png)
6. The final page to get approval from parent to sign in a child Google Account to the application.

   ![Parental approval for child to sign in page](https://developers.google.com/static/identity/gsi/web/images/familylink/has-session/parent-consent.png)
7. After the parent clicks the **Continue** button, an ID token is shared with your website.

### Button using FedCM

Sign in with Google Button with FedCM enabled doesn't support Family Link
accounts at the moment.

## Additional information on FedCM button flow

- Add `allow="identity-credentials-get"` attribute to parent frame if your
  web app calls Button API from cross-origin iframes. See [step 7](https://developers.google.com/identity/gsi/web/guides/fedcm-migration#cross_origin)
  for more information.

- Properly set up the Content Security Policy (CSP) of your site. See
  [step 8](https://developers.google.com/identity/gsi/web/guides/fedcm-migration#csp) for more information.

- The cooldown status and Third-party sign-in settings in Chrome have no
  impact on the FedCM button flow. The status (as shown in the following
  screenshots) affects One Tap UX only.

  [![The cooldown status and Third-party sign-in settings in Chrome have no
  impact on the FedCM button flow.](https://developers.google.com/static/identity/gsi/web/images/fedcm-button/browser_settings.png)](https://developers.google.com/static/identity/gsi/web/images/fedcm-button/browser_settings.png)