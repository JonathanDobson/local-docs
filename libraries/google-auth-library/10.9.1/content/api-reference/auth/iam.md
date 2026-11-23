---
title: Type declarations: build/src/auth/iam.d.ts
source: https://registry.npmjs.org/google-auth-library/-/google-auth-library-10.9.1.tgz (package/build/src/auth/iam.d.ts)
---

# Type declarations: build/src/auth/iam.d.ts

Verbatim file from the official source, wrapped in a code block for search.

```ts
export interface RequestMetadata {
    'x-goog-iam-authority-selector': string;
    'x-goog-iam-authorization-token': string;
}
export declare class IAMAuth {
    selector: string;
    token: string;
    /**
     * IAM credentials.
     *
     * @param selector the iam authority selector
     * @param token the token
     * @constructor
     */
    constructor(selector: string, token: string);
    /**
     * Acquire the HTTP headers required to make an authenticated request.
     */
    getRequestHeaders(): {
        'x-goog-iam-authority-selector': string;
        'x-goog-iam-authorization-token': string;
    };
}
```
