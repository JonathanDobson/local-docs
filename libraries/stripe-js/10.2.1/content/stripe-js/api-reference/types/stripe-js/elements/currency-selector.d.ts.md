---
title: "types/stripe-js/elements/currency-selector.d.ts"
source_url: https://github.com/stripe/stripe-js/blob/v10.2.1/types/stripe-js/elements/currency-selector.d.ts
---

# `types/stripe-js/elements/currency-selector.d.ts` (stripe/stripe-js v10.2.1)

Verbatim source file, wrapped in Markdown so it can be searched. Source: https://github.com/stripe/stripe-js/blob/v10.2.1/types/stripe-js/elements/currency-selector.d.ts

```ts
import {StripeElementBase} from './base';
import {StripeError} from '../stripe';

export type StripeCurrencySelectorElement = StripeElementBase & {
  /**
   * Triggered when the element is fully rendered and can accept `element.focus` calls.
   */
  on(
    eventType: 'ready',
    handler: (event: {elementType: 'currencySelector'}) => any
  ): StripeCurrencySelectorElement;
  once(
    eventType: 'ready',
    handler: (event: {elementType: 'currencySelector'}) => any
  ): StripeCurrencySelectorElement;
  off(
    eventType: 'ready',
    handler?: (event: {elementType: 'currencySelector'}) => any
  ): StripeCurrencySelectorElement;

  /**
   * Triggered when the element gains focus.
   */
  on(
    eventType: 'focus',
    handler: (event: {elementType: 'currencySelector'}) => any
  ): StripeCurrencySelectorElement;
  once(
    eventType: 'focus',
    handler: (event: {elementType: 'currencySelector'}) => any
  ): StripeCurrencySelectorElement;
  off(
    eventType: 'focus',
    handler?: (event: {elementType: 'currencySelector'}) => any
  ): StripeCurrencySelectorElement;

  /**
   * Triggered when the element loses focus.
   */
  on(
    eventType: 'blur',
    handler: (event: {elementType: 'currencySelector'}) => any
  ): StripeCurrencySelectorElement;
  once(
    eventType: 'blur',
    handler: (event: {elementType: 'currencySelector'}) => any
  ): StripeCurrencySelectorElement;
  off(
    eventType: 'blur',
    handler?: (event: {elementType: 'currencySelector'}) => any
  ): StripeCurrencySelectorElement;

  /**
   * Triggered when the escape key is pressed within the element.
   */
  on(
    eventType: 'escape',
    handler: (event: {elementType: 'currencySelector'}) => any
  ): StripeCurrencySelectorElement;
  once(
    eventType: 'escape',
    handler: (event: {elementType: 'currencySelector'}) => any
  ): StripeCurrencySelectorElement;
  off(
    eventType: 'escape',
    handler?: (event: {elementType: 'currencySelector'}) => any
  ): StripeCurrencySelectorElement;

  /**
   * Triggered when the element fails to load.
   */
  on(
    eventType: 'loaderror',
    handler: (event: {
      elementType: 'currencySelector';
      error: StripeError;
    }) => any
  ): StripeCurrencySelectorElement;
  once(
    eventType: 'loaderror',
    handler: (event: {
      elementType: 'currencySelector';
      error: StripeError;
    }) => any
  ): StripeCurrencySelectorElement;
  off(
    eventType: 'loaderror',
    handler?: (event: {
      elementType: 'currencySelector';
      error: StripeError;
    }) => any
  ): StripeCurrencySelectorElement;
};

export interface StripeCurrencySelectorElementOptions {}

```
