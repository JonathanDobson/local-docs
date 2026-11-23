---
source: https://developers.google.com/identity/gsi/web/amp/intermediate-support-reference
markdown_source: https://developers.google.com/identity/gsi/web/amp/intermediate-support-reference.md.txt
title: "Intermediate iframe Support JavaScript API reference  |  Web guides  |  Google for Developers"
fetched: 2026-11-23
---

This reference page describes the Intermediate iframe Support JavaScript API,
used by One Tap to manipulate the intermediate iframe in subsequent UX.

See the [Integrate One Tap using an Iframe](https://developers.google.com/identity/gsi/web/amp/intermediate-iframe) guide to learn how to use
intermediate iframes.

The following table lists all available methods and their behaviors.

| Methods ||
|---|---|
| `https://developers.google.com/identity/gsi/web/amp/intermediate-support-reference#verifyParentOrigin` | performs the parent origin verification |
| `https://developers.google.com/identity/gsi/web/amp/intermediate-support-reference#notifyParentClose` | notifies the parent frame the One Tap UX flow is skipped |
| `https://developers.google.com/identity/gsi/web/amp/intermediate-support-reference#notifyParentDone` | notifies the parent frame the One Tap UX flow is done |
| `https://developers.google.com/identity/gsi/web/amp/intermediate-support-reference#notifyParentResize` | notifies the parent frame to resize the intermediate iframe |
| `https://developers.google.com/identity/gsi/web/amp/intermediate-support-reference#notifyParentTapOutsideMode` | notifies the parent frame whether to cancel the intermediate iframe when the user clicks outside the intermediate iframe |

<br />

## Load the Intermediate Iframe Support JavaScript Library

Place the following code snippet into any HTML pages where you want to load the
intermediate iframe:

```
<script src="https://accounts.google.com/gsi/intermediatesupport"></script>
```

## Method: google.accounts.id.intermediate.verifyParentOrigin

The `google.accounts.id.intermediate.verifyParentOrigin` method performs the
parent origin verification. See the following code example of the method:

    google.accounts.id.intermediate.verifyParentOrigin(
        origins, verifiedCallback, verificationFailedCallback)

The following code example shows how to show UI only after the parent origin is
verified:

    <script>
      window.onload = () => {
        google.accounts.id.intermediate.verifyParentOrigin(
            "https://example.com", showUI, showError);
      };
    </script>

The following table lists the parameters:

| Parameter ||
|---|---|
| `https://developers.google.com/identity/gsi/web/amp/intermediate-support-reference#origins` | The origins that are allowed to embed the intermediate iframe. |
| `https://developers.google.com/identity/gsi/web/amp/intermediate-support-reference#verifiedCallback` | The JavaScript callback method triggered when the current parent origin is allowed to embed the intermediate iframe. |
| `https://developers.google.com/identity/gsi/web/amp/intermediate-support-reference#verificationFailedCallback` | The JavaScript callback method triggered when the current parent origin is not allowed to embed the intermediate iframe. |

### origins

The origins that are allowed to embed the intermediate iframe. See the following
table for further information:

| Type | Required | Example |
|---|---|---|
| string, string array or function | Optional | `allowed_parent_origin: "https://example.com"` |

The following table lists the supported value types and their descriptions.

| Value Types |||
|---|---|---|
| `string` | A single domain URI. | "https://example.com" |
| `string array` | An array of domain URIs. | "https://news.example.com,https://local.example.com" |

> [!NOTE]
> **Note:** A string with comma-separated URIs is invalid. Use a JavaScript Array object instead.

### verifiedCallback

This field is a JavaScript callback method triggered when the current parent
origin is allowed to embed the intermediate iframe.

### verificationFailedCallback

This field is a JavaScript callback method triggered when the current parent
origin is not allowed to embed the intermediate iframe.

> [!WARNING]
> **Warning:** if the content page doesn't respond to the domain verification request, the verification process waits forever. In this case, neither `verifiedCallback` nor `verificationFailedCallback` is invoked.

## Method: google.accounts.id.intermediate.notifyParentClose

The `google.accounts.id.intermediate.notifyParentClose` method notifies the
parent frame to close the intermediate iframe when the One Tap UX flow is
skipped. See the following code example of the method:

    google.accounts.id.intermediate.notifyParentClose()

## Method: google.accounts.id.intermediate.notifyParentDone

The `google.accounts.id.intermediate.notifyParentDone` method notifies the
parent frame to close the intermediate iframe and refresh the login status. See
the following code example of the method:

    google.accounts.id.intermediate.notifyParentDone()

## Method: google.accounts.id.intermediate.notifyParentResize

The `google.accounts.id.intermediate.notifyParentResize` method notifies the
parent frame to resize the intermediate iframe. See the following code example
of the method:

    google.accounts.id.intermediate.notifyParentResize(height)

> [!NOTE]
> **Note:** You cannot change the width of the intermediate iframe.

### height

The new height in pixel. This is a required field. The value must be a
non-negative number.

If the height parameter is greater than 0, the intermediate iframe is set to
the new height. If the height parameter is 0, the intermediate iframe becomes
invisible. A hidden iframe is not closed. It can be shown later by another
resize method call.

## Method: google.accounts.id.intermediate.notifyParentTapOutsideMode

The `google.accounts.id.intermediate.notifyParentTapOutsideMode` method notifies
the parent frame whether to cancel the intermediate iframe when the user clicks
outside the intermediate iframe. See the following code example of the method:

    google.accounts.id.intermediate.notifyParentTapOutsideMode(cancel)

### cancel

This required boolean value indicates whether to cancel the intermediate iframe
when the user clicks outside the intermediate iframe.