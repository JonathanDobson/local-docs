# Docker HUB API 2-beta — repositories

## GET /v2/namespaces/{namespace}/repositories/{repository}/tags

operationId: `ListRepositoryTags`

List repository tags

Returns the list of tags for the specified repository.

This operation accepts bearer tokens issued from organization access tokens (OATs). The token must have the required resource access and scopes.

| Parameter | In | Type | Required | Description |
|---|---|---|---|---|
| `namespace` | path | string | yes | Namespace of the repository, such as a user or organization name. |
| `repository` | path | string | yes | Name of the repository within the namespace. |
| `page` | query | integer |  | Page number (starts on 1). |
| `page_size` | query | integer |  | Number of items (rows) per page. |

| Response | Description | Body |
|---|---|---|
| 200 | list repository tags (`list_tags`) | `paginated_tags` |
| 403 | Forbidden (`Forbidden`) | `error` |
| 404 | Not Found (`NotFound`) | `error` |

## HEAD /v2/namespaces/{namespace}/repositories/{repository}/tags

operationId: `headV2NamespacesByNamespaceRepositoriesByRepositoryTags`

Check repository tags

Checks whether the repository has any tags.

This operation accepts bearer tokens issued from organization access tokens (OATs). The token must have the required resource access and scopes.

| Parameter | In | Type | Required | Description |
|---|---|---|---|---|
| `namespace` | path | string | yes | Namespace of the repository, such as a user or organization name. |
| `repository` | path | string | yes | Name of the repository within the namespace. |

| Response | Description | Body |
|---|---|---|
| 200 | Repository contains tags |  |
| 403 | Forbidden (`Forbidden`) | `error` |
| 404 | Not Found (`NotFound`) | `error` |

## GET /v2/namespaces/{namespace}/repositories/{repository}/tags/{tag}

operationId: `GetRepositoryTag`

Read repository tag

Returns details for a specific tag in the specified repository.

This operation accepts bearer tokens issued from organization access tokens (OATs). The token must have the required resource access and scopes.

| Parameter | In | Type | Required | Description |
|---|---|---|---|---|
| `namespace` | path | string | yes | Namespace of the repository, such as a user or organization name. |
| `repository` | path | string | yes | Name of the repository within the namespace. |
| `tag` | path | string | yes | Name of the image tag. |

| Response | Description | Body |
|---|---|---|
| 200 | repository tag (`get_tag`) | `tag` |
| 403 | Forbidden (`Forbidden`) | `error` |
| 404 | Not Found (`NotFound`) | `error` |

## HEAD /v2/namespaces/{namespace}/repositories/{repository}/tags/{tag}

operationId: `headV2NamespacesByNamespaceRepositoriesByRepositoryTagsByTag`

Check repository tag

Checks whether the specified tag exists in the repository.

This operation accepts bearer tokens issued from organization access tokens (OATs). The token must have the required resource access and scopes.

| Parameter | In | Type | Required | Description |
|---|---|---|---|---|
| `namespace` | path | string | yes | Namespace of the repository, such as a user or organization name. |
| `repository` | path | string | yes | Name of the repository within the namespace. |
| `tag` | path | string | yes | Name of the image tag. |

| Response | Description | Body |
|---|---|---|
| 200 | Repository tag exists |  |
| 403 | Forbidden (`Forbidden`) | `error` |
| 404 | Not Found (`NotFound`) | `error` |

## PATCH /v2/namespaces/{namespace}/repositories/{repository}/immutabletags

operationId: `UpdateRepositoryImmutableTags`

Update repository immutable tags

Updates the immutable tags configuration for this repository.

**Only users with administrative privileges for the repository can modify these settings.**

This operation accepts bearer tokens issued from organization access tokens (OATs). The token must have the required resource access and scopes.

| Parameter | In | Type | Required | Description |
|---|---|---|---|---|
| `namespace` | path | string | yes | Namespace of the repository, such as a user or organization name. |
| `repository` | path | string | yes | Name of the repository within the namespace. |

| Response | Description | Body |
|---|---|---|
| 200 |  (`update_repository_immutable_tags_response`) | `repository_info` |
| 400 | Bad Request (`bad_request`) | `error` |
| 401 | Unauthorized (`unauthorized`) | `error` |
| 403 | Forbidden (`forbidden`) | `error` |
| 404 | Not Found (`not_found`) | `error` |

## POST /v2/namespaces/{namespace}/repositories/{repository}/immutabletags/verify

operationId: `VerifyRepositoryImmutableTags`

Verify repository immutable tags

Validates the immutable tags regex passed in the request body and returns a list of tags matching it in this repository.

**Only users with administrative privileges for the repository can call this endpoint.**

This operation accepts bearer tokens issued from organization access tokens (OATs). The token must have the required resource access and scopes.

| Parameter | In | Type | Required | Description |
|---|---|---|---|---|
| `namespace` | path | string | yes | Namespace of the repository, such as a user or organization name. |
| `repository` | path | string | yes | Name of the repository within the namespace. |

| Response | Description | Body |
|---|---|---|
| 200 |  (`immutable_tags_verify_response`) | `immutable_tags_verify_response` |
| 400 | Bad Request (`bad_request`) | `error` |
| 401 | Unauthorized (`unauthorized`) | `error` |
| 403 | Forbidden (`forbidden`) | `error` |
| 404 | Not Found (`not_found`) | `error` |

