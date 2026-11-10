# Docker HUB API 2-beta — schemas

## AuditLog

Audit log event.

| Field | Type | Required | Description |
|---|---|---|---|
| `account` | string |  |  |
| `action` | string |  |  |
| `name` | string |  |  |
| `actor` | string |  |  |
| `data` | object |  |  |
| `timestamp` | string (date-time) |  |  |
| `action_description` | string |  |  |

## AuditLogAction

Audit Log action

| Field | Type | Required | Description |
|---|---|---|---|
| `name` | string |  | Name of audit log action. |
| `description` | string |  | Description of audit log action. |
| `label` | string |  | Label for audit log action. |

## AuditLogActions

| Field | Type | Required | Description |
|---|---|---|---|
| `actions` | array of `AuditLogAction` |  | List of audit log actions. |
| `label` | string |  | Grouping label for a particular set of audit log actions. |

## AuthCreateTokenResponse

successful access token response

| Field | Type | Required | Description |
|---|---|---|---|
| `access_token` | string |  | The created access token. This expires in 10 minutes. |

## GetAuditActionsResponse

GetAuditActions response.

| Field | Type | Required | Description |
|---|---|---|---|
| `actions` | object |  | Map of audit log actions. |

## GetAuditLogsResponse

GetAuditLogs response.

| Field | Type | Required | Description |
|---|---|---|---|
| `logs` | array of `AuditLog` |  | List of audit log events. |

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
| `login_2fa_token` | ['string', 'null'] |  | Short time lived token to be used on `/v2/users/2fa-login` to complete the authentication. This field is present only if 2FA is enabled. |

## PostUsersLoginSuccessResponse

successful user login response

| Field | Type | Required | Description |
|---|---|---|---|
| `token` | string |  | Created authentication token. This token can be used in the HTTP Authorization header as a JWT to authenticate with the Docker Hub APIs. |

## RepositoryGroup

| Field | Type | Required | Description |
|---|---|---|---|
| `group_name` | string |  | The name of the group |
| `permission` | string enum: read, write, admin |  | The permission level granted to the group |
| `group_id` | integer (int64) |  | The ID of the group |

## RepositoryGroupCreationRequest

| Field | Type | Required | Description |
|---|---|---|---|
| `group_id` | integer (int64) | yes | The ID of the organization group to grant access to |
| `permission` | string enum: read, write, admin | yes | The permission level to grant to the group: - read: Can view and pull from the repository - write: Can view, pull, and push to the repository - admin: Can view, pull, push, and manage repository settings |

## Users2FALoginRequest

Second factor user login details

| Field | Type | Required | Description |
|---|---|---|---|
| `login_2fa_token` | string | yes | The intermediate 2FA token returned from `/v2/auth/token` API. |
| `code` | string | yes | The Time-based One-Time Password of the Docker Hub account to authenticate with. |

## UsersLoginRequest

User login details

| Field | Type | Required | Description |
|---|---|---|---|
| `username` | string | yes | The username of the Docker Hub account to authenticate with. |
| `password` | string | yes | The password or personal access token (PAT) of the Docker Hub account to authenticate with. |

## accessToken

| Field | Type | Required | Description |
|---|---|---|---|
| `uuid` | string |  |  |
| `client_id` | string |  |  |
| `creator_ip` | string |  |  |
| `creator_ua` | string |  |  |
| `created_at` | string |  |  |
| `last_used` | ['string', 'null'] |  |  |
| `generated_by` | string |  |  |
| `is_active` | boolean |  |  |
| `token` | string |  | Token value returned on creation. Later responses redact the value as ***. |
| `token_label` | string |  |  |
| `scopes` | array of string |  |  |
| `expires_at` | ['string', 'null', ' ', '(', 'd', 'a', 't', 'e', '-', 't', 'i', 'm', 'e', ')'] |  |  |

## bulk_invite

| Field | Type | Required | Description |
|---|---|---|---|
| `invitees` | array of object |  | A list of invitees |

## category

Repository category for classification and discovery

| Field | Type | Required | Description |
|---|---|---|---|
| `name` | string | yes | Human-readable name of the category |
| `slug` | string | yes | URL-friendly identifier for the category |

## createAccessTokenRequest

| Field | Type | Required | Description |
|---|---|---|---|
| `token_label` | string | yes | Friendly name for you to identify the token. |
| `scopes` | array of string | yes | Valid scopes: "repo:admin", "repo:write", "repo:read", "repo:public_read", "sandbox:use". Include one repository scope, "sandbox:use", or both. |
| `expires_at` | string (date-time) |  | Optional expiration date for the token. If omitted, the token will remain valid indefinitely. |

