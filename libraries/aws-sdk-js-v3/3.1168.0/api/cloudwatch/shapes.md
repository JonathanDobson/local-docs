# Amazon CloudWatch — data types

Structures, unions and enums used by the operations (operation inputs and outputs are on the operation pages).

## ActionConfiguration (structure)

Settings that change the content of the notifications and events that an alarm sends
when its state changes. These settings apply to the alarm's actions, whichever state
triggers them.

### `AlarmTagsPropagation` — AlarmTagsPropagation

Settings for including the alarm's tags in its action notifications and
state-change events.

## ActionsSuppressedBy (enum)

Values: `WaitPeriod`, `ExtensionPeriod`, `Alarm`

## AlarmContributor (structure)

Represents an individual contributor to a multi-timeseries alarm, containing
information about a specific time series and its contribution to the alarm's
state.

### `ContributorId` — string · **required**

The unique identifier for this alarm contributor.

### `ContributorAttributes` — map<string, string> · **required**

A map of attributes that describe the contributor, such as metric dimensions and other
identifying characteristics.

### `StateReason` — string · **required**

An explanation for the contributor's current state, providing context about why it is
in its current condition.

### `StateTransitionedTimestamp` — timestamp

The timestamp when the contributor last transitioned to its current state.

## AlarmHistoryItem (structure)

Represents the history of a specific alarm.

### `AlarmName` — string

The descriptive name for the alarm.

### `AlarmContributorId` — string

The unique identifier of the alarm contributor associated with this history item, if
applicable.

### `AlarmType` — AlarmType (enum)

The type of alarm, either metric alarm or composite alarm.

Values: `CompositeAlarm`, `MetricAlarm`, `LogAlarm`

### `Timestamp` — timestamp

The time stamp for the alarm history item.

### `HistoryItemType` — HistoryItemType (enum)

The type of alarm history item.

Values: `ConfigurationUpdate`, `StateUpdate`, `Action`, `AlarmContributorStateUpdate`, `AlarmContributorAction`

### `HistorySummary` — string

A summary of the alarm history, in text format.

### `HistoryData` — string

Data about the alarm, in JSON format.

### `AlarmContributorAttributes` — map<string, string>

A map of attributes that describe the alarm contributor associated with this history
item, providing context about the contributor's characteristics at the time of the
event.

## AlarmMuteRuleStatus (enum)

Values: `SCHEDULED`, `ACTIVE`, `EXPIRED`

## AlarmMuteRuleSummary (structure)

Summary information about an alarm mute rule, including its name, status, and
configuration details.

### `AlarmMuteRuleArn` — string

The Amazon Resource Name (ARN) of the alarm mute rule.

### `ExpireDate` — timestamp

The date and time when the mute rule expires and is no longer evaluated. This field
is only present if an expiration date was configured.

### `Status` — AlarmMuteRuleStatus (enum)

The current status of the alarm mute rule. Valid values are `SCHEDULED`,
`ACTIVE`, or `EXPIRED`.

Values: `SCHEDULED`, `ACTIVE`, `EXPIRED`

### `MuteType` — string

Indicates whether the mute rule is one-time or recurring. Valid values are
`ONE_TIME` or `RECURRING`.

### `LastUpdatedTimestamp` — timestamp

The date and time when the mute rule was last updated.

## AlarmPromQLCriteria (structure)

Contains the configuration that determines how a PromQL alarm evaluates its
contributors, including the query to run and the durations that define when contributors
transition between states.

### `Query` — string · **required**

The PromQL query that the alarm evaluates. The query must return a result of vector
type. Each entry in the vector result represents an alarm contributor.

### `PendingPeriod` — integer

The duration, in seconds, that a contributor must be continuously breaching before
it transitions to the `ALARM` state.

### `RecoveryPeriod` — integer

The duration, in seconds, that a contributor must continuously not be breaching
before it transitions back to the `OK` state.

## AlarmTagsPropagation (structure)

Includes the alarm's tags in the notifications that the alarm sends to Amazon SNS
topics and Lambda functions. The tags are also included in the alarm's
state-change events in Amazon EventBridge. Other types of alarm actions don't receive
the tags.

By default, the alarm's tags aren't included.

Use this to route or filter notifications and events by tag, such as by team or
environment. You can also use it to read the alarm's tags without looking them up
separately.

To limit which tags are included, specify either `IncludedTagKeys` or
`ExcludedTagKeys`. You can't specify both. If you specify neither, all of
the alarm's tags are included. This includes tags that you add to the alarm later.

### `Enabled` — boolean · **required**

Set to `true` to include the alarm's tags. Set to `false` to
stop including them.

When this is `true`, you must have the
`cloudwatch:ListTagsForResource` permission on the alarm to create or
update it.

### `IncludedTagKeys` — list<string>

The tag keys to include. Only the alarm's tags with these keys are included.

You can specify 1 to 50 tag keys. Each tag key must be 1 to 128 characters long.

You can't specify both `IncludedTagKeys` and
`ExcludedTagKeys`.

### `ExcludedTagKeys` — list<string>

The tag keys to exclude. All of the alarm's tags except those with these keys are
included.

You can specify 1 to 50 tag keys. Each tag key must be 1 to 128 characters long.

You can't specify both `IncludedTagKeys` and
`ExcludedTagKeys`.

## AlarmType (enum)

Values: `CompositeAlarm`, `MetricAlarm`, `LogAlarm`

## AnomalyDetector (structure)

An anomaly detection model associated with a particular CloudWatch metric, statistic,
or metric math expression. You can use the model to display a band of expected, normal
values when the metric is graphed.

If you have enabled unified cross-account observability, and this account is a
monitoring account, the metric can be in the same account or a source account.

### `AnomalyDetectorId` — string

The unique identifier of the anomaly detector.

The identifier does not restrict access to a specific anomaly detector in an IAM
policy. Permissions for anomaly detector operations apply to all anomaly detectors
in the account.

### `Namespace` — string · **deprecated**

The namespace of the metric associated with the anomaly detection model.

### `MetricName` — string · **deprecated**

The name of the metric associated with the anomaly detection model.

### `Dimensions` — list<Dimension> · **deprecated**

The metric dimensions associated with the anomaly detection model.

### `Stat` — string · **deprecated**

The statistic associated with the anomaly detection model.

### `Configuration` — AnomalyDetectorConfiguration

The configuration specifies details about how the anomaly detection model is to be
trained, including time ranges to exclude from use for training the model, and the time
zone to use for the metric.

### `StateValue` — AnomalyDetectorStateValue (enum)

The current status of the anomaly detector's training.

Values: `PENDING_TRAINING`, `TRAINED_INSUFFICIENT_DATA`, `TRAINED`

### `MetricCharacteristics` — MetricCharacteristics

This object includes parameters that you can use to provide information about your
metric to CloudWatch to help it build more accurate anomaly detection models.
Currently, it includes the `PeriodicSpikes` parameter.

### `SingleMetricAnomalyDetector` — SingleMetricAnomalyDetector

The CloudWatch metric and statistic for this anomaly detector.

### `MetricMathAnomalyDetector` — MetricMathAnomalyDetector

The CloudWatch metric math expression for this anomaly detector.

## AnomalyDetectorAdaptationSpeed (enum)

Values: `FAST`, `NORMAL`, `SLOW`

## AnomalyDetectorConfiguration (structure)

The configuration specifies details about how the anomaly detection model is to be
trained, including time ranges to exclude from use for training the model and the time
zone to use for the metric.

### `ExcludedTimeRanges` — list<Range>

An array of time ranges to exclude from use when the anomaly detection model is
trained. Use this to make sure that events that could cause unusual values for the
metric, such as deployments, aren't used when CloudWatch creates the model.

### `MetricTimezone` — string

The time zone to use for the metric. This is useful to enable the model to
automatically account for daylight savings time changes if the metric is sensitive to
such time changes.

