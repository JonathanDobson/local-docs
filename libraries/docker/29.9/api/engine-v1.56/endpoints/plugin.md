# Docker Engine API 1.56 — Plugin

## GET /v1.56/plugins

operationId: `PluginList`

List plugins

Returns information about installed plugins.

| Parameter | In | Type | Required | Description |
|---|---|---|---|---|
| `filters` | query | string |  | A JSON encoded value of the filters (a `map[string][]string`) to process on the plugin list. Available filters: - `capability=<capability name>` - `enable=<true>\|<false>` |

| Response | Description | Body |
|---|---|---|
| 200 | No error | array of `Plugin` |
| 500 | Server error | `ErrorResponse` |

## GET /v1.56/plugins/privileges

operationId: `GetPluginPrivileges`

Get plugin privileges

| Parameter | In | Type | Required | Description |
|---|---|---|---|---|
| `remote` | query | string | yes | The name of the plugin. The `:latest` tag is optional, and is the default if omitted. |

| Response | Description | Body |
|---|---|---|
| 200 | no error | array of `PluginPrivilege` |
| 500 | server error | `ErrorResponse` |

## POST /v1.56/plugins/pull

operationId: `PluginPull`

Install a plugin

Pulls and installs a plugin. After the plugin is installed, it can be
enabled using the [`POST /plugins/{name}/enable` endpoint](#operation/PostPluginsEnable).

| Parameter | In | Type | Required | Description |
|---|---|---|---|---|
| `remote` | query | string | yes | Remote reference for plugin to install. The `:latest` tag is optional, and is used as the default if omitted. |
| `name` | query | string |  | Local name for the pulled plugin. The `:latest` tag is optional, and is used as the default if omitted. |
| `X-Registry-Auth` | header | string |  | A base64url-encoded auth configuration to use when pulling a plugin from a registry. Refer to the [authentication section](#section/Authentication) for details. |

Request body: array of `PluginPrivilege`

| Response | Description | Body |
|---|---|---|
| 204 | no error |  |
| 500 | server error | `ErrorResponse` |

## GET /v1.56/plugins/{name}/json

operationId: `PluginInspect`

Inspect a plugin

| Parameter | In | Type | Required | Description |
|---|---|---|---|---|
| `name` | path | string | yes | The name of the plugin. The `:latest` tag is optional, and is the default if omitted. |

| Response | Description | Body |
|---|---|---|
| 200 | no error | `Plugin` |
| 404 | plugin is not installed | `ErrorResponse` |
| 500 | server error | `ErrorResponse` |

## DELETE /v1.56/plugins/{name}

operationId: `PluginDelete`

Remove a plugin

| Parameter | In | Type | Required | Description |
|---|---|---|---|---|
| `name` | path | string | yes | The name of the plugin. The `:latest` tag is optional, and is the default if omitted. |
| `force` | query | boolean |  | Disable the plugin before removing. This may result in issues if the plugin is in use by a container. |

| Response | Description | Body |
|---|---|---|
| 200 | no error | `Plugin` |
| 404 | plugin is not installed | `ErrorResponse` |
| 500 | server error | `ErrorResponse` |

## POST /v1.56/plugins/{name}/enable

operationId: `PluginEnable`

Enable a plugin

| Parameter | In | Type | Required | Description |
|---|---|---|---|---|
| `name` | path | string | yes | The name of the plugin. The `:latest` tag is optional, and is the default if omitted. |
| `timeout` | query | integer |  | Set the HTTP client timeout (in seconds) |

| Response | Description | Body |
|---|---|---|
| 200 | no error |  |
| 404 | plugin is not installed | `ErrorResponse` |
| 500 | server error | `ErrorResponse` |

## POST /v1.56/plugins/{name}/disable

operationId: `PluginDisable`

Disable a plugin

| Parameter | In | Type | Required | Description |
|---|---|---|---|---|
| `name` | path | string | yes | The name of the plugin. The `:latest` tag is optional, and is the default if omitted. |
| `force` | query | boolean |  | Force disable a plugin even if still in use. |

| Response | Description | Body |
|---|---|---|
| 200 | no error |  |
| 404 | plugin is not installed | `ErrorResponse` |
| 500 | server error | `ErrorResponse` |

## POST /v1.56/plugins/{name}/upgrade

operationId: `PluginUpgrade`

Upgrade a plugin

| Parameter | In | Type | Required | Description |
|---|---|---|---|---|
| `name` | path | string | yes | The name of the plugin. The `:latest` tag is optional, and is the default if omitted. |
| `remote` | query | string | yes | Remote reference to upgrade to. The `:latest` tag is optional, and is used as the default if omitted. |
| `X-Registry-Auth` | header | string |  | A base64url-encoded auth configuration to use when pulling a plugin from a registry. Refer to the [authentication section](#section/Authentication) for details. |

Request body: array of `PluginPrivilege`

| Response | Description | Body |
|---|---|---|
| 204 | no error |  |
| 404 | plugin not installed | `ErrorResponse` |
| 500 | server error | `ErrorResponse` |

## POST /v1.56/plugins/create

operationId: `PluginCreate`

Create a plugin

| Parameter | In | Type | Required | Description |
|---|---|---|---|---|
| `name` | query | string | yes | The name of the plugin. The `:latest` tag is optional, and is the default if omitted. |

Request body: string (binary)

| Response | Description | Body |
|---|---|---|
| 204 | no error |  |
| 500 | server error | `ErrorResponse` |

## POST /v1.56/plugins/{name}/push

operationId: `PluginPush`

Push a plugin

Push a plugin to the registry.

| Parameter | In | Type | Required | Description |
|---|---|---|---|---|
| `name` | path | string | yes | The name of the plugin. The `:latest` tag is optional, and is the default if omitted. |

| Response | Description | Body |
|---|---|---|
| 200 | no error |  |
| 404 | plugin not installed | `ErrorResponse` |
| 500 | server error | `ErrorResponse` |

## POST /v1.56/plugins/{name}/set

operationId: `PluginSet`

Configure a plugin

| Parameter | In | Type | Required | Description |
|---|---|---|---|---|
| `name` | path | string | yes | The name of the plugin. The `:latest` tag is optional, and is the default if omitted. |

Request body: array of string

| Response | Description | Body |
|---|---|---|
| 204 | No error |  |
| 404 | Plugin not installed | `ErrorResponse` |
| 500 | Server error | `ErrorResponse` |
