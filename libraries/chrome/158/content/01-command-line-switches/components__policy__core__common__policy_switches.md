# Command-line switches: `components/policy/core/common/policy_switches`

Generated from `components/policy/core/common/policy_switches.h` and `components/policy/core/common/policy_switches.cc` in the Chromium source. Each switch is passed to the browser as `--name` or `--name=value`. The description is the source comment verbatim; *Condition* is the build/platform `#if` it is defined under.

10 switches.

## `--device-management-url`

- Constant: `kDeviceManagementUrl`

Specifies the URL at which to communicate with the device management backend to fetch configuration policies and perform other device tasks.

## `--realtime-reporting-url`

- Constant: `kRealtimeReportingUrl`

Specifies the URL at which to upload real-time reports.

## `--encrypted-reporting-url`

- Constant: `kEncryptedReportingUrl`

Specifies the URL at which to upload encrypted reports.

## `--policy`

- Constant: `kChromePolicy`

Set policy value by command line.

## `--secure-connect-api-url`

- Constant: `kSecureConnectApiUrl`

Specifies the base URL to contact the secure connect Api.

## `--file-storage-server-upload-url`

- Constant: `kFileStorageServerUploadUrl`

Specifies the URL at which to communicate with File Storage Server (go/crosman-file-storage-server) to upload log and support packet files.

## `--policy-verification-key`

- Constant: `kPolicyVerificationKey`

Replace the original verification_key with the one provided by the command line flag. Can be used only for unit tests or browser tests.

## `--disable-policy-key-verification`

- Constant: `kDisablePolicyKeyVerification`
- Condition: `BUILDFLAG(IS_CHROMEOS)`

Disables the verification of policy signing keys. It just works on Chrome OS test images and crashes otherwise. TODO(crbug.com/1225054): This flag might introduce security risks. Find a better solution to enable policy tast test for Family Link account.

## `--force-device-ownership`

- Constant: `kForceDeviceOwnership`
- Condition: `BUILDFLAG(IS_ANDROID)`

_No description in the source._

## `--use-fake-dmserver`

- Constant: `kUseFakeDmserver`
- Condition: `!BUILDFLAG(GOOGLE_CHROME_BRANDING)`

_No description in the source._
