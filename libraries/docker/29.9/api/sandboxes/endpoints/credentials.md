# Docker Sandboxes API v1 — Credentials

## POST /sandboxes/v1/identity/exchange

operationId: `exchangeDockerCredential`

ExchangeDockerCredential consumes an identity token once for the authenticated owner.

ExchangeDockerCredential consumes an identity token once for the authenticated owner.
The exchanged credential is stored for that owner; the response is empty.

Returns unimplemented when this operation is unavailable. Support does not grant permission.

Request body (application/json): `IdentityExchangeServiceExchangeDockerCredentialRequest`

| Response | Description | Body |
|---|---|---|
| 200 | Success | `ExchangeCompositionCredentialResponse` |
| 501 | This operation is not available on this service. | `Error` |
| default | The structured Error body identifies the failure with a stable code and optional typed details. | `Error` |
