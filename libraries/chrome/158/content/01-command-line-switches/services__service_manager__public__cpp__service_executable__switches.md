# Command-line switches: `services/service_manager/public/cpp/service_executable/switches`

Generated from `services/service_manager/public/cpp/service_executable/switches.h` and `services/service_manager/public/cpp/service_executable/switches.cc` in the Chromium source. Each switch is passed to the browser as `--name` or `--name=value`. The description is the source comment verbatim; *Condition* is the build/platform `#if` it is defined under.

2 switches.

## `--service-name`

- Constant: `kServiceName`

All switches in alphabetical order. The switches should be documented alongside the definition of their values in the .cc file. Indicates the name of the service to run. Useful for debugging, or if a service executable is built to support being run as a number of potential different services.

## `--service-request-attachment-name`

- Constant: `kServiceRequestAttachmentName`

The name of the |mojo::PendingReceiver<service_manager::mojom::Service>| message pipe handle that is attached to the incoming Mojo invitation received by the service.
