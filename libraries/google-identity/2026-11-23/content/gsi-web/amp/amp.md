---
source: https://developers.google.com/identity/gsi/web/amp/amp
markdown_source: https://developers.google.com/identity/gsi/web/amp/amp.md.txt
title: "Display One Tap in AMP pages  |  Authentication  |  Google for Developers"
fetched: 2026-11-23
---

# Display One Tap in AMP pages

To add One Tap to your Accelerated Mobile Pages,

1. Add One Tap into an intermediate Iframe hosted by your own website.

2. Embed the intermediate iframe, instead of One Tap, into your AMP pages using
   the `<amp-onetap-google>` component.

> [!NOTE]
> **Note:** See the [Integrate One Tap using an Iframe](https://developers.google.com/identity/gsi/web/amp/intermediate-iframe) section for more.

Place the following code snippet into any AMP pages that you want Google One
Tap to display:

    <script custom-element="amp-onetap-google" src="https://cdn.ampproject.org/v0/amp-onetap-google-0.1.js" async></script>
    <amp-onetap-google
      layout="nodisplay"
      data-src="https://example.com/onetap_iframe.html">
    </amp-onetap-google>

Set the `data-src` attribute to the URI of your intermediate iframe.