## createAccessTokensResponse

Type: `accessToken`

## createOrgAccessTokenRequest

| Field | Type | Required | Description |
|---|---|---|---|
| `label` | string | yes | Label for the access token |
| `description` | string |  | Description of the access token |
| `resources` | array of `orgAccessTokenResource` | yes | Resources this token has access to |
| `expires_at` | ['string', 'null', ' ', '(', 'd', 'a', 't', 'e', '-', 't', 'i', 'm', 'e', ')'] |  | Expiration date for the token |

## createOrgAccessTokenResponse

Type: allOf(object, object)

## email_address

| Field | Type | Required | Description |
|---|---|---|---|
| `id` | number |  |  |
| `user_id` | number |  |  |
| `email` | string |  |  |
| `verified` | boolean |  |  |
| `primary` | boolean |  |  |

## email_with_username

Type: allOf(`email_address`, object)

## error

Error details vary by endpoint. The message describes the failure; errinfo can contain additional context.

| Field | Type | Required | Description |
|---|---|---|---|
| `errinfo` | ['object', 'null'] |  | Additional error context, when available. |
| `detail` | string |  |  |
| `message` | string |  |  |

## getAccessTokensResponse

| Field | Type | Required | Description |
|---|---|---|---|
| `count` | number |  |  |
| `next` | ['string', 'null'] |  |  |
| `previous` | ['string', 'null'] |  |  |
| `active_count` | number |  |  |
| `results` | array of allOf(`accessToken`, object) |  |  |

## getOrgAccessTokenResponse

Type: allOf(`orgAccessToken`, object)

## getOrgAccessTokensResponse

| Field | Type | Required | Description |
|---|---|---|---|
| `total` | number |  |  |
| `next` | ['string', 'null'] |  |  |
| `previous` | ['string', 'null'] |  |  |
| `results` | array of `orgAccessToken` |  |  |

## group_member

| Field | Type | Required | Description |
|---|---|---|---|
| `id` | string |  | The UUID trimmed |
| `company` | string |  |  |
| `date_joined` | string (date-time) |  |  |
| `full_name` | string |  |  |
| `gravatar_email` | string |  |  |
| `gravatar_url` | string |  |  |
| `location` | string |  |  |
| `profile_url` | string |  |  |
| `type` | string enum: User, Org |  |  |
| `username` | string |  |  |
| `email` | string |  |  |

## image

| Field | Type | Required | Description |
|---|---|---|---|
| `architecture` | string |  | CPU architecture |
| `features` | ['string', 'null'] |  | CPU features |
| `variant` | ['string', 'null'] |  | CPU variant |
| `digest` | ['string', 'null'] |  | image digest |
| `layers` | array of `layer` |  |  |
| `os` | string |  | operating system |
| `os_features` | ['string', 'null'] |  | OS features |
| `os_version` | ['string', 'null'] |  | OS version |
| `size` | integer |  | size of the image |
| `status` | string enum: active, inactive |  | Status of the image |
| `last_pulled` | ['string', 'null'] |  | datetime of last pull |
| `last_pushed` | ['string', 'null'] |  | datetime of last push |

## immutable_tags_settings

| Field | Type | Required | Description |
|---|---|---|---|
| `enabled` | boolean | yes | Whether immutable tags are enabled |
| `rules` | array of string | yes | List of immutable tag rules |

## immutable_tags_verify_request

| Field | Type | Required | Description |
|---|---|---|---|
| `regex` | string | yes | Regular expression using Go regular expression syntax. Commas are not permitted. |

## immutable_tags_verify_response

| Field | Type | Required | Description |
|---|---|---|---|
| `tags` | array of string | yes | List of tags that match the provided regex pattern |

## invite

| Field | Type | Required | Description |
|---|---|---|---|
| `id` | string |  | uuid representing the invite id |
| `inviter_username` | string |  |  |
| `invitee` | string |  | can either be a dockerID for registered users or an email for non-registered users |
| `org` | string |  | name of the org to join |
| `team` | string |  | name of the team (user group) to join |
| `created_at` | string |  |  |

## layer

| Field | Type | Required | Description |
|---|---|---|---|
| `digest` | ['string', 'null'] |  | image layer digest |
| `size` | integer |  | size of the layer |
| `instruction` | string |  | Dockerfile instruction |

## legacy_email_address

Type: allOf(`email_address`, object)

## list_repositories_response

Type: allOf(`page`, object)

## orgAccessToken

