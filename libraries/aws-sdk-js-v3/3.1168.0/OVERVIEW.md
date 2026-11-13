# AWS SDK for JavaScript v3 (3.1168.0) — overview

The **AWS SDK for JavaScript v3**, release **3.1168.0** (newest on 2026-11-13),
from the aws/aws-sdk-js-v3 repository: the SDK's own guides and package READMEs,
plus the full **API reference** of the five services these projects call: S3,
Lambda, Secrets Manager, CloudWatch and Bedrock Runtime. The API reference is
generated from the exact Smithy models this SDK release was built from, so it
carries AWS's own description of every operation, parameter, error and example.

## Layout

| Folder | What it holds |
|---|---|
| `content/README.md` | SDK overview: modular packages, `Client` + `Command` style, `send()` |
| `content/UPGRADING.md` | v2 → v3: client constructors, error handling, credential providers |
| `content/guides/` | `CLIENTS.md` (every client constructor option: `region`, `credentials`, `profile`, `endpoint`, `requestHandler`, `retryStrategy`/`maxAttempts`, `logger`…), `ERROR_HANDLING.md`, `EFFECTIVE_PRACTICES.md`, `AWS_LAMBDA.md`, `TYPESCRIPT.md`, `SCHEMAS.md`, `MD5_FALLBACK.md`, `performance/` |
| `content/clients/` | The five clients' READMEs (install, usage, list of commands) |
| `content/packages/` | `credential-providers.md` (`fromIni`, `fromTemporaryCredentials`, `fromNodeProviderChain`…), `credential-provider-node.md` (the default chain), `s3-request-presigner.md` (`getSignedUrl`), `lib-storage.md` (`Upload` for multipart uploads) |
| `api/<service>/README.md` | Service description and every operation with a one-line summary |
| `api/<service>/operations/<Operation>.md` | One operation: JS command name, HTTP method and path, description, every input and output member (type, required, header/query/path), errors, examples |
| `api/<service>/shapes.md` | Data types: structures, unions and enums used by the operations |
| `api/<service>/<service>.json` | The Smithy model (source of truth) |

Services: `s3`, `lambda`, `secrets-manager`, `cloudwatch`, `bedrock-runtime`.

## Where to look for…

- **Configure a client (region, credentials, retries, timeouts, custom endpoint)** — `guides/CLIENTS.md`.
- **Where credentials come from by default** — `packages/credential-provider-node.md`; other providers in `packages/credential-providers.md`.
- **Handle and inspect errors (`$metadata`, `name`, retries)** — `guides/ERROR_HANDLING.md`.
- **Use the SDK inside Lambda** — `guides/AWS_LAMBDA.md`.
- **Pre-signed S3 URLs** — `packages/s3-request-presigner.md`, plus `api/s3/operations/GetObject.md` / `PutObject.md`.
- **Large or streaming S3 uploads** — `packages/lib-storage.md`.
- **Read a secret** — `api/secrets-manager/operations/GetSecretValue.md`.
- **Invoke a Lambda function** — `api/lambda/operations/Invoke.md`.
- **Publish a CloudWatch metric** — `api/cloudwatch/operations/PutMetricData.md`.
- **Call a Bedrock model** — `api/bedrock-runtime/operations/Converse.md`, `ConverseStream.md`, `InvokeModel.md`.
- **Moving code from SDK v2** — `UPGRADING.md`.

## Version notes

- v3 is modular: one package per service (`@aws-sdk/client-s3`), each operation a `Command` class sent with `client.send()`.
- Operation pages reflect the service APIs as of this release; services evolve independently of the SDK's version number, which increases with every weekly release.

## Search tips

- Search by operation name (`GetObject`) or command name (`GetObjectCommand`); pages give both.
- Member names are the API's PascalCase (`SecretId`, `FunctionName`, `MetricData`).
- "Sent as httpLabel" means the value goes in the URL path; "header `x-amz-…`" and "query `…`" say where else a member is sent.
