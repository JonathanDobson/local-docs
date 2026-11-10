# Docker Engine API 1.56 — Container

## GET /v1.56/containers/json

operationId: `ContainerList`

List containers

Returns a list of containers. For details on the format, see the
[inspect endpoint](#operation/ContainerInspect).

Note that it uses a different, smaller representation of a container
than inspecting a single container. For example, the list of linked
containers is not propagated .

| Parameter | In | Type | Required | Description |
|---|---|---|---|---|
| `all` | query | boolean |  | Return all containers. By default, only running containers are shown. |
| `limit` | query | integer |  | Return this number of most recently created containers, including non-running ones. |
| `size` | query | boolean |  | Return the size of container as fields `SizeRw` and `SizeRootFs`. |
| `filters` | query | string |  | Filters to process on the container list, encoded as JSON (a `map[string][]string`). For example, `{"status": ["paused"]}` will only return paused containers. Available filters: - `ancestor`=(`<image-name>[:<tag>]`, `<image id>`, or `<image@digest>`) - `annotation=key` or `annotation="key=value"` of a container annotation - `before`=(`<container id>` or `<container name>`) - `expose`=(`<port>[/<proto>]`\|`<startport-endport>/[<proto>]`) - `exited=<int>` containers with exit code of `<int>` - `health`=(`starting`\|`healthy`\|`unhealthy`\|`none`) - `id=<ID>` a container's ID - `isolation=`(`default`\|`process`\|`hyperv`) (Windows daemon only) - `is-task=`(`true`\|`false`) - `label=key` or `label="key=value"` of a container label - `name=<name>` a container's name - `network`=(`<network id>` or `<network name>`) - `publish`=(`<port>[/<proto>]`\|`<startport-endport>/[<proto>]`) - `since`=(`<container id>` or `<container name>`) - `status=`(`created`\|`restarting`\|`running`\|`removing`\|`paused`\|`exited`\|`dead`) - `volume`=(`<volume name>` or `<mount point destination>`) |

| Response | Description | Body |
|---|---|---|
| 200 | no error | array of `ContainerSummary` |
| 400 | bad parameter | `ErrorResponse` |
| 500 | server error | `ErrorResponse` |

## POST /v1.56/containers/create

operationId: `ContainerCreate`

Create a container

| Parameter | In | Type | Required | Description |
|---|---|---|---|---|
| `name` | query | string |  | Assign the specified name to the container. Must match `/?[a-zA-Z0-9][a-zA-Z0-9_.-]+`. |
| `platform` | query | string |  | Platform in the format `os[/arch[/variant]]` used for image lookup. When specified, the daemon checks if the requested image is present in the local image cache with the given OS and Architecture, and otherwise returns a `404` status. If the option is not set, the host's native OS and Architecture are used to look up the image in the image cache. However, if no platform is passed and the given image does exist in the local image cache, but its OS or architecture does not match, the container is created with the available image, and a warning is added to the `Warnings` field in the response, for example; WARNING: The requested image's platform (linux/arm64/v8) does not match the detected host platform (linux/amd64) and no specific platform was requested |

Request body: allOf(`ContainerConfig`, object)

| Response | Description | Body |
|---|---|---|
| 201 | Container created successfully | `ContainerCreateResponse` |
| 400 | bad parameter | `ErrorResponse` |
| 404 | no such image | `ErrorResponse` |
| 409 | conflict | `ErrorResponse` |
| 500 | server error | `ErrorResponse` |

## GET /v1.56/containers/{id}/json

operationId: `ContainerInspect`

Inspect a container

Return low-level information about a container.

| Parameter | In | Type | Required | Description |
|---|---|---|---|---|
| `id` | path | string | yes | ID or name of the container |
| `size` | query | boolean |  | Return the size of container as fields `SizeRw` and `SizeRootFs` |

| Response | Description | Body |
|---|---|---|
| 200 | no error | `ContainerInspectResponse` |
| 404 | no such container | `ErrorResponse` |
| 500 | server error | `ErrorResponse` |

## GET /v1.56/containers/{id}/top

operationId: `ContainerTop`

List processes running inside a container

On Unix systems, this is done by running the `ps` command. This endpoint
is not supported on Windows.

| Parameter | In | Type | Required | Description |
|---|---|---|---|---|
| `id` | path | string | yes | ID or name of the container |
| `ps_args` | query | string |  | The arguments to pass to `ps`. For example, `aux` |

| Response | Description | Body |
|---|---|---|
| 200 | no error | `ContainerTopResponse` |
| 404 | no such container | `ErrorResponse` |
| 500 | server error | `ErrorResponse` |

## GET /v1.56/containers/{id}/logs

operationId: `ContainerLogs`

Get container logs

Get `stdout` and `stderr` logs from a container.

Note: This endpoint works only for containers with the `json-file` or
`journald` logging driver.

| Parameter | In | Type | Required | Description |
|---|---|---|---|---|
| `id` | path | string | yes | ID or name of the container |
| `follow` | query | boolean |  | Keep connection after returning logs. |
| `stdout` | query | boolean |  | Return logs from `stdout` |
| `stderr` | query | boolean |  | Return logs from `stderr` |
| `since` | query | integer |  | Only return logs since this time, as a UNIX timestamp |
| `until` | query | integer |  | Only return logs before this time, as a UNIX timestamp |
| `timestamps` | query | boolean |  | Add timestamps to every log line |
| `tail` | query | string |  | Only return this number of log lines from the end of the logs. Specify as an integer or `all` to output all log lines. |

| Response | Description | Body |
|---|---|---|
| 200 | logs returned as a stream in response body. For the stream format, [see the documentation for the attach endpoint](#operation/ContainerAttach). Note that unlike the attach endpoint, the logs endpoint does not upgrade the connection and does not set Content-Type. | string (binary) |
| 404 | no such container | `ErrorResponse` |
| 500 | server error | `ErrorResponse` |

## GET /v1.56/containers/{id}/changes

operationId: `ContainerChanges`

Get changes on a container’s filesystem

Returns which files in a container's filesystem have been added, deleted,
or modified. The `Kind` of modification can be one of:

- `0`: Modified ("C")
- `1`: Added ("A")
- `2`: Deleted ("D")

| Parameter | In | Type | Required | Description |
|---|---|---|---|---|
| `id` | path | string | yes | ID or name of the container |

| Response | Description | Body |
|---|---|---|
| 200 | The list of changes | array of `FilesystemChange` |
| 404 | no such container | `ErrorResponse` |
| 500 | server error | `ErrorResponse` |

## GET /v1.56/containers/{id}/export

operationId: `ContainerExport`

Export a container

Export the contents of a container as a tarball.

| Parameter | In | Type | Required | Description |
|---|---|---|---|---|
| `id` | path | string | yes | ID or name of the container |

| Response | Description | Body |
|---|---|---|
| 200 | no error |  |
| 404 | no such container | `ErrorResponse` |
| 500 | server error | `ErrorResponse` |

## GET /v1.56/containers/{id}/stats

operationId: `ContainerStats`

Get container stats based on resource usage

This endpoint returns a live stream of a container’s resource usage
statistics.

The `precpu_stats` is the CPU statistic of the *previous* read, and is
used to calculate the CPU usage percentage. It is not an exact copy
of the `cpu_stats` field.

If either `precpu_stats.online_cpus` or `cpu_stats.online_cpus` is
nil then for compatibility with older daemons the length of the
corresponding `cpu_usage.percpu_usage` array should be used.

On a cgroup v2 host, the following fields are not set
* `blkio_stats`: all fields other than `io_service_bytes_recursive`
* `cpu_stats`: `cpu_usage.percpu_usage`
* `memory_stats`: `max_usage` and `failcnt`
Also, `memory_stats.stats` fields are incompatible with cgroup v1.

To calculate the values shown by the `stats` command of the docker cli tool
the following formulas can be used:
* used_memory = `memory_stats.usage - memory_stats.stats.cache` (cgroups v1)
* used_memory = `memory_stats.usage - memory_stats.stats.inactive_file` (cgroups v2)
* available_memory = `memory_stats.limit`
* Memory usage % = `(used_memory / available_memory) * 100.0`
* cpu_delta = `cpu_stats.cpu_usage.total_usage - precpu_stats.cpu_usage.total_usage`
* system_cpu_delta = `cpu_stats.system_cpu_usage - precpu_stats.system_cpu_usage`
* number_cpus = `length(cpu_stats.cpu_usage.percpu_usage)` or `cpu_stats.online_cpus`
* CPU usage % = `(cpu_delta / system_cpu_delta) * number_cpus * 100.0`

| Parameter | In | Type | Required | Description |
|---|---|---|---|---|
| `id` | path | string | yes | ID or name of the container |
| `stream` | query | boolean |  | Stream the output. If false, the stats will be output once and then it will disconnect. |
| `one-shot` | query | boolean |  | Only get a single stat instead of waiting for 2 cycles. Must be used with `stream=false`. |

| Response | Description | Body |
|---|---|---|
| 200 | no error | `ContainerStatsResponse` |
| 404 | no such container | `ErrorResponse` |
| 500 | server error | `ErrorResponse` |

## POST /v1.56/containers/{id}/resize

operationId: `ContainerResize`

Resize a container TTY

Resize the TTY for a container.

| Parameter | In | Type | Required | Description |
|---|---|---|---|---|
| `id` | path | string | yes | ID or name of the container |
| `h` | query | integer | yes | Height of the TTY session in characters |
| `w` | query | integer | yes | Width of the TTY session in characters |

| Response | Description | Body |
|---|---|---|
| 200 | no error |  |
| 404 | no such container | `ErrorResponse` |
| 500 | cannot resize container | `ErrorResponse` |

## POST /v1.56/containers/{id}/start

operationId: `ContainerStart`

Start a container

| Parameter | In | Type | Required | Description |
|---|---|---|---|---|
| `id` | path | string | yes | ID or name of the container |
| `detachKeys` | query | string |  | Override the key sequence for detaching a container. Format is a single character `[a-Z]` or `ctrl-<value>` where `<value>` is one of: `a-z`, `@`, `^`, `[`, `,` or `_`. |

| Response | Description | Body |
|---|---|---|
| 204 | no error |  |
| 304 | container already started |  |
| 400 | bad parameter, including an invalid checkpoint ID | `ErrorResponse` |
| 404 | no such container | `ErrorResponse` |
| 500 | server error | `ErrorResponse` |

## POST /v1.56/containers/{id}/stop

operationId: `ContainerStop`

Stop a container

| Parameter | In | Type | Required | Description |
|---|---|---|---|---|
| `id` | path | string | yes | ID or name of the container |
| `signal` | query | string |  | Signal to send to the container as an integer or string (e.g. `SIGINT`). |
| `t` | query | integer |  | Number of seconds to wait before killing the container |

| Response | Description | Body |
|---|---|---|
| 204 | no error |  |
| 304 | container already stopped |  |
| 404 | no such container | `ErrorResponse` |
| 500 | server error | `ErrorResponse` |

## POST /v1.56/containers/{id}/restart

operationId: `ContainerRestart`

Restart a container

| Parameter | In | Type | Required | Description |
|---|---|---|---|---|
| `id` | path | string | yes | ID or name of the container |
| `signal` | query | string |  | Signal to send to the container as an integer or string (e.g. `SIGINT`). |
| `t` | query | integer |  | Number of seconds to wait before killing the container |

| Response | Description | Body |
|---|---|---|
| 204 | no error |  |
| 404 | no such container | `ErrorResponse` |
| 500 | server error | `ErrorResponse` |

## POST /v1.56/containers/{id}/kill

operationId: `ContainerKill`

Kill a container

Send a POSIX signal to a container, defaulting to killing to the
container.

| Parameter | In | Type | Required | Description |
|---|---|---|---|---|
| `id` | path | string | yes | ID or name of the container |
| `signal` | query | string |  | Signal to send to the container as an integer or string (e.g. `SIGINT`). |

| Response | Description | Body |
|---|---|---|
| 204 | no error |  |
| 404 | no such container | `ErrorResponse` |
| 409 | container is not running | `ErrorResponse` |
| 500 | server error | `ErrorResponse` |

## POST /v1.56/containers/{id}/update

operationId: `ContainerUpdate`

Update a container

Change various configuration options of a container without having to
recreate it.

| Parameter | In | Type | Required | Description |
|---|---|---|---|---|
| `id` | path | string | yes | ID or name of the container |

Request body: allOf(`Resources`, object)

| Response | Description | Body |
|---|---|---|
| 200 | The container has been updated. | `ContainerUpdateResponse` |
| 404 | no such container | `ErrorResponse` |
| 500 | server error | `ErrorResponse` |

## POST /v1.56/containers/{id}/rename

operationId: `ContainerRename`

Rename a container

| Parameter | In | Type | Required | Description |
|---|---|---|---|---|
| `id` | path | string | yes | ID or name of the container |
| `name` | query | string | yes | New name for the container |

| Response | Description | Body |
|---|---|---|
| 204 | no error |  |
| 404 | no such container | `ErrorResponse` |
| 409 | name already in use | `ErrorResponse` |
| 500 | server error | `ErrorResponse` |

## POST /v1.56/containers/{id}/pause

operationId: `ContainerPause`

Pause a container

Use the freezer cgroup to suspend all processes in a container.

Traditionally, when suspending a process the `SIGSTOP` signal is used,
which is observable by the process being suspended. With the freezer
cgroup the process is unaware, and unable to capture, that it is being
suspended, and subsequently resumed.

| Parameter | In | Type | Required | Description |
|---|---|---|---|---|
| `id` | path | string | yes | ID or name of the container |

| Response | Description | Body |
|---|---|---|
| 204 | no error |  |
| 404 | no such container | `ErrorResponse` |
| 500 | server error | `ErrorResponse` |

## POST /v1.56/containers/{id}/unpause

operationId: `ContainerUnpause`

Unpause a container

Resume a container which has been paused.

| Parameter | In | Type | Required | Description |
|---|---|---|---|---|
| `id` | path | string | yes | ID or name of the container |

| Response | Description | Body |
|---|---|---|
| 204 | no error |  |
| 404 | no such container | `ErrorResponse` |
| 500 | server error | `ErrorResponse` |

## POST /v1.56/containers/{id}/attach

operationId: `ContainerAttach`

Attach to a container

Attach to a container to read its output or send it input. You can attach
to the same container multiple times and you can reattach to containers
that have been detached.

Either the `stream` or `logs` parameter must be `true` for this endpoint
to do anything.

See the [documentation for the `docker attach` command](https://docs.docker.com/engine/reference/commandline/attach/)
for more details.

### Hijacking

This endpoint hijacks the HTTP connection to transport `stdin`, `stdout`,
and `stderr` on the same socket.

This is the response from the daemon for an attach request:

```
HTTP/1.1 200 OK
Content-Type: application/vnd.docker.raw-stream

[STREAM]
```

After the headers and two new lines, the TCP connection can now be used
for raw, bidirectional communication between the client and server.

To hint potential proxies about connection hijacking, the Docker client
can also optionally send connection upgrade headers.

For example, the client sends this request to upgrade the connection:

```
POST /containers/16253994b7c4/attach?stream=1&stdout=1 HTTP/1.1
Upgrade: tcp
Connection: Upgrade
```

The Docker daemon will respond with a `101 UPGRADED` response, and will
similarly follow with the raw stream:

```
HTTP/1.1 101 UPGRADED
Content-Type: application/vnd.docker.raw-stream
Connection: Upgrade
Upgrade: tcp

[STREAM]
```

### Stream format

When the TTY setting is disabled in [`POST /containers/create`](#operation/ContainerCreate),
the HTTP Content-Type header is set to application/vnd.docker.multiplexed-stream
and the stream over the hijacked connected is multiplexed to separate out
`stdout` and `stderr`. The stream consists of a series of frames, each
containing a header and a payload.

The header contains the information which the stream writes (`stdout` or
`stderr`). It also contains the size of the associated frame encoded in
the last four bytes (`uint32`).

It is encoded on the first eight bytes like this:

```go
header := [8]byte{STREAM_TYPE, 0, 0, 0, SIZE1, SIZE2, SIZE3, SIZE4}
```

`STREAM_TYPE` can be:

- 0: `stdin` (is written on `stdout`)
- 1: `stdout`
- 2: `stderr`

`SIZE1, SIZE2, SIZE3, SIZE4` are the four bytes of the `uint32` size
encoded as big endian.

Following the header is the payload, which is the specified number of
bytes of `STREAM_TYPE`.

The simplest way to implement this protocol is the following:

1. Read 8 bytes.
2. Choose `stdout` or `stderr` depending on the first byte.
3. Extract the frame size from the last four bytes.
4. Read the extracted size and output it on the correct output.
5. Goto 1.

### Stream format when using a TTY

When the TTY setting is enabled in [`POST /containers/create`](#operation/ContainerCreate),
the stream is not multiplexed. The data exchanged over the hijacked
connection is simply the raw data from the process PTY and client's
`stdin`.

| Parameter | In | Type | Required | Description |
|---|---|---|---|---|
| `id` | path | string | yes | ID or name of the container |
| `detachKeys` | query | string |  | Override the key sequence for detaching a container.Format is a single character `[a-Z]` or `ctrl-<value>` where `<value>` is one of: `a-z`, `@`, `^`, `[`, `,` or `_`. |
| `logs` | query | boolean |  | Replay previous logs from the container. This is useful for attaching to a container that has started and you want to output everything since the container started. If `stream` is also enabled, once all the previous output has been returned, it will seamlessly transition into streaming current output. |
| `stream` | query | boolean |  | Stream attached streams from the time the request was made onwards. |
| `stdin` | query | boolean |  | Attach to `stdin` |
| `stdout` | query | boolean |  | Attach to `stdout` |
| `stderr` | query | boolean |  | Attach to `stderr` |

| Response | Description | Body |
|---|---|---|
| 101 | no error, hints proxy about hijacking |  |
| 200 | no error, no upgrade header found |  |
| 400 | bad parameter | `ErrorResponse` |
| 404 | no such container | `ErrorResponse` |
| 500 | server error | `ErrorResponse` |

## GET /v1.56/containers/{id}/attach/ws

operationId: `ContainerAttachWebsocket`

Attach to a container via a websocket

| Parameter | In | Type | Required | Description |
|---|---|---|---|---|
| `id` | path | string | yes | ID or name of the container |
| `detachKeys` | query | string |  | Override the key sequence for detaching a container.Format is a single character `[a-Z]` or `ctrl-<value>` where `<value>` is one of: `a-z`, `@`, `^`, `[`, `,`, or `_`. |
| `logs` | query | boolean |  | Return logs |
| `stream` | query | boolean |  | Return stream |
| `stdin` | query | boolean |  | Attach to `stdin` |
| `stdout` | query | boolean |  | Attach to `stdout` |
| `stderr` | query | boolean |  | Attach to `stderr` |

| Response | Description | Body |
|---|---|---|
| 101 | no error, hints proxy about hijacking |  |
| 200 | no error, no upgrade header found |  |
| 400 | bad parameter | `ErrorResponse` |
| 404 | no such container | `ErrorResponse` |
| 500 | server error | `ErrorResponse` |

## POST /v1.56/containers/{id}/wait

operationId: `ContainerWait`

Wait for a container

Block until a container stops, then returns the exit code.

| Parameter | In | Type | Required | Description |
|---|---|---|---|---|
| `id` | path | string | yes | ID or name of the container |
| `condition` | query | string enum: not-running, next-exit, removed |  | Wait until a container state reaches the given condition. Defaults to `not-running` if omitted or empty. |

| Response | Description | Body |
|---|---|---|
| 200 | The container has exit. | `ContainerWaitResponse` |
| 400 | bad parameter | `ErrorResponse` |
| 404 | no such container | `ErrorResponse` |
| 500 | server error | `ErrorResponse` |

## DELETE /v1.56/containers/{id}

operationId: `ContainerDelete`

Remove a container

| Parameter | In | Type | Required | Description |
|---|---|---|---|---|
| `id` | path | string | yes | ID or name of the container |
| `v` | query | boolean |  | Remove anonymous volumes associated with the container. |
| `force` | query | boolean |  | If the container is running, kill it before removing it. |
| `link` | query | boolean |  | Remove the specified link associated with the container. |

| Response | Description | Body |
|---|---|---|
| 204 | no error |  |
| 400 | bad parameter | `ErrorResponse` |
| 404 | no such container | `ErrorResponse` |
| 409 | conflict | `ErrorResponse` |
| 500 | server error | `ErrorResponse` |

## GET /v1.56/containers/{id}/archive

operationId: `ContainerArchive`

Get an archive of a filesystem resource in a container

Get a tar archive of a resource in the filesystem of container id.

| Parameter | In | Type | Required | Description |
|---|---|---|---|---|
| `id` | path | string | yes | ID or name of the container |
| `path` | query | string | yes | Resource in the container’s filesystem to archive. |

| Response | Description | Body |
|---|---|---|
| 200 | no error |  |
| 400 | Bad parameter | `ErrorResponse` |
| 404 | Container or path does not exist | `ErrorResponse` |
| 500 | server error | `ErrorResponse` |

## PUT /v1.56/containers/{id}/archive

operationId: `PutContainerArchive`

Extract an archive of files or folders to a directory in a container

Upload a tar archive to be extracted to a path in the filesystem of container id.
`path` parameter is asserted to be a directory. If it exists as a file, 400 error
will be returned with message "not a directory".

| Parameter | In | Type | Required | Description |
|---|---|---|---|---|
| `id` | path | string | yes | ID or name of the container |
| `path` | query | string | yes | Path to a directory in the container to extract the archive’s contents into. |
| `noOverwriteDirNonDir` | query | string |  | If `1`, `true`, or `True` then it will be an error if unpacking the given content would cause an existing directory to be replaced with a non-directory and vice versa. |
| `copyUIDGID` | query | string |  | If `1`, `true`, then it will copy UID/GID maps to the dest file or dir |

Request body: string (binary)

| Response | Description | Body |
|---|---|---|
| 200 | The content was extracted successfully |  |
| 400 | Bad parameter | `ErrorResponse` |
| 403 | Permission denied, the volume or container rootfs is marked as read-only. | `ErrorResponse` |
| 404 | No such container or path does not exist inside the container | `ErrorResponse` |
| 500 | Server error | `ErrorResponse` |

## HEAD /v1.56/containers/{id}/archive

operationId: `ContainerArchiveInfo`

Get information about files in a container

A response header `X-Docker-Container-Path-Stat` is returned, containing
a base64 - encoded JSON object with some filesystem header information
about the path.

| Parameter | In | Type | Required | Description |
|---|---|---|---|---|
| `id` | path | string | yes | ID or name of the container |
| `path` | query | string | yes | Resource in the container’s filesystem to archive. |

| Response | Description | Body |
|---|---|---|
| 200 | no error |  |
| 400 | Bad parameter | `ErrorResponse` |
| 404 | Container or path does not exist | `ErrorResponse` |
| 500 | Server error | `ErrorResponse` |

## POST /v1.56/containers/prune

operationId: `ContainerPrune`

Delete stopped containers

| Parameter | In | Type | Required | Description |
|---|---|---|---|---|
| `filters` | query | string |  | Filters to process on the prune list, encoded as JSON (a `map[string][]string`). Available filters: - `until=<timestamp>` Prune containers created before this timestamp. The `<timestamp>` can be Unix timestamps, date formatted timestamps, or Go duration strings (e.g. `10m`, `1h30m`) computed relative to the daemon machine’s time. - `label` (`label=<key>`, `label=<key>=<value>`, `label!=<key>`, or `label!=<key>=<value>`) Prune containers with (or without, in case `label!=...` is used) the specified labels. |

| Response | Description | Body |
|---|---|---|
| 200 | No error | object |
| 500 | Server error | `ErrorResponse` |
