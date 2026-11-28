# Command-line switches: `services/webnn/webnn_switches`

Generated from `services/webnn/webnn_switches.h` and `services/webnn/webnn_switches.cc` in the Chromium source. Each switch is passed to the browser as `--name` or `--name=value`. The description is the source comment verbatim; *Condition* is the build/platform `#if` it is defined under.

17 switches.

## `--webnn-coreml-dump-model`

- Constant: `kWebNNCoreMlDumpModel`
- Condition: `BUILDFLAG(IS_MAC)`

Copy the generated Core ML model to the folder specified by --webnn-coreml-dump-model, note: folder needs to be accessible from the GPU sandbox or use --no-sandbox. Usage: --no-sandbox --webnn-coreml-dump-model=/tmp/CoreMLModels

## `--webnn-tflite-dump-model`

- Constant: `kWebNNTfliteDumpModel`
- Condition: `BUILDFLAG(WEBNN_USE_TFLITE) || BUILDFLAG(WEBNN_USE_LITERT)`

Save the generated TFLite model file to the folder specified by --webnn-tflite-dump-model. Note, the folder needs to be accessible from the GPU process sandbox or --no-sandbox must be used. Usage: --no-sandbox --webnn-tflite-dump-model=/tmp/tflite_models

## `--webnn-ort-logging-level`

- Constant: `kWebNNOrtLoggingLevel`
- Condition: `BUILDFLAG(IS_WIN)`

Configure the logging severity level of ONNX Runtime. Usage: --webnn-ort-logging-level=VERBOSE Other severity levels could be "INFO", "WARNING", "ERROR" (default), and "FATAL".

## `--webnn-ort-dump-model`

- Constant: `kWebNNOrtDumpModel`
- Condition: `BUILDFLAG(IS_WIN)`

Set the folder specified by --webnn-ort-dump-model for ONNX Runtime to save optimized models after graph level transformations. By default, ORT saves the optimized ONNX model. Some EPs (e.g., OpenVINO) dump their own IR models via a session config entry specified by `EpInfo::model_dump_config_key` instead. Usage: --no-sandbox --webnn-ort-dump-model=/tmp/ort_models

## `--webnn-ort-library-path-for-testing`

- Constant: `kWebNNOrtLibraryPathForTesting`
- Condition: `BUILDFLAG(IS_WIN)`

Force onnxruntime.dll to be loaded from a location specified by the switch for testing development ORT build. This switch is not to be used in shipping scenarios and is ignored by default. Usage: --webnn-ort-library-path-for-testing="C:\Program Files\ONNXRuntime" --allow-third-party-modules

## `--webnn-ort-ep-library-path-for-testing`

- Constant: `kWebNNOrtEpLibraryPathForTesting`
- Condition: `BUILDFLAG(IS_WIN)`

Specify one or more ORT EP name and library path pairs via this switch for testing development EP builds. Libraries of each ORT EP specified by the EP name are forced to be loaded from the specified path. This switch is not to be used in shipping scenarios and is ignored by default. Each pair should be in the format <ep_name>?<ep_library_path>, and multiple pairs are separated by ",", e.g. <ep_name1>?<ep_library_path1>,<ep_name2>?<ep_library_path2>. Library paths must not contain ",". Each EP name may only appear once. Any invalid pair disables the whole switch. Usage: --webnn-ort-ep-library-path-for-testing="OpenVINOExecutionProvider?C:\Program Files\ONNXRuntime-EP\onnxruntime_providers_openvino_plugin.dll, WebGpuExecutionProvider?C:\Program Files\ONNXRuntime-EP\onnxruntime_providers_webgpu.dll" --allow-third-party-modules

## `--webnn-ort-ep-device`

- Constant: `kWebNNOrtEpDevice`
- Condition: `BUILDFLAG(IS_WIN)`

Force ONNX Runtime to only select one specific execution provider (EP) device which matches the given EP name, hardware vendor id and hardware device id for WebNN during the ORT session creation stage. Notes: 1. Available EP devices can be queried in logs when the `webnn-ort-logging-level` is set to `VERBOSE` or `INFO`. If no matching device is found, the ORT session creation fails. 2. The CPU fallback EP device is added implicitly in ORT by default unless disabled explicitly by `webnn-ort-disable-cpu-fallback` switch.  The value should be in the format: <ep_name>,<hardware_vendor_id>,<hardware_device_id> Please note that all the entries must be provided in order, and both hardware_vendor_id and hardware_device_id are hexadecimal strings.  Usage: For example, specifying an Intel GPU device using OpenVINO EP: --webnn-ort-ep-device=OpenVINOExecutionProvider,0x8086,0x4680

