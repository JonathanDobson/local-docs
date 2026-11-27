# Schema domain

Chrome DevTools Protocol, JavaScript / V8 inspector protocol (protocol 1.3).

**Deprecated**

This domain is deprecated.

1 methods, 0 events, 1 types.

## Methods

### Schema.getDomains

Returns supported domains.

No parameters.

**Return object**

| Name | Type | Description |
|---|---|---|
| `domains` | array of [Schema.Domain](#type-domain) | List of supported domains. |

## Types

<a id="type-domain"></a>
### Schema.Domain

Description of the protocol domain.

Type: object

**Properties**

| Name | Type | Description |
|---|---|---|
| `name` | string | Domain name. |
| `version` | string | Domain version. |