| Field | Type | Required | Description |
|---|---|---|---|
| `id` | string |  |  |
| `label` | string |  |  |
| `created_by` | string |  |  |
| `is_active` | boolean |  |  |
| `created_at` | string (date-time) |  |  |
| `expires_at` | ['string', 'null', ' ', '(', 'd', 'a', 't', 'e', '-', 't', 'i', 'm', 'e', ')'] |  |  |
| `last_used_at` | ['string', 'null', ' ', '(', 'd', 'a', 't', 'e', '-', 't', 'i', 'm', 'e', ')'] |  |  |

## orgAccessTokenResource

| Field | Type | Required | Description |
|---|---|---|---|
| `type` | string enum: TYPE_REPO, TYPE_ORG | yes | The type of resource |
| `path` | string | yes | The path of the resource. The format of this will change depending on the type of resource. For TYPE_REPO resources: - Must be an existing repository name (e.g., "myorg/myrepo") - Can use glob patterns (e.g., "myorg/*" for all repositories in the organization) - Use "*/*/public" to reference all public repositories |
| `scopes` | array of string | yes | The scopes this token has access to |

## orgSettings

| Field | Type | Required | Description |
|---|---|---|---|
| `restricted_images` | `restricted_images` |  |  |

## org_group

| Field | Type | Required | Description |
|---|---|---|---|
| `id` | number |  | Group ID |
| `uuid` | string |  | UUID for the group |
| `name` | string |  | Name of the group |
| `description` | string |  | Description of the group |
| `member_count` | number |  | Member count of the group |
| `role` | ['string', 'null'] |  | Role assigned to the team. A core role (`owner`, `editor`, or `member`) or the name of a custom role (not the label or UUID). |

## org_member

