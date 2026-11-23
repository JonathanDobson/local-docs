# google-auth-library 10.9.1 (Node.js)

Google's official Node.js authentication client, npm package `google-auth-library`,
**release 10.9.1**. It is the newest 10.x release (npm dist-tag `legacy-18`, released
2026-07-23, `engines.node >=18`). The latest release when this set was made was 11.3.4.
The README, samples and changelog come from the `google-auth-library-v10.9.1` tag of the
`googleapis/google-cloud-node` monorepo (`core/packages/google-auth-library-nodejs`,
commit `6b9fd1af`). The old standalone repo `googleapis/google-auth-library-nodejs` is
archived. Google's HTML API reference isn't hosted for 10.9.1, so the **API reference here
is the package's own TypeScript declaration files** (`build/src/**/*.d.ts` from the npm
tarball, with their doc comments), plus the source of `OAuth2Client` and `LoginTicket`.
Every page wraps the original file verbatim in a code block.

For Sign in with Google on the browser side, see the `google-identity` set.

## Layout

| Folder | What it holds |
|---|---|
| `content/README.md` | The full package README: ADC, OAuth2, JWT, Compute, workload/workforce identity federation, ID tokens, impersonation, downscoping, supported Node versions |
| `content/samples/` | Official samples: `verifyIdToken.js`, `verifyGoogleIdToken.js`, `verifyIdToken-iap.js`, `oauth2.js`, `oauth2-codeVerifier.js`, `adc.js`, `jwt.js`, `keyfile.js`, `headers.js`, `credentials.js`, `compute.js`, `idTokenFromServiceAccount.js`, `idtokens-serverless.js` |
| `content/release-notes/` | `CHANGELOG.md` (all history up to 10.9.1), `CHANGELOG-11.x.md` (entries 11.0.0–11.3.4 for comparison) |
| `content/api-reference/` | One page per `.d.ts`: `index.md` (exports), `auth/oauth2client.md`, `auth/loginticket.md`, `auth/googleauth.md`, `auth/jwtclient.md`, `auth/idtokenclient.md`, … |
| `content/api-reference/source/auth/` | `oauth2client.ts.md`, `loginticket.ts.md`: implementation, for exact verification behaviour |

## Where to look for…

| Task | File |
|---|---|
| **Verify a Google ID token** (`OAuth2Client.verifyIdToken({idToken, audience, maxExpiry})` → `LoginTicket`) | README "Verifying ID Tokens"; `samples/verifyGoogleIdToken.md`, `samples/verifyIdToken.md`; `content/api-reference/auth/oauth2client.md` (`VerifyIdTokenOptions`) |
| `LoginTicket.getPayload()` and the `TokenPayload` fields (`sub`, `email`, `email_verified`, `hd`, `nonce`, `aud`, `iss`, `exp`, `azp`, `name`, `picture`…) | `content/api-reference/auth/loginticket.md` |
| Exactly what `verifyIdToken` checks | `content/api-reference/source/auth/oauth2client.ts.md` (`verifySignedJwtWithCertsAsync`) |
| Constructing `OAuth2Client` (clientId, clientSecret, redirectUri, `issuers`, endpoints) | `content/api-reference/auth/oauth2client.md` (`OAuth2ClientOptions`) |
| OAuth2 authorization-code flow, refresh tokens, `tokens` event | README "OAuth2"; `samples/oauth2.md`; PKCE: `samples/oauth2-codeVerifier.md` |
| Application Default Credentials (ADC), `GoogleAuth` | README "Application Default Credentials"; `content/api-reference/auth/googleauth.md` |
| Service-account JWT auth | README "JSON Web Tokens"; `content/api-reference/auth/jwtclient.md` |
| Fetching ID tokens for calling Cloud Run / IAP | README "Fetching ID Tokens"; `samples/idtokens-serverless.md` |
| Supported Node.js versions, versioning policy | README "Supported Node.js Versions" |
| What changed in a release | `content/release-notes/CHANGELOG.md` |

## How `verifyIdToken` behaves in 10.9.1 (from the source)

- It fetches Google's signing certificates (`https://www.googleapis.com/oauth2/v1/certs`
  PEM, or `/oauth2/v3/certs` JWK), checks the signature, then the claims.
- **`audience` is optional, and if you omit it `aud` is not checked.** Always pass your web
  client ID (a string or an array of IDs). Mismatch throws
  `Wrong recipient, payload audience != requiredAudience`.
- Issuers accepted by default: `accounts.google.com`, `https://accounts.google.com`, and
  the universe domain (override with the `issuers` constructor option).
- `iat`/`exp` are checked with a 300-second clock skew (`CLOCK_SKEW_SECS_`). Errors read
  `Token used too early` / `Token used too late`. `maxExpiry` defaults to 86400 s
  (`DEFAULT_MAX_TOKEN_LIFETIME_SECS_`).
- It does **not** check `nonce`, `hd` or `email_verified`. Read them from
  `ticket.getPayload()` and check them yourself.

## Version notes: 10.9.1 vs 11.x

- **11.0.0's only breaking change is a minimum Node.js version of 22**
  (`CHANGELOG-11.x.md`). 10.9.1 needs Node >=18.
- A `diff -r` of every `.d.ts` under `build/src` in the 10.9.1 and 11.3.4 npm tarballs
  found **no differences**: `OAuth2Client`, `verifyIdToken`, `LoginTicket` and
  `TokenPayload` have the same types in 11.x.
- 11.x moves its dependencies up a major version (`gaxios` ^8, `gcp-metadata` ^9,
  `google-logging-utils` ^2; recorded in the manifest notes). Check
  `CHANGELOG-11.x.md` for fixes after 11.0.0.
- So code written against 10.9.1 for ID-token verification should run unchanged on
  11.x once the runtime is Node 22+.

## Search tips

- The class is `OAuth2Client` (capital O, "Client"); the result type is `LoginTicket`;
  the claims type is `TokenPayload`; options type is `VerifyIdTokenOptions`.
- "ADC" means Application Default Credentials. "Universe domain" refers to Google Cloud
  universes other than googleapis.com (default `googleapis.com`).
- README links still point at the archived `googleapis/google-auth-library-nodejs` repo.
  That is upstream text. The local copies of samples are under `content/samples/`.
