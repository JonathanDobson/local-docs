---
source: https://developers.google.com/identity/gsi/web/guides/display-browsers-native-credential-manager
markdown_source: https://developers.google.com/identity/gsi/web/guides/display-browsers-native-credential-manager.md.txt
title: "Display the browser's native credential manager  |  Web guides  |  Google for Developers"
fetched: 2026-11-23
---

# Display the browser&#39;s native credential manager

> [!NOTE]
> **Objective:** If the default login flow doesn't meet your requirements, you can customize it in several ways. Read the following information for available customization options.

A browser's native credential manager stores a user's password credentials. To
enable the browser's native credential manager, set the `data-native_login_uri`
attribute.

The One Tap prompt and the native credential manager dialog aren't displayed
together on the same page. The native dialog is only displayed when the One Tap
prompt isn't displayed. See the following code example:

    <div id="g_id_onload"
         data-client_id="YOUR_GOOGLE_CLIENT_ID"
         data-login_uri="https://your.domain/your_login_endpoint"
         data-native_login_uri="https://your.domain/your_password_login_endpoint">
    </div>