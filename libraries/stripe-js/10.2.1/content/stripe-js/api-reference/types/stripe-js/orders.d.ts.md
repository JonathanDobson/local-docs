---
title: "types/stripe-js/orders.d.ts"
source_url: https://github.com/stripe/stripe-js/blob/v10.2.1/types/stripe-js/orders.d.ts
---

# `types/stripe-js/orders.d.ts` (stripe/stripe-js v10.2.1)

Verbatim source file, wrapped in Markdown so it can be searched. Source: https://github.com/stripe/stripe-js/blob/v10.2.1/types/stripe-js/orders.d.ts

```ts
/**
 * Parameters that will be passed on to the Stripe API to confirm payment for an Order's PaymentIntent.
 */
export interface ProcessOrderParams {
  /**
   * The url your customer will be directed to after they complete payment.
   */
  return_url: string;
}

```
