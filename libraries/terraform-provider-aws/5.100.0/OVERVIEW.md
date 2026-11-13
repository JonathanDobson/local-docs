# Terraform AWS Provider 5.100.0 — overview

HashiCorp's **Terraform AWS provider**, release **v5.100.0** — the last of the 5.x
line, which this user's Terraform pins (`~> 5.0`). (The newest provider is 6.73.0;
6.x isn't included.) The docs are the Markdown the Terraform Registry renders,
taken from `website/docs` at the release tag, plus the 5.x changelog.

## Layout

| Folder | What it holds |
|---|---|
| `content/r/<name>.html.markdown` | **Resources**: `r/s3_bucket.html.markdown` documents `aws_s3_bucket` — Example Usage, Argument Reference, Attribute Reference, Timeouts, Import |
| `content/d/<name>.html.markdown` | **Data sources**: `d/iam_policy_document.html.markdown` documents `data "aws_iam_policy_document"` |
| `content/ephemeral-resources/` | Ephemeral resources (values never stored in state): `secretsmanager_secret_version`, `ssm_parameter`, `kms_secrets`, `lambda_invocation`, `eks_cluster_auth`… |
| `content/functions/` | Provider functions: `arn_build`, `arn_parse`, `trim_iam_role_path` |
| `content/guides/` | `version-5-upgrade` (and 2–4), `resource-tagging` (`default_tags`), `custom-service-endpoints`, `continuous-validation-examples`, `using-aws-with-awscc-provider` |
| `content/index.html.markdown` | Provider configuration: authentication and credential order, `region`, `assume_role`, `default_tags`, `ignore_tags`, all provider arguments |
| `content/release-notes/CHANGELOG-5.x.md` | Every 5.x release, newest first |

Each page's front matter has `subcategory` (the AWS service, e.g. "S3 (Simple Storage)") and `page_title` ("AWS: aws_s3_bucket").

## Where to look for…

- **A resource's arguments and attributes** — `r/<name without aws_>.html.markdown` (`r/lambda_function`, `r/cloudfront_distribution`, `r/lb_listener`, `r/cloudwatch_metric_alarm`, `r/secretsmanager_secret`).
- **Look something up instead of creating it** — `d/<name>.html.markdown` (`d/caller_identity`, `d/iam_policy_document`, `d/ami`).
- **Import an existing resource** — the "Import" section at the end of each resource page.
- **Provider authentication, regions, assume role** — `index.html.markdown`.
- **Tags on every resource** — `guides/resource-tagging.html.markdown` (`default_tags`).
- **Upgrading from 4.x** — `guides/version-5-upgrade.html.markdown`.
- **When a resource or argument appeared or changed** — `release-notes/CHANGELOG-5.x.md`.
- **Reading a secret without storing it in state** — `ephemeral-resources/secretsmanager_secret_version.html.markdown`.

## Version notes

- **5.0.0** (from `guides/version-5-upgrade.html.markdown`): EC2-Classic and Macie Classic retired; provider argument and `default_tags` changes; many per-resource changes (e.g. `aws_db_instance` uses `db_name` instead of `name` and its `id` is no longer the identifier).
- 5.x adds ephemeral resources (the pages call them a new feature that may evolve, linking Terraform's v1.10 language docs) and provider functions.
- 5.100.0 (June 2025) adds resources such as `aws_dsql_cluster` and `aws_vpc_route_server`.

## Search tips

- File names drop the `aws_` prefix: `aws_iam_role` → `r/iam_role.html.markdown`.
- Sections are always "Example Usage", "Argument Reference", "Attribute Reference", "Import"; arguments are listed as `` * `name` - (Required|Optional) … ``.
- Search by the AWS service's subcategory name ("S3 (Simple Storage)", "Lambda") to find all its resources.
