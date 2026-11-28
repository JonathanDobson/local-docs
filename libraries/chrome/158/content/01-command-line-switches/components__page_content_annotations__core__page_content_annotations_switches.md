# Command-line switches: `components/page_content_annotations/core/page_content_annotations_switches`

Generated from `components/page_content_annotations/core/page_content_annotations_switches.h` and `components/page_content_annotations/core/page_content_annotations_switches.cc` in the Chromium source. Each switch is passed to the browser as `--name` or `--name=value`. The description is the source comment verbatim; *Condition* is the build/platform `#if` it is defined under.

6 switches.

## `--enable-page-content-annotations-logging`

- Constant: `kPageContentAnnotationsLoggingEnabled`

_No description in the source._

## `--page-content-annotations-validation-startup-delay-seconds`

- Constant: `kPageContentAnnotationsValidationStartupDelaySeconds`

_No description in the source._

## `--page-content-annotations-validation-batch-size`

- Constant: `kPageContentAnnotationsValidationBatchSizeOverride`

_No description in the source._

## `--page-content-annotations-validation-content-visibility`

- Constant: `kPageContentAnnotationsValidationContentVisibility`

Enables the specific annotation type to run validation at startup after a delay. A comma separated list of inputs can be given as a value which will be used as input for the validation job.

## `--page-content-annotations-validation-write-to-file`

- Constant: `kPageContentAnnotationsValidationWriteToFile`

Writes the output of page content annotation validations to the given file.

## `--page-content-annotations-skip-fcp-wait-for-testing`

- Constant: `kPageContentAnnotationsSkipFCPWaitForTesting`

If enabled, page content annotations requests will not wait for FCP.
