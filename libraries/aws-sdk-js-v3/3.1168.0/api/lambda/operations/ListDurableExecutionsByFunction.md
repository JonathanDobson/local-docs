# ListDurableExecutionsByFunction

Service: AWS Lambda · SDK for JavaScript v3: `ListDurableExecutionsByFunctionCommand` from `@aws-sdk/client-lambda` · HTTP: `GET /2025-12-01/functions/{FunctionName}/durable-executions` · Paginated (token `Marker` → `NextMarker`)

Returns a list of [durable executions](https://docs.aws.amazon.com/lambda/latest/dg/durable-functions.html) for a specified Lambda function. You can filter the results by execution name, status, and start time range. This API supports pagination for large result sets.

## Input (`ListDurableExecutionsByFunctionRequest`)

### `FunctionName` — string · **required** · sent as httpLabel

The name or ARN of the Lambda function. You can specify a function name, a partial ARN, or a full ARN.

### `Qualifier` — string · sent as query `Qualifier`

The function version to filter executions by. If you don't specify a qualifier, this operation returns executions across all versions of the Lambda function.

### `DurableExecutionName` — string · sent as query `DurableExecutionName`

Filter executions by name. Only executions with names that matches this string are returned.

### `Statuses` — list<ExecutionStatus (enum)> · sent as query `Statuses`

Filter executions by status. Valid values: RUNNING, SUCCEEDED, FAILED, TIMED\_OUT, STOPPED.

### `StartedAfter` — timestamp · sent as query `StartedAfter`

Filter executions that started after this timestamp (ISO 8601 format).

### `StartedBefore` — timestamp · sent as query `StartedBefore`

Filter executions that started before this timestamp (ISO 8601 format).

### `ReverseOrder` — boolean · sent as query `ReverseOrder`

Set to true to return results in chronological order (oldest first). Default is false.

### `Marker` — string · sent as query `Marker`

Pagination token from a previous request to continue retrieving results.

### `MaxItems` — integer · sent as query `MaxItems` · default `0`

Maximum number of executions to return (1-1000). Default is 100.

## Output (`ListDurableExecutionsByFunctionResponse`)

### `DurableExecutions` — list<Execution>

List of durable execution summaries matching the filter criteria.

### `NextMarker` — string

Pagination token for retrieving additional results. Present only if there are more results available.

## Errors

- `InvalidParameterValueException` — One of the parameters in the request is not valid.
- `ResourceNotFoundException` — The resource specified in the request does not exist.
- `ServiceException` — The Lambda service encountered an internal error.
- `TooManyRequestsException` — The request throughput limit was exceeded.
