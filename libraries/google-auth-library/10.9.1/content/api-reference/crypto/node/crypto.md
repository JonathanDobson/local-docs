---
title: Type declarations: build/src/crypto/node/crypto.d.ts
source: https://registry.npmjs.org/google-auth-library/-/google-auth-library-10.9.1.tgz (package/build/src/crypto/node/crypto.d.ts)
---

# Type declarations: build/src/crypto/node/crypto.d.ts

Verbatim file from the official source, wrapped in a code block for search.

```ts
import { Crypto } from '../shared';
export declare class NodeCrypto implements Crypto {
    sha256DigestBase64(str: string): Promise<string>;
    randomBytesBase64(count: number): string;
    verify(pubkey: string, data: string | Buffer, signature: string): Promise<boolean>;
    sign(privateKey: string, data: string | Buffer): Promise<string>;
    decodeBase64StringUtf8(base64: string): string;
    encodeBase64StringUtf8(text: string): string;
    /**
     * Computes the SHA-256 hash of the provided string.
     * @param str The plain text string to hash.
     * @return A promise that resolves with the SHA-256 hash of the provided
     *   string in hexadecimal encoding.
     */
    sha256DigestHex(str: string): Promise<string>;
    /**
     * Computes the HMAC hash of a message using the provided crypto key and the
     * SHA-256 algorithm.
     * @param key The secret crypto key in utf-8 or ArrayBuffer format.
     * @param msg The plain text message.
     * @return A promise that resolves with the HMAC-SHA256 hash in ArrayBuffer
     *   format.
     */
    signWithHmacSha256(key: string | ArrayBuffer, msg: string): Promise<ArrayBuffer>;
}
```
