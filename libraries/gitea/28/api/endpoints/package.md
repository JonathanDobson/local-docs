# Gitea API 28.3.0 — package

## GET /api/v1/packages/{owner}

operationId: `listPackages`

Gets all packages of an owner

| Parameter | In | Type | Required | Description |
|---|---|---|---|---|
| `owner` | path | string | yes | owner of the packages |
| `page` | query | integer |  | page number of results to return (1-based) |
| `limit` | query | integer |  | page size of results |
| `type` | query | string enum: alpine, cargo, chef, composer, conan, conda, container, cran, debian, generic, go, helm |  | package type filter |
| `q` | query | string |  | name filter |

| Response | Description | Body |
|---|---|---|
| 200 | PackageList (`PackageList`) | array of `Package` |
| 404 | APINotFound is a not found empty response (`notFound`) |  |

## GET /api/v1/packages/{owner}/{type}/{name}

operationId: `listPackageVersions`

Gets all versions of a package

| Parameter | In | Type | Required | Description |
|---|---|---|---|---|
| `owner` | path | string | yes | owner of the package |
| `type` | path | string | yes | type of the package |
| `name` | path | string | yes | name of the package |
| `page` | query | integer |  | page number of results to return (1-based) |
| `limit` | query | integer |  | page size of results |

| Response | Description | Body |
|---|---|---|
| 200 | PackageList (`PackageList`) | array of `Package` |
| 404 | APINotFound is a not found empty response (`notFound`) |  |

## DELETE /api/v1/packages/{owner}/{type}/{name}

operationId: `deletePackage`

Delete a package

| Parameter | In | Type | Required | Description |
|---|---|---|---|---|
| `owner` | path | string | yes | owner of the package |
| `type` | path | string | yes | type of the package |
| `name` | path | string | yes | name of the package |

| Response | Description | Body |
|---|---|---|
| 204 | APIEmpty is an empty response (`empty`) |  |
| 404 | APINotFound is a not found empty response (`notFound`) |  |

## GET /api/v1/packages/{owner}/{type}/{name}/-/latest

operationId: `getLatestPackageVersion`

Gets the latest version of a package

| Parameter | In | Type | Required | Description |
|---|---|---|---|---|
| `owner` | path | string | yes | owner of the package |
| `type` | path | string | yes | type of the package |
| `name` | path | string | yes | name of the package |

| Response | Description | Body |
|---|---|---|
| 200 | Package (`Package`) | `Package` |
| 404 | APINotFound is a not found empty response (`notFound`) |  |

## POST /api/v1/packages/{owner}/{type}/{name}/-/link/{repo_name}

operationId: `linkPackage`

Link a package to a repository

| Parameter | In | Type | Required | Description |
|---|---|---|---|---|
| `owner` | path | string | yes | owner of the package |
| `type` | path | string | yes | type of the package |
| `name` | path | string | yes | name of the package |
| `repo_name` | path | string | yes | name of the repository to link. |

| Response | Description | Body |
|---|---|---|
| 201 | APIEmpty is an empty response (`empty`) |  |
| 404 | APINotFound is a not found empty response (`notFound`) |  |

## POST /api/v1/packages/{owner}/{type}/{name}/-/unlink

operationId: `unlinkPackage`

Unlink a package from a repository

| Parameter | In | Type | Required | Description |
|---|---|---|---|---|
| `owner` | path | string | yes | owner of the package |
| `type` | path | string | yes | type of the package |
| `name` | path | string | yes | name of the package |

| Response | Description | Body |
|---|---|---|
| 201 | APIEmpty is an empty response (`empty`) |  |
| 404 | APINotFound is a not found empty response (`notFound`) |  |

## GET /api/v1/packages/{owner}/{type}/{name}/{version}

operationId: `getPackage`

Gets a package

| Parameter | In | Type | Required | Description |
|---|---|---|---|---|
| `owner` | path | string | yes | owner of the package |
| `type` | path | string | yes | type of the package |
| `name` | path | string | yes | name of the package |
| `version` | path | string | yes | version of the package |

| Response | Description | Body |
|---|---|---|
| 200 | Package (`Package`) | `Package` |
| 404 | APINotFound is a not found empty response (`notFound`) |  |

## DELETE /api/v1/packages/{owner}/{type}/{name}/{version}

operationId: `deletePackageVersion`

Delete a package version

| Parameter | In | Type | Required | Description |
|---|---|---|---|---|
| `owner` | path | string | yes | owner of the package |
| `type` | path | string | yes | type of the package |
| `name` | path | string | yes | name of the package |
| `version` | path | string | yes | version of the package |

| Response | Description | Body |
|---|---|---|
| 204 | APIEmpty is an empty response (`empty`) |  |
| 404 | APINotFound is a not found empty response (`notFound`) |  |

## GET /api/v1/packages/{owner}/{type}/{name}/{version}/files

operationId: `listPackageFiles`

Gets all files of a package

| Parameter | In | Type | Required | Description |
|---|---|---|---|---|
| `owner` | path | string | yes | owner of the package |
| `type` | path | string | yes | type of the package |
| `name` | path | string | yes | name of the package |
| `version` | path | string | yes | version of the package |

| Response | Description | Body |
|---|---|---|
| 200 | PackageFileList (`PackageFileList`) | array of `PackageFile` |
| 404 | APINotFound is a not found empty response (`notFound`) |  |
