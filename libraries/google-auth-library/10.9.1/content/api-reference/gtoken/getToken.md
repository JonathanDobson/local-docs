---
title: Type declarations: build/src/gtoken/getToken.d.ts
source: https://registry.npmjs.org/google-auth-library/-/google-auth-library-10.9.1.tgz (package/build/src/gtoken/getToken.d.ts)
---

# Type declarations: build/src/gtoken/getToken.d.ts

Verbatim file from the official source, wrapped in a code block for search.

```ts
import { TokenOptions } from './tokenOptions';
/**
 * Interface for the data returned from the token endpoint.
 */
interface TokenData {
    /** An optional refresh token. */
    refresh_token?: string;
    /** The duration of the token in seconds. */
    expires_in?: number;
    /** The access token. */
    access_token?: string;
    /** The type of token, e.g., "Bearer". */
    token_type?: string;
    /** An optional ID token. */
    id_token?: string;
}
/**
 * Fetches an access token.
 * @param tokenOptions The options for the token.
 * @returns A promise that resolves with the token data.
 */
declare function getToken(tokenOptions: TokenOptions): Promise<TokenData>;
export { getToken, TokenData };
```