To specify a time zone, use the name of the time zone as specified in the standard
tz database. For more information, see [tz database](https://en.wikipedia.org/wiki/Tz_database).

### `AdaptationSpeed` — AnomalyDetectorAdaptationSpeed (enum)

The speed at which the anomaly detection model adapts to sustained changes in the
metric's baseline. Faster adaptation lets the model track shifting workloads sooner, but
increases the chance that the model treats a real, lasting change as normal.

Valid values:

- `FAST` - The model adapts quickly to sustained changes in the baseline.
- `NORMAL` - The model adapts at a moderate pace. This is the default value.
- `SLOW` - The model adapts slowly, reducing the risk of treating a real change as normal.

Values: `FAST`, `NORMAL`, `SLOW`

### `OutlierFilteringStrength` — AnomalyDetectorOutlierFilteringStrength (enum)

The aggressiveness with which CloudWatch filters outliers from the metric data
that the anomaly detection model uses. Stronger filtering excludes more extreme values,
which can produce a tighter band of expected values but may also suppress legitimate
spikes.

Valid values:

- `MINIMAL` - Excludes only the most extreme outliers.
- `MODERATE` - Excludes a moderate range of outliers. This is the default value.
- `STRICT` - Excludes a wider range of outliers, which can suppress legitimate spikes.

Values: `MINIMAL`, `MODERATE`, `STRICT`

## AnomalyDetectorOutlierFilteringStrength (enum)

Values: `MINIMAL`, `MODERATE`, `STRICT`

## AnomalyDetectorStateValue (enum)

Values: `PENDING_TRAINING`, `TRAINED_INSUFFICIENT_DATA`, `TRAINED`

## AnomalyDetectorType (enum)

Values: `SINGLE_METRIC`, `METRIC_MATH`

## ComparisonOperator (enum)

Values: `GreaterThanOrEqualToThreshold`, `GreaterThanThreshold`, `LessThanThreshold`, `LessThanOrEqualToThreshold`, `LessThanLowerOrGreaterThanUpperThreshold`, `LessThanLowerThreshold`, `GreaterThanUpperThreshold`

## CompositeAlarm (structure)

The details about a composite alarm.

### `ActionsEnabled` — boolean

Indicates whether actions should be executed during any changes to the alarm
state.

### `AlarmActions` — list<string>

The actions to execute when this alarm transitions to the ALARM state from any other
state. Each action is specified as an Amazon Resource Name (ARN).

### `AlarmArn` — string

The Amazon Resource Name (ARN) of the alarm.

### `AlarmConfigurationUpdatedTimestamp` — timestamp

The time stamp of the last update to the alarm configuration.

### `AlarmDescription` — string

The description of the alarm.

### `AlarmName` — string

The name of the alarm.

### `AlarmRule` — string

The rule that this alarm uses to evaluate its alarm state.

### `InsufficientDataActions` — list<string>

The actions to execute when this alarm transitions to the INSUFFICIENT\_DATA state from
any other state. Each action is specified as an Amazon Resource Name (ARN).

### `OKActions` — list<string>

The actions to execute when this alarm transitions to the OK state from any other
state. Each action is specified as an Amazon Resource Name (ARN).

### `StateReason` — string

An explanation for the alarm state, in text format.

### `StateReasonData` — string

An explanation for the alarm state, in JSON format.

### `StateUpdatedTimestamp` — timestamp

Tracks the timestamp of any state update, even if `StateValue` doesn't
change.

### `StateValue` — StateValue (enum)

The state value for the alarm.

Values: `OK`, `ALARM`, `INSUFFICIENT_DATA`

### `StateTransitionedTimestamp` — timestamp

The timestamp of the last change to the alarm's `StateValue`.

### `ActionsSuppressedBy` — ActionsSuppressedBy (enum)

When the value is `ALARM`, it means that the actions are suppressed
because the suppressor alarm is in `ALARM` When the value is
`WaitPeriod`, it means that the actions are suppressed because the
composite alarm is waiting for the suppressor alarm to go into into the
`ALARM` state. The maximum waiting time is as specified in
`ActionsSuppressorWaitPeriod`. After this time, the composite alarm
performs its actions. When the value is `ExtensionPeriod`, it means that the
actions are suppressed because the composite alarm is waiting after the suppressor alarm
went out of the `ALARM` state. The maximum waiting time is as specified in
`ActionsSuppressorExtensionPeriod`. After this time, the composite alarm
performs its actions.

Values: `WaitPeriod`, `ExtensionPeriod`, `Alarm`

### `ActionsSuppressedReason` — string

Captures the reason for action suppression.

### `ActionsSuppressor` — string

Actions will be suppressed if the suppressor alarm is in the `ALARM`
state. `ActionsSuppressor` can be an AlarmName or an Amazon Resource Name
(ARN) from an existing alarm.

### `ActionsSuppressorWaitPeriod` — integer

The maximum time in seconds that the composite alarm waits for the suppressor alarm
to go into the `ALARM` state. After this time, the composite alarm performs
its actions.

`WaitPeriod` is required only when `ActionsSuppressor` is
specified.

### `ActionsSuppressorExtensionPeriod` — integer

The maximum time in seconds that the composite alarm waits after suppressor alarm
goes out of the `ALARM` state. After this time, the composite alarm performs
its actions.

`ExtensionPeriod` is required only when `ActionsSuppressor` is
specified.

### `ActionConfiguration` — ActionConfiguration

Settings that change the content of the notifications and events that the alarm
sends when its state changes. These settings apply to the alarm's actions, whichever
state triggers them.

## DashboardEntry (structure)

Represents a specific dashboard.

### `DashboardName` — string

The name of the dashboard.

### `DashboardArn` — string

The Amazon Resource Name (ARN) of the dashboard.

### `LastModified` — timestamp

The time stamp of when the dashboard was last modified, either by an API call or
through the console. This number is expressed as the number of milliseconds since Jan 1,
1970 00:00:00 UTC.

### `Size` — long

The size of the dashboard, in bytes.

## DashboardValidationMessage (structure)

An error or warning for the operation.

### `DataPath` — string

The data path related to the message.

### `Message` — string

A message describing the error or warning.

## Datapoint (structure)

Encapsulates the statistical data that CloudWatch computes from metric
data.

### `Timestamp` — timestamp

The time stamp used for the data point.

### `SampleCount` — double

The number of metric values that contributed to the aggregate value of this data
point.

### `Average` — double

The average of the metric values that correspond to the data point.

### `Sum` — double

The sum of the metric values for the data point.

### `Minimum` — double

The minimum metric value for the data point.

### `Maximum` — double

The maximum metric value for the data point.

### `Unit` — StandardUnit (enum)

The standard unit for the data point.

Values: `Seconds`, `Microseconds`, `Milliseconds`, `Bytes`, `Kilobytes`, `Megabytes`, `Gigabytes`, `Terabytes`, `Bits`, `Kilobits`, `Megabits`, `Gigabits`, `Terabits`, `Percent`, `Count`, `Bytes/Second`, `Kilobytes/Second`, `Megabytes/Second`, `Gigabytes/Second`, `Terabytes/Second`, `Bits/Second`, `Kilobits/Second`, `Megabits/Second`, `Gigabits/Second`, `Terabits/Second`, `Count/Second`, `None`

### `ExtendedStatistics` — map<string, double>

The percentile statistic for the data point.

## Dimension (structure)

A dimension is a name/value pair that is part of the identity of a metric. Because
dimensions are part of the unique identifier for a metric, whenever you add a unique
name/value pair to one of your metrics, you are creating a new variation of that metric.
For example, many Amazon EC2 metrics publish `InstanceId` as a
dimension name, and the actual instance ID as the value for that dimension.

You can assign up to 30 dimensions to a metric.

### `Name` — string · **required**

The name of the dimension. Dimension names must contain only ASCII characters, must
include at least one non-whitespace character, and cannot start with a colon
(`:`). ASCII control characters are not supported as part of dimension
names.

### `Value` — string · **required**

The value of the dimension. Dimension values must contain only ASCII characters and
must include at least one non-whitespace character. ASCII control characters are not
supported as part of dimension values.

## DimensionFilter (structure)

Represents filters for a dimension.

### `Name` — string · **required**

The dimension name to be matched.

### `Value` — string

The value of the dimension to be matched.

## Entity (structure)

An entity associated with metrics, to allow for finding related telemetry. An entity
is typically a resource or service within your system. For example, metrics from an
Amazon EC2 instance could be associated with that instance as the entity.
Similarly, metrics from a service that you own could be associated with that service as
the entity.

### `KeyAttributes` — map<string, string>

The attributes of the entity which identify the specific entity, as a list of
key-value pairs. Entities with the same `KeyAttributes` are considered to be
the same entity. For an entity to be valid, the `KeyAttributes` must exist
and be formatted correctly.

There are five allowed attributes (key names): `Type`,
`ResourceType`, `Identifier`, `Name`, and
`Environment`.

For details about how to use the key attributes to specify an entity, see [How
to add related information to telemetry](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/adding-your-own-related-telemetry.html) in the *CloudWatch
User Guide*.

### `Attributes` — map<string, string>

Additional attributes of the entity that are not used to specify the identity of the
entity. A list of key-value pairs.

For details about how to use the attributes, see [How
to add related information to telemetry](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/adding-your-own-related-telemetry.html) in the *CloudWatch
User Guide*.

## EntityMetricData (structure)

A set of metrics that are associated with an entity, such as a specific service or
resource. Contains the entity and the list of metric data associated with it.

### `Entity` — Entity

The entity associated with the metrics.

### `MetricData` — list<MetricDatum>

The metric data.

## EvaluationCriteria (union)

The evaluation criteria for an alarm. This is a union type that currently supports
`PromQLCriteria`.

### `PromQLCriteria` — AlarmPromQLCriteria

The PromQL criteria for the alarm evaluation.

## EvaluationState (enum)

Values: `PARTIAL_DATA`, `EVALUATION_FAILURE`, `EVALUATION_ERROR`

## EvaluationWindow (union)

The evaluation window that an alarm uses to select the range of metric data that it
evaluates each time it runs. This is a union type. Set exactly one of its members,
`SlidingWindow` or `WallClockWindow`. If you don't set
`EvaluationWindow`, the alarm uses a `SlidingWindow` by
default.

For more information, see [Alarm
evaluation windows](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/alarm-evaluation-window.html) in the *CloudWatch User
Guide*.

### `WallClockWindow` — WallClockWindow

A wall clock window, which aligns the evaluated range to fixed clock boundaries that
match the alarm's period, such as the top of the hour, midnight, or the start of the
calendar week.

### `SlidingWindow` — SlidingWindow

A sliding window, which advances each time the alarm is evaluated, forming a rolling
time window. This is the default evaluation window.

## HistoryItemType (enum)

Values: `ConfigurationUpdate`, `StateUpdate`, `Action`, `AlarmContributorStateUpdate`, `AlarmContributorAction`

## InsightRule (structure)

This structure contains the definition for a Contributor Insights rule. For more
information about this rule, see [Using Constributor Insights to analyze high-cardinality data](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/ContributorInsights.html) in the
*Amazon CloudWatch User Guide*.

### `Name` — string · **required**

The name of the rule.

### `State` — string · **required**

Indicates whether the rule is enabled or disabled.

### `Schema` — string · **required**

For rules that you create, this is always `{"Name": "CloudWatchLogRule",
"Version": 1}`. For managed rules, this is `{"Name": "ServiceLogRule",
"Version": 1}`

### `Definition` — string · **required**

The definition of the rule, as a JSON object. The definition contains the keywords
used to define contributors, the value to aggregate on if this rule returns a sum
instead of a count, and the filters. For details on the valid syntax, see [Contributor Insights Rule Syntax](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/ContributorInsights-RuleSyntax.html).

### `ManagedRule` — boolean

An optional built-in rule that Amazon Web Services manages.

### `ApplyOnTransformedLogs` — boolean

Displays whether the rule is evaluated on the transformed versions of logs, for log
groups that have [Log
transformation](https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/CloudWatch-Logs-Transformation.html) enabled. If this is `false`, log events are
evaluated before they are transformed.

## InsightRuleContributor (structure)

One of the unique contributors found by a Contributor Insights rule. If the rule
contains multiple keys, then a unique contributor is a unique combination of values from
all the keys in the rule.

If the rule contains a single key, then each unique contributor is each unique value
for this key.

For more information, see [GetInsightRuleReport](https://docs.aws.amazon.com/AmazonCloudWatch/latest/APIReference/API_GetInsightRuleReport.html).

### `Keys` — list<string> · **required**

One of the log entry field keywords that is used to define contributors for this
rule.

### `ApproximateAggregateValue` — double · **required**

An approximation of the aggregate value that comes from this contributor.

### `Datapoints` — list<InsightRuleContributorDatapoint> · **required**

An array of the data points where this contributor is present. Only the data points
when this contributor appeared are included in the array.

## InsightRuleContributorDatapoint (structure)

One data point related to one contributor.

For more information, see [GetInsightRuleReport](https://docs.aws.amazon.com/AmazonCloudWatch/latest/APIReference/API_GetInsightRuleReport.html) and [InsightRuleContributor](https://docs.aws.amazon.com/AmazonCloudWatch/latest/APIReference/API_InsightRuleContributor.html).

### `Timestamp` — timestamp · **required**

The timestamp of the data point.

### `ApproximateValue` — double · **required**

The approximate value that this contributor added during this timestamp.

## InsightRuleMetricDatapoint (structure)

One data point from the metric time series returned in a Contributor Insights rule
report.

For more information, see [GetInsightRuleReport](https://docs.aws.amazon.com/AmazonCloudWatch/latest/APIReference/API_GetInsightRuleReport.html).

### `Timestamp` — timestamp · **required**

The timestamp of the data point.

### `UniqueContributors` — double

The number of unique contributors who published data during this timestamp.

This statistic is returned only if you included it in the `Metrics` array
in your request.

### `MaxContributorValue` — double

The maximum value provided by one contributor during this timestamp. Each timestamp is
evaluated separately, so the identity of the max contributor could be different for each
timestamp.

This statistic is returned only if you included it in the `Metrics` array
in your request.

### `SampleCount` — double

The number of occurrences that matched the rule during this data point.

This statistic is returned only if you included it in the `Metrics` array
in your request.

### `Average` — double

The average value from all contributors during the time period represented by that
data point.

This statistic is returned only if you included it in the `Metrics` array
in your request.

### `Sum` — double

The sum of the values from all contributors during the time period represented by that
data point.

This statistic is returned only if you included it in the `Metrics` array
in your request.

### `Minimum` — double

The minimum value from a single contributor during the time period represented by that
data point.

This statistic is returned only if you included it in the `Metrics` array
in your request.

### `Maximum` — double

The maximum value from a single occurence from a single contributor during the time
period represented by that data point.

This statistic is returned only if you included it in the `Metrics` array
in your request.

## LabelOptions (structure)

This structure includes the `Timezone` parameter, which you can use to
specify your time zone so that the labels that are associated with returned metrics
display the correct time for your time zone.

The `Timezone` value affects a label only if you have a time-based dynamic
expression in the label. For more information about dynamic expressions in labels, see
[Using Dynamic
Labels](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/graph-dynamic-labels.html).

### `Timezone` — string

The time zone to use for metric data return in this operation. The format is
`+` or `-` followed by four digits. The first two digits
indicate the number of hours ahead or behind of UTC, and the final two digits are the
number of minutes. For example, +0130 indicates a time zone that is 1 hour and 30
minutes ahead of UTC. The default is +0000.

## LogAlarm (structure)

The details about a log alarm.

### `AlarmName` — string

The name of the alarm.

### `AlarmArn` — string

The Amazon Resource Name (ARN) of the alarm.

### `AlarmDescription` — string

The description of the alarm.

### `AlarmConfigurationUpdatedTimestamp` — timestamp

The time stamp of the last update to the alarm configuration.

### `ActionsEnabled` — boolean

Indicates whether actions should be executed during any changes to the alarm state.

### `OKActions` — list<string>

The actions to execute when this alarm transitions to the `OK` state from any other state. Each action is specified as an Amazon Resource Name (ARN).

### `AlarmActions` — list<string>

The actions to execute when this alarm transitions to the `ALARM` state from any other state. Each action is specified as an Amazon Resource Name (ARN).

### `InsufficientDataActions` — list<string>

The actions to execute when this alarm transitions to the `INSUFFICIENT_DATA` state from any other state. Each action is specified as an Amazon Resource Name (ARN).

### `StateValue` — StateValue (enum)

The state value for the alarm.

Values: `OK`, `ALARM`, `INSUFFICIENT_DATA`

### `StateReason` — string

An explanation for the alarm state, in text format.

### `StateReasonData` — string

An explanation for the alarm state, in JSON format.

### `StateUpdatedTimestamp` — timestamp

The time stamp of the last update to the value of either the `StateValue` or `EvaluationState` parameters.

### `ScheduledQueryConfiguration` — ScheduledQueryConfiguration

The configuration of the underlying CloudWatch Logs scheduled query, including the query string, log groups, schedule, aggregation expression, and the ARN of the managed scheduled query.

### `QueryResultsToEvaluate` — integer

The number of most recent scheduled query results that the alarm evaluates against the threshold (the N in M-of-N evaluation).

### `QueryResultsToAlarm` — integer

The number of query results, out of the most recent `QueryResultsToEvaluate` results, that must breach the threshold to trigger the alarm to transition to `ALARM` (the M in M-of-N evaluation).

### `Threshold` — double

The value to compare with the aggregated query result.

### `ComparisonOperator` — ComparisonOperator (enum)

The arithmetic operation to use when comparing the aggregated query result and the threshold. The aggregated query result is used as the first operand.

Values: `GreaterThanOrEqualToThreshold`, `GreaterThanThreshold`, `LessThanThreshold`, `LessThanOrEqualToThreshold`, `LessThanLowerOrGreaterThanUpperThreshold`, `LessThanLowerThreshold`, `GreaterThanUpperThreshold`

### `TreatMissingData` — string

How this alarm handles missing data points. Valid values are `breaching`, `notBreaching`, `ignore`, and `missing`.

### `StateTransitionedTimestamp` — timestamp

The date and time that the alarm's `StateValue` most recently changed.

### `EvaluationState` — EvaluationState (enum)

If the value of this field is `EVALUATION_ERROR`, it indicates configuration errors in the alarm setup that require review and correction. Refer to the `StateReason` field of the alarm for more details.

If the value of this field is `EVALUATION_FAILURE`, it indicates temporary CloudWatch issues. We recommend manual monitoring until the issue is resolved.

If the value of this field is `PARTIAL_DATA`, it indicates that the query returned the maximum 500 contributor groups but more matched. The alarm evaluates the available contributors, but results might be incomplete.

Values: `PARTIAL_DATA`, `EVALUATION_FAILURE`, `EVALUATION_ERROR`

### `ActionLogLineCount` — integer

The number of log lines from the most recent scheduled query execution that are included in alarm action notifications. Valid range is 0 through 50. A value of 0 means no log lines are included.

### `ActionLogLineRoleArn` — string

The Amazon Resource Name (ARN) of the IAM role that CloudWatch assumes to retrieve log events for inclusion in alarm action notifications. Set when `ActionLogLineCount` is greater than 0.

### `WarmUpConfiguration` — WarmUpConfiguration

The warm-up configuration for the alarm. A warm-up period delays alarm evaluation
after you create or update the alarm. During the warm-up period, the alarm stays in
`INSUFFICIENT_DATA` and does not perform alarm actions.

For more information, see [Alarm warm-up
periods](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/alarm-warm-up.html) in the *Amazon CloudWatch User Guide*.

### `ActionConfiguration` — ActionConfiguration

Settings that change the content of the notifications and events that the alarm
sends when its state changes. These settings apply to the alarm's actions, whichever
state triggers them.

## ManagedRule (structure)

Contains the information that's required to enable a managed Contributor Insights
rule for an Amazon Web Services resource.

### `TemplateName` — string · **required**

The template name for the managed Contributor Insights rule, as returned by
`ListManagedInsightRules`.

### `ResourceARN` — string · **required**

The ARN of an Amazon Web Services resource that has managed Contributor Insights
rules.

### `Tags` — list<Tag>

A list of key-value pairs that you can associate with a managed Contributor Insights
rule. You can associate as many as 50 tags with a rule. Tags can help you organize and
categorize your resources. You also can use them to scope user permissions by granting a
user permission to access or change only the resources that have certain tag values. To
associate tags with a rule, you must have the `cloudwatch:TagResource`
permission in addition to the `cloudwatch:PutInsightRule` permission. If you
are using this operation to update an existing Contributor Insights rule, any tags that
you specify in this parameter are ignored. To change the tags of an existing rule, use
`TagResource`.

## ManagedRuleDescription (structure)

Contains information about managed Contributor Insights rules, as returned by
`ListManagedInsightRules`.

### `TemplateName` — string

The template name for the managed rule. Used to enable managed rules using
`PutManagedInsightRules`.

### `ResourceARN` — string

If a managed rule is enabled, this is the ARN for the related Amazon Web Services
resource.

### `RuleState` — ManagedRuleState

Describes the state of a managed rule. If present, it contains information about the
Contributor Insights rule that contains information about the related Amazon Web Services
resource.

## ManagedRuleState (structure)

The status of a managed Contributor Insights rule.

### `RuleName` — string · **required**

The name of the Contributor Insights rule that contains data for the specified
Amazon Web Services resource.

### `State` — string · **required**

Indicates whether the rule is enabled or disabled.

## MessageData (structure)

A message returned by the `GetMetricData`API, including a code and a
description.

If a cross-Region `GetMetricData` operation fails with a code of
`Forbidden` and a value of `Authentication too complex to retrieve
cross region data`, you can correct the problem by running the
`GetMetricData` operation in the same Region where the metric data
is.

### `Code` — string

The error code or status code associated with the message.

### `Value` — string

The message text.

## Metric (structure)

Represents a specific metric.

### `Namespace` — string

The namespace of the metric.

### `MetricName` — string

The name of the metric. This is a required field.

### `Dimensions` — list<Dimension>

The dimensions for the metric.

## MetricAlarm (structure)

The details about a metric alarm.

### `AlarmName` — string

The name of the alarm.

### `AlarmArn` — string

The Amazon Resource Name (ARN) of the alarm.

### `AlarmDescription` — string

The description of the alarm.

### `AlarmConfigurationUpdatedTimestamp` — timestamp

The time stamp of the last update to the alarm configuration.

### `ActionsEnabled` — boolean

Indicates whether actions should be executed during any changes to the alarm
state.

### `OKActions` — list<string>

The actions to execute when this alarm transitions to the `OK` state
from any other state. Each action is specified as an Amazon Resource Name
(ARN).

### `AlarmActions` — list<string>

The actions to execute when this alarm transitions to the `ALARM` state
from any other state. Each action is specified as an Amazon Resource Name
(ARN).

### `InsufficientDataActions` — list<string>

The actions to execute when this alarm transitions to the
`INSUFFICIENT_DATA` state from any other state. Each action is specified
as an Amazon Resource Name (ARN).

### `StateValue` — StateValue (enum)

The state value for the alarm.

Values: `OK`, `ALARM`, `INSUFFICIENT_DATA`

### `StateReason` — string

An explanation for the alarm state, in text format.

### `StateReasonData` — string

An explanation for the alarm state, in JSON format.

### `StateUpdatedTimestamp` — timestamp

The time stamp of the last update to the value of either the
`StateValue` or `EvaluationState` parameters.

### `MetricName` — string

The name of the metric associated with the alarm, if this is an alarm based on a
single metric.

### `Namespace` — string

The namespace of the metric associated with the alarm.

### `Statistic` — Statistic (enum)

The statistic for the metric associated with the alarm, other than percentile. For
percentile statistics, use `ExtendedStatistic`.

Values: `SampleCount`, `Average`, `Sum`, `Minimum`, `Maximum`

### `ExtendedStatistic` — string

The percentile statistic for the metric associated with the alarm. Specify a value
between p0.0 and p100.

### `Dimensions` — list<Dimension>

The dimensions for the metric associated with the alarm.

### `Period` — integer

The period, in seconds, over which the statistic is applied.

### `Unit` — StandardUnit (enum)

The unit of the metric associated with the alarm.

Values: `Seconds`, `Microseconds`, `Milliseconds`, `Bytes`, `Kilobytes`, `Megabytes`, `Gigabytes`, `Terabytes`, `Bits`, `Kilobits`, `Megabits`, `Gigabits`, `Terabits`, `Percent`, `Count`, `Bytes/Second`, `Kilobytes/Second`, `Megabytes/Second`, `Gigabytes/Second`, `Terabytes/Second`, `Bits/Second`, `Kilobits/Second`, `Megabits/Second`, `Gigabits/Second`, `Terabits/Second`, `Count/Second`, `None`

### `EvaluationPeriods` — integer

The number of periods over which data is compared to the specified
threshold.

### `DatapointsToAlarm` — integer

The number of data points that must be breaching to trigger the alarm.

### `Threshold` — double

The value to compare with the specified statistic.

### `ComparisonOperator` — ComparisonOperator (enum)

The arithmetic operation to use when comparing the specified statistic and
threshold. The specified statistic value is used as the first operand.

Values: `GreaterThanOrEqualToThreshold`, `GreaterThanThreshold`, `LessThanThreshold`, `LessThanOrEqualToThreshold`, `LessThanLowerOrGreaterThanUpperThreshold`, `LessThanLowerThreshold`, `GreaterThanUpperThreshold`

### `TreatMissingData` — string

Sets how this alarm is to handle missing data points. The valid values are
`breaching`, `notBreaching`, `ignore`, and
`missing`. For more information, see [Configuring how CloudWatch alarms treat missing data](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/AlarmThatSendsEmail.html#alarms-and-missing-data).

If this parameter is omitted, the default behavior of `missing` is
used.

This parameter is not applicable to PromQL alarms.

### `EvaluateLowSampleCountPercentile` — string

Used only for alarms based on percentiles. If `ignore`, the alarm state
does not change during periods with too few data points to be statistically significant.
If `evaluate` or this parameter is not used, the alarm is always evaluated
and possibly changes state no matter how many data points are available.

### `Metrics` — list<MetricDataQuery>

An array of MetricDataQuery structures, used in an alarm based on a metric math
expression. Each structure either retrieves a metric or performs a math expression. One
item in the Metrics array is the math expression that the alarm watches. This expression
by designated by having `ReturnData` set to true.

### `ThresholdMetricId` — string

In an alarm based on an anomaly detection model, this is the ID of the
`ANOMALY_DETECTION_BAND` function used as the threshold for the
alarm.

### `EvaluationState` — EvaluationState (enum)

If the value of this field is `PARTIAL_DATA`, it indicates that not all the
available data was able to be retrieved due to quota limitations. For more information,
see [Create
alarms on Metrics Insights queries](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/Create_Metrics_Insights_Alarm.html).

If the value of this field is `EVALUATION_ERROR`, it indicates
configuration errors in alarm setup that require review and correction. Refer to
StateReason field of the alarm for more details.

If the value of this field is `EVALUATION_FAILURE`, it indicates temporary
CloudWatch issues. We recommend manual monitoring until the issue is resolved

Values: `PARTIAL_DATA`, `EVALUATION_FAILURE`, `EVALUATION_ERROR`

### `StateTransitionedTimestamp` — timestamp

The date and time that the alarm's `StateValue` most recently
changed.

### `EvaluationWindow` — EvaluationWindow

The evaluation window that the alarm uses to select the range of metric data that it
evaluates. This is either a sliding window or a wall clock window. For more information,
see [Alarm
evaluation windows](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/alarm-evaluation-window.html) in the *CloudWatch User
Guide*.

### `WarmUpConfiguration` — WarmUpConfiguration

The warm-up configuration for the alarm. A warm-up period delays alarm evaluation
after you create or update the alarm. During the warm-up period, the alarm stays in
`INSUFFICIENT_DATA` and does not perform alarm actions.

For more information, see [Alarm warm-up
periods](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/alarm-warm-up.html) in the *Amazon CloudWatch User Guide*.

### `EvaluationCriteria` — EvaluationCriteria

The evaluation criteria for the alarm.

### `EvaluationInterval` — integer

The frequency, in seconds, at which the alarm is evaluated.

### `ActionConfiguration` — ActionConfiguration

Settings that change the content of the notifications and events that the alarm
sends when its state changes. These settings apply to the alarm's actions, whichever
state triggers them.

## MetricCharacteristics (structure)

This object includes parameters that you can use to provide information to CloudWatch to help it build more accurate anomaly detection models.

### `PeriodicSpikes` — boolean

Set this parameter to `true` if values for this metric consistently include
spikes that should not be considered to be anomalies. With this set to
`true`, CloudWatch will expect to see spikes that occurred
consistently during the model training period, and won't flag future similar spikes as
anomalies.

## MetricDataQuery (structure)

This structure is used in both `GetMetricData` and
`PutMetricAlarm`. The supported use of this structure is different for
those two operations.

When used in `GetMetricData`, it indicates the metric data to return, and
whether this call is just retrieving a batch set of data for one metric, or is
performing a Metrics Insights query or a math expression. A single
`GetMetricData` call can include up to 500 `MetricDataQuery`
structures.

When used in `PutMetricAlarm`, it enables you to create an alarm based on a
metric math expression. Each `MetricDataQuery` in the array specifies either
a metric to retrieve, or a math expression to be performed on retrieved metrics. A
single `PutMetricAlarm` call can include up to 20
`MetricDataQuery` structures in the array. The 20 structures can include
as many as 10 structures that contain a `MetricStat` parameter to retrieve a
metric, and as many as 10 structures that contain the `Expression` parameter
to perform a math expression. Of those `Expression` structures, one must have
`true` as the value for `ReturnData`. The result of this
expression is the value the alarm watches.

Any expression used in a `PutMetricAlarm` operation must return a single
time series. For more information, see [Metric Math Syntax and Functions](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/using-metric-math.html#metric-math-syntax) in the *Amazon CloudWatch User
Guide*.

Some of the parameters of this structure also have different uses whether you are
using this structure in a `GetMetricData` operation or a
`PutMetricAlarm` operation. These differences are explained in the
following parameter list.

### `Id` — string · **required**

A short name used to tie this object to the results in the response. This name must be
unique within a single call to `GetMetricData`. If you are performing math
expressions on this set of data, this name represents that data and can serve as a
variable in the mathematical expression. The valid characters are letters, numbers, and
underscore. The first character must be a lowercase letter.

### `MetricStat` — MetricStat

The metric to be returned, along with statistics, period, and units. Use this
parameter only if this object is retrieving a metric and not performing a math
expression on returned data.

Within one MetricDataQuery object, you must specify either `Expression` or
`MetricStat` but not both.

### `Expression` — string

This field can contain either a Metrics Insights query, or a metric math expression to
be performed on the returned data. For more information about Metrics Insights queries,
see [Metrics Insights query components and syntax](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/cloudwatch-metrics-insights-querylanguage) in the *Amazon
CloudWatch User Guide*.

A math expression can use the `Id` of the other metrics or queries to refer
to those metrics, and can also use the `Id` of other expressions to use the
result of those expressions. For more information about metric math expressions, see
[Metric Math Syntax and Functions](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/using-metric-math.html#metric-math-syntax) in the *Amazon CloudWatch User
Guide*.

Within each MetricDataQuery object, you must specify either `Expression` or
`MetricStat` but not both.

### `Label` — string

A human-readable label for this metric or expression. This is especially useful if
this is an expression, so that you know what the value represents. If the metric or
expression is shown in a CloudWatch dashboard widget, the label is shown. If Label is
omitted, CloudWatch generates a default.

You can put dynamic expressions into a label, so that it is more descriptive. For more
information, see [Using Dynamic
Labels](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/graph-dynamic-labels.html).

### `ReturnData` — boolean

When used in `GetMetricData`, this option indicates whether to return the
timestamps and raw data values of this metric. If you are performing this call just to
do math expressions and do not also need the raw data returned, you can specify
`false`. If you omit this, the default of `true` is
used.

When used in `PutMetricAlarm`, specify `true` for the one
expression result to use as the alarm. For all other metrics and expressions in the same
`PutMetricAlarm` operation, specify `ReturnData` as
False.

### `Period` — integer

The granularity, in seconds, of the returned data points. For metrics with regular
resolution, a period can be as short as one minute (60 seconds) and must be a multiple
of 60. For high-resolution metrics that are collected at intervals of less than one
minute, the period can be 1, 5, 10, 20, 30, 60, or any multiple of 60. High-resolution
metrics are those metrics stored by a `PutMetricData` operation that includes
a `StorageResolution of 1 second`.

### `AccountId` — string

The ID of the account where the metrics are located.

If you are performing a `GetMetricData` operation in a monitoring account,
use this to specify which account to retrieve this metric from.

If you are performing a `PutMetricAlarm` operation, use this to specify
which account contains the metric that the alarm is watching.

## MetricDataQueryDefinitionSummary (structure)

Summary information about a metric data query definition. To get the expression,
call `GetMetricDataQueryDefinition`.

### `Id` — string · **required**

The ID of the metric data query definition.

### `Path` — string · **required**

The path of the metric data query definition.

### `Type` — QueryType (enum) · **required**

The language of the expression. Valid values are the following:

- `PROMQL` – A PromQL query.
- `SQL` – A CloudWatch Metrics Insights query.
- `METRIC_MATH` – A metric math expression.

Values: `PROMQL`, `SQL`, `METRIC_MATH`

### `UpdatedAt` — timestamp

The date and time when you last updated the metric data query
definition.

## MetricDataResult (structure)

A `GetMetricData` call returns an array of `MetricDataResult`
structures. Each of these structures includes the data points for that metric, along
with the timestamps of those data points and other identifying information.

### `Id` — string

The short name you specified to represent this metric.

### `Label` — string

The human-readable label associated with the data.

### `Timestamps` — list<timestamp>

The timestamps for the data points, formatted in Unix timestamp format. The number of
timestamps always matches the number of values and the value for Timestamps[x] is
Values[x].

### `Values` — list<double>

The data points for the metric corresponding to `Timestamps`. The number of
values always matches the number of timestamps and the timestamp for Values[x] is
Timestamps[x].

### `StatusCode` — StatusCode (enum)

The status of the returned data. `Complete` indicates that all data points
in the requested time range were returned. `PartialData` means that an
incomplete set of data points were returned. You can use the `NextToken`
value that was returned and repeat your request to get more data points.
`NextToken` is not returned if you are performing a math expression.
`InternalError` indicates that an error occurred. Retry your request
using `NextToken`, if present.

Values: `Complete`, `InternalError`, `PartialData`, `Forbidden`

### `Messages` — list<MessageData>

A list of messages with additional information about the data returned.

## MetricDatum (structure)

Encapsulates the information sent to either create a metric or add new values to be
aggregated into an existing metric.

### `MetricName` — string · **required**

The name of the metric.

### `Dimensions` — list<Dimension>

The dimensions associated with the metric.

### `Timestamp` — timestamp

The time the metric data was received, expressed as the number of milliseconds
since Jan 1, 1970 00:00:00 UTC.

### `Value` — double

The value for the metric.

Although the parameter accepts numbers of type Double, CloudWatch rejects values
that are either too small or too large. Values must be in the range of -2^360 to 2^360.
In addition, special values (for example, NaN, +Infinity, -Infinity) are not
supported.

### `StatisticValues` — StatisticSet

The statistical values for the metric.

### `Values` — list<double>

Array of numbers representing the values for the metric during the period. Each unique
value is listed just once in this array, and the corresponding number in the
`Counts` array specifies the number of times that value occurred during
the period. You can include up to 150 unique values in each `PutMetricData`
action that specifies a `Values` array.

Although the `Values` array accepts numbers of type `Double`,
CloudWatch rejects values that are either too small or too large. Values must be in the
range of -2^360 to 2^360. In addition, special values (for example, NaN, +Infinity,
-Infinity) are not supported.

### `Counts` — list<double>

Array of numbers that is used along with the `Values` array. Each number in
the `Count` array is the number of times the corresponding value in the
`Values` array occurred during the period.

If you omit the `Counts` array, the default of 1 is used as the value for
each count. If you include a `Counts` array, it must include the same amount
of values as the `Values` array.

### `Unit` — StandardUnit (enum)

When you are using a `Put` operation, this defines what unit you want to
use when storing the metric.

In a `Get` operation, this displays the unit that is used for the
metric.

Values: `Seconds`, `Microseconds`, `Milliseconds`, `Bytes`, `Kilobytes`, `Megabytes`, `Gigabytes`, `Terabytes`, `Bits`, `Kilobits`, `Megabits`, `Gigabits`, `Terabits`, `Percent`, `Count`, `Bytes/Second`, `Kilobytes/Second`, `Megabytes/Second`, `Gigabytes/Second`, `Terabytes/Second`, `Bits/Second`, `Kilobits/Second`, `Megabits/Second`, `Gigabits/Second`, `Terabits/Second`, `Count/Second`, `None`

### `StorageResolution` — integer

Valid values are 1 and 60. Setting this to 1 specifies this metric as a
high-resolution metric, so that CloudWatch stores the metric with sub-minute resolution
down to one second. Setting this to 60 specifies this metric as a regular-resolution
metric, which CloudWatch stores at 1-minute resolution. Currently, high resolution is
available only for custom metrics. For more information about high-resolution metrics,
see [High-Resolution Metrics](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/publishingMetrics.html#high-resolution-metrics) in the *Amazon CloudWatch User
Guide*.

This field is optional, if you do not specify it the default of 60 is
used.

## MetricMathAnomalyDetector (structure)

Indicates the CloudWatch math expression that provides the time series the anomaly
detector uses as input. The designated math expression must return a single time
series.

### `MetricDataQueries` — list<MetricDataQuery>

An array of metric data query structures that enables you to create an anomaly
detector based on the result of a metric math expression. Each item in
`MetricDataQueries` gets a metric or performs a math expression. One item
in `MetricDataQueries` is the expression that provides the time series that
the anomaly detector uses as input. Designate the expression by setting
`ReturnData` to `true` for this object in the array. For all
other expressions and metrics, set `ReturnData` to `false`. The
designated expression must return a single time series.

## MetricStat (structure)

This structure defines the metric to be returned, along with the statistics, period,
and units.

### `Metric` — Metric · **required**

The metric to return, including the metric name, namespace, and dimensions.

### `Period` — integer · **required**

The granularity, in seconds, of the returned data points. For metrics with regular
resolution, a period can be as short as one minute (60 seconds) and must be a multiple
of 60. For high-resolution metrics that are collected at intervals of less than one
minute, the period can be 1, 5, 10, 20, 30, 60, or any multiple of 60. High-resolution
metrics are those metrics stored by a `PutMetricData` call that includes a
`StorageResolution` of 1 second.

If the `StartTime` parameter specifies a time stamp that is greater than
3 hours ago, you must specify the period as follows or no data points in that time range
is returned:

- Start time between 3 hours and 15 days ago - Use a multiple of 60 seconds
  (1 minute).
- Start time between 15 and 63 days ago - Use a multiple of 300 seconds (5
  minutes).
- Start time greater than 63 days ago - Use a multiple of 3600 seconds (1
  hour).

### `Stat` — string · **required**

The statistic to return. It can include any CloudWatch statistic or extended
statistic.

### `Unit` — StandardUnit (enum)

When you are using a `Put` operation, this defines what unit you want to
use when storing the metric.

In a `Get` operation, if you omit `Unit` then all data that
was collected with any unit is returned, along with the corresponding units that were
specified when the data was reported to CloudWatch. If you specify a unit, the operation
returns only data that was collected with that unit specified. If you specify a unit
that does not match the data collected, the results of the operation are null.
CloudWatch does not perform unit conversions.

Values: `Seconds`, `Microseconds`, `Milliseconds`, `Bytes`, `Kilobytes`, `Megabytes`, `Gigabytes`, `Terabytes`, `Bits`, `Kilobits`, `Megabits`, `Gigabits`, `Terabits`, `Percent`, `Count`, `Bytes/Second`, `Kilobytes/Second`, `Megabytes/Second`, `Gigabytes/Second`, `Terabytes/Second`, `Bits/Second`, `Kilobits/Second`, `Megabits/Second`, `Gigabits/Second`, `Terabits/Second`, `Count/Second`, `None`

## MetricStreamEntry (structure)

This structure contains the configuration information about one metric stream.

### `Arn` — string

The ARN of the metric stream.

### `CreationDate` — timestamp

The date that the metric stream was originally created.

### `LastUpdateDate` — timestamp

The date that the configuration of this metric stream was most recently
updated.

### `Name` — string

The name of the metric stream.

### `FirehoseArn` — string

The ARN of the Kinesis Firehose devlivery stream that is used for this metric
stream.

### `State` — string

The current state of this stream. Valid values are `running` and
`stopped`.

### `OutputFormat` — MetricStreamOutputFormat (enum)

The output format of this metric stream. Valid values are `json`,
`opentelemetry1.0`, and `opentelemetry0.7`.

Values: `json`, `opentelemetry0.7`, `opentelemetry1.0`

## MetricStreamFilter (structure)

This structure contains a metric namespace and optionally, a list of metric names, to
either include in a metric stream or exclude from a metric stream.

A metric stream's filters can include up to 1000 total names. This limit applies to
the sum of namespace names and metric names in the filters. For example, this could
include 10 metric namespace filters with 99 metrics each, or 20 namespace filters with
49 metrics specified in each filter.

### `Namespace` — string

The name of the metric namespace for this filter.

The namespace can contain only ASCII printable characters (ASCII range 32 through
126). It must contain at least one non-whitespace character.

### `MetricNames` — list<string>

The names of the metrics to either include or exclude from the metric stream.

If you omit this parameter, all metrics in the namespace are included or excluded,
depending on whether this filter is specified as an exclude filter or an include
filter.

Each metric name can contain only ASCII printable characters (ASCII range 32 through
126). Each metric name must contain at least one non-whitespace character.

## MetricStreamOutputFormat (enum)

Values: `json`, `opentelemetry0.7`, `opentelemetry1.0`

## MetricStreamStatisticsConfiguration (structure)

By default, a metric stream always sends the `MAX`, `MIN`,
`SUM`, and `SAMPLECOUNT` statistics for each metric that is
streamed. This structure contains information for one metric that includes additional
statistics in the stream. For more information about statistics, see CloudWatch,
listed in [CloudWatch statistics definitions](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/Statistics-definitions.html).

### `IncludeMetrics` — list<MetricStreamStatisticsMetric> · **required**

An array of metric name and namespace pairs that stream the additional statistics
listed in the value of the `AdditionalStatistics` parameter. There can be as
many as 100 pairs in the array.

All metrics that match the combination of metric name and namespace will be streamed
with the additional statistics, no matter their dimensions.

### `AdditionalStatistics` — list<string> · **required**

The list of additional statistics that are to be streamed for the metrics listed in
the `IncludeMetrics` array in this structure. This list can include as many
as 20 statistics.

If the `OutputFormat` for the stream is `opentelemetry1.0` or
`opentelemetry0.7`, the only valid values are
`p??` percentile statistics such as
`p90`, `p99` and so on.

If the `OutputFormat` for the stream is `json`, the valid values
include the abbreviations for all of the statistics listed in [CloudWatch statistics definitions](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/Statistics-definitions.html). For example, this includes
`tm98,`
`wm90`, `PR(:300)`, and so on.

## MetricStreamStatisticsMetric (structure)

This object contains the information for one metric that is to be streamed with
additional statistics.

### `Namespace` — string · **required**

The namespace of the metric.

### `MetricName` — string · **required**

The name of the metric.

## MuteTargets (structure)

Specifies which alarms an alarm mute rule applies to.

You can target up to 100 specific alarms by name. When a mute rule is active, the
targeted alarms continue to evaluate metrics and transition between states, but their
configured actions are muted.

### `AlarmNames` — list<string> · **required**

The list of alarm names that this mute rule targets. You can specify up to 100 alarm
names.

Each alarm name must be between 1 and 255 characters in length. The alarm names must
match existing alarms in your Amazon Web Services account and region.

## OTelEnrichmentMetricSelector (structure)

Selects the metrics in one namespace, for use in the `IncludeFilters` or
`ExcludeFilters` parameter of [StartOTelEnrichment](https://docs.aws.amazon.com/AmazonCloudWatch/latest/APIReference/API_StartOTelEnrichment.html) or [UpdateOTelEnrichment](https://docs.aws.amazon.com/AmazonCloudWatch/latest/APIReference/API_UpdateOTelEnrichment.html).

A maximum of 100 selectors is allowed across `IncludeFilters` and
`ExcludeFilters` combined.

### `Namespace` — string · **required**

The namespace of the metrics to select. Namespaces are matched exactly and are
case-sensitive.

### `MetricNames` — list<string>

The names of the metrics to select within the namespace. Metric names are matched
exactly and are case-sensitive. If this parameter is omitted, every metric in the
namespace is selected.

A maximum of 100 metric names is allowed for each selector.

## OTelEnrichmentStatus (enum)

The status of OTel enrichment for the account.

Values: `Running`, `Stopped`

## PartialFailure (structure)

This array is empty if the API operation was successful for all the rules specified in
the request. If the operation could not process one of the rules, the following data is
returned for each of those rules.

### `FailureResource` — string

The specified rule that could not be deleted.

### `ExceptionType` — string

The type of error.

### `FailureCode` — string

The code of the error.

### `FailureDescription` — string

A description of the error.

## QueryType (enum)

Values: `PROMQL`, `SQL`, `METRIC_MATH`

## Range (structure)

Specifies one range of days or times to exclude from use for training an anomaly
detection model.

### `StartTime` — timestamp · **required**

The start time of the range to exclude. The format is
`yyyy-MM-dd'T'HH:mm:ss`. For example,
`2019-07-01T23:59:59`.

### `EndTime` — timestamp · **required**

The end time of the range to exclude. The format is
`yyyy-MM-dd'T'HH:mm:ss`. For example,
`2019-07-01T23:59:59`.

## RecentlyActive (enum)

Values: `PT3H`

## ResourceMetricSelection (structure)

Specifies which metrics Amazon CloudWatch collects for a resource metrics
configuration. Include this in a [CreateResourceMetricsConfiguration](https://docs.aws.amazon.com/AmazonCloudWatch/latest/APIReference/API_CreateResourceMetricsConfiguration.html) or [UpdateResourceMetricsConfiguration](https://docs.aws.amazon.com/AmazonCloudWatch/latest/APIReference/API_UpdateResourceMetricsConfiguration.html) request to limit collection to a specific
set of metrics. If you omit metric selections, Amazon CloudWatch collects all
available detailed metrics for the resource.

### `IncludeMetrics` — list<string> · **required**

The names of the metrics to collect for the resource. Amazon CloudWatch collects
only the metrics that you list here.

## ResourceMetricsConfiguration (structure)

Represents a resource metrics configuration for an Amazon Web Services resource. A
resource metrics configuration enables detailed metric collection for the resource that
is identified by its Amazon Resource Name (ARN). Each Amazon Web Services resource can
have only one resource metrics configuration.

This structure is returned by the [CreateResourceMetricsConfiguration](https://docs.aws.amazon.com/AmazonCloudWatch/latest/APIReference/API_CreateResourceMetricsConfiguration.html), [UpdateResourceMetricsConfiguration](https://docs.aws.amazon.com/AmazonCloudWatch/latest/APIReference/API_UpdateResourceMetricsConfiguration.html), and [GetResourceMetricsConfiguration](https://docs.aws.amazon.com/AmazonCloudWatch/latest/APIReference/API_GetResourceMetricsConfiguration.html) operations.

### `ResourceArn` — string · **required**

The Amazon Resource Name (ARN) of the Amazon Web Services resource that this
configuration applies to.

### `CreatedAt` — timestamp · **required**

The date and time that the resource metrics configuration was created.

### `UpdatedAt` — timestamp · **required**

The date and time that the resource metrics configuration was last updated. When the
configuration is first created, this value is the same as
`CreatedAt`.

### `MetricSelections` — list<ResourceMetricSelection>

The metrics that Amazon CloudWatch collects for the resource. If this field is not
present, Amazon CloudWatch collects all available detailed metrics for the
resource.

## Rule (structure)

Defines the schedule configuration for an alarm mute rule.

The rule contains a schedule that specifies when and how long alarms should be muted.
The schedule can be a recurring pattern using cron expressions or a one-time mute window
using at expressions.

### `Schedule` — Schedule · **required**

The schedule configuration that defines when the mute rule activates and how long it
remains active.

## ScanBy (enum)

Values: `TimestampDescending`, `TimestampAscending`

## Schedule (structure)

Specifies when and how long an alarm mute rule is active.

The schedule uses either a cron expression for recurring mute windows or an at
expression for one-time mute windows. When the schedule activates, the mute rule mutes
alarm actions for the specified duration.

### `Expression` — string · **required**

The schedule expression that defines when the mute rule activates. The expression must
be between 1 and 256 characters in length.

You can use one of two expression formats:

- **Cron expressions** - For recurring mute
  windows. Format: `cron(Minutes Hours Day-of-month Month
  Day-of-week)`

  Examples:

  - `cron(0 2 * * *)` - Activates daily at 2:00 AM
  - `cron(0 2 * * SUN)` - Activates every Sunday at 2:00 AM for
    weekly system maintenance
  - `cron(0 1 1 * *)` - Activates on the first day of each
    month at 1:00 AM for monthly database maintenance
  - `cron(0 18 * * FRI)` - Activates every Friday at 6:00
    PM
  - `cron(0 23 * * *)` - Activates every day at 11:00 PM during
    nightly backup operations

  The characters `*`, `-`, and `,` are
  supported in all fields. English names can be used for the month (JAN-DEC) and
  day of week (SUN-SAT) fields.
- **At expressions** - For one-time mute windows.
  Format: `at(yyyy-MM-ddThh:mm)`

  Examples:

  - `at(2024-05-10T14:00)` - Activates once on May 10, 2024 at
    2:00 PM during an active incident response session
  - `at(2024-12-23T00:00)` - Activates once on December 23,
    2024 at midnight during annual company shutdown

### `Duration` — string · **required**

The length of time that alarms remain muted when the schedule activates. The duration
must be between 1 and 50 characters in length.

Specify the duration using ISO 8601 duration format with a minimum of 1 minute
(`PT1M`) and maximum of 15 days (`P15D`).

Examples:

- `PT4H` - 4 hours for weekly system maintenance
- `P2DT12H` - 2 days and 12 hours for weekend muting from Friday 6:00
  PM to Monday 6:00 AM
- `PT6H` - 6 hours for monthly database maintenance
- `PT2H` - 2 hours for nightly backup operations
- `P7D` - 7 days for annual company shutdown

The duration begins when the schedule expression time is reached. For recurring
schedules, the duration applies to each occurrence.

### `Timezone` — string

The time zone to use when evaluating the schedule expression. The time zone must be
between 1 and 50 characters in length.

Specify the time zone using standard timezone identifiers (for example,
`America/New_York`, `Europe/London`, or
`Asia/Tokyo`).

If you don't specify a time zone, UTC is used by default. The time zone affects how
cron and at expressions are interpreted, as well as start and expire dates you
specify

Examples:

- `America/New_York` - Eastern Time (US)
- `America/Los_Angeles` - Pacific Time (US)
- `Europe/London` - British Time
- `Asia/Tokyo` - Japan Standard Time
- `UTC` - Coordinated Universal Time

## ScheduleConfiguration (structure)

Contains the schedule expression and time-range offsets that define when a scheduled query runs and what time range each execution covers.

### `ScheduleExpression` — string · **required**

The schedule expression that defines how often the underlying CloudWatch Logs scheduled query runs. Specify a `rate()` expression, for example `rate(5 minutes)`.

### `StartTimeOffset` — long · **required**

The offset, in seconds, before the scheduled execution time at which the query time range begins. For example, an offset of 360 (6 minutes) on a query running at 12:05:00 starts the query time range at 11:59:00.

### `EndTimeOffset` — long

The offset, in seconds, before the scheduled execution time at which the query time range ends. Must be non-negative and less than `StartTimeOffset`. The default is 0.

## ScheduledQueryConfiguration (structure)

The configuration of the CloudWatch Logs scheduled query that backs a log alarm.

### `QueryString` — string · **required**

The CloudWatch Logs query to execute on each scheduled run. Length constraints: maximum of 10,000 characters.

### `LogGroupIdentifiers` — list<string>

The log groups to query. Each entry can be a log group name or ARN. Use the ARN form when querying log groups in a different account (for example, when running cross-account queries from a monitoring account). The list must contain between 1 and 50 entries.

### `QueryARN` — string

The Amazon Resource Name (ARN) of the CloudWatch Logs scheduled query that the alarm uses. This field is populated in `DescribeAlarms` responses.

### `ScheduledQueryRoleARN` — string · **required**

The Amazon Resource Name (ARN) of the IAM role that CloudWatch assumes when executing the scheduled query against the configured log groups.

### `ScheduleConfiguration` — ScheduleConfiguration · **required**

The schedule and time-range offset configuration for the underlying scheduled query.

### `AggregationExpression` — string · **required**

The expression that defines how to aggregate query results into one or more scalar values for alarm evaluation. For example, `count(*)` or `avg(latency) by host | sort desc`. Length constraints: minimum 1 character, maximum 2048 characters.

### `Tags` — list<Tag>

A list of key-value pairs to associate with the underlying scheduled query resource.

## SingleMetricAnomalyDetector (structure)

Designates the CloudWatch metric and statistic that provides the time series the
anomaly detector uses as input. If you have enabled unified cross-account observability,
and this account is a monitoring account, the metric can be in the same account or a
source account.

### `AccountId` — string

If the CloudWatch metric that provides the time series that the anomaly
detector uses as input is in another account, specify that account ID here. If you omit
this parameter, the current account is used.

### `Namespace` — string

The namespace of the metric to create the anomaly detection model for.

### `MetricName` — string

The name of the metric to create the anomaly detection model for.

### `Dimensions` — list<Dimension>

The metric dimensions to create the anomaly detection model for.

### `Stat` — string

The statistic to use for the metric and anomaly detection model.

## SlidingWindow (structure)

An evaluation window that advances each time the alarm is evaluated, forming a rolling
time window. This is the default evaluation window. A sliding window has no additional
configuration options.

Choose a sliding window when you need the fastest detection and the calendar
boundaries of the data don't matter, such as for continuous performance, latency, or
resource-exhaustion monitoring.

## StandardUnit (enum)

Values: `Seconds`, `Microseconds`, `Milliseconds`, `Bytes`, `Kilobytes`, `Megabytes`, `Gigabytes`, `Terabytes`, `Bits`, `Kilobits`, `Megabits`, `Gigabits`, `Terabits`, `Percent`, `Count`, `Bytes/Second`, `Kilobytes/Second`, `Megabytes/Second`, `Gigabytes/Second`, `Terabytes/Second`, `Bits/Second`, `Kilobits/Second`, `Megabits/Second`, `Gigabits/Second`, `Terabits/Second`, `Count/Second`, `None`

## StateValue (enum)

Values: `OK`, `ALARM`, `INSUFFICIENT_DATA`

## Statistic (enum)

Values: `SampleCount`, `Average`, `Sum`, `Minimum`, `Maximum`

## StatisticSet (structure)

Represents a set of statistics that describes a specific metric.

### `SampleCount` — double · **required**

The number of samples used for the statistic set.

### `Sum` — double · **required**

The sum of values for the sample set.

### `Minimum` — double · **required**

The minimum value of the sample set.

### `Maximum` — double · **required**

The maximum value of the sample set.

## StatusCode (enum)

Values: `Complete`, `InternalError`, `PartialData`, `Forbidden`

## Tag (structure)

A key-value pair associated with a CloudWatch resource.

### `Key` — string · **required**

A string that you can use to assign a value. The combination of tag keys and values
can help you organize and categorize your resources.

### `Value` — string · **required**

The value for the specified tag key.

## WallClockWindow (structure)

An evaluation window that aligns the evaluated range to fixed clock boundaries that
match the alarm's period, such as the top of the hour, midnight, or the start of the
calendar week, optionally in a specific time zone.

When you use a wall clock window, the alarm's period must be 1 minute (60 seconds),
5 minutes (300 seconds), 1 hour (3,600 seconds), 1 day (86,400 seconds), or 1 week
(604,800 seconds). Other period values aren't supported with a wall clock window.

Choose a wall clock window when your monitoring is tied to a business or calendar
period, such as daily reports, batch jobs, or backups, or when you want alarm
evaluations to match the periods shown on a metric dashboard.

### `Timezone` — string

The time zone to use when the alarm aligns the evaluation window to clock boundaries.
You can specify an IANA time zone name (for example, `America/New_York`), a
fixed UTC offset (for example, `+05:30`), or an offset-prefixed identifier
(for example, `UTC+05:30`). The offset must be aligned to a multiple of
5 minutes. If you don't specify a time zone, CloudWatch uses
`UTC`.

The time zone affects window alignment for all periods, including periods of one
hour or shorter.

## WarmUpConfiguration (structure)

The configuration settings that define the warm-up behavior for an alarm. Use these
settings to delay alarm evaluation after you create or update the alarm, which reduces
alarm noise while a new resource or service starts publishing data.

During the warm-up period, the alarm stays in `INSUFFICIENT_DATA` and
does not perform alarm actions.

### `WarmUpPeriodDurationInMinutes` — integer · **required**

The length of the warm-up period, in minutes. After you create or update the alarm,
the alarm stays in `INSUFFICIENT_DATA` for this duration. During this time,
the alarm does not perform alarm actions.

You can change this value at any time, including after the warm-up period ends. If
you change it after the warm-up period ends, the new value does not restart the
warm-up period.

### `OnlyStartEvaluatingAfterWarmUpPeriodEnds` — boolean

Specifies whether the alarm waits for the full warm-up period before it starts
to evaluate. The default is `false`. If `true`, the alarm waits
the entire `WarmUpPeriodDurationInMinutes` before it starts to evaluate, even
if metric data arrives earlier. If `false`, the alarm ends the warm-up period
early. Evaluation begins as soon as the alarm has enough metric data to fill its
evaluation window.