## POST /v2/repositories/{namespace}/{repository}/groups

operationId: `CreateRepositoryGroup`

Assign a group (Team) to a repository for access

Assigns an organization group (team) to a repository with a specified permission level.

This operation accepts bearer tokens issued from organization access tokens (OATs). The token must have the required resource access and scopes.

| Parameter | In | Type | Required | Description |
|---|---|---|---|---|
| `namespace` | path | string | yes | Namespace of the repository, such as a user or organization name. |
| `repository` | path | string | yes | Name of the repository within the namespace. |

Request body (application/json): `RepositoryGroupCreationRequest`

| Response | Description | Body |
|---|---|---|
| 200 | Repository group permission created successfully | `RepositoryGroup` |
| 400 | Bad Request - Invalid request parameters | `error` |
| 401 | Unauthorized (`unauthorized`) | `error` |
| 403 | Forbidden (`forbidden`) | `error` |
| 404 | Not Found (`NotFound`) | `error` |

## GET /v2/namespaces/{namespace}/repositories

operationId: `listNamespaceRepositories`

List repositories in a namespace

Returns a list of repositories within the specified namespace (organization or user).

Public repositories are accessible to everyone, while private repositories require appropriate authentication and permissions.



**OAT listing behavior**: an OAT with the `scope-repository-list` scope sees all repositories including private ones. An OAT without that scope only sees public repositories. This filtering is silent: the response is a normal `200` with no indication that private repositories were withheld.

This operation accepts bearer tokens issued from organization access tokens (OATs). The token must have the required resource access and scopes.

| Parameter | In | Type | Required | Description |
|---|---|---|---|---|
| `namespace` | path | string | yes | Namespace of the repository, such as a user or organization name. |
| `page` | query | integer |  | Page number (starts on 1). |
| `page_size` | query | integer |  | Number of items (rows) per page. |
| `name` | query | string |  | Filter repositories by name (partial match). |
| `ordering` | query | string enum: name, -name, last_updated, -last_updated, pull_count, -pull_count |  | Order repositories by the specified field. Prefix with '-' for descending order. Available options: - `name` / `-name`: Repository name (ascending/descending) - `last_updated` / `-last_updated`: Last update time (ascending/descending) - `pull_count` / `-pull_count`: Number of pulls (ascending/descending) |

| Response | Description | Body |
|---|---|---|
| 200 | List of repositories | `list_repositories_response` |
| 400 | Bad Request - Invalid request parameters | `error` |
| 401 | Unauthorized (`unauthorized`) | `error` |
| 403 | Forbidden (`forbidden`) | `error` |
| 404 | Page not found - occurs when requesting a page number `>1` that exceeds the available results | `error` |

## POST /v2/namespaces/{namespace}/repositories

operationId: `CreateRepository`

Create a new repository

Creates a new repository within the specified namespace. The repository will be created
with the provided metadata including name, description, and privacy settings.

This operation accepts bearer tokens issued from organization access tokens (OATs). The token must have the required resource access and scopes.

| Parameter | In | Type | Required | Description |
|---|---|---|---|---|
| `namespace` | path | string | yes | Namespace of the repository, such as a user or organization name. |

Request body (application/json): `repo_creation_request`

| Response | Description | Body |
|---|---|---|
| 201 | Repository created successfully | `repository_info` |
| 400 | Bad Request (`bad_request`) | `error` |
| 401 | Unauthorized (`unauthorized`) | `error` |
| 403 | Forbidden (`forbidden`) | `error` |
| 404 | Not Found (`not_found`) | `error` |
| 500 | Internal (`internal_error`) | `error` |

## GET /v2/namespaces/{namespace}/repositories/{repository}

operationId: `GetRepository`

Get repository in a namespace

Returns a repository within the specified namespace (organization or user).

Public repositories are accessible to everyone, while private repositories require appropriate authentication and permissions.

This operation accepts bearer tokens issued from organization access tokens (OATs). The token must have the required resource access and scopes.

| Parameter | In | Type | Required | Description |
|---|---|---|---|---|
| `namespace` | path | string | yes | Namespace of the repository, such as a user or organization name. |
| `repository` | path | string | yes | Name of the repository within the namespace. |

| Response | Description | Body |
|---|---|---|
| 200 |  | `repository_info` |
| 401 | Unauthorized (`unauthorized`) | `error` |
| 403 | Forbidden (`forbidden`) | `error` |
| 404 | Not Found (`not_found`) | `error` |
| 500 | Internal (`internal_error`) | `error` |

## HEAD /v2/namespaces/{namespace}/repositories/{repository}

operationId: `CheckRepository`

Check repository in a namespace

Check a repository within the specified namespace (organization or user).

Public repositories are accessible to everyone, while private repositories require appropriate authentication and permissions.

This operation accepts bearer tokens issued from organization access tokens (OATs). The token must have the required resource access and scopes.

| Parameter | In | Type | Required | Description |
|---|---|---|---|---|
| `namespace` | path | string | yes | Namespace of the repository, such as a user or organization name. |
| `repository` | path | string | yes | Name of the repository within the namespace. |

| Response | Description | Body |
|---|---|---|
| 200 |  |  |
| 401 | Unauthorized (`unauthorized`) | `error` |
| 403 | Forbidden (`forbidden`) | `error` |
| 404 | Not Found (`not_found`) | `error` |
| 500 | Internal (`internal_error`) | `error` |