| Field | Type | Required | Description |
|---|---|---|---|
| `email` | string |  | User's email address |
| `role` | string enum: Owner, Editor, Member, Invitee |  | The member's role in the organization (`Owner`, `Editor`, `Member`, or `Invitee` for pending invites). |
| `groups` | array of string |  | Groups (Teams) that the user is member of |
| `is_guest` | boolean |  | If the organization has verified domains, members that have email addresses outside of those domains will be flagged as guests. |
| `primary_email` | string |  | The user's email primary address. |
| `last_logged_in_at` | ['string', 'null', ' ', '(', 'd', 'a', 't', 'e', '-', 't', 'i', 'm', 'e', ')'] |  | Last time the user logged in. To access this field, you must have insights visible for your organization. See [Insights](https://docs.docker.com/accounts/organization/insights/#view-insights-for-organization-users). |
| `last_seen_at` | ['string', 'null', ' ', '(', 'd', 'a', 't', 'e', '-', 't', 'i', 'm', 'e', ')'] |  | Last time the user was seen. To access this field, you must have insights visible for your organization. See [Insights](https://docs.docker.com/accounts/organization/insights/#view-insights-for-organization-users). |
| `last_desktop_version` | string |  | Last desktop version the user used. To access this field, you must have insights visible for your organization. See [Insights](https://docs.docker.com/accounts/organization/insights/#view-insights-for-organization-users). |

## org_member_paginated

| Field | Type | Required | Description |
|---|---|---|---|
| `count` | number |  | The total number of items that match with the search. |
| `previous` | ['string', 'null'] |  | The URL or link for the previous page of items. |
| `next` | ['string', 'null'] |  | The URL or link for the next page of items. |
| `results` | array of `org_member` |  | List of accounts. |

## page

| Field | Type | Required | Description |
|---|---|---|---|
| `count` | integer |  | total number of results available across all pages |
| `next` | ['string', 'null'] |  | link to next page of results if any |
| `previous` | ['string', 'null'] |  | link to previous page of results if any |

## paginated_tags

Type: allOf(`page`, object)

## patchAccessTokenRequest

| Field | Type | Required | Description |
|---|---|---|---|
| `token_label` | string |  |  |
| `is_active` | boolean |  |  |

## patchAccessTokenResponse

Type: `accessToken`

## repo_creation_request

| Field | Type | Required | Description |
|---|---|---|---|
| `name` | string | yes | The name of the repository. Must be 2-255 characters long and may only include alphanumeric characters, periods (.), underscores (_), or hyphens (-). Letters must be lowercase. |
| `namespace` | string | yes | The namespace where the repository will be created |
| `description` | string |  | Short description of the repository |
| `full_description` | string |  | Detailed description of the repository |
| `registry` | string |  | The registry where the repository will be hosted |
| `is_private` | boolean |  | Whether the repository should be private |

## repo_permissions

| Field | Type | Required | Description |
|---|---|---|---|
| `read` | boolean | yes | Read permission |
| `write` | boolean | yes | Write permission |
| `admin` | boolean | yes | Admin permission |

## repository_info

| Field | Type | Required | Description |
|---|---|---|---|
| `user` | string | yes | Username of the repository owner |
| `name` | string | yes | Repository name |
| `namespace` | string | yes | Repository namespace |
| `repository_type` | ['string', 'null'] |  | Type of the repository |
| `status` | integer | yes | Repository status code |
| `status_description` | string | yes | Description of the repository status |
| `description` | string | yes | Short description of the repository |
| `is_private` | boolean | yes | Whether the repository is private |
| `is_automated` | boolean | yes | Whether the repository has automated builds |
| `star_count` | integer (int64) | yes | Number of stars |
| `pull_count` | integer (int64) | yes | Number of pulls |
| `last_updated` | string (date-time) | yes | ISO 8601 timestamp of when repository was last updated |
| `last_modified` | ['string', 'null', ' ', '(', 'd', 'a', 't', 'e', '-', 't', 'i', 'm', 'e', ')'] |  | ISO 8601 timestamp of when repository was last modified |
| `date_registered` | string (date-time) | yes | ISO 8601 timestamp of when repository was created |
| `collaborator_count` | integer (int64) | yes | Number of collaborators |
| `affiliation` | ['string', 'null'] |  | Repository affiliation |
| `hub_user` | ['string', 'null'] |  | Hub user information |
| `has_starred` | boolean | yes | Whether the current user has starred this repository |
| `full_description` | ['string', 'null'] |  | Full description of the repository |
| `permissions` | `repo_permissions` | yes |  |
| `media_types` | array of ['string', 'null'] | yes | Supported media types |
| `content_types` | array of string | yes | Supported content types |
| `categories` | array of `category` | yes | Repository categories |
| `immutable_tags_settings` | `immutable_tags_settings` | yes |  |
| `storage_size` | ['integer', 'null', ' ', '(', 'i', 'n', 't', '6', '4', ')'] |  | Storage size in bytes |
| `source` | ['string', 'null'] |  | Source of the repository, where it was created from |

## repository_list_entry

| Field | Type | Required | Description |
|---|---|---|---|
| `name` | string |  | Name of the repository |
| `namespace` | string |  | Namespace (organization or username) that owns the repository |
| `repository_type` | ['string', 'null', ' ', 'e', 'n', 'u', 'm', ':', ' ', 'i', 'm', 'a', 'g', 'e', ',', ' ', 'p', 'l', 'u', 'g', 'i', 'n', ',', ' ', 'N', 'o', 'n', 'e'] |  | Type of repository |
| `status` | integer |  | Repository status code |
| `status_description` | string enum: active, inactive |  | Human-readable repository status |
| `description` | ['string', 'null'] |  | Repository description |
| `is_private` | boolean |  | Whether the repository is private |
| `star_count` | integer |  | Number of users who starred this repository |
| `pull_count` | integer |  | Total number of pulls for this repository |
| `last_updated` | ['string', 'null', ' ', '(', 'd', 'a', 't', 'e', '-', 't', 'i', 'm', 'e', ')'] |  | ISO 8601 timestamp of when the repository was last updated |
| `last_modified` | ['string', 'null', ' ', '(', 'd', 'a', 't', 'e', '-', 't', 'i', 'm', 'e', ')'] |  | ISO 8601 timestamp of when the repository was last modified |
| `date_registered` | string (date-time) |  | ISO 8601 timestamp of when the repository was created |
| `affiliation` | string |  | User's affiliation with the repository (empty string if no affiliation) |
| `media_types` | array of string |  | Media types supported by this repository |
| `content_types` | array of string |  | Content types supported by this repository |
| `categories` | array of `category` |  | Categories associated with this repository |
| `storage_size` | integer |  | Storage size in bytes used by this repository |

## restricted_images

| Field | Type | Required | Description |
|---|---|---|---|
| `enabled` | boolean |  | Whether or not to restrict image usage for users in the organization. |
| `allow_official_images` | boolean |  | Allow usage of official images if "enabled" is `true`. |
| `allow_verified_publishers` | boolean |  | Allow usage of verified publisher images if "enabled" is `true`. |

## scim_email

| Field | Type | Required | Description |
|---|---|---|---|
| `value` | string |  |  |
| `display` | string |  |  |
| `primary` | boolean |  |  |

## scim_error

| Field | Type | Required | Description |
|---|---|---|---|
| `status` | string |  | The status code for the response in string format. |
| `schemas` | array of string |  |  |
| `detail` | string |  | Details about why the request failed. |

## scim_group

| Field | Type | Required | Description |
|---|---|---|---|
| `value` | string |  |  |
| `display` | string |  |  |

## scim_resource_type

| Field | Type | Required | Description |
|---|---|---|---|
| `schemas` | array of string |  |  |
| `id` | string |  |  |
| `name` | string |  |  |
| `description` | string |  |  |
| `endpoint` | string |  |  |
| `schema` | string |  |  |

## scim_schema

| Field | Type | Required | Description |
|---|---|---|---|
| `schemas` | array of string |  |  |
| `id` | string |  |  |
| `name` | string |  |  |
| `description` | string |  |  |
| `attributes` | array of `scim_schema_parent_attribute` |  |  |

## scim_schema_attribute

| Field | Type | Required | Description |
|---|---|---|---|
| `name` | string |  |  |
| `type` | string enum: string, boolean, complex |  |  |
| `multiValued` | boolean |  |  |
| `description` | string |  |  |
| `required` | boolean |  |  |
| `caseExact` | boolean |  |  |
| `mutability` | string |  |  |
| `returned` | string |  |  |
| `uniqueness` | string |  |  |

## scim_schema_parent_attribute

Type: allOf(`scim_schema_attribute`, object)

## scim_service_provider_config

| Field | Type | Required | Description |
|---|---|---|---|
| `schemas` | array of string |  |  |
| `documentationUri` | string |  |  |
| `patch` | object |  |  |
| `bulk` | object |  |  |
| `filter` | object |  |  |
| `changePassword` | object |  |  |
| `sort` | object |  |  |
| `etag` | object |  |  |
| `authenticationSchemes` | array of object |  |  |

## scim_user

| Field | Type | Required | Description |
|---|---|---|---|
| `schemas` | `scim_user_schemas` |  |  |
| `id` | `scim_user_id` |  |  |
| `userName` | `scim_user_username` |  |  |
| `name` | `scim_user_name` |  |  |
| `displayName` | `scim_user_display_name` |  |  |
| `active` | boolean |  |  |
| `emails` | array of `scim_email` |  |  |
| `groups` | array of `scim_group` |  |  |
| `meta` | object |  |  |

## scim_user_display_name

The username in Docker. Also known as the "Docker ID".

Type: string

## scim_user_id

The unique identifier for the user. A v4 UUID.

Type: string

## scim_user_name

| Field | Type | Required | Description |
|---|---|---|---|
| `givenName` | string |  |  |
| `familyName` | string |  |  |

## scim_user_schemas

Type: array of string

## scim_user_username

The user's email address. This must be reachable via email.

Type: string

## tag

| Field | Type | Required | Description |
|---|---|---|---|
| `id` | integer |  | tag ID |
| `images` | ['array', 'null'] |  |  |
| `creator` | integer |  | ID of the user that pushed the tag |
| `last_updated` | ['string', 'null'] |  | datetime of last update |
| `last_updater` | integer |  | ID of the last user that updated the tag |
| `last_updater_username` | string |  | Hub username of the user that updated the tag |
| `name` | string |  | name of the tag |
| `repository` | integer |  | repository ID |
| `full_size` | integer |  | compressed size (sum of all layers) of the tagged image |
| `v2` | boolean |  | Whether the tag uses the Registry V2 format. |
| `tag_last_pulled` | ['string', 'null'] |  | datetime of last pull |
| `tag_last_pushed` | ['string', 'null'] |  | datetime of last push |
| `tag_status` | string enum: active, inactive |  | whether a tag has been pushed to or pulled in the past month |

## updateOrgAccessTokenRequest

| Field | Type | Required | Description |
|---|---|---|---|
| `label` | string |  | Label for the access token |
| `description` | string |  | Description of the access token |
| `resources` | array of `orgAccessTokenResource` |  | Resources this token has access to |
| `is_active` | boolean |  | Whether the token is active |

## updateOrgAccessTokenResponse

Type: allOf(`orgAccessToken`, object)

## update_repository_immutable_tags_request

| Field | Type | Required | Description |
|---|---|---|---|
| `immutable_tags` | boolean | yes | Whether immutable tags are enabled |
| `immutable_tags_rules` | array of string | yes | List of immutable tag rules |

## user

| Field | Type | Required | Description |
|---|---|---|---|
| `id` | string |  | The UUID trimmed |
| `company` | string |  |  |
| `date_joined` | string |  |  |
| `full_name` | string |  |  |
| `gravatar_email` | string |  |  |
| `gravatar_url` | string |  |  |
| `location` | string |  |  |
| `profile_url` | string |  |  |
| `type` | string enum: User, Org |  |  |
| `username` | string |  |  |

