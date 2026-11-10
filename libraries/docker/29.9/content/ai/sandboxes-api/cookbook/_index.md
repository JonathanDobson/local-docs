---
title: "Docker Sandboxes SDK cookbook"
source: https://docs.docker.com/ai/sandboxes-api/cookbook/
---

# Docker Sandboxes SDK cookbook


Use these recipes to add file transfers, processes, storage, and other sandbox
operations to your application. Each recipe shows the relevant SDK calls and
an expandable complete TypeScript example.

Start with [Get started](/ai/sandboxes-api/get-started/) to run your first sandbox, or
[install the SDK](/ai/sandboxes-api/install/) to use these examples in an existing project.
For HTTP operations and request fields, see the
[API reference](/reference/api/sandboxes/latest/).

## Get started

Authenticate and launch a kit before exploring individual SDK operations.


- [Authenticate to Docker](https://docs.docker.com/ai/sandboxes-api/cookbook/connect-to-cloud-with-a-bearer-token/): Sign in interactively, use a Docker personal access token, or supply an access token from your application.

- [Run a complete example](https://docs.docker.com/ai/sandboxes-api/cookbook/run-a-complete-example/): Sign in, launch the shell kit, print a greeting, and clean up with one runnable program.

- [Create your first sandbox](https://docs.docker.com/ai/sandboxes-api/cookbook/create-your-first-sandbox/): Launch a kit, run a command in its sandbox, and inspect the result.

- [Run agents with kits](https://docs.docker.com/ai/sandboxes-api/cookbook/add-tools-with-kits/): Discover the available kits, launch an agent sandbox, and run work inside it.

- [Run your first command](https://docs.docker.com/ai/sandboxes-api/cookbook/run-your-first-command/): Connect to a running sandbox, run a command in it, and tell a command that exited unsuccessfully apart from a call that failed.

- [Delete a cloud sandbox](https://docs.docker.com/ai/sandboxes-api/cookbook/delete-a-cloud-sandbox/): Delete a sandbox you have read back and wait until it is gone, with the option to override a refusal based on its current state.



## Working in a sandbox

Use a running sandbox for commands, project files, and web applications.


- [Run an interactive shell in a cloud sandbox](https://docs.docker.com/ai/sandboxes-api/cookbook/run-an-interactive-shell-in-a-cloud-sandbox/): Start a shell on a pseudo-terminal, send it input and read its output over one connection, connect again and pick up the output the service kept, and stop it.

- [Copy a file into a cloud sandbox](https://docs.docker.com/ai/sandboxes-api/cookbook/copy-a-file-into-a-cloud-sandbox/): Create a directory inside a running cloud sandbox, write one file into it from memory, and read the size the write reports back.

- [Read files out of a sandbox](https://docs.docker.com/ai/sandboxes-api/cookbook/read-files-out-of-a-sandbox/): List a directory in a running cloud sandbox, download files from it into memory, then move or remove paths inside it.

- [Expose a port from a cloud sandbox](https://docs.docker.com/ai/sandboxes-api/cookbook/expose-a-port-from-a-cloud-sandbox/): Publish a TCP port that a program inside a cloud sandbox listens on, read back the URL that reaches it, list the sandbox's published ports, and withdraw the publication.

- [Stop and restart a sandbox](https://docs.docker.com/ai/sandboxes-api/cookbook/stop-and-restart-a-sandbox/): Stop a running sandbox without deleting it, wait for the stop to settle, and start the same sandbox again when you need it.

- [What your workload starts with](https://docs.docker.com/ai/sandboxes-api/cookbook/what-your-workload-starts-with/): Read the environment variables every command in a sandbox starts with, and see which source wins when two of them set the same name.

- [Run something that produces real output](https://docs.docker.com/ai/sandboxes-api/cookbook/run-something-that-produces-real-output/): Choose between a call that returns a command's captured output when it finishes and a process whose output you read while it runs.



## Packaging and state

Keep an environment or its state for later work.


- [Register and manage an image](https://docs.docker.com/ai/sandboxes-api/cookbook/register-and-manage-an-image/): Register an image with Cloud Sandboxes, get the target to push its content to, check when it is ready, list your images, and delete one you no longer need.

- [Snapshot and fork a sandbox](https://docs.docker.com/ai/sandboxes-api/cookbook/snapshot-and-fork-a-sandbox/): Capture the state of a running sandbox as a snapshot, then start a new sandbox from that snapshot.



## Security and policy

Give agents the access they need without embedding credentials in application code.


- [Control what a sandbox can reach](https://docs.docker.com/ai/sandboxes-api/cookbook/control-what-a-sandbox-can-reach/): Attach your account's network policies to a new sandbox, read the policy the service enforces, and review which destinations it allowed or blocked.

- [Manage cloud secrets](https://docs.docker.com/ai/sandboxes-api/cookbook/manage-cloud-secrets/): Store a token as a stored secret, list your secrets' metadata, replace the token, and delete the secret.

- [Give a sandbox an MCP gateway](https://docs.docker.com/ai/sandboxes-api/cookbook/give-a-sandbox-an-mcp-gateway/): Configure MCP tools when launching a kit, then inspect, authorize, and manage the gateway.

- [Add a Docker credential for cloud sandboxes](https://docs.docker.com/ai/sandboxes-api/cookbook/add-a-docker-credential-for-cloud-sandboxes/): Exchange a Docker OIDC identity token for a credential that the service stores for your sandboxes to use.

- [Get a stored secret into a sandbox](https://docs.docker.com/ai/sandboxes-api/cookbook/get-a-stored-secret-into-a-sandbox/): Store a credential once, then pass its resource name when creating a sandbox so the sandbox starts with that secret attached.

- [Manage network policies](https://docs.docker.com/ai/sandboxes-api/cookbook/manage-network-policies/): Create, read, update, and delete personal network policies through the SDK.



## Connect and configure

Choose a different image, control lifetime, or connect additional storage and clients.


- [Run your own container image](https://docs.docker.com/ai/sandboxes-api/cookbook/run-your-own-container-image/): Start a sandbox from a container image in a registry you name, instead of from a managed image.

- [Keep a cloud sandbox running](https://docs.docker.com/ai/sandboxes-api/cookbook/keep-a-cloud-sandbox-running/): Choose a sandbox's lifetime and what happens when it ends, then renew the lifetime before the deadline passes.

- [Attach persistent storage](https://docs.docker.com/ai/sandboxes-api/cookbook/attach-persistent-storage/): Create a volume, mount it into a new sandbox so its data outlives the sandbox, and delete the volume when you no longer need it.

- [Get an SSH certificate](https://docs.docker.com/ai/sandboxes-api/cookbook/get-an-ssh-certificate/): Have the service sign your SSH public key for one sandbox and return the host, port, username, and host keys your SSH client needs.

- [Get image pull URLs](https://docs.docker.com/ai/sandboxes-api/cookbook/get-image-pull-urls/): Get the manifest details and short-lived download URLs for a managed image so a registry tool can pull its contents.

- [Let a stopped sandbox resume on demand](https://docs.docker.com/ai/sandboxes-api/cookbook/let-a-stopped-sandbox-resume-on-demand/): Choose at creation whether a stopped cloud sandbox starts itself when a request arrives at one of its published ports, then read back the setting in force.



## Requests and responses

Handle request options and failures deliberately.


- [Handle errors and degradation](https://docs.docker.com/ai/sandboxes-api/cookbook/handle-errors-and-degradation/): Tell an API refusal, a failed sandbox transition, and a nonzero command exit apart, and read the code and details each one carries.

- [Retry without creating duplicates](https://docs.docker.com/ai/sandboxes-api/cookbook/retry-without-creating-duplicates/): Retry a sandbox or process create under one request ID so a failure you can't interpret never leaves two copies behind.

- [Page through and filter lists](https://docs.docker.com/ai/sandboxes-api/cookbook/page-through-and-filter-lists/): Walk every page of a list with the SDK's iterators, and narrow a list on the server with a filter and an ordering.

- [Send values the API accepts](https://docs.docker.com/ai/sandboxes-api/cookbook/send-values-the-api-accepts/): Build a create request whose durations, counts, and flags mean what you intend, then read back the values the service settled on.

- [Work within the limits](https://docs.docker.com/ai/sandboxes-api/cookbook/work-within-the-limits/): Choose a supported compute size, understand account quotas, and handle refusals without endless retries.



## Long-running work

Continue work across lost connections or coordinate several sandboxes.


- [Find a process you lost track of](https://docs.docker.com/ai/sandboxes-api/cookbook/find-a-process-you-lost-track-of/): Look up a running process by the session tag you gave it when you created it, then pick up its output from the resume point its own report publishes.

- [Clone a cloud sandbox](https://docs.docker.com/ai/sandboxes-api/cookbook/clone-a-cloud-sandbox/): Read how a running sandbox was configured, then create a second sandbox with the same image and environment.

- [Run work across many sandboxes](https://docs.docker.com/ai/sandboxes-api/cookbook/run-work-across-many-sandboxes/): Run one command on every running sandbox you hold, a bounded number at a time, and read one answer per sandbox even when some of them fail.

- [Recover when the endpoint moves](https://docs.docker.com/ai/sandboxes-api/cookbook/recover-when-the-endpoint-moves/): Read a sandbox again to learn its current endpoint, then run one command through a connection built for that endpoint.