## `--webnn-ort-session-config-entries-for-testing`

- Constant: `kWebNNOrtSessionConfigEntriesForTesting`
- Condition: `BUILDFLAG(IS_WIN)`

Add arbitrary ONNX Runtime session configuration entries for testing. The value must use the format <key>,<value>[,<key>,<value>...]. Like other testing switches, this is available in release builds and must only be supplied through a trusted startup command line. Existing session configuration entries, including dispatch security settings, cannot be replaced. Usage: --webnn-ort-session-config-entries-for-testing= ep.qnnexecutionprovider.webnn_scenario,1,key2,value2

## `--webnn-ort-ignore-ep-blocklist`

- Constant: `kWebNNOrtIgnoreEpBlocklist`
- Condition: `BUILDFLAG(IS_WIN)`

Enable all execution providers, ignoring the enabled flag blocklist.

## `--webnn-ort-ignore-ihv-eps`

- Constant: `kWebNNOrtIgnoreIhvEps`
- Condition: `BUILDFLAG(IS_WIN)`

Ignore all IHV execution providers, only the default CPUExecutionProvider and DmlExecutionProvider will be used.

## `--webnn-ort-disable-virtual-devices`

- Constant: `kWebNNOrtDisableVirtualDevices`
- Condition: `BUILDFLAG(IS_WIN)`

Disable ORT virtual devices in the Compiler process, requiring actual hardware devices for compilation instead. This switch is for testing only. Note that online compilation requires access to actual hardware which is blocked by the compiler sandbox, so this switch is usually used together with `--disable-webnn-compiler-sandbox`.

## `--webnn-ort-allow-all-compiler-devices`

- Constant: `kWebNNOrtAllowAllCompilerDevices`
- Condition: `BUILDFLAG(IS_WIN)`

Allow all EP devices to be selected for the Compiler process, regardless of whether `kKnownEPs` declares offline compilation support for them. For testing only.

## `--webnn-ort-graph-optimization-level`

- Constant: `kWebNNOrtGraphOptimizationLevel`
- Condition: `BUILDFLAG(IS_WIN)`

Configure the graph optimization level of ONNX Runtime. Usage: --webnn-ort-graph-optimization-level=DISABLE_ALL Other levels could be "BASIC", "EXTENDED" and "ALL".

## `--webnn-ort-enable-profiling`

- Constant: `kWebNNOrtEnableProfiling`
- Condition: `BUILDFLAG(IS_WIN)`

This switch allows us to collect ORT profile data for performance analysis. The profile data file is generated in Chrome's folder with a fixed naming format "prefix_date_time.json". The prefix can be provided by user or use "WebNNOrtProfile" as default. Usage: --no-sandbox --webnn-ort-enable-profiling="WebNNOrtOvCpuProfile"

## `--webnn-ort-disable-cpu-fallback`

- Constant: `kWebNNOrtDisableCpuFallback`
- Condition: `BUILDFLAG(IS_WIN)`

This switch allows us to disable the fallback to default ORT CPU EP which is enabled by default. When this switch is set: 1. ORT session creation fails if non-CPU EPs cannot fully support all graph nodes. 2. Disables OpenVINO EP internal CPU fallback if NPU model compilation fails (for debugging). Usage: --webnn-ort-disable-cpu-fallback

## `--webnn-compiler-ep-library`

- Constant: `kWebNNCompilerEpLibrary`
- Condition: `BUILDFLAG(IS_WIN)`

Used internally to pass the target EP library path from the browser process to the WebNN Compiler utility process. The compiler process reads this switch during PreSandboxInit() to load the EP libraries before sandbox lockdown.

## `--webnn-compiler-ep-device-info`

- Constant: `kWebNNCompilerEpDeviceInfo`
- Condition: `BUILDFLAG(IS_WIN)`

Used internally to pass the target EP device info from the browser process to the WebNN Compiler utility process, alongside `kWebNNCompilerEpLibrary`. The compiler process parses this switch during PreSandboxInit() to register the correct EP device before sandbox lockdown. The value is produced by webnn::EpDeviceInfo::ToSwitchValue().
