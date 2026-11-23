---
title: Type declarations: build/src/gtoken/getCredentials.d.ts
source: https://registry.npmjs.org/google-auth-library/-/google-auth-library-10.9.1.tgz (package/build/src/gtoken/getCredentials.d.ts)
---

# Type declarations: build/src/gtoken/getCredentials.d.ts

Verbatim file from the official source, wrapped in a code block for search.

```ts
/**
 * Credentials object.
 */
interface Credentials {
    privateKey: string;
    clientEmail?: string;
}
/**
 * Given a keyFile, extract the key and client email if available
 * @param keyFile Path to a json, pem, or p12 file that contains the key.
 * @returns an object with privateKey and clientEmail properties
 */
declare function getCredentials(keyFilePath: string): Promise<Credentials>;
export { getCredentials, Credentials };
```
