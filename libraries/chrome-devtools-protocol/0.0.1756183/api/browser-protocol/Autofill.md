# Autofill domain

Chrome DevTools Protocol, browser protocol (tip-of-tree) (protocol 1.3).

**Experimental**

Defines commands and events for Autofill.

4 methods, 1 events, 7 types.

## Methods

### Autofill.trigger

Trigger autofill on a form identified by the fieldId.
If the field and related form cannot be autofilled, returns an error.
Returns once the values have been applied to the form fields.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `fieldId` | [DOM.BackendNodeId](DOM.md#type-backendnodeid) | Identifies a field that serves as an anchor for autofill. |
| `frameId` (optional) | [Page.FrameId](Page.md#type-frameid) | Identifies the frame that field belongs to. |
| `card` (optional) | [Autofill.CreditCard](#type-creditcard) | Credit card information to fill out the form. Credit card data is not saved. Mutually exclusive with `address`. |
| `address` (optional) | [Autofill.Address](#type-address) | Address to fill out the form. Address data is not saved. Mutually exclusive with `card`. |

### Autofill.setAddresses

Set addresses so that developers can verify their forms implementation.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `addresses` | array of [Autofill.Address](#type-address) |  |

### Autofill.disable

Disables autofill domain notifications.

No parameters.

### Autofill.enable

Enables autofill domain notifications.

No parameters.

## Events

### Autofill.addressFormFilled

Emitted when an address form is filled.

**Event parameters**

| Name | Type | Description |
|---|---|---|
| `filledFields` | array of [Autofill.FilledField](#type-filledfield) | Information about the fields that were filled |
| `addressUi` | [Autofill.AddressUI](#type-addressui) | An UI representation of the address used to fill the form. Consists of a 2D array where each child represents an address/profile line. |

## Types

<a id="type-creditcard"></a>
### Autofill.CreditCard

Type: object

**Properties**

| Name | Type | Description |
|---|---|---|
| `number` | string | 16-digit credit card number. |
| `name` | string | Name of the credit card owner. |
| `expiryMonth` | string | 2-digit expiry month. |
| `expiryYear` | string | 4-digit expiry year. |
| `cvc` | string | 3-digit card verification code. |

<a id="type-addressfield"></a>
### Autofill.AddressField

Type: object

**Properties**

| Name | Type | Description |
|---|---|---|
| `name` | string | address field name, for example GIVEN_NAME. The full list of supported field names: https://source.chromium.org/chromium/chromium/src/+/main:components/autofill/core/browser/field_types.cc;l=38 |
| `value` | string | address field value, for example Jon Doe. |

<a id="type-addressfields"></a>
### Autofill.AddressFields

A list of address fields.

Type: object

**Properties**

| Name | Type | Description |
|---|---|---|
| `fields` | array of [Autofill.AddressField](#type-addressfield) |  |

<a id="type-address"></a>
### Autofill.Address

Type: object

**Properties**

| Name | Type | Description |
|---|---|---|
| `fields` | array of [Autofill.AddressField](#type-addressfield) | fields and values defining an address. |

<a id="type-addressui"></a>
### Autofill.AddressUI

Defines how an address can be displayed like in chrome://settings/addresses.
Address UI is a two dimensional array, each inner array is an "address information line", and when rendered in a UI surface should be displayed as such.
The following address UI for instance:
[[{name: "GIVE_NAME", value: "Jon"}, {name: "FAMILY_NAME", value: "Doe"}], [{name: "CITY", value: "Munich"}, {name: "ZIP", value: "81456"}]]
should allow the receiver to render:
Jon Doe
Munich 81456

Type: object

**Properties**

| Name | Type | Description |
|---|---|---|
| `addressFields` | array of [Autofill.AddressFields](#type-addressfields) | A two dimension array containing the representation of values from an address profile. |

<a id="type-fillingstrategy"></a>
### Autofill.FillingStrategy

Specified whether a filled field was done so by using the html autocomplete attribute or autofill heuristics.

Type: string

Allowed values: `autocompleteAttribute`, `autofillInferred`

<a id="type-filledfield"></a>
### Autofill.FilledField

Type: object

**Properties**

| Name | Type | Description |
|---|---|---|
| `htmlType` | string | The type of the field, e.g text, password etc. |
| `id` | string | the html id |
| `name` | string | the html name |
| `value` | string | the field value |
| `autofillType` | string | The actual field type, e.g FAMILY_NAME |
| `fillingStrategy` | [Autofill.FillingStrategy](#type-fillingstrategy) | The filling strategy |
| `frameId` | [Page.FrameId](Page.md#type-frameid) | The frame the field belongs to |
| `fieldId` | [DOM.BackendNodeId](DOM.md#type-backendnodeid) | The form field's DOM node |
