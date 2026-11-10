# Docker HUB API 2-beta — scim

## GET /v2/scim/2.0/ServiceProviderConfig

operationId: `getV2Scim20ServiceProviderConfig`

Get service provider config

Returns a service provider config for Docker's configuration.

| Response | Description | Body |
|---|---|---|
| 200 |  (`scim_get_service_provider_config_resp`) | `scim_service_provider_config` |
| 401 | Unauthorized (`scim_unauthorized`) | allOf(`scim_error`, object) |
| 500 | Internal Error (`scim_error`) | allOf(`scim_error`, object) |

## GET /v2/scim/2.0/ResourceTypes

operationId: `getV2Scim20ResourceTypes`

List resource types

Returns all resource types supported for the SCIM configuration.

| Response | Description | Body |
|---|---|---|
| 200 |  (`scim_get_resource_types_resp`) | object |
| 401 | Unauthorized (`scim_unauthorized`) | allOf(`scim_error`, object) |
| 500 | Internal Error (`scim_error`) | allOf(`scim_error`, object) |

## GET /v2/scim/2.0/ResourceTypes/{name}

operationId: `getV2Scim20ResourceTypesByName`

Get a resource type

Returns a resource type by name.

| Parameter | In | Type | Required | Description |
|---|---|---|---|---|
| `name` | path | string | yes | Name of the SCIM resource type. |

| Response | Description | Body |
|---|---|---|
| 200 |  (`scim_get_resource_type_resp`) | `scim_resource_type` |
| 401 | Unauthorized (`scim_unauthorized`) | allOf(`scim_error`, object) |
| 404 | Not Found (`scim_not_found`) | allOf(`scim_error`, object) |
| 500 | Internal Error (`scim_error`) | allOf(`scim_error`, object) |

## GET /v2/scim/2.0/Schemas

operationId: `getV2Scim20Schemas`

List schemas

Returns all schemas supported for the SCIM configuration.

| Response | Description | Body |
|---|---|---|
| 200 |  (`scim_get_schemas_resp`) | object |
| 401 | Unauthorized (`scim_unauthorized`) | allOf(`scim_error`, object) |
| 500 | Internal Error (`scim_error`) | allOf(`scim_error`, object) |

## GET /v2/scim/2.0/Schemas/{id}

operationId: `getV2Scim20SchemasById`

Get a schema

Returns a schema by ID.

| Parameter | In | Type | Required | Description |
|---|---|---|---|---|
| `id` | path | string | yes | URN identifying the SCIM schema. |

| Response | Description | Body |
|---|---|---|
| 200 |  (`scim_get_schema_resp`) | `scim_schema` |
| 401 | Unauthorized (`scim_unauthorized`) | allOf(`scim_error`, object) |
| 404 | Not Found (`scim_not_found`) | allOf(`scim_error`, object) |
| 500 | Internal Error (`scim_error`) | allOf(`scim_error`, object) |

## GET /v2/scim/2.0/Users

operationId: `getV2Scim20Users`

List users

Returns paginated users for an organization. Use `startIndex` and `count` query parameters to receive paginated results.

**Sorting:**

Sorting allows you to specify the order in which resources are returned by specifying a combination of `sortBy` and `sortOrder` query parameters.

The `sortBy` parameter specifies the attribute whose value will be used to order the returned responses. The `sortOrder` parameter defines the order in which the `sortBy` parameter is applied. Allowed values are "ascending" and "descending".

**Filtering:**

You can request a subset of resources by specifying the `filter` query parameter containing a filter expression. Attribute names and attribute operators used in filters are case insensitive. The filter parameter must contain at least one valid expression. Each expression must contain an attribute name followed by an attribute operator and an optional value.

Supported operators are listed below.

- `eq` equal
- `ne` not equal
- `co` contains
- `sw` starts with
- `and` Logical "and"
- `or` Logical "or"
- `not` "Not" function
- `()` Precedence grouping

| Parameter | In | Type | Required | Description |
|---|---|---|---|---|
| `startIndex` | query | integer |  | One-based index of the first result to return. |
| `count` | query | integer |  | Maximum number of results to return. |
| `filter` | query | string |  | SCIM filter expression used to select users. |
| `attributes` | query | string |  | Comma delimited list of attributes to limit to in the response. |
| `sortOrder` | query | string enum: ascending, descending |  | Sort direction applied to the attribute specified by sortBy. |
| `sortBy` | query | string |  | User attribute to sort by. |

| Response | Description | Body |
|---|---|---|
| 200 |  (`scim_get_users_resp`) | object |
| 400 | Bad Request (`scim_bad_request`) | allOf(`scim_error`, object) |
| 401 | Unauthorized (`scim_unauthorized`) | allOf(`scim_error`, object) |
| 403 | Forbidden (`scim_forbidden`) | allOf(`scim_error`, object) |
| 404 | Not Found (`scim_not_found`) | allOf(`scim_error`, object) |
| 500 | Internal Error (`scim_error`) | allOf(`scim_error`, object) |

## POST /v2/scim/2.0/Users

operationId: `postV2Scim20Users`

Create user

Creates a user. If the user already exists by email, they are assigned to the organization on the "company" team.

| Response | Description | Body |
|---|---|---|
| 201 |  (`scim_create_user_resp`) | `scim_user` |
| 400 | Bad Request (`scim_bad_request`) | allOf(`scim_error`, object) |
| 401 | Unauthorized (`scim_unauthorized`) | allOf(`scim_error`, object) |
| 403 | Forbidden (`scim_forbidden`) | allOf(`scim_error`, object) |
| 404 | Not Found (`scim_not_found`) | allOf(`scim_error`, object) |
| 409 | Conflict (`scim_conflict`) | allOf(`scim_error`, object) |
| 500 | Internal Error (`scim_error`) | allOf(`scim_error`, object) |

## GET /v2/scim/2.0/Users/{id}

operationId: `getV2Scim20UsersById`

Get a user

Returns a user by ID.

| Parameter | In | Type | Required | Description |
|---|---|---|---|---|
| `id` | path | string | yes | The user ID. |

| Response | Description | Body |
|---|---|---|
| 200 |  (`scim_get_user_resp`) | `scim_user` |
| 400 | Bad Request (`scim_bad_request`) | allOf(`scim_error`, object) |
| 401 | Unauthorized (`scim_unauthorized`) | allOf(`scim_error`, object) |
| 403 | Forbidden (`scim_forbidden`) | allOf(`scim_error`, object) |
| 404 | Not Found (`scim_not_found`) | allOf(`scim_error`, object) |
| 500 | Internal Error (`scim_error`) | allOf(`scim_error`, object) |

## PUT /v2/scim/2.0/Users/{id}

operationId: `putV2Scim20UsersById`

Update a user

Updates a user. This route is used to change the user's name, activate, and deactivate the user.

| Parameter | In | Type | Required | Description |
|---|---|---|---|---|
| `id` | path | string | yes | The user ID. |

| Response | Description | Body |
|---|---|---|
| 200 |  (`scim_update_user_resp`) | `scim_user` |
| 400 | Bad Request (`scim_bad_request`) | allOf(`scim_error`, object) |
| 401 | Unauthorized (`scim_unauthorized`) | allOf(`scim_error`, object) |
| 403 | Forbidden (`scim_forbidden`) | allOf(`scim_error`, object) |
| 404 | Not Found (`scim_not_found`) | allOf(`scim_error`, object) |
| 409 | Conflict (`scim_conflict`) | allOf(`scim_error`, object) |
| 500 | Internal Error (`scim_error`) | allOf(`scim_error`, object) |
