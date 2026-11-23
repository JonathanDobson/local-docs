---
title: Type declarations: build/src/gtoken/revokeToken.d.ts
source: https://registry.npmjs.org/google-auth-library/-/google-auth-library-10.9.1.tgz (package/build/src/gtoken/revokeToken.d.ts)
---

# Type declarations: build/src/gtoken/revokeToken.d.ts

Verbatim file from the official source, wrapped in a code block for search.

```ts
import { Transporter } from './tokenOptions';
/**
 * Revokes a given access token.
 * @param accessToken The access token to revoke.
 * @param transporter The transporter to make the request with.
 * @returns A promise that resolves with the revocation response.
 */
declare function revokeToken(accessToken: string, transporter: Transporter): Promise<import("gaxios").GaxiosResponse<unknown>>;
export { revokeToken };
```
