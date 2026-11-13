# GetCodeSigningConfig

Service: AWS Lambda · SDK for JavaScript v3: `GetCodeSigningConfigCommand` from `@aws-sdk/client-lambda` · HTTP: `GET /2020-04-22/code-signing-configs/{CodeSigningConfigArn}`

Returns information about the specified code signing configuration.

## Input (`GetCodeSigningConfigRequest`)

### `CodeSigningConfigArn` — string · **required** · sent as httpLabel

The The Amazon Resource Name (ARN) of the code signing configuration.

## Output (`GetCodeSigningConfigResponse`)

### `CodeSigningConfig` — CodeSigningConfig · **required**

The code signing configuration

## Errors

- `InvalidParameterValueException` — One of the parameters in the request is not valid.
- `ResourceNotFoundException` — The resource specified in the request does not exist.
- `ServiceException` — The Lambda service encountered an internal error.
