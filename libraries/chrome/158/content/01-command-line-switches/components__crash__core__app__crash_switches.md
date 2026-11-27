# Command-line switches: `components/crash/core/app/crash_switches`

Generated from `components/crash/core/app/crash_switches.h` and `components/crash/core/app/crash_switches.cc` in the Chromium source. Each switch is passed to the browser as `--name` or `--name=value`. The description is the source comment verbatim; *Condition* is the build/platform `#if` it is defined under.

3 switches.

## `--crashpad-handler`

- Constant: `kCrashpadHandler`

A process type (switches::kProcessType) that indicates chrome.exe or setup.exe is being launched as crashpad_handler. This is only used on Windows. We bundle the handler into chrome.exe on Windows because there is high probability of a "new" .exe being blocked or interfered with by application firewalls, AV software, etc. On other platforms, crashpad_handler is a standalone executable.

## `--crashpad-handler-pid`

- Constant: `kCrashpadHandlerPid`
- Condition: `BUILDFLAG(IS_LINUX) || BUILDFLAG(IS_CHROMEOS)`

The process ID of the Crashpad handler.

## `--crash-loop-before`

- Constant: `kCrashLoopBefore`
- Condition: `BUILDFLAG(IS_CHROMEOS)`

A time_t. Passed by session_manager into the Chrome user session, indicating that if Chrome crashes before the indicated time, session_manager will consider this to be a crash-loop situation and log the user out. Chrome mostly just passes this to crash_reporter if it crashes.
