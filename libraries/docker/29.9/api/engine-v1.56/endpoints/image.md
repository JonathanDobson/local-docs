# Docker Engine API 1.56 — Image

## GET /v1.56/images/json

operationId: `ImageList`

List Images

Returns a list of images on the server. Note that it uses a different, smaller representation of an image than inspecting a single image.

| Parameter | In | Type | Required | Description |
|---|---|---|---|---|
| `all` | query | boolean |  | Show all images. Only images from a final layer (no children) are shown by default. |
| `filters` | query | string |  | A JSON encoded value of the filters (a `map[string][]string`) to process on the images list. Available filters: - `before`=(`<image-name>[:<tag>]`, `<image id>` or `<image@digest>`) - `dangling=true` - `label=key` or `label="key=value"` of an image label - `reference`=(`<image-name>[:<tag>]`) - `since`=(`<image-name>[:<tag>]`, `<image id>` or `<image@digest>`) - `until=<timestamp>` |
| `shared-size` | query | boolean |  | Compute and show shared size as a `SharedSize` field on each image. |
| `digests` | query | boolean |  | Show digest information as a `RepoDigests` field on each image. |
| `manifests` | query | boolean |  | Include `Manifests` in the image summary. |
| `identity` | query | boolean |  | Include `Identity` in each manifest summary. Requires `manifests=1`. |

| Response | Description | Body |
|---|---|---|
| 200 | Summary image data for the images matching the query | array of `ImageSummary` |
| 500 | server error | `ErrorResponse` |

## POST /v1.56/build

operationId: `ImageBuild`

Build an image

Build an image from a tar archive with a `Dockerfile` in it.

The `Dockerfile` specifies how the image is built from the tar archive. It is typically in the archive's root, but can be at a different path or have a different name by specifying the `dockerfile` parameter. [See the `Dockerfile` reference for more information](https://docs.docker.com/engine/reference/builder/).

The Docker daemon performs a preliminary validation of the `Dockerfile` before starting the build, and returns an error if the syntax is incorrect. After that, each instruction is run one-by-one until the ID of the new image is output.

The build is canceled if the client drops the connection by quitting or being killed.

| Parameter | In | Type | Required | Description |
|---|---|---|---|---|
| `dockerfile` | query | string |  | Path within the build context to the `Dockerfile`. This is ignored if `remote` is specified and points to an external `Dockerfile`. |
| `t` | query | string |  | A name and optional tag to apply to the image in the `name:tag` format. If you omit the tag the default `latest` value is assumed. You can provide several `t` parameters. |
| `extrahosts` | query | string |  | Extra hosts to add to /etc/hosts |
| `remote` | query | string |  | A Git repository URI or HTTP/HTTPS context URI. If the URI points to a single text file, the file’s contents are placed into a file called `Dockerfile` and the image is built from that file. If the URI points to a tarball, the file is downloaded by the daemon and the contents therein used as the context for the build. If the URI points to a tarball and the `dockerfile` parameter is also specified, there must be a file with the corresponding path inside the tarball. |
| `q` | query | boolean |  | Suppress verbose build output. |
| `nocache` | query | boolean |  | Do not use the cache when building the image. |
| `cachefrom` | query | string |  | JSON array of images used for build cache resolution. |
| `pull` | query | string |  | Attempt to pull the image even if an older image exists locally. |
| `rm` | query | boolean |  | Remove intermediate containers after a successful build. |
| `forcerm` | query | boolean |  | Always remove intermediate containers, even upon failure. |
| `memory` | query | integer (int64) |  | Set memory limit for build. |
| `memswap` | query | integer (int64) |  | Total memory (memory + swap). Set as `-1` to disable swap. |
| `cpushares` | query | integer (int64) |  | CPU shares (relative weight). |
| `cpusetcpus` | query | string |  | CPUs in which to allow execution (e.g., `0-3`, `0,1`). |
| `cpuperiod` | query | integer (int64) |  | The length of a CPU period in microseconds. |
| `cpuquota` | query | integer (int64) |  | Microseconds of CPU time that the container can get in a CPU period. |
| `buildargs` | query | string |  | JSON map of string pairs for build-time variables. Users pass these values at build-time. Docker uses the buildargs as the environment context for commands run via the `Dockerfile` RUN instruction, or for variable expansion in other `Dockerfile` instructions. This is not meant for passing secret values. For example, the build arg `FOO=bar` would become `{"FOO":"bar"}` in JSON. This would result in the query parameter `buildargs={"FOO":"bar"}`. Note that `{"FOO":"bar"}` should be URI component encoded. [Read more about the buildargs instruction.](https://docs.docker.com/engine/reference/builder/#arg) |
| `shmsize` | query | integer (int64) |  | Size of `/dev/shm` in bytes. The size must be greater than 0. If omitted the system uses 64MB. |
| `squash` | query | boolean |  | Squash the resulting images layers into a single layer. *(Experimental release only.)* |
| `labels` | query | string |  | Arbitrary key/value labels to set on the image, as a JSON map of string pairs. |
| `networkmode` | query | string |  | Sets the networking mode for the run commands during build. Supported standard values are: `bridge`, `host`, `none`, and `container:<name\|id>`. Any other value is taken as a custom network's name or ID to which this container should connect to. |
| `Content-type` | header | string enum: application/x-tar |  |  |
| `X-Registry-Config` | header | string |  | This is a base64-encoded JSON object with auth configurations for multiple registries that a build may refer to. The key is a registry URL, and the value is an auth configuration object, [as described in the authentication section](#section/Authentication). For example: ``` { "docker.example.com": { "username": "janedoe", "password": "hunter2" }, "https://index.docker.io/v1/": { "username": "mobydock", "password": "conta1n3rize14" } } ``` Only the registry domain name (and port if not the default 443) are required. However, for legacy reasons, the Docker Hub registry must be specified with both a `https://` prefix and a `/v1/` suffix even though Docker will prefer to use the v2 registry API. |
| `platform` | query | string |  | Platform in the format os[/arch[/variant]] |
| `target` | query | string |  | Target build stage |
| `outputs` | query | string |  | BuildKit output configuration in the format of a stringified JSON array of objects. Each object must have two top-level properties: `Type` and `Attrs`. The `Type` property must be set to 'moby'. The `Attrs` property is a map of attributes for the BuildKit output configuration. See https://docs.docker.com/build/exporters/oci-docker/ for more information. Example: ``` [{"Type":"moby","Attrs":{"type":"image","force-compression":"true","compression":"zstd"}}] ``` |
| `version` | query | string enum: 1, 2 |  | Version of the builder backend to use. - `1` is the first generation classic (deprecated) builder in the Docker daemon (default) - `2` is [BuildKit](https://github.com/moby/buildkit) |

Request body: string (binary)

| Response | Description | Body |
|---|---|---|
| 200 | no error |  |
| 400 | Bad parameter | `ErrorResponse` |
| 500 | server error | `ErrorResponse` |

## POST /v1.56/build/prune

operationId: `BuildPrune`

Delete builder cache

| Parameter | In | Type | Required | Description |
|---|---|---|---|---|
| `reserved-space` | query | integer (int64) |  | Amount of disk space in bytes to keep for cache |
| `max-used-space` | query | integer (int64) |  | Maximum amount of disk space allowed to keep for cache |
| `min-free-space` | query | integer (int64) |  | Target amount of free disk space after pruning |
| `all` | query | boolean |  | Remove all types of build cache |
| `filters` | query | string |  | A JSON encoded value of the filters (a `map[string][]string`) to process on the list of build cache objects. Available filters: - `until=<timestamp>` remove cache older than `<timestamp>`. The `<timestamp>` can be Unix timestamps, date formatted timestamps, or Go duration strings (e.g. `10m`, `1h30m`) computed relative to the daemon's local time. - `id=<id>` - `parent=<id>` - `type=<string>` - `description=<string>` - `inuse` - `shared` - `private` |

| Response | Description | Body |
|---|---|---|
| 200 | No error | object |
| 500 | Server error | `ErrorResponse` |

## POST /v1.56/images/create

operationId: `ImageCreate`

Create an image

Pull or import an image.

| Parameter | In | Type | Required | Description |
|---|---|---|---|---|
| `fromImage` | query | string |  | Name of the image to pull. If the name includes a tag or digest, specific behavior applies: - If only `fromImage` includes a tag, that tag is used. - If both `fromImage` and `tag` are provided, `tag` takes precedence. - If `fromImage` includes a digest, the image is pulled by digest, and `tag` is ignored. - If neither a tag nor digest is specified, all tags are pulled. |
| `fromSrc` | query | string |  | Source to import. The value may be a URL from which the image can be retrieved or `-` to read the image from the request body. This parameter may only be used when importing an image. |
| `repo` | query | string |  | Repository name given to an image when it is imported. The repo may include a tag. This parameter may only be used when importing an image. |
| `tag` | query | string |  | Tag or digest. If empty when pulling an image, this causes all tags for the given image to be pulled. |
| `message` | query | string |  | Set commit message for imported image. |
| `X-Registry-Auth` | header | string |  | A base64url-encoded auth configuration. Refer to the [authentication section](#section/Authentication) for details. |
| `changes` | query | array of string |  | Apply `Dockerfile` instructions to the image that is created, for example: `changes=ENV DEBUG=true`. Note that `ENV DEBUG=true` should be URI component encoded. Repeat the parameter to apply multiple instructions. Supported `Dockerfile` instructions: `CMD`\|`ENTRYPOINT`\|`ENV`\|`EXPOSE`\|`ONBUILD`\|`USER`\|`VOLUME`\|`WORKDIR` |
| `platform` | query | string |  | Platform in the format os[/arch[/variant]]. When used in combination with the `fromImage` option, the daemon checks if the given image is present in the local image cache with the given OS and Architecture, and otherwise attempts to pull the image. If the option is not set, the host's native OS and Architecture are used. If the given image does not exist in the local image cache, the daemon attempts to pull the image with the host's native OS and Architecture. If the given image does exists in the local image cache, but its OS or architecture does not match, a warning is produced. When used with the `fromSrc` option to import an image from an archive, this option sets the platform information for the imported image. If the option is not set, the host's native OS and Architecture are used for the imported image. |

Request body: string

| Response | Description | Body |
|---|---|---|
| 200 | no error |  |
| 404 | repository does not exist or no read access | `ErrorResponse` |
| 500 | server error | `ErrorResponse` |

## GET /v1.56/images/{name}/json

operationId: `ImageInspect`

Inspect an image

Return low-level information about an image.

| Parameter | In | Type | Required | Description |
|---|---|---|---|---|
| `name` | path | string | yes | Image name or id |
| `manifests` | query | boolean |  | Include Manifests in the image summary. The `manifests` and `platform` options are mutually exclusive, and an error is produced if both are set. |
| `platform` | query | string |  | JSON-encoded OCI platform to select the platform-variant. If omitted, it defaults to any locally available platform, prioritizing the daemon's host platform. If the daemon provides a multi-platform image store, this selects the platform-variant to show inspect. If the image is a single-platform image, or if the multi-platform image does not provide a variant matching the given platform, an error is returned. The `platform` and `manifests` options are mutually exclusive, and an error is produced if both are set. Example: `{"os": "linux", "architecture": "arm", "variant": "v5"}` |

| Response | Description | Body |
|---|---|---|
| 200 | No error | `ImageInspect` |
| 404 | No such image | `ErrorResponse` |
| 500 | Server error | `ErrorResponse` |

## GET /v1.56/images/{name}/attestations

operationId: `ImageAttestations`

Get attestation statements for an image

Return the in-toto attestation statements attached to the image for the
given platform. The daemon locates the attestation manifest(s) that
reference the matching platform image manifest, reads their statement
layers, and returns the verbatim statement JSON together with layer
metadata.

If the image has no attestations an empty array is returned.

| Parameter | In | Type | Required | Description |
|---|---|---|---|---|
| `name` | path | string | yes | Image name or id |
| `platform` | query | array of string |  | JSON-encoded OCI platform to select the image variant whose attestations to return. If omitted, the daemon's default (host) platform is used. Only one platform value is currently accepted; passing more than one returns an error. The parameter is declared as an array so the wire shape can accept multiple values in the future without an API version bump. Example: `{"os": "linux", "architecture": "amd64"}` |
| `type` | query | array of string |  | In-toto predicate type URI to filter returned statements. May be repeated to accept any of several predicate types. If omitted, all statements are returned. Example: `type=https://slsa.dev/provenance/v0.2&type=https://spdx.dev/Document` |
| `statement` | query | boolean |  | Include the verbatim in-toto statement body in each returned entry. Defaults to false; when omitted or false, only the descriptor and predicate type are returned and statement blobs are not read. |

| Response | Description | Body |
|---|---|---|
| 200 | No error | array of `AttestationStatement` |
| 400 | Bad parameter (e.g. malformed `platform` value) | `ErrorResponse` |
| 404 | No such image, or no manifest found for the requested platform | `ErrorResponse` |
| 500 | Server error | `ErrorResponse` |
| 501 | The daemon's image backend does not support attestations. This is returned by the legacy (graphdriver) image store, which does not preserve OCI image indexes. | `ErrorResponse` |

## GET /v1.56/images/{name}/history

operationId: `ImageHistory`

Get the history of an image

Return parent layers of an image.

| Parameter | In | Type | Required | Description |
|---|---|---|---|---|
| `name` | path | string | yes | Image name or ID |
| `platform` | query | string |  | JSON-encoded OCI platform to select the platform-variant. If omitted, it defaults to any locally available platform, prioritizing the daemon's host platform. If the daemon provides a multi-platform image store, this selects the platform-variant to show the history for. If the image is a single-platform image, or if the multi-platform image does not provide a variant matching the given platform, an error is returned. Example: `{"os": "linux", "architecture": "arm", "variant": "v5"}` |

| Response | Description | Body |
|---|---|---|
| 200 | List of image layers | array of `ImageHistoryResponseItem` |
| 404 | No such image | `ErrorResponse` |
| 500 | Server error | `ErrorResponse` |

## POST /v1.56/images/{name}/push

operationId: `ImagePush`

Push an image

Push an image to a registry.

If you wish to push an image on to a private registry, that image must
already have a tag which references the registry. For example,
`registry.example.com/myimage:latest`.

The push is cancelled if the HTTP connection is closed.

| Parameter | In | Type | Required | Description |
|---|---|---|---|---|
| `name` | path | string | yes | Name of the image to push. For example, `registry.example.com/myimage`. The image must be present in the local image store with the same name. The name should be provided without tag; if a tag is provided, it is ignored. For example, `registry.example.com/myimage:latest` is considered equivalent to `registry.example.com/myimage`. Use the `tag` parameter to specify the tag to push. |
| `tag` | query | string |  | Tag of the image to push. For example, `latest`. If no tag is provided, all tags of the given image that are present in the local image store are pushed. |
| `platform` | query | string |  | JSON-encoded OCI platform to select the platform-variant to push. If not provided, all available variants will attempt to be pushed. If the daemon provides a multi-platform image store, this selects the platform-variant to push to the registry. If the image is a single-platform image, or if the multi-platform image does not provide a variant matching the given platform, an error is returned. Example: `{"os": "linux", "architecture": "arm", "variant": "v5"}` |
| `X-Registry-Auth` | header | string | yes | A base64url-encoded auth configuration. Refer to the [authentication section](#section/Authentication) for details. |

| Response | Description | Body |
|---|---|---|
| 200 | No error |  |
| 404 | No such image | `ErrorResponse` |
| 500 | Server error | `ErrorResponse` |

## POST /v1.56/images/{name}/tag

operationId: `ImageTag`

Tag an image

Create a tag that refers to a source image.

This creates an additional reference (tag) to the source image. The tag
can include a different repository name and/or tag. If the repository
or tag already exists, it will be overwritten.

| Parameter | In | Type | Required | Description |
|---|---|---|---|---|
| `name` | path | string | yes | Image name or ID to tag. |
| `repo` | query | string |  | The repository to tag in. For example, `someuser/someimage`. |
| `tag` | query | string |  | The name of the new tag. |

| Response | Description | Body |
|---|---|---|
| 201 | No error |  |
| 400 | Bad parameter | `ErrorResponse` |
| 404 | No such image | `ErrorResponse` |
| 409 | Conflict | `ErrorResponse` |
| 500 | Server error | `ErrorResponse` |

## DELETE /v1.56/images/{name}

operationId: `ImageDelete`

Remove an image

Remove an image, along with any untagged parent images that were
referenced by that image.

Images can't be removed if they have descendant images, are being
used by a running container or are being used by a build.

| Parameter | In | Type | Required | Description |
|---|---|---|---|---|
| `name` | path | string | yes | Image name or ID |
| `force` | query | boolean |  | Remove the image even if it is being used by stopped containers or has other tags |
| `noprune` | query | boolean |  | Do not delete untagged parent images |
| `platforms` | query | array of string |  | Select platform-specific content to delete. Repeat the parameter to select multiple platforms. Each platform is a OCI platform encoded as a JSON string. |

| Response | Description | Body |
|---|---|---|
| 200 | The image was deleted successfully | array of `ImageDeleteResponseItem` |
| 404 | No such image | `ErrorResponse` |
| 409 | Conflict | `ErrorResponse` |
| 500 | Server error | `ErrorResponse` |

## GET /v1.56/images/search

operationId: `ImageSearch`

Search images

Search for an image on Docker Hub.

| Parameter | In | Type | Required | Description |
|---|---|---|---|---|
| `term` | query | string | yes | Term to search |
| `limit` | query | integer |  | Maximum number of results to return |
| `filters` | query | string |  | A JSON encoded value of the filters (a `map[string][]string`) to process on the images list. Available filters: - `is-official=(true\|false)` - `stars=<number>` Matches images that has at least 'number' stars. |

| Response | Description | Body |
|---|---|---|
| 200 | No error | array of object |
| 500 | Server error | `ErrorResponse` |

## POST /v1.56/images/prune

operationId: `ImagePrune`

Delete unused images

| Parameter | In | Type | Required | Description |
|---|---|---|---|---|
| `filters` | query | string |  | Filters to process on the prune list, encoded as JSON (a `map[string][]string`). Available filters: - `dangling=<boolean>` When set to `true` (or `1`), prune only unused *and* untagged images. When set to `false` (or `0`), all unused images are pruned. - `until=<string>` Prune images created before this timestamp. The `<timestamp>` can be Unix timestamps, date formatted timestamps, or Go duration strings (e.g. `10m`, `1h30m`) computed relative to the daemon machine’s time. - `label` (`label=<key>`, `label=<key>=<value>`, `label!=<key>`, or `label!=<key>=<value>`) Prune images with (or without, in case `label!=...` is used) the specified labels. |

| Response | Description | Body |
|---|---|---|
| 200 | No error | object |
| 500 | Server error | `ErrorResponse` |

## POST /v1.56/commit

operationId: `ImageCommit`

Create a new image from a container

| Parameter | In | Type | Required | Description |
|---|---|---|---|---|
| `container` | query | string |  | The ID or name of the container to commit |
| `repo` | query | string |  | Repository name for the created image |
| `tag` | query | string |  | Tag name for the create image |
| `comment` | query | string |  | Commit message |
| `author` | query | string |  | Author of the image (e.g., `John Hannibal Smith <hannibal@a-team.com>`) |
| `pause` | query | boolean |  | Whether to pause the container before committing |
| `changes` | query | string |  | `Dockerfile` instructions to apply while committing |

Request body: `ContainerConfig`

| Response | Description | Body |
|---|---|---|
| 201 | no error | `IDResponse` |
| 404 | no such container | `ErrorResponse` |
| 500 | server error | `ErrorResponse` |

## GET /v1.56/images/{name}/get

operationId: `ImageGet`

Export an image

Get a tarball containing all images and metadata for a repository.

If `name` is a specific name and tag (e.g. `ubuntu:latest`), then only that image (and its parents) are returned. If `name` is an image ID, similarly only that image (and its parents) are returned, but with the exclusion of the `repositories` file in the tarball, as there were no image names referenced.

### Image tarball format

An image tarball contains [Content as defined in the OCI Image Layout Specification](https://github.com/opencontainers/image-spec/blob/v1.1.1/image-layout.md#content).

Additionally, includes the manifest.json file associated with a backwards compatible docker save format.

If the tarball defines a repository, the tarball should also include a `repositories` file at the root that contains a list of repository and tag names mapped to layer IDs.

```json
{
  "hello-world": {
    "latest": "565a9d68a73f6706862bfe8409a7f659776d4d60a8d096eb4a3cbce6999cc2a1"
  }
}
```

| Parameter | In | Type | Required | Description |
|---|---|---|---|---|
| `name` | path | string | yes | Image name or ID |
| `platform` | query | array of string |  | JSON encoded OCI platform describing a platform which will be used to select a platform-specific image to be saved if the image is multi-platform. If not provided, the full multi-platform image will be saved. Example: `{"os": "linux", "architecture": "arm", "variant": "v5"}` |

| Response | Description | Body |
|---|---|---|
| 200 | no error | string (binary) |
| 500 | server error | `ErrorResponse` |

## GET /v1.56/images/get

operationId: `ImageGetAll`

Export several images

Get a tarball containing all images and metadata for several image
repositories.

For each value of the `names` parameter: if it is a specific name and
tag (e.g. `ubuntu:latest`), then only that image (and its parents) are
returned; if it is an image ID, similarly only that image (and its parents)
are returned and there would be no names referenced in the 'repositories'
file for this image ID.

For details on the format, see the [export image endpoint](#operation/ImageGet).

| Parameter | In | Type | Required | Description |
|---|---|---|---|---|
| `names` | query | array of string |  | Image names to filter by. Repeat the parameter for multiple images. |
| `platform` | query | array of string |  | JSON encoded OCI platform(s) which will be used to select the platform-specific image(s) to be saved if the image is multi-platform. If not provided, the full multi-platform image will be saved. Example: `{"os": "linux", "architecture": "arm", "variant": "v5"}` |

| Response | Description | Body |
|---|---|---|
| 200 | no error | string (binary) |
| 500 | server error | `ErrorResponse` |

## POST /v1.56/images/load

operationId: `ImageLoad`

Import images

Load a set of images and tags into a repository.

For details on the format, see the [export image endpoint](#operation/ImageGet).

| Parameter | In | Type | Required | Description |
|---|---|---|---|---|
| `quiet` | query | boolean |  | Suppress progress details during load. |
| `platform` | query | array of string |  | JSON encoded OCI platform(s) which will be used to select the platform-specific image(s) to load if the image is multi-platform. If not provided, the full multi-platform image will be loaded. Example: `{"os": "linux", "architecture": "arm", "variant": "v5"}` |

Request body: string (binary)

| Response | Description | Body |
|---|---|---|
| 200 | no error |  |
| 500 | server error | `ErrorResponse` |
