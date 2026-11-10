# Headscale 0.29.x changelog

The 0.29 releases from Headscale's `CHANGELOG.md` at tag v0.29.7.

## 0.29.7 (2026-10-30)

**Minimum supported Tailscale client version: v1.80.0**

### Security

This is a security release. It fixes findings from Anthropic's oss-scanner project and
the Tailworm report. None are critical, but some can cause denial of service in
Headscale. We recommend that all users upgrade to Headscale 0.29.7 **and** Tailscale
v1.104.4 or newer as soon as possible, especially those using Tailscale SSH.

Tailscale v1.104.4 fixes vulnerabilities in SSH forwarding, SSH session handling and
Serve. These fixes run in `tailscaled` on your nodes; upgrading Headscale alone does
not apply them.

See Tailscale's
[security bulletins](https://tailscale.com/security-bulletins#ts-2026-014) and
[Tailscale SSH: Findings and fixes](https://tailscale.com/blog/tailscale-ssh-findings-fixes).

To disable SSH agent and port forwarding on a node, set
`TS_SSH_DISABLE_FORWARDING=1` in the `tailscaled` service environment and restart
the service. This setting applies to all Tailscale SSH sessions on that node and
is also available in older clients. [#3624](https://github.com/juanfont/headscale/pull/3624)

This release also fixes the issues that [oss-scanner](https://github.com/anthropics/oss-scanner/tree/main/projects/headscale)
reported in Headscale: ANT-2026-MLP8ZR5T, ANT-2026-LYVGXVSW, ANT-2026-AWGRB7O1, ANT-2026-QMCAFJ1Q, ANT-2026-RQS7JAPP, ANT-2026-5B6KE87K, ANT-2026-KFCFFM34, ANT-2026-K903ZEUA, ANT-2026-NM50ZP4N, ANT-2026-ZC18AF82, ANT-2026-NWTIBB02, ANT-2026-MX8FKG4K. [#3603](https://github.com/juanfont/headscale/pull/3603)

### Changes

- Metrics are no longer exposed to unregistered clients through the Noise protocol. They remain available only on the configured metrics listener; an empty `metrics_listen_addr` disables that listener [#3623](https://github.com/juanfont/headscale/pull/3623)
- Update the Tailscale dependency to v1.104.4, which bounds how much of an unexpected DERP HTTP response is read [#3577](https://github.com/juanfont/headscale/pull/3577)
- Keep pending registrations and OIDC logins at capacity instead of evicting ones awaiting approval; new requests get a retry response, and registered nodes keep capacity for SSH checks [#3586](https://github.com/juanfont/headscale/pull/3586)
- Cap stored pending registration data at 64 KiB, keeping tags and expiry; oversized interactive registrations are rejected [#3586](https://github.com/juanfont/headscale/pull/3586)
- Check the OIDC login type before storing anything, accept each OIDC callback only once, and free an SSH check's slot once the client has read its result [#3586](https://github.com/juanfont/headscale/pull/3586)
- Stop serving a route that is a single address inside the node IP ranges, such as `100.64.0.11/32` or `::ffff:100.64.0.11/128`, because it names a node, not a subnet; the route stays approved and listed, and wider routes are still served [#3603](https://github.com/juanfont/headscale/pull/3603)
- Require a valid pre-auth key to re-register an expired tagged node [#3603](https://github.com/juanfont/headscale/pull/3603)
- Another user's key or login on a tagged machine now creates a new device for that user instead of re-authenticating the tagged node [#3603](https://github.com/juanfont/headscale/pull/3603)
- Fix one node with a stored key expiry outside the years 0 to 9999 in UTC failing the map of every node that can see it; it is now left out of its peers' maps and the startup check names it with the fix command [#3603](https://github.com/juanfont/headscale/pull/3603)
- Refuse a key expiry outside the years 0 to 9999 in UTC on registration, on the OIDC token-expiry path and in `headscale nodes expire` / `POST /api/v1/node/{node_id}/expire` (HTTP 400); the latest accepted expiry no longer fails node listings on PostgreSQL in a zone east of UTC [#3603](https://github.com/juanfont/headscale/pull/3603)
- Keep the first 256 endpoints and 4096 announced routes from client reports; oversized hostnames, requested tags or other metadata return a registration error or HTTP 413 on map updates. Zoned IPv6 endpoints are refused [#3603](https://github.com/juanfont/headscale/pull/3603)
- At startup, trim stored hostnames, endpoints and routes to the client-report limits and remove zoned endpoints. Hostinfo exceeding its size or tag limit is dropped until the next valid report [#3603](https://github.com/juanfont/headscale/pull/3603)
- Pending interactive registrations and follow-up waits keep only the hostname, OS and requested tags; other device details arrive with the first map request. Reauthentication preserves routes, services and endpoints [#3603](https://github.com/juanfont/headscale/pull/3603)
- Fix web reauthentication dropping the discovery key, so peers could not reach the device [#3603](https://github.com/juanfont/headscale/pull/3603)
- A stalled request body, or a Noise tunnel with no open request, is closed after 30 seconds [#3603](https://github.com/juanfont/headscale/pull/3603)
- A registration follow-up from a machine other than the one that started the registration is refused before it waits [#3603](https://github.com/juanfont/headscale/pull/3603)
- Only the newest follow-up waits on a pending registration or SSH check; older ones are answered at once [#3603](https://github.com/juanfont/headscale/pull/3603)
- Fix registration locks staying in memory after the registration ends [#3603](https://github.com/juanfont/headscale/pull/3603)
- Fix concurrent deletes of one node freeing its addresses and announcing its removal more than once [#3603](https://github.com/juanfont/headscale/pull/3603)
- OIDC verifies an email against the document supplying it; an `email_verified` flag without an address no longer verifies another document's email [#3603](https://github.com/juanfont/headscale/pull/3603)
- Fix release builds reporting their version with a `+dirty` suffix [#3584](https://github.com/juanfont/headscale/pull/3584)
- Fix SSH policy `acceptEnv` having no effect, so allowed environment variables reach SSH sessions. Upgrade SSH destination nodes to Tailscale v1.104.4 or newer before using `acceptEnv`, because older clients can disclose forwarded values [#3569](https://github.com/juanfont/headscale/pull/3569)

## 0.29.6 (2026-10-24)

**Minimum supported Tailscale client version: v1.80.0**

### Security

- Build with Go 1.27.3 to reject certificate chains containing the compromised eMudhra intermediate keys (CVE-2026-111943) [Go #82345](https://github.com/golang/go/issues/82345)
- Update and pin the normal and debug container bases to images whose CA bundles no longer include `emSign ECC Root CA - G3` [#3579](https://github.com/juanfont/headscale/issues/3579)
- Update `golang.org/x/net` to v0.60.0, `golang.org/x/text` to v0.42.0 and gRPC to v1.83.2 to address HTTP/2 denial-of-service and text-processing vulnerabilities ([x/net](https://pkg.go.dev/vuln/GO-2026-6617), [x/text](https://pkg.go.dev/vuln/GO-2026-6629), [gRPC](https://pkg.go.dev/vuln/GO-2026-6348))

Custom builds must be rebuilt with Go 1.27.3 or newer to receive the certificate-chain protection.

### Changes

- Speed up peer-map construction on large tailnets by finding each node's matching rules once, instead of checking every pair of nodes against every rule [#3556](https://github.com/juanfont/headscale/pull/3556)
- Build the peer map once per policy write instead of twice, and skip the rebuild when reloading an unchanged policy [#3557](https://github.com/juanfont/headscale/pull/3557)
- Reduce work when broadcasting map updates by avoiding repeated recipient filtering [#3568](https://github.com/juanfont/headscale/pull/3568)
- Avoid `INTERNAL_ERROR` stream errors when a node logs out or is deleted, or when Headscale shuts down; writes already in progress have a short grace period to finish, while clients that stop reading are still disconnected [#3575](https://github.com/juanfont/headscale/pull/3575)
- Return database-open errors instead of risking a panic or returning a partially initialized database handle [#3496](https://github.com/juanfont/headscale/pull/3496)
- Update the Tailscale dependency to v1.102.0 for Go 1.27 JSON compatibility in SSH check responses

## 0.29.5 (2026-10-13)

**Minimum supported Tailscale client version: v1.80.0**

### Changes

- Fix `via` exit-node steering being undone by an unrelated ACL or grant rule that matches the viewer [#3495](https://github.com/juanfont/headscale/pull/3495)
- Fix `via` grants not offering exit nodes and subnet routes to a group that names an unknown user [#3516](https://github.com/juanfont/headscale/pull/3516)
- Fix SSH `check` periods and app grants dropping a group that names an unknown user [#3516](https://github.com/juanfont/headscale/pull/3516)
- Fix policy `tests` and `sshTests` failing for a group that names an unknown user [#3516](https://github.com/juanfont/headscale/pull/3516)
- Fix an unknown user in `nodeAttrs` rejecting the policy [#3516](https://github.com/juanfont/headscale/pull/3516)
- Fix every grant being fully resolved as if it had `via` when the policy has no `via` grants, slowing map generation on large tailnets [#3538](https://github.com/juanfont/headscale/pull/3538)
- Fix a data race in `via` route resolution when the policy has both `via` grants and ACLs [#3515](https://github.com/juanfont/headscale/pull/3515)
- Fix packet filters under `autogroup:self` not updating after a user is added or renamed [#3501](https://github.com/juanfont/headscale/pull/3501)
- Fix a rejected policy leaving its packet filter active [#3501](https://github.com/juanfont/headscale/pull/3501)
- Fix an exit node or subnet router not seeing its own approved routes until it reconnected, so `tailscale status` did not show it offering an exit node [#3518](https://github.com/juanfont/headscale/pull/3518)
- Fix deleted nodes, and peers hidden by a policy change, staying listed in the Tailscale Android app; removed peers are now sent as their own incremental map update [#3492](https://github.com/juanfont/headscale/pull/3492) [#3527](https://github.com/juanfont/headscale/pull/3527)
- Policy changes no longer resend DNS configuration to every node, sparing clients a full netmap rebuild; a node gets its DNS configuration when its own NextDNS nodeAttrs, tags or hostname change, which also fixes NextDNS device metadata going stale after a hostname change [#3492](https://github.com/juanfont/headscale/pull/3492)
- Fix SSH access surviving the removal of its policy rules; clients kept their last SSH rules, and a pending SSH check could still be approved [#3517](https://github.com/juanfont/headscale/pull/3517)
- Fix SSH check periods coming from the first check rule for a node pair instead of the rule for the login user [#3517](https://github.com/juanfont/headscale/pull/3517)
- Policy changes resend a node's SSH policy only when it changed, sparing clients a full netmap rebuild [#3517](https://github.com/juanfont/headscale/pull/3517)
- Fix SSH check accepting a repeated follow-up for an already-decided session, even after a rejection [#3526](https://github.com/juanfont/headscale/pull/3526)
- Fix an ephemeral node being deleted while online, when it reconnected while its previous session was being marked offline [#3539](https://github.com/juanfont/headscale/pull/3539)
- Fix peers dropping traffic from a node that re-authenticates after its key expired [#3541](https://github.com/juanfont/headscale/pull/3541)
- Fix clients uploading logs to Tailscale Inc. while `logtail.enabled` is `false`; clients also granted the `data-plane-audit-logs` node attribute now go down until `tailscale up` [#3522](https://github.com/juanfont/headscale/pull/3522)
- Fix a node ping being lost when a full map update is queued at the same time [#3523](https://github.com/juanfont/headscale/pull/3523)

## 0.29.4 (2026-09-23)

**Minimum supported Tailscale client version: v1.80.0**

### Changes

- Fix a node being listed among its own peers in an incremental map update, which crashes the Tailscale Android app on the device list [#3459](https://github.com/juanfont/headscale/pull/3459)
- Fix deleting a node leaving its long poll open, so the client stayed connected instead of asking for a new login [#3449](https://github.com/juanfont/headscale/pull/3449)
- Fix interactive OIDC login when the confirmation page is reloaded by an ad blocker, back navigation, or pull-to-refresh; the confirmation page now has its own URL, keeping single-use authorization codes out of reloads [#3448](https://github.com/juanfont/headscale/pull/3448)
- Harden the OIDC callback: state and nonce cookies take their Secure flag from `server_url` so they survive a TLS-terminating proxy, a callback state is single-use, and an invalid `oidc.issuer` or a missing `oidc.client_id`/`oidc.client_secret` now fails at startup [#3334](https://github.com/juanfont/headscale/pull/3334)
- Fix HTTP metrics only counting `OPTIONS` requests, so `http_requests_total` and `http_request_duration_seconds` now cover regular traffic [#3414](https://github.com/juanfont/headscale/pull/3414)
- Fix extra-records filewatcher hanging on shutdown after the watched file is deleted, and leaking the watcher when setup fails [#3437](https://github.com/juanfont/headscale/pull/3437)
- Lowercase DNS extra record names so mixed-case records resolve [#3366](https://github.com/juanfont/headscale/pull/3366)
- Fix `headscale users rename` sending the raw `--identifier` flag value instead of the matched user's identifier, so renaming by name works again [#3442](https://github.com/juanfont/headscale/pull/3442)
- Fix tailsql not shutting down with headscale, leaving the process hanging on graceful shutdown [#3400](https://github.com/juanfont/headscale/pull/3400)
- Fix tvOS setup instructions: install the VPN configuration before setting the coordination server URL [#3431](https://github.com/juanfont/headscale/pull/3431)
- Map requests that only bump LastSeen, endpoints or DERP region no longer resend the whole node to every peer, and health probes that change nothing no longer write. Adds `headscale_mapper_changes_dropped_total` and `headscale_ha_health_updates_total` [#3417](https://github.com/juanfont/headscale/issues/3417) [#3450](https://github.com/juanfont/headscale/pull/3450)
- The peer map is keyed by node ID and reused for writes that cannot change peer visibility, so a routine map request no longer rebuilds it. Adds `headscale_nodestore_snapshot_builds_total` [#3417](https://github.com/juanfont/headscale/issues/3417) [#3450](https://github.com/juanfont/headscale/pull/3450)
- Fix an expired node staying online forever, because expiring it updated the key deadline without ending its map session [#3472](https://github.com/juanfont/headscale/pull/3472)
- Fix ACME renewal stopping permanently after a `badNonce` reply, because the error logging middleware drained the response body the acme client needs to detect it [#3461](https://github.com/juanfont/headscale/pull/3461)
- Fix `#`-prefixed metadata fields being rejected outside `acls`, so policy editors can store metadata in grants, SSH rules and `nodeAttrs` [#3481](https://github.com/juanfont/headscale/pull/3481)
- Fix exit nodes not offered by recent macOS and iOS clients, which read the `suggest-exit-node` peer attribute rather than the advertised `0.0.0.0/0` routes [#3487](https://github.com/juanfont/headscale/pull/3487)
- Fix exit node not offered to viewers whose only matching rule is a `via` grant; peer visibility now comes from the peer map alone [#3409](https://github.com/juanfont/headscale/pull/3409)

## 0.29.3 (2026-07-29)

**Minimum supported Tailscale client version: v1.80.0**

### Changes

- Fix tagged node stuck expired after `tailscale logout`, unable to re-authenticate [#3394](https://github.com/juanfont/headscale/pull/3394)
- Re-registering a tagged node with a different pre-auth key now applies the new key's tags instead of silently keeping the old ones [#3394](https://github.com/juanfont/headscale/pull/3394)
- Fix re-authenticating an already-tagged node with `--advertise-tags` being rejected when the authenticating user owns the tags [#3394](https://github.com/juanfont/headscale/pull/3394)
- Fix ephemeral nodes lingering as disconnected after reconnect churn [#3383](https://github.com/juanfont/headscale/pull/3383)
- Fix node registration falsely returning `401 registration timed out` when auth completes as the request context expires [#3392](https://github.com/juanfont/headscale/pull/3392)
- Check the machine key on the followup registration poll so a leaked auth ID cannot return the registering user's identity [#3393](https://github.com/juanfont/headscale/pull/3393)
- Reject `/key` requests below the supported capability version floor, matching `/ts2021` [#3391](https://github.com/juanfont/headscale/pull/3391)

## 0.29.2 (2026-07-01)

**Minimum supported Tailscale client version: v1.80.0**

### Changes

- Fix map generation serializing on the policy lock, so a mass reconnect on `autogroup:self`, via or relay policies no longer stalls clients into `unexpected EOF` retry loops [#3358](https://github.com/juanfont/headscale/pull/3358)
- Fix `/ts2021` rejecting the WebSocket `GET` upgrade with 405, which prevented Tailscale JS/WASM control clients from connecting [#3359](https://github.com/juanfont/headscale/pull/3359)
- Gracefully handle nodes with an invalid FQDN (empty or too long) instead of failing map delivery; offending names are logged at startup with the fix command [#3349](https://github.com/juanfont/headscale/pull/3349)

## 0.29.1 (2026-06-18)

**Minimum supported Tailscale client version: v1.80.0**

### Changes

- Fix nodes with `tags='null'` losing their assigned user on upgrade [#3325](https://github.com/juanfont/headscale/pull/3325)

## 0.29.0 (2026-06-17)

**Minimum supported Tailscale client version: v1.80.0**

### Tailscale ACL compatibility improvements

Extensive test cases were systematically generated using Tailscale clients and the official SaaS
to understand how the packet filter should be generated. We discovered a few differences, but
overall our implementation was very close.
[#3036](https://github.com/juanfont/headscale/pull/3036)

### SSH check action

SSH rules with `"action": "check"` are now supported. When a client initiates a SSH connection to a node
with a `check` action policy, the user is prompted to authenticate via OIDC or CLI approval before access
is granted. OIDC approval requires the authenticated user to own the source node; tagged source nodes
cannot use SSH check-mode.

A new `headscale auth` CLI command group supports the approval flow:

- `headscale auth approve --auth-id <id>` approves a pending authentication request (SSH check or web auth)
- `headscale auth reject --auth-id <id>` rejects a pending authentication request
- `headscale auth register --auth-id <id> --user <user>` registers a node (replaces deprecated `headscale nodes register`)

[#1850](https://github.com/juanfont/headscale/pull/1850)
[#3180](https://github.com/juanfont/headscale/pull/3180)

### Policy tests (beta)

Headscale now evaluates the `tests` block in a policy file. Tests assert reachability between
named sources and destinations and cover the whole policy — both `acls` and `grants` rules
contribute. They run on user-initiated writes via `headscale policy set`, on SIGHUP reload
(`systemctl reload headscale` / `kill -HUP $(pidof headscale)`), and on `headscale policy check`.
A failing test rejects the write before it is applied, with the same error message Tailscale SaaS
would return for the same policy.

At boot a stored policy whose tests no longer pass — for example because a referenced user was
deleted while the server was offline — logs a warning and the server keeps running. Fix the
policy and reload.

This feature is **beta** while behavioural coverage against Tailscale SaaS broadens.

[#3229](https://github.com/juanfont/headscale/pull/3229)

### SSH policy tests (beta)

Headscale now evaluates the `sshTests` block in a policy file. Each entry names a source, one or
more destination hosts, and three optional user lists: `accept` asserts the listed login users
reach every destination via an accept- or check-action SSH rule, `deny` asserts none of them
reach any destination, and `check` requires reachability specifically through a check-action
rule. Tests run on `headscale policy set`, on SIGHUP reload (`systemctl reload headscale` /
`kill -HUP $(pidof headscale)`), and on `headscale policy check`. A failing test rejects the
write before it is applied, with the same error message Tailscale SaaS would return for the same
policy.

At boot a stored policy whose sshTests no longer pass — for example because a referenced user was
deleted while the server was offline — logs a warning and the server keeps running. Fix the
policy and reload.

This feature is **beta** while behavioural coverage against Tailscale SaaS broadens.

[#3263](https://github.com/juanfont/headscale/pull/3263)

### SSH rule validation

SSH rule parsing now trims surrounding whitespace on `action`, `users`, `src`, and `dst`,
rejects empty or wildcard entries in `users`, rejects empty `acceptEnv`, and rejects negative
`checkPeriod`. `hosts:` aliases are rejected as SSH destinations, non-ASCII tag names are
rejected at parse time, and the wording for group-nesting cycles matches Tailscale SaaS.
[#3263](https://github.com/juanfont/headscale/pull/3263)

### Grants

We now support [Tailscale grants](https://tailscale.com/docs/features/access-control/grants)
alongside ACLs. Grants extend what you can express in a policy beyond packet filtering: the `app`
field controls application-level features like Taildrive file sharing and peer relay, and the `via`
field steers traffic through specific tagged subnet routers or exit nodes. The `ip` field works like
an ACL rule. Grants can be mixed with ACLs in the same policy file.
[#2180](https://github.com/juanfont/headscale/pull/2180)

As part of this, we added `autogroup:danger-all`. It resolves to `0.0.0.0/0` and `::/0`, all IP
addresses, including those outside the tailnet. This replaces the old behaviour where `*` matched
all IPs (see BREAKING below). The name is intentional: accepting traffic from the entire
internet is a security-sensitive choice. `autogroup:danger-all` can only be used as a source.

### Node attributes (`nodeAttrs`)

ACL policies now accept a `nodeAttrs` block. Each entry hands a list of
Tailscale node capabilities to every node matching `target`. The accepted
target forms are the same as `acls.src` and `grants.src`: users, groups,
tags, hosts, prefixes, `autogroup:member`, `autogroup:tagged`, and `*`.

```jsonc
{
  "randomizeClientPort": true,
  "nodeAttrs": [
    { "target": ["autogroup:tagged"], "attr": ["disable-captive-portal-detection"] },
    { "target": ["alice@example.com"], "attr": ["nextdns:abc123"] },
  ],
}
```

Frequently requested capabilities this unlocks include `magicdns-aaaa`,
`disable-relay-server`, `disable-captive-portal-detection`,
`nextdns:<profile>` / `nextdns:no-device-info`, `randomize-client-port`,
and the Taildrive `drive:share` / `drive:access` pair. The set is not
limited to these, any string-only cap an operator places in policy
reaches clients unchanged.

`randomizeClientPort` also lands as a top-level policy field that toggles
the default for every node, replacing the old server-config knob.

A new `auto_update.enabled` config option controls the tailnet-wide
default for client auto-update. When true, every node's CapMap carries
`default-auto-update: [true]` so fresh clients pick up the default
unless they make a local opt-in / opt-out choice.

Policies that use the `funnel` cap, `ipPool` blocks, or
`autogroup:admin` / `autogroup:owner` targets are rejected at load —
those features depend on machinery headscale does not yet ship.

[#3251](https://github.com/juanfont/headscale/pull/3251)

### Taildrive

Taildrive ([file-sync between
nodes](https://tailscale.com/docs/features/taildrive)) is now
configurable through policy. Grant `drive:share` to the node that
hosts files and `drive:access` to nodes that read or write them; pair
with a `tailscale.com/cap/drive` grant to set the per-share access
mode:

```jsonc
{
  "nodeAttrs": [
    { "target": ["tag:fileserver"], "attr": ["drive:share"] },
    { "target": ["autogroup:member"], "attr": ["drive:access"] },
  ],
  "grants": [
    {
      "src": ["autogroup:member"],
      "dst": ["tag:fileserver"],
      "app": {
        "tailscale.com/cap/drive": [{ "shares": ["*"], "access": "rw" }],
      },
    },
  ],
}
```

A wildcard `nodeAttrs` (`"target": ["*"]`) hands the caps to every
node when fine-grained control is not needed.

### Hostname sanitisation

Hostnames are now santised using Tailscales `magicdns` sanitisation rules, matching Tailscale SaaS behavior. This means that hostnames with non-ASCII characters, special characters, or reserved DNS label characters are now transformed into valid DNS labels for MagicDNS. This improves our previously too strict sanitisation that rejected hostnames based on our guesswork and not based on the Tailscale upstream behaviour.

Examples that previously regressed and now work:

| Input                | Raw (Hostname)       | DNS label (GivenName) |
| -------------------- | -------------------- | --------------------- |
| `Joe's Mac mini`     | `Joe's Mac mini`     | `joes-mac-mini`       |
| `Yuri's MacBook Pro` | `Yuri's MacBook Pro` | `yuris-macbook-pro`   |
| `Test@Host`          | `Test@Host`          | `test-host`           |
| `mail.server`        | `mail.server`        | `mail-server`         |
| `My-PC!`             | `My-PC!`             | `my-pc`               |
| `我的电脑`           | `我的电脑`           | `node`                |

[#3202](https://github.com/juanfont/headscale/pull/3202)

### HA subnet router health probing

Headscale now actively probes HA subnet routers to detect nodes that are connected but not
forwarding traffic. The control plane periodically pings HA subnet routers via the Noise
control channel and fails over to a healthy standby if the primary stops responding. This is
enabled by default (`node.routes.ha.probe_interval: 10s`, `probe_timeout: 5s`) and only
active when HA routes exist (2+ nodes advertising the same prefix). Set `probe_interval` to
`0` to disable. This complements the existing disconnect-based failover, catching "zombie
connected" routers that maintain their control session but cannot route packets.
[#3194](https://github.com/juanfont/headscale/pull/3194)

### BREAKING

#### Hostname handling

- The `GivenName` collision policy changed from an 8-char random hash suffix (`laptop-abc12xyz`) to a monotonic numeric suffix (`laptop`, `laptop-1`, `laptop-2`, …), matching Tailscale SaaS. Empty / all-non-ASCII hostnames now fall back to the literal `node` instead of `invalid-<rand>`. MagicDNS names change on upgrade for any node whose previous label was a random-suffix form; the raw `Hostname` column is unchanged. [#3202](https://github.com/juanfont/headscale/pull/3202)

#### ACL Policy

- Wildcard (`*`) in ACL sources and destinations now resolves to Tailscale's CGNAT range (`100.64.0.0/10`) and ULA range (`fd7a:115c:a1e0::/48`) instead of all IPs (`0.0.0.0/0` and `::/0`) [#3036](https://github.com/juanfont/headscale/pull/3036)
  - This better matches Tailscale's security model where `*` means "any node in the tailnet" rather than "any IP address"
  - Policies that need to match all IP addresses including non-Tailscale IPs should use `autogroup:danger-all` as a source, or explicit CIDR ranges as destinations [#2180](https://github.com/juanfont/headscale/pull/2180)
  - `autogroup:danger-all` can only be used as a source; it cannot be used as a destination
  - **Note**: Users with non-standard IP ranges configured in `prefixes.ipv4` or `prefixes.ipv6` (which is unsupported and produces a warning) will need to explicitly specify their CIDR ranges in ACL rules instead of using `*`
- Validate `autogroup:self` source restrictions matching Tailscale behavior - tags, hosts, and IPs are rejected as sources for `autogroup:self` destinations [#3036](https://github.com/juanfont/headscale/pull/3036)
  - Policies using tags, hosts, or IP addresses as sources for `autogroup:self` destinations will now fail validation
- The `proto:icmp` protocol name now only includes ICMPv4 (protocol 1), matching Tailscale behavior [#3036](https://github.com/juanfont/headscale/pull/3036)
  - Previously, `proto:icmp` included both ICMPv4 and ICMPv6
  - Use `proto:ipv6-icmp` or protocol number `58` explicitly for ICMPv6

#### Upgrade Path

- Headscale now enforces a strict version upgrade path [#3083](https://github.com/juanfont/headscale/pull/3083)
  - Skipping minor versions (e.g. 0.27 → 0.29) is blocked; upgrade one minor version at a time
  - Downgrading to a previous minor version is blocked
  - Patch version changes within the same minor are always allowed

#### Configuration

- The `randomize_client_port` server-config key was removed; the
  toggle now lives in the policy file as a top-level
  `randomizeClientPort` field, matching the Tailscale-hosted schema. [#3251](https://github.com/juanfont/headscale/pull/3251)
  Headscale refuses to start when the old key is set. Move it to the
  policy file referenced by `policy.path`:

  ```jsonc
  {
    "randomizeClientPort": true,
  }
  ```

  If you do not have a policy file yet, create one with that minimal
  content and point `policy.path` at it. The default carries over —
  empty / absent policy means `randomizeClientPort: false`, matching
  the previous behaviour for operators who never set the key. Per-node
  opt-in via `nodeAttrs` is also supported and stacks on top of the
  global default.

#### CLI

- `headscale nodes register` is deprecated in favour of `headscale auth register --auth-id <id> --user <user>` [#1850](https://github.com/juanfont/headscale/pull/1850)
  - The old command continues to work but will be removed in a future release

### Changes

#### ACL Policy

- Fix subnet-to-subnet peer visibility — subnet routers now correctly become peers when ACL rules reference only subnet CIDRs as sources, without requiring node IP rules [#3175](https://github.com/juanfont/headscale/pull/3175)
- Fix filter rule reduction to use only approved subnet routes instead of all advertised routes, matching Tailscale SaaS behavior [#3175](https://github.com/juanfont/headscale/pull/3175)
- Add ICMP and IPv6-ICMP protocols to default filter rules when no protocol is specified [#3036](https://github.com/juanfont/headscale/pull/3036)
- Fix autogroup:self handling for tagged nodes - tagged nodes no longer incorrectly receive autogroup:self filter rules [#3036](https://github.com/juanfont/headscale/pull/3036)
- Use CIDR format for autogroup:self destination IPs matching Tailscale behavior [#3036](https://github.com/juanfont/headscale/pull/3036)
- Merge filter rules with identical SrcIPs and IPProto matching Tailscale behavior - multiple ACL rules with the same source now produce a single FilterRule with combined DstPorts [#3036](https://github.com/juanfont/headscale/pull/3036)
- Fix exit nodes incorrectly receiving filter rules for destinations that only overlap via exit routes [#3169](https://github.com/juanfont/headscale/issues/3169) [#3175](https://github.com/juanfont/headscale/pull/3175)
- Fix address-based aliases (hosts, raw IPs) incorrectly expanding to include the matching node's other address family [#2180](https://github.com/juanfont/headscale/pull/2180)
- Fix identity-based aliases (tags, users, groups) resolving to IPv4 only; they now include both IPv4 and IPv6 matching Tailscale behavior [#2180](https://github.com/juanfont/headscale/pull/2180)
- Fix wildcard (`*`) source in ACLs now using actually-approved subnet routes instead of autoApprover policy prefixes [#2180](https://github.com/juanfont/headscale/pull/2180)
- Fix non-wildcard source IPs being dropped when combined with wildcard `*` in the same ACL rule [#2180](https://github.com/juanfont/headscale/pull/2180)
- Fix exit node approval not triggering filter rule recalculation for peers [#2180](https://github.com/juanfont/headscale/pull/2180)
- Policy validation error messages now include field context (e.g., `src=`, `dst=`) and are more descriptive [#2180](https://github.com/juanfont/headscale/pull/2180)
- Reject policies whose `user@` tokens match multiple DB users; rename the duplicate via `headscale users rename` to load [#3160](https://github.com/juanfont/headscale/issues/3160)
- Evaluate the policy `tests` block on user-initiated writes across both `acls` and `grants`; reject policies whose tests fail (beta) [#1803](https://github.com/juanfont/headscale/issues/1803)

#### Grants

- Add support for policy grants with `ip`, `app`, and `via` fields [#2180](https://github.com/juanfont/headscale/pull/2180)
- Add `autogroup:danger-all` as a source-only autogroup resolving to all IP addresses [#2180](https://github.com/juanfont/headscale/pull/2180)
- Add capability grants for Taildrive (`cap/drive`) and peer relay (`cap/relay`) with automatic companion capabilities [#2180](https://github.com/juanfont/headscale/pull/2180)
- Add per-viewer via route steering — grants with `via` tags control which subnet router or exit node handles traffic for each group of viewers [#2180](https://github.com/juanfont/headscale/pull/2180)
- Enable Taildrive node attributes on all nodes; actual access is controlled by `cap/drive` grants [#2180](https://github.com/juanfont/headscale/pull/2180)

#### SSH Policy

- Add support for `localpart:*@<domain>` in SSH rule `users` field, mapping each matching user's email local-part as their OS username [#3091](https://github.com/juanfont/headscale/pull/3091)
- Add SSH `check` action support with OIDC and CLI-based approval flows [#1850](https://github.com/juanfont/headscale/pull/1850)

#### CLI

- Add `headscale auth register`, `headscale auth approve`, and `headscale auth reject` CLI commands [#1850](https://github.com/juanfont/headscale/pull/1850)
- Deprecate `headscale nodes register --key` in favour of `headscale auth register --auth-id` [#1850](https://github.com/juanfont/headscale/pull/1850)
- `headscale policy check --bypass-grpc-and-access-database-directly` validates `user@` tokens against the live user database [#3160](https://github.com/juanfont/headscale/issues/3160)
- Remove deprecated `--namespace` flag from `nodes list`, `nodes register`, and `debug create-node` commands (use `--user` instead) [#3093](https://github.com/juanfont/headscale/pull/3093)
- Remove deprecated `namespace`/`ns` command aliases for `users` and `machine`/`machines` aliases for `nodes` [#3093](https://github.com/juanfont/headscale/pull/3093)
- Fix `DestroyUser` deleting all pre-auth keys in the database instead of only the target user's keys [#3155](https://github.com/juanfont/headscale/pull/3155)
- `headscale policy check` evaluates the `tests` block when invoked with `--bypass-grpc-and-access-database-directly`; without the flag it warns instead of running the tests against empty data [#1803](https://github.com/juanfont/headscale/issues/1803)

#### API

- Add `auth` related routes. The `auth/register` endpoint now expects data as JSON [#1850](https://github.com/juanfont/headscale/pull/1850)
- Remove gRPC reflection from the remote (TCP) server [#3180](https://github.com/juanfont/headscale/pull/3180)

#### OIDC

- Add a confirmation page before completing node registration, showing the device hostname and machine key fingerprint [#3180](https://github.com/juanfont/headscale/pull/3180)
- Generalise auth templates into reusable `AuthSuccess` and `AuthWeb` components [#1850](https://github.com/juanfont/headscale/pull/1850)
- Unify auth pipeline with `AuthVerdict` type, supporting registration, reauthentication, and SSH checks [#1850](https://github.com/juanfont/headscale/pull/1850)

#### Configuration

- Add `node.expiry` configuration option to set a default node key expiry for nodes registered via auth key [#3122](https://github.com/juanfont/headscale/pull/3122)
  - Tagged nodes (registered with tagged pre-auth keys) are exempt from default expiry
  - `oidc.expiry` has been removed; use `node.expiry` instead (applies to all registration methods including OIDC)
  - `ephemeral_node_inactivity_timeout` is deprecated in favour of `node.ephemeral.inactivity_timeout`
- Add `trusted_proxies` to gate `True-Client-IP` / `X-Real-IP` / `X-Forwarded-For` (previously honoured from any client) [#3268](https://github.com/juanfont/headscale/pull/3268)

#### Debug

- Add node connectivity ping page for verifying control-plane reachability [#3183](https://github.com/juanfont/headscale/pull/3183)
- Omit secret fields (`Pass`, `ClientSecret`, `APIKey`) from `/debug/config` JSON output [#3180](https://github.com/juanfont/headscale/pull/3180)
- Route `statsviz` through `tsweb.Protected` [#3180](https://github.com/juanfont/headscale/pull/3180)

#### Other

- Remove old migrations for the debian package [#3185](https://github.com/juanfont/headscale/pull/3185)
- Install `config-example.yaml` as example for the debian package [#3186](https://github.com/juanfont/headscale/pull/3186)
- Fix user-owned re-registration with zero client expiry and no default storing `0001-01-01 00:00:00` in the database instead of `NULL` [#3199](https://github.com/juanfont/headscale/pull/3199)
- Fix `tailscaled` restart on a node with no expiry resetting `NULL` to `0001-01-01 00:00:00` in the database, affecting both tagged and untagged nodes [#3197](https://github.com/juanfont/headscale/pull/3197)
- Backfill `nodes.expiry` rows persisted by older versions as `0001-01-01 00:00:00` to `NULL`, so nodes upgraded from <0.28 stop reporting as expired [#3284](https://github.com/juanfont/headscale/issues/3284)
- Update reverse proxy documentation for `trusted_proxies` configuration option [#3292](https://github.com/juanfont/headscale/pull/3292)

