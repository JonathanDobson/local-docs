---
title: "AI Governance Audit Logs API 1"
source: https://docs.docker.com/reference/api/ai-governance-audit-logs/latest/
---

# AI Governance Audit Logs API 1


[API catalog](/reference/api/) · [AI Governance Audit Logs overview](/reference/api/ai-governance-audit-logs/latest/) · [Product manual](https://docs.docker.com/ai/governance/organization/audit/) · [OpenAPI specification](/reference/api/ai-governance-audit-logs/api.yaml)

API version: 1




## Overview

Retrieve Docker AI Governance audit events for an organization.

The API returns cloud-delivered governance records in reverse chronological
order. Use filters to investigate policy decisions, principals, resources,
sessions, and agents. Results use cursor-based pagination.

Send an Organization Access Token (OAT) with the **View audit logs**
permission as the bearer token. Personal Access Tokens (PATs) and Docker
account session tokens aren't supported. The organization in the request
path must match the organization associated with the OAT.

An AI Governance subscription and Docker Cloud audit delivery are required.

The API and gateway each enforce a limit of 5 requests per second per
organization. All clients and tokens in an organization share these limits,
and each pagination request counts. The gateway also limits requests to
600 per minute per source IP address. Gateway platform limits also apply.
Application rate-limit responses report the configured quota and window.

## Connecting to the AI Governance Audit Logs API


### bearerAuth

A raw Organization Access Token with the **View audit logs** permission.
Pass the OAT in the `Authorization: Bearer <OAT>` header. Don't exchange
the OAT for a Docker account session token. PATs aren't supported.



Server: `https://api.docker.com`




- [Retrieve audit events with the API](https://docs.docker.com/ai/governance/organization/audit/api/)



## Audit events

Retrieve Docker AI Governance audit events.

## Operations

- [GET /v2/auditlogs/governance/{org_name}](/reference/api/ai-governance-audit-logs/latest/operations/listAuditEvents/): List audit events

## Schemas

- [ApplicationRateLimitError](/reference/api/ai-governance-audit-logs/latest/schemas/ApplicationRateLimitError/)

- [AuditEvent](/reference/api/ai-governance-audit-logs/latest/schemas/AuditEvent/)

- [Error](/reference/api/ai-governance-audit-logs/latest/schemas/Error/)

- [ListAuditEventsResponse](/reference/api/ai-governance-audit-logs/latest/schemas/ListAuditEventsResponse/)
