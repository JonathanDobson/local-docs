---
source: https://developers.google.com/identity/gsi/web/guides/change-position
markdown_source: https://developers.google.com/identity/gsi/web/guides/change-position.md.txt
title: "Change the One Tap prompt position  |  Web guides  |  Google for Developers"
fetched: 2026-11-23
---

# Change the One Tap prompt position

> [!WARNING]
> **Warning:** When One Tap migrates to use the [FedCM API](https://developers.googleblog.com/2024/02/federated-credential-management-migration-for-google-identity-services.html), the browser controls the size and position of One Tap prompt. Custom positions are not supported. For new One Tap integration, you shouldn't customize the prompt's position. For existing integration, review the [migration guide](https://developers.google.com/identity/gsi/web/guides/fedcm-migration#layout) and update your app if necessary.

> [!NOTE]
> **Objective:** If the default login flow doesn't meet your requirements, you can customize it in several ways. Read the following information for available customization options.

By default, the One Tap prompt is displayed in the top-right corner of desktop
web browser windows. When [FedCM](https://developers.google.com/identity/gsi/web/guides/supported-browsers#compatibility) is used, browser fully controls the
prompt location. Hence, custom layouts are **not** supported.

Otherwise, display One Tap inside a container element to change prompt position.
To do so, specify the DOM ID of the container element in the
`data-prompt_parent_id` attribute.

> [!WARNING]
> **Warning:** Don't hide any One Tap prompt content. Don't obscure the perception that the One Tap prompt content is from a Google iframe. Failure to do so may result in project suspension, account suspension, or both.

The following code example reuses the `g_id_onload` element as the container
element and displays the One Tap prompt in the specified position:

    <div id="g_id_onload"
         data-client_id="YOUR_GOOGLE_CLIENT_ID"
         data-login_uri="https://your.domain/your_login_endpoint"
         data-prompt_parent_id="g_id_onload"
         style="position: absolute; top: 100px; right: 30px;
                width: 0; height: 0; z-index: 1001;">
    </div>

The `data-prompt_parent_id` attribute is ignored on mobile web browsers.