# ListLayers

Service: AWS Lambda · SDK for JavaScript v3: `ListLayersCommand` from `@aws-sdk/client-lambda` · HTTP: `GET /2018-10-31/layers` · Paginated

Lists [Lambda layers](https://docs.aws.amazon.com/lambda/latest/dg/invocation-layers.html) and shows information about the latest version of each. Specify a [runtime identifier](https://docs.aws.amazon.com/lambda/latest/dg/lambda-runtimes.html) to list only layers that indicate that they're compatible with that runtime. Specify a compatible architecture to include only layers that are compatible with that [instruction set architecture](https://docs.aws.amazon.com/lambda/latest/dg/foundation-arch.html).

## Input (`ListLayersRequest`)

### `CompatibleArchitecture` — Architecture (enum) · sent as query `CompatibleArchitecture`

The compatible [instruction set architecture](https://docs.aws.amazon.com/lambda/latest/dg/foundation-arch.html).

Values: `x86_64`, `arm64`

### `CompatibleRuntime` — Runtime (enum) · sent as query `CompatibleRuntime`

A runtime identifier.

The following list includes deprecated runtimes. For more information, see [Runtime use after deprecation](https://docs.aws.amazon.com/lambda/latest/dg/lambda-runtimes.html#runtime-deprecation-levels).

For a list of all currently supported runtimes, see [Supported runtimes](https://docs.aws.amazon.com/lambda/latest/dg/lambda-runtimes.html#runtimes-supported).

Values: `nodejs`, `nodejs4.3`, `nodejs6.10`, `nodejs8.10`, `nodejs10.x`, `nodejs12.x`, `nodejs14.x`, `nodejs16.x`, `nodejs18.x`, `nodejs20.x`, `nodejs22.x`, `nodejs24.x`, `java8`, `java8.al2`, `java11`, `java17`, `java21`, `java25`, `python2.7`, `python3.6`, `python3.7`, `python3.8`, `python3.9`, `python3.10`, `python3.11`, `python3.12`, `python3.13`, `python3.14`, `dotnetcore1.0`, `dotnetcore2.0`, `dotnetcore2.1`, `dotnetcore3.1`, `dotnet6`, `dotnet8`, `dotnet10`, `nodejs4.3-edge`, `go1.x`, `ruby2.5`, `ruby2.7`, `ruby3.2`, `ruby3.3`, `ruby3.4`, `ruby4.0`, `provided`, `provided.al2`, `provided.al2023`, `nodejs26.x`, `python3.15`, `java8.al2023`, `java11.al2023`, `java17.al2023`

### `Marker` — string · sent as query `Marker`

A pagination token returned by a previous call.

### `MaxItems` — integer · sent as query `MaxItems`

The maximum number of layers to return.

## Output (`ListLayersResponse`)

### `NextMarker` — string

A pagination token returned when the response doesn't contain all layers.

### `Layers` — list<LayersListItem>

A list of function layers.

## Errors

- `InvalidParameterValueException` — One of the parameters in the request is not valid.
- `ServiceException` — The Lambda service encountered an internal error.
- `TooManyRequestsException` — The request throughput limit was exceeded.

## Examples

### To list the layers that are compatible with your function's runtime

The following example returns information about layers that are compatible with the Python 3.7 runtime.

Input:

```json
{
  "CompatibleRuntime": "python3.7"
}
```

Output:

```json
{
  "Layers": [
    {
      "LatestMatchingVersion": {
        "CompatibleRuntimes": [
          "python3.6",
          "python3.7"
        ],
        "CreatedDate": "2018-11-15T00:37:46.592+0000",
        "Description": "My layer",
        "LayerVersionArn": "arn:aws:lambda:us-east-2:123456789012:layer:my-layer:2",
        "Version": 2
      },
      "LayerArn": "arn:aws:lambda:us-east-2:123456789012:layer:my-layer",
      "LayerName": "my-layer"
    }
  ]
}
```
