---
title: "Publisher analytics API 1.0.0"
source: https://docs.docker.com/reference/api/dvp/latest/
---

# Publisher analytics API 1.0.0


[API catalog](/reference/api/) · [Publisher analytics overview](/reference/api/dvp/latest/) · [Product manual](https://docs.docker.com/docker-hub/repos/manage/trusted-content/insights-analytics/) · [OpenAPI specification](/reference/api/dvp/latest.yaml)

API version: 1.0.0




## Overview

The Docker DVP Data API allows [Docker Verified Publishers](https://docs.docker.com/docker-hub/publish/) to view image pull analytics data for their namespaces. Analytics data can be retrieved in a CSV as raw data, or in a summary format.
  
#### Summary data

In your summary data CSV, you will have access to the data points listed below. You can request summary data for a complete week (Monday through Sunday) or for a complete month (available on the first day of the following month). 

There are two levels of summary data:

- Repository-level, a summary of every namespace and repository
- Tag- or digest-level, a summary of every namespace, repository, and reference
  (tag or digest)

The summary data formats contain the following data points:

- Unique IP address count
- Pulls by tag count
- Pulls by digest count
- Version check count

#### Raw data

In your raw data CSV you will have access to the data points listed below. You can request raw data for a complete week (Monday through Sunday) or for a complete month (available on the first day of the following month). **Note:** each action is represented as a single row.

- Type (industry)
- Host (cloud provider)
- Country (geolocation)
- Timestamp
- Namespace
- Repository
- Reference (digest is always included, tag is provided when available)
- HTTP request method
- Action, one of the following:
  - Pull by tag
  - Pull by digest
  - Version check
- User-Agent

## Connecting to the Publisher analytics API


### Docker Hub Authentication

JWT Bearer Authentication is required to access the Docker DVP Data API.  
  
This authentication documentation is duplicated from the [Hub API Authentication docs](https://docs.docker.com/reference/api/hub/latest/#authentication)



Server: `https://hub.docker.com/api/publisher/analytics/v1`





## Operations

- [GET /](/reference/api/dvp/latest/operations/getNamespaces/): Get namespaces and repos

- [GET /namespaces](/reference/api/dvp/latest/operations/getUserNamespaces/): Get user's namespaces

- [GET /namespaces/{namespace}](/reference/api/dvp/latest/operations/getNamespace/): Get namespace

- [GET /namespaces/{namespace}/pulls](/reference/api/dvp/latest/operations/getNamespacePulls/): Get pull data

- [GET /namespaces/{namespace}/pulls/exports/years](/reference/api/dvp/latest/operations/getNamespaceYears/): Get years with data

- [GET /namespaces/{namespace}/pulls/exports/years/{year}/{timespantype}](/reference/api/dvp/latest/operations/getNamespaceTimespans/): Get timespans with data

- [GET /namespaces/{namespace}/pulls/exports/years/{year}/{timespantype}/{timespan}](/reference/api/dvp/latest/operations/getNamespaceTimespanMetadata/): Get namespace metadata for timespan

- [GET /namespaces/{namespace}/pulls/exports/years/{year}/{timespantype}/{timespan}/{dataview}](/reference/api/dvp/latest/operations/getNamespaceDataByTimespan/): Get namespace data for timespan

- [GET /namespaces/{namespace}/repos/{repo}/pulls](/reference/api/dvp/latest/operations/getRepoPulls/): Get pull data

- [GET /repos/pulls](/reference/api/dvp/latest/operations/getManyReposPulls/): Get pull data for multiple repos

- [POST /v2/users/2fa-login](/reference/api/dvp/latest/operations/PostUsers2FALogin/): Second factor authentication

- [POST /v2/users/login](/reference/api/dvp/latest/operations/PostUsersLogin/): Create an authentication token

## Schemas

- [DatasetModel](/reference/api/dvp/latest/schemas/DatasetModel/)

- [DatasetType](/reference/api/dvp/latest/schemas/DatasetType/)

- [DataviewType](/reference/api/dvp/latest/schemas/DataviewType/)

- [GroupType](/reference/api/dvp/latest/schemas/GroupType/)

- [MonthData](/reference/api/dvp/latest/schemas/MonthData/)

- [MonthModel](/reference/api/dvp/latest/schemas/MonthModel/)

- [NamespaceData](/reference/api/dvp/latest/schemas/NamespaceData/)

- [NamespaceMetadata](/reference/api/dvp/latest/schemas/NamespaceMetadata/)

- [PeriodType](/reference/api/dvp/latest/schemas/PeriodType/)

- [PostUsers2FALoginErrorResponse](/reference/api/dvp/latest/schemas/PostUsers2FALoginErrorResponse/)

- [PostUsersLoginErrorResponse](/reference/api/dvp/latest/schemas/PostUsersLoginErrorResponse/)

- [PostUsersLoginSuccessResponse](/reference/api/dvp/latest/schemas/PostUsersLoginSuccessResponse/)

- [PullData](/reference/api/dvp/latest/schemas/PullData/)

- [PullModel](/reference/api/dvp/latest/schemas/PullModel/)

- [ReposPullData](/reference/api/dvp/latest/schemas/ReposPullData/)

- [ResponseData](/reference/api/dvp/latest/schemas/ResponseData/)

- [ResponseDataFile](/reference/api/dvp/latest/schemas/ResponseDataFile/)

- [TimespanData](/reference/api/dvp/latest/schemas/TimespanData/)

- [TimespanModel](/reference/api/dvp/latest/schemas/TimespanModel/)

- [TimespanType](/reference/api/dvp/latest/schemas/TimespanType/)

- [Users2FALoginRequest](/reference/api/dvp/latest/schemas/Users2FALoginRequest/)

- [UsersLoginRequest](/reference/api/dvp/latest/schemas/UsersLoginRequest/)

- [WeekData](/reference/api/dvp/latest/schemas/WeekData/)

- [WeekModel](/reference/api/dvp/latest/schemas/WeekModel/)

- [YearData](/reference/api/dvp/latest/schemas/YearData/)

- [YearModel](/reference/api/dvp/latest/schemas/YearModel/)
