# Stripe.js 10.2.1 and React Stripe.js 7.0.1

**`@stripe/stripe-js` 10.2.1** is the npm loader and TypeScript definitions for
Stripe.js, Stripe's browser SDK. Major version 10 is pinned to the Stripe.js
release **`endive`** (it loads `https://js.stripe.com/endive/stripe.js`).
**`@stripe/react-stripe-js` 7.0.1** wraps it for React: the `<Elements>`
provider, the `useStripe` / `useElements` hooks and one component per Element
(`CardElement`, `PaymentElement`, ...). Its peer dependency is
`@stripe/stripe-js >=10.0.0 <11.0.0`. Both come from Stripe's GitHub repos at
the release tags (MIT).

Stripe doesn't publish its Stripe.js prose reference under an open licence, so
here the **type definitions are the reference**: every method and option carries
JSDoc copied from that reference. For the prose pages (docs.stripe.com/js, React
Stripe.js reference, Payment Element and 3-D Secure guides) search the
local-only **`stripe-guides`** set; for the server-side REST API see
**`stripe-api`**.

## Layout

| Path | What it holds |
|---|---|
| `content/stripe-js/README.md` | Install, versioning table (package major → Stripe.js release), `loadStripe`, `@stripe/stripe-js/pure`, `loadStripe.setLoadParameters({advancedFraudSignals: false})` |
| `content/stripe-js/api-reference/types/stripe-js/` | The `Stripe` instance (`stripe.d.ts.md`), PaymentIntent/SetupIntent confirm option types, `elements-group.d.ts.md` (`stripe.elements()` options), and `elements/` (one file per Element type and its options/events) |
| `content/stripe-js/api-reference/types/api/` | Client-side shapes of API objects (`payment-intents`, `payment-methods`, `setup-intents`, ...) |
| `content/stripe-js/api-reference/src/` | Loader source (`shared.ts`: script URL, `RELEASE_TRAIN`) |
| `content/react-stripe-js/README.md`, `migrating.md` | Getting started; migrating from `react-stripe-elements` |
| `content/react-stripe-js/api-reference/src/` | `components/Elements.tsx` (provider, `useElements`), `useStripe.tsx`, `createElementComponent.tsx` (how Element components mount/update/fire events), `types/index.ts` (component prop types), `index.ts` (all exports) |
| `content/react-stripe-js/examples/` | Working examples: `hooks/0-Card-Minimal`, `1-Card-Detailed`, `2-Split-Card`, `9-Payment-Element`, `11-Custom-Checkout`, ...; same in `class-components/` |
| `content/release-notes/` | GitHub release notes, stripe-js v10.0.0-v10.2.1 and react-stripe-js v7.0.0-v7.0.1 |

Every source/type file is the verbatim file wrapped in a Markdown code fence,
named `<original name>.md`.

## Where to look for…

| Task | File |
|---|---|
| Load Stripe.js once (`loadStripe(publishableKey, options)`) | `content/stripe-js/README.md` |
| Wrap the app in `<Elements stripe={stripePromise} options={...}>` | `content/react-stripe-js/api-reference/src/components/Elements.tsx.md`, examples |
| Get the instances inside a component (`useStripe()`, `useElements()`) | `components/useStripe.tsx.md`, `components/Elements.tsx.md` |
| `CardElement` props and options (`hidePostalCode`, style, `onChange`) | `content/stripe-js/api-reference/types/stripe-js/elements/card.d.ts.md`, `content/react-stripe-js/api-reference/src/types/index.ts.md` |
| `PaymentElement` options (layout, `fields`, `wallets`, `update()`) | `types/stripe-js/elements/payment.d.ts.md` |
| `stripe.createPaymentMethod({type: 'card', card: cardElement, billing_details})` or `{elements}` | `types/stripe-js/stripe.d.ts.md` (search `createPaymentMethod`) |
| `stripe.confirmCardPayment(clientSecret, {payment_method: {card}})`: confirms and runs 3-D Secure when the PaymentIntent needs it | `types/stripe-js/stripe.d.ts.md`, option types in `types/stripe-js/payment-intents.d.ts.md` |
| PaymentIntent in `requires_action` confirmed on your server: `stripe.handleNextAction({clientSecret})` (or `handleCardAction` for manual confirmation) | `types/stripe-js/stripe.d.ts.md` |
| `stripe.confirmPayment({elements, confirmParams: {return_url}, redirect: 'if_required'})` for the Payment Element | `types/stripe-js/stripe.d.ts.md` |
| Saving a card for later (`confirmCardSetup`, `confirmSetup`) | `types/stripe-js/stripe.d.ts.md`, `types/stripe-js/setup-intents.d.ts.md` |
| Result shape (`{paymentIntent}` or `{error}`) and the `StripeError` / `StripeErrorType` types | `types/stripe-js/stripe.d.ts.md` |
| Payment Element with React | `content/react-stripe-js/examples/hooks/9-Payment-Element.tsx.md` |
| Card Element with React | `content/react-stripe-js/examples/hooks/0-Card-Minimal.tsx.md`, `1-Card-Detailed.tsx.md` |

## Version notes

- **stripe-js 10.0.0** (2026-10-01): moved to Stripe.js `endive`; removed the
  payment request button and the Elements `paymentMethodTypes` option from the
  types; added a retry to the loader.
- **stripe-js 10.2.0**: `defaultCollapsed` and `paymentMethodLogoPosition`
  removed from the PaymentElement `update()` types (they can't be updated).
- **react-stripe-js 7.0.0** (2026-10-01): "Upgrade to React 19"; payment
  request button removed. The package's peer range is still React
  `>=16.8.0 <20.0.0`.
- **react-stripe-js 7.0.1**: fixes `EmbeddedCheckoutProvider` not registering
  with Stripe.js.
- Stripe.js releases (`acacia`, `basil`, `clover`, `dahlia`, `endive`) each
  correspond to a major of this package (see the README's versioning table).

## Search tips

- Methods are on the `Stripe` interface in `stripe.d.ts.md`; option and result
  types are named `Confirm*Data`, `*Options`, `PaymentIntentResult`,
  `PaymentMethodResult`.
- Element type names are lowercase strings in `elements.create('card')` /
  `getElement(CardElement)`; their option types are `Stripe<Name>ElementOptions`
  in `types/stripe-js/elements/<name>.d.ts.md`.
- React components are `<Name>Element` (`CardElement`, `PaymentElement`,
  `AddressElement`, `ExpressCheckoutElement`).
