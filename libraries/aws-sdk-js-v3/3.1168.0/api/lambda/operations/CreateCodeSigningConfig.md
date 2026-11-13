# CreateCodeSigningConfig

Service: AWS Lambda · SDK for JavaScript v3: `CreateCodeSigningConfigCommand` from `@aws-sdk/client-lambda` · HTTP: `POST /2020-04-22/code-signing-configs`

Creates a code signing configuration. A [code signing configuration](https://docs.aws.amazon.com/lambda/latest/dg/configuration-codesigning.html) defines a list of allowed signing profiles and defines the code-signing validation policy (action to be taken if deployment validation checks fail).

## Input (`CreateCodeSigningConfigRequest`)

### `Description` — string

Descriptive name for this code signing configuration.

### `AllowedPublishers` — AllowedPublishers · **required**

Signing profiles for this code signing configuration.

### `CodeSigningPolicies` — CodeSigningPolicies

The code signing policies define the actions to take if the validation checks fail.

### `Tags` — map<string, string>

A list of tags to add to the code signing configuration.

## Output (`CreateCodeSigningConfigResponse`)

### `CodeSigningConfig` — CodeSigningConfig · **required**

The code signing configuration.

## Errors

- `InvalidParameterValueException` — One of the parameters in the request is not valid.
- `ServiceException` — The Lambda service encountered an internal error.
