---
title: "src/utils/usePrevious.ts"
source_url: https://github.com/stripe/react-stripe-js/blob/v7.0.1/src/utils/usePrevious.ts
---

# `src/utils/usePrevious.ts` (stripe/react-stripe-js v7.0.1)

Verbatim source file, wrapped in Markdown so it can be searched. Source: https://github.com/stripe/react-stripe-js/blob/v7.0.1/src/utils/usePrevious.ts

```ts
import React from 'react';

export const usePrevious = <T>(value: T): T => {
  const ref = React.useRef(value);

  React.useEffect(() => {
    ref.current = value;
  }, [value]);

  return ref.current;
};

```
