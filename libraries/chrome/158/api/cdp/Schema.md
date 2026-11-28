# Schema domain *(deprecated)*

This domain is deprecated.

Methods are called as `Schema.<command>` and events arrive as `Schema.<event>`.

## Commands

### Schema.getDomains

Returns supported domains.

**Returns**

| Name | Type | Description |
|---|---|---|
| `domains` | array of [Domain](#type-domain) | List of supported domains. |

## Types

<a id="type-domain"></a>
### Schema.Domain

Type: object

Description of the protocol domain.

**Properties**

| Name | Type | Description |
|---|---|---|
| `name` | string | Domain name. |
| `version` | string | Domain version. |

