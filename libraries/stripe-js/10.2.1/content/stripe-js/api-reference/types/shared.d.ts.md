---
title: "types/shared.d.ts"
source_url: https://github.com/stripe/stripe-js/blob/v10.2.1/types/shared.d.ts
---

# `types/shared.d.ts` (stripe/stripe-js v10.2.1)

Verbatim source file, wrapped in Markdown so it can be searched. Source: https://github.com/stripe/stripe-js/blob/v10.2.1/types/shared.d.ts

```ts
import {StripeConstructorOptions, Stripe} from './stripe-js';

export type ReleaseTrain = 'endive';

export const loadStripe: (
  publishableKey: string,
  options?: StripeConstructorOptions | undefined
) => Promise<Stripe | null>;

```
