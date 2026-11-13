# Amazon CloudWatch — API reference

API version `2010-08-01` · protocol awsJson1_0, awsQuery, awsQueryCompatible · SDK for JavaScript v3 client `@aws-sdk/client-cloudwatch`

Amazon CloudWatch enables you to publish, monitor, and manage various metrics, as well
as configure alarm actions based on data from metrics. This guide provides detailed
information about CloudWatch actions, data types, parameters, and errors. For
more information about CloudWatch features, see [Amazon CloudWatch](https://aws.amazon.com/cloudwatch) and the
*Amazon CloudWatch User Guide*.

For information about the metrics that other Amazon Web Services products send to
CloudWatch, see the [Amazon CloudWatch
Metrics and Dimensions Reference](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/aws-services-cloudwatch-metrics.html) in the *Amazon CloudWatch User
Guide*.

Use the following links to get started using the CloudWatch Query API:

: An alphabetical list of all CloudWatch
actions.

: An alphabetical list of all CloudWatch data
types.

CommonParameters: Parameters that all Query actions can use.

CommonErrors: Client and server errors that all actions can
return.

[Regions and Endpoints](https://docs.aws.amazon.com/general/latest/gr/rande.html#cw_region): Supported regions and endpoints for all Amazon Web
Services products.

Alternatively, you can use one of the [Amazon Web Services SDKs](https://aws.amazon.com/tools/#sdk) to access CloudWatch using an API tailored
to your programming language or platform.

Developers in the Amazon Web Services developer community also provide their own
libraries, which you can find at the following Amazon Web Services developer
centers:

[Java Developer Center](http://aws.amazon.com/java/)

[JavaScript Developer
Center](http://aws.amazon.com/javascript/)

[Amazon Web Services Mobile
Services](http://aws.amazon.com/mobile/)

[PHP Developer Center](http://aws.amazon.com/php/)

[Python Developer Center](http://aws.amazon.com/python/)

[Ruby Developer Center](http://aws.amazon.com/ruby/)

[Windows and .NET Developer
Center](http://aws.amazon.com/net/)

## Operations (59)

- [`AssociateDatasetKmsKey`](operations/AssociateDatasetKmsKey.md) — Associates an Amazon Web Services Key Management Service (Amazon Web Services KMS) customer managed key with the specified dataset.
- [`CreateResourceMetricsConfiguration`](operations/CreateResourceMetricsConfiguration.md) — Creates a resource metrics configuration for an Amazon Web Services resource.
- [`DeleteAlarmMuteRule`](operations/DeleteAlarmMuteRule.md) — Deletes a specific alarm mute rule.
- [`DeleteAlarms`](operations/DeleteAlarms.md) — Deletes the specified alarms.
- [`DeleteAnomalyDetector`](operations/DeleteAnomalyDetector.md) — Deletes the specified anomaly detection model from your account.
- [`DeleteDashboards`](operations/DeleteDashboards.md) — Deletes all dashboards that you specify.
- [`DeleteInsightRules`](operations/DeleteInsightRules.md) — Permanently deletes the specified Contributor Insights rules.
- [`DeleteMetricDataQueryDefinition`](operations/DeleteMetricDataQueryDefinition.md) — Deletes a metric data query definition.
- [`DeleteMetricStream`](operations/DeleteMetricStream.md) — Permanently deletes the metric stream that you specify.
- [`DeleteResourceMetricsConfiguration`](operations/DeleteResourceMetricsConfiguration.md) — Deletes the resource metrics configuration for an Amazon Web Services resource.
- [`DescribeAlarmContributors`](operations/DescribeAlarmContributors.md) — Returns the information of the current alarm contributors that are in `ALARM` state.
- [`DescribeAlarmHistory`](operations/DescribeAlarmHistory.md) — Retrieves the history for the specified alarm.
- [`DescribeAlarms`](operations/DescribeAlarms.md) — Retrieves the specified alarms.
- [`DescribeAlarmsForMetric`](operations/DescribeAlarmsForMetric.md) — Retrieves the alarms for the specified metric.
- [`DescribeAnomalyDetectors`](operations/DescribeAnomalyDetectors.md) — Lists the anomaly detection models that you have created in your account.
- [`DescribeInsightRules`](operations/DescribeInsightRules.md) — Returns a list of all the Contributor Insights rules in your account.
- [`DisableAlarmActions`](operations/DisableAlarmActions.md) — Disables the actions for the specified alarms.
- [`DisableInsightRules`](operations/DisableInsightRules.md) — Disables the specified Contributor Insights rules.
- [`DisassociateDatasetKmsKey`](operations/DisassociateDatasetKmsKey.md) — Removes the customer managed Amazon Web Services Key Management Service (Amazon Web Services KMS) key association from the specified dataset.
- [`EnableAlarmActions`](operations/EnableAlarmActions.md) — Enables the actions for the specified alarms.
- [`EnableInsightRules`](operations/EnableInsightRules.md) — Enables the specified Contributor Insights rules.
- [`GetAlarmMuteRule`](operations/GetAlarmMuteRule.md) — Retrieves details for a specific alarm mute rule.
- [`GetDashboard`](operations/GetDashboard.md) — Displays the details of the dashboard that you specify.
- [`GetDataset`](operations/GetDataset.md) — Returns information about the specified dataset.
- [`GetInsightRuleReport`](operations/GetInsightRuleReport.md) — This operation returns the time series data collected by a Contributor Insights rule.
- [`GetMetricData`](operations/GetMetricData.md) — You can use the `GetMetricData` API to retrieve CloudWatch metric values.
- [`GetMetricDataQueryDefinition`](operations/GetMetricDataQueryDefinition.md) — Returns a metric data query definition, including its expression.
- [`GetMetricStatistics`](operations/GetMetricStatistics.md) — Gets statistics for the specified metric.
- [`GetMetricStream`](operations/GetMetricStream.md) — Returns information about the metric stream that you specify.
- [`GetMetricWidgetImage`](operations/GetMetricWidgetImage.md) — You can use the `GetMetricWidgetImage` API to retrieve a snapshot graph of one or more Amazon CloudWatch metrics as a bitmap image.
- [`GetOTelEnrichment`](operations/GetOTelEnrichment.md) — Returns the current status of vended metric enrichment for the account, including whether CloudWatch vended metrics are enriched with resource ARN and resource tag labels and queryable using PromQL.
- [`GetResourceMetricsConfiguration`](operations/GetResourceMetricsConfiguration.md) — Retrieves the current resource metrics configuration for an Amazon Web Services resource.
- [`ListAlarmMuteRules`](operations/ListAlarmMuteRules.md) — Lists alarm mute rules in your Amazon Web Services account and region.
- [`ListDashboards`](operations/ListDashboards.md) — Returns a list of the dashboards for your account.
- [`ListManagedInsightRules`](operations/ListManagedInsightRules.md) — Returns a list that contains the number of managed Contributor Insights rules in your account.
- [`ListMetricDataQueryDefinitions`](operations/ListMetricDataQueryDefinitions.md) — Lists the metric data query definitions in your account and Region.
- [`ListMetricStreams`](operations/ListMetricStreams.md) — Returns a list of metric streams in this account.
- [`ListMetrics`](operations/ListMetrics.md) — List the specified metrics.
- [`ListTagsForResource`](operations/ListTagsForResource.md) — Displays the tags associated with a CloudWatch resource.
- [`PutAlarmMuteRule`](operations/PutAlarmMuteRule.md) — Creates or updates an alarm mute rule.
- [`PutAnomalyDetector`](operations/PutAnomalyDetector.md) — Creates an anomaly detection model for a CloudWatch metric.
- [`PutCompositeAlarm`](operations/PutCompositeAlarm.md) — Creates or updates a *composite alarm*.
- [`PutDashboard`](operations/PutDashboard.md) — Creates a dashboard if it does not already exist, or updates an existing dashboard.
- [`PutInsightRule`](operations/PutInsightRule.md) — Creates a Contributor Insights rule.
- [`PutLogAlarm`](operations/PutLogAlarm.md) — Creates or updates a log alarm.
- [`PutManagedInsightRules`](operations/PutManagedInsightRules.md) — Creates a managed Contributor Insights rule for a specified Amazon Web Services resource.
- [`PutMetricAlarm`](operations/PutMetricAlarm.md) — Creates or updates an alarm and associates it with the specified metric, metric math expression, anomaly detection model, Metrics Insights query, or PromQL query.
- [`PutMetricData`](operations/PutMetricData.md) — Publishes metric data to Amazon CloudWatch.
- [`PutMetricDataQueryDefinition`](operations/PutMetricDataQueryDefinition.md) — Creates or updates a metric data query definition.
- [`PutMetricStream`](operations/PutMetricStream.md) — Creates or updates a metric stream.
- [`SetAlarmState`](operations/SetAlarmState.md) — Temporarily sets the state of an alarm for testing purposes.
- [`StartMetricStreams`](operations/StartMetricStreams.md) — Starts the streaming of metrics for one or more of your metric streams.
- [`StartOTelEnrichment`](operations/StartOTelEnrichment.md) — Enables enrichment and PromQL access for CloudWatch vended metrics for [supported Amazon Web Services resources](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/UsingResourceTagsForTel…
- [`StopMetricStreams`](operations/StopMetricStreams.md) — Stops the streaming of metrics for one or more of your metric streams.
- [`StopOTelEnrichment`](operations/StopOTelEnrichment.md) — Disables enrichment and PromQL access for CloudWatch vended metrics for [supported Amazon Web Services resources](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/UsingResourceTagsForTe…
- [`TagResource`](operations/TagResource.md) — Assigns one or more tags (key-value pairs) to the specified CloudWatch resource.
- [`UntagResource`](operations/UntagResource.md) — Removes one or more tags from the specified resource.
- [`UpdateOTelEnrichment`](operations/UpdateOTelEnrichment.md) — Replaces the filters that determine which CloudWatch vended metrics are enriched with resource ARN and resource tag labels for the account.
- [`UpdateResourceMetricsConfiguration`](operations/UpdateResourceMetricsConfiguration.md) — Updates the resource metrics configuration for an Amazon Web Services resource.
