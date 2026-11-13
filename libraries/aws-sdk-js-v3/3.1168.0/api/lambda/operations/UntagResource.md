# UntagResource

Service: AWS Lambda · SDK for JavaScript v3: `UntagResourceCommand` from `@aws-sdk/client-lambda` · HTTP: `DELETE /2017-03-31/tags/{Resource}`

Removes [tags](https://docs.aws.amazon.com/lambda/latest/dg/tagging.html) from a function, event source mapping, or code signing configuration.

## Input (`UntagResourceRequest`)

### `Resource` — string · **required** · sent as httpLabel

The resource's Amazon Resource Name (ARN).

### `TagKeys` — list<string> · **required** · sent as query `tagKeys`

A list of tag keys to remove from the resource.

## Output (`Unit`)

_None._

## Errors

- `InvalidParameterValueException` — One of the parameters in the request is not valid.
- `ResourceConflictException` — The resource already exists, or another operation is in progress.
- `ResourceNotFoundException` — The resource specified in the request does not exist.
- `ServiceException` — The Lambda service encountered an internal error.
- `TooManyRequestsException` — The request throughput limit was exceeded.

## Examples

### To remove tags from an existing Lambda function

The following example removes the tag with the key name DEPARTMENT tag from the my-function Lambda function.

Input:

```json
{
  "Resource": "arn:aws:lambda:us-west-2:123456789012:function:my-function",
  "TagKeys": [
    "DEPARTMENT"
  ]
}
```
