# Command-line switches: `components/actor/core/actor_switches`

Generated from `components/actor/core/actor_switches.h` and `components/actor/core/actor_switches.cc` in the Chromium source. Each switch is passed to the browser as `--name` or `--name=value`. The description is the source comment verbatim; *Condition* is the build/platform `#if` it is defined under.

6 switches.

## `--disable-actor-safety-checks`

- Constant: `kDisableActorSafetyChecks`

Bypasses several of the actor's safety checks, such as requiring SafeBrowsing to be enabled and the blocklist. Note that some checks, like requiring https, are not affected by this.

## `--attempt-form-filling-tool-skips-ui`

- Constant: `kAttemptFormFillingToolSkipsUI`

Bypasses the selection of the data to be filled by the `AttemptFormFillingTool` and just picks the first suggestion for each form section. This is only intended for testing.

## `--attempt-otp-filling-tool-mock-value-skips-checks`

- Constant: `kAttemptOtpFillingToolMockValueSkipsChecks`

Supplies a mock OTP value for the `AttemptOtpFillingTool` and bypasses Google Account consent fetching, opt-in dialogs, and user confirmation dialogs, filling the mock value directly into the OTP field. This is only intended for testing. Takes precedence over one_time_tokens::switches::kMockOtpValue in AttemptOtpFillingTool if both are set.

## `--enable-actor-journal-vlog`

- Constant: `kEnableActorJournalVLog`

Forces logging of the actor aggregated journal events in VLOG(1). Useful on Android as VLOGs are removed on official builds.

## `--actor-trace-path`

- Constant: `kActorTracePath`

File or directory path where actor traces should be recorded.

## `--actor-sensitive-sites`

- Constant: `kActorSensitiveSites`

Specifies a comma-separated list of SchemefulSite strings that should be treated as sensitive sites by the actor execution engine (bypassing the optimization guide component updater check). Useful for testing. Note that these entries are site-scoped (scheme and eTLD+1), not origin-scoped, so specifying a site will match all subdomains and ports on that site. Examples: --actor-sensitive-sites="https://example.com" --actor-sensitive-sites="https://bank.com,https://example.org"
