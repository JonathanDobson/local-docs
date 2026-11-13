# ListAsyncInvokes

Service: Amazon Bedrock Runtime · SDK for JavaScript v3: `ListAsyncInvokesCommand` from `@aws-sdk/client-bedrock-runtime` · HTTP: `GET /async-invoke` · Paginated (token `nextToken` → `nextToken`)

Lists asynchronous invocations.

## Input (`ListAsyncInvokesRequest`)

### `submitTimeAfter` — timestamp · sent as query `submitTimeAfter`

Include invocations submitted after this time.

### `submitTimeBefore` — timestamp · sent as query `submitTimeBefore`

Include invocations submitted before this time.

### `statusEquals` — AsyncInvokeStatus (enum) · sent as query `statusEquals`

Filter invocations by status.

Values: `InProgress`, `Completed`, `Failed`

### `maxResults` — integer · sent as query `maxResults`

The maximum number of invocations to return in one page of results.

### `nextToken` — string · sent as query `nextToken`

Specify the pagination token from a previous request to retrieve the next page of results.

### `sortBy` — SortAsyncInvocationBy (enum) · sent as query `sortBy` · default `"SubmissionTime"`

How to sort the response.

Values: `SubmissionTime`

### `sortOrder` — SortOrder (enum) · sent as query `sortOrder` · default `"Descending"`

The sorting order for the response.

Values: `Ascending`, `Descending`

## Output (`ListAsyncInvokesResponse`)

### `nextToken` — string

Specify the pagination token from a previous request to retrieve the next page of results.

### `asyncInvokeSummaries` — list<AsyncInvokeSummary>

A list of invocation summaries.

## Errors

- `AccessDeniedException` — The request is denied because you do not have sufficient permissions to perform the requested action.
- `InternalServerException` — An internal server error occurred.
- `ThrottlingException` — Your request was denied due to exceeding the account quotas for *Amazon Bedrock*.
- `ValidationException` — The input fails to satisfy the constraints specified by *Amazon Bedrock*.
