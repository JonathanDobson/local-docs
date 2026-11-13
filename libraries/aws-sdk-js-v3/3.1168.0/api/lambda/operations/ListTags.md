# ListTags

Service: AWS Lambda · SDK for JavaScript v3: `ListTagsCommand` from `@aws-sdk/client-lambda` · HTTP: `GET /2017-03-31/tags/{Resource}`

Returns a function, event source mapping, or code signing configuration's [tags](https://docs.aws.amazon.com/lambda/latest/dg/tagging.html). You can also view function tags with GetFunction.

## Input (`ListTagsRequest`)

### `Resource` — string · **required** · sent as httpLabel

The resource's Amazon Resource Name (ARN). Note: Lambda does not support adding tags to function aliases or versions.

## Output (`ListTagsResponse`)

### `Tags` — map<string, string>

The function's tags.

## Errors

- `InvalidParameterValueException` — One of the parameters in the request is not valid.
- `ResourceNotFoundException` — The resource specified in the request does not exist.
- `ServiceException` — The Lambda service encountered an internal error.
- `TooManyRequestsException` — The request throughput limit was exceeded.

## Examples

### To retrieve the list of tags for a Lambda function

The following example displays the tags attached to the my-function Lambda function.

Input:

```json
{
  "Resource": "arn:aws:lambda:us-west-2:123456789012:function:my-function"
}
```

Output:

```json
{
  "Tags": {
    "Category": "Web Tools",
    "Department": "Sales"
  }
}
```
