---
title: Type declarations: build/src/gtoken/errorWithCode.d.ts
source: https://registry.npmjs.org/google-auth-library/-/google-auth-library-10.9.1.tgz (package/build/src/gtoken/errorWithCode.d.ts)
---

# Type declarations: build/src/gtoken/errorWithCode.d.ts

Verbatim file from the official source, wrapped in a code block for search.

```ts
declare class ErrorWithCode extends Error {
    code: string;
    constructor(message: string, code: string);
}
export { ErrorWithCode };
```
