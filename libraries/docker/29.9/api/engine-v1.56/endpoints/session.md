# Docker Engine API 1.56 — Session

## POST /v1.56/session

operationId: `Session`

Initialize interactive session

Start a new interactive session with a server. Session allows server to
call back to the client for advanced capabilities.

> **Deprecated**: This endpoint is deprecated and will be removed in a future version.
> Server should support gRPC directly on the listening socket.

### Hijacking

This endpoint hijacks the HTTP connection to HTTP2 transport that allows
the client to expose gPRC services on that connection.

For example, the client sends this request to upgrade the connection:

```
POST /session HTTP/1.1
Upgrade: h2c
Connection: Upgrade
```

The Docker daemon responds with a `101 UPGRADED` response follow with
the raw stream:

```
HTTP/1.1 101 UPGRADED
Connection: Upgrade
Upgrade: h2c
```

| Response | Description | Body |
|---|---|---|
| 101 | no error, hijacking successful |  |
| 400 | bad parameter | `ErrorResponse` |
| 500 | server error | `ErrorResponse` |
