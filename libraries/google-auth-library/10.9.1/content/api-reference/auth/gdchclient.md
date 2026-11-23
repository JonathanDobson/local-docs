---
title: Type declarations: build/src/auth/gdchclient.d.ts
source: https://registry.npmjs.org/google-auth-library/-/google-auth-library-10.9.1.tgz (package/build/src/auth/gdchclient.d.ts)
---

# Type declarations: build/src/auth/gdchclient.d.ts

Verbatim file from the official source, wrapped in a code block for search.

```ts
import { GaxiosOptions, GaxiosResponse } from 'gaxios';
import { GetTokenResponse, OAuth2Client, OAuth2ClientOptions } from './oauth2client';
export declare const GDCH_SERVICE_ACCOUNT_TYPE = "gdch_service_account";
export interface GdchClientOptions extends OAuth2ClientOptions {
    projectId?: string | null;
    privateKeyId?: string;
    privateKey?: string;
    serviceIdentityName?: string;
    tokenServerUri?: string;
    caCertPath?: string;
    apiAudience?: string;
    lifetime?: number;
}
export interface GdchCredentialsInput {
    type: 'gdch_service_account';
    format_version: string;
    project: string;
    private_key_id: string;
    private_key: string;
    name: string;
    token_uri: string;
    ca_cert_path?: string;
}
export declare class GdchClient extends OAuth2Client {
    projectId?: string;
    privateKeyId?: string;
    privateKey?: string;
    serviceIdentityName?: string;
    tokenServerUri?: string;
    caCertPath?: string;
    apiAudience?: string;
    lifetime: number;
    private gdchOptions;
    private caAgentPromise?;
    private cachedCaCertPath?;
    private lastCaCertReadTime;
    private readonly CA_CERT_TTL_MS;
    constructor(options?: GdchClientOptions);
    createWithGdchAudience(apiAudience: string): GdchClient;
    fromJSON(json: GdchCredentialsInput): void;
    protected refreshTokenNoCache(): Promise<GetTokenResponse>;
    private createAssertion;
    requestAsync<T>(opts: GaxiosOptions, retry?: boolean): Promise<GaxiosResponse<T>>;
    private getCaAgent;
    toJSON(): Record<string, any>;
    private base64UrlEncode;
}
```
