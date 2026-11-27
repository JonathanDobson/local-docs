# Command-line switches: `chrome/windows_services/service_program/switches`

Generated from `chrome/windows_services/service_program/switches.h` in the Chromium source. Each switch is passed to the browser as `--name` or `--name=value`. The description is the source comment verbatim; *Condition* is the build/platform `#if` it is defined under.

3 switches.

## `--log-file-handle`

- Constant: `kLogFileHandle`

A switch conveying a handle value for the file to which the service should emit its logs.

## `--log-file-source`

- Constant: `kLogFileSource`

A switch conveying the PID of the process in which the log file handle value is valid.

## `--unattended-test`

- Constant: `kUnattendedTest`

A switch that indicates that the service is running on behalf of an unattended test (i.e., one for which CHROME_HEADLESS is set in its environment block).
