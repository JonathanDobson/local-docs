# Command-line switches: `chrome/browser/webauthn/webauthn_switches`

Generated from `chrome/browser/webauthn/webauthn_switches.h` and `chrome/browser/webauthn/webauthn_switches.cc` in the Chromium source. Each switch is passed to the browser as `--name` or `--name=value`. The description is the source comment verbatim; *Condition* is the build/platform `#if` it is defined under.

3 switches.

## `--webauthn-remote-proxied-requests-allowed-additional-origin`

- Constant: `kRemoteProxiedRequestsAllowedAdditionalOrigin`

Allows specifying one additional origin for the WebAuthenticationRemoteProxiedRequestsAllowed enterprise policy. The origin must be ordinarily allowed to perform WebAuthn requests (i.e. it must either be secure or http://localhost).

## `--webauthn-permit-enterprise-attestation`

- Constant: `kPermitEnterpriseAttestationOriginList`

A list of origins that are permitted to request enterprise attestation when creating a WebAuthn credential.

## `--webauthn-gpm-magic-arch-url`

- Constant: `kGpmMagicArchUrlSwitch`

The domain for Magic Arch.
