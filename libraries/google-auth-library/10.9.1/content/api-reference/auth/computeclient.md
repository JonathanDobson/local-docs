---
title: Type declarations: build/src/auth/computeclient.d.ts
source: https://registry.npmjs.org/google-auth-library/-/google-auth-library-10.9.1.tgz (package/build/src/auth/computeclient.d.ts)
---

# Type declarations: build/src/auth/computeclient.d.ts

Verbatim file from the official source, wrapped in a code block for search.

```ts
import { GaxiosError } from 'gaxios';
import { GetTokenResponse, OAuth2Client, OAuth2ClientOptions } from './oauth2client';
export interface ComputeOptions extends OAuth2ClientOptions {
    /**
     * The service account email to use, or 'default'. A Compute Engine instance
     * may have multiple service accounts.
     */
    serviceAccountEmail?: string;
    /**
     * The scopes that will be requested when acquiring service account
     * credentials. Only applicable to modern App Engine and Cloud Function
     * runtimes as of March 2019.
     */
    scopes?: string | string[];
}
export declare class Compute extends OAuth2Client {
    readonly serviceAccountEmail: string;
    scopes: string[];
    /**
     * Google Compute Engine service account credentials.
     *
     * Retrieve access token from the metadata server.
     * See: https://cloud.google.com/compute/docs/access/authenticate-workloads#applications
     */
    constructor(options?: ComputeOptions);
    /**
     * Refreshes the access token.
     * @param refreshToken Unused parameter
     */
    protected refreshTokenNoCache(): Promise<GetTokenResponse>;
    /**
     * Fetches an ID token.
     * @param targetAudience the audience for the fetched ID token.
     */
    fetchIdToken(targetAudience: string): Promise<string>;
    protected wrapError(e: GaxiosError): void;
}
```
