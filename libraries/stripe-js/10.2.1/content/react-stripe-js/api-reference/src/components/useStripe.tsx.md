---
title: "src/components/useStripe.tsx"
source_url: https://github.com/stripe/react-stripe-js/blob/v7.0.1/src/components/useStripe.tsx
---

# `src/components/useStripe.tsx` (stripe/react-stripe-js v7.0.1)

Verbatim source file, wrapped in Markdown so it can be searched. Source: https://github.com/stripe/react-stripe-js/blob/v7.0.1/src/components/useStripe.tsx

```tsx
import * as stripeJs from '@stripe/stripe-js';
import {useElementsOrCheckoutContextWithUseCase} from '../checkout/components/CheckoutContext';

/**
 * @docs https://stripe.com/docs/stripe-js/react#usestripe-hook
 */
export const useStripe = (): stripeJs.Stripe | null => {
  const {stripe} = useElementsOrCheckoutContextWithUseCase('calls useStripe()');
  return stripe;
};

```
