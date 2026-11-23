---
title: "types/utils.d.ts"
source_url: https://github.com/stripe/stripe-js/blob/v10.2.1/types/utils.d.ts
---

# `types/utils.d.ts` (stripe/stripe-js v10.2.1)

Verbatim source file, wrapped in Markdown so it can be searched. Source: https://github.com/stripe/stripe-js/blob/v10.2.1/types/utils.d.ts

```ts
// Polyfill for TypeScript < 3.5 compatibility
export type Omit<T, K extends keyof any> = Pick<T, Exclude<keyof T, K>>;

```
