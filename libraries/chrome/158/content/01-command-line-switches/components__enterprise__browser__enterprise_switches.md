# Command-line switches: `components/enterprise/browser/enterprise_switches`

Generated from `components/enterprise/browser/enterprise_switches.h` and `components/enterprise/browser/enterprise_switches.cc` in the Chromium source. Each switch is passed to the browser as `--name` or `--name=value`. The description is the source comment verbatim; *Condition* is the build/platform `#if` it is defined under.

1 switches.

## `--enable-chrome-browser-cloud-management`

- Constant: `kEnableChromeBrowserCloudManagement`
- Condition: `!BUILDFLAG(IS_CHROMEOS)`

Enables the Chrome Browser Cloud Management integration on Chromium builds. CBCM is always enabled in branded builds.
