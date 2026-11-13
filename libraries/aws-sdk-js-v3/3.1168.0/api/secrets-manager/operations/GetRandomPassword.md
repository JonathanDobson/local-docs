# GetRandomPassword

Service: AWS Secrets Manager · SDK for JavaScript v3: `GetRandomPasswordCommand` from `@aws-sdk/client-secrets-manager`

Generates a random password. We recommend that you specify the maximum length and
include every character type that the system you are generating a password for can
support. By default, Secrets Manager uses uppercase and lowercase letters, numbers, and the
following characters in passwords:
`` !\"#$%&'()*+,-./:;<=>?@[\\]^_`{|}~ ``

Secrets Manager generates a CloudTrail log entry when you call this
action.

**Required permissions:**
`secretsmanager:GetRandomPassword`. For more information, see [IAM policy actions for Secrets Manager](https://docs.aws.amazon.com/secretsmanager/latest/userguide/reference_iam-permissions.html#reference_iam-permissions_actions) and [Authentication
and access control in Secrets Manager](https://docs.aws.amazon.com/secretsmanager/latest/userguide/auth-and-access.html).

## Input (`GetRandomPasswordRequest`)

### `PasswordLength` — long

The length of the password. If you don't include this parameter, the default length is
32 characters.

### `ExcludeCharacters` — string

A string of the characters that you don't want in the password.

### `ExcludeNumbers` — boolean · default `null`

Specifies whether to exclude numbers from the password. If you don't include this
switch, the password can contain numbers.

### `ExcludePunctuation` — boolean · default `null`

Specifies whether to exclude the following punctuation characters from the password:
`` ! " # $ % & ' ( ) * + , - . / : ; < = > ? @ [ \ ] ^ _ ` { | }
~ ``. If you don't include this switch, the password can contain
punctuation.

### `ExcludeUppercase` — boolean · default `null`

Specifies whether to exclude uppercase letters from the password. If you don't include
this switch, the password can contain uppercase letters.

### `ExcludeLowercase` — boolean · default `null`

Specifies whether to exclude lowercase letters from the password. If you don't include
this switch, the password can contain lowercase letters.

### `IncludeSpace` — boolean · default `null`

Specifies whether to include the space character. If you include this switch, the
password can contain space characters.

### `RequireEachIncludedType` — boolean · default `null`

Specifies whether to include at least one upper and lowercase letter, one number, and
one punctuation. If you don't include this switch, the password contains at least one of
every character type.

## Output (`GetRandomPasswordResponse`)

### `RandomPassword` — string

A string with the password.

## Errors

- `InternalServiceError` — An error occurred on the server side.
- `InvalidParameterException` — The parameter name or value is invalid.
- `InvalidRequestException` — A parameter value is not valid for the current state of the resource.

## Examples

### To generate a random password

The following example shows how to request a randomly generated password. This example includes the optional flags to require spaces and at least one character of each included type. It specifies a length of 20 characters.

Input:

```json
{
  "PasswordLength": 20,
  "IncludeSpace": true,
  "RequireEachIncludedType": true
}
```

Output:

```json
{
  "RandomPassword": "EXAMPLE-PASSWORD"
}
```
