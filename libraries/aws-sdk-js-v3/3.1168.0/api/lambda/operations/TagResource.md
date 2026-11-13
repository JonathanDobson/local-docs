# TagResource

Service: AWS Lambda · SDK for JavaScript v3: `TagResourceCommand` from `@aws-sdk/client-lambda` · HTTP: `POST /2017-03-31/tags/{Resource}`

Adds [tags](https://docs.aws.amazon.com/lambda/latest/dg/tagging.html) to a function, event source mapping, or code signing configuration.

## Input (`TagResourceRequest`)

### `Resource` — string · **required** · sent as httpLabel

The resource's Amazon Resource Name (ARN).

### `Tags` — map<string, string> · **required**

A list of tags to apply to the resource.

## Output (`Unit`)

_None._

## Errors

- `InvalidParameterValueException` — One of the parameters in the request is not valid.
- `ResourceConflictException` — The resource already exists, or another operation is in progress.
- `ResourceNotFoundException` — The resource specified in the request does not exist.
- `ServiceException` — The Lambda service encountered an internal error.
- `TooManyRequestsException` — The request throughput limit was exceeded.

## Examples

### To add tags to an existing Lambda function

The following example adds a tag with the key name DEPARTMENT and a value of 'Department A' to the specified Lambda function.

Input:

```json
{
  "Resource": "arn:aws:lambda:us-west-2:123456789012:function:my-function",
  "Tags": {
    "DEPARTMENT": "Department A"
  }
}
```
