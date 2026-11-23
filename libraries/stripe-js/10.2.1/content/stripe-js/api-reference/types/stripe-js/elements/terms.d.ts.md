---
title: "types/stripe-js/elements/terms.d.ts"
source_url: https://github.com/stripe/stripe-js/blob/v10.2.1/types/stripe-js/elements/terms.d.ts
---

# `types/stripe-js/elements/terms.d.ts` (stripe/stripe-js v10.2.1)

Verbatim source file, wrapped in Markdown so it can be searched. Source: https://github.com/stripe/stripe-js/blob/v10.2.1/types/stripe-js/elements/terms.d.ts

```ts
import {StripeElementBase} from './base';
import {StripeError} from '../stripe';

export type StripeTermsElement = StripeElementBase & {
  /**
   * Triggered when the element is fully rendered and can accept `element.focus` calls.
   */
  on(
    eventType: 'ready',
    handler: (event: {elementType: 'terms'}) => any
  ): StripeTermsElement;
  once(
    eventType: 'ready',
    handler: (event: {elementType: 'terms'}) => any
  ): StripeTermsElement;
  off(
    eventType: 'ready',
    handler?: (event: {elementType: 'terms'}) => any
  ): StripeTermsElement;

  /**
   * Triggered when the element gains focus.
   */
  on(
    eventType: 'focus',
    handler: (event: {elementType: 'terms'}) => any
  ): StripeTermsElement;
  once(
    eventType: 'focus',
    handler: (event: {elementType: 'terms'}) => any
  ): StripeTermsElement;
  off(
    eventType: 'focus',
    handler?: (event: {elementType: 'terms'}) => any
  ): StripeTermsElement;

  /**
   * Triggered when the element loses focus.
   */
  on(
    eventType: 'blur',
    handler: (event: {elementType: 'terms'}) => any
  ): StripeTermsElement;
  once(
    eventType: 'blur',
    handler: (event: {elementType: 'terms'}) => any
  ): StripeTermsElement;
  off(
    eventType: 'blur',
    handler?: (event: {elementType: 'terms'}) => any
  ): StripeTermsElement;

  /**
   * Triggered when the escape key is pressed within the element.
   */
  on(
    eventType: 'escape',
    handler: (event: {elementType: 'terms'}) => any
  ): StripeTermsElement;
  once(
    eventType: 'escape',
    handler: (event: {elementType: 'terms'}) => any
  ): StripeTermsElement;
  off(
    eventType: 'escape',
    handler?: (event: {elementType: 'terms'}) => any
  ): StripeTermsElement;

  /**
   * Triggered when the element fails to load.
   */
  on(
    eventType: 'loaderror',
    handler: (event: {elementType: 'terms'; error: StripeError}) => any
  ): StripeTermsElement;
  once(
    eventType: 'loaderror',
    handler: (event: {elementType: 'terms'; error: StripeError}) => any
  ): StripeTermsElement;
  off(
    eventType: 'loaderror',
    handler?: (event: {elementType: 'terms'; error: StripeError}) => any
  ): StripeTermsElement;

  /**
   * Triggered when the loader UI is mounted to the DOM and ready to be displayed.
   */
  on(
    eventType: 'loaderstart',
    handler: (event: {elementType: 'terms'}) => any
  ): StripeTermsElement;
  once(
    eventType: 'loaderstart',
    handler: (event: {elementType: 'terms'}) => any
  ): StripeTermsElement;
  off(
    eventType: 'loaderstart',
    handler?: (event: {elementType: 'terms'}) => any
  ): StripeTermsElement;
};

export interface StripeTermsElementOptions {}

```
