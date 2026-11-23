---
source: https://developers.google.com/identity/gsi/web/guides/display-google-one-tap
markdown_source: https://developers.google.com/identity/gsi/web/guides/display-google-one-tap.md.txt
title: "Display Google One Tap  |  Web guides  |  Google for Developers"
fetched: 2026-11-23
---

Add a One Tap prompt to your site to enable users to sign-up or sign-in to your
web app. Use HTML and JavaScript to render and customize the prompt.

## Prerequisites

Follow the steps described in [Setup](https://developers.google.com/identity/gsi/web/guides/get-google-api-clientid) to configure your OAuth Consent
Screen, obtain a client ID, and load the client library.

Add a Sign in with Google [button](https://developers.google.com/identity/gsi/web/guides/display-button) to your login page.

## Prompt rendering

Place a code snippet into any pages where you want One Tap displayed.

### HTML

Display the One Tap prompt, returning the JWT credential to a login endpoint.

    <div id="g_id_onload"
       data-client_id="YOUR_GOOGLE_CLIENT_ID"
       data-login_uri="https://your.domain/your_login_endpoint"
       data-your_own_param_1_to_login="any_value"
       data-your_own_param_2_to_login="any_value">
    </div>

The `data-login_uri` attribute is the URI of the login endpoint of your
web app. You can add custom data attributes, which are sent to your login
endpoint along with the ID token issued by Google.

Optionally, use the `data-skip_prompt_cookie` attribute and a cookie to
control whether or not the One Tap prompt is displayed in static HTML pages
where you cannot change the content. If the specified cookie is set the
prompt isn't displayed.

Use the optional `data-context` attribute to change the text used in the
prompt title. For example, `data-context: "signup"` changes "Sign in to" to
"Sign up to".

By default, the One Tap prompt closes automatically if the user clicks
outside of the prompt. You can disable this behavior if you set the
`data-cancel_on_tap_outside` attribute to false.

For a full list of supported attributes, see [`g_id_onload` reference](https://developers.google.com/identity/gsi/web/reference/html-reference#element_with_id_g_id_onload).

### JavaScript

Display the One Tap prompt, returning the JWT credential to the browser's
JavaScript callback handler.

    <script>
      window.onload = function () {
        google.accounts.id.initialize({
          client_id: 'YOUR_GOOGLE_CLIENT_ID',
          callback: 'YOUR_CALLBACK_HANDLER'
        });
        google.accounts.id.prompt();
      }
    </script>

To configure the One Tap prompt in JavaScript, you first need to call the
`initialize()` method. Then, call the `prompt()` method to display the prompt
UI.

Use the optional `context` field to change the text used in the prompt title.
For example, `context: 'signup'` changes "Sign in to" to "Sign up to".

By default, the One Tap prompt closes automatically if the user clicks
outside of the prompt. You can disable this behavior if you set the
`cancel_on_tap_outside` property to false.

For the full list of data options, see [`idConfiguration` reference](https://developers.google.com/identity/gsi/web/reference/js-reference).

> [!IMPORTANT]
> **Key Point:** Use the [code generator](https://developers.google.com/identity/gsi/web/tools/configurator) to interactively customize One Tap and to create code snippets for use in your website.

## Prompt status

Use a JavaScript callback function to listen for prompt UI status notifications.

Notifications are sent for the following moments:

- **Display moment:** This occurs after the `prompt()` method is called. The
  notification contains a boolean value to indicate whether the UI is
  displayed or not.

- **Skipped moment:** This occurs when the One Tap prompt is closed by an auto
  cancel, a manual cancel, or when Google fails to issue a credential, such as
  when the selected session is signed out of Google.

  In this case, we recommend that you continue on to the next identity
  providers, if there are any.
- **Dismissed moment:** This occurs when Google successfully retrieves a
  credential, or a user wants to stop the credential retrieval flow. For
  example, when the user begins to input their username and password into
  the login dialog, you can call the `google.accounts.id.cancel()` method to
  close the One Tap prompt and trigger a dismissed moment.

  > [!WARNING]
  > **Warning:** When a dismissed moment occurs, don't try any of the next identity providers.

### HTML

Use the `data-moment_callback` attribute to specify a JavaScript callback
function. A callback handler is required to receive notifications.

    <html>
      <head>
        <script>
          function continueWithNextIdp(notification) {
            if (notification.isNotDisplayed() || notification.isSkippedMoment()) {
              // try Next provider if One Tap is not displayed or skipped
            }
          }
        </script>
      </head>
      <body>
        ...
        <div id="g_id_onload"
          data-client_id="YOUR_GOOGLE_CLIENT_ID"
          data-login_uri="https://your.domain/your_login_endpoint"
          data-moment_callback="continueWithNextIdp"
        </div>
        ...
      </body>
    </html>

To facilitate your users to sign in or sign up, you can communicate with
multiple identity providers to find available credentials. You might want to
know our prompt UI status so that you can call the next identity provider.

### JavaScript

Pass your callback handler as a parameter to `google.accounts.id.prompt`,
here an arrow function is used to handle notification updates.

    <script>
    window.onload = function () {
      google.accounts.id.initialize({
        client_id: 'YOUR_GOOGLE_CLIENT_ID',
        callback: 'YOUR_CALLBACK_HANDLER'
      });
      google.accounts.id.prompt((notification) =\> {
    if (notification.isNotDisplayed() \|\| notification.isSkippedMoment()) {
    // try next provider if OneTap is not displayed or skipped
    }
    });
    }
    </script>

## Button and prompt

The Sign in with Google button and One Tap prompt may be displayed together
on a single page.

### HTML

Display both the Sign in with Google button and One Tap prompt by including
both the `g_id_onload` and `g_id_signin` elements.

    <div id="g_id_onload"
       data-client_id="YOUR_GOOGLE_CLIENT_ID"
       data-context="signin"
       data-ux_mode="redirect"
       data-login_uri="https://your.domain/your_login_endpoint"
       data-itp_support="true">
    </div>

    <div class="g_id_signin"
       data-type="standard"
       data-shape="rectangular"
       data-theme="outline"
       data-text="signin_with"
       data-size="large"
       data-logo_alignment="left">
    </div>

### JavaScript

Display the Sign in with Google button and One Tap prompt by calling
both the `renderButton()` and `prompt()` functions at the same time.

    <script>
    window.onload = function () {
      google.accounts.id.initialize({
        client_id: 'YOUR_GOOGLE_CLIENT_ID',
        callback: 'YOUR_CALLBACK_HANDLER'
      });
      const parent = document.getElementById('google_btn');
      google.accounts.id.renderButton(parent, {theme: "filled_blue"});
      google.accounts.id.prompt();
    }
    </script>

## Don't cover One Tap

This section only applies when FedCM is disabled, when FedCM is enabled the
browser displays user prompts on top of page content.

To make sure end users see all the information displayed, Google One Tap must
not be covered by any other content. Otherwise, pop-up windows may be triggered
in some cases.

Double check your page layout and elements' z-index properties, to make sure
Google One Tap is not covered by any other content at any time. The UX flow
change may be triggered even when only a single pixel in the borders is covered.

> [!IMPORTANT]
> **Key Point:** Don't cover Google One Tap by any other content.

> [!WARNING]
> **Warning:** Don't hide any content of One Tap prompt. Don't obscure the perception that the content of the One Tap prompt is from a Google iframe. Failure to do so may result in project suspension or account suspension.

## Credential response

Included in the [credential response](https://developers.google.com/identity/gsi/web/reference/js-reference#CredentialResponse) is a Google signed JWT. The response
is returned either to the browser using a JavaScript callback function or to
your platform through a redirect to a login endpoint.

> [!IMPORTANT]
> **Important:** After receiving the JWT, it is strongly recommended that you [Verify the Google ID token on your server](https://developers.google.com/identity/sign-in/web/backend-auth).

### JS callback

Use either HTML or JavaScript to configure a callback.

### HTML

    <div id="g_id_onload"
      data-client_id="YOUR_GOOGLE_CLIENT_ID"
      data-callback="YOUR_CALLBACK_HANDLER"
    </div>

> [!NOTE]
> **Note:** You cannot set both the `data-login_uri` attribute and the `data-callback` attribute.

### JavaScript

    google.accounts.id.initialize({
      client_id: 'YOUR_GOOGLE_CLIENT_ID',
      callback: 'YOUR_CALLBACK_HANDLER'
    });

> [!NOTE]
> **Note:** You cannot set both the `login_uri` field and the `callback` field.

As an example, `handleCredentialResponse` decodes the JWT and prints some
of the ID token fields to the console.

    <script>
      google.accounts.id.initialize({
        client_id: 'YOUR_GOOGLE_CLIENT_ID',
        callback: handleCredentialResponse
      });

      function handleCredentialResponse(response) {
        const responsePayload = decodeJwtResponse(response.credential);

        console.log("ID: " + responsePayload.sub);
        console.log('Full Name: ' + responsePayload.name);
        console.log('Given Name: ' + responsePayload.given_name);
        console.log('Family Name: ' + responsePayload.family_name);
        console.log("Image URL: " + responsePayload.picture);
        console.log("Email: " + responsePayload.email);
      }

      function decodeJwtResponse(token) {
        let base64Url = token.split('.')[1];
        let base64 = base64Url.replace(/-/g, '+').replace(/_/g, '/');
        let jsonPayload = decodeURIComponent(atob(base64).split('').map(function(c) {
            return '%' + ('00' + c.charCodeAt(0).toString(16)).slice(-2);
        }).join(''));

        return JSON.parse(jsonPayload);
      }
    </script>

### Redirect

To return a credential to your platform's login endpoint add the URL to
the [Authorized redirect URI](https://developers.google.com/identity/gsi/web/guides/get-google-api-clientid#get_your_google_api_client_id) settings of your OAuth 2.0 web client.

Use either HTML or JavaScript to configure a redirect URI.

### HTML

    <div id="g_id_onload"
      data-client_id="YOUR_GOOGLE_CLIENT_ID"
      data-ux_mode="redirect"
    data-login-uri="YOUR_LOGIN_URI"
    </div>

> [!NOTE]
> **Note:** You cannot set both the `data-login_uri` attribute and the `data-callback` attribute.

### JavaScript

    google.accounts.id.initialize({
      client_id: 'YOUR_GOOGLE_CLIENT_ID',
      ux_mode: 'redirect',
      login_uri: 'YOUR_LOGIN_URI'
    });

> [!NOTE]
> **Note:** You cannot set both the `login_uri` field and the `callback` field.