# UpdateCodeSigningConfig

Service: AWS Lambda · SDK for JavaScript v3: `UpdateCodeSigningConfigCommand` from `@aws-sdk/client-lambda` · HTTP: `PUT /2020-04-22/code-signing-configs/{CodeSigningConfigArn}`

Update the code signing configuration. Changes to the code signing configuration take effect the next time a user tries to deploy a code package to the function.

## Input (`UpdateCodeSigningConfigRequest`)

### `CodeSigningConfigArn` — string · **required** · sent as httpLabel

The The Amazon Resource Name (ARN) of the code signing configuration.

### `Description` — string

Descriptive name for this code signing configuration.

### `AllowedPublishers` — AllowedPublishers

Signing profiles for this code signing configuration.

### `CodeSigningPolicies` — CodeSigningPolicies

The code signing policy.

## Output (`UpdateCodeSigningConfigResponse`)

### `CodeSigningConfig` — CodeSigningConfig · **required**

The code signing configuration

## Errors

- `InvalidParameterValueException` — One of the parameters in the request is not valid.
- `ResourceNotFoundException` — The resource specified in the request does not exist.
- `ServiceException` — The Lambda service encountered an internal error.
