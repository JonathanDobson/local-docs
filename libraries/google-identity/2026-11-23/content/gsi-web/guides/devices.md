---
source: https://developers.google.com/identity/gsi/web/guides/devices
markdown_source: https://developers.google.com/identity/gsi/web/guides/devices.md.txt
title: "Sign-In on TVs and Limited Input Devices  |  Web guides  |  Google for Developers"
fetched: 2026-11-23
---

# Sign-In on TVs and Limited Input Devices

You can let users sign in to your app with their Google Accounts on devices with
limited input capabilities, such as Internet-connected TVs.

The app displays a short code and sign-in URL to the user. Then, the user opens
the sign-in URL in a web browser, enters the code, and grants the app permission
to access the user's sign-in information. Finally, the app receives confirmation
and the user is signed in.

To use this sign-in flow, the app must run on a device that meets the following
criteria:

- The device must be capable of displaying a 40-character URL and a 15-character user code, along with instructions to the user.
- The device must be connected to the Internet.

## Get a client ID and client secret

Your app needs an OAuth 2.0 client ID and client secret to make requests to
Google's sign-in endpoints.

To find your project's client ID and client secret, do the following:

1. Select an existing OAuth 2.0 credential or open the [Credentials page](https://console.cloud.google.com/apis/credentials).
2. If you haven't done so already, create your project's OAuth 2.0 credentials by clicking **Create credentials \> OAuth client ID**, and providing the information needed to create the credentials.
3. Look for the **Client ID** in the **OAuth 2.0 client IDs** section. For details, click the client ID.

If you are creating a new client ID, select the
**TVs and Limited Input devices** application type.

## Obtain a user code and verification URL

Once a user requests to sign in using a Google Account, you obtain a user code
and verification URL by sending an HTTP POST request to the OAuth 2.0 device
endpoint, `https://oauth2.googleapis.com/device/code`. Include your client ID
and a list of the scopes you need with the request. If you only want to sign in
users with their Google Accounts, request only the `profile` and `email` scopes;
or, if you want to request permission to call a [supported API](https://developers.google.com/identity/protocols/oauth2/limited-input-device#allowedscopes) on behalf of
users, request the required scopes in addition to the `profile` and `email`
scopes.

The following is an example request for a user code:

    POST /device/code HTTP/1.1
    Host: oauth2.googleapis.com
    Content-Type: application/x-www-form-urlencoded

    client_id=YOUR_GOOGLE_CLIENT_ID&scope=email%20profile

Using `curl`:

    curl -d "client_id=YOUR_GOOGLE_CLIENT_ID&scope=email profile" https://oauth2.googleapis.com/device/code

The response is returned as a JSON object:

     {
      "device_code" : "4/4-GMMhmHCXhWEzkobqIHGG_EnNYYsAkukHspeYUk9E8",
      "user_code" : "GQVQ-JKEC",
      "verification_url" : "https://www.google.com/device",
      "expires_in" : 1800,
      "interval" : 5
    }

Your app displays the `user_code` and `verification_url` values to the user,
and, at the same time, polls the sign-in endpoint at the specified `interval`
until either the user signs in or the time specified by `expires_in` has passed.

## Display the user code and verification URL

After you receive a user code and verification URL from the device endpoint,
display them and instruct the user to open the URL and enter the user code.

The values of `verification_url` and `user_code` are subject to change. Design
your UI in a way that can handle the following limits:

- `user_code` must be displayed in a field wide enough to handle 15 `W`-sized characters.
- `verification_url` must be displayed in a field wide enough to handle a URL string that is 40 characters long.

Both strings can contain any printable character from the US-ASCII character
set.

When you display the `user_code` string, don't modify the string in any way
(such as changing the case or inserting other formatting characters), because
your app might break if the format of the code changes in the future.

You can modify the `verification_url` string by stripping off the scheme from
the URL for display purposes if you choose. If you do, be sure your app can
handle both "http" and "https" variants. Don't otherwise modify the
`verification_url` string.

When the user navigates to the verification URL, they see a page similar to the
following:

![Connect a device by entering a code](https://developers.google.com/static/identity/protocols/images/oauth2/device/user-code.png)

After the user enters the user code, the Google sign-in site presents a consent
screen similar to the following:

![Example consent screen for a device client](https://developers.google.com/static/identity/protocols/images/oauth2/device/approval.png)

If the user clicks **Allow**, then your app can obtain an ID token to identify
the user, an access token to call Google APIs, and a refresh token to acquire
new tokens.

## Obtain an ID token and refresh token

After your app displays the user code and verification URL, begin polling the
token endpoint (`https://oauth2.googleapis.com/token`) with the device code that
you received from the device endpoint. Poll the token endpoint at the interval,
in seconds, specified by the `interval` value.

The following is an example request:

    POST /token HTTP/1.1
    Host: oauth2.googleapis.com
    Content-Type: application/x-www-form-urlencoded

    client_id=YOUR_GOOGLE_CLIENT_ID&client_secret=YOUR_CLIENT_SECRET&code=DEVICE_CODE&grant_type=http://oauth.net/grant_type/device/1.0

Using `curl`:

    curl -d "client_id=YOUR_CLIENT_ID&client_secret=YOUR_CLIENT_SECRET&code=YOUR_DEVICE_CODE&grant_type=http://oauth.net/grant_type/device/1.0" https://oauth2.googleapis.com/token

If the user has not yet approved the request, the response is as follows:

    {
      "error" : "authorization_pending"
    }

Your app should repeat these requests at a rate that does not exceed the value
of `interval`. If your app polls too quickly, the response is as follows:

    {
      "error" : "slow_down"
    }

Once the user signs in and grants your app access to the scopes you requested,
the response to your app's next request includes an ID token, an access token,
and a refresh token:

    {
      "access_token": "ya29.AHES6ZSuY8f6WFLswSv0HZLP2J4cCvFSj-8GiZM0Pr6cgXU",
      "token_type": "Bearer",
      "expires_in": 3600,
      "refresh_token": "1/551G1yXUqgkDGnkfFk6ZbjMMMDIMxo3JFc8lY8CAR-Q",
      "id_token": "eyJhbGciOiJSUzI..."
    }

Upon receipt of this response, your app can decode the ID token to get basic
profile information about the signed-in user, or [send the ID token to your
app's backend server](https://developers.google.com/identity/sign-in/web/backend-auth) to securely authenticate with the server. Also, your
app can use the access token to [call the Google APIs](https://developers.google.com/identity/protocols/oauth2/limited-input-device#callinganapi) that the user
authorized.

ID and access tokens have limited lifetimes. To keep the user signed in beyond
the tokens' lifetimes, store the refresh token and use it to [request new
tokens](https://developers.google.com/identity/protocols/oauth2/limited-input-device#offline).

## Get user profile information from the ID token

You can get profile information about the signed-in user by decoding the ID
token with any [JWT-decoding library](https://jwt.io/#libraries-io). For example, using the Auth0
[jwt-decode](https://github.com/auth0/jwt-decode) JavaScript library:

    var user_profile = jwt_decode(<var>id_token</var>);

    // The "sub" field is available on all ID tokens. This value is unique for each
    // Google account and can be used to identify the user. (But do not send this
    // value to your server; instead, send the whole ID token so its authenticity
    // can be verified.)
    var user_id = user_profile["sub"];

    // These values are available when you request the "profile" and "email" scopes.
    var user_email = user_profile["email"];
    var email_verified = user_profile["email_verified"];
    var user_name = user_profile["name"];
    var user_photo_url = user_profile["picture"];
    var user_given_name = user_profile["given_name"];
    var user_family_name = user_profile["family_name"];
    var user_locale = user_profile["locale"];

> [!NOTE]
> **Note:** Because you received the ID token directly from Google, you can decode the token without validating it. Whenever you receive an ID token from a source other than Google, such as from a client app to your backend server, you must validate the token to ensure its authenticity. See [Authenticate with a backend
> server](https://developers.google.com/identity/sign-in/web/backend-auth#using-a-google-api-client-library).

> [!IMPORTANT]
> **Key Point:** Only use **`sub`** field as identifier for the user as it is unique among all Google Accounts and never reused. **Don't** use email address as an identifier because a Google Account can have multiple email addresses at different points in time.

## More information

- To keep users signed-in beyond the lifetime of an ID token, see [Refreshing
  an access token](https://developers.google.com/identity/protocols/oauth2/limited-input-device#offline).
- If you need to authenticate with a backend server, see [Authenticate with a
  backend server](https://developers.google.com/identity/sign-in/web/backend-auth#using-a-google-api-client-library) for information on doing so securely.