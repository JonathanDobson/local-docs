# DeleteCodeSigningConfig

Service: AWS Lambda · SDK for JavaScript v3: `DeleteCodeSigningConfigCommand` from `@aws-sdk/client-lambda` · HTTP: `DELETE /2020-04-22/code-signing-configs/{CodeSigningConfigArn}`

Deletes the code signing configuration. You can delete the code signing configuration only if no function is using it.

## Input (`DeleteCodeSigningConfigRequest`)

### `CodeSigningConfigArn` — string · **required** · sent as httpLabel

The The Amazon Resource Name (ARN) of the code signing configuration.

## Output (`DeleteCodeSigningConfigResponse`)

_None._

## Errors

- `InvalidParameterValueException` — One of the parameters in the request is not valid.
- `ResourceConflictException` — The resource already exists, or another operation is in progress.
- `ResourceNotFoundException` — The resource specified in the request does not exist.
- `ServiceException` — The Lambda service encountered an internal error.
