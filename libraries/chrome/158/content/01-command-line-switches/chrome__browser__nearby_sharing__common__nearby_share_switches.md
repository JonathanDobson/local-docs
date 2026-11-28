# Command-line switches: `chrome/browser/nearby_sharing/common/nearby_share_switches`

Generated from `chrome/browser/nearby_sharing/common/nearby_share_switches.h` and `chrome/browser/nearby_sharing/common/nearby_share_switches.cc` in the Chromium source. Each switch is passed to the browser as `--name` or `--name=value`. The description is the source comment verbatim; *Condition* is the build/platform `#if` it is defined under.

4 switches.

## `--nearby-share-certificate-validity-period-hours`

- Constant: `kNearbyShareCertificateValidityPeriodHours`

All switches in alphabetical order. The switches should be documented alongside the definition of their values in the .cc file. Overrides the default validity period for Nearby Share certificates. Value must be larger than 0.

## `--nearby-share-device-id`

- Constant: `kNearbyShareDeviceID`

Overrides the default device ID to provide a stable ID in test environments. By default we generate a random 10-character string.

## `--nearbysharing-http-host`

- Constant: `kNearbyShareHTTPHost`

Overrides the default URL for Google APIs (https://www.googleapis.com) used by Nearby Share

## `--nearby-share-num-private-certificates`

- Constant: `kNearbyShareNumPrivateCertificates`

Overrides the default number of private certificates generated. Value must be larger than 0.
