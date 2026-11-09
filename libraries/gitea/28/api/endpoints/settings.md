# Gitea API 28.3.0 — settings

## GET /api/v1/settings/api

operationId: `getGeneralAPISettings`

Get instance's global settings for api

| Response | Description | Body |
|---|---|---|
| 200 | GeneralAPISettings (`GeneralAPISettings`) | `GeneralAPISettings` |

## GET /api/v1/settings/attachment

operationId: `getGeneralAttachmentSettings`

Get instance's global settings for Attachment

| Response | Description | Body |
|---|---|---|
| 200 | GeneralAttachmentSettings (`GeneralAttachmentSettings`) | `GeneralAttachmentSettings` |

## GET /api/v1/settings/repository

operationId: `getGeneralRepositorySettings`

Get instance's global settings for repositories

| Response | Description | Body |
|---|---|---|
| 200 | GeneralRepoSettings (`GeneralRepoSettings`) | `GeneralRepoSettings` |

## GET /api/v1/settings/ui

operationId: `getGeneralUISettings`

Get instance's global settings for ui

| Response | Description | Body |
|---|---|---|
| 200 | GeneralUISettings (`GeneralUISettings`) | `GeneralUISettings` |
