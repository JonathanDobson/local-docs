---
title: Type declarations: build/src/auth/idtokenclient.d.ts
source: https://registry.npmjs.org/google-auth-library/-/google-auth-library-10.9.1.tgz (package/build/src/auth/idtokenclient.d.ts)
---

# Type declarations: build/src/auth/idtokenclient.d.ts

Verbatim file from the official source, wrapped in a code block for search.

```ts
import { OAuth2Client, OAuth2ClientOptions, RequestMetadataResponse } from './oauth2client';
export interface IdTokenOptions extends OAuth2ClientOptions {
    /**
     * The client to make the request to fetch an ID token.
     */
    idTokenProvider: IdTokenProvider;
    /**
     * The audience to use when requesting an ID token.
     */
    targetAudience: string;
}
export interface IdTokenProvider {
    fetchIdToken: (targetAudience: string) => Promise<string>;
}
export declare class IdTokenClient extends OAuth2Client {
    targetAudience: string;
    idTokenProvider: IdTokenProvider;
    /**
     * Google ID Token client
     *
     * Retrieve ID token from the metadata server.
     * See: https://cloud.google.com/docs/authentication/get-id-token#metadata-server
     */
    constructor(options: IdTokenOptions);
    protected getRequestMetadataAsync(): Promise<RequestMetadataResponse>;
    private getIdTokenExpiryDate;
}
```
