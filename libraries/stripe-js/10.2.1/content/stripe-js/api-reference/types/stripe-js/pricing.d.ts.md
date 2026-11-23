---
title: "types/stripe-js/pricing.d.ts"
source_url: https://github.com/stripe/stripe-js/blob/v10.2.1/types/stripe-js/pricing.d.ts
---

# `types/stripe-js/pricing.d.ts` (stripe/stripe-js v10.2.1)

Verbatim source file, wrapped in Markdown so it can be searched. Source: https://github.com/stripe/stripe-js/blob/v10.2.1/types/stripe-js/pricing.d.ts

```ts
export type CurrencyInfo = {
  currency: string;
};

export type ResolvedPriceAmount = {amount: string; minorUnitsAmount: number};

export type ResolvedPrice = {
  currency: string;
  unitAmount: null | ResolvedPriceAmount;
  unitAmountDecimal: null | ResolvedPriceAmount;
  minorUnitsAmountDivisor: number;
};

export type PricingToken = {
  id: string;
};

export type PricingChangeEvent = Record<string, never>;

export type InitializePricingOptions = {
  pricingPolicy: string;
  detectedCurrencyOverride?: string;
};

/**
 * Requires beta access: Contact [Stripe support](https://support.stripe.com/) for more information.
 */
export interface Pricing {
  getAvailableCurrencies(): Promise<CurrencyInfo[]>;

  getSelectedCurrency(): Promise<CurrencyInfo>;

  setSelectedCurrency(currency: string): Promise<void>;

  resolvePrice(price: string): Promise<ResolvedPrice>;

  createPricingToken(): Promise<PricingToken>;

  on(eventType: 'change', handler: (event: PricingChangeEvent) => void): this;

  once(eventType: 'change', handler: (event: PricingChangeEvent) => void): this;

  off(
    eventType: 'change',
    handler?: ((event: PricingChangeEvent) => void) | null
  ): this;
}

```
