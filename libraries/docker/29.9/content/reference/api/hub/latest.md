---
title: "Docker Hub API 2-beta"
source: https://docs.docker.com/reference/api/hub/latest/
---

# Docker Hub API 2-beta


[API catalog](/reference/api/) · [Docker Hub overview](/reference/api/hub/latest/) · [Product manual](https://docs.docker.com/docker-hub/) · [OpenAPI specification](/reference/api/hub/latest.yaml)

API version: 2-beta




## Overview

Docker Hub is a service provided by Docker for finding and sharing container images with your team.

It is the world's largest library and community for container images.

In addition to the [Docker Hub UI](https://docs.docker.com/docker-hub/) and [Docker Hub CLI tool](https://github.com/docker/hub-tool#readme) (currently experimental), Docker provides an API that allows you to interact with Docker Hub.

Browse through the Docker Hub API documentation to explore the supported endpoints.

## Connecting to the Docker Hub API


### scimToken

Use the SCIM provisioning token configured for the organization.


Server: `https://hub.docker.com`




- [Set up SCIM provisioning](https://docs.docker.com/security/provisioning/scim/provision-scim/)



## Changelog

See the [Changelog](https://docs.docker.com/reference/api/hub/changelog) for a summary of changes across Docker Hub API versions.


## Resources

The following resources are available to interact with the documented API:
- [Docker Hub CLI tool](https://github.com/docker/hub-tool#readme) (currently experimental)


## Rate Limiting

The Docker Hub API is limited on the amount of requests you can perform per minute against it.

If you haven't hit the limit, each request to the API will return the following headers in the response.

- `X-RateLimit-Limit` - The limit of requests per minute.
- `X-RateLimit-Remaining` - The remaining amount of calls within the limit period.
- `X-RateLimit-Reset` - The unix timestamp of when the remaining resets.

If you have hit the limit, you will receive a response status of `429` and the `Retry-After` header in the response.

The [`Retry-After` header](https://developer.mozilla.org/en-US/docs/Web/HTTP/Reference/Headers/Retry-After) specifies the number of seconds to wait until you can call the API again.

**Note**: These rate limits are separate from anti-abuse and Docker Hub download, or pull rate limiting.
To learn more about Docker Hub pull rate limiting, see [Usage and limits](https://docs.docker.com/docker-hub/usage/).


## Authentication

Most Docker Hub API endpoints require you to authenticate using your Docker credentials before using them.

Additionally, similar to the Docker Hub UI features, API endpoint responses may vary depending on your subscription (Personal, Pro, or Team) and your account's permissions.

To learn more about the features available in each subscription and to upgrade your existing subscription, see [Docker Pricing](https://www.docker.com/pricing?ref=Docs&refAction=DocsApiHub).

# Types

The Docker Hub API supports the following authentication types.

You must use each authentication type with the [Create access token](/reference/api/hub/latest/operations/AuthCreateAccessToken/) route to obtain a bearer token.

## Password
Using a username and password is the most powerful, yet least secure way 
to authenticate with Docker as a user. It allows access to resources 
for the user without scopes. 

_In general, it is recommended to use a personal access token (PAT) instead._

_**The password authentication type is not available if your organization has SSO enforced.**_

## Personal Access Token (PAT)
Using a username and PAT is the most secure way to authenticate with 
Docker as a user. PATs are scoped to specific resources and scopes.

Currently, a PAT is a more secure password due to limited functionality. 
In the future, we may add fine-grained access like organization 
access tokens for enhanced usage and security.

## Organization Access Token (OAT)
Organization access tokens are scoped to specific resources and scopes 
in an organization. They are managed by organization owners. 

These tokens are meant for automation and are not meant to be used by 
users.

Operations that support bearer tokens issued from OATs state this in their descriptions.



## Authentication

The authentication endpoints allow you to authenticate with Docker Hub APIs.

For more information, see [Authentication](/reference/api/hub/latest/#tag-authentication).


## Personal Access Tokens

The Personal Access Token endpoints lets you manage personal access tokens. For more information, see [Access Tokens](https://docs.docker.com/security/access-tokens/personal-access-tokens/).

You can use a personal access token instead of a password in the [Docker CLI](https://docs.docker.com/reference/cli/docker/) or in the [Create an authentication token](/reference/api/hub/latest/operations/PostUsersLogin/) route to obtain a bearer token.

### Scopes

For each scope grouping (in this case "repo"), you only need to define 1 scope as any lower scopes are assumed.
For example: If you define `repo:write`, the API assumes the scope of both `repo:read` *and* `repo:public_read` as well.
If you were to define both `repo:write` *and* `repo:read`, then `repo:read` is assumed by `repo:write` and ignored.

`sandbox:use` is a separate grouping for Cloud Sandboxes. A repository scope does not include it, and it does not include a repository scope. A request can include `sandbox:use` on its own or with one repository scope.

***Treat your personal access token like your password and keep it secret. You cannot retrieve your token after it is generated.***


## Audit Logs

The Audit Logs API endpoints allow you to query audit log events across a namespace.

For more information, see [Audit Logs](https://docs.docker.com/admin/activity-logs/).


## Org Settings

The Org Settings API endpoints allow you to manage your organization's settings.


## Repositories

The repository endpoints allow you to access your repository's tags.


## Organizations

The organization endpoints allow you to interact with and manage your organizations.

For more information, see [Organization administration overview](https://docs.docker.com/admin/organization/).


## Groups (Teams)

The groups endpoints allow you to manage your organization's teams and their members.

For more information, see [Create and manage a team](https://docs.docker.com/admin/organization/manage/manage-a-team/).


## Invites

The invites endpoints allow you to manage invites for users to join your Docker organization.

For more information, see [Invite members](https://docs.docker.com/accounts/organization/manage/members/#invite-members).


## SCIM

SCIM is a provisioning system that lets you manage users within your identity provider (IdP).

For more information, see [System for Cross-domain Identity management](https://docs.docker.com/security/for-admins/provisioning/scim/).


## Organization Access Tokens

The organization access token endpoints allow you to manage organization access tokens (OATs). See [Organization access tokens](https://docs.docker.com/security/for-admins/access-tokens/) for more information.

OATs only authenticate requests to the modern namespace-scoped routes under `/v2/namespaces/{namespace}/repositories/`. Legacy repository paths are OAT unsupported, regardless of the token's scopes, and reject every OAT with `403 token issued from organization access token is not allowed`:

- `GET /v2/repositories/{namespace}/{repository}` — use [Get repository](/reference/api/hub/latest/operations/GetRepository/) instead.
- `GET /v2/repositories/{namespace}` — use [List repositories](/reference/api/hub/latest/operations/listNamespaceRepositories/) instead.
- `GET /v2/users/{username}/repositories` — use [List repositories](/reference/api/hub/latest/operations/listNamespaceRepositories/) instead.


## Operations

- [GET /v2/access-tokens](/reference/api/hub/latest/operations/getV2AccessTokens/): List personal access tokens

- [POST /v2/access-tokens](/reference/api/hub/latest/operations/postV2AccessTokens/): Create personal access token

- [GET /v2/access-tokens/{uuid}](/reference/api/hub/latest/operations/getV2AccessTokensByUuid/): Get personal access token

- [DELETE /v2/access-tokens/{uuid}](/reference/api/hub/latest/operations/deleteV2AccessTokensByUuid/): Delete personal access token

- [PATCH /v2/access-tokens/{uuid}](/reference/api/hub/latest/operations/patchV2AccessTokensByUuid/): Update personal access token

- [GET /v2/auditlogs/{account}](/reference/api/hub/latest/operations/AuditLogs_ListAuditLogs/): List audit log events

- [GET /v2/auditlogs/{account}/actions](/reference/api/hub/latest/operations/AuditLogs_ListAuditActions/): List audit log actions

- [POST /v2/auth/token](/reference/api/hub/latest/operations/AuthCreateAccessToken/): Create access token

- [POST /v2/invites/bulk](/reference/api/hub/latest/operations/postV2InvitesBulk/): Bulk create invites

- [DELETE /v2/invites/{id}](/reference/api/hub/latest/operations/deleteV2InvitesById/): Cancel an invite

- [PATCH /v2/invites/{id}/resend](/reference/api/hub/latest/operations/patchV2InvitesByIdResend/): Resend an invite

- [GET /v2/namespaces/{namespace}/repositories](/reference/api/hub/latest/operations/listNamespaceRepositories/): List repositories in a namespace

- [POST /v2/namespaces/{namespace}/repositories](/reference/api/hub/latest/operations/CreateRepository/): Create a new repository

- [GET /v2/namespaces/{namespace}/repositories/{repository}](/reference/api/hub/latest/operations/GetRepository/): Get repository in a namespace

- [HEAD /v2/namespaces/{namespace}/repositories/{repository}](/reference/api/hub/latest/operations/CheckRepository/): Check repository in a namespace

- [PATCH /v2/namespaces/{namespace}/repositories/{repository}/immutabletags](/reference/api/hub/latest/operations/UpdateRepositoryImmutableTags/): Update repository immutable tags

- [POST /v2/namespaces/{namespace}/repositories/{repository}/immutabletags/verify](/reference/api/hub/latest/operations/VerifyRepositoryImmutableTags/): Verify repository immutable tags

- [GET /v2/namespaces/{namespace}/repositories/{repository}/tags](/reference/api/hub/latest/operations/ListRepositoryTags/): List repository tags

- [HEAD /v2/namespaces/{namespace}/repositories/{repository}/tags](/reference/api/hub/latest/operations/headV2NamespacesByNamespaceRepositoriesByRepositoryTags/): Check repository tags

- [GET /v2/namespaces/{namespace}/repositories/{repository}/tags/{tag}](/reference/api/hub/latest/operations/GetRepositoryTag/): Read repository tag

- [HEAD /v2/namespaces/{namespace}/repositories/{repository}/tags/{tag}](/reference/api/hub/latest/operations/headV2NamespacesByNamespaceRepositoriesByRepositoryTagsByTag/): Check repository tag

- [GET /v2/orgs/{org_name}/access-tokens](/reference/api/hub/latest/operations/getV2OrgsByNameAccessTokens/): List access tokens

- [POST /v2/orgs/{org_name}/access-tokens](/reference/api/hub/latest/operations/postV2OrgsByNameAccessTokens/): Create access token

- [GET /v2/orgs/{org_name}/access-tokens/{access_token_id}](/reference/api/hub/latest/operations/getV2OrgsByOrgNameAccessTokensByAccessTokenId/): Get access token

- [DELETE /v2/orgs/{org_name}/access-tokens/{access_token_id}](/reference/api/hub/latest/operations/deleteV2OrgsByOrgNameAccessTokensByAccessTokenId/): Delete access token

- [PATCH /v2/orgs/{org_name}/access-tokens/{access_token_id}](/reference/api/hub/latest/operations/patchV2OrgsByOrgNameAccessTokensByAccessTokenId/): Update access token

- [GET /v2/orgs/{org_name}/groups](/reference/api/hub/latest/operations/getV2OrgsByOrgNameGroups/): Get groups of an organization

- [POST /v2/orgs/{org_name}/groups](/reference/api/hub/latest/operations/postV2OrgsByOrgNameGroups/): Create a new group

- [GET /v2/orgs/{org_name}/groups/{group_name}](/reference/api/hub/latest/operations/getV2OrgsByOrgNameGroupsByGroupName/): Get a group of an organization

- [PUT /v2/orgs/{org_name}/groups/{group_name}](/reference/api/hub/latest/operations/putV2OrgsByOrgNameGroupsByGroupName/): Update the details for an organization group

- [DELETE /v2/orgs/{org_name}/groups/{group_name}](/reference/api/hub/latest/operations/deleteV2OrgsByOrgNameGroupsByGroupName/): Delete an organization group

- [PATCH /v2/orgs/{org_name}/groups/{group_name}](/reference/api/hub/latest/operations/patchV2OrgsByOrgNameGroupsByGroupName/): Update some details for an organization group

- [GET /v2/orgs/{org_name}/groups/{group_name}/members](/reference/api/hub/latest/operations/getV2OrgsByOrgNameGroupsByGroupNameMembers/): List members of a group

- [POST /v2/orgs/{org_name}/groups/{group_name}/members](/reference/api/hub/latest/operations/postV2OrgsByOrgNameGroupsByGroupNameMembers/): Add a member to a group

- [DELETE /v2/orgs/{org_name}/groups/{group_name}/members/{username}](/reference/api/hub/latest/operations/deleteV2OrgsByOrgNameGroupsByGroupNameMembersByUsername/): Remove a user from a group

- [GET /v2/orgs/{org_name}/invites](/reference/api/hub/latest/operations/getV2OrgsByOrgNameInvites/): List org invites

- [GET /v2/orgs/{org_name}/members](/reference/api/hub/latest/operations/getV2OrgsByOrgNameMembers/): List org members

- [GET /v2/orgs/{org_name}/members/export](/reference/api/hub/latest/operations/getV2OrgsByOrgNameMembersExport/): Export org members CSV

- [PUT /v2/orgs/{org_name}/members/{username}](/reference/api/hub/latest/operations/putV2OrgsByOrgNameMembersByUsername/): Update org member (role)

- [DELETE /v2/orgs/{org_name}/members/{username}](/reference/api/hub/latest/operations/deleteV2OrgsByOrgNameMembersByUsername/): Remove member from org

- [GET /v2/orgs/{org_name}/settings](/reference/api/hub/latest/operations/getV2OrgsByNameSettings/): Get organization settings

- [PUT /v2/orgs/{org_name}/settings](/reference/api/hub/latest/operations/putV2OrgsByNameSettings/): Update organization settings

- [POST /v2/repositories/{namespace}/{repository}/groups](/reference/api/hub/latest/operations/CreateRepositoryGroup/): Assign a group (Team) to a repository for access

- [GET /v2/scim/2.0/ResourceTypes](/reference/api/hub/latest/operations/getV2Scim20ResourceTypes/): List resource types

- [GET /v2/scim/2.0/ResourceTypes/{name}](/reference/api/hub/latest/operations/getV2Scim20ResourceTypesByName/): Get a resource type

- [GET /v2/scim/2.0/Schemas](/reference/api/hub/latest/operations/getV2Scim20Schemas/): List schemas

- [GET /v2/scim/2.0/Schemas/{id}](/reference/api/hub/latest/operations/getV2Scim20SchemasById/): Get a schema

- [GET /v2/scim/2.0/ServiceProviderConfig](/reference/api/hub/latest/operations/getV2Scim20ServiceProviderConfig/): Get service provider config

- [GET /v2/scim/2.0/Users](/reference/api/hub/latest/operations/getV2Scim20Users/): List users

- [POST /v2/scim/2.0/Users](/reference/api/hub/latest/operations/postV2Scim20Users/): Create user

- [GET /v2/scim/2.0/Users/{id}](/reference/api/hub/latest/operations/getV2Scim20UsersById/): Get a user

- [PUT /v2/scim/2.0/Users/{id}](/reference/api/hub/latest/operations/putV2Scim20UsersById/): Update a user

- [POST /v2/users/2fa-login](/reference/api/hub/latest/operations/PostUsers2FALogin/): Second factor authentication

- [POST /v2/users/login](/reference/api/hub/latest/operations/PostUsersLogin/): Create an authentication token

## Schemas

- [AuditLog](/reference/api/hub/latest/schemas/AuditLog/)

- [AuditLogAction](/reference/api/hub/latest/schemas/AuditLogAction/)

- [AuditLogActions](/reference/api/hub/latest/schemas/AuditLogActions/)

- [AuthCreateTokenResponse](/reference/api/hub/latest/schemas/AuthCreateTokenResponse/)

- [GetAuditActionsResponse](/reference/api/hub/latest/schemas/GetAuditActionsResponse/)

- [GetAuditLogsResponse](/reference/api/hub/latest/schemas/GetAuditLogsResponse/)

- [PostUsers2FALoginErrorResponse](/reference/api/hub/latest/schemas/PostUsers2FALoginErrorResponse/)

- [PostUsersLoginErrorResponse](/reference/api/hub/latest/schemas/PostUsersLoginErrorResponse/)

- [PostUsersLoginSuccessResponse](/reference/api/hub/latest/schemas/PostUsersLoginSuccessResponse/)

- [RepositoryGroup](/reference/api/hub/latest/schemas/RepositoryGroup/)

- [RepositoryGroupCreationRequest](/reference/api/hub/latest/schemas/RepositoryGroupCreationRequest/)

- [Users2FALoginRequest](/reference/api/hub/latest/schemas/Users2FALoginRequest/)

- [UsersLoginRequest](/reference/api/hub/latest/schemas/UsersLoginRequest/)

- [accessToken](/reference/api/hub/latest/schemas/accessToken/)

- [bulk_invite](/reference/api/hub/latest/schemas/bulk_invite/)

- [category](/reference/api/hub/latest/schemas/category/)

- [createAccessTokenRequest](/reference/api/hub/latest/schemas/createAccessTokenRequest/)

- [createAccessTokensResponse](/reference/api/hub/latest/schemas/createAccessTokensResponse/)

- [createOrgAccessTokenRequest](/reference/api/hub/latest/schemas/createOrgAccessTokenRequest/)

- [createOrgAccessTokenResponse](/reference/api/hub/latest/schemas/createOrgAccessTokenResponse/)

- [email_address](/reference/api/hub/latest/schemas/email_address/)

- [email_with_username](/reference/api/hub/latest/schemas/email_with_username/)

- [error](/reference/api/hub/latest/schemas/error/)

- [getAccessTokensResponse](/reference/api/hub/latest/schemas/getAccessTokensResponse/)

- [getOrgAccessTokenResponse](/reference/api/hub/latest/schemas/getOrgAccessTokenResponse/)

- [getOrgAccessTokensResponse](/reference/api/hub/latest/schemas/getOrgAccessTokensResponse/)

- [group_member](/reference/api/hub/latest/schemas/group_member/)

- [image](/reference/api/hub/latest/schemas/image/)

- [immutable_tags_settings](/reference/api/hub/latest/schemas/immutable_tags_settings/)

- [immutable_tags_verify_request](/reference/api/hub/latest/schemas/immutable_tags_verify_request/)

- [immutable_tags_verify_response](/reference/api/hub/latest/schemas/immutable_tags_verify_response/)

- [invite](/reference/api/hub/latest/schemas/invite/)

- [layer](/reference/api/hub/latest/schemas/layer/)

- [legacy_email_address](/reference/api/hub/latest/schemas/legacy_email_address/)

- [list_repositories_response](/reference/api/hub/latest/schemas/list_repositories_response/)

- [orgAccessToken](/reference/api/hub/latest/schemas/orgAccessToken/)

- [orgAccessTokenResource](/reference/api/hub/latest/schemas/orgAccessTokenResource/)

- [orgSettings](/reference/api/hub/latest/schemas/orgSettings/)

- [org_group](/reference/api/hub/latest/schemas/org_group/)

- [org_member](/reference/api/hub/latest/schemas/org_member/)

- [org_member_paginated](/reference/api/hub/latest/schemas/org_member_paginated/)

- [page](/reference/api/hub/latest/schemas/page/)

- [paginated_tags](/reference/api/hub/latest/schemas/paginated_tags/)

- [patchAccessTokenRequest](/reference/api/hub/latest/schemas/patchAccessTokenRequest/)

- [patchAccessTokenResponse](/reference/api/hub/latest/schemas/patchAccessTokenResponse/)

- [repo_creation_request](/reference/api/hub/latest/schemas/repo_creation_request/)

- [repo_permissions](/reference/api/hub/latest/schemas/repo_permissions/)

- [repository_info](/reference/api/hub/latest/schemas/repository_info/)

- [repository_list_entry](/reference/api/hub/latest/schemas/repository_list_entry/)

- [restricted_images](/reference/api/hub/latest/schemas/restricted_images/)

- [scim_email](/reference/api/hub/latest/schemas/scim_email/)

- [scim_error](/reference/api/hub/latest/schemas/scim_error/)

- [scim_group](/reference/api/hub/latest/schemas/scim_group/)

- [scim_resource_type](/reference/api/hub/latest/schemas/scim_resource_type/)

- [scim_schema](/reference/api/hub/latest/schemas/scim_schema/)

- [scim_schema_attribute](/reference/api/hub/latest/schemas/scim_schema_attribute/)

- [scim_schema_parent_attribute](/reference/api/hub/latest/schemas/scim_schema_parent_attribute/)

- [scim_service_provider_config](/reference/api/hub/latest/schemas/scim_service_provider_config/)

- [scim_user](/reference/api/hub/latest/schemas/scim_user/)

- [scim_user_display_name](/reference/api/hub/latest/schemas/scim_user_display_name/)

- [scim_user_id](/reference/api/hub/latest/schemas/scim_user_id/)

- [scim_user_name](/reference/api/hub/latest/schemas/scim_user_name/)

- [scim_user_schemas](/reference/api/hub/latest/schemas/scim_user_schemas/)

- [scim_user_username](/reference/api/hub/latest/schemas/scim_user_username/)

- [tag](/reference/api/hub/latest/schemas/tag/)

- [updateOrgAccessTokenRequest](/reference/api/hub/latest/schemas/updateOrgAccessTokenRequest/)

- [updateOrgAccessTokenResponse](/reference/api/hub/latest/schemas/updateOrgAccessTokenResponse/)

- [update_repository_immutable_tags_request](/reference/api/hub/latest/schemas/update_repository_immutable_tags_request/)

- [user](/reference/api/hub/latest/schemas/user/)
