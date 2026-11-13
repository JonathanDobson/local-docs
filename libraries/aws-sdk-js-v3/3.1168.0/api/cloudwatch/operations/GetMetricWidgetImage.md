# GetMetricWidgetImage

Service: Amazon CloudWatch · SDK for JavaScript v3: `GetMetricWidgetImageCommand` from `@aws-sdk/client-cloudwatch`

You can use the `GetMetricWidgetImage` API to retrieve a snapshot graph
of one or more Amazon CloudWatch metrics as a bitmap image. You can then embed this
image into your services and products, such as wiki pages, reports, and documents. You
could also retrieve images regularly, such as every minute, and create your own custom
live dashboard.

`GetMetricWidgetImage` is not available in the Amazon Web Services
GovCloud (US) Regions. In those Regions, calls to this operation fail. For the list
of Amazon CloudWatch features that are not available in Amazon Web Services
GovCloud (US), see [Amazon CloudWatch in
Amazon Web Services GovCloud (US)](https://docs.aws.amazon.com/govcloud-us/latest/UserGuide/govcloud-cw.html).

The graph you retrieve can include all CloudWatch metric graph features, including
metric math and horizontal and vertical annotations.

There is a limit of 20 transactions per second for this API. Each
`GetMetricWidgetImage` action has the following limits:

- As many as 100 metrics in the graph.
- Up to 100 KB uncompressed payload.

## Input (`GetMetricWidgetImageInput`)

### `MetricWidget` — string · **required**

A JSON string that defines the bitmap graph to be retrieved. The string includes
the metrics to include in the graph, statistics, annotations, title, axis limits, and so
on. You can include only one `MetricWidget` parameter in each
`GetMetricWidgetImage` call.

For more information about the syntax of `MetricWidget` see [GetMetricWidgetImage: Metric Widget Structure and Syntax](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch-Metric-Widget-Structure.html).

If any metric on the graph could not load all the requested data points, an orange
triangle with an exclamation point appears next to the graph legend.

### `OutputFormat` — string

The format of the resulting image. Only PNG images are supported.

The default is `png`. If you specify `png`, the API returns
an HTTP response with the content-type set to `text/xml`. The image data is
in a `MetricWidgetImage` field. For example:

`>`

`iVBORw0KGgoAAAANSUhEUgAAAlgAAAGQEAYAAAAip...`

`6f0d4192-4d42-11e8-82c1-f539a07e0e3b`

The `image/png` setting is intended only for custom HTTP requests. For
most use cases, and all actions using an Amazon Web Services SDK, you should use
`png`. If you specify `image/png`, the HTTP response has a
content-type set to `image/png`, and the body of the response is a PNG
image.

## Output (`GetMetricWidgetImageOutput`)

### `MetricWidgetImage` — blob

The image of the graph, in the output format specified. The output is
base64-encoded.
