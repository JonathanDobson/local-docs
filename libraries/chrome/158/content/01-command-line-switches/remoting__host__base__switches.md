# Command-line switches: `remoting/host/base/switches`

Generated from `remoting/host/base/switches.h` and `remoting/host/base/switches.cc` in the Chromium source. Each switch is passed to the browser as `--name` or `--name=value`. The description is the source comment verbatim; *Condition* is the build/platform `#if` it is defined under.

37 switches.

## `--elevate`

- Constant: `kElevateSwitchName`

"--elevate=<binary>" requests |binary| to be launched elevated (possibly causing a UAC prompt).

## `--help`

- Constant: `kHelpSwitchName`

"--help" prints the usage message.

## `--type`

- Constant: `kProcessTypeSwitchName`

Used to specify the type of the process. kProcessType* constants specify possible values.

## `--?`

- Constant: `kQuestionSwitchName`

"--?" prints the usage message.

## `--version`

- Constant: `kVersionSwitchName`

The command line switch used to get version of the daemon.

## `--controller`

- Constant: `kProcessTypeController`

Values for kProcessTypeSwitchName.

## `--daemon`

- Constant: `kProcessTypeDaemon`

_No description in the source._

## `--desktop`

- Constant: `kProcessTypeDesktop`

_No description in the source._

## `--network`

- Constant: `kProcessTypeNetwork`

_No description in the source._

## `--peer_connection`

- Constant: `kProcessTypePeerConnection`

_No description in the source._

## `--single_process_host`

- Constant: `kProcessTypeSingleProcessHost`

_No description in the source._

## `--rdp_desktop_session`

- Constant: `kProcessTypeRdpDesktopSession`

_No description in the source._

## `--evaluate_capability`

- Constant: `kProcessTypeEvaluateCapability`

_No description in the source._

## `--file_chooser`

- Constant: `kProcessTypeFileChooser`

_No description in the source._

## `--url_forwarder_configurator`

- Constant: `kProcessTypeUrlForwarderConfigurator`

_No description in the source._

## `--xsession_chooser`

- Constant: `kProcessTypeXSessionChooser`
- Condition: `BUILDFLAG(IS_LINUX) || BUILDFLAG(IS_CHROMEOS)`

_No description in the source._

## `--evaluate-type`

- Constant: `kEvaluateCapabilitySwitchName`

_No description in the source._

## `--enable-wtmpdb`

- Constant: `kEnableWtmpdb`
- Condition: `BUILDFLAG(IS_LINUX)`

Used to record client sessions to wtmpd.

## `--crashpad-handler-socket-fd`

- Constant: `kCrashpadHandlerSocketFd`
- Condition: `BUILDFLAG(IS_LINUX)`

Used to pass inherited Crashpad handler socket descriptor and PID.

## `--crashpad-handler-pid`

- Constant: `kCrashpadHandlerPid`
- Condition: `BUILDFLAG(IS_LINUX)`

_No description in the source._

## `--enable-corp-messaging`

- Constant: `kEnableCorpMessaging`

Indicates whether Corp Messaging should be enabled for signaling.

## `--d3d-support`

- Constant: `kEvaluateD3D`
- Condition: `BUILDFLAG(IS_WIN)`

Executes EvaluateD3D() function.

## `--3d-display-mode`

- Constant: `kEvaluate3dDisplayMode`
- Condition: `BUILDFLAG(IS_WIN)`

Executes Evaluate3dDisplayMode() function.

## `--setup`

- Constant: `kSetUpUrlForwarderSwitchName`
- Condition: `BUILDFLAG(IS_WIN)`

Used in combination with |kProcessTypeUrlForwarderConfigurator| to set up the URL forwarder on Windows.

## `--parent-window`

- Constant: `kParentWindowSwitchName`

Used to pass the HWND for the parent process to a child process.

## `--input`

- Constant: `kInputSwitchName`

Name of the pipe used to communicate from the parent to the child process.

## `--output`

- Constant: `kOutputSwitchName`

Name of the pipe used to communicate from the child to the parent process.

## `--mojo-pipe-token`

- Constant: `kMojoPipeToken`

Token used to create a message pipe between a pair of child and parent processes.

## `--crash-server-pipe-handle`

- Constant: `kCrashServerPipeHandle`

A server pipe handle used by the child process to initialize crash reporting.

## `--use-peer-connection-process`

- Constant: `kUsePeerConnectionProcessSwitch`
- Condition: `BUILDFLAG(IS_WIN)`

TODO(crbug.com/502281489): Remove this switch once the PC process is enabled by default. Specifies whether to use the dedicated Peer Connection process.

## `--check-permission`

- Constant: `kCheckPermissionSwitchName`
- Condition: `BUILDFLAG(IS_APPLE)`

NativeMessagingHost switch to check for required OS permissions and request them if necessary.

## `--check-accessibility-permission`

- Constant: `kCheckAccessibilityPermissionSwitchName`
- Condition: `BUILDFLAG(IS_APPLE)`

Command line switch to check for Accessibility permission.

## `--check-screen-recording-permission`

- Constant: `kCheckScreenRecordingPermissionSwitchName`
- Condition: `BUILDFLAG(IS_APPLE)`

Command line switch to check for Screen Recording permission.

## `--list-audio-devices`

- Constant: `kListAudioDevicesSwitchName`
- Condition: `BUILDFLAG(IS_APPLE)`

Command line switch to list all audio devices and their UID.

## `--agent-status`

- Constant: `kAgentStatusSwitchName`

Reports the AI agent state to the running host via Mojo IPC.

## `--terminal-id`

- Constant: `kTerminalIdSwitchName`

Specifies the terminal ID associated with `--agent-status` or `--terminal-title`.

## `--terminal-title`

- Constant: `kTerminalTitleSwitchName`

Sets the title of the terminal tab via Mojo IPC.
