---
title: "types/stripe-js/elements/au-bank-account.d.ts"
source_url: https://github.com/stripe/stripe-js/blob/v10.2.1/types/stripe-js/elements/au-bank-account.d.ts
---

# `types/stripe-js/elements/au-bank-account.d.ts` (stripe/stripe-js v10.2.1)

Verbatim source file, wrapped in Markdown so it can be searched. Source: https://github.com/stripe/stripe-js/blob/v10.2.1/types/stripe-js/elements/au-bank-account.d.ts

```ts
import {
  StripeElementBase,
  StripeElementStyle,
  StripeElementClasses,
  StripeElementChangeEvent,
} from './base';

export type StripeAuBankAccountElement = StripeElementBase & {
  /**
   * The change event is triggered when the `Element`'s value changes.
   */
  on(
    eventType: 'change',
    handler: (event: StripeAuBankAccountElementChangeEvent) => any
  ): StripeAuBankAccountElement;
  once(
    eventType: 'change',
    handler: (event: StripeAuBankAccountElementChangeEvent) => any
  ): StripeAuBankAccountElement;
  off(
    eventType: 'change',
    handler?: (event: StripeAuBankAccountElementChangeEvent) => any
  ): StripeAuBankAccountElement;

  /**
   * Triggered when the element is fully rendered and can accept `element.focus` calls.
   */
  on(
    eventType: 'ready',
    handler: (event: {elementType: 'auBankAccount'}) => any
  ): StripeAuBankAccountElement;
  once(
    eventType: 'ready',
    handler: (event: {elementType: 'auBankAccount'}) => any
  ): StripeAuBankAccountElement;
  off(
    eventType: 'ready',
    handler?: (event: {elementType: 'auBankAccount'}) => any
  ): StripeAuBankAccountElement;

  /**
   * Triggered when the element gains focus.
   */
  on(
    eventType: 'focus',
    handler: (event: {elementType: 'auBankAccount'}) => any
  ): StripeAuBankAccountElement;
  once(
    eventType: 'focus',
    handler: (event: {elementType: 'auBankAccount'}) => any
  ): StripeAuBankAccountElement;
  off(
    eventType: 'focus',
    handler?: (event: {elementType: 'auBankAccount'}) => any
  ): StripeAuBankAccountElement;

  /**
   * Triggered when the element loses focus.
   */
  on(
    eventType: 'blur',
    handler: (event: {elementType: 'auBankAccount'}) => any
  ): StripeAuBankAccountElement;
  once(
    eventType: 'blur',
    handler: (event: {elementType: 'auBankAccount'}) => any
  ): StripeAuBankAccountElement;
  off(
    eventType: 'blur',
    handler?: (event: {elementType: 'auBankAccount'}) => any
  ): StripeAuBankAccountElement;

  /**
   * Triggered when the escape key is pressed within the element.
   */
  on(
    eventType: 'escape',
    handler: (event: {elementType: 'auBankAccount'}) => any
  ): StripeAuBankAccountElement;
  once(
    eventType: 'escape',
    handler: (event: {elementType: 'auBankAccount'}) => any
  ): StripeAuBankAccountElement;
  off(
    eventType: 'escape',
    handler?: (event: {elementType: 'auBankAccount'}) => any
  ): StripeAuBankAccountElement;

  /**
   * Updates the options the `AuBankAccountElement` was initialized with.
   * Updates are merged into the existing configuration.
   *
   * The styles of an `AuBankAccountElement` can be dynamically changed using `element.update`.
   * This method can be used to simulate CSS media queries that automatically adjust the size of elements when viewed on different devices.
   */
  update(options: Partial<StripeAuBankAccountElementOptions>): void;
};

export interface StripeAuBankAccountElementOptions {
  classes?: StripeElementClasses;

  style?: StripeElementStyle;

  /**
   * Appearance of the icon in the Element.
   */
  iconStyle?: 'default' | 'solid';

  /**
   * Hides the icon in the Element.
   * Default is `false`.
   */
  hideIcon?: boolean;

  /**
   * Applies a disabled state to the Element such that user input is not accepted.
   * Default is false.
   */
  disabled?: boolean;
}

export interface StripeAuBankAccountElementChangeEvent
  extends StripeElementChangeEvent {
  /**
   * The type of element that emitted this event.
   */
  elementType: 'auBankAccount';

  /**
   * The bank name corresponding to the entered BSB.
   */
  bankName?: string;

  /**
   * The branch name corresponding to the entered BSB.
   */
  branchName?: string;
}

```
