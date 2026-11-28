# Command-line switches: `components/metrics/metrics_switches`

Generated from `components/metrics/metrics_switches.h` and `components/metrics/metrics_switches.cc` in the Chromium source. Each switch is passed to the browser as `--name` or `--name=value`. The description is the source comment verbatim; *Condition* is the build/platform `#if` it is defined under.

10 switches.

## `--export-uma-logs-to-file`

- Constant: `kExportUmaLogsToFile`

Enables the observing of all UMA logs created during the session and automatically exports them to the passed file path on shutdown (the file is created if it does not already exist). This also enables viewing all UMA logs in the chrome://metrics-internals debug page. The format of the exported file is outlined in MetricsServiceObserver::ExportLogsAsJson(). Example usage: --export-uma-logs-to-file=/tmp/logs.json

## `--export-ukm-logs-to-file`

- Constant: `kExportUkmLogsToFile`

Enables the observing of all UKM logs created during the session and automatically exports them to the passed file path on shutdown (the file is created if it does not already exist). This also enables viewing all UKM logs in the chrome://metrics-internals debug page. The format of the exported file is outlined in MetricsServiceObserver::ExportLogsAsJson(). Example usage: --export-ukm-logs-to-file=/tmp/logs.json

## `--force-enable-metrics-reporting`

- Constant: `kForceEnableMetricsReporting`

Forces metrics reporting to be enabled. Should not be used for tests as it will send data to servers.

## `--force-msbb-setting-on-for-ukm`

- Constant: `kForceMsbbSettingOnForUkm`

Forces MSBB setting to be on for UKM recording. Should only be used in automated testing browser sessions in which it is infeasible or impractical to toggle the setting manually.

## `--metrics-recording-only`

- Constant: `kMetricsRecordingOnly`

Enables the recording of metrics reports but disables reporting. In contrast to kForceEnableMetricsReporting, this executes all the code that a normal client would use for reporting, except the report is dropped rather than sent to the server. This is useful for finding issues in the metrics code during UI and performance tests.

## `--metrics-upload-interval`

- Constant: `kMetricsUploadIntervalSec`

Override the standard time interval between each metrics report upload for UMA and UKM. It is useful to set to a short interval for debugging. Unit in seconds. (The default is 1800 seconds on desktop).

## `--reset-variation-state`

- Constant: `kResetVariationState`

Forces a reset of the one-time-randomized FieldTrials on this client, also known as the Chrome Variations state.

## `--ukm-server-url`

- Constant: `kUkmServerUrl`

Overrides the URL of the server that UKM reports are uploaded to. This can only be used in debug builds.

## `--uma-insecure-server-url`

- Constant: `kUmaInsecureServerUrl`

Overrides the URL of the server that UMA reports are uploaded to when the connection to the default secure URL fails (see |kUmaServerUrl|). This can only be used in debug builds.

## `--uma-server-url`

- Constant: `kUmaServerUrl`

Overrides the URL of the server that UMA reports are uploaded to. This can only be used in debug builds.
