---
title: "src/utils/registerWithStripeJs.ts"
source_url: https://github.com/stripe/react-stripe-js/blob/v7.0.1/src/utils/registerWithStripeJs.ts
---

# `src/utils/registerWithStripeJs.ts` (stripe/react-stripe-js v7.0.1)

Verbatim source file, wrapped in Markdown so it can be searched. Source: https://github.com/stripe/react-stripe-js/blob/v7.0.1/src/utils/registerWithStripeJs.ts

```ts
import * as stripeJs from '@stripe/stripe-js';

export const registerWithStripeJs = (stripe: stripeJs.Stripe | null) => {
  if (
    !stripe ||
    !('_registerWrapper' in stripe) ||
    typeof stripe._registerWrapper !== 'function' ||
    typeof stripe.registerAppInfo !== 'function'
  ) {
    return;
  }

  stripe._registerWrapper({name: 'react-stripe-js', version: _VERSION});

  stripe.registerAppInfo({
    name: 'react-stripe-js',
    version: _VERSION,
    url: 'https://stripe.com/docs/stripe-js/react',
  });
};

```
