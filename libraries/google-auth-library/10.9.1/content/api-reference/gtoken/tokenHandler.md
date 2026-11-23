---
title: Type declarations: build/src/gtoken/tokenHandler.d.ts
source: https://registry.npmjs.org/google-auth-library/-/google-auth-library-10.9.1.tgz (package/build/src/gtoken/tokenHandler.d.ts)
---

# Type declarations: build/src/gtoken/tokenHandler.d.ts

Verbatim file from the official source, wrapped in a code block for search.

```ts
import { TokenData } from './getToken';
import { TokenOptions } from './tokenOptions';
/**
 * Manages the fetching and caching of access tokens.
 */
declare class TokenHandler {
    /** The cached access token. */
    token: TokenData | undefined;
    /** The expiration time of the cached access token. */
    tokenExpiresAt: number | undefined;
    /** A promise for an in-flight token request. */
    private inFlightRequest;
    private tokenOptions;
    /**
     * Creates an instance of TokenHandler.
     * @param tokenOptions The options for fetching tokens.
     * @param transporter The transporter to use for making requests.
     */
    constructor(tokenOptions: TokenOptions);
    /**
     * Processes the credentials, loading them from a key file if necessary.
     * This method is called before any token request.
     */
    private processCredentials;
    /**
     * Checks if the cached token is expired or close to expiring.
     * @returns True if the token is expiring, false otherwise.
     */
    isTokenExpiring(): boolean;
    /**
     * Returns whether the token has completely expired.
     *
     * @returns true if the token has expired, false otherwise.
     */
    hasExpired(): boolean;
    /**
     * Fetches an access token, using a cached one if available and not expired.
     * @param forceRefresh If true, forces a new token to be fetched.
     * @returns A promise that resolves with the token data.
     */
    getToken(forceRefresh: boolean): Promise<TokenData>;
}
export { TokenHandler };
```
