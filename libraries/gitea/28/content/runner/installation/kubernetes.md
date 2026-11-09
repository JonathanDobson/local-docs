---
sidebar_position: 3
---

# Install on Kubernetes

A runner in Kubernetes can run jobs in two ways:

- **Job pods**: Each job runs in its own pod under the cluster's quotas and policies, without privileged containers. Docker actions and `docker://` steps are not supported.
- **Docker-in-Docker**: Jobs run in a Docker daemon alongside the runner. All workflow features are supported. The daemon is privileged, so a job can break out of its container and access the node.

The manifests below are in the runner repository's [`examples/kubernetes`](https://gitea.com/gitea/runner/src/branch/main/examples/kubernetes) directory. They read the registration token from the `runner-secret` Secret and store the `.runner` registration file in a volume at `/data`. This preserves registration when the pod restarts.

## Job pods

Deploy [`kubernetes-pods.yaml`](https://gitea.com/gitea/runner/src/branch/main/examples/kubernetes/kubernetes-pods.yaml). It registers the runner with a `kubernetes` label:

```text
ubuntu-latest:kubernetes://docker.gitea.com/runner-images:ubuntu-latest
```

The runner creates job pods in its own namespace using its service account. The manifest grants the permissions it needs:

| Resource | Verbs |
| --- | --- |
| `pods` | `create`, `get`, `list`, `delete` |
| `pods/exec` | `create`, `get` |
| `pods/log` | `get` |
| `secrets` | `create`, `delete` |

The cluster must run Kubernetes 1.30 or later. Job images need `sh`, `tar`, `tail`, and `env`. A runner outside the cluster uses the current context from the first file in `$KUBECONFIG`, or from `~/.kube/config` if `$KUBECONFIG` is unset.

Use pod templates to set resources, node selectors, image pull secrets, and other settings for job pods:

```yaml
kubernetes:
  pod_template:
    spec:
      containers:
        - name: job          # merged into the job container
          resources:
            limits:
              memory: 4Gi
        - name: $services    # merged into every service container
          resources:
            limits:
              memory: 1Gi
  pod_templates:
    gpu:                     # merged on top for jobs with runs-on: gpu
      spec:
        nodeSelector:
          nvidia.com/gpu.present: "true"
```

Services share the job pod's network. Steps reach them by their service ID or `localhost`. Two services cannot use the same port. Only `--health-*` is supported in a service's `options`. Job pods do not receive a service account token unless the template sets `automountServiceAccountToken: true`.

## Docker-in-Docker

| Manifest | Deployment type |
| --- | --- |
| [`dind-docker.yaml`](https://gitea.com/gitea/runner/src/branch/main/examples/kubernetes/dind-docker.yaml) | `Deployment` with a privileged `docker:dind` sidecar |
| [`statefulset-dind.yaml`](https://gitea.com/gitea/runner/src/branch/main/examples/kubernetes/statefulset-dind.yaml) | `StatefulSet` with a privileged `docker:dind` sidecar, for multiple replicas |
| [`rootless-docker.yaml`](https://gitea.com/gitea/runner/src/branch/main/examples/kubernetes/rootless-docker.yaml) | `Deployment` with the `dind-rootless` image |

Use the `StatefulSet` for multiple replicas so each has its own registration volume. A [Helm chart](https://gitea.com/gitea/helm-actions) is also available.

The Docker daemon stores images pulled for jobs in `/var/lib/docker`, or `/home/rootless/.local/share/docker` in the rootless image. The manifests mount this directory on a volume so a new pod does not pull every image again.

## Shutdown

The manifests set `terminationGracePeriodSeconds` to give a pod three hours to stop. To let running jobs finish, set `runner.shutdown_timeout` a little lower than that grace period. Otherwise, the runner cancels running jobs when the pod stops.
