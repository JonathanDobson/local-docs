# Command-line switches: `components/media_router/common/providers/cast/certificate/switches`

Generated from `components/media_router/common/providers/cast/certificate/switches.h` and `components/media_router/common/providers/cast/certificate/switches.cc` in the Chromium source. Each switch is passed to the browser as `--name` or `--name=value`. The description is the source comment verbatim; *Condition* is the build/platform `#if` it is defined under.

2 switches.

## `--cast-developer-certificate-path`

- Constant: `kCastDeveloperCertificatePath`

When enabled by build flags, passing this argument allows the Cast authentication utils to use a custom root developer certificate in the trust store instead of the root Google-signed cert.

## `--cast-log-device-cert-chain`

- Constant: `kCastLogDeviceCertChain`

When enabled, prints a PEM-encoded the device certificate chain at VLOG level 3.
