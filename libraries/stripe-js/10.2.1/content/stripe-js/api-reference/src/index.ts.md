---
title: "src/index.ts"
source_url: https://github.com/stripe/stripe-js/blob/v10.2.1/src/index.ts
---

# `src/index.ts` (stripe/stripe-js v10.2.1)

Verbatim source file, wrapped in Markdown so it can be searched. Source: https://github.com/stripe/stripe-js/blob/v10.2.1/src/index.ts

```ts
import {StripeConstructor} from '../types';
import {loadScript, initStripe, LoadStripe} from './shared';

let stripePromise: Promise<StripeConstructor | null> | null;
let loadCalled = false;

const getStripePromise: () => Promise<StripeConstructor | null> = () => {
  if (stripePromise) {
    return stripePromise;
  }

  stripePromise = loadScript(null).catch((error) => {
    // clear cache on error
    stripePromise = null;
    return Promise.reject(error);
  });
  return stripePromise;
};

// Execute our own script injection after a tick to give users time to do their
// own script injection.
Promise.resolve()
  .then(() => getStripePromise())
  .catch((error) => {
    if (!loadCalled) {
      console.warn(error);
    }
  });

export const loadStripe: LoadStripe = (...args) => {
  loadCalled = true;
  const startTime = Date.now();

  // if previous attempts are unsuccessful, will re-load script
  return getStripePromise().then((maybeStripe) =>
    initStripe(maybeStripe, args, startTime)
  );
};

```
