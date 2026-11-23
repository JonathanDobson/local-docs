---
source: https://developers.google.com/identity/gsi/web/guides/features
markdown_source: https://developers.google.com/identity/gsi/web/guides/features.md.txt
title: "Understand the One Tap user experience  |  Web guides  |  Google for Developers"
fetched: 2026-11-23
---

This guide contains detailed descriptions of the One Tap user experience,
including when One Tap is or is not displayed and user session behaviors.

## Globally opt out

Users can opt out of One Tap if they disable the Google Account sign-in prompts
flag in the [Apps with access to your account](https://myaccount.google.com/permissions) page. The opted-out sessions
aren't shown in One Tap. If all Google sessions are opted out, One Tap doesn't
display.

If a user disables third-party sign-in on browsers with [FedCM enabled](https://developers.google.com/identity/gsi/web/guides/overview.md.txt#federated_credential_manager_fedcm), One
Tap is not displayed. In Chrome settings under the Privacy and Security section
users control the display of [third-party sign-in](https://support.google.com/chrome/answer/14264742) prompts either globally
or for individual sites.

## Exponential cooldown

If the user closes the One Tap prompt manually, the One Tap prompt is
suppressed. A user closes One Tap when they tap **Close**
in the
top-right corner of the prompt, after which One Tap wouldn't display in the
same browser or the last website visited for a period of time.

The following exponential time periods are used for cooldowns when FedCM is
**not** enabled:

| Consecutive times closed | Time period that One Tap is disabled |
|---|---|
| 1 | Two hours |
| 2 | One day |
| 3 | One week |
| 4+ | Four weeks |

The cooldown status resets after a successful sign-in using One Tap or the Sign
in with Google button.

When FedCM is enabled, browser vendors may define their own, different, cooldown
time periods.

> [!NOTE]
> **Note:** When FedCM is enabled, Chrome users can reset cooldown status by clicking on the lock icon in the address bar and clicking the *Reset Permission* button.

## Auto-dismissal on mobile browsers

On **mobile** browsers, and when FedCM is not enabled, Google One Tap closes
automatically after a short time period unless the user directly interacts with
the One Tap UI.

The threshold for auto-dismissal is 90 seconds. This is subject to change.

> [!NOTE]
> **Note:** Auto-dismissal doesn't trigger a cooldown. Auto-dismissal doesn't happen on desktop, iPad, and tablet browsers.

## Show a dialog to prevent unintended clicks

> [!NOTE]
> **Objective:** It's important that users understand the purpose of One Tap. They should be fully aware of the call to action when they give their consent to create an account, since they must share some personal information, such as their first name, last name, email, and profile picture.

One Tap now comes with different security measures to enforce the integrity of
the dialog, but some browsers don't support these capabilities. Unsupported
browsers include non-Chromium-based ones or those before v75. In these cases, or
if the dialog is covered with other content, a pop-up window is displayed that
requests the user's consent to create an account.

![**Figure 3.** Sign-in dialog box](https://developers.google.com/static/identity/gsi/web/images/sign-in-dialog-box.png)

## Upgraded UX on ITP browsers

Due to
[Intelligent Tracking Prevention](https://webkit.org/blog/9521/intelligent-tracking-prevention-2-3/) (ITP), the
normal One Tap UX doesn't work on Chrome on iOS, Safari, or Firefox. A different
UX is provided instead on these browsers. You have the option to disable this UX
on ITP browsers by setting the [`data-itp_support`](https://developers.google.com/identity/gsi/web/reference/html-reference.md.txt#data-itp_support) attribute.

The upgraded One Tap UX on ITP browsers begins with a welcome page as shown
below. After the user selects Continue, a pop-up window is opened. The UX in the
pop-up window is very similar to normal One Tap.

![**Figure 4.** Welcome Page](https://developers.google.com/static/identity/gsi/web/images/warm-welcome.png)

When there is no Google session, after the 'Continue' button is clicked, users
must first sign in to their Google Account. See
[One Tap support on ITP browsers](https://developers.google.com/identity/gsi/web/guides/itp) for more details.

> [!NOTE]
> **Note:** To avoid the flashing pop-up issue, auto sign in isn't supported.

## Key user journeys

> [!NOTE]
> **Note:** Refer to [Automatic sign-in key user journeys](https://developers.google.com/identity/gsi/web/guides/automatic-sign-in-sign-out.md.txt#key_user_journeys) for the UX flow when automatic sign-in is enabled.

The user journeys vary based on the following statuses.

- Session status on Google websites. The following terms are used to indicate
  different Google session status when the user journey starts.

  - Single-session: There is exactly one active session on Google websites.
  - Multiple-session: There are more than one active sessions on Google websites.

  > [!IMPORTANT]
  > **Key Point:** One Tap is not shown if there is no active session on Google websites.

- Whether the selected Google Account has approved your website when the user
  journey starts. The following terms are used to indicate different approval
  status.

  - New user: The selected account hasn't approved your website.
  - Returning user: The selected account has approved your website before.

### Single-session new user journey

1. The new user consent page.

   ![Google One Tap consent page](https://developers.google.com/static/identity/gsi/web/images/one-tap-ui-fedcm.png)
2. The second confirmation dialog in a pop-up window for non-Chromium browsers.

   ![Consent page in a pop-up window for non-Chromium browsers.](https://developers.google.com/static/identity/gsi/web/images/sign-in-dialog-box.png)
3. After users confirm, an ID token is shared with your website.

### Single-session returning user journey

1. The returning user page.

   ![One Tap returning user page](https://developers.google.com/static/identity/gsi/web/images/one-tap-sign-in-fedcm.png)
2. After users click the button, an ID token is shared with your website.

### Multiple-session new user journey

1. The account chooser page.

   ![Account Chooser Page](https://developers.google.com/static/identity/gsi/web/images/one-tap-ac-fedcm.png)
2. The consent page.

   ![Google One Tap consent page](https://developers.google.com/static/identity/gsi/web/images/one-tap-ui-fedcm.png)

   For non-Chromium browsers, this confirmation dialog is displayed in a
   pop-up window:

   ![Consent page in a pop-up window for non-Chromium browsers.](https://developers.google.com/static/identity/gsi/web/images/sign-in-dialog-box.png)
3. After user consent, an ID token is shared with your website.

### Multiple-session returning user journey

1. The account chooser page.

   ![Account Chooser Page](https://developers.google.com/static/identity/gsi/web/images/one-tap-ac-fedcm.png)
2. After users select a returning account, an ID token is shared with your
   website.