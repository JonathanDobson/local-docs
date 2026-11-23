---
title: "types/pure.d.ts"
source_url: https://github.com/stripe/stripe-js/blob/v10.2.1/types/pure.d.ts
---

# `types/pure.d.ts` (stripe/stripe-js v10.2.1)

Verbatim source file, wrapped in Markdown so it can be searched. Source: https://github.com/stripe/stripe-js/blob/v10.2.1/types/pure.d.ts

```ts
import {loadStripe as _loadStripe} from './shared';

export {ReleaseTrain} from './shared';

export const loadStripe: typeof _loadStripe & {
  setLoadParameters: (params: {advancedFraudSignals: boolean}) => void;
};

```
