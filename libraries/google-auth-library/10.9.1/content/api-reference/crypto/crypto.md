---
title: Type declarations: build/src/crypto/crypto.d.ts
source: https://registry.npmjs.org/google-auth-library/-/google-auth-library-10.9.1.tgz (package/build/src/crypto/crypto.d.ts)
---

# Type declarations: build/src/crypto/crypto.d.ts

Verbatim file from the official source, wrapped in a code block for search.

```ts
import { Crypto } from './shared';
export * from './shared';
export interface CryptoSigner {
    update(data: string): void;
    sign(key: string, outputFormat: string): string;
}
export declare function createCrypto(): Crypto;
export declare function hasBrowserCrypto(): boolean;
```
