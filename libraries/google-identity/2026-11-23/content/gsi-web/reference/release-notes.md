---
source: https://developers.google.com/identity/gsi/web/reference/release-notes
markdown_source: https://developers.google.com/identity/gsi/web/reference/release-notes.md.txt
title: "Sign In With Google Release Notes  |  Web guides  |  Google for Developers"
fetched: 2026-11-23
---

# Sign In With Google Release Notes

This page contains a list of the new features and significant changes to the
Google Identity Services JavaScript library.

## 2025-03-17

- [Sign in with Google button](https://developers.google.com/identity/gsi/web/guides/personalized-button) supports [Federated Credential Management (FedCM)](https://developers.google.com/privacy-sandbox/cookies/fedcm) and adhere to [Google Workspace](https://workspace.google.com/) policies set by the organization's administrator.

## 2024-12-01

- [Sign in with Google button](https://developers.google.com/identity/gsi/web/guides/personalized-button) supports [Family Link](https://families.google/familylink/) and adhere to [Google Workspace](https://workspace.google.com/) policies set by the organization's administrator.

## 2023-12-21

- [Federated Credential Management (FedCM) Beta](https://developers.googleblog.com/2023/08/announcing-federated-credential-management-beta-for-gis.html) for Google Identity
  Services was launched in August 2023. Many developers tested the API and have
  provided valuable feedback.

  One response Google heard from developers is about the FedCM automatic sign-in
  flow user gesture requirement. For improved privacy, Chrome requires users to
  reconfirm that they want to sign in to the website with Google Account in each
  Chrome instance even if the user approved the website prior to the FedCM
  rollout. This one-time reconfirmation is achieved through a single click of
  the One Tap prompt to demonstrate user intent to sign-in. This change may
  cause an initial disruption in automatic sign-in conversion rates for some
  websites.

  Recently in M121, Chrome made a [change](https://developers.google.com/privacy-sandbox/3pcd/fedcm-updates#chrome_121_december_2023) to the FedCM automatic sign-in
  flow UX. The reconfirmation is only required when third-party cookies are
  restricted. This means:
  1. Before third-party cookie restrictions are ramped up to 100% (see Privacy
     Sandbox [News and Update](https://privacysandbox.com/news/) page for latest timeline),
     FedCM automatic sign-in does not require reconfirmation for returning users.
     If users reconfirm with FedCM UI, this reconfirmation will count toward the
     user gesture requirement.

  2. FedCM automatic sign-in will check the confirmation status when the
     third-party cookies are manually restricted by users today, or by default in
     future Chrome.

  With this change, we recommend all automatic sign-in developers migrate to
  FedCM as soon as possible, to reduce disruption to automatic sign-in
  conversion rates.

  For the automatic sign-in flow, GIS JavaScript won't trigger FedCM on an older
  Chrome (before M121), even if your website chooses to opt-in to FedCM.

## 2023-08-15

- Added [support](https://developers.google.com/identity/gsi/web/guides/supported-browsers#third-party_cookies) for the Federated Credential Management API (FedCM).
- [Accelerated Mobile Pages](https://developers.google.com/identity/gsi/web/amp/amp) is unsupported. AMP is not available when FedCM is enabled.

## 2022-04-12

- [Upgraded One Tap UX on ITP browsers](https://developers.google.com/identity/gsi/web/guides/features#upgraded_ux_on_itp_browsers) is supported.

## 2021-4-13

- [Sign In With Google button](https://developers.google.com/identity/gsi/web/guides/personalized-button) is supported.

## 2021-03-17

- [Accelerated Mobile Pages](https://developers.google.com/identity/gsi/web/amp/amp) is supported.

## 2020-3-24

- [Exponential Cool Down](https://developers.google.com/identity/gsi/web/guides/features#exponential_cool_down) is supported.