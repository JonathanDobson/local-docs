---
title: "Integrating Docker Scout with other systems"
source: https://docs.docker.com/scout/integrations/
---

# Integrating Docker Scout with other systems


By default, Docker Scout integrates with your Docker organization and your
Docker Scout-enabled repositories on Docker Hub. You can integrate Docker Scout
with additional third-party systems to get access to even more insights,
including real-time information about you running workloads.

## Integration categories

You'll get different insights depending on where and how you choose to integrate
Docker Scout.

### Container registries

Integrating Docker Scout with third-party container
registries enables Docker Scout to run image analysis on those repositories,
so that you can get insights into the composition of those images even if they
aren't hosted on Docker Hub.

Docker Scout integrates with any Docker/OCI-compliant registry using
[`docker scout watch`](/scout/integrations/registry/), including Amazon ECR, Azure
Container Registry, JFrog Artifactory, Harbor, and Sonatype Nexus.

### Continuous Integration

Integrating Docker Scout with Continuous Integration (CI) systems is a great way
to get instant, automatic feedback about your security posture in your inner
loop. Analysis running in CI also gets the benefit of additional context that's
useful for getting even more insights.

The following CI integrations are available:

- [GitHub Actions](/scout/integrations/ci/gha/)
- [GitLab](/scout/integrations/ci/gitlab/)
- [Microsoft Azure DevOps Pipelines](/scout/integrations/ci/azure/)
- [Circle CI](/scout/integrations/ci/circle-ci/)
- [Jenkins](/scout/integrations/ci/jenkins/)

### Environment monitoring

Environment monitoring refers to integrating Docker Scout with your deployments.
This can give you information in real-time about your running container workloads.

Integrating with environments lets you compare production workloads to other
versions, in your image repositories or in your other environments.

The following environment monitoring integrations are available:
- [Docker Scout GitHub Action](/scout/integrations/environment/)
- [Generic CLI integration](/scout/integrations/environment/cli/)
For more information about environment integrations, see
[Environments](/scout/integrations/environment/).
