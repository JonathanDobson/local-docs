---
title: "Traefik StripPrefix Documentation"
description: "In Traefik Proxy's HTTP middleware, StripPrefix removes prefixes from paths before forwarding requests. Read the technical documentation."
---

The `stripPrefix` middleware strips the matching path prefix and stores it in an `X-Forwarded-Prefix` header.

!!! tip

    Use a `StripPrefix` middleware if your backend listens on the root path (`/`) but should be exposed on a specific prefix.

## Configuration Examples

```yaml tab="Structured (YAML)"
# Strip prefix /foobar and /fiibar
http:
  middlewares:
    test-stripprefix:
      stripPrefix:
        prefixes:
          - "/foobar"
          - "/fiibar"
```

```toml tab="Structured (TOML)"
# Strip prefix /foobar and /fiibar
[http.middlewares]
  [http.middlewares.test-stripprefix.stripPrefix]
    prefixes = ["/foobar", "/fiibar"]
```

```yaml tab="Labels"
# Strip prefix /foobar and /fiibar
labels:
  - "traefik.http.middlewares.test-stripprefix.stripprefix.prefixes=/foobar,/fiibar"
```

```json tab="Tags"
// Strip prefix /foobar and /fiibar
{
  "Tags" : [
    "traefik.http.middlewares.test-stripprefix.stripprefix.prefixes=/foobar,/fiibar"
  ]
}
```

```yaml tab="Kubernetes"
# Strip prefix /foobar and /fiibar
apiVersion: traefik.io/v1alpha1
kind: Middleware
metadata:
  name: test-stripprefix
spec:
  stripPrefix:
    prefixes:
      - /foobar
      - /fiibar
```

## Configuration Options

| Field                        | Description           | Default | Required |
|:-----------------------------|:--------------------------------------------------------------|:--------|:---------|
| <a id="opt-prefixes" href="#opt-prefixes" title="#opt-prefixes">`prefixes`</a> | List of prefixes to strip from the request URL.<br />If your backend is serving assets (for example, images or JavaScript files), it can use the `X-Forwarded-Prefix` header to construct relative URLs. | [] | No |

---

!!! question "Using Traefik OSS in Production?"

    If you are using Traefik at work, consider adding enterprise-grade API gateway capabilities or commercial support for Traefik OSS.

    - [Watch our API Gateway Demo Video](https://info.traefik.io/watch-traefik-api-gw-demo?cta=doc)
    - [Request 24/7/365 OSS Support](https://info.traefik.io/request-commercial-support?cta=doc)

    Adding API Gateway capabilities to Traefik OSS is fast and seamless. There's no rip and replace and all configurations remain intact. See it in action via [this short video](https://info.traefik.io/watch-traefik-api-gw-demo?cta=doc).