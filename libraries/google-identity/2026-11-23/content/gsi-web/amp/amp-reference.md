---
source: https://developers.google.com/identity/gsi/web/amp/amp-reference
markdown_source: https://developers.google.com/identity/gsi/web/amp/amp-reference.md.txt
title: "AMP Component API reference  |  Web guides  |  Google for Developers"
fetched: 2026-11-23
---

# AMP Component API reference

This reference page describes the API of the `<amp-onetap-google>` AMP
component.

See the [Integrate One Tap using an Iframe](https://developers.google.com/identity/gsi/web/amp/intermediate-iframe) guide to learn how to use
intermediate iframes.

## Load the `<amp-onetap-google>` AMP Component

Place the following code snippet into any AMP pages where you want to use the
`<amp-onetap-google>` AMP Component:

    <script custom-element="amp-onetap-google" src="https://cdn.ampproject.org/v0/amp-onetap-google-0.1.js" async></script>

## The `<amp-onetap-google>` AMP Component

The following table lists the data attributes with their descriptions:

| Attribute ||
|---|---|
| `https://developers.google.com/identity/gsi/web/amp/amp-reference#data-src` | The URI of your One Tap intermediate iframe |
| `https://developers.google.com/identity/gsi/web/amp/amp-reference#layout` | The layout of the AMP component. Only "nodisplay" is allowed. |

### data-src

This attribute is the URI of your One Tap intermediate iframe. See the following
table for further information:

| Type | Required | Example |
|---|---|---|
| string | Yes | `data-src="https://example.com/onetap_iframe.html"` |

### layout

This attribute is the layout of the AMP component, which is a required attribute
of AMP components. For the `<amp-onetap-google>` component, only
"nodisplay" is allowed. See the following table for further information:

| Type | Required | Example |
|---|---|---|
| string | Yes | `layout="nondisplay"` |