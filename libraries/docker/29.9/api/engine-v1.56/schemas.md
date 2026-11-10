# Docker Engine API 1.56 — schemas

## Address

Address represents an IPv4 or IPv6 IP address.

| Field | Type | Required | Description |
|---|---|---|---|
| `Addr` | string |  | IP address. |
| `PrefixLen` | integer |  | Mask length of the IP address. |

## AttestationStatement

AttestationStatement is a single in-toto statement attached to an image.

| Field | Type | Required | Description |
|---|---|---|---|
| `Descriptor` | `OCIDescriptor` | yes |  |
| `PredicateType` | string | yes | The in-toto predicate type URI of this statement. |
| `Statement` | object |  | The verbatim in-toto statement JSON. Only included when the caller opts in via the `statement=true` query parameter; otherwise absent. |

## AuthConfig

| Field | Type | Required | Description |
|---|---|---|---|
| `username` | string |  |  |
| `password` | string |  |  |
| `serveraddress` | string |  |  |

## AuthResponse

An identity token was generated successfully.

| Field | Type | Required | Description |
|---|---|---|---|
| `Status` | string | yes | The status of the authentication |
| `IdentityToken` | string |  | An opaque token used to authenticate a user after a successful login |

## BuildCache

BuildCache contains information about a build cache record.

| Field | Type | Required | Description |
|---|---|---|---|
| `ID` | string |  | Unique ID of the build cache record. |
| `Parents` | array of string |  | List of parent build cache record IDs. |
| `Type` | string enum: internal, frontend, source.local, source.git.checkout, exec.cachemount, regular |  | Cache record type. |
| `Description` | string |  | Description of the build-step that produced the build cache. |
| `InUse` | boolean |  | Indicates if the build cache is in use. |
| `Shared` | boolean |  | Indicates if the build cache is shared. |
| `Size` | integer |  | Amount of disk space used by the build cache (in bytes). |
| `CreatedAt` | string (dateTime) |  | Date and time at which the build cache was created in [RFC 3339](https://www.ietf.org/rfc/rfc3339.txt) format with nano-seconds. |
| `LastUsedAt` | string (dateTime) |  | Date and time at which the build cache was last used in [RFC 3339](https://www.ietf.org/rfc/rfc3339.txt) format with nano-seconds. |
| `UsageCount` | integer |  |  |

## BuildCacheDiskUsage

represents system data usage for build cache resources.

| Field | Type | Required | Description |
|---|---|---|---|
| `ActiveCount` | integer (int64) |  | Count of active build cache records. |
| `TotalCount` | integer (int64) |  | Count of all build cache records. |
| `Reclaimable` | integer (int64) |  | Disk space that can be reclaimed by removing inactive build cache records. |
| `TotalSize` | integer (int64) |  | Disk space in use by build cache records. |
| `Items` | array of object |  | List of build cache records. |

## BuildIdentity

BuildIdentity contains build reference information if image was created via build.

| Field | Type | Required | Description |
|---|---|---|---|
| `Ref` | string |  | Ref is the identifier for the build request. This reference can be used to look up the build details in BuildKit history API. |
| `CreatedAt` | string (date-time) |  | CreatedAt is the time when the build ran. |

## BuildInfo

| Field | Type | Required | Description |
|---|---|---|---|
| `id` | string |  |  |
| `stream` | string |  |  |
| `errorDetail` | `ErrorDetail` |  |  |
| `status` | string |  |  |
| `progressDetail` | `ProgressDetail` |  |  |
| `aux` | `ImageID` |  |  |

## ChangeType

Kind of change

Can be one of:

- `0`: Modified ("C")
- `1`: Added ("A")
- `2`: Deleted ("D")

Type: integer (uint8) enum: 0, 1, 2

## ClusterInfo

ClusterInfo represents information about the swarm as is returned by the
"/info" endpoint. Join-tokens are not included.

| Field | Type | Required | Description |
|---|---|---|---|
| `ID` | string |  | The ID of the swarm. |
| `Version` | `ObjectVersion` |  |  |
| `CreatedAt` | string (dateTime) |  | Date and time at which the swarm was initialised in [RFC 3339](https://www.ietf.org/rfc/rfc3339.txt) format with nano-seconds. |
| `UpdatedAt` | string (dateTime) |  | Date and time at which the swarm was last updated in [RFC 3339](https://www.ietf.org/rfc/rfc3339.txt) format with nano-seconds. |
| `Spec` | `SwarmSpec` |  |  |
| `TLSInfo` | `TLSInfo` |  |  |
| `RootRotationInProgress` | boolean |  | Whether there is currently a root CA rotation in progress for the swarm |
| `DataPathPort` | integer (uint32) |  | DataPathPort specifies the data path port number for data traffic. Acceptable port range is 1024 to 49151. If no port is set or is set to 0, the default port (4789) is used. |
| `DefaultAddrPool` | array of string (CIDR) |  | Default Address Pool specifies default subnet pools for global scope networks. |
| `SubnetSize` | integer (uint32) |  | SubnetSize specifies the subnet size of the networks created from the default subnet pool. |

## ClusterVolume

Options and information specific to, and only present on, Swarm CSI
cluster volumes.

| Field | Type | Required | Description |
|---|---|---|---|
| `ID` | string |  | The Swarm ID of this volume. Because cluster volumes are Swarm objects, they have an ID, unlike non-cluster volumes. This ID can be used to refer to the Volume instead of the name. |
| `Version` | `ObjectVersion` |  |  |
| `CreatedAt` | string (dateTime) |  |  |
| `UpdatedAt` | string (dateTime) |  |  |
| `Spec` | `ClusterVolumeSpec` |  |  |
| `Info` | object |  | Information about the global status of the volume. |
| `PublishStatus` | array of object |  | The status of the volume as it pertains to its publishing and use on specific nodes |

## ClusterVolumeSpec

Cluster-specific options used to create the volume.

| Field | Type | Required | Description |
|---|---|---|---|
| `Group` | string |  | Group defines the volume group of this volume. Volumes belonging to the same group can be referred to by group name when creating Services. Referring to a volume by group instructs Swarm to treat volumes in that group interchangeably for the purpose of scheduling. Volumes with an empty string for a group technically all belong to the same, emptystring group. |
| `AccessMode` | object |  | Defines how the volume is used by tasks. |

## Commit

Commit holds the Git-commit (SHA1) that a binary was built from, as
reported in the version-string of external tools, such as `containerd`,
or `runC`.

| Field | Type | Required | Description |
|---|---|---|---|
| `ID` | string |  | Actual commit ID of external tool. |

## Config

| Field | Type | Required | Description |
|---|---|---|---|
| `ID` | string |  |  |
| `Version` | `ObjectVersion` |  |  |
| `CreatedAt` | string (dateTime) |  |  |
| `UpdatedAt` | string (dateTime) |  |  |
| `Spec` | `ConfigSpec` |  |  |

## ConfigReference

The config-only network source to provide the configuration for
this network.

| Field | Type | Required | Description |
|---|---|---|---|
| `Network` | string |  | The name of the config-only network that provides the network's configuration. The specified network must be an existing config-only network. Only network names are allowed, not network IDs. |

## ConfigSpec

| Field | Type | Required | Description |
|---|---|---|---|
| `Name` | string |  | User-defined name of the config. |
| `Labels` | object |  | User-defined key/value metadata. |
| `Data` | string |  | Data is the data to store as a config, formatted as a standard base64-encoded ([RFC 4648](https://tools.ietf.org/html/rfc4648#section-4)) string. The maximum allowed size is 1000KB, as defined in [MaxConfigSize](https://pkg.go.dev/github.com/moby/swarmkit/v2@v2.0.0-20250103191802-8c1959736554/manager/controlapi#MaxConfigSize). |
| `Templating` | `Driver` |  | Templating driver, if applicable Templating controls whether and how to evaluate the config payload as a template. If no driver is set, no templating is used. |

## ContainerBlkioStatEntry

Blkio stats entry.

This type is Linux-specific and omitted for Windows containers.

| Field | Type | Required | Description |
|---|---|---|---|
| `major` | integer (uint64) |  |  |
| `minor` | integer (uint64) |  |  |
| `op` | string |  |  |
| `value` | integer (uint64) |  |  |

## ContainerBlkioStats

BlkioStats stores all IO service stats for data read and write.

This type is Linux-specific and holds many fields that are specific to cgroups v1.
On a cgroup v2 host, all fields other than `io_service_bytes_recursive`
are omitted or `null`.

This type is only populated on Linux and omitted for Windows containers.

| Field | Type | Required | Description |
|---|---|---|---|
| `io_service_bytes_recursive` | array of `ContainerBlkioStatEntry` |  |  |
| `io_serviced_recursive` | array of `ContainerBlkioStatEntry` |  | This field is only available when using Linux containers with cgroups v1. It is omitted or `null` when using cgroups v2. |
| `io_queue_recursive` | array of `ContainerBlkioStatEntry` |  | This field is only available when using Linux containers with cgroups v1. It is omitted or `null` when using cgroups v2. |
| `io_service_time_recursive` | array of `ContainerBlkioStatEntry` |  | This field is only available when using Linux containers with cgroups v1. It is omitted or `null` when using cgroups v2. |
| `io_wait_time_recursive` | array of `ContainerBlkioStatEntry` |  | This field is only available when using Linux containers with cgroups v1. It is omitted or `null` when using cgroups v2. |
| `io_merged_recursive` | array of `ContainerBlkioStatEntry` |  | This field is only available when using Linux containers with cgroups v1. It is omitted or `null` when using cgroups v2. |
| `io_time_recursive` | array of `ContainerBlkioStatEntry` |  | This field is only available when using Linux containers with cgroups v1. It is omitted or `null` when using cgroups v2. |
| `sectors_recursive` | array of `ContainerBlkioStatEntry` |  | This field is only available when using Linux containers with cgroups v1. It is omitted or `null` when using cgroups v2. |

## ContainerCPUStats

CPU related info of the container

| Field | Type | Required | Description |
|---|---|---|---|
| `cpu_usage` | `ContainerCPUUsage` |  |  |
| `system_cpu_usage` | integer (uint64) |  | System Usage. This field is Linux-specific and omitted for Windows containers. |
| `online_cpus` | integer (uint32) |  | Number of online CPUs. This field is Linux-specific and omitted for Windows containers. |
| `throttling_data` | `ContainerThrottlingData` |  |  |

## ContainerCPUUsage

All CPU stats aggregated since container inception.

| Field | Type | Required | Description |
|---|---|---|---|
| `total_usage` | integer (uint64) |  | Total CPU time consumed in nanoseconds (Linux) or 100's of nanoseconds (Windows). |
| `percpu_usage` | array of integer (uint64) |  | Total CPU time (in nanoseconds) consumed per core (Linux). This field is Linux-specific when using cgroups v1. It is omitted when using cgroups v2 and Windows containers. |
| `usage_in_kernelmode` | integer (uint64) |  | Time (in nanoseconds) spent by tasks of the cgroup in kernel mode (Linux), or time spent (in 100's of nanoseconds) by all container processes in kernel mode (Windows). Not populated for Windows containers using Hyper-V isolation. |
| `usage_in_usermode` | integer (uint64) |  | Time (in nanoseconds) spent by tasks of the cgroup in user mode (Linux), or time spent (in 100's of nanoseconds) by all container processes in kernel mode (Windows). Not populated for Windows containers using Hyper-V isolation. |

## ContainerConfig

Configuration for a container that is portable between hosts.

| Field | Type | Required | Description |
|---|---|---|---|
| `Hostname` | string |  | The hostname to use for the container, as a valid RFC 1123 hostname. |
| `Domainname` | string |  | The domain name to use for the container. |
| `User` | string |  | Commands run as this user inside the container. If omitted, commands run as the user specified in the image the container was started from. Can be either user-name or UID, and optional group-name or GID, separated by a colon (`<user-name\|UID>[<:group-name\|GID>]`). |
| `AttachStdin` | boolean |  | Whether to attach to `stdin`. |
| `AttachStdout` | boolean |  | Whether to attach to `stdout`. |
| `AttachStderr` | boolean |  | Whether to attach to `stderr`. |
| `ExposedPorts` | object |  | An object mapping ports to an empty object in the form: `{"<port>/<tcp\|udp\|sctp>": {}}` |
| `Tty` | boolean |  | Attach standard streams to a TTY, including `stdin` if it is not closed. |
| `OpenStdin` | boolean |  | Open `stdin` |
| `StdinOnce` | boolean |  | Close `stdin` after one attached client disconnects |
| `Env` | array of string |  | A list of environment variables to set inside the container in the form `["VAR=value", ...]`. A variable without `=` is removed from the environment, rather than to have an empty value. |
| `Cmd` | array of string |  | Command to run specified as a string or an array of strings. |
| `Healthcheck` | `HealthConfig` |  |  |
| `ArgsEscaped` | boolean |  | Command is already escaped (Windows only) |
| `Image` | string |  | The name (or reference) of the image to use when creating the container, or which was used when the container was created. |
| `Volumes` | object |  | An object mapping mount point paths inside the container to empty objects. |
| `WorkingDir` | string |  | The working directory for commands to run in. |
| `Entrypoint` | array of string |  | The entry point for the container as a string or an array of strings. If the array consists of exactly one empty string (`[""]`) then the entry point is reset to system default (i.e., the entry point used by docker when there is no `ENTRYPOINT` instruction in the `Dockerfile`). |
| `NetworkDisabled` | boolean |  | Disable networking for the container. |
| `OnBuild` | array of string |  | `ONBUILD` metadata that were defined in the image's `Dockerfile`. |
| `Labels` | object |  | User-defined key/value metadata. |
| `StopSignal` | string |  | Signal to stop a container as a string or unsigned integer. |
| `StopTimeout` | integer |  | Timeout to stop a container in seconds. If omitted, the daemon-wide default (`default-stop-timeout`) is used. |
| `Shell` | array of string |  | Shell for when `RUN`, `CMD`, and `ENTRYPOINT` uses a shell. |

## ContainerCreateResponse

OK response to ContainerCreate operation

| Field | Type | Required | Description |
|---|---|---|---|
| `Id` | string | yes | The ID of the created container |
| `Warnings` | array of string | yes | Warnings encountered when creating the container |

## ContainerInspectResponse

| Field | Type | Required | Description |
|---|---|---|---|
| `Id` | string |  | The ID of this container as a 128-bit (64-character) hexadecimal string (32 bytes). |
| `Created` | string (dateTime) |  | Date and time at which the container was created, formatted in [RFC 3339](https://www.ietf.org/rfc/rfc3339.txt) format with nano-seconds. |
| `Path` | string |  | The path to the command being run |
| `Args` | array of string |  | The arguments to the command being run |
| `State` | `ContainerState` |  |  |
| `Image` | string |  | The ID (digest) of the image that this container was created from. |
| `ResolvConfPath` | string |  | Location of the `/etc/resolv.conf` generated for the container on the host. This file is managed through the docker daemon, and should not be accessed or modified by other tools. |
| `HostnamePath` | string |  | Location of the `/etc/hostname` generated for the container on the host. This file is managed through the docker daemon, and should not be accessed or modified by other tools. |
| `HostsPath` | string |  | Location of the `/etc/hosts` generated for the container on the host. This file is managed through the docker daemon, and should not be accessed or modified by other tools. |
| `LogPath` | string |  | Location of the file used to buffer the container's logs. Depending on the logging-driver used for the container, this field may be omitted. This file is managed through the docker daemon, and should not be accessed or modified by other tools. |
| `Name` | string |  | The name associated with this container. For historic reasons, the name may be prefixed with a forward-slash (`/`). |
| `RestartCount` | integer |  | Number of times the container was restarted since it was created, or since daemon was started. |
| `Driver` | string |  | The storage-driver used for the container's filesystem (graph-driver or snapshotter). |
| `Platform` | string |  | The platform (operating system) for which the container was created. This field was introduced for the experimental "LCOW" (Linux Containers On Windows) features, which has been removed. In most cases, this field is equal to the host's operating system (`linux` or `windows`). |
| `ImageManifestDescriptor` | `OCIDescriptor` |  | OCI descriptor of the platform-specific manifest of the image the container was created from. Note: Only available if the daemon provides a multi-platform image store. |
| `MountLabel` | string |  | SELinux mount label set for the container. |
| `ProcessLabel` | string |  | SELinux process label set for the container. |
| `AppArmorProfile` | string |  | The AppArmor profile set for the container. |
| `ExecIDs` | array of string |  | IDs of exec instances that are running in the container. |
| `HostConfig` | `HostConfig` |  |  |
| `GraphDriver` | `DriverData` |  |  |
| `Storage` | `Storage` |  |  |
| `SizeRw` | integer (int64) |  | The size of files that have been created or changed by this container. This field is omitted by default, and only set when size is requested in the API request. |
| `SizeRootFs` | integer (int64) |  | The total size of all files in the read-only layers from the image that the container uses. These layers can be shared between containers. This field is omitted by default, and only set when size is requested in the API request. |
| `Mounts` | array of `MountPoint` |  | List of mounts used by the container. |
| `Config` | `ContainerConfig` |  |  |
| `NetworkSettings` | `NetworkSettings` |  |  |

## ContainerMemoryStats

Aggregates all memory stats since container inception on Linux.
Windows returns stats for commit and private working set only.

| Field | Type | Required | Description |
|---|---|---|---|
| `usage` | integer (uint64) |  | Current `res_counter` usage for memory. This field is Linux-specific and omitted for Windows containers. |
| `max_usage` | integer (uint64) |  | Maximum usage ever recorded. This field is Linux-specific and only supported on cgroups v1. It is omitted when using cgroups v2 and for Windows containers. |
| `stats` | object |  | All the stats exported via memory.stat. The fields in this object differ between cgroups v1 and v2. On cgroups v1, fields such as `cache`, `rss`, `mapped_file` are available. On cgroups v2, fields such as `file`, `anon`, `inactive_file` are available. This field is Linux-specific and omitted for Windows containers. |
| `failcnt` | integer (uint64) |  | Number of times memory usage hits limits. This field is Linux-specific and only supported on cgroups v1. It is omitted when using cgroups v2 and for Windows containers. |
| `limit` | integer (uint64) |  | This field is Linux-specific and omitted for Windows containers. |
| `commitbytes` | integer (uint64) |  | Committed bytes. This field is Windows-specific and omitted for Linux containers. |
| `commitpeakbytes` | integer (uint64) |  | Peak committed bytes. This field is Windows-specific and omitted for Linux containers. |
| `privateworkingset` | integer (uint64) |  | Private working set. This field is Windows-specific and omitted for Linux containers. |

## ContainerNetworkStats

Aggregates the network stats of one container

| Field | Type | Required | Description |
|---|---|---|---|
| `rx_bytes` | integer (uint64) |  | Bytes received. Windows and Linux. |
| `rx_packets` | integer (uint64) |  | Packets received. Windows and Linux. |
| `rx_errors` | integer (uint64) |  | Received errors. Not used on Windows. This field is Linux-specific and always zero for Windows containers. |
| `rx_dropped` | integer (uint64) |  | Incoming packets dropped. Windows and Linux. |
| `tx_bytes` | integer (uint64) |  | Bytes sent. Windows and Linux. |
| `tx_packets` | integer (uint64) |  | Packets sent. Windows and Linux. |
| `tx_errors` | integer (uint64) |  | Sent errors. Not used on Windows. This field is Linux-specific and always zero for Windows containers. |
| `tx_dropped` | integer (uint64) |  | Outgoing packets dropped. Windows and Linux. |
| `endpoint_id` | string |  | Endpoint ID. Not used on Linux. This field is Windows-specific and omitted for Linux containers. |
| `instance_id` | string |  | Instance ID. Not used on Linux. This field is Windows-specific and omitted for Linux containers. |

## ContainerPidsStats

PidsStats contains Linux-specific stats of a container's process-IDs (PIDs).

This type is Linux-specific and omitted for Windows containers.

| Field | Type | Required | Description |
|---|---|---|---|
| `current` | integer (uint64) |  | Current is the number of PIDs in the cgroup. |
| `limit` | integer (uint64) |  | Limit is the hard limit on the number of pids in the cgroup. A "Limit" of 0 means that there is no limit. |

## ContainerState

ContainerState stores container's running state. It's part of ContainerJSONBase
and will be returned by the "inspect" command.

| Field | Type | Required | Description |
|---|---|---|---|
| `Status` | string enum: created, running, paused, restarting, removing, exited, dead |  | String representation of the container state. Can be one of "created", "running", "paused", "restarting", "removing", "exited", or "dead". |
| `Running` | boolean |  | Whether this container is running. Note that a running container can be _paused_. The `Running` and `Paused` booleans are not mutually exclusive: When pausing a container (on Linux), the freezer cgroup is used to suspend all processes in the container. Freezing the process requires the process to be running. As a result, paused containers are both `Running` _and_ `Paused`. Use the `Status` field instead to determine if a container's state is "running". |
| `Paused` | boolean |  | Whether this container is paused. |
| `Restarting` | boolean |  | Whether this container is restarting. |
| `OOMKilled` | boolean |  | Whether a process within this container has been killed because it ran out of memory since the container was last started. |
| `Dead` | boolean |  |  |
| `Pid` | integer |  | The process ID of this container |
| `ExitCode` | integer |  | The last exit code of this container |
| `Error` | string |  |  |
| `StartedAt` | string |  | The time when this container was last started. |
| `FinishedAt` | string |  | The time when this container last exited. |
| `Health` | `Health` |  |  |

## ContainerStatsResponse

Statistics sample for a container.

| Field | Type | Required | Description |
|---|---|---|---|
| `id` | string |  | ID of the container for which the stats were collected. |
| `name` | string |  | Name of the container for which the stats were collected. |
| `os_type` | string |  | OSType is the OS of the container ("linux" or "windows") to allow platform-specific handling of stats. |
| `read` | string (date-time) |  | Date and time at which this sample was collected. The value is formatted as [RFC 3339](https://www.ietf.org/rfc/rfc3339.txt) with nano-seconds. |
| `cpu_stats` | `ContainerCPUStats` |  |  |
| `memory_stats` | `ContainerMemoryStats` |  |  |
| `networks` | object |  | Network statistics for the container per interface. This field is omitted if the container has no networking enabled. |
| `pids_stats` | `ContainerPidsStats` |  |  |
| `blkio_stats` | `ContainerBlkioStats` |  |  |
| `num_procs` | integer (uint32) |  | The number of processors on the system. This field is Windows-specific and always zero for Linux containers. |
| `storage_stats` | `ContainerStorageStats` |  |  |
| `preread` | string (date-time) |  | Date and time at which this first sample was collected. This field is not propagated if the "one-shot" option is set. If the "one-shot" option is set, this field may be omitted, empty, or set to a default date (`0001-01-01T00:00:00Z`). The value is formatted as [RFC 3339](https://www.ietf.org/rfc/rfc3339.txt) with nano-seconds. |
| `precpu_stats` | `ContainerCPUStats` |  |  |

## ContainerStatus

represents the status of a container.

| Field | Type | Required | Description |
|---|---|---|---|
| `ContainerID` | string |  |  |
| `PID` | integer |  |  |
| `ExitCode` | integer |  |  |

## ContainerStorageStats

StorageStats is the disk I/O stats for read/write on Windows.

This type is Windows-specific and omitted for Linux containers.

| Field | Type | Required | Description |
|---|---|---|---|
| `read_count_normalized` | integer (uint64) |  |  |
| `read_size_bytes` | integer (uint64) |  |  |
| `write_count_normalized` | integer (uint64) |  |  |
| `write_size_bytes` | integer (uint64) |  |  |

## ContainerSummary

| Field | Type | Required | Description |
|---|---|---|---|
| `Id` | string |  | The ID of this container as a 128-bit (64-character) hexadecimal string (32 bytes). |
| `Names` | array of string |  | The names associated with this container. Most containers have a single name, but when using legacy "links", the container can have multiple names. For historic reasons, names are prefixed with a forward-slash (`/`). |
| `Image` | string |  | The name or ID of the image used to create the container. This field shows the image reference as was specified when creating the container, which can be in its canonical form (e.g., `docker.io/library/ubuntu:latest` or `docker.io/library/ubuntu@sha256:72297848456d5d37d1262630108ab308d3e9ec7ed1c3286a32fe09856619a782`), short form (e.g., `ubuntu:latest`)), or the ID(-prefix) of the image (e.g., `72297848456d`). The content of this field can be updated at runtime if the image used to create the container is untagged, in which case the field is updated to contain the the image ID (digest) it was resolved to in its canonical, non-truncated form (e.g., `sha256:72297848456d5d37d1262630108ab308d3e9ec7ed1c3286a32fe09856619a782`). |
| `ImageID` | string |  | The ID (digest) of the image that this container was created from. |
| `ImageManifestDescriptor` | `OCIDescriptor` |  | OCI descriptor of the platform-specific manifest of the image the container was created from. Note: Only available if the daemon provides a multi-platform image store. This field is not populated in the `GET /system/df` endpoint. |
| `Command` | string |  | Command to run when starting the container |
| `Created` | integer (int64) |  | Date and time at which the container was created as a Unix timestamp (number of seconds since EPOCH). |
| `Ports` | array of `PortSummary` |  | Port-mappings for the container. |
| `SizeRw` | integer (int64) |  | The size of files that have been created or changed by this container. This field is omitted by default, and only set when size is requested in the API request. |
| `SizeRootFs` | integer (int64) |  | The total size of all files in the read-only layers from the image that the container uses. These layers can be shared between containers. This field is omitted by default, and only set when size is requested in the API request. |
| `Labels` | object |  | User-defined key/value metadata. |
| `State` | string enum: created, running, paused, restarting, exited, removing, dead |  | The state of this container. |
| `Status` | string |  | Additional human-readable status of this container (e.g. `Exit 0`) |
| `HostConfig` | object |  | Summary of host-specific runtime information of the container. This is a reduced set of information in the container's "HostConfig" as available in the container "inspect" response. |
| `NetworkSettings` | object |  | Summary of the container's network settings |
| `Mounts` | array of `MountPoint` |  | List of mounts used by the container. |
| `Health` | object |  | Summary of health status Added in v1.52, before that version all container summary not include Health. After this attribute introduced, it includes containers with no health checks configured, or containers that are not running with none |

## ContainerThrottlingData

CPU throttling stats of the container.

This type is Linux-specific and omitted for Windows containers.

| Field | Type | Required | Description |
|---|---|---|---|
| `periods` | integer (uint64) |  | Number of periods with throttling active. |
| `throttled_periods` | integer (uint64) |  | Number of periods when the container hit its throttling limit. |
| `throttled_time` | integer (uint64) |  | Aggregated time (in nanoseconds) the container was throttled for. |

## ContainerTopResponse

Container "top" response.

| Field | Type | Required | Description |
|---|---|---|---|
| `Titles` | array of string |  | The ps column titles |
| `Processes` | array of array of string |  | Each process running in the container, where each process is an array of values corresponding to the titles. |

## ContainerUpdateResponse

Response for a successful container-update.

| Field | Type | Required | Description |
|---|---|---|---|
| `Warnings` | array of string |  | Warnings encountered when updating the container. |

## ContainerWaitExitError

container waiting error, if any

| Field | Type | Required | Description |
|---|---|---|---|
| `Message` | string |  | Details of an error |

## ContainerWaitResponse

OK response to ContainerWait operation

| Field | Type | Required | Description |
|---|---|---|---|
| `StatusCode` | integer (int64) | yes | Exit code of the container |
| `Error` | `ContainerWaitExitError` |  |  |

## ContainerdInfo

Information for connecting to the containerd instance that is used by the daemon.
This is included for debugging purposes only.

| Field | Type | Required | Description |
|---|---|---|---|
| `Address` | string |  | The address of the containerd socket. |
| `Namespaces` | object |  | The namespaces that the daemon uses for running containers and plugins in containerd. These namespaces can be configured in the daemon configuration, and are considered to be used exclusively by the daemon, Tampering with the containerd instance may cause unexpected behavior. As these namespaces are considered to be exclusively accessed by the daemon, it is not recommended to change these values, or to change them to a value that is used by other systems, such as cri-containerd. |

## ContainersDiskUsage

represents system data usage information for container resources.

| Field | Type | Required | Description |
|---|---|---|---|
| `ActiveCount` | integer (int64) |  | Count of active containers. |
| `TotalCount` | integer (int64) |  | Count of all containers. |
| `Reclaimable` | integer (int64) |  | Disk space that can be reclaimed by removing inactive containers. |
| `TotalSize` | integer (int64) |  | Disk space in use by containers. |
| `Items` | array of object |  | List of container summaries. |

## CreateImageInfo

| Field | Type | Required | Description |
|---|---|---|---|
| `id` | string |  |  |
| `errorDetail` | `ErrorDetail` |  |  |
| `status` | string |  |  |
| `progressDetail` | `ProgressDetail` |  |  |

## DeviceInfo

DeviceInfo represents a device that can be used by a container.

| Field | Type | Required | Description |
|---|---|---|---|
| `Source` | string |  | The origin device driver. |
| `ID` | string |  | The unique identifier for the device within its source driver. For CDI devices, this would be an FQDN like "vendor.com/gpu=0". |

## DeviceMapping

A device mapping between the host and container

| Field | Type | Required | Description |
|---|---|---|---|
| `PathOnHost` | string |  |  |
| `PathInContainer` | string |  |  |
| `CgroupPermissions` | string |  |  |

## DeviceRequest

A request for devices to be sent to device drivers

| Field | Type | Required | Description |
|---|---|---|---|
| `Driver` | string |  | The name of the device driver to use for this request. Note that if this is specified the capabilities are ignored when selecting a device driver. |
| `Count` | integer |  |  |
| `DeviceIDs` | array of string |  |  |
| `Capabilities` | array of array of string |  | A list of capabilities; an OR list of AND lists of capabilities. Note that if a driver is specified the capabilities have no effect on selecting a driver as the driver name is used directly. Note that if no driver is specified the capabilities are used to select a driver with the required capabilities. |
| `Options` | object |  | Driver-specific options, specified as a key/value pairs. These options are passed directly to the driver. |

## DistributionInspect

Describes the result obtained from contacting the registry to retrieve
image metadata.

| Field | Type | Required | Description |
|---|---|---|---|
| `Descriptor` | `OCIDescriptor` | yes |  |
| `Platforms` | array of `OCIPlatform` | yes | An array containing all platforms supported by the image. |

## Driver

Driver represents a driver (network, logging, secrets).

| Field | Type | Required | Description |
|---|---|---|---|
| `Name` | string | yes | Name of the driver. |
| `Options` | object |  | Key/value map of driver-specific options. |

## DriverData

Information about the storage driver used to store the container's and
image's filesystem.

| Field | Type | Required | Description |
|---|---|---|---|
| `Name` | string | yes | Name of the storage driver. |
| `Data` | object | yes | Low-level storage metadata, provided as key/value pairs. This information is driver-specific, and depends on the storage-driver in use, and should be used for informational purposes only. |

## EndpointIPAMConfig

EndpointIPAMConfig represents an endpoint's IPAM configuration.

| Field | Type | Required | Description |
|---|---|---|---|
| `IPv4Address` | string |  |  |
| `IPv6Address` | string |  |  |
| `LinkLocalIPs` | array of string |  |  |

## EndpointPortConfig

| Field | Type | Required | Description |
|---|---|---|---|
| `Name` | string |  |  |
| `Protocol` | string enum: tcp, udp, sctp |  |  |
| `TargetPort` | integer |  | The port inside the container. |
| `PublishedPort` | integer |  | The port on the swarm hosts. |
| `PublishMode` | string enum: ingress, host |  | The mode in which port is published. <p><br /></p> - "ingress" makes the target port accessible on every node, regardless of whether there is a task for the service running on that node or not. - "host" bypasses the routing mesh and publish the port directly on the swarm node where that service is running. |

## EndpointResource

contains network resources allocated and used for a container in a network.

| Field | Type | Required | Description |
|---|---|---|---|
| `Name` | string |  |  |
| `EndpointID` | string |  |  |
| `MacAddress` | string |  |  |
| `IPv4Address` | string |  |  |
| `IPv6Address` | string |  |  |

## EndpointSettings

Configuration for a network endpoint.

| Field | Type | Required | Description |
|---|---|---|---|
| `IPAMConfig` | `EndpointIPAMConfig` |  |  |
| `Links` | array of string |  |  |
| `MacAddress` | string |  | MAC address for the endpoint on this network. The network driver might ignore this parameter. |
| `Aliases` | array of string |  |  |
| `DriverOpts` | object |  | DriverOpts is a mapping of driver options and values. These options are passed directly to the driver and are driver specific. |
| `GwPriority` | integer (int64) |  | This property determines which endpoint will provide the default gateway for a container. The endpoint with the highest priority will be used. If multiple endpoints have the same priority, endpoints are lexicographically sorted based on their network name, and the one that sorts first is picked. |
| `NetworkID` | string |  | Unique ID of the network. |
| `EndpointID` | string |  | Unique ID for the service endpoint in a Sandbox. |
| `Gateway` | string |  | Gateway address for this network. |
| `IPAddress` | string |  | IPv4 address. |
| `IPPrefixLen` | integer |  | Mask length of the IPv4 address. |
| `IPv6Gateway` | string |  | IPv6 gateway address. |
| `GlobalIPv6Address` | string |  | Global IPv6 address. |
| `GlobalIPv6PrefixLen` | integer (int64) |  | Mask length of the global IPv6 address. |
| `DNSNames` | array of string |  | List of all DNS names an endpoint has on a specific network. This list is based on the container name, network aliases, container short ID, and hostname. These DNS names are non-fully qualified but can contain several dots. You can get fully qualified DNS names by appending `.<network-name>`. For instance, if container name is `my.ctr` and the network is named `testnet`, `DNSNames` will contain `my.ctr` and the FQDN will be `my.ctr.testnet`. |

## EndpointSpec

Properties that can be configured to access and load balance a service.

| Field | Type | Required | Description |
|---|---|---|---|
| `Mode` | string enum: vip, dnsrr |  | The mode of resolution to use for internal load balancing between tasks. |
| `Ports` | array of `EndpointPortConfig` |  | List of exposed ports that this service is accessible on from the outside. Ports can only be provided if `vip` resolution mode is used. |

## EngineDescription

EngineDescription provides information about an engine.

| Field | Type | Required | Description |
|---|---|---|---|
| `EngineVersion` | string |  |  |
| `Labels` | object |  |  |
| `Plugins` | array of object |  |  |

## ErrorDetail

| Field | Type | Required | Description |
|---|---|---|---|
| `code` | integer |  |  |
| `message` | string |  |  |

## ErrorResponse

Represents an error.

| Field | Type | Required | Description |
|---|---|---|---|
| `message` | string | yes | The error message. |

## EventActor

Actor describes something that generates events, like a container, network,
or a volume.

| Field | Type | Required | Description |
|---|---|---|---|
| `ID` | string |  | The ID of the object emitting the event |
| `Attributes` | object |  | Various key/value attributes of the object, depending on its type. |

## EventMessage

EventMessage represents the information an event contains.

| Field | Type | Required | Description |
|---|---|---|---|
| `Type` | string enum: builder, config, container, daemon, image, network, node, plugin, secret, service, volume |  | The type of object emitting the event |
| `Action` | string |  | The type of event |
| `Actor` | `EventActor` |  |  |
| `scope` | string enum: local, swarm |  | Scope of the event. Engine events are `local` scope. Cluster (Swarm) events are `swarm` scope. |
| `time` | integer (int64) |  | Timestamp of event |
| `timeNano` | integer (int64) |  | Timestamp of event, with nanosecond accuracy |

## FilesystemChange

Change in the container's filesystem.

| Field | Type | Required | Description |
|---|---|---|---|
| `Path` | string | yes | Path to file or directory that has changed. |
| `Kind` | `ChangeType` | yes |  |

## FirewallInfo

Information about the daemon's firewalling configuration.

This field is currently only used on Linux, and omitted on other platforms.

| Field | Type | Required | Description |
|---|---|---|---|
| `Driver` | string |  | The name of the firewall backend driver. |
| `Info` | array of array of string |  | Information about the firewall backend, provided as "label" / "value" pairs. <p><br /></p> > **Note**: The information returned in this field, including the > formatting of values and labels, should not be considered stable, > and may change without notice. |

## GenericResources

User-defined resources can be either Integer resources (e.g, `SSD=3`) or
String resources (e.g, `GPU=UUID1`).

Type: array of object

## Health

Health stores information about the container's healthcheck results.

| Field | Type | Required | Description |
|---|---|---|---|
| `Status` | string enum: none, starting, healthy, unhealthy |  | Status is one of `none`, `starting`, `healthy` or `unhealthy` - "none" Indicates there is no healthcheck - "starting" Starting indicates that the container is not yet ready - "healthy" Healthy indicates that the container is running correctly - "unhealthy" Unhealthy indicates that the container has a problem |
| `FailingStreak` | integer |  | FailingStreak is the number of consecutive failures |
| `Log` | array of `HealthcheckResult` |  | Log contains the last few results (oldest first) |

## HealthConfig

A test to perform to check that the container is healthy.
Healthcheck commands should be side-effect free.

| Field | Type | Required | Description |
|---|---|---|---|
| `Test` | array of string |  | The test to perform. Possible values are: - `[]` inherit healthcheck from image or parent image - `["NONE"]` disable healthcheck - `["CMD", args...]` exec arguments directly - `["CMD-SHELL", command]` run command with system's default shell A non-zero exit code indicates a failed healthcheck: - `0` healthy - `1` unhealthy - `2` reserved (treated as unhealthy) - other values: error running probe |
| `Interval` | integer (int64) |  | The time to wait between checks in nanoseconds. It should be 0 or at least 1000000 (1 ms). 0 means inherit. |
| `Timeout` | integer (int64) |  | The time to wait before considering the check to have hung. It should be 0 or at least 1000000 (1 ms). 0 means inherit. If the health check command does not complete within this timeout, the check is considered failed and the health check process is forcibly terminated without a graceful shutdown. |
| `Retries` | integer |  | The number of consecutive failures needed to consider a container as unhealthy. 0 means inherit. |
| `StartPeriod` | integer (int64) |  | Start period for the container to initialize before starting health-retries countdown in nanoseconds. It should be 0 or at least 1000000 (1 ms). 0 means inherit. |
| `StartInterval` | integer (int64) |  | The time to wait between checks in nanoseconds during the start period. It should be 0 or at least 1000000 (1 ms). 0 means inherit. |

## HealthcheckResult

HealthcheckResult stores information about a single run of a healthcheck probe

| Field | Type | Required | Description |
|---|---|---|---|
| `Start` | string (date-time) |  | Date and time at which this check started in [RFC 3339](https://www.ietf.org/rfc/rfc3339.txt) format with nano-seconds. |
| `End` | string (dateTime) |  | Date and time at which this check ended in [RFC 3339](https://www.ietf.org/rfc/rfc3339.txt) format with nano-seconds. |
| `ExitCode` | integer |  | ExitCode meanings: - `0` healthy - `1` unhealthy - `2` reserved (considered unhealthy) - other values: error running probe |
| `Output` | string |  | Output from last check |

## HostConfig

Container configuration that depends on the host we are running on

Type: allOf(`Resources`, object)

## IDResponse

Response to an API call that returns just an Id

| Field | Type | Required | Description |
|---|---|---|---|
| `Id` | string | yes | The id of the newly created object. |

## IPAM

| Field | Type | Required | Description |
|---|---|---|---|
| `Driver` | string |  | Name of the IPAM driver to use. |
| `Config` | array of `IPAMConfig` |  | List of IPAM configuration options, specified as a map: ``` {"Subnet": <CIDR>, "IPRange": <CIDR>, "Gateway": <IP address>, "AuxAddress": <device_name:IP address>} ``` |
| `Options` | object |  | Driver-specific options, specified as a map. |

## IPAMConfig

| Field | Type | Required | Description |
|---|---|---|---|
| `Subnet` | string |  |  |
| `IPRange` | string |  |  |
| `Gateway` | string |  |  |
| `AuxiliaryAddresses` | object |  |  |

## IPAMStatus

| Field | Type | Required | Description |
|---|---|---|---|
| `Subnets` | object |  |  |

## Identity

Identity holds information about the identity and origin of the image.
This is trusted information verified by the daemon and cannot be modified
by tagging an image to a different name.

| Field | Type | Required | Description |
|---|---|---|---|
| `Signature` | array of `SignatureIdentity` |  | Signature contains the properties of verified signatures for the image. |
| `Pull` | array of `PullIdentity` |  | Pull contains remote location information if image was created via pull. If image was pulled via mirror, this contains the original repository location. After successful push this images also contains the pushed repository location. |
| `Build` | array of `BuildIdentity` |  | Build contains build reference information if image was created via build. |

## ImageConfig

Configuration of the image. These fields are used as defaults
when starting a container from the image.

| Field | Type | Required | Description |
|---|---|---|---|
| `User` | string |  | The user that commands are run as inside the container. |
| `ExposedPorts` | object |  | An object mapping ports to an empty object in the form: `{"<port>/<tcp\|udp\|sctp>": {}}` |
| `Env` | array of string |  | A list of environment variables to set inside the container in the form `["VAR=value", ...]`. A variable without `=` is removed from the environment, rather than to have an empty value. |
| `Cmd` | array of string |  | Command to run specified as a string or an array of strings. |
| `Healthcheck` | `HealthConfig` |  |  |
| `ArgsEscaped` | boolean |  | Command is already escaped (Windows only) |
| `Volumes` | object |  | An object mapping mount point paths inside the container to empty objects. |
| `WorkingDir` | string |  | The working directory for commands to run in. |
| `Entrypoint` | array of string |  | The entry point for the container as a string or an array of strings. If the array consists of exactly one empty string (`[""]`) then the entry point is reset to system default (i.e., the entry point used by docker when there is no `ENTRYPOINT` instruction in the `Dockerfile`). |
| `OnBuild` | array of string |  | `ONBUILD` metadata that were defined in the image's `Dockerfile`. |
| `Labels` | object |  | User-defined key/value metadata. |
| `StopSignal` | string |  | Signal to stop a container as a string or unsigned integer. |
| `Shell` | array of string |  | Shell for when `RUN`, `CMD`, and `ENTRYPOINT` uses a shell. |

## ImageDeleteResponseItem

| Field | Type | Required | Description |
|---|---|---|---|
| `Untagged` | string |  | The image ID of an image that was untagged |
| `Deleted` | string |  | The image ID of an image that was deleted |

## ImageHistoryResponseItem

individual image layer information in response to ImageHistory operation

| Field | Type | Required | Description |
|---|---|---|---|
| `Id` | string | yes |  |
| `Created` | integer (int64) | yes |  |
| `CreatedBy` | string | yes |  |
| `Tags` | array of string | yes |  |
| `Size` | integer (int64) | yes |  |
| `Comment` | string | yes |  |

## ImageID

Image ID or Digest

| Field | Type | Required | Description |
|---|---|---|---|
| `ID` | string |  |  |

## ImageInspect

Information about an image in the local image cache.

| Field | Type | Required | Description |
|---|---|---|---|
| `Id` | string |  | ID is the content-addressable ID of an image. This identifier is a content-addressable digest calculated from the image's configuration (which includes the digests of layers used by the image). Note that this digest differs from the `RepoDigests` below, which holds digests of image manifests that reference the image. |
| `Descriptor` | `OCIDescriptor` |  | Descriptor is an OCI descriptor of the image target. In case of a multi-platform image, this descriptor points to the OCI index or a manifest list. This field is only present if the daemon provides a multi-platform image store. WARNING: This is experimental and may change at any time without any backward compatibility. |
| `Manifests` | array of `ImageManifestSummary` |  | Manifests is a list of image manifests available in this image. It provides a more detailed view of the platform-specific image manifests or other image-attached data like build attestations. Only available if the daemon provides a multi-platform image store and the `manifests` option is set in the inspect request. WARNING: This is experimental and may change at any time without any backward compatibility. |
| `Identity` | `Identity` |  | Identity holds information about the identity and origin of the image. This is trusted information verified by the daemon and cannot be modified by tagging an image to a different name. |
| `RepoTags` | array of string |  | List of image names/tags in the local image cache that reference this image. Multiple image tags can refer to the same image, and this list may be empty if no tags reference the image, in which case the image is "untagged", in which case it can still be referenced by its ID. |
| `RepoDigests` | array of string |  | List of content-addressable digests of locally available image manifests that the image is referenced from. Multiple manifests can refer to the same image. These digests are usually only available if the image was either pulled from a registry, or if the image was pushed to a registry, which is when the manifest is generated and its digest calculated. |
| `Comment` | string |  | Optional message that was set when committing or importing the image. |
| `Created` | string (dateTime) |  | Date and time at which the image was created, formatted in [RFC 3339](https://www.ietf.org/rfc/rfc3339.txt) format with nano-seconds. This information is only available if present in the image, and omitted otherwise. |
| `Author` | string |  | Name of the author that was specified when committing the image, or as specified through MAINTAINER (deprecated) in the Dockerfile. |
| `Config` | `ImageConfig` |  |  |
| `Architecture` | string |  | Hardware CPU architecture that the image runs on. |
| `Variant` | string |  | CPU architecture variant (presently ARM-only). |
| `Os` | string |  | Operating System the image is built to run on. |
| `OsVersion` | string |  | Operating System version the image is built to run on (especially for Windows). |
| `Size` | integer (int64) |  | Total size of the image variant, including all layers it is composed of. For multi-platform images, this is the size of the platform variant selected by the `platform` query parameter. If no platform is specified, the daemon selects a platform as described in the `platform` parameter. When using the containerd image store, this includes both the image content that's present locally and the unpacked snapshot data for the selected variant. Image data may be shared between images, so this size does not indicate how much space would be reclaimed by deleting the image. |
| `GraphDriver` | `DriverData` |  |  |
| `RootFS` | object |  | Information about the image's RootFS, including the layer IDs. |
| `Metadata` | object |  | Additional metadata of the image in the local cache. This information is local to the daemon, and not part of the image itself. |

## ImageManifestSummary

ImageManifestSummary represents a summary of an image manifest.

| Field | Type | Required | Description |
|---|---|---|---|
| `ID` | string | yes | ID is the content-addressable ID of an image and is the same as the digest of the image manifest. |
| `Descriptor` | `OCIDescriptor` | yes |  |
| `Available` | boolean | yes | Indicates whether all the child content (image config, layers) is fully available locally. |
| `Size` | object | yes |  |
| `Kind` | string enum: image, attestation, unknown | yes | The kind of the manifest. kind \| description -------------\|----------------------------------------------------------- image \| Image manifest that can be used to start a container. attestation \| Attestation manifest produced by the Buildkit builder for a specific image manifest. |
| `ImageData` | object |  | The image data for the image manifest. This field is only populated when Kind is "image". |
| `AttestationData` | object |  | The image data for the attestation manifest. This field is only populated when Kind is "attestation". |

## ImageSummary

| Field | Type | Required | Description |
|---|---|---|---|
| `Id` | string | yes | ID is the content-addressable ID of an image. This identifier is a content-addressable digest calculated from the image's configuration (which includes the digests of layers used by the image). Note that this digest differs from the `RepoDigests` below, which holds digests of image manifests that reference the image. |
| `ParentId` | string | yes | ID of the parent image. Depending on how the image was created, this field may be empty and is only set for images that were built/created locally. This field is empty if the image was pulled from an image registry. |
| `RepoTags` | array of string | yes | List of image names/tags in the local image cache that reference this image. Multiple image tags can refer to the same image, and this list may be empty if no tags reference the image, in which case the image is "untagged", in which case it can still be referenced by its ID. |
| `RepoDigests` | array of string | yes | List of content-addressable digests of locally available image manifests that the image is referenced from. Multiple manifests can refer to the same image. These digests are usually only available if the image was either pulled from a registry, or if the image was pushed to a registry, which is when the manifest is generated and its digest calculated. |
| `Created` | integer | yes | Date and time at which the image was created as a Unix timestamp (number of seconds since EPOCH). |
| `Size` | integer (int64) | yes | Total size of the image including all layers it is composed of. |
| `SharedSize` | integer (int64) | yes | Total size of image layers that are shared between this image and other images. This size is not calculated by default. `-1` indicates that the value has not been set / calculated. |
| `Labels` | object | yes | User-defined key/value metadata. |
| `Containers` | integer | yes | Number of containers using this image. Includes both stopped and running containers. `-1` indicates that the value has not been set / calculated. |
| `Manifests` | array of `ImageManifestSummary` |  | Manifests is a list of manifests available in this image. It provides a more detailed view of the platform-specific image manifests or other image-attached data like build attestations. WARNING: This is experimental and may change at any time without any backward compatibility. |
| `Descriptor` | `OCIDescriptor` |  | Descriptor is an OCI descriptor of the image target. In case of a multi-platform image, this descriptor points to the OCI index or a manifest list. This field is only present if the daemon provides a multi-platform image store. WARNING: This is experimental and may change at any time without any backward compatibility. |

## ImagesDiskUsage

represents system data usage for image resources.

| Field | Type | Required | Description |
|---|---|---|---|
| `ActiveCount` | integer (int64) |  | Count of active images. |
| `TotalCount` | integer (int64) |  | Count of all images. |
| `Reclaimable` | integer (int64) |  | Disk space that can be reclaimed by removing unused images. |
| `TotalSize` | integer (int64) |  | Disk space in use by images. |
| `Items` | array of object |  | List of image summaries. |

## IndexInfo

IndexInfo contains information about a registry.

| Field | Type | Required | Description |
|---|---|---|---|
| `Name` | string |  | Name of the registry, such as "docker.io". |
| `Mirrors` | array of string |  | List of mirrors, expressed as URIs. |
| `Secure` | boolean |  | Indicates if the registry is part of the list of insecure registries. If `false`, the registry is insecure. Insecure registries accept un-encrypted (HTTP) and/or untrusted (HTTPS with certificates from unknown CAs) communication. > **Warning**: Insecure registries can be useful when running a local > registry. However, because its use creates security vulnerabilities > it should ONLY be enabled for testing purposes. For increased > security, users should add their CA to their system's list of > trusted CAs instead of enabling this option. |
| `Official` | boolean |  | Indicates whether this is an official registry (i.e., Docker Hub / docker.io) |

## JoinTokens

JoinTokens contains the tokens workers and managers need to join the swarm.

| Field | Type | Required | Description |
|---|---|---|---|
| `Worker` | string |  | The token workers can use to join the swarm. |
| `Manager` | string |  | The token managers can use to join the swarm. |

## KnownSignerIdentity

KnownSignerIdentity is an identifier for a special signer identity that is known to the implementation.

Type: string enum: DHI

## Limit

An object describing a limit on resources which can be requested by a task.

| Field | Type | Required | Description |
|---|---|---|---|
| `NanoCPUs` | integer (int64) |  |  |
| `MemoryBytes` | integer (int64) |  |  |
| `Pids` | integer (int64) |  | Limits the maximum number of PIDs in the container. Set `0` for unlimited. |

## LocalNodeState

Current local status of this node.

Type: string enum: , inactive, pending, active, error, locked

## ManagerStatus

ManagerStatus represents the status of a manager.

It provides the current status of a node's manager component, if the node
is a manager.

| Field | Type | Required | Description |
|---|---|---|---|
| `Leader` | boolean |  |  |
| `Reachability` | `Reachability` |  |  |
| `Addr` | string |  | The IP address and port at which the manager is reachable. |

## Mount

| Field | Type | Required | Description |
|---|---|---|---|
| `Target` | string |  | Container path. |
| `Source` | string |  | Mount source (e.g. a volume name, a host path). The source cannot be specified when using `Type=tmpfs`. For `Type=bind`, the source path must either exist, or the `CreateMountpoint` must be set to `true` to create the source path on the host if missing. For `Type=npipe`, the pipe must exist prior to creating the container. |
| `Type` | allOf(`MountType`) |  | The mount type. Available types: - `bind` Mounts a file or directory from the host into the container. The `Source` must exist prior to creating the container. - `cluster` a Swarm cluster volume - `image` Mounts an image. - `npipe` Mounts a named pipe from the host into the container. The `Source` must exist prior to creating the container. - `tmpfs` Create a tmpfs with the given options. The mount `Source` cannot be specified for tmpfs. - `volume` Creates a volume with the given name and options (or uses a pre-existing volume with the same name and options). These are **not** removed when the container is removed. |
| `ReadOnly` | boolean |  | Whether the mount should be read-only. |
| `Consistency` | string |  | The consistency requirement for the mount: `default`, `consistent`, `cached`, or `delegated`. |
| `BindOptions` | object |  | Optional configuration for the `bind` type. |
| `VolumeOptions` | object |  | Optional configuration for the `volume` type. |
| `ImageOptions` | object |  | Optional configuration for the `image` type. |
| `TmpfsOptions` | object |  | Optional configuration for the `tmpfs` type. |

## MountPoint

MountPoint represents a mount point configuration inside the container.
This is used for reporting the mountpoints in use by a container.

| Field | Type | Required | Description |
|---|---|---|---|
| `Type` | allOf(`MountType`) |  | The mount type: - `bind` a mount of a file or directory from the host into the container. - `cluster` a Swarm cluster volume. - `image` an OCI image. - `npipe` a named pipe from the host into the container. - `tmpfs` a `tmpfs`. - `volume` a docker volume with the given `Name`. |
| `Name` | string |  | Name is the name reference to the underlying data defined by `Source` e.g., the volume name. |
| `Source` | string |  | Source location of the mount. For volumes, this contains the storage location of the volume (within `/var/lib/docker/volumes/`). For bind-mounts, and `npipe`, this contains the source (host) part of the bind-mount. For `tmpfs` mount points, this field is empty. |
| `Destination` | string |  | Destination is the path relative to the container root (`/`) where the `Source` is mounted inside the container. |
| `Driver` | string |  | Driver is the volume driver used to create the volume (if it is a volume). |
| `Mode` | string |  | Mode is a comma separated list of options supplied by the user when creating the bind/volume mount. The default is platform-specific (`"z"` on Linux, empty on Windows). |
| `RW` | boolean |  | Whether the mount is mounted writable (read-write). |
| `Propagation` | string |  | Propagation describes how mounts are propagated from the host into the mount point, and vice-versa. Refer to the [Linux kernel documentation](https://www.kernel.org/doc/Documentation/filesystems/sharedsubtree.txt) for details. This field is not used on Windows. |

## MountType

The mount type. Available types:

- `bind` a mount of a file or directory from the host into the container.
- `cluster` a Swarm cluster volume.
- `image` an OCI image.
- `npipe` a named pipe from the host into the container.
- `tmpfs` a `tmpfs`.
- `volume` a docker volume with the given `Name`.

Type: string enum: bind, cluster, image, npipe, tmpfs, volume

## NRIInfo

Information about the Node Resource Interface (NRI).

This field is only present if NRI is enabled.

| Field | Type | Required | Description |
|---|---|---|---|
| `Info` | array of array of string |  | Information about NRI, provided as "label" / "value" pairs. <p><br /></p> > **Note**: The information returned in this field, including the > formatting of values and labels, should not be considered stable, > and may change without notice. |

## Network

| Field | Type | Required | Description |
|---|---|---|---|
| `Name` | string |  | Name of the network. |
| `Id` | string |  | ID that uniquely identifies a network on a single machine. |
| `Created` | string (dateTime) |  | Date and time at which the network was created in [RFC 3339](https://www.ietf.org/rfc/rfc3339.txt) format with nano-seconds. |
| `Scope` | string |  | The level at which the network exists (e.g. `swarm` for cluster-wide or `local` for machine level) |
| `Driver` | string |  | The name of the driver used to create the network (e.g. `bridge`, `overlay`). |
| `EnableIPv4` | boolean |  | Whether the network was created with IPv4 enabled. |
| `EnableIPv6` | boolean |  | Whether the network was created with IPv6 enabled. |
| `IPAM` | `IPAM` |  | The network's IP Address Management. |
| `Internal` | boolean |  | Whether the network is created to only allow internal networking connectivity. |
| `Attachable` | boolean |  | Whether a global / swarm scope network is manually attachable by regular containers from workers in swarm mode. |
| `Ingress` | boolean |  | Whether the network is providing the routing-mesh for the swarm cluster. |
| `ConfigFrom` | `ConfigReference` |  |  |
| `ConfigOnly` | boolean |  | Whether the network is a config-only network. Config-only networks are placeholder networks for network configurations to be used by other networks. Config-only networks cannot be used directly to run containers or services. |
| `Options` | object |  | Network-specific options uses when creating the network. |
| `Labels` | object |  | Metadata specific to the network being created. |
| `Peers` | array of `PeerInfo` |  | List of peer nodes for an overlay network. This field is only present for overlay networks, and omitted for other network types. |

## NetworkAttachment

Specifies how a task is attached to a network, and the addresses the
task was assigned on that network.

| Field | Type | Required | Description |
|---|---|---|---|
| `Network` | `Network` |  |  |
| `Addresses` | array of string (cidr) |  | The IP addresses (in CIDR notation) assigned to the task on this network. To maintain backward compatibility this field accepts CIDR notation, but only the IP address is used. |

## NetworkAttachmentConfig

Specifies how a service should be attached to a particular network.

| Field | Type | Required | Description |
|---|---|---|---|
| `Target` | string |  | The target network for attachment. Must be a network name or ID. |
| `Aliases` | array of string |  | Discoverable alternate names for the service on this network. |
| `DriverOpts` | object |  | Driver attachment options for the network target. |

## NetworkConnectRequest

NetworkConnectRequest represents the data to be used to connect a container to a network.

| Field | Type | Required | Description |
|---|---|---|---|
| `Container` | string | yes | The ID or name of the container to connect to the network. |
| `EndpointConfig` | `EndpointSettings` |  |  |

## NetworkCreateResponse

OK response to NetworkCreate operation

| Field | Type | Required | Description |
|---|---|---|---|
| `Id` | string | yes | The ID of the created network. |
| `Warning` | string | yes | Warnings encountered when creating the container |

## NetworkDisconnectRequest

NetworkDisconnectRequest represents the data to be used to disconnect a container from a network.

| Field | Type | Required | Description |
|---|---|---|---|
| `Container` | string | yes | The ID or name of the container to disconnect from the network. |
| `Force` | boolean |  | Force the container to disconnect from the network. |

## NetworkInspect

The body of the "get network" http response message.

| Field | Type | Required | Description |
|---|---|---|---|
| `Containers` | object |  | Contains endpoints attached to the network. |
| `Services` | object |  | List of services using the network. This field is only present for swarm scope networks, and omitted for local scope networks. |
| `Status` | `NetworkStatus` |  | provides runtime information about the network such as the number of allocated IPs. |

## NetworkSettings

NetworkSettings exposes the network settings in the API

| Field | Type | Required | Description |
|---|---|---|---|
| `SandboxID` | string |  | SandboxID uniquely represents a container's network stack. |
| `SandboxKey` | string |  | SandboxKey is the full path of the netns handle |
| `Ports` | `PortMap` |  |  |
| `Networks` | object |  | Information about all networks that the container is connected to. |

## NetworkStatus

provides runtime information about the network such as the number of allocated IPs.

| Field | Type | Required | Description |
|---|---|---|---|
| `IPAM` | `IPAMStatus` |  |  |

## NetworkSummary

Network list response item

Type: allOf(`Network`)

## NetworkTaskInfo

carries the information about one backend task

| Field | Type | Required | Description |
|---|---|---|---|
| `Name` | string |  |  |
| `EndpointID` | string |  |  |
| `EndpointIP` | string |  |  |
| `Info` | object |  |  |

## NetworkingConfig

NetworkingConfig represents the container's networking configuration for
each of its interfaces.
It is used for the networking configs specified in the `docker create`
and `docker network connect` commands.

| Field | Type | Required | Description |
|---|---|---|---|
| `EndpointsConfig` | object |  | A mapping of network name to endpoint configuration for that network. The endpoint configuration can be left empty to connect to that network with no particular endpoint configuration. |

## Node

| Field | Type | Required | Description |
|---|---|---|---|
| `ID` | string |  |  |
| `Version` | `ObjectVersion` |  |  |
| `CreatedAt` | string (dateTime) |  | Date and time at which the node was added to the swarm in [RFC 3339](https://www.ietf.org/rfc/rfc3339.txt) format with nano-seconds. |
| `UpdatedAt` | string (dateTime) |  | Date and time at which the node was last updated in [RFC 3339](https://www.ietf.org/rfc/rfc3339.txt) format with nano-seconds. |
| `Spec` | `NodeSpec` |  |  |
| `Description` | `NodeDescription` |  |  |
| `Status` | `NodeStatus` |  |  |
| `ManagerStatus` | `ManagerStatus` |  |  |

## NodeDescription

NodeDescription encapsulates the properties of the Node as reported by the
agent.

| Field | Type | Required | Description |
|---|---|---|---|
| `Hostname` | string |  |  |
| `Platform` | `Platform` |  |  |
| `Resources` | `ResourceObject` |  |  |
| `Engine` | `EngineDescription` |  |  |
| `TLSInfo` | `TLSInfo` |  |  |

## NodeSpec

| Field | Type | Required | Description |
|---|---|---|---|
| `Name` | string |  | Name for the node. |
| `Labels` | object |  | User-defined key/value metadata. |
| `Role` | string enum: worker, manager |  | Role of the node. |
| `Availability` | string enum: active, pause, drain |  | Availability of the node. |

## NodeState

NodeState represents the state of a node.

Type: string enum: unknown, down, ready, disconnected

## NodeStatus

NodeStatus represents the status of a node.

It provides the current status of the node, as seen by the manager.

| Field | Type | Required | Description |
|---|---|---|---|
| `State` | `NodeState` |  |  |
| `Message` | string |  |  |
| `Addr` | string |  | IP address of the node. |

## OCIDescriptor

A descriptor struct containing digest, media type, and size, as defined in
the [OCI Content Descriptors Specification](https://github.com/opencontainers/image-spec/blob/v1.0.1/descriptor.md).

| Field | Type | Required | Description |
|---|---|---|---|
| `mediaType` | string |  | The media type of the object this schema refers to. |
| `digest` | string |  | The digest of the targeted content. |
| `size` | integer (int64) |  | The size in bytes of the blob. |
| `urls` | array of string (uri) |  | List of URLs from which this object MAY be downloaded. |
| `annotations` | object |  | Arbitrary metadata relating to the targeted content. |
| `data` | string |  | Data is an embedding of the targeted content. This is encoded as a base64 string when marshalled to JSON (automatically, by encoding/json). If present, Data can be used directly to avoid fetching the targeted content. |
| `platform` | `OCIPlatform` |  |  |
| `artifactType` | string |  | ArtifactType is the IANA media type of this artifact. |

## OCIPlatform

Describes the platform which the image in the manifest runs on, as defined
in the [OCI Image Index Specification](https://github.com/opencontainers/image-spec/blob/v1.0.1/image-index.md).

| Field | Type | Required | Description |
|---|---|---|---|
| `architecture` | string |  | The CPU architecture, for example `amd64` or `ppc64`. |
| `os` | string |  | The operating system, for example `linux` or `windows`. |
| `os.version` | string |  | Optional field specifying the operating system version, for example on Windows `10.0.19041.1165`. |
| `os.features` | array of string |  | Optional field specifying an array of strings, each listing a required OS feature (for example on Windows `win32k`). |
| `variant` | string |  | Optional field specifying a variant of the CPU, for example `v7` to specify ARMv7 when architecture is `arm`. |

## ObjectVersion

The version number of the object such as node, service, etc. This is needed
to avoid conflicting writes. The client must send the version number along
with the modified specification when updating these objects.

This approach ensures safe concurrency and determinism in that the change
on the object may not be applied if the version number has changed from the
last read. In other words, if two update requests specify the same base
version, only one of the requests can succeed. As a result, two separate
update requests that happen at the same time will not unintentionally
overwrite each other.

| Field | Type | Required | Description |
|---|---|---|---|
| `Index` | integer (uint64) |  |  |

## PeerInfo

represents one peer of an overlay network.

| Field | Type | Required | Description |
|---|---|---|---|
| `Name` | string |  | ID of the peer-node in the Swarm cluster. |
| `IP` | string |  | IP-address of the peer-node in the Swarm cluster. |

## PeerNode

Represents a peer-node in the swarm

| Field | Type | Required | Description |
|---|---|---|---|
| `NodeID` | string |  | Unique identifier of for this node in the swarm. |
| `Addr` | string |  | IP address and ports at which this node can be reached. |

## Platform

Platform represents the platform (Arch/OS).

| Field | Type | Required | Description |
|---|---|---|---|
| `Architecture` | string |  | Architecture represents the hardware architecture (for example, `x86_64`). |
| `OS` | string |  | OS represents the Operating System (for example, `linux` or `windows`). |

## Plugin

A plugin for the Engine API

| Field | Type | Required | Description |
|---|---|---|---|
| `Id` | string |  |  |
| `Name` | string | yes |  |
| `Enabled` | boolean | yes | True if the plugin is running. False if the plugin is not running, only installed. |
| `Settings` | object | yes | user-configurable settings for the plugin. |
| `PluginReference` | string |  | plugin remote reference used to push/pull the plugin |
| `Config` | object | yes | The config of a plugin. |

## PluginDevice

| Field | Type | Required | Description |
|---|---|---|---|
| `Name` | string | yes |  |
| `Description` | string | yes |  |
| `Settable` | array of string | yes |  |
| `Path` | string | yes |  |

## PluginEnv

| Field | Type | Required | Description |
|---|---|---|---|
| `Name` | string | yes |  |
| `Description` | string | yes |  |
| `Settable` | array of string | yes |  |
| `Value` | string | yes |  |

## PluginMount

| Field | Type | Required | Description |
|---|---|---|---|
| `Name` | string | yes |  |
| `Description` | string | yes |  |
| `Settable` | array of string | yes |  |
| `Source` | string | yes |  |
| `Destination` | string | yes |  |
| `Type` | string | yes |  |
| `Options` | array of string | yes |  |

## PluginPrivilege

Describes a permission the user has to accept upon installing
the plugin.

| Field | Type | Required | Description |
|---|---|---|---|
| `Name` | string |  |  |
| `Description` | string |  |  |
| `Value` | array of string |  |  |

## PluginsInfo

Available plugins per type.

<p><br /></p>

> **Note**: Only unmanaged (V1) plugins are included in this list.
> V1 plugins are "lazily" loaded, and are not returned in this list
> if there is no resource using the plugin.

| Field | Type | Required | Description |
|---|---|---|---|
| `Volume` | array of string |  | Names of available volume-drivers, and network-driver plugins. |
| `Network` | array of string |  | Names of available network-drivers, and network-driver plugins. |
| `Authorization` | array of string |  | Names of available authorization plugins. |
| `Log` | array of string |  | Names of available logging-drivers, and logging-driver plugins. |

## PortBinding

PortBinding represents a binding between a host IP address and a host
port.

| Field | Type | Required | Description |
|---|---|---|---|
| `HostIp` | string |  | Host IP address that the container's port is mapped to. |
| `HostPort` | string |  | Host port number that the container's port is mapped to. |

## PortMap

PortMap describes the mapping of container ports to host ports, using the
container's port-number and protocol as key in the format `<port>/<protocol>`,
for example, `80/udp`.

If a container's port is mapped for multiple protocols, separate entries
are added to the mapping table.

Type: object

## PortStatus

represents the port status of a task's host ports whose service has published host ports

| Field | Type | Required | Description |
|---|---|---|---|
| `Ports` | array of `EndpointPortConfig` |  |  |

## PortSummary

Describes a port-mapping between the container and the host.

| Field | Type | Required | Description |
|---|---|---|---|
| `IP` | string (ip-address) |  | Host IP address that the container's port is mapped to |
| `PrivatePort` | integer (uint16) | yes | Port on the container |
| `PublicPort` | integer (uint16) |  | Port exposed on the host |
| `Type` | string enum: tcp, udp, sctp | yes |  |

## ProcessConfig

| Field | Type | Required | Description |
|---|---|---|---|
| `privileged` | boolean |  |  |
| `user` | string |  |  |
| `tty` | boolean |  |  |
| `entrypoint` | string |  |  |
| `arguments` | array of string |  |  |

## ProgressDetail

| Field | Type | Required | Description |
|---|---|---|---|
| `current` | integer |  |  |
| `total` | integer |  |  |

## PullIdentity

PullIdentity contains remote location information if image was created via pull.
If image was pulled via mirror, this contains the original repository location.

| Field | Type | Required | Description |
|---|---|---|---|
| `Repository` | string |  | Repository is the remote repository location the image was pulled from. |

## PushImageInfo

| Field | Type | Required | Description |
|---|---|---|---|
| `errorDetail` | `ErrorDetail` |  |  |
| `status` | string |  |  |
| `progressDetail` | `ProgressDetail` |  |  |

## Reachability

Reachability represents the reachability of a node.

Type: string enum: unknown, unreachable, reachable

## RegistryServiceConfig

RegistryServiceConfig stores daemon registry services configuration.

| Field | Type | Required | Description |
|---|---|---|---|
| `InsecureRegistryCIDRs` | array of string |  | List of IP ranges of insecure registries, using the CIDR syntax ([RFC 4632](https://tools.ietf.org/html/4632)). Insecure registries accept un-encrypted (HTTP) and/or untrusted (HTTPS with certificates from unknown CAs) communication. By default, local registries (`::1/128` and `127.0.0.0/8`) are configured as insecure. All other registries are secure. Communicating with an insecure registry is not possible if the daemon assumes that registry is secure. This configuration override this behavior, insecure communication with registries whose resolved IP address is within the subnet described by the CIDR syntax. Registries can also be marked insecure by hostname. Those registries are listed under `IndexConfigs` and have their `Secure` field set to `false`. > **Warning**: Using this option can be useful when running a local > registry, but introduces security vulnerabilities. This option > should therefore ONLY be used for testing purposes. For increased > security, users should add their CA to their system's list of trusted > CAs instead of enabling this option. |
| `IndexConfigs` | object |  |  |
| `Mirrors` | array of string |  | List of registry URLs that act as a mirror for the official (`docker.io`) registry. |

## ResourceObject

An object describing the resources which can be advertised by a node and
requested by a task.

| Field | Type | Required | Description |
|---|---|---|---|
| `NanoCPUs` | integer (int64) |  |  |
| `MemoryBytes` | integer (int64) |  |  |
| `GenericResources` | `GenericResources` |  |  |

## Resources

A container's resources (cgroups config, ulimits, etc)

| Field | Type | Required | Description |
|---|---|---|---|
| `CpuShares` | integer |  | An integer value representing this container's relative CPU weight versus other containers. |
| `Memory` | integer (int64) |  | Memory limit in bytes. |
| `CgroupParent` | string |  | Path to `cgroups` under which the container's `cgroup` is created. If the path is not absolute, the path is considered to be relative to the `cgroups` path of the init process. Cgroups are created if they do not already exist. |
| `BlkioWeight` | integer |  | Block IO weight (relative weight). |
| `BlkioWeightDevice` | array of object |  | Block IO weight (relative device weight) in the form: ``` [{"Path": "device_path", "Weight": weight}] ``` |
| `BlkioDeviceReadBps` | array of `ThrottleDevice` |  | Limit read rate (bytes per second) from a device, in the form: ``` [{"Path": "device_path", "Rate": rate}] ``` |
| `BlkioDeviceWriteBps` | array of `ThrottleDevice` |  | Limit write rate (bytes per second) to a device, in the form: ``` [{"Path": "device_path", "Rate": rate}] ``` |
| `BlkioDeviceReadIOps` | array of `ThrottleDevice` |  | Limit read rate (IO per second) from a device, in the form: ``` [{"Path": "device_path", "Rate": rate}] ``` |
| `BlkioDeviceWriteIOps` | array of `ThrottleDevice` |  | Limit write rate (IO per second) to a device, in the form: ``` [{"Path": "device_path", "Rate": rate}] ``` |
| `CpuPeriod` | integer (int64) |  | The length of a CPU period in microseconds. |
| `CpuQuota` | integer (int64) |  | Microseconds of CPU time that the container can get in a CPU period. |
| `CpuRealtimePeriod` | integer (int64) |  | The length of a CPU real-time period in microseconds. Set to 0 to allocate no time allocated to real-time tasks. |
| `CpuRealtimeRuntime` | integer (int64) |  | The length of a CPU real-time runtime in microseconds. Set to 0 to allocate no time allocated to real-time tasks. |
| `CpusetCpus` | string |  | CPUs in which to allow execution (e.g., `0-3`, `0,1`). |
| `CpusetMems` | string |  | Memory nodes (MEMs) in which to allow execution (0-3, 0,1). Only effective on NUMA systems. |
| `Devices` | array of `DeviceMapping` |  | A list of devices to add to the container. |
| `DeviceCgroupRules` | array of string |  | a list of cgroup rules to apply to the container |
| `DeviceRequests` | array of `DeviceRequest` |  | A list of requests for devices to be sent to device drivers. |
| `MemoryReservation` | integer (int64) |  | Memory soft limit in bytes. |
| `MemorySwap` | integer (int64) |  | Total memory limit (memory + swap). Set as `-1` to enable unlimited swap. |
| `MemorySwappiness` | integer (int64) |  | Tune a container's memory swappiness behavior. Accepts an integer between 0 and 100. |
| `NanoCpus` | integer (int64) |  | CPU quota in units of 10<sup>-9</sup> CPUs. |
| `OomKillDisable` | boolean |  | Disable OOM Killer for the container. |
| `Init` | boolean |  | Run an init inside the container that forwards signals and reaps processes. This field is omitted if empty, and the default (as configured on the daemon) is used. |
| `PidsLimit` | integer (int64) |  | Tune a container's PIDs limit. Set `0` or `-1` for unlimited, or `null` to not change. |
| `Ulimits` | array of object |  | A list of resource limits to set in the container. For example: ``` {"Name": "nofile", "Soft": 1024, "Hard": 2048} ``` |
| `CpuCount` | integer (int64) |  | The number of usable CPUs (Windows only). On Windows Server containers, the processor resource controls are mutually exclusive. The order of precedence is `CPUCount` first, then `CPUShares`, and `CPUPercent` last. |
| `CpuPercent` | integer (int64) |  | The usable percentage of the available CPUs (Windows only). On Windows Server containers, the processor resource controls are mutually exclusive. The order of precedence is `CPUCount` first, then `CPUShares`, and `CPUPercent` last. |
| `IOMaximumIOps` | integer (int64) |  | Maximum IOps for the container system drive (Windows only) |
| `IOMaximumBandwidth` | integer (int64) |  | Maximum IO in bytes per second for the container system drive (Windows only). |

## RestartPolicy

The behavior to apply when the container exits. The default is not to
restart.

An ever increasing delay (double the previous delay, starting at 100ms) is
added before each restart to prevent flooding the server.

| Field | Type | Required | Description |
|---|---|---|---|
| `Name` | string enum: , no, always, unless-stopped, on-failure |  | - Empty string means not to restart - `no` Do not automatically restart - `always` Always restart - `unless-stopped` Restart always except when the user has manually stopped the container - `on-failure` Restart only when the container exit code is non-zero |
| `MaximumRetryCount` | integer |  | If `on-failure` is used, the number of times to retry before giving up. |

## RootFSStorage

Information about the storage used for the container's root filesystem.

| Field | Type | Required | Description |
|---|---|---|---|
| `Snapshot` | `RootFSStorageSnapshot` |  | Information about the snapshot used for the container's root filesystem. |

## RootFSStorageSnapshot

Information about a snapshot backend of the container's root filesystem.

| Field | Type | Required | Description |
|---|---|---|---|
| `Name` | string |  | Name of the snapshotter. |

## Runtime

Runtime describes an [OCI compliant](https://github.com/opencontainers/runtime-spec)
runtime.

The runtime is invoked by the daemon via the `containerd` daemon. OCI
runtimes act as an interface to the Linux kernel namespaces, cgroups,
and SELinux.

| Field | Type | Required | Description |
|---|---|---|---|
| `path` | string |  | Name and, optional, path, of the OCI executable binary. If the path is omitted, the daemon searches the host's `$PATH` for the binary and uses the first result. |
| `runtimeArgs` | array of string |  | List of command-line arguments to pass to the runtime when invoked. |
| `status` | object |  | Information specific to the runtime. While this API specification does not define data provided by runtimes, the following well-known properties may be provided by runtimes: `org.opencontainers.runtime-spec.features`: features structure as defined in the [OCI Runtime Specification](https://github.com/opencontainers/runtime-spec/blob/main/features.md), in a JSON string representation. <p><br /></p> > **Note**: The information returned in this field, including the > formatting of values and labels, should not be considered stable, > and may change without notice. |

## Secret

| Field | Type | Required | Description |
|---|---|---|---|
| `ID` | string |  |  |
| `Version` | `ObjectVersion` |  |  |
| `CreatedAt` | string (dateTime) |  |  |
| `UpdatedAt` | string (dateTime) |  |  |
| `Spec` | `SecretSpec` |  |  |

## SecretSpec

| Field | Type | Required | Description |
|---|---|---|---|
| `Name` | string |  | User-defined name of the secret. |
| `Labels` | object |  | User-defined key/value metadata. |
| `Data` | string |  | Data is the data to store as a secret, formatted as a standard base64-encoded ([RFC 4648](https://tools.ietf.org/html/rfc4648#section-4)) string. It must be empty if the Driver field is set, in which case the data is loaded from an external secret store. The maximum allowed size is 500KB, as defined in [MaxSecretSize](https://pkg.go.dev/github.com/moby/swarmkit/v2@v2.0.0/api/validation#MaxSecretSize). This field is only used to _create_ a secret, and is not returned by other endpoints. |
| `Driver` | `Driver` |  | Name of the secrets driver used to fetch the secret's value from an external secret store. |
| `Templating` | `Driver` |  | Templating driver, if applicable Templating controls whether and how to evaluate the config payload as a template. If no driver is set, no templating is used. |

## Service

| Field | Type | Required | Description |
|---|---|---|---|
| `ID` | string |  |  |
| `Version` | `ObjectVersion` |  |  |
| `CreatedAt` | string (dateTime) |  |  |
| `UpdatedAt` | string (dateTime) |  |  |
| `Spec` | `ServiceSpec` |  |  |
| `Endpoint` | object |  |  |
| `UpdateStatus` | object |  | The status of a service update. |
| `ServiceStatus` | object |  | The status of the service's tasks. Provided only when requested as part of a ServiceList operation. |
| `JobStatus` | object |  | The status of the service when it is in one of ReplicatedJob or GlobalJob modes. Absent on Replicated and Global mode services. The JobIteration is an ObjectVersion, but unlike the Service's version, does not need to be sent with an update request. |

## ServiceCreateResponse

contains the information returned to a client on the
creation of a new service.

| Field | Type | Required | Description |
|---|---|---|---|
| `ID` | string |  | The ID of the created service. |
| `Warnings` | array of string |  | Optional warning message. FIXME(thaJeztah): this should have "omitempty" in the generated type. |

## ServiceInfo

represents service parameters with the list of service's tasks

| Field | Type | Required | Description |
|---|---|---|---|
| `VIP` | string |  |  |
| `Ports` | array of string |  |  |
| `LocalLBIndex` | integer (int) |  |  |
| `Tasks` | array of `NetworkTaskInfo` |  |  |

## ServiceSpec

User modifiable configuration for a service.

| Field | Type | Required | Description |
|---|---|---|---|
| `Name` | string |  | Name of the service. |
| `Labels` | object |  | User-defined key/value metadata. |
| `TaskTemplate` | `TaskSpec` |  |  |
| `Mode` | object |  | Scheduling mode for the service. |
| `UpdateConfig` | object |  | Specification for the update strategy of the service. |
| `RollbackConfig` | object |  | Specification for the rollback strategy of the service. |
| `Networks` | array of `NetworkAttachmentConfig` |  | Specifies which networks the service should attach to. Deprecated: This field is deprecated since v1.44. The Networks field in TaskSpec should be used instead. |
| `EndpointSpec` | `EndpointSpec` |  |  |

## ServiceUpdateResponse

| Field | Type | Required | Description |
|---|---|---|---|
| `Warnings` | array of string |  | Optional warning messages |

## SignatureIdentity

SignatureIdentity contains the properties of verified signatures for the image.

| Field | Type | Required | Description |
|---|---|---|---|
| `Name` | string |  | Name is a textual description summarizing the type of signature. |
| `Timestamps` | array of `SignatureTimestamp` |  | Timestamps contains a list of verified signed timestamps for the signature. |
| `KnownSigner` | `KnownSignerIdentity` |  | KnownSigner is an identifier for a special signer identity that is known to the implementation. |
| `DockerReference` | string |  | DockerReference is the Docker image reference associated with the signature. This is an optional field only present in older hashedrecord signatures. |
| `Signer` | `SignerIdentity` |  | Signer contains information about the signer certificate used to sign the image. |
| `SignatureType` | `SignatureType` |  | SignatureType is the type of signature format. E.g. "bundle-v0.3" or "hashedrecord". |
| `Error` | string |  | Error contains error information if signature verification failed. Other fields will be empty in this case. |
| `Warnings` | array of string |  | Warnings contains any warnings that occurred during signature verification. For example, if there was no internet connectivity and cached trust roots were used. Warning does not indicate a failed verification but may point to configuration issues. |

## SignatureTimestamp

SignatureTimestamp contains information about a verified signed timestamp for an image signature.

| Field | Type | Required | Description |
|---|---|---|---|
| `Type` | `SignatureTimestampType` |  |  |
| `URI` | string |  |  |
| `Timestamp` | string (date-time) |  |  |

## SignatureTimestampType

SignatureTimestampType is the type of timestamp used in the signature.

Type: string enum: Tlog, TimestampAuthority

## SignatureType

SignatureType is the type of signature format.

Type: string enum: bundle-v0.3, simplesigning-v1

## SignerIdentity

SignerIdentity contains information about the signer certificate used to sign the image.

| Field | Type | Required | Description |
|---|---|---|---|
| `CertificateIssuer` | string |  | CertificateIssuer is the certificate issuer. |
| `SubjectAlternativeName` | string |  | SubjectAlternativeName is the certificate subject alternative name. |
| `Issuer` | string |  | The OIDC issuer. Should match `iss` claim of ID token or, in the case of a federated login like Dex it should match the issuer URL of the upstream issuer. The issuer is not set the extensions are invalid and will fail to render. |
| `BuildSignerURI` | string |  | Reference to specific build instructions that are responsible for signing. |
| `BuildSignerDigest` | string |  | Immutable reference to the specific version of the build instructions that is responsible for signing. |
| `RunnerEnvironment` | string |  | Specifies whether the build took place in platform-hosted cloud infrastructure or customer/self-hosted infrastructure. |
| `SourceRepositoryURI` | string |  | Source repository URL that the build was based on. |
| `SourceRepositoryDigest` | string |  | Immutable reference to a specific version of the source code that the build was based upon. |
| `SourceRepositoryRef` | string |  | Source Repository Ref that the build run was based upon. |
| `SourceRepositoryIdentifier` | string |  | Immutable identifier for the source repository the workflow was based upon. |
| `SourceRepositoryOwnerURI` | string |  | Source repository owner URL of the owner of the source repository that the build was based on. |
| `SourceRepositoryOwnerIdentifier` | string |  | Immutable identifier for the owner of the source repository that the workflow was based upon. |
| `BuildConfigURI` | string |  | Build Config URL to the top-level/initiating build instructions. |
| `BuildConfigDigest` | string |  | Immutable reference to the specific version of the top-level/initiating build instructions. |
| `BuildTrigger` | string |  | Event or action that initiated the build. |
| `RunInvocationURI` | string |  | Run Invocation URL to uniquely identify the build execution. |
| `SourceRepositoryVisibilityAtSigning` | string |  | Source repository visibility at the time of signing the certificate. |

## Storage

Information about the storage used by the container.

| Field | Type | Required | Description |
|---|---|---|---|
| `RootFS` | `RootFSStorage` |  | Information about the storage used for the container's root filesystem. |

## SubnetStatus

| Field | Type | Required | Description |
|---|---|---|---|
| `IPsInUse` | integer (uint64) |  | Number of IP addresses in the subnet that are in use or reserved and are therefore unavailable for allocation, saturating at 2<sup>64</sup> - 1. |
| `DynamicIPsAvailable` | integer (uint64) |  | Number of IP addresses within the network's IPRange for the subnet that are available for allocation, saturating at 2<sup>64</sup> - 1. |

## Swarm

Type: allOf(`ClusterInfo`, object)

## SwarmInfo

Represents generic information about swarm.

| Field | Type | Required | Description |
|---|---|---|---|
| `NodeID` | string |  | Unique identifier of for this node in the swarm. |
| `NodeAddr` | string |  | IP address at which this node can be reached by other nodes in the swarm. |
| `LocalNodeState` | `LocalNodeState` |  |  |
| `ControlAvailable` | boolean |  |  |
| `Error` | string |  |  |
| `RemoteManagers` | array of `PeerNode` |  | List of ID's and addresses of other managers in the swarm. |
| `Nodes` | integer |  | Total number of nodes in the swarm. |
| `Managers` | integer |  | Total number of managers in the swarm. |
| `Cluster` | `ClusterInfo` |  |  |

## SwarmSpec

User modifiable swarm configuration.

| Field | Type | Required | Description |
|---|---|---|---|
| `Name` | string |  | Name of the swarm. |
| `Labels` | object |  | User-defined key/value metadata. |
| `Orchestration` | object |  | Orchestration configuration. |
| `Raft` | object |  | Raft configuration. |
| `Dispatcher` | object |  | Dispatcher configuration. |
| `CAConfig` | object |  | CA configuration. |
| `EncryptionConfig` | object |  | Parameters related to encryption-at-rest. |
| `TaskDefaults` | object |  | Defaults for creating tasks in this cluster. |

## SystemInfo

| Field | Type | Required | Description |
|---|---|---|---|
| `ID` | string |  | Unique identifier of the daemon. <p><br /></p> > **Note**: The format of the ID itself is not part of the API, and > should not be considered stable. |
| `Containers` | integer |  | Total number of containers on the host. |
| `ContainersRunning` | integer |  | Number of containers with status `"running"`. |
| `ContainersPaused` | integer |  | Number of containers with status `"paused"`. |
| `ContainersStopped` | integer |  | Number of containers with status `"stopped"`. |
| `Images` | integer |  | Total number of images on the host. Both _tagged_ and _untagged_ (dangling) images are counted. |
| `Driver` | string |  | Name of the storage driver in use. |
| `DriverStatus` | array of array of string |  | Information specific to the storage driver, provided as "label" / "value" pairs. This information is provided by the storage driver, and formatted in a way consistent with the output of `docker info` on the command line. <p><br /></p> > **Note**: The information returned in this field, including the > formatting of values and labels, should not be considered stable, > and may change without notice. |
| `DockerRootDir` | string |  | Root directory of persistent Docker state. Defaults to `/var/lib/docker` on Linux, and `C:\ProgramData\docker` on Windows. |
| `Plugins` | `PluginsInfo` |  |  |
| `MemoryLimit` | boolean |  | Indicates if the host has memory limit support enabled. |
| `SwapLimit` | boolean |  | Indicates if the host has memory swap limit support enabled. |
| `CpuCfsPeriod` | boolean |  | Indicates if CPU CFS(Completely Fair Scheduler) period is supported by the host. |
| `CpuCfsQuota` | boolean |  | Indicates if CPU CFS(Completely Fair Scheduler) quota is supported by the host. |
| `CPUShares` | boolean |  | Indicates if CPU Shares limiting is supported by the host. |
| `CPUSet` | boolean |  | Indicates if CPUsets (cpuset.cpus, cpuset.mems) are supported by the host. See [cpuset(7)](https://www.kernel.org/doc/Documentation/cgroup-v1/cpusets.txt) |
| `PidsLimit` | boolean |  | Indicates if the host kernel has PID limit support enabled. |
| `OomKillDisable` | boolean |  | Indicates if OOM killer disable is supported on the host. |
| `IPv4Forwarding` | boolean |  | Indicates IPv4 forwarding is enabled. |
| `Debug` | boolean |  | Indicates if the daemon is running in debug-mode / with debug-level logging enabled. |
| `NFd` | integer |  | The total number of file Descriptors in use by the daemon process. This information is only returned if debug-mode is enabled. |
| `NGoroutines` | integer |  | The number of goroutines that currently exist. This information is only returned if debug-mode is enabled. |
| `SystemTime` | string |  | Current system-time in [RFC 3339](https://www.ietf.org/rfc/rfc3339.txt) format with nano-seconds. |
| `LoggingDriver` | string |  | The logging driver to use as a default for new containers. |
| `CgroupDriver` | string enum: cgroupfs, systemd, none |  | The driver to use for managing cgroups. |
| `CgroupVersion` | string enum: 1, 2 |  | The version of the cgroup. |
| `NEventsListener` | integer |  | Number of event listeners subscribed. |
| `KernelVersion` | string |  | Kernel version of the host. On Linux, this information obtained from `uname`. On Windows this information is queried from the <kbd>HKEY_LOCAL_MACHINE\\SOFTWARE\\Microsoft\\Windows NT\\CurrentVersion\\</kbd> registry value, for example _"10.0 14393 (14393.1198.amd64fre.rs1_release_sec.170427-1353)"_. |
| `OperatingSystem` | string |  | Name of the host's operating system, for example: "Ubuntu 24.04 LTS" or "Windows Server 2016 Datacenter" |
| `OSVersion` | string |  | Version of the host's operating system <p><br /></p> > **Note**: The information returned in this field, including its > very existence, and the formatting of values, should not be considered > stable, and may change without notice. |
| `OSType` | string |  | Generic type of the operating system of the host, as returned by the Go runtime (`GOOS`). Currently returned values are "linux" and "windows". A full list of possible values can be found in the [Go documentation](https://go.dev/doc/install/source#environment). |
| `Architecture` | string |  | Hardware architecture of the host, as returned by the operating system. This is equivalent to the output of `uname -m` on Linux. Unlike `Arch` (from `/version`), this reports the machine's native architecture, which can differ from the Go runtime architecture when running a binary compiled for a different architecture (for example, a 32-bit binary running on 64-bit hardware). |
| `NCPU` | integer |  | The number of logical CPUs usable by the daemon. The number of available CPUs is checked by querying the operating system when the daemon starts. Changes to operating system CPU allocation after the daemon is started are not reflected. |
| `MemTotal` | integer (int64) |  | Total amount of physical memory available on the host, in bytes. |
| `IndexServerAddress` | string |  | Address / URL of the index server that is used for image search, and as a default for user authentication for Docker Hub and Docker Cloud. |
| `RegistryConfig` | `RegistryServiceConfig` |  |  |
| `GenericResources` | `GenericResources` |  |  |
| `HttpProxy` | string |  | HTTP-proxy configured for the daemon. This value is obtained from the [`HTTP_PROXY`](https://www.gnu.org/software/wget/manual/html_node/Proxies.html) environment variable. Credentials ([user info component](https://tools.ietf.org/html/rfc3986#section-3.2.1)) in the proxy URL are masked in the API response. Containers do not automatically inherit this configuration. |
| `HttpsProxy` | string |  | HTTPS-proxy configured for the daemon. This value is obtained from the [`HTTPS_PROXY`](https://www.gnu.org/software/wget/manual/html_node/Proxies.html) environment variable. Credentials ([user info component](https://tools.ietf.org/html/rfc3986#section-3.2.1)) in the proxy URL are masked in the API response. Containers do not automatically inherit this configuration. |
| `NoProxy` | string |  | Comma-separated list of domain extensions for which no proxy should be used. This value is obtained from the [`NO_PROXY`](https://www.gnu.org/software/wget/manual/html_node/Proxies.html) environment variable. Containers do not automatically inherit this configuration. |
| `Name` | string |  | Hostname of the host. |
| `Labels` | array of string |  | User-defined labels (key/value metadata) as set on the daemon. <p><br /></p> > **Note**: When part of a Swarm, nodes can both have _daemon_ labels, > set through the daemon configuration, and _node_ labels, set from a > manager node in the Swarm. Node labels are not included in this > field. Node labels can be retrieved using the `/nodes/(id)` endpoint > on a manager node in the Swarm. |
| `ExperimentalBuild` | boolean |  | Indicates if experimental features are enabled on the daemon. |
| `ServerVersion` | string |  | Version string of the daemon. |
| `Runtimes` | object |  | List of [OCI compliant](https://github.com/opencontainers/runtime-spec) runtimes configured on the daemon. Keys hold the "name" used to reference the runtime. The Docker daemon relies on an OCI compliant runtime (invoked via the `containerd` daemon) as its interface to the Linux kernel namespaces, cgroups, and SELinux. The default runtime is `runc`, and automatically configured. Additional runtimes can be configured by the user and will be listed here. |
| `DefaultRuntime` | string |  | Name of the default OCI runtime that is used when starting containers. The default can be overridden per-container at create time. |
| `Swarm` | `SwarmInfo` |  |  |
| `LiveRestoreEnabled` | boolean |  | Indicates if live restore is enabled. If enabled, containers are kept running when the daemon is shutdown or upon daemon start if running containers are detected. |
| `Isolation` | string enum: default, hyperv, process, |  | Represents the isolation technology to use as a default for containers. The supported values are platform-specific. If no isolation value is specified on daemon start, on Windows client, the default is `hyperv`, and on Windows server, the default is `process`. This option is currently not used on other platforms. |
| `InitBinary` | string |  | Name and, optional, path of the `docker-init` binary. If the path is omitted, the daemon searches the host's `$PATH` for the binary and uses the first result. |
| `ContainerdCommit` | `Commit` |  |  |
| `RuncCommit` | `Commit` |  |  |
| `InitCommit` | `Commit` |  |  |
| `SecurityOptions` | array of string |  | List of security features that are enabled on the daemon, such as apparmor, seccomp, SELinux, user-namespaces (userns), rootless and no-new-privileges. Additional configuration options for each security feature may be present, and are included as a comma-separated list of key/value pairs. |
| `ProductLicense` | string |  | Reports a summary of the product license on the daemon. If a commercial license has been applied to the daemon, information such as number of nodes, and expiration are included. |
| `DefaultAddressPools` | array of object |  | List of custom default address pools for local networks, which can be specified in the daemon.json file or dockerd option. Example: a Base "10.10.0.0/16" with Size 24 will define the set of 256 10.10.[0-255].0/24 address pools. |
| `FirewallBackend` | `FirewallInfo` |  |  |
| `DiscoveredDevices` | array of `DeviceInfo` |  | List of devices discovered by device drivers. Each device includes information about its source driver, kind, name, and additional driver-specific attributes. |
| `NRI` | `NRIInfo` |  |  |
| `Warnings` | array of string |  | List of warnings / informational messages about missing features, or issues related to the daemon configuration. These messages can be printed by the client as information to the user. |
| `CDISpecDirs` | array of string |  | List of directories where (Container Device Interface) CDI specifications are located. These specifications define vendor-specific modifications to an OCI runtime specification for a container being created. An empty list indicates that CDI device injection is disabled. Note that since using CDI device injection requires the daemon to have experimental enabled. For non-experimental daemons an empty list will always be returned. |
| `Containerd` | `ContainerdInfo` |  |  |

## SystemVersion

Response of Engine API: GET "/version"

| Field | Type | Required | Description |
|---|---|---|---|
| `Platform` | object |  |  |
| `Components` | array of object |  | Information about system components |
| `Version` | string |  | The version of the daemon |
| `ApiVersion` | string |  | The default (and highest) API version that is supported by the daemon |
| `MinAPIVersion` | string |  | The minimum API version that is supported by the daemon |
| `GitCommit` | string |  | The Git commit of the source code that was used to build the daemon |
| `GoVersion` | string |  | The version Go used to compile the daemon, and the version of the Go runtime in use. |
| `Os` | string |  | The operating system that the daemon is running on ("linux" or "windows") |
| `Arch` | string |  | Architecture of the daemon, as returned by the Go runtime (`GOARCH`). A full list of possible values can be found in the [Go documentation](https://go.dev/doc/install/source#environment). |
| `KernelVersion` | string |  | The kernel version (`uname -r`) that the daemon is running on. This field is omitted when empty. |
| `Experimental` | boolean |  | Indicates if the daemon is started with experimental features enabled. This field is omitted when empty / false. |
| `BuildTime` | string |  | The date and time that the daemon was compiled. |

## TLSInfo

Information about the issuer of leaf TLS certificates and the trusted root
CA certificate.

| Field | Type | Required | Description |
|---|---|---|---|
| `TrustRoot` | string |  | The root CA certificate(s) that are used to validate leaf TLS certificates. |
| `CertIssuerSubject` | string |  | The base64-url-safe-encoded raw subject bytes of the issuer. |
| `CertIssuerPublicKey` | string |  | The base64-url-safe-encoded raw public key bytes of the issuer. |

## Task

| Field | Type | Required | Description |
|---|---|---|---|
| `ID` | string |  | The ID of the task. |
| `Version` | `ObjectVersion` |  |  |
| `CreatedAt` | string (dateTime) |  |  |
| `UpdatedAt` | string (dateTime) |  |  |
| `Name` | string |  | Name of the task. |
| `Labels` | object |  | User-defined key/value metadata. |
| `Spec` | `TaskSpec` |  |  |
| `ServiceID` | string |  | The ID of the service this task is part of. |
| `Slot` | integer |  |  |
| `NodeID` | string |  | The ID of the node that this task is on. |
| `AssignedGenericResources` | `GenericResources` |  |  |
| `Status` | `TaskStatus` |  |  |
| `DesiredState` | `TaskState` |  |  |
| `JobIteration` | `ObjectVersion` |  | If the Service this Task belongs to is a job-mode service, contains the JobIteration of the Service this Task was created for. Absent if the Task was created for a Replicated or Global Service. |
| `NetworksAttachments` | array of `NetworkAttachment` |  | The networks that this task is attached to, and the addresses the task was assigned on each of them. |

## TaskSpec

User modifiable task configuration.

| Field | Type | Required | Description |
|---|---|---|---|
| `PluginSpec` | object |  | Plugin spec for the service. *(Experimental release only.)* <p><br /></p> > **Note**: ContainerSpec, NetworkAttachmentSpec, and PluginSpec are > mutually exclusive. PluginSpec is only used when the Runtime field > is set to `plugin`. NetworkAttachmentSpec is used when the Runtime > field is set to `attachment`. |
| `ContainerSpec` | object |  | Container spec for the service. <p><br /></p> > **Note**: ContainerSpec, NetworkAttachmentSpec, and PluginSpec are > mutually exclusive. PluginSpec is only used when the Runtime field > is set to `plugin`. NetworkAttachmentSpec is used when the Runtime > field is set to `attachment`. |
| `NetworkAttachmentSpec` | object |  | Read-only spec type for non-swarm containers attached to swarm overlay networks. <p><br /></p> > **Note**: ContainerSpec, NetworkAttachmentSpec, and PluginSpec are > mutually exclusive. PluginSpec is only used when the Runtime field > is set to `plugin`. NetworkAttachmentSpec is used when the Runtime > field is set to `attachment`. |
| `Resources` | object |  | Resource requirements which apply to each individual container created as part of the service. |
| `RestartPolicy` | object |  | Specification for the restart policy which applies to containers created as part of this service. |
| `Placement` | object |  |  |
| `ForceUpdate` | integer (uint64) |  | A counter that triggers an update even if no relevant parameters have been changed. |
| `Runtime` | string |  | Runtime is the type of runtime specified for the task executor. |
| `Networks` | array of `NetworkAttachmentConfig` |  | Specifies which networks the service should attach to. |
| `LogDriver` | object |  | Specifies the log driver to use for tasks created from this spec. If not present, the default one for the swarm will be used, finally falling back to the engine default if not specified. |

## TaskState

Type: string enum: new, allocated, pending, assigned, accepted, preparing, ready, starting, running, complete, shutdown, failed

## TaskStatus

represents the status of a task.

| Field | Type | Required | Description |
|---|---|---|---|
| `Timestamp` | string (dateTime) |  |  |
| `State` | `TaskState` |  |  |
| `Message` | string |  |  |
| `Err` | string |  |  |
| `ContainerStatus` | `ContainerStatus` |  |  |
| `PortStatus` | `PortStatus` |  |  |

## ThrottleDevice

| Field | Type | Required | Description |
|---|---|---|---|
| `Path` | string |  | Device path |
| `Rate` | integer (int64) |  | Rate |

## Topology

A map of topological domains to topological segments. For in depth
details, see documentation for the Topology object in the CSI
specification.

| Field | Type | Required | Description |
|---|---|---|---|
| `Segments` | object |  |  |

## Volume

| Field | Type | Required | Description |
|---|---|---|---|
| `Name` | string | yes | Name of the volume. |
| `Driver` | string | yes | Name of the volume driver used by the volume. |
| `Mountpoint` | string | yes | Mount path of the volume on the host. |
| `CreatedAt` | string (dateTime) |  | Date/Time the volume was created. |
| `Status` | object |  | Low-level details about the volume, provided by the volume driver. Details are returned as a map with key/value pairs: `{"key":"value","key2":"value2"}`. The `Status` field is optional, and is omitted if the volume driver does not support this feature. |
| `Labels` | object | yes | User-defined key/value metadata. |
| `Scope` | string enum: local, global | yes | The level at which the volume exists. Either `global` for cluster-wide, or `local` for machine level. |
| `ClusterVolume` | `ClusterVolume` |  |  |
| `Options` | object | yes | The driver specific options used when creating the volume. |
| `UsageData` | object |  | Usage details about the volume. This information is used by the `GET /system/df` endpoint, and omitted in other endpoints. |

## VolumeCreateRequest

Volume configuration

| Field | Type | Required | Description |
|---|---|---|---|
| `Name` | string |  | The new volume's name. If not specified, Docker generates a name. |
| `Driver` | string |  | Name of the volume driver to use. |
| `DriverOpts` | object |  | A mapping of driver options and values. These options are passed directly to the driver and are driver specific. |
| `Labels` | object |  | User-defined key/value metadata. |
| `ClusterVolumeSpec` | `ClusterVolumeSpec` |  |  |

## VolumeListResponse

Volume list response

| Field | Type | Required | Description |
|---|---|---|---|
| `Volumes` | array of `Volume` |  | List of volumes |
| `Warnings` | array of string |  | Warnings that occurred when fetching the list of volumes. |

## VolumesDiskUsage

represents system data usage for volume resources.

| Field | Type | Required | Description |
|---|---|---|---|
| `ActiveCount` | integer (int64) |  | Count of active volumes. |
| `TotalCount` | integer (int64) |  | Count of all volumes. |
| `Reclaimable` | integer (int64) |  | Disk space that can be reclaimed by removing inactive volumes. |
| `TotalSize` | integer (int64) |  | Disk space in use by volumes. |
| `Items` | array of object |  | List of volumes. |

