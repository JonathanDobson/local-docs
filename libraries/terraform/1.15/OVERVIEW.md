# Terraform 1.15 (CLI and configuration language)

HashiCorp Terraform core, release line **1.15**. The docs are the `v1.15.x` folder of
HashiCorp's `web-unified-docs` repo (what developer.hashicorp.com/terraform shows for
1.15), commit `af88f7b`, describing the latest 1.15 patch, **1.15.9**. The CLI installed
on this machine is **1.15.5**; the 1.15.6–1.15.9 changes are bug fixes (see the
changelog). Provider docs (`aws_*` resources) are a separate set:
`terraform-provider-aws` 5.100.0.

## Layout

- `content/docs/cli/` — the `terraform` command: `commands/` (one page per command,
  `state/`, `workspace/`, `providers/`, `stacks/`), `config/` (CLI config file,
  environment variables), `init/`, `run/`, `state/`, `workspaces/`, `import/`, `test/`,
  `cloud/` (HCP Terraform integration), `auth/`, `plugins/`.
- `content/docs/language/` — the configuration language: `block/` (reference page per
  block: `terraform`, `resource`, `data`, `variable`, `output`, `locals`, `module`,
  `provider`, `moved`, `removed`, `import`, `check`, `ephemeral`, `action`), `backend/`
  (one page per backend type, `s3.mdx`), `state/`, `values/`, `expressions/`,
  `functions/` (one page per built-in function), `meta-arguments/`, `modules/`,
  `providers/`, `files/` (lock file, override files, `.tftest.hcl`), `tests/`,
  `stacks/`, `upgrade-guides/`.
- `content/docs/intro/`, `content/docs/internals/` — concepts; JSON output formats,
  debugging, registry protocols.
- `content/release-notes/CHANGELOG-v1.15.9.md` — 1.15.0 to 1.15.9.

## Where to look for…

| Task | File |
|---|---|
| S3 backend: `bucket`, `key`, `region`, `encrypt`, `use_lockfile`, `kms_key_id`, IAM permissions, workspaces | `docs/language/backend/s3.mdx` |
| Partial backend configuration, `-backend-config` files | `docs/language/backend/index.mdx` (Partial configuration) |
| `terraform init` options (`-backend-config`, `-reconfigure`, `-migrate-state`, `-upgrade`) | `docs/cli/commands/init.mdx` |
| `plan` / `apply` options (`-var`, `-var-file`, `-out`, saved plans) | `docs/cli/commands/plan.mdx`, `apply.mdx` |
| `validate`, `fmt -check -recursive` | `docs/cli/commands/validate.mdx`, `fmt.mdx` |
| Input variables, `.tfvars` / `*.auto.tfvars`, precedence, `sensitive`, `validation` | `docs/language/values/variables.mdx`, `docs/language/block/variable.mdx` |
| Environment variables (`TF_VAR_name`, `TF_LOG`, `TF_DATA_DIR`) | `docs/cli/config/environment-variables.mdx` |
| State locking, remote state, workspaces | `docs/language/state/` |
| `terraform` block, `required_providers`, `required_version` | `docs/language/block/terraform.mdx` |
| Dependency lock file `.terraform.lock.hcl` | `docs/language/files/dependency-lock.mdx` |
| Version constraint syntax (`~> 5.0`) | `docs/language/expressions/version-constraints.mdx` |
| `count`, `for_each`, `depends_on`, `lifecycle` | `docs/language/meta-arguments/` |
| Refactoring: `moved`, `removed`, `import` blocks | `docs/language/block/moved.mdx`, `removed.mdx`, `import.mdx` |
| Built-in functions | `docs/language/functions/<name>.mdx` |
| Upgrading to 1.15 | `docs/language/upgrade-guides/index.mdx`, the changelog |

## Version notes (from the changelog)

- 1.15.0 (2026-04-29): `deprecated` attribute on `variable` and `output` blocks;
  `output` blocks can have a type constraint; variables and locals allowed in module
  `source` and `version`; new `convert` function; `terraform validate` now checks the
  `backend` block; backend/s3 supports authentication via `aws login`.
- 1.15.5 (2026-05-27, installed here): module `version` may evaluate to `null`.
- 1.15.6–1.15.9: bug fixes; 1.15.8 changes `terraform init` output and order (module
  installation after backend initialization again); 1.15.9 makes `validate` report
  invalid `backend`/`cloud`/`import`/`list` blocks in child modules.
- S3 backend: `dynamodb_table` is **deprecated**; locking uses `use_lockfile = true`,
  which writes `<key>.tflock` beside the state object (default `false`).

## Search tips

- Pages are MDX with HashiCorp components (`<CodeBlockConfig>`, `<Note>`, `<Tabs>`).
- The S3 lock file is "lockfile" / `.tflock`; DynamoDB locking is the deprecated path.
- "Partial configuration" is the term for leaving backend settings out of the code and
  passing them with `-backend-config=FILE` or `-backend-config="KEY=VALUE"`.
- `.tfvars` files are called "variable definition files".
- HCP Terraform integration pages live under `docs/cli/cloud/`.
