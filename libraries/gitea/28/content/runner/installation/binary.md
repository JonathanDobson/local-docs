---
sidebar_position: 1
---

# Install from a binary

The runner is a single binary, `gitea-runner`, built for Linux, macOS, Windows, and FreeBSD.

## Download

Download releases from [dl.gitea.com/gitea-runner](https://dl.gitea.com/gitea-runner/). Each binary has a matching `.sha256` checksum file:

```bash
VERSION=5.2.0
curl -sSLO "https://dl.gitea.com/gitea-runner/$VERSION/gitea-runner-$VERSION-linux-amd64"
curl -sSLO "https://dl.gitea.com/gitea-runner/$VERSION/gitea-runner-$VERSION-linux-amd64.sha256"
sha256sum -c "gitea-runner-$VERSION-linux-amd64.sha256"
sudo install -m 0755 "gitea-runner-$VERSION-linux-amd64" /usr/local/bin/gitea-runner
```

To build the runner yourself, run `make build` in a clone of [gitea/runner](https://gitea.com/gitea/runner).

## First run

```bash
gitea-runner register --instance https://gitea.example.com --token <token>
gitea-runner daemon
```

`register` prompts for the remaining settings and writes the `.runner` registration file to the working directory. Run `daemon` from the same directory so it can read the file. See [Registration](../registration.md).

## systemd

Create a user and a configuration file. Then register the runner as that user from its home directory:

```bash
sudo useradd --system --home-dir /var/lib/gitea-runner --create-home gitea-runner
sudo mkdir -p /etc/gitea-runner
sudo gitea-runner config init -c /etc/gitea-runner/config.yaml
sudo chown gitea-runner /etc/gitea-runner/config.yaml
cd /var/lib/gitea-runner
sudo -u gitea-runner gitea-runner register -c /etc/gitea-runner/config.yaml \
  --instance https://gitea.example.com --token <token>
```

Install the unit as `/etc/systemd/system/gitea-runner.service`:

```ini
[Unit]
Description=Gitea Actions runner
Documentation=https://gitea.com/gitea/runner
After=network-online.target
Wants=network-online.target
# Uncomment when jobs use the local Docker daemon:
# After=docker.service
# Requires=docker.service

[Service]
Type=simple
ExecStart=/usr/local/bin/gitea-runner daemon --config /etc/gitea-runner/config.yaml
WorkingDirectory=/var/lib/gitea-runner
User=gitea-runner
Group=gitea-runner
Restart=on-failure
RestartSec=5s
TimeoutStopSec=3h

[Install]
WantedBy=multi-user.target
```

```bash
sudo systemctl daemon-reload
sudo systemctl enable --now gitea-runner
```

Stopping the service cancels running jobs unless `runner.shutdown_timeout` gives them time to finish. Keep `runner.shutdown_timeout` below `TimeoutStopSec`:

```bash
sudo -u gitea-runner gitea-runner config set -c /etc/gitea-runner/config.yaml runner.shutdown_timeout 2h50m
```

For jobs in containers, give the `gitea-runner` user access to the Docker daemon's socket, for example through the `docker` group. That access is [equivalent to root](https://docs.docker.com/engine/security/#docker-daemon-attack-surface) on the host. Set the runner's environment variables, such as [proxy settings](../proxy.md), with `Environment=` lines in the unit.

## launchd (macOS)

Adjust the paths and user for your setup, then save this file as `/Library/LaunchDaemons/com.gitea.runner.plist`:

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
    <key>Label</key>
    <string>com.gitea.runner</string>
    <key>ProgramArguments</key>
    <array>
        <string>/usr/local/bin/gitea-runner</string>
        <string>daemon</string>
        <string>--config</string>
        <string>/etc/gitea-runner/config.yaml</string>
    </array>
    <key>UserName</key>
    <string>_gitea-runner</string>
    <key>WorkingDirectory</key>
    <string>/var/lib/gitea-runner</string>
    <key>EnvironmentVariables</key>
    <dict>
        <key>PATH</key>
        <string>/usr/local/bin:/usr/bin:/bin:/usr/sbin:/sbin</string>
        <key>HOME</key>
        <string>/var/lib/gitea-runner</string>
    </dict>
    <key>StandardErrorPath</key>
    <string>/var/lib/gitea-runner/runner.log</string>
    <key>RunAtLoad</key>
    <true/>
    <key>KeepAlive</key>
    <true/>
</dict>
</plist>
```

```bash
sudo launchctl bootstrap system /Library/LaunchDaemons/com.gitea.runner.plist
```

## Windows

Run `gitea-runner daemon` with a service wrapper such as [WinSW](https://github.com/winsw/winsw). The runner has no service installer of its own.

On macOS and Windows, jobs usually run directly on the runner's machine with [host labels](../labels.md).
