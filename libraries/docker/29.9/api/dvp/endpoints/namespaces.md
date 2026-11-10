# DVP Data API 1.0.0 — namespaces

## GET /api/publisher/analytics/v1/namespaces/{namespace}/pulls

operationId: `getNamespacePulls`

Get pull data

Gets pulls for the given namespace.

| Parameter | In | Type | Required | Description |
|---|---|---|---|---|
| `namespace` | path | string | yes | Namespace to fetch data for |
| `timespan` | query | `TimespanType` |  | Timespan type for fetching data |
| `period` | query | `PeriodType` |  | Relative period of the period to fetch data |
| `group` | query | `GroupType` |  | Field to group the data by |

| Response | Description | Body |
|---|---|---|
| 200 | Success | `PullData` |
| 404 | Not found - namespace doesn't exist or user does not have permission to access it |  |

## GET /api/publisher/analytics/v1/namespaces/{namespace}/repos/{repo}/pulls

operationId: `getRepoPulls`

Get pull data

Gets pulls for the given repo.

| Parameter | In | Type | Required | Description |
|---|---|---|---|---|
| `namespace` | path | string | yes | Namespace to fetch data for |
| `repo` | path | string | yes | Repository to fetch data for |
| `timespan` | query | `TimespanType` |  | Timespan type for fetching data |
| `period` | query | `PeriodType` |  | Relative period of the period to fetch data |
| `group` | query | `GroupType` |  | Field to group the data by |

| Response | Description | Body |
|---|---|---|
| 200 | Success | `PullData` |
| 404 | Not found - repo doesn't exist or user does not have permission to access it |  |

## GET /api/publisher/analytics/v1/namespaces/{namespace}/pulls/exports/years

operationId: `getNamespaceYears`

Get years with data

Gets a list of years that have data for the given namespace.

| Parameter | In | Type | Required | Description |
|---|---|---|---|---|
| `namespace` | path | string | yes | Namespace to fetch data for |

| Response | Description | Body |
|---|---|---|
| 200 | Success | `YearData` |

## GET /api/publisher/analytics/v1/namespaces/{namespace}/pulls/exports/years/{year}/{timespantype}

operationId: `getNamespaceTimespans`

Get timespans with data

Gets a list of timespans of the given type that have data for the given namespace and year.

| Parameter | In | Type | Required | Description |
|---|---|---|---|---|
| `namespace` | path | string | yes | Namespace to fetch data for |
| `year` | path | integer | yes | Year to fetch data for |
| `timespantype` | path | `TimespanType` | yes | Type of timespan to fetch data for |

| Response | Description | Body |
|---|---|---|
| 200 | Success | `TimespanData` |

## GET /api/publisher/analytics/v1/namespaces/{namespace}/pulls/exports/years/{year}/{timespantype}/{timespan}

operationId: `getNamespaceTimespanMetadata`

Get namespace metadata for timespan

Gets info about data for the given namespace and timespan.

| Parameter | In | Type | Required | Description |
|---|---|---|---|---|
| `namespace` | path | string | yes | Namespace to fetch data for |
| `year` | path | integer | yes | Year to fetch data for |
| `timespantype` | path | `TimespanType` | yes | Type of timespan to fetch data for |
| `timespan` | path | integer | yes | Timespan to fetch data for |

| Response | Description | Body |
|---|---|---|
| 200 | Success | `TimespanModel` |
| 404 | Not Found |  |

## GET /api/publisher/analytics/v1/namespaces/{namespace}/pulls/exports/years/{year}/{timespantype}/{timespan}/{dataview}

operationId: `getNamespaceDataByTimespan`

Get namespace data for timespan

Gets a list of URLs that can be used to download the pull data for the given namespace and timespan.

| Parameter | In | Type | Required | Description |
|---|---|---|---|---|
| `namespace` | path | string | yes | Namespace to fetch data for |
| `year` | path | integer | yes | Year to fetch data for |
| `timespantype` | path | `TimespanType` | yes | Type of timespan to fetch data for |
| `timespan` | path | integer | yes | Timespan to fetch data for |
| `dataview` | path | `DataviewType` | yes | Type of data to fetch |

| Response | Description | Body |
|---|---|---|
| 200 | Success | `ResponseData` |

## GET /api/publisher/analytics/v1/repos/pulls

operationId: `getManyReposPulls`

Get pull data for multiple repos

Gets pull for the given repos.

| Parameter | In | Type | Required | Description |
|---|---|---|---|---|
| `repos` | query | array of string | yes | Repositories to fetch data for (maximum of 50 repositories per request). |
| `timespan` | query | `TimespanType` |  | Timespan type for fetching data |
| `period` | query | `PeriodType` |  | Relative period of the period to fetch data |
| `group` | query | `GroupType` |  | Field to group the data by |

| Response | Description | Body |
|---|---|---|
| 200 | Success | `ReposPullData` |
