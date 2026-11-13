# UntagResource

Service: Amazon CloudWatch · SDK for JavaScript v3: `UntagResourceCommand` from `@aws-sdk/client-cloudwatch`

Removes one or more tags from the specified resource. Currently, alarms, dashboards,
metric streams and Contributor Insights rules support tagging.

## Input (`UntagResourceInput`)

### `ResourceARN` — string · **required**

The ARN of the CloudWatch resource that you're removing tags from.

The ARN format of an alarm is
`arn:aws:cloudwatch:Region:account-id:alarm:alarm-name`

The ARN format of a Contributor Insights rule is
`arn:aws:cloudwatch:Region:account-id:insight-rule/insight-rule-name`

The ARN format of a dashboard is
`arn:aws:cloudwatch::account-id:dashboard/dashboard-name`

The ARN format of a metric stream is
`arn:aws:cloudwatch:Region:account-id:metric-stream/metric-stream-name`

For more information about ARN format, see  [Resource Types Defined by Amazon CloudWatch](https://docs.aws.amazon.com/IAM/latest/UserGuide/list_amazoncloudwatch.html#amazoncloudwatch-resources-for-iam-policies) in the *Amazon Web
Services General Reference*.

### `TagKeys` — list<string> · **required**

The list of tag keys to remove from the resource.

## Output (`UntagResourceOutput`)

_None._

## Errors

- `ConcurrentModificationException` — More than one process tried to modify a resource at the same time.
- `ConflictException` — This operation attempted to create a resource that already exists.
- `InternalServiceFault` — Request processing has failed due to some unknown error, exception, or failure.
- `InvalidParameterValueException` — The value of an input parameter is bad or out-of-range.
- `ResourceNotFoundException` — The named resource does not exist.
