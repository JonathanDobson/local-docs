---
source: https://developers.google.com/identity/gsi/web/amp/nonamp-reference
markdown_source: https://developers.google.com/identity/gsi/web/amp/nonamp-reference.md.txt
title: "Intermediate iframe API reference  |  Web guides  |  Google for Developers"
fetched: 2026-11-23
---

This reference page describes the Intermediate iframe API, used to embed the
One Tap prompt into web pages using an iframe.

See [Integrate One Tap using an iframe](https://developers.google.com/identity/gsi/web/amp/intermediate-iframe) for more information on working
with intermediate iframes.

## Load the Intermediate Iframe JavaScript Library

Place the following code snippet into any HTML pages that you want to Google One
Tap to display:

    <script src="https://accounts.google.com/gsi/intermediate"></script>

## HTML API

You can load the intermediate iframe by including an HTML element with the ID
attribute set to `g_id_intermediate_iframe`. See the following example code
snippet:

    <script src="https://accounts.google.com/gsi/intermediate"></script>
    <div id="g_id_intermediate_iframe"
         data-src="https://example.com/onetap_iframe.html">
    </div>

### Element with ID "g_id_intermediate_iframe"

You can put the intermediate iframe data attributes in any visible or invisible
elements, such as `<div>` and `<span>`. The only requirement is that the element
ID is set to `g_id_intermediate_iframe`. Don't put this ID on multiple
elements.

The following table lists the data attributes with their descriptions:

| Attribute ||
|---|---|
| `https://developers.google.com/identity/gsi/web/amp/nonamp-reference#data-src` | The URI of your One Tap intermediate iframe |
| `https://developers.google.com/identity/gsi/web/amp/nonamp-reference#data-done` | A JavaScript callback method to be triggered when the One Tap UX is done. |

#### data-src

This attribute is the URI of your One Tap intermediate iframe. See the following
table for further information:

| Type | Required | Example |
|---|---|---|
| string | Yes | `data-src="https://example.com/onetap_iframe.html"` |

#### data-done

This attribute is a JavaScript callback method triggered when the One Tap UX
is done.

By default, the content page is reloaded when the One Tap UX is done. You
can override the default behavior by providing your own done callback. See the
following table for further information:

| Type | Required | Example |
|---|---|---|
| Function | Optional | `data-done="onOneTapSuccess"` |

## JavaScript API

You can load the intermediate iframe by calling a JavaScript method.

### Method: google.accounts.id.initializeIntermediate

The `google.accounts.id.initializeIntermediate` method load the intermediate
iframe based on the configuration object. See the following code example of the
method:

    google.accounts.id.initializeIntermediate(IntermediateConfig)

The following code example implements the
`google.accounts.id.initializeIntermediate` method with an `onload` function:

    <script>
      window.onload = function () {
        google.accounts.id.initializeIntermediate({
          src: 'https://example.com/intermediate'
        });
      };
    </script>

### Data type: IntermediateConfig

The following table lists the fields with their descriptions:

| Field ||
|---|---|
| `https://developers.google.com/identity/gsi/web/amp/nonamp-reference#src` | The URI of your One Tap intermediate iframe |
| `https://developers.google.com/identity/gsi/web/amp/nonamp-reference#done` | A JavaScript callback method to be triggered when the One Tap UX is one. |

#### src

This field is the URI of your One Tap intermediate iframe. See the following
table for further information:

| Type | Required | Example |
|---|---|---|
| string | Yes | `src: "https://example.com/onetap_iframe.html"` |

#### done

This field is the JavaScript callback method to be triggered when the One Tap UX
is done.

By default, the content page is reloaded when the One Tap UX is done. You
can override the default behavior by providing your own done callback. See the
following table for further information:

| Type | Required | Example |
|---|---|---|
| Function | Optional | `done: onOneTapSuccess` |