# DVP Data API 1.0.0 — schemas

## DatasetModel

Datasets and views available to the publisher, based on its entitlements.

| Field | Type | Required | Description |
|---|---|---|---|
| `name` | `DatasetType` |  |  |
| `views` | array of `DataviewType` |  |  |
| `timespans` | array of `TimespanType` |  |  |

## DatasetType

Type: string enum: pulls, extensions

## DataviewType

Type: string enum: raw, summary, repo-summary, namespace-summary, geo-repo-summary, ext-summary, ext-premium-summary, ext-premium-geo

## GroupType

Type: string enum: repo, namespace

## MonthData

| Field | Type | Required | Description |
|---|---|---|---|
| `months` | array of `MonthModel` | yes |  |

## MonthModel

| Field | Type | Required | Description |
|---|---|---|---|
| `month` | integer | yes |  |

## NamespaceData

| Field | Type | Required | Description |
|---|---|---|---|
| `namespaces` | array of string |  |  |

## NamespaceMetadata

| Field | Type | Required | Description |
|---|---|---|---|
| `namespace` | string |  |  |
| `extraRepos` | ['array', 'null'] |  | Additional repositories associated with the namespace. Null when none are configured. |
| `datasets` | array of `DatasetModel` |  |  |
| `publisherType` | string |  | Publisher program associated with the namespace. |
| `extensionPublisher` | boolean |  | Whether the namespace is an extension publisher. |

## PeriodType

Type: string enum: last-2-months, last-3-months, last-6-months, last-12-months

## PostUsers2FALoginErrorResponse

failed second factor login response.

| Field | Type | Required | Description |
|---|---|---|---|
| `detail` | string |  | Description of the error. |

## PostUsersLoginErrorResponse

failed user login response or second factor required

| Field | Type | Required | Description |
|---|---|---|---|
| `detail` | string | yes | Description of the error. |
| `login_2fa_token` | ['string', 'null'] |  | Short-lived token to be used on `/v2/users/2fa-login` to complete the authentication. This field is present only if 2FA is enabled. |

## PostUsersLoginSuccessResponse

successful user login response

| Field | Type | Required | Description |
|---|---|---|---|
| `token` | string |  | Created authentication token. This token can be used in the HTTP Authorization header as a JWT to authenticate with the Docker Hub APIs. |

## PullData

| Field | Type | Required | Description |
|---|---|---|---|
| `pulls` | ['array', 'null'] |  | Pull statistics for the selected interval. Null when no records are returned. |

## PullModel

| Field | Type | Required | Description |
|---|---|---|---|
| `start` | string (date-time) |  | Start of the reporting interval in RFC 3339 format. |
| `end` | string (date-time) |  | End of the reporting interval in RFC 3339 format. |
| `repo` | string |  | Repository name. Present for results grouped by repository. |
| `namespace` | string |  | Namespace name. Present for results grouped by namespace. |
| `pullCount` | integer |  |  |
| `ipCount` | integer |  |  |
| `country` | string |  | Country. Present for results grouped by geography and repository. |

## ReposPullData

| Field | Type | Required | Description |
|---|---|---|---|
| `repos` | object |  |  |

## ResponseData

Download locations for the selected export. Large exports can span multiple files.

| Field | Type | Required | Description |
|---|---|---|---|
| `data` | array of `ResponseDataFile` |  | Download URLs and file sizes for the export. |

## ResponseDataFile

| Field | Type | Required | Description |
|---|---|---|---|
| `url` | string (uri) |  | Signed download URL. URLs expire six hours after generation. |
| `size` | integer (int64) |  | Size of the file in bytes. |

## TimespanData

Type: oneOf(`MonthData`, `WeekData`)

## TimespanModel

Type: oneOf(`MonthModel`, `WeekModel`)

## TimespanType

Type: string enum: months, weeks

## Users2FALoginRequest

Second factor user login details

| Field | Type | Required | Description |
|---|---|---|---|
| `login_2fa_token` | string | yes | The intermediate 2FA token returned from `/v2/users/login` API. |
| `code` | string | yes | The Time-based One-Time Password of the Docker Hub account to authenticate with. |

## UsersLoginRequest

User login details

| Field | Type | Required | Description |
|---|---|---|---|
| `username` | string | yes | The username of the Docker Hub account to authenticate with. |
| `password` | string | yes | The password or personal access token (PAT) of the Docker Hub account to authenticate with. |

## WeekData

| Field | Type | Required | Description |
|---|---|---|---|
| `weeks` | array of `WeekModel` | yes |  |

## WeekModel

| Field | Type | Required | Description |
|---|---|---|---|
| `week` | integer | yes |  |

## YearData

| Field | Type | Required | Description |
|---|---|---|---|
| `years` | array of `YearModel` |  |  |

## YearModel

| Field | Type | Required | Description |
|---|---|---|---|
| `year` | integer |  |  |

