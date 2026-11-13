# ListFunctions

Service: AWS Lambda · SDK for JavaScript v3: `ListFunctionsCommand` from `@aws-sdk/client-lambda` · HTTP: `GET /2015-03-31/functions` · Paginated

Returns a list of Lambda Event Functions, with the version-specific configuration of each. Lambda returns up to 50 functions per call.

Set `FunctionVersion` to `ALL` to include all published versions of each function in addition to the unpublished version.

The `ListFunctions` operation returns a subset of the FunctionConfiguration fields. To get the additional fields (State, StateReasonCode, StateReason, LastUpdateStatus, LastUpdateStatusReason, LastUpdateStatusReasonCode, RuntimeVersionConfig) for a function or version, use GetFunction.

## Input (`ListFunctionsRequest`)

### `MasterRegion` — string · sent as query `MasterRegion`

For Lambda@Edge functions, the Amazon Web Services Region of the master function. For example, `us-east-1` filters the list of functions to include only Lambda@Edge functions replicated from a master function in US East (N. Virginia). If specified, you must set `FunctionVersion` to `ALL`.

### `FunctionVersion` — FunctionVersion (enum) · sent as query `FunctionVersion`

Set to `ALL` to include entries for all published versions of each function.

Values: `ALL`

### `Marker` — string · sent as query `Marker`

Specify the pagination token that's returned by a previous request to retrieve the next page of results.

### `MaxItems` — integer · sent as query `MaxItems`

The maximum number of functions to return in the response. Note that `ListFunctions` returns a maximum of 50 items in each response, even if you set the number higher.

## Output (`ListFunctionsResponse`)

### `NextMarker` — string

The pagination token that's included if more results are available.

### `Functions` — list<FunctionConfiguration>

A list of Lambda functions.

## Errors

- `InvalidParameterValueException` — One of the parameters in the request is not valid.
- `ServiceException` — The Lambda service encountered an internal error.
- `TooManyRequestsException` — The request throughput limit was exceeded.

## Examples

### To get a list of Lambda functions

This operation returns a list of Lambda functions.

Output:

```json
{
  "Functions": [
    {
      "CodeSha256": "dBG9m8SGdmlEjw/JYXlhhvCrAv5TxvXsbL/RMr0fT/I=",
      "CodeSize": 294,
      "Description": "",
      "FunctionArn": "arn:aws:lambda:us-west-2:123456789012:function:helloworld",
      "FunctionName": "helloworld",
      "Handler": "helloworld.handler",
      "LastModified": "2019-09-23T18:32:33.857+0000",
      "MemorySize": 128,
      "RevisionId": "1718e831-badf-4253-9518-d0644210af7b",
      "Role": "arn:aws:iam::123456789012:role/service-role/MyTestFunction-role-zgur6bf4",
      "Runtime": "nodejs10.x",
      "Timeout": 3,
      "TracingConfig": {
        "Mode": "PassThrough"
      },
      "Version": "$LATEST"
    },
    {
      "CodeSha256": "sU0cJ2/hOZevwV/lTxCuQqK3gDZP3i8gUoqUUVRmY6E=",
      "CodeSize": 266,
      "Description": "",
      "DurableConfig": {
        "ExecutionTimeout": 31622400,
        "RetentionPeriodInDays": 30
      },
      "FunctionArn": "arn:aws:lambda:us-west-2:123456789012:function:my-function",
      "FunctionName": "my-function",
      "Handler": "index.handler",
      "LastModified": "2019-10-01T16:47:28.490+0000",
      "MemorySize": 256,
      "RevisionId": "93017fc9-59cb-41dc-901b-4845ce4bf668",
      "Role": "arn:aws:iam::123456789012:role/service-role/helloWorldPython-role-uy3l9qyq",
      "Runtime": "nodejs10.x",
      "Timeout": 3,
      "TracingConfig": {
        "Mode": "PassThrough"
      },
      "Version": "$LATEST",
      "VpcConfig": {
        "SecurityGroupIds": [],
        "SubnetIds": [],
        "VpcId": ""
      }
    }
  ],
  "NextMarker": ""
}
```
