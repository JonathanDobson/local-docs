---
title: Type declarations: build/src/auth/passthrough.d.ts
source: https://registry.npmjs.org/google-auth-library/-/google-auth-library-10.9.1.tgz (package/build/src/auth/passthrough.d.ts)
---

# Type declarations: build/src/auth/passthrough.d.ts

Verbatim file from the official source, wrapped in a code block for search.

```ts
import { GaxiosOptions } from 'gaxios';
import { AuthClient, GetAccessTokenResponse } from './authclient';
/**
 * An AuthClient without any Authentication information. Useful for:
 * - Anonymous access
 * - Local Emulators
 * - Testing Environments
 *
 */
export declare class PassThroughClient extends AuthClient {
    /**
     * Creates a request without any authentication headers or checks.
     *
     * @remarks
     *
     * In testing environments it may be useful to change the provided
     * {@link AuthClient.transporter} for any desired request overrides/handling.
     *
     * @param opts
     * @returns The response of the request.
     */
    request<T>(opts: GaxiosOptions): Promise<import("gaxios").GaxiosResponse<T>>;
    /**
     * A required method of the base class.
     * Always will return an empty object.
     *
     * @returns {}
     */
    getAccessToken(): Promise<GetAccessTokenResponse>;
    /**
     * A required method of the base class.
     * Always will return an empty object.
     *
     * @returns {}
     */
    getRequestHeaders(): Promise<Headers>;
}
```
