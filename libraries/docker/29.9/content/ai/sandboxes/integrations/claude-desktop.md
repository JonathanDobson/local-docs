---
title: "Connect Claude Desktop to a sandbox"
source: https://docs.docker.com/ai/sandboxes/integrations/claude-desktop/
---

# Connect Claude Desktop to a sandbox




These connection instructions use a local sandbox. For cloud SSH setup, see
[Connect with SSH](/ai/sandboxes/integrations/cloud/usage/#connect-with-ssh).

Claude Desktop can run Claude Code on a remote machine over SSH. Point it at a
sandbox so the agent works inside the isolated environment instead of on your
host.

> [!NOTE]
> This page covers Claude Desktop connecting to a sandbox over SSH. To run the
> Claude Code CLI inside a sandbox directly, see
> [Claude Code](/ai/sandboxes/integrations/agents/claude-code/).

## Prerequisites

- Claude credentials configured in Docker Sandboxes. See
  [Claude Code authentication](/ai/sandboxes/integrations/agents/claude-code/#authentication).
- SSH access set up. See [Editor and app integrations](/ai/sandboxes/integrations/claude-desktop/#enable-ssh-access).
- Claude Desktop installed.

Use a sandbox created with the Claude agent type. The Claude sandbox template
configures credential injection and network access for the remote Claude Code
session. You must supply the credential before connecting.

> [!WARNING]
> Claude Desktop can write Anthropic credentials directly into the sandbox
> during OAuth refresh. When this happens, requests use those credentials
> instead of proxy credential injection. The credentials are exposed inside
> the sandbox, reducing isolation guarantees.

## Connect

For a dedicated sandbox created on first connection, see
[Set up desktop app connections](/ai/sandboxes/integrations/claude-desktop/#set-up-desktop-app-connections).
The following steps connect to a sandbox with a mounted host workspace.

Create a named Claude sandbox for the current directory if you don't already
have one:

```console
$ sbx create --name demo claude .
```

Confirm that you can connect to the sandbox from a terminal:

```console
$ ssh demo.sbx
```

In Claude Desktop, open the environment drop-down before starting a session and
select **+ Add SSH connection**. Enter a name for the connection and enter the
sandbox hostname, such as `demo.sbx`, in **SSH Host**. Leave **SSH Port** and
**Identity File** empty because the managed SSH config supplies them.

Select the connection from the environment drop-down, then use the remote
folder picker to
[select the mounted workspace](/ai/sandboxes/integrations/claude-desktop/#select-the-workspace-folder). The
picker might initially open at `/home/agent`.

For more connection options, see the Claude Desktop instructions for
[SSH sessions](https://code.claude.com/docs/en/desktop#ssh-sessions).

## Troubleshoot a broken SSH connection after token refresh

The SSH connection drops when the Anthropic token expires and needs to be
refreshed. To work around this, run the sandbox manually from your host:

```console
$ sbx run --name <sandbox-name>
```

## Troubleshoot SSH connection timeouts on Windows

Claude Desktop requires Git on Windows. If an SSH connection times out and the
Claude Desktop logs include `ProxyCommand error: spawn sh ENOENT`, install
[Git for Windows](https://git-scm.com/download/win).

If Git is already installed, verify that `sh.exe` is available on your `PATH`:

```powershell
PS> where.exe sh
```

If the command doesn't find `sh.exe`, add the Git `bin` directory to your user
`Path`. The default directory is `C:\Program Files\Git\bin`. Quit and restart
Claude Desktop after updating `Path`.

## Related

- [Editor and app integrations](/ai/sandboxes/integrations/claude-desktop/) — how SSH access works and how to
  set it up
- [Claude Code](/ai/sandboxes/integrations/agents/claude-code/) — run the Claude Code CLI inside a
  sandbox
