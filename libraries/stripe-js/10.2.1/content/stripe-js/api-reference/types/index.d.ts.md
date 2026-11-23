---
title: "types/index.d.ts"
source_url: https://github.com/stripe/stripe-js/blob/v10.2.1/types/index.d.ts
---

# `types/index.d.ts` (stripe/stripe-js v10.2.1)

Verbatim source file, wrapped in Markdown so it can be searched. Source: https://github.com/stripe/stripe-js/blob/v10.2.1/types/index.d.ts

```ts
export * from './api';
export * from './stripe-js';

import {StripeConstructor} from './stripe-js';

export {loadStripe, ReleaseTrain} from './shared';

declare global {
  interface Window {
    // Stripe.js must be loaded directly from https://js.stripe.com/v3, which
    // places a `Stripe` object on the window
    Stripe?: StripeConstructor;
  }
}

```
