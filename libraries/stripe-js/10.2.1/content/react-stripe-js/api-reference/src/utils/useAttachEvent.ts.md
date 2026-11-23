---
title: "src/utils/useAttachEvent.ts"
source_url: https://github.com/stripe/react-stripe-js/blob/v7.0.1/src/utils/useAttachEvent.ts
---

# `src/utils/useAttachEvent.ts` (stripe/react-stripe-js v7.0.1)

Verbatim source file, wrapped in Markdown so it can be searched. Source: https://github.com/stripe/react-stripe-js/blob/v7.0.1/src/utils/useAttachEvent.ts

```ts
import React from 'react';
import * as stripeJs from '@stripe/stripe-js';

export const useAttachEvent = <A extends unknown[]>(
  element: stripeJs.StripeElement | null,
  event: string,
  cb?: (...args: A) => any
) => {
  const cbDefined = !!cb;
  const cbRef = React.useRef(cb);

  // In many integrations the callback prop changes on each render.
  // Using a ref saves us from calling element.on/.off every render.
  React.useEffect(() => {
    cbRef.current = cb;
  }, [cb]);

  React.useEffect(() => {
    if (!cbDefined || !element) {
      return () => {};
    }

    const decoratedCb = (...args: A) => {
      if (cbRef.current) {
        return cbRef.current(...args);
      }
      return undefined;
    };

    (element as any).on(event, decoratedCb);

    return () => {
      (element as any).off(event, decoratedCb);
    };
  }, [cbDefined, event, element, cbRef]);
};

```
