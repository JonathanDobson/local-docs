# Gitea API 28.3.0 — miscellaneous

## GET /api/v1/gitignore/templates

operationId: `listGitignoresTemplates`

Returns a list of all gitignore templates

| Response | Description | Body |
|---|---|---|
| 200 | GitignoreTemplateList (`GitignoreTemplateList`) | array of string |

## GET /api/v1/gitignore/templates/{name}

operationId: `getGitignoreTemplateInfo`

Returns information about a gitignore template

| Parameter | In | Type | Required | Description |
|---|---|---|---|---|
| `name` | path | string | yes | name of the template |

| Response | Description | Body |
|---|---|---|
| 200 | GitignoreTemplateInfo (`GitignoreTemplateInfo`) | `GitignoreTemplateInfo` |
| 404 | APINotFound is a not found empty response (`notFound`) |  |

## GET /api/v1/label/templates

operationId: `listLabelTemplates`

Returns a list of all label templates

| Response | Description | Body |
|---|---|---|
| 200 | LabelTemplateList (`LabelTemplateList`) | array of string |

## GET /api/v1/label/templates/{name}

operationId: `getLabelTemplateInfo`

Returns all labels in a template

| Parameter | In | Type | Required | Description |
|---|---|---|---|---|
| `name` | path | string | yes | name of the template |

| Response | Description | Body |
|---|---|---|
| 200 | LabelTemplateInfo (`LabelTemplateInfo`) | array of `LabelTemplate` |
| 404 | APINotFound is a not found empty response (`notFound`) |  |

## GET /api/v1/licenses

operationId: `listLicenseTemplates`

Returns a list of all license templates

| Response | Description | Body |
|---|---|---|
| 200 | LicenseTemplateList (`LicenseTemplateList`) | array of `LicensesTemplateListEntry` |

## GET /api/v1/licenses/{name}

operationId: `getLicenseTemplateInfo`

Returns information about a license template

| Parameter | In | Type | Required | Description |
|---|---|---|---|---|
| `name` | path | string | yes | name of the license |

| Response | Description | Body |
|---|---|---|
| 200 | LicenseTemplateInfo (`LicenseTemplateInfo`) | `LicenseTemplateInfo` |
| 404 | APINotFound is a not found empty response (`notFound`) |  |

## POST /api/v1/markdown

operationId: `renderMarkdown`

Render a markdown document as HTML

Request body (application/json): `MarkdownOption`

| Response | Description | Body |
|---|---|---|
| 200 | MarkdownRender is a rendered markdown document (`MarkdownRender`) | string |
| 422 | APIValidationError is error format response related to input validation (`validationError`) |  |

## POST /api/v1/markdown/raw

operationId: `renderMarkdownRaw`

Render raw markdown as HTML

Request body (text/plain): string

| Response | Description | Body |
|---|---|---|
| 200 | MarkdownRender is a rendered markdown document (`MarkdownRender`) | string |
| 422 | APIValidationError is error format response related to input validation (`validationError`) |  |

## POST /api/v1/markup

operationId: `renderMarkup`

Render a markup document as HTML

Request body (application/json): `MarkupOption`

| Response | Description | Body |
|---|---|---|
| 200 | MarkupRender is a rendered markup document (`MarkupRender`) | string |
| 422 | APIValidationError is error format response related to input validation (`validationError`) |  |

## GET /api/v1/signing-key.gpg

operationId: `getSigningKey`

Get default signing-key.gpg

| Response | Description | Body |
|---|---|---|
| 200 | GPG armored public key | string |

## GET /api/v1/signing-key.pub

operationId: `getSigningKeySSH`

Get default signing-key.pub

| Response | Description | Body |
|---|---|---|
| 200 | ssh public key | string |

## GET /api/v1/token

operationId: `getCurrentToken`

Get the currently authenticated token

| Response | Description | Body |
|---|---|---|
| 200 | CurrentAccessToken represents the currently authenticated access token. (`CurrentAccessToken`) | `CurrentAccessToken` |

## DELETE /api/v1/token

operationId: `deleteCurrentToken`

Delete the currently authenticated token

| Response | Description | Body |
|---|---|---|
| 204 | token deleted |  |

## GET /api/v1/version

operationId: `getVersion`

Returns the version of the Gitea application

| Response | Description | Body |
|---|---|---|
| 200 | ServerVersion (`ServerVersion`) | `ServerVersion` |
