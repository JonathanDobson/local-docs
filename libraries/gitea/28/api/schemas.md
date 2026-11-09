# Gitea API 28.3.0 — schemas

## APIError

APIError is an api error with a message

| Field | Type | Required | Description |
|---|---|---|---|
| `message` | string |  | Message contains the error description |
| `url` | string (uri) |  | URL contains the documentation URL for this error |

## AccessLevelName

Type: string enum: none, read, write, admin, owner

## AccessToken

| Field | Type | Required | Description |
|---|---|---|---|
| `created_at` | string (date-time) |  | The timestamp when the token was created |
| `id` | integer (int64) |  | The unique identifier of the access token |
| `last_used_at` | string (date-time) |  | The timestamp when the token was last used |
| `name` | string |  | The name of the access token |
| `scopes` | array of string |  | The scopes granted to this access token |
| `sha1` | string |  | The SHA1 hash of the access token |
| `token_last_eight` | string |  | The last eight characters of the token |

## ActionArtifact

ActionArtifact represents a ActionArtifact

| Field | Type | Required | Description |
|---|---|---|---|
| `archive_download_url` | string (uri) |  |  |
| `created_at` | string (date-time) |  |  |
| `expired` | boolean |  |  |
| `expires_at` | string (date-time) |  |  |
| `id` | integer (int64) |  |  |
| `name` | string |  |  |
| `size_in_bytes` | integer (int64) |  |  |
| `updated_at` | string (date-time) |  |  |
| `url` | string (uri) |  |  |
| `workflow_run` | `ActionWorkflowRun` |  |  |

## ActionArtifactsResponse

ActionArtifactsResponse returns ActionArtifacts

| Field | Type | Required | Description |
|---|---|---|---|
| `artifacts` | array of `ActionArtifact` |  |  |
| `total_count` | integer (int64) |  |  |

## ActionRunner

ActionRunner represents a Runner

| Field | Type | Required | Description |
|---|---|---|---|
| `busy` | boolean |  |  |
| `disabled` | boolean |  |  |
| `ephemeral` | boolean |  |  |
| `id` | integer (int64) |  |  |
| `labels` | array of `ActionRunnerLabel` |  |  |
| `name` | string |  |  |
| `status` | string |  |  |

## ActionRunnerLabel

ActionRunnerLabel represents a Runner Label

| Field | Type | Required | Description |
|---|---|---|---|
| `id` | integer (int64) |  |  |
| `name` | string |  |  |
| `type` | string |  |  |

## ActionRunnersResponse

ActionRunnersResponse returns Runners

| Field | Type | Required | Description |
|---|---|---|---|
| `runners` | array of `ActionRunner` |  |  |
| `total_count` | integer (int64) |  |  |

## ActionTask

ActionTask represents a ActionTask

| Field | Type | Required | Description |
|---|---|---|---|
| `created_at` | string (date-time) |  |  |
| `display_title` | string |  | DisplayTitle is the display title for the workflow run |
| `event` | string |  | Event is the type of event that triggered the workflow |
| `head_branch` | string |  | HeadBranch is the branch that triggered the workflow |
| `head_sha` | string |  | HeadSHA is the commit SHA that triggered the workflow |
| `id` | integer (int64) |  | ID is the unique identifier for the action task |
| `name` | string |  | Name is the name of the workflow |
| `run_number` | integer (int64) |  | RunNumber is the sequential number of the workflow run |
| `run_started_at` | string (date-time) |  |  |
| `status` | string |  | Status indicates the current status of the workflow run |
| `updated_at` | string (date-time) |  |  |
| `url` | string (uri) |  | URL is the API URL for this workflow run |
| `workflow_id` | string |  | WorkflowID is the identifier of the workflow |

## ActionTaskResponse

ActionTaskResponse returns a ActionTask

| Field | Type | Required | Description |
|---|---|---|---|
| `total_count` | integer (int64) |  | TotalCount is the total number of workflow runs |
| `workflow_runs` | array of `ActionTask` |  | Entries contains the list of workflow runs |

## ActionVariable

ActionVariable return value of the query API

| Field | Type | Required | Description |
|---|---|---|---|
| `data` | string |  | the value of the variable |
| `description` | string |  | the description of the variable |
| `name` | string |  | the name of the variable |
| `owner_id` | integer (int64) |  | the owner to which the variable belongs |
| `repo_id` | integer (int64) |  | the repository to which the variable belongs |

## ActionWorkflow

ActionWorkflow represents a ActionWorkflow

| Field | Type | Required | Description |
|---|---|---|---|
| `badge_url` | string (uri) |  | BadgeURL is the URL for the workflow badge |
| `created_at` | string (date-time) |  |  |
| `deleted_at` | string (date-time) |  |  |
| `html_url` | string (uri) |  | HTMLURL is the web URL for viewing the workflow |
| `id` | string |  | ID is the unique identifier for the workflow |
| `name` | string |  | Name is the name of the workflow |
| `path` | string |  | Path is the file path of the workflow |
| `state` | string |  | State indicates if the workflow is active or disabled |
| `updated_at` | string (date-time) |  |  |
| `url` | string (uri) |  | URL is the API URL for this workflow |

## ActionWorkflowJob

ActionWorkflowJob represents a WorkflowJob

| Field | Type | Required | Description |
|---|---|---|---|
| `completed_at` | string (date-time) |  |  |
| `conclusion` | string |  |  |
| `created_at` | string (date-time) |  |  |
| `head_branch` | string |  |  |
| `head_sha` | string |  |  |
| `html_url` | string (uri) |  |  |
| `id` | integer (int64) |  |  |
| `labels` | array of string |  |  |
| `name` | string |  |  |
| `run_attempt` | integer (int64) |  |  |
| `run_id` | integer (int64) |  |  |
| `run_url` | string (uri) |  |  |
| `runner_id` | integer (int64) |  |  |
| `runner_name` | string |  |  |
| `started_at` | string (date-time) |  |  |
| `status` | string |  |  |
| `steps` | array of `ActionWorkflowStep` |  |  |
| `url` | string (uri) |  |  |

## ActionWorkflowJobsResponse

ActionWorkflowJobsResponse returns ActionWorkflowJobs

| Field | Type | Required | Description |
|---|---|---|---|
| `jobs` | array of `ActionWorkflowJob` |  |  |
| `total_count` | integer (int64) |  |  |

## ActionWorkflowResponse

ActionWorkflowResponse returns a ActionWorkflow

| Field | Type | Required | Description |
|---|---|---|---|
| `total_count` | integer (int64) |  |  |
| `workflows` | array of `ActionWorkflow` |  |  |

## ActionWorkflowRun

ActionWorkflowRun represents a WorkflowRun

| Field | Type | Required | Description |
|---|---|---|---|
| `actor` | `User` |  |  |
| `artifacts_url` | string (uri) |  |  |
| `cancel_url` | string (uri) |  |  |
| `completed_at` | string (date-time) |  |  |
| `conclusion` | string |  |  |
| `created_at` | string (date-time) |  |  |
| `display_title` | string |  |  |
| `event` | string |  |  |
| `head_branch` | string |  |  |
| `head_repository` | `Repository` |  |  |
| `head_sha` | string |  |  |
| `html_url` | string (uri) |  |  |
| `id` | integer (int64) |  |  |
| `jobs_url` | string (uri) |  |  |
| `logs_url` | string (uri) |  |  |
| `path` | string |  |  |
| `previous_attempt_url` | string (uri) |  | PreviousAttemptURL is the API URL of the previous attempt of this run, e.g. ".../actions/runs/{run_id}/attempts/{attempt-1}". It is set only when the current attempt is > 1 (i.e. a rerun). For the first attempt, or for legacy runs that pre-date ActionRunAttempt, it is null. |
| `pull_requests` | array of `PullRequestMinimal` |  |  |
| `repository` | `Repository` |  |  |
| `repository_id` | integer (int64) |  |  |
| `rerun_url` | string (uri) |  |  |
| `run_attempt` | integer (int64) |  | RunAttempt is 1-based for runs created after ActionRunAttempt was introduced. A value of 0 is a legacy-only sentinel for runs created before attempts existed and indicates no corresponding /attempts/{n} resource is available. |
| `run_number` | integer (int64) |  |  |
| `started_at` | string (date-time) |  |  |
| `status` | string |  |  |
| `trigger_actor` | `User` |  |  |
| `updated_at` | string (date-time) |  |  |
| `url` | string (uri) |  |  |

## ActionWorkflowRunsResponse

ActionWorkflowRunsResponse returns ActionWorkflowRuns

| Field | Type | Required | Description |
|---|---|---|---|
| `total_count` | integer (int64) |  |  |
| `workflow_runs` | array of `ActionWorkflowRun` |  |  |

## ActionWorkflowStep

ActionWorkflowStep represents a step of a WorkflowJob

| Field | Type | Required | Description |
|---|---|---|---|
| `completed_at` | string (date-time) |  |  |
| `conclusion` | string |  |  |
| `name` | string |  |  |
| `number` | integer (int64) |  |  |
| `started_at` | string (date-time) |  |  |
| `status` | string |  |  |

## Activity

| Field | Type | Required | Description |
|---|---|---|---|
| `act_user` | `User` |  |  |
| `act_user_id` | integer (int64) |  | The ID of the user who performed the action |
| `comment` | `Comment` |  |  |
| `comment_id` | integer (int64) |  | The ID of the comment associated with the activity (if applicable) |
| `content` | string |  | Additional content or details about the activity |
| `created` | string (date-time) |  | The date and time when the activity occurred |
| `id` | integer (int64) |  | The unique identifier of the activity |
| `is_private` | boolean |  | Whether this activity is from a private repository |
| `op_type` | string enum: create_repo, rename_repo, star_repo, watch_repo, commit_repo, create_issue, create_pull_request, transfer_repo, push_tag, comment_issue, merge_pull_request, close_issue |  | the type of action |
| `ref_name` | string |  | The name of the git reference (branch/tag) associated with the activity |
| `repo` | `Repository` |  |  |
| `repo_id` | integer (int64) |  | The ID of the repository associated with the activity |
| `user_id` | integer (int64) |  | The ID of the user who receives/sees this activity |

## AddCollaboratorOption

AddCollaboratorOption options when adding a user as a collaborator of a repository

| Field | Type | Required | Description |
|---|---|---|---|
| `permission` | allOf(`RepoWritePermission`) |  | Permission level to grant the collaborator |

## AddTimeOption

AddTimeOption options for adding time to an issue

| Field | Type | Required | Description |
|---|---|---|---|
| `created` | string (date-time) |  |  |
| `time` | integer (int64) | yes | time in seconds |
| `user_name` | string |  | username of the user who spent the time working on the issue (optional) |

## AnnotatedTag

AnnotatedTag represents an annotated tag

| Field | Type | Required | Description |
|---|---|---|---|
| `message` | string |  | The message associated with the annotated tag |
| `object` | `AnnotatedTagObject` |  |  |
| `sha` | string |  | The SHA hash of the annotated tag |
| `tag` | string |  | The name of the annotated tag |
| `tagger` | `CommitUser` |  |  |
| `url` | string (uri) |  | The URL to access the annotated tag |
| `verification` | `PayloadCommitVerification` |  |  |

## AnnotatedTagObject

AnnotatedTagObject contains meta information of the tag object

| Field | Type | Required | Description |
|---|---|---|---|
| `sha` | string |  | The SHA hash of the tagged object |
| `type` | string |  | The type of the tagged object (e.g., commit, tree) |
| `url` | string (uri) |  | The URL to access the tagged object |

## ApplyDiffPatchFileOptions

ApplyDiffPatchFileOptions options for applying a diff patch
Note: `author` and `committer` are optional (if only one is given, it will be used for the other, otherwise the authenticated user will be used)

| Field | Type | Required | Description |
|---|---|---|---|
| `author` | `Identity` |  |  |
| `branch` | string |  | branch (optional) is the base branch for the changes. If not supplied, the default branch is used |
| `committer` | `Identity` |  |  |
| `content` | string | yes |  |
| `dates` | `CommitDateOptions` |  |  |
| `force_push` | boolean |  | force_push (optional) will do a force-push if the new branch already exists |
| `message` | string |  | message (optional) is the commit message of the changes. If not supplied, a default message will be used |
| `new_branch` | string |  | new_branch (optional) will make a new branch from base branch for the changes. If not supplied, the changes will be committed to the base branch |
| `signoff` | boolean |  | Add a Signed-off-by trailer by the committer at the end of the commit log message. |

## Attachment

Attachment a generic attachment

| Field | Type | Required | Description |
|---|---|---|---|
| `browser_download_url` | string (uri) |  | DownloadURL is the URL to download the attachment |
| `created_at` | string (date-time) |  | Created is the time when the attachment was uploaded |
| `download_count` | integer (int64) |  | DownloadCount is the number of times the attachment has been downloaded |
| `id` | integer (int64) |  | ID is the unique identifier for the attachment |
| `name` | string |  | Name is the filename of the attachment |
| `size` | integer (int64) |  | Size is the file size in bytes |
| `uuid` | string |  | UUID is the unique identifier for the attachment file |

## Badge

Badge represents a user badge

| Field | Type | Required | Description |
|---|---|---|---|
| `description` | string |  |  |
| `id` | integer (int64) |  |  |
| `image_url` | string (uri) |  |  |
| `slug` | string |  |  |

## Branch

Branch represents a repository branch

| Field | Type | Required | Description |
|---|---|---|---|
| `commit` | `PayloadCommit` |  |  |
| `effective_branch_protection_name` | string |  | EffectiveBranchProtectionName is the name of the effective branch protection rule |
| `enable_status_check` | boolean |  | EnableStatusCheck indicates if status checks are enabled |
| `name` | string |  | Name is the branch name |
| `protected` | boolean |  | Protected indicates if the branch is protected |
| `required_approvals` | integer (int64) |  | RequiredApprovals is the number of required approvals for pull requests |
| `status_check_contexts` | array of string |  | StatusCheckContexts contains the list of required status check contexts |
| `user_can_merge` | boolean |  | UserCanMerge indicates if the current user can merge to this branch |
| `user_can_push` | boolean |  | UserCanPush indicates if the current user can push to this branch |

## BranchProtection

BranchProtection represents a branch protection for a repository

| Field | Type | Required | Description |
|---|---|---|---|
| `approvals_whitelist_teams` | array of string |  |  |
| `approvals_whitelist_username` | array of string |  |  |
| `block_admin_merge_override` | boolean |  |  |
| `block_on_codeowner_reviews` | boolean |  |  |
| `block_on_official_review_requests` | boolean |  |  |
| `block_on_outdated_branch` | boolean |  |  |
| `block_on_rejected_reviews` | boolean |  |  |
| `branch_name` | string |  |  |
| `bypass_allowlist_teams` | array of string |  |  |
| `bypass_allowlist_usernames` | array of string |  |  |
| `created_at` | string (date-time) |  |  |
| `dismiss_stale_approvals` | boolean |  |  |
| `enable_approvals_whitelist` | boolean |  |  |
| `enable_bypass_allowlist` | boolean |  |  |
| `enable_force_push` | boolean |  |  |
| `enable_force_push_allowlist` | boolean |  |  |
| `enable_merge_whitelist` | boolean |  |  |
| `enable_push` | boolean |  |  |
| `enable_push_whitelist` | boolean |  |  |
| `enable_status_check` | boolean |  |  |
| `force_push_allowlist_deploy_keys` | boolean |  |  |
| `force_push_allowlist_teams` | array of string |  |  |
| `force_push_allowlist_usernames` | array of string |  |  |
| `ignore_stale_approvals` | boolean |  |  |
| `merge_whitelist_teams` | array of string |  |  |
| `merge_whitelist_usernames` | array of string |  |  |
| `priority` | integer (int64) |  | Priority is the priority of this branch protection rule |
| `protected_file_patterns` | string |  |  |
| `push_whitelist_deploy_keys` | boolean |  |  |
| `push_whitelist_teams` | array of string |  |  |
| `push_whitelist_usernames` | array of string |  |  |
| `require_signed_commits` | boolean |  |  |
| `required_approvals` | integer (int64) |  |  |
| `rule_name` | string |  | RuleName is the name of the branch protection rule |
| `status_check_contexts` | array of string |  |  |
| `unprotected_file_patterns` | string |  |  |
| `updated_at` | string (date-time) |  |  |

## ChangeFileOperation

ChangeFileOperation for creating, updating or deleting a file

| Field | Type | Required | Description |
|---|---|---|---|
| `content` | string |  | new or updated file content, it must be base64 encoded |
| `from_path` | string |  | old path of the file to move |
| `operation` | string enum: create, update, upload, rename, delete | yes | indicates what to do with the file: "create" for creating a new file, "update" for updating an existing file, "upload" for creating or updating a file, "rename" for renaming a file, and "delete" for deleting an existing file. |
| `path` | string | yes | path to the existing or new file |
| `sha` | string |  | the blob ID (SHA) for the file that already exists, required for changing existing files |

## ChangeFilesOptions

ChangeFilesOptions options for creating, updating or deleting multiple files
Note: `author` and `committer` are optional (if only one is given, it will be used for the other, otherwise the authenticated user will be used)

| Field | Type | Required | Description |
|---|---|---|---|
| `author` | `Identity` |  |  |
| `branch` | string |  | branch (optional) is the base branch for the changes. If not supplied, the default branch is used |
| `committer` | `Identity` |  |  |
| `dates` | `CommitDateOptions` |  |  |
| `files` | array of `ChangeFileOperation` | yes | list of file operations |
| `force_push` | boolean |  | force_push (optional) will do a force-push if the new branch already exists |
| `message` | string |  | message (optional) is the commit message of the changes. If not supplied, a default message will be used |
| `new_branch` | string |  | new_branch (optional) will make a new branch from base branch for the changes. If not supplied, the changes will be committed to the base branch |
| `signoff` | boolean |  | Add a Signed-off-by trailer by the committer at the end of the commit log message. |

## ChangedFile

ChangedFile store information about files affected by the pull request

| Field | Type | Required | Description |
|---|---|---|---|
| `additions` | integer (int64) |  | The number of lines added to the file |
| `changes` | integer (int64) |  | The total number of changes to the file |
| `contents_url` | string (uri) |  | The API URL to get the file contents |
| `deletions` | integer (int64) |  | The number of lines deleted from the file |
| `filename` | string |  | The name of the changed file |
| `html_url` | string (uri) |  | The HTML URL to view the file changes |
| `previous_filename` | string |  | The previous filename if the file was renamed |
| `raw_url` | string (uri) |  | The raw URL to download the file |
| `status` | string |  | The status of the file change (added, modified, deleted, etc.) |

## CombinedStatus

CombinedStatus holds the combined state of several statuses for a single commit

| Field | Type | Required | Description |
|---|---|---|---|
| `commit_url` | string (uri) |  | CommitURL is the API URL for the commit |
| `repository` | `Repository` |  |  |
| `sha` | string |  | SHA is the commit SHA this status applies to |
| `state` | allOf(`CommitStatusState`) |  | State is the overall combined status state |
| `statuses` | array of `CommitStatus` |  | Statuses contains all individual commit statuses |
| `total_count` | integer (int64) |  | TotalCount is the total number of statuses |
| `url` | string (uri) |  | URL is the API URL for this combined status |

## Comment

Comment represents a comment on a commit or issue

| Field | Type | Required | Description |
|---|---|---|---|
| `assets` | array of `Attachment` |  | Attachments contains files attached to the comment |
| `body` | string |  | Body contains the comment text content |
| `created_at` | string (date-time) |  |  |
| `html_url` | string (uri) |  | HTMLURL is the web URL for viewing the comment |
| `id` | integer (int64) |  | ID is the unique identifier for the comment |
| `issue_url` | string (uri) |  | IssueURL is the API URL for the issue |
| `original_author` | string |  | OriginalAuthor is the original author name (for imported comments) |
| `original_author_id` | integer (int64) |  | OriginalAuthorID is the original author ID (for imported comments) |
| `pull_request_url` | string (uri) |  | PRURL is the API URL for the pull request (if applicable) |
| `updated_at` | string (date-time) |  |  |
| `user` | `User` |  |  |

## Commit

| Field | Type | Required | Description |
|---|---|---|---|
| `author` | `User` |  |  |
| `commit` | `RepoCommit` |  |  |
| `committer` | `User` |  |  |
| `created` | string (date-time) |  | Created is the time when the commit was created |
| `files` | array of `CommitAffectedFiles` |  | Files contains information about files affected by the commit |
| `html_url` | string (uri) |  | HTMLURL is the web URL for viewing the commit |
| `parents` | array of `CommitMeta` |  | Parents contains the parent commit information |
| `sha` | string |  | SHA is the commit SHA hash |
| `stats` | `CommitStats` |  |  |
| `url` | string (uri) |  | URL is the API URL for the commit |

## CommitAffectedFiles

CommitAffectedFiles store information about files affected by the commit

| Field | Type | Required | Description |
|---|---|---|---|
| `filename` | string |  | Filename is the path of the affected file |
| `status` | string |  | Status indicates how the file was affected (added, modified, deleted) |

## CommitDateOptions

CommitDateOptions store dates for GIT_AUTHOR_DATE and GIT_COMMITTER_DATE

| Field | Type | Required | Description |
|---|---|---|---|
| `author` | string (date-time) |  | Author is the author date for the commit |
| `committer` | string (date-time) |  | Committer is the committer date for the commit |

## CommitMeta

| Field | Type | Required | Description |
|---|---|---|---|
| `created` | string (date-time) |  | Created is the time when the commit was created |
| `sha` | string |  | SHA is the commit SHA hash |
| `url` | string (uri) |  | URL is the API URL for the commit |

## CommitStats

CommitStats is statistics for a RepoCommit

| Field | Type | Required | Description |
|---|---|---|---|
| `additions` | integer (int64) |  | Additions is the number of lines added |
| `deletions` | integer (int64) |  | Deletions is the number of lines deleted |
| `total` | integer (int64) |  | Total is the total number of lines changed |

## CommitStatus

CommitStatus holds a single status of a single Commit

| Field | Type | Required | Description |
|---|---|---|---|
| `context` | string |  | Context is the unique context identifier for the status |
| `created_at` | string (date-time) |  |  |
| `creator` | `User` |  |  |
| `description` | string |  | Description provides a brief description of the status |
| `id` | integer (int64) |  | ID is the unique identifier for the commit status |
| `status` | allOf(`CommitStatusState`) |  | State represents the status state (pending, success, error, failure) |
| `target_url` | string (uri) |  | TargetURL is the URL to link to for more details |
| `updated_at` | string (date-time) |  |  |
| `url` | string (uri) |  | URL is the API URL for this status |

## CommitStatusState

Type: string enum: pending, success, error, failure, warning, skipped

## CommitUser

| Field | Type | Required | Description |
|---|---|---|---|
| `date` | string |  | Date is the commit date in string format |
| `email` | string (email) |  | Email is the person's email address |
| `name` | string |  | Name is the person's name |

## Compare

| Field | Type | Required | Description |
|---|---|---|---|
| `commits` | array of `Commit` |  |  |
| `total_commits` | integer (int64) |  |  |

## ContentsExtResponse

| Field | Type | Required | Description |
|---|---|---|---|
| `dir_contents` | array of `ContentsResponse` |  | DirContents contains directory listing when the path represents a directory |
| `file_contents` | `ContentsResponse` |  |  |

## ContentsResponse

ContentsResponse contains information about a repo's entry's (dir, file, symlink, submodule) metadata and content

| Field | Type | Required | Description |
|---|---|---|---|
| `_links` | `FileLinksResponse` |  |  |
| `content` | string |  | `content` is populated when `type` is `file`, otherwise null |
| `download_url` | string (uri) |  | DownloadURL is the direct download URL for this file |
| `encoding` | string |  | `encoding` is populated when `type` is `file`, otherwise null |
| `git_url` | string (uri) |  | GitURL is the Git API URL for this blob or tree |
| `html_url` | string (uri) |  | HTMLURL is the web URL for this file or directory |
| `last_author_date` | string (date-time) |  |  |
| `last_commit_message` | string |  | LastCommitMessage is the message of the last commit that affected this file |
| `last_commit_sha` | string |  | LastCommitSHA is the SHA of the last commit that affected this file |
| `last_committer_date` | string (date-time) |  |  |
| `lfs_oid` | string |  | LfsOid is the Git LFS object ID if this file is stored in LFS |
| `lfs_size` | integer (int64) |  | LfsSize is the file size if this file is stored in LFS |
| `mode` | string |  | `mode` is the Git file mode as an octal string, e.g. `100644` (regular), `100755` (executable), `120000` (symlink), `160000` (submodule) |
| `name` | string |  | Name is the file or directory name |
| `path` | string |  | Path is the full path to the file or directory |
| `sha` | string |  | SHA is the Git blob or tree SHA |
| `size` | integer (int64) |  | Size is the file size in bytes |
| `submodule_git_url` | string (uri) |  | `submodule_git_url` is populated when `type` is `submodule`, otherwise null |
| `target` | string |  | `target` is populated when `type` is `symlink`, otherwise null |
| `type` | string |  | `type` will be `file`, `dir`, `symlink`, or `submodule` |
| `url` | string (uri) |  | URL is the API URL for this file or directory |

## CreateAccessTokenOption

CreateAccessTokenOption options when create access token

| Field | Type | Required | Description |
|---|---|---|---|
| `name` | string | yes |  |
| `scopes` | array of string |  |  |

## CreateActionWorkflowDispatch

CreateActionWorkflowDispatch represents the payload for triggering a workflow dispatch event

| Field | Type | Required | Description |
|---|---|---|---|
| `inputs` | object |  |  |
| `ref` | string | yes |  |

## CreateBranchProtectionOption

CreateBranchProtectionOption options for creating a branch protection

| Field | Type | Required | Description |
|---|---|---|---|
| `approvals_whitelist_teams` | array of string |  |  |
| `approvals_whitelist_username` | array of string |  |  |
| `block_admin_merge_override` | boolean |  |  |
| `block_on_codeowner_reviews` | boolean |  |  |
| `block_on_official_review_requests` | boolean |  |  |
| `block_on_outdated_branch` | boolean |  |  |
| `block_on_rejected_reviews` | boolean |  |  |
| `branch_name` | string |  |  |
| `bypass_allowlist_teams` | array of string |  |  |
| `bypass_allowlist_usernames` | array of string |  |  |
| `dismiss_stale_approvals` | boolean |  |  |
| `enable_approvals_whitelist` | boolean |  |  |
| `enable_bypass_allowlist` | boolean |  |  |
| `enable_force_push` | boolean |  |  |
| `enable_force_push_allowlist` | boolean |  |  |
| `enable_merge_whitelist` | boolean |  |  |
| `enable_push` | boolean |  |  |
| `enable_push_whitelist` | boolean |  |  |
| `enable_status_check` | boolean |  |  |
| `force_push_allowlist_deploy_keys` | boolean |  |  |
| `force_push_allowlist_teams` | array of string |  |  |
| `force_push_allowlist_usernames` | array of string |  |  |
| `ignore_stale_approvals` | boolean |  |  |
| `merge_whitelist_teams` | array of string |  |  |
| `merge_whitelist_usernames` | array of string |  |  |
| `priority` | integer (int64) |  |  |
| `protected_file_patterns` | string |  |  |
| `push_whitelist_deploy_keys` | boolean |  |  |
| `push_whitelist_teams` | array of string |  |  |
| `push_whitelist_usernames` | array of string |  |  |
| `require_signed_commits` | boolean |  |  |
| `required_approvals` | integer (int64) |  |  |
| `rule_name` | string |  |  |
| `status_check_contexts` | array of string |  |  |
| `unprotected_file_patterns` | string |  |  |

## CreateBranchRepoOption

CreateBranchRepoOption options when creating a branch in a repository

| Field | Type | Required | Description |
|---|---|---|---|
| `new_branch_name` | string | yes | Name of the branch to create |
| `old_branch_name` | string |  | Name of the old branch to create from |
| `old_ref_name` | string |  | Name of the old branch/tag/commit to create from |

## CreateDeployKeyTokenOption

| Field | Type | Required | Description |
|---|---|---|---|
| `read_only` | boolean |  | Describe if the token has only read access or read/write |
| `title` | string | yes | Title of the token to add |

## CreateEmailOption

CreateEmailOption options when creating email addresses

| Field | Type | Required | Description |
|---|---|---|---|
| `emails` | array of string |  | email addresses to add |

## CreateFileOptions

CreateFileOptions options for creating a file
Note: `author` and `committer` are optional (if only one is given, it will be used for the other, otherwise the authenticated user will be used)

| Field | Type | Required | Description |
|---|---|---|---|
| `author` | `Identity` |  |  |
| `branch` | string |  | branch (optional) is the base branch for the changes. If not supplied, the default branch is used |
| `committer` | `Identity` |  |  |
| `content` | string | yes | content must be base64 encoded |
| `dates` | `CommitDateOptions` |  |  |
| `force_push` | boolean |  | force_push (optional) will do a force-push if the new branch already exists |
| `message` | string |  | message (optional) is the commit message of the changes. If not supplied, a default message will be used |
| `new_branch` | string |  | new_branch (optional) will make a new branch from base branch for the changes. If not supplied, the changes will be committed to the base branch |
| `signoff` | boolean |  | Add a Signed-off-by trailer by the committer at the end of the commit log message. |

## CreateForkOption

CreateForkOption options for creating a fork

| Field | Type | Required | Description |
|---|---|---|---|
| `name` | string |  | name of the forked repository |
| `organization` | string |  | organization name, if forking into an organization |

## CreateGPGKeyOption

CreateGPGKeyOption options create user GPG key

| Field | Type | Required | Description |
|---|---|---|---|
| `armored_public_key` | string | yes | An armored GPG key to add |
| `armored_signature` | string |  | An optional armored signature for the GPG key |

## CreateHookOption

CreateHookOption options when create a hook

| Field | Type | Required | Description |
|---|---|---|---|
| `active` | boolean |  | Whether the webhook should be active upon creation |
| `authorization_header` | string |  | Authorization header to include in webhook requests |
| `branch_filter` | string |  | Branch filter pattern to determine which branches trigger the webhook |
| `config` | `CreateHookOptionConfig` | yes |  |
| `events` | array of string |  | List of events that will trigger this webhook |
| `name` | string |  | Optional human-readable name for the webhook |
| `type` | string enum: dingtalk, discord, gitea, gogs, msteams, slack, telegram, feishu, wechatwork, packagist | yes | The type of the webhook to create |

## CreateHookOptionConfig

CreateHookOptionConfig has all config options in it
required are "content_type" and "url" Required

Type: object

## CreateIssueCommentOption

CreateIssueCommentOption options for creating a comment on an issue

| Field | Type | Required | Description |
|---|---|---|---|
| `body` | string | yes | Body is the comment text content |

## CreateIssueOption

CreateIssueOption options to create one issue

| Field | Type | Required | Description |
|---|---|---|---|
| `assignee` | string |  | deprecated |
| `assignees` | array of string |  |  |
| `body` | string |  |  |
| `closed` | boolean |  |  |
| `due_date` | string (date-time) |  |  |
| `labels` | array of integer (int64) |  | list of label ids |
| `milestone` | integer (int64) |  | milestone id |
| `projects` | array of integer (int64) |  | list of project ids |
| `ref` | string |  |  |
| `title` | string | yes |  |

## CreateKeyOption

| Field | Type | Required | Description |
|---|---|---|---|
| `key` | string | yes | An armored SSH key to add |
| `read_only` | boolean |  | Describe if the key has only read access or read/write |
| `title` | string | yes | Title of the key to add |

## CreateLabelOption

CreateLabelOption options for creating a label

| Field | Type | Required | Description |
|---|---|---|---|
| `color` | string | yes |  |
| `description` | string |  | Description provides additional context about the label's purpose |
| `exclusive` | boolean |  |  |
| `is_archived` | boolean |  |  |
| `name` | string | yes | Name is the display name for the new label |

## CreateMilestoneOption

CreateMilestoneOption options for creating a milestone

| Field | Type | Required | Description |
|---|---|---|---|
| `description` | string |  | Description provides details about the milestone |
| `due_on` | string (date-time) |  | Deadline is the due date for the milestone |
| `state` | allOf(`StateType`) |  | State indicates the initial state of the milestone |
| `title` | string |  | Title is the title of the new milestone |

## CreateOAuth2ApplicationOptions

CreateOAuth2ApplicationOptions holds options to create an oauth2 application

| Field | Type | Required | Description |
|---|---|---|---|
| `confidential_client` | boolean |  | Whether the client is confidential |
| `name` | string |  | The name of the OAuth2 application |
| `redirect_uris` | array of string |  | The list of allowed redirect URIs |
| `skip_secondary_authorization` | boolean |  | Whether to skip secondary authorization |

## CreateOrUpdateSecretOption

CreateOrUpdateSecretOption options when creating or updating secret

| Field | Type | Required | Description |
|---|---|---|---|
| `data` | string | yes | Data of the secret to update |
| `description` | string |  | Description of the secret to update |

## CreateOrgOption

CreateOrgOption options for creating an organization

| Field | Type | Required | Description |
|---|---|---|---|
| `description` | string |  | The description of the organization |
| `email` | string |  | The email address of the organization |
| `full_name` | string |  | The full display name of the organization |
| `location` | string |  | The location of the organization |
| `repo_admin_change_team_access` | boolean |  | Whether repository administrators can change team access |
| `username` | string | yes | username of the organization |
| `visibility` | allOf(`VisibilityString`) |  | possible values are `public` (default), `limited` or `private` |
| `website` | string |  | The website URL of the organization |

## CreateProjectColumnOption

CreateProjectColumnOption represents options for creating a project column

| Field | Type | Required | Description |
|---|---|---|---|
| `color` | string |  | Column color in 6-digit hex format, e.g. #FF0000 |
| `title` | string | yes |  |

## CreateProjectOption

CreateProjectOption represents options for creating a project

| Field | Type | Required | Description |
|---|---|---|---|
| `card_type` | string |  | Card type: "text_only" or "images_and_text" |
| `description` | string |  |  |
| `template_type` | string |  | Template type: "none", "basic_kanban" or "bug_triage" |
| `title` | string | yes |  |

## CreatePullRequestOption

CreatePullRequestOption options when creating a pull request

| Field | Type | Required | Description |
|---|---|---|---|
| `allow_maintainer_edit` | boolean |  | Whether maintainers can edit the pull request |
| `assignee` | string |  | The primary assignee username |
| `assignees` | array of string |  | The list of assignee usernames |
| `base` | string |  | The base branch for the pull request |
| `body` | string |  | The description body of the pull request |
| `due_date` | string (date-time) |  |  |
| `head` | string |  | The head branch for the pull request, it could be a branch name on the base repository or a form like `<username>:<branch>` which refers to the user's fork repository's branch. |
| `labels` | array of integer (int64) |  | The list of label IDs to assign to the pull request |
| `milestone` | integer (int64) |  | The milestone ID to assign to the pull request |
| `reviewers` | array of string |  | The list of reviewer usernames |
| `team_reviewers` | array of string |  | The list of team reviewer names |
| `title` | string |  | The title of the pull request |

## CreatePullReviewComment

CreatePullReviewComment represent a review comment for creation api

| Field | Type | Required | Description |
|---|---|---|---|
| `body` | string |  |  |
| `new_position` | integer (int64) |  | if comment to new file line or 0 |
| `old_position` | integer (int64) |  | if comment to old file line or 0 |
| `path` | string |  | the tree path |

## CreatePullReviewCommentReplyOptions

CreatePullReviewCommentReplyOptions are options to reply to a pull request review comment

| Field | Type | Required | Description |
|---|---|---|---|
| `body` | string |  |  |

## CreatePullReviewOptions

CreatePullReviewOptions are options to create a pull request review

| Field | Type | Required | Description |
|---|---|---|---|
| `body` | string |  |  |
| `comments` | array of `CreatePullReviewComment` |  |  |
| `commit_id` | string |  |  |
| `event` | `ReviewStateType` |  |  |

## CreatePushMirrorOption

| Field | Type | Required | Description |
|---|---|---|---|
| `interval` | string |  | The sync interval for automatic updates |
| `remote_address` | string |  | The remote repository URL to push to |
| `remote_password` | string |  | The password for authentication with the remote repository |
| `remote_username` | string |  | The username for authentication with the remote repository |
| `sync_on_commit` | boolean |  | Whether to sync on every commit |

## CreateReleaseOption

CreateReleaseOption options when creating a release

| Field | Type | Required | Description |
|---|---|---|---|
| `body` | string |  | The release notes or description |
| `draft` | boolean |  | Whether to create the release as a draft |
| `name` | string |  | The display title of the release |
| `prerelease` | boolean |  | Whether to mark the release as a prerelease |
| `tag_message` | string |  | The message for the git tag |
| `tag_name` | string | yes |  |
| `target_commitish` | string |  | The target commitish for the release |

## CreateRepoOption

CreateRepoOption options when creating repository

| Field | Type | Required | Description |
|---|---|---|---|
| `auto_init` | boolean |  | Whether the repository should be auto-initialized? |
| `default_branch` | string |  | DefaultBranch of the repository (used when initializes and in template) |
| `description` | string |  | Description of the repository to create |
| `gitignores` | string |  | Gitignores to use |
| `issue_labels` | string |  | Label-Set to use |
| `license` | string |  | License to use |
| `name` | string | yes | Name of the repository to create |
| `object_format_name` | allOf(`ObjectFormatName`) |  | ObjectFormatName of the underlying git repository, empty string for default (sha1) |
| `private` | boolean |  | Whether the repository is private |
| `readme` | string |  | Readme of the repository to create |
| `template` | boolean |  | Whether the repository is template |
| `trust_model` | string enum: default, collaborator, committer, collaboratorcommitter |  | TrustModel of the repository |

## CreateStatusOption

CreateStatusOption holds the information needed to create a new CommitStatus for a Commit

| Field | Type | Required | Description |
|---|---|---|---|
| `context` | string |  | Context is the unique context identifier for the status |
| `description` | string |  | Description provides a brief description of the status |
| `state` | allOf(`CommitStatusState`) |  | State represents the status state to set (pending, success, error, failure) |
| `target_url` | string (uri) |  | TargetURL is the URL to link to for more details |

## CreateTagOption

CreateTagOption options when creating a tag

| Field | Type | Required | Description |
|---|---|---|---|
| `message` | string |  | The message to associate with the tag |
| `tag_name` | string | yes | The name of the tag to create |
| `target` | string |  | The target commit SHA or branch name for the tag |

## CreateTagProtectionOption

CreateTagProtectionOption options for creating a tag protection

| Field | Type | Required | Description |
|---|---|---|---|
| `name_pattern` | string |  | The pattern to match tag names for protection |
| `whitelist_teams` | array of string |  | List of team names allowed to create/delete protected tags |
| `whitelist_usernames` | array of string |  | List of usernames allowed to create/delete protected tags |

## CreateTeamOption

CreateTeamOption options for creating a team

| Field | Type | Required | Description |
|---|---|---|---|
| `can_create_org_repo` | boolean |  | Whether the team can create repositories in the organization |
| `description` | string |  | The description of the team |
| `includes_all_repositories` | boolean |  | Whether the team has access to all repositories in the organization |
| `name` | string | yes |  |
| `permission` | allOf(`RepoWritePermission`) |  | All units have this permission (read/write/admin) |
| `units` | array of string |  | Deprecated: This variable should be replaced by UnitsMap and will be dropped in later versions. |
| `units_map` | object |  |  |
| `visibility` | allOf(`TeamVisibility`) |  | Team visibility within the organization. Defaults to "private". |

## CreateUserOption

CreateUserOption create user options

| Field | Type | Required | Description |
|---|---|---|---|
| `created_at` | string (date-time) |  | For explicitly setting the user creation timestamp. Useful when users are migrated from other systems. When omitted, the user's creation timestamp will be set to "now". |
| `email` | string | yes |  |
| `full_name` | string |  | The full display name of the user |
| `login_name` | string |  | identifier of the user, provided by the external authenticator (if configured) |
| `must_change_password` | boolean |  | Whether the user must change password on first login |
| `password` | string |  | The plain text password for the user |
| `restricted` | boolean |  | Whether the user has restricted access privileges |
| `send_notify` | boolean |  | Whether to send welcome notification email to the user |
| `source_id` | integer (int64) |  | The authentication source ID to associate with the user |
| `username` | string | yes | username of the user |
| `visibility` | allOf(`VisibilityString`) |  | User visibility level: public, limited, or private |

## CreateVariableOption

CreateVariableOption the option when creating variable

| Field | Type | Required | Description |
|---|---|---|---|
| `description` | string |  | Description of the variable to create |
| `value` | string | yes | Value of the variable to create |

## CreateWikiPageOptions

CreateWikiPageOptions form for creating wiki

| Field | Type | Required | Description |
|---|---|---|---|
| `content_base64` | string |  | content must be base64 encoded |
| `message` | string |  | optional commit message summarizing the change |
| `title` | string |  | page title. leave empty to keep unchanged |

## Cron

Cron represents a Cron task

| Field | Type | Required | Description |
|---|---|---|---|
| `exec_times` | integer (int64) |  | The total number of times this cron task has been executed |
| `name` | string |  | The name of the cron task |
| `next` | string (date-time) |  | The next scheduled execution time |
| `prev` | string (date-time) |  | The previous execution time |
| `schedule` | string |  | The cron schedule expression (e.g., "0 0 * * *") |

## CurrentAccessToken

| Field | Type | Required | Description |
|---|---|---|---|
| `created_at` | string (date-time) |  | The timestamp when the token was created |
| `id` | integer (int64) |  | The unique identifier of the access token |
| `last_used_at` | string (date-time) |  | The timestamp when the token was last used |
| `name` | string |  | The name of the access token |
| `scopes` | array of string |  | The scopes granted to this access token |
| `user` | `UserMeta` |  |  |

## DeleteEmailOption

DeleteEmailOption options when deleting email addresses

| Field | Type | Required | Description |
|---|---|---|---|
| `emails` | array of string |  | email addresses to delete |

## DeleteFileOptions

DeleteFileOptions options for deleting a file
Note: `author` and `committer` are optional (if only one is given, it will be used for the other, otherwise the authenticated user will be used)

| Field | Type | Required | Description |
|---|---|---|---|
| `author` | `Identity` |  |  |
| `branch` | string |  | branch (optional) is the base branch for the changes. If not supplied, the default branch is used |
| `committer` | `Identity` |  |  |
| `dates` | `CommitDateOptions` |  |  |
| `force_push` | boolean |  | force_push (optional) will do a force-push if the new branch already exists |
| `message` | string |  | message (optional) is the commit message of the changes. If not supplied, a default message will be used |
| `new_branch` | string |  | new_branch (optional) will make a new branch from base branch for the changes. If not supplied, the changes will be committed to the base branch |
| `sha` | string | yes | the blob ID (SHA) for the file to delete |
| `signoff` | boolean |  | Add a Signed-off-by trailer by the committer at the end of the commit log message. |

## DeployKey

| Field | Type | Required | Description |
|---|---|---|---|
| `created_at` | string (date-time) |  | Created is the time when the deploy-key was added |
| `fingerprint` | string |  | Fingerprint is the key's fingerprint |
| `id` | integer (int64) |  | ID is the unique identifier for the deploy-key |
| `key` | string |  | Key contains the actual SSH key content |
| `key_id` | integer (int64) |  | KeyID is the associated public key ID |
| `key_type` | string enum: ssh, token |  | Type tells whether the key authenticates over SSH or with a token over HTTPS |
| `read_only` | boolean |  | ReadOnly indicates if the key has read-only access |
| `repository` | `Repository` |  |  |
| `title` | string |  | Title is the human-readable name for the key |
| `token` | string |  | Token is the plaintext token of an HTTPS key, only returned when it is created |
| `url` | string (uri) |  | URL is the API URL for this deploy-key |

## DismissPullReviewOptions

DismissPullReviewOptions are options to dismiss a pull request review

| Field | Type | Required | Description |
|---|---|---|---|
| `message` | string |  |  |
| `priors` | boolean |  |  |

## EditActionRunnerOption

| Field | Type | Required | Description |
|---|---|---|---|
| `disabled` | boolean | yes |  |

## EditAttachmentOptions

EditAttachmentOptions options for editing attachments

| Field | Type | Required | Description |
|---|---|---|---|
| `name` | string |  | Name is the new filename for the attachment |

## EditBranchProtectionOption

EditBranchProtectionOption options for editing a branch protection

| Field | Type | Required | Description |
|---|---|---|---|
| `approvals_whitelist_teams` | array of string |  |  |
| `approvals_whitelist_username` | array of string |  |  |
| `block_admin_merge_override` | boolean |  |  |
| `block_on_codeowner_reviews` | boolean |  |  |
| `block_on_official_review_requests` | boolean |  |  |
| `block_on_outdated_branch` | boolean |  |  |
| `block_on_rejected_reviews` | boolean |  |  |
| `bypass_allowlist_teams` | array of string |  |  |
| `bypass_allowlist_usernames` | array of string |  |  |
| `dismiss_stale_approvals` | boolean |  |  |
| `enable_approvals_whitelist` | boolean |  |  |
| `enable_bypass_allowlist` | boolean |  |  |
| `enable_force_push` | boolean |  |  |
| `enable_force_push_allowlist` | boolean |  |  |
| `enable_merge_whitelist` | boolean |  |  |
| `enable_push` | boolean |  |  |
| `enable_push_whitelist` | boolean |  |  |
| `enable_status_check` | boolean |  |  |
| `force_push_allowlist_deploy_keys` | boolean |  |  |
| `force_push_allowlist_teams` | array of string |  |  |
| `force_push_allowlist_usernames` | array of string |  |  |
| `ignore_stale_approvals` | boolean |  |  |
| `merge_whitelist_teams` | array of string |  |  |
| `merge_whitelist_usernames` | array of string |  |  |
| `priority` | integer (int64) |  |  |
| `protected_file_patterns` | string |  |  |
| `push_whitelist_deploy_keys` | boolean |  |  |
| `push_whitelist_teams` | array of string |  |  |
| `push_whitelist_usernames` | array of string |  |  |
| `require_signed_commits` | boolean |  |  |
| `required_approvals` | integer (int64) |  |  |
| `status_check_contexts` | array of string |  |  |
| `unprotected_file_patterns` | string |  |  |

## EditDeadlineOption

EditDeadlineOption options for creating a deadline

| Field | Type | Required | Description |
|---|---|---|---|
| `due_date` | string (date-time) | yes |  |

## EditGitHookOption

EditGitHookOption options when modifying one Git hook

| Field | Type | Required | Description |
|---|---|---|---|
| `content` | string |  | Content is the new script content for the hook |

## EditHookOption

EditHookOption options when modify one hook

| Field | Type | Required | Description |
|---|---|---|---|
| `active` | boolean |  | Whether the webhook is active and will be triggered |
| `authorization_header` | string |  | Authorization header to include in webhook requests |
| `branch_filter` | string |  | Branch filter pattern to determine which branches trigger the webhook |
| `config` | object |  | Configuration settings for the webhook |
| `events` | array of string |  | List of events that trigger this webhook |
| `name` | string |  | Optional human-readable name |

## EditIssueCommentOption

EditIssueCommentOption options for editing a comment

| Field | Type | Required | Description |
|---|---|---|---|
| `body` | string | yes | Body is the updated comment text content |

## EditIssueOption

EditIssueOption options for editing an issue

| Field | Type | Required | Description |
|---|---|---|---|
| `assignee` | string |  | deprecated |
| `assignees` | array of string |  |  |
| `body` | string |  |  |
| `content_version` | integer (int64) |  | The current version of the issue content to detect conflicts during editing |
| `due_date` | string (date-time) |  |  |
| `milestone` | integer (int64) |  |  |
| `projects` | array of integer (int64) |  | list of project ids to set (replaces existing projects) |
| `ref` | string |  |  |
| `state` | string |  |  |
| `title` | string |  |  |
| `unset_due_date` | boolean |  |  |

## EditLabelOption

EditLabelOption options for editing a label

| Field | Type | Required | Description |
|---|---|---|---|
| `color` | string |  |  |
| `description` | string |  | Description provides additional context about the label's purpose |
| `exclusive` | boolean |  |  |
| `is_archived` | boolean |  |  |
| `name` | string |  | Name is the new display name for the label |

## EditMilestoneOption

EditMilestoneOption options for editing a milestone

| Field | Type | Required | Description |
|---|---|---|---|
| `description` | string |  | Description provides updated details about the milestone |
| `due_on` | string (date-time) |  | Deadline is the due date for the milestone, use null or empty string to remove the deadline |
| `state` | allOf(`StateType`) |  | State indicates the updated state of the milestone |
| `title` | string |  | Title is the updated title of the milestone |

## EditOrgOption

EditOrgOption options for editing an organization

| Field | Type | Required | Description |
|---|---|---|---|
| `description` | string |  | The description of the organization |
| `email` | string |  | The email address of the organization; use empty string to clear |
| `full_name` | string |  | The full display name of the organization |
| `location` | string |  | The location of the organization |
| `repo_admin_change_team_access` | boolean |  | Whether repository administrators can change team access |
| `visibility` | allOf(`VisibilityString`) |  | possible values are `public`, `limited` or `private` |
| `website` | string |  | The website URL of the organization |

## EditProjectColumnOption

EditProjectColumnOption represents options for editing a project column

| Field | Type | Required | Description |
|---|---|---|---|
| `color` | string |  | Column color in 6-digit hex format, e.g. #FF0000 |
| `sorting` | integer (int64) |  | Position of the column within the project, between -128 and 127 |
| `title` | string |  |  |

## EditProjectOption

EditProjectOption represents options for editing a project

| Field | Type | Required | Description |
|---|---|---|---|
| `card_type` | string |  | Card type: "text_only" or "images_and_text" |
| `description` | string |  |  |
| `state` | `StateType` |  |  |
| `title` | string |  |  |

## EditPullRequestOption

EditPullRequestOption options when modify pull request

| Field | Type | Required | Description |
|---|---|---|---|
| `allow_maintainer_edit` | boolean |  | Whether to allow maintainer edits |
| `assignee` | string |  | The new primary assignee username |
| `assignees` | array of string |  | The new list of assignee usernames |
| `base` | string |  | The new base branch for the pull request |
| `body` | string |  | The new description body for the pull request |
| `content_version` | integer (int64) |  | The current version of the pull request content to detect conflicts during editing |
| `due_date` | string (date-time) |  |  |
| `labels` | array of integer (int64) |  | The new list of label IDs for the pull request |
| `milestone` | integer (int64) |  | The new milestone ID for the pull request |
| `state` | string |  | The new state for the pull request |
| `title` | string |  | The new title for the pull request |
| `unset_due_date` | boolean |  | Whether to remove the current deadline |

## EditReactionOption

EditReactionOption contain the reaction type

| Field | Type | Required | Description |
|---|---|---|---|
| `content` | string |  | The reaction content (e.g., emoji or reaction type) |

## EditReleaseOption

EditReleaseOption options when editing a release

| Field | Type | Required | Description |
|---|---|---|---|
| `body` | string |  | The new release notes or description |
| `draft` | boolean |  | Whether to change the draft status |
| `name` | string |  | The new display title of the release |
| `prerelease` | boolean |  | Whether to change the prerelease status |
| `tag_name` | string |  | The new name of the git tag |
| `target_commitish` | string |  | The new target commitish for the release |

## EditRepoOption

EditRepoOption options when editing a repository's properties

| Field | Type | Required | Description |
|---|---|---|---|
| `allow_fast_forward_only_merge` | boolean |  | either `true` to allow fast-forward-only merging pull requests, or `false` to prevent fast-forward-only merging. |
| `allow_manual_merge` | boolean |  | either `true` to allow mark pr as merged manually, or `false` to prevent it. |
| `allow_merge_commits` | boolean |  | either `true` to allow merging pull requests with a merge commit, or `false` to prevent merging pull requests with merge commits. |
| `allow_merge_update` | boolean |  | either `true` to allow updating pull request branch by merge, or `false` to prevent it. |
| `allow_rebase` | boolean |  | either `true` to allow rebase-merging pull requests, or `false` to prevent rebase-merging. |
| `allow_rebase_explicit` | boolean |  | either `true` to allow rebase with explicit merge commits (--no-ff), or `false` to prevent rebase with explicit merge commits. |
| `allow_rebase_update` | boolean |  | either `true` to allow updating pull request branch by rebase, or `false` to prevent it. |
| `allow_squash_merge` | boolean |  | either `true` to allow squash-merging pull requests, or `false` to prevent squash-merging. |
| `archived` | boolean |  | set to `true` to archive this repository. |
| `autodetect_manual_merge` | boolean |  | either `true` to enable AutodetectManualMerge, or `false` to prevent it. Note: In some special cases, misjudgments can occur. |
| `default_allow_maintainer_edit` | boolean |  | set to `true` to allow edits from maintainers by default |
| `default_branch` | string |  | sets the default branch for this repository. |
| `default_delete_branch_after_merge` | boolean |  | set to `true` to delete pr branch after merge by default |
| `default_merge_style` | string |  | set to a merge style to be used by this repository: "merge", "rebase", "rebase-merge", "squash", or "fast-forward-only". |
| `default_update_style` | string |  | set to an update style to be used by this repository: "merge" or "rebase". |
| `description` | string |  | a short description of the repository. |
| `enable_prune` | boolean |  | enable prune - remove obsolete remote-tracking references when mirroring |
| `external_tracker` | `ExternalTracker` |  |  |
| `external_wiki` | `ExternalWiki` |  |  |
| `has_actions` | boolean |  | either `true` to enable actions unit, or `false` to disable them. |
| `has_code` | boolean |  | either `true` to enable code for this repository or `false` to disable it. |
| `has_issues` | boolean |  | either `true` to enable issues for this repository or `false` to disable them. |
| `has_packages` | boolean |  | either `true` to enable packages unit, or `false` to disable them. |
| `has_projects` | boolean |  | either `true` to enable project unit, or `false` to disable them. |
| `has_pull_requests` | boolean |  | either `true` to allow pull requests, or `false` to prevent pull request. |
| `has_releases` | boolean |  | either `true` to enable releases unit, or `false` to disable them. |
| `has_wiki` | boolean |  | either `true` to enable the wiki for this repository or `false` to disable it. |
| `ignore_whitespace_conflicts` | boolean |  | either `true` to ignore whitespace for conflicts, or `false` to not ignore whitespace. |
| `internal_tracker` | `InternalTracker` |  |  |
| `mirror_interval` | string |  | set to a string like `8h30m0s` to set the mirror interval time |
| `mirror_password` | string |  | authentication password for the remote repository (mirrors) |
| `mirror_token` | string |  | authentication token for the remote repository (mirrors) |
| `mirror_username` | string |  | authentication username for the remote repository (mirrors) |
| `name` | string |  | name of the repository |
| `private` | boolean |  | either `true` to make the repository private or `false` to make it public. Note: you will get a 422 error if the organization restricts changing repository visibility to organization owners and a non-owner tries to change the value of private. |
| `projects_mode` | string |  | `repo` to only allow repo-level projects, `owner` to only allow owner projects, `all` to allow both. |
| `template` | boolean |  | either `true` to make this repository a template or `false` to make it a normal repository |
| `website` | string |  | a URL with more information about the repository. |

## EditTagProtectionOption

EditTagProtectionOption options for editing a tag protection

| Field | Type | Required | Description |
|---|---|---|---|
| `name_pattern` | string |  | The pattern to match tag names for protection |
| `whitelist_teams` | array of string |  | List of team names allowed to create/delete protected tags |
| `whitelist_usernames` | array of string |  | List of usernames allowed to create/delete protected tags |

## EditTeamOption

EditTeamOption options for editing a team

| Field | Type | Required | Description |
|---|---|---|---|
| `can_create_org_repo` | boolean |  | Whether the team can create repositories in the organization |
| `description` | string |  | The description of the team |
| `includes_all_repositories` | boolean |  | Whether the team has access to all repositories in the organization |
| `name` | string | yes |  |
| `permission` | allOf(`RepoWritePermission`) |  | All units have this permission (read/write/admin) |
| `units` | array of string |  | Deprecated: This variable should be replaced by UnitsMap and will be dropped in later versions. |
| `units_map` | object |  |  |
| `visibility` | allOf(`TeamVisibility`) |  | Team visibility within the organization. When omitted, visibility is left unchanged. |

## EditUserOption

EditUserOption edit user options

| Field | Type | Required | Description |
|---|---|---|---|
| `active` | boolean |  | Whether the user account is active |
| `admin` | boolean |  | Whether the user has administrator privileges |
| `allow_create_organization` | boolean |  | Whether the user can create organizations |
| `allow_git_hook` | boolean |  | Whether the user can use Git hooks |
| `allow_import_local` | boolean |  | Whether the user can import local repositories |
| `description` | string |  | The user's personal description or bio |
| `email` | string (email) |  | The email address of the user |
| `full_name` | string |  | The full display name of the user |
| `location` | string |  | The user's location or address |
| `login_name` | string |  | identifier of the user, provided by the external authenticator (if configured) |
| `max_repo_creation` | integer (int64) |  | Maximum number of repositories the user can create |
| `must_change_password` | boolean |  | Whether the user must change password on next login |
| `password` | string |  | The plain text password for the user |
| `prohibit_login` | boolean |  | Whether the user is prohibited from logging in |
| `restricted` | boolean |  | Whether the user has restricted access privileges |
| `source_id` | integer (int64) | yes | The authentication source ID to associate with the user |
| `type` | allOf(`UserTypeString`) |  | The user type |
| `visibility` | allOf(`VisibilityString`) |  | User visibility level: public, limited, or private |
| `website` | string |  | The user's personal website URL |

## Email

Email an email address belonging to a user

| Field | Type | Required | Description |
|---|---|---|---|
| `email` | string (email) |  | The email address |
| `primary` | boolean |  | Whether this is the primary email address |
| `user_id` | integer (int64) |  | The unique identifier of the user who owns this email |
| `username` | string |  | username of the user |
| `verified` | boolean |  | Whether the email address has been verified |

## ExternalTracker

ExternalTracker represents settings for external tracker

| Field | Type | Required | Description |
|---|---|---|---|
| `external_tracker_format` | string |  | External Issue Tracker URL Format. Use the placeholders {user}, {repo} and {index} for the username, repository name and issue index. |
| `external_tracker_regexp_pattern` | string |  | External Issue Tracker issue regular expression |
| `external_tracker_style` | string |  | External Issue Tracker Number Format, either `numeric`, `alphanumeric`, or `regexp` |
| `external_tracker_url` | string (uri) |  | URL of external issue tracker. |

## ExternalWiki

ExternalWiki represents setting for external wiki

| Field | Type | Required | Description |
|---|---|---|---|
| `external_wiki_url` | string (uri) |  | URL of external wiki. |

## FileCommitResponse

| Field | Type | Required | Description |
|---|---|---|---|
| `author` | `CommitUser` |  |  |
| `committer` | `CommitUser` |  |  |
| `created` | string (date-time) |  | Created is the time when the commit was created |
| `html_url` | string (uri) |  | HTMLURL is the web URL for viewing this commit |
| `message` | string |  | Message is the commit message |
| `parents` | array of `CommitMeta` |  | Parents contains parent commit metadata |
| `sha` | string |  | SHA is the commit SHA hash |
| `tree` | `CommitMeta` |  |  |
| `url` | string (uri) |  | URL is the API URL for the commit |

## FileDeleteResponse

FileDeleteResponse contains information about a repo's file that was deleted

| Field | Type | Required | Description |
|---|---|---|---|
| `commit` | `FileCommitResponse` |  |  |
| `content` | object |  | Content is always null for delete operations |
| `verification` | `PayloadCommitVerification` |  |  |

## FileLinksResponse

FileLinksResponse contains the links for a repo's file

| Field | Type | Required | Description |
|---|---|---|---|
| `git` | string |  | GitURL is the Git API URL for this file |
| `html` | string |  | HTMLURL is the web URL for this file |
| `self` | string |  | Self is the API URL for this file |

## FileResponse

FileResponse contains information about a repo's file

| Field | Type | Required | Description |
|---|---|---|---|
| `commit` | `FileCommitResponse` |  |  |
| `content` | `ContentsResponse` |  |  |
| `verification` | `PayloadCommitVerification` |  |  |

## FilesResponse

FilesResponse contains information about multiple files from a repo

| Field | Type | Required | Description |
|---|---|---|---|
| `commit` | `FileCommitResponse` |  |  |
| `files` | array of `ContentsResponse` |  | Files contains the list of file contents and metadata |
| `verification` | `PayloadCommitVerification` |  |  |

## GPGKey

GPGKey a user GPG key to sign commit and tag in repository

| Field | Type | Required | Description |
|---|---|---|---|
| `can_certify` | boolean |  | Whether the key can be used for certification |
| `can_encrypt_comms` | boolean |  | Whether the key can be used for encrypting communications |
| `can_encrypt_storage` | boolean |  | Whether the key can be used for encrypting storage |
| `can_sign` | boolean |  | Whether the key can be used for signing |
| `created_at` | string (date-time) |  | The date and time when the GPG key was created |
| `emails` | array of `GPGKeyEmail` |  | List of email addresses associated with this GPG key |
| `expires_at` | string (date-time) |  | The date and time when the GPG key expires |
| `id` | integer (int64) |  | The unique identifier of the GPG key |
| `key_id` | string |  | The key ID of the GPG key |
| `primary_key_id` | string |  | The primary key ID of the GPG key |
| `public_key` | string |  | The public key content in armored format |
| `subkeys` | array of `GPGKey` |  | List of subkeys of this GPG key |
| `verified` | boolean |  | Whether the GPG key has been verified |

## GPGKeyEmail

GPGKeyEmail an email attached to a GPGKey

| Field | Type | Required | Description |
|---|---|---|---|
| `email` | string |  | The email address associated with the GPG key |
| `verified` | boolean |  | Whether the email address has been verified |

## GeneralAPISettings

GeneralAPISettings contains global api settings exposed by it

| Field | Type | Required | Description |
|---|---|---|---|
| `default_git_trees_per_page` | integer (int64) |  | DefaultGitTreesPerPage is the default number of Git tree items per page |
| `default_max_blob_size` | integer (int64) |  | DefaultMaxBlobSize is the default maximum blob size for API responses |
| `default_max_response_size` | integer (int64) |  | DefaultMaxResponseSize is the default maximum response size |
| `default_paging_num` | integer (int64) |  | DefaultPagingNum is the default number of items per page |
| `max_response_items` | integer (int64) |  | MaxResponseItems is the maximum number of items returned in API responses |

## GeneralAttachmentSettings

GeneralAttachmentSettings contains global Attachment settings exposed by API

| Field | Type | Required | Description |
|---|---|---|---|
| `allowed_types` | string |  | AllowedTypes contains the allowed file types for attachments |
| `enabled` | boolean |  | Enabled indicates if file attachments are enabled |
| `max_files` | integer (int64) |  | MaxFiles is the maximum number of files per attachment |
| `max_size` | integer (int64) |  | MaxSize is the maximum size for individual attachments |

## GeneralRepoSettings

GeneralRepoSettings contains global repository settings exposed by API

| Field | Type | Required | Description |
|---|---|---|---|
| `http_git_disabled` | boolean |  | HTTPGitDisabled indicates if HTTP Git operations are disabled |
| `lfs_disabled` | boolean |  | LFSDisabled indicates if Git LFS support is disabled |
| `migrations_disabled` | boolean |  | MigrationsDisabled indicates if repository migrations are disabled |
| `mirrors_disabled` | boolean |  | MirrorsDisabled indicates if repository mirroring is disabled |
| `stars_disabled` | boolean |  | StarsDisabled indicates if repository starring is disabled |
| `time_tracking_disabled` | boolean |  | TimeTrackingDisabled indicates if time tracking is disabled |

## GeneralUISettings

GeneralUISettings contains global ui settings exposed by API

| Field | Type | Required | Description |
|---|---|---|---|
| `allowed_reactions` | array of string |  | AllowedReactions contains the list of allowed emoji reactions |
| `custom_emojis` | array of string |  | CustomEmojis contains the list of custom emojis |
| `default_theme` | string |  | DefaultTheme is the default UI theme |

## GenerateRepoOption

GenerateRepoOption options when creating a repository using a template

| Field | Type | Required | Description |
|---|---|---|---|
| `avatar` | boolean |  | include avatar of the template repo |
| `default_branch` | string |  | Default branch of the new repository |
| `description` | string |  | Description of the repository to create |
| `git_content` | boolean |  | include git content of default branch in template repo |
| `git_hooks` | boolean |  | include git hooks in template repo |
| `labels` | boolean |  | include labels in template repo |
| `name` | string | yes |  |
| `owner` | string | yes | the organization's name or individual user's name who will own the new repository |
| `private` | boolean |  | Whether the repository is private |
| `protected_branch` | boolean |  | include protected branches in template repo |
| `topics` | boolean |  | include topics in template repo |
| `webhooks` | boolean |  | include webhooks in template repo |

## GetFilesOptions

GetFilesOptions options for retrieving metadate and content of multiple files

| Field | Type | Required | Description |
|---|---|---|---|
| `files` | array of string |  | Files is the list of file paths to retrieve |

## GitBlobResponse

GitBlobResponse represents a git blob

| Field | Type | Required | Description |
|---|---|---|---|
| `content` | string |  | The content of the git blob (may be base64 encoded) |
| `encoding` | string |  | The encoding used for the content (e.g., "base64") |
| `lfs_oid` | string |  | The LFS object ID if this blob is stored in LFS |
| `lfs_size` | integer (int64) |  | The size of the LFS object if this blob is stored in LFS |
| `sha` | string |  | The SHA hash of the git blob |
| `size` | integer (int64) |  | The size of the git blob in bytes |
| `url` | string (uri) |  | The URL to access this git blob |

## GitEntry

GitEntry represents a git tree

| Field | Type | Required | Description |
|---|---|---|---|
| `mode` | string |  | Mode is the file mode (permissions) |
| `path` | string |  | Path is the file or directory path |
| `sha` | string |  | SHA is the Git object SHA |
| `size` | integer (int64) |  | Size is the file size in bytes |
| `type` | string |  | Type indicates if this is a file, directory, or symlink |
| `url` | string (uri) |  | URL is the API URL for this tree entry |

## GitHook

GitHook represents a Git repository hook

| Field | Type | Required | Description |
|---|---|---|---|
| `content` | string |  | Content contains the script content of the hook |
| `is_active` | boolean |  | IsActive indicates if the hook is active |
| `name` | string |  | Name is the name of the Git hook |

## GitObject

| Field | Type | Required | Description |
|---|---|---|---|
| `sha` | string |  | The SHA hash of the Git object |
| `type` | string |  | The type of the Git object (e.g., commit, tag, tree, blob) |
| `url` | string (uri) |  | The URL to access this Git object |

## GitTreeResponse

GitTreeResponse returns a git tree

| Field | Type | Required | Description |
|---|---|---|---|
| `page` | integer (int64) |  | Page is the current page number for pagination |
| `sha` | string |  | SHA is the tree object SHA |
| `total_count` | integer (int64) |  | TotalCount is the total number of entries in the tree |
| `tree` | array of `GitEntry` |  | Entries contains the tree entries (files and directories) |
| `truncated` | boolean |  | Truncated indicates if the response was truncated due to size |
| `url` | string (uri) |  | URL is the API URL for this tree |

## GitignoreTemplateInfo

GitignoreTemplateInfo name and text of a gitignore template

| Field | Type | Required | Description |
|---|---|---|---|
| `name` | string |  | Name is the name of the gitignore template |
| `source` | string |  | Source contains the content of the gitignore template |

## Hook

Hook a hook is a web hook when one repository changed

| Field | Type | Required | Description |
|---|---|---|---|
| `active` | boolean |  | Whether the webhook is active and will be triggered |
| `authorization_header` | string |  | Authorization header to include in webhook requests |
| `branch_filter` | string |  | Branch filter pattern to determine which branches trigger the webhook |
| `config` | object |  | Configuration settings for the webhook |
| `created_at` | string (date-time) |  | The date and time when the webhook was created |
| `events` | array of string |  | List of events that trigger this webhook |
| `id` | integer (int64) |  | The unique identifier of the webhook |
| `name` | string |  | Optional human-readable name for the webhook |
| `type` | string |  | The type of the webhook (e.g., gitea, slack, discord) |
| `updated_at` | string (date-time) |  | The date and time when the webhook was last updated |

## Identity

Identity for a person's identity like an author or committer

| Field | Type | Required | Description |
|---|---|---|---|
| `email` | string (email) |  | Email is the person's email address |
| `name` | string |  | Name is the person's name |

## InternalTracker

InternalTracker represents settings for internal tracker

| Field | Type | Required | Description |
|---|---|---|---|
| `allow_only_contributors_to_track_time` | boolean |  | Let only contributors track time (Built-in issue tracker) |
| `enable_issue_dependencies` | boolean |  | Enable dependencies for issues and pull requests (Built-in issue tracker) |
| `enable_time_tracker` | boolean |  | Enable time tracking (Built-in issue tracker) |

## Issue

Issue represents an issue in a repository

| Field | Type | Required | Description |
|---|---|---|---|
| `assets` | array of `Attachment` |  |  |
| `assignee` | `User` |  |  |
| `assignees` | array of `User` |  |  |
| `body` | string |  |  |
| `closed_at` | string (date-time) |  |  |
| `comments` | integer (int64) |  |  |
| `content_version` | integer (int64) |  | The version of the issue content for optimistic locking |
| `created_at` | string (date-time) |  |  |
| `due_date` | string (date-time) |  |  |
| `html_url` | string (uri) |  |  |
| `id` | integer (int64) |  |  |
| `is_locked` | boolean |  |  |
| `labels` | array of `Label` |  |  |
| `milestone` | `Milestone` |  |  |
| `number` | integer (int64) |  |  |
| `original_author` | string |  |  |
| `original_author_id` | integer (int64) |  |  |
| `pin_order` | integer (int64) |  |  |
| `projects` | array of `Project` |  |  |
| `pull_request` | `PullRequestMeta` |  |  |
| `ref` | string |  |  |
| `repository` | `RepositoryMeta` |  |  |
| `state` | `StateType` |  |  |
| `time_estimate` | integer (int64) |  |  |
| `title` | string |  |  |
| `updated_at` | string (date-time) |  |  |
| `url` | string (uri) |  |  |
| `user` | `User` |  |  |

## IssueAssigneesOption

IssueAssigneesOption options for adding/removing issue assignees

| Field | Type | Required | Description |
|---|---|---|---|
| `assignees` | array of string |  |  |

## IssueConfig

| Field | Type | Required | Description |
|---|---|---|---|
| `blank_issues_enabled` | boolean |  |  |
| `contact_links` | array of `IssueConfigContactLink` |  |  |

## IssueConfigContactLink

| Field | Type | Required | Description |
|---|---|---|---|
| `about` | string |  |  |
| `name` | string |  |  |
| `url` | string (uri) |  |  |

## IssueConfigValidation

| Field | Type | Required | Description |
|---|---|---|---|
| `message` | string |  |  |
| `valid` | boolean |  |  |

## IssueDeadline

IssueDeadline represents an issue deadline

| Field | Type | Required | Description |
|---|---|---|---|
| `due_date` | string (date-time) |  |  |

## IssueFormField

IssueFormField represents a form field

| Field | Type | Required | Description |
|---|---|---|---|
| `attributes` | object |  |  |
| `id` | string |  |  |
| `type` | string enum: markdown, textarea, input, dropdown, checkboxes |  |  |
| `validations` | object |  |  |
| `visible` | array of string enum: form, content |  |  |

## IssueLabelsOption

IssueLabelsOption a collection of labels

| Field | Type | Required | Description |
|---|---|---|---|
| `labels` | array of |  | Labels can be a list of integers representing label IDs or a list of strings representing label names. If a repository label and an organization label share a name, the repository label is used. |

## IssueMeta

IssueMeta basic issue information

| Field | Type | Required | Description |
|---|---|---|---|
| `index` | integer (int64) |  |  |
| `owner` | string |  | owner of the issue's repo |
| `repo` | string |  |  |

## IssueTemplate

IssueTemplate represents an issue template for a repository

| Field | Type | Required | Description |
|---|---|---|---|
| `about` | string |  |  |
| `assignees` | `IssueTemplateStringSlice` |  |  |
| `body` | array of `IssueFormField` |  |  |
| `content` | string |  |  |
| `file_name` | string |  |  |
| `labels` | `IssueTemplateStringSlice` |  |  |
| `name` | string |  |  |
| `ref` | string |  |  |
| `title` | string |  |  |

## IssueTemplateStringSlice

Type: array of string

## Label

Label a label to an issue or a pr

| Field | Type | Required | Description |
|---|---|---|---|
| `color` | string |  |  |
| `description` | string |  | Description provides additional context about the label's purpose |
| `exclusive` | boolean |  |  |
| `id` | integer (int64) |  | ID is the unique identifier for the label |
| `is_archived` | boolean |  |  |
| `name` | string |  | Name is the display name of the label |
| `url` | string (uri) |  | URL is the API endpoint for accessing this label |

## LabelTemplate

LabelTemplate info of a Label template

| Field | Type | Required | Description |
|---|---|---|---|
| `color` | string |  |  |
| `description` | string |  | Description provides additional context about the label template's purpose |
| `exclusive` | boolean |  |  |
| `name` | string |  | Name is the display name of the label template |

## LicenseTemplateInfo

LicensesInfo contains information about a License

| Field | Type | Required | Description |
|---|---|---|---|
| `body` | string |  | Body contains the full text of the license |
| `implementation` | string |  | Implementation contains license implementation details |
| `key` | string |  | Key is the unique identifier for the license template |
| `name` | string |  | Name is the display name of the license |
| `url` | string (uri) |  | URL is the reference URL for the license |

## LicensesTemplateListEntry

LicensesListEntry is used for the API

| Field | Type | Required | Description |
|---|---|---|---|
| `key` | string |  | Key is the unique identifier for the license template |
| `name` | string |  | Name is the display name of the license |
| `url` | string (uri) |  | URL is the reference URL for the license |

## LockIssueOption

LockIssueOption options to lock an issue

| Field | Type | Required | Description |
|---|---|---|---|
| `lock_reason` | string |  |  |

## MarkdownOption

MarkdownOption markdown options

| Field | Type | Required | Description |
|---|---|---|---|
| `Context` | string |  | URL path for rendering issue, media and file links Expected format: /subpath/{user}/{repo}/src/{branch, commit, tag}/{identifier/path}/{file/dir} |
| `Mode` | string |  | Mode to render (markdown, comment, wiki, file) |
| `Text` | string |  | Text markdown to render |
| `Wiki` | boolean |  | Is it a wiki page? (use mode=wiki instead) |

## MarkupOption

MarkupOption markup options

| Field | Type | Required | Description |
|---|---|---|---|
| `Context` | string |  | URL path for rendering issue, media and file links Expected format: /subpath/{user}/{repo}/src/{branch, commit, tag}/{identifier/path}/{file/dir} |
| `FilePath` | string |  | File path for detecting extension in file mode |
| `Mode` | string |  | Mode to render (markdown, comment, wiki, file) |
| `Text` | string |  | Text markup to render |
| `Wiki` | boolean |  | Is it a wiki page? (use mode=wiki instead) |

## MergePullRequestOption

MergePullRequestForm form for merging Pull Request

| Field | Type | Required | Description |
|---|---|---|---|
| `delete_branch_after_merge` | boolean |  |  |
| `do` | string enum: merge, rebase, rebase-merge, squash, fast-forward-only, manually-merged | yes |  |
| `force_merge` | boolean |  |  |
| `head_commit_id` | string |  |  |
| `merge_commit_id` | string |  |  |
| `merge_message_field` | string |  |  |
| `merge_title_field` | string |  |  |
| `merge_when_checks_succeed` | boolean |  |  |

## MergeUpstreamRequest

| Field | Type | Required | Description |
|---|---|---|---|
| `branch` | string |  |  |
| `ff_only` | boolean |  |  |

## MergeUpstreamResponse

| Field | Type | Required | Description |
|---|---|---|---|
| `merge_type` | string |  |  |

## MigrateRepoOptions

MigrateRepoOptions options for migrating repository's
this is used to interact with api v1

| Field | Type | Required | Description |
|---|---|---|---|
| `auth_password` | string |  |  |
| `auth_token` | string |  |  |
| `auth_username` | string |  |  |
| `aws_access_key_id` | string |  |  |
| `aws_secret_access_key` | string |  |  |
| `clone_addr` | string | yes |  |
| `description` | string |  |  |
| `issues` | boolean |  |  |
| `labels` | boolean |  |  |
| `lfs` | boolean |  |  |
| `lfs_endpoint` | string |  |  |
| `milestones` | boolean |  |  |
| `mirror` | boolean |  |  |
| `mirror_interval` | string |  |  |
| `private` | boolean |  |  |
| `pull_requests` | boolean |  |  |
| `releases` | boolean |  |  |
| `repo_name` | string | yes |  |
| `repo_owner` | string |  | the organization's name or individual user's name who will own the migrated repository |
| `service` | string enum: git, github, gitea, gitlab, gogs, onedev, gitbucket, codebase, codecommit |  |  |
| `uid` | integer (int64) |  | deprecated (only for backwards compatibility, use repo_owner instead) |
| `wiki` | boolean |  |  |

## Milestone

Milestone milestone is a collection of issues on one repository

| Field | Type | Required | Description |
|---|---|---|---|
| `closed_at` | string (date-time) |  |  |
| `closed_issues` | integer (int64) |  | ClosedIssues is the number of closed issues in this milestone |
| `created_at` | string (date-time) |  |  |
| `description` | string |  | Description provides details about the milestone |
| `due_on` | string (date-time) |  |  |
| `id` | integer (int64) |  | ID is the unique identifier for the milestone |
| `open_issues` | integer (int64) |  | OpenIssues is the number of open issues in this milestone |
| `state` | allOf(`StateType`) |  | State indicates if the milestone is open or closed |
| `title` | string |  | Title is the title of the milestone |
| `updated_at` | string (date-time) |  |  |

## MoveProjectColumnsOption

MoveProjectColumnsOption represents options for reordering a project's columns

| Field | Type | Required | Description |
|---|---|---|---|
| `column_ids` | array of integer (int64) | yes | Every column ID of the project, in the desired left-to-right order |

## MoveProjectIssueOption

MoveProjectIssueOption represents options for moving an issue between columns

| Field | Type | Required | Description |
|---|---|---|---|
| `column_id` | integer (int64) | yes | Target column to move the issue into |
| `sorting` | integer (int64) |  | Position within the column, ascending. Omit to append. Negative values sort above the rest, equal values are ordered newest first. |

## NewIssuePinsAllowed

NewIssuePinsAllowed represents an API response that says if new Issue Pins are allowed

| Field | Type | Required | Description |
|---|---|---|---|
| `issues` | boolean |  |  |
| `pull_requests` | boolean |  |  |

## Note

Note contains information related to a git note

| Field | Type | Required | Description |
|---|---|---|---|
| `commit` | `Commit` |  |  |
| `message` | string |  | The content message of the git note |

## NotificationCount

NotificationCount number of unread notifications

| Field | Type | Required | Description |
|---|---|---|---|
| `new` | integer (int64) |  | New is the number of unread notifications |

## NotificationSubject

NotificationSubject contains the notification subject (Issue/Pull/Commit)

| Field | Type | Required | Description |
|---|---|---|---|
| `html_url` | string (uri) |  | HTMLURL is the web URL for the notification subject |
| `latest_comment_html_url` | string (uri) |  | LatestCommentHTMLURL is the web URL for the latest comment |
| `latest_comment_url` | string (uri) |  | LatestCommentURL is the API URL for the latest comment |
| `state` | string enum: open, closed, merged |  | State indicates the current state of the notification subject |
| `title` | string |  | Title is the title of the notification subject |
| `type` | string enum: Issue, Pull, Commit, Repository |  | Type indicates the type of the notification subject |
| `url` | string (uri) |  | URL is the API URL for the notification subject |

## NotificationThread

NotificationThread expose Notification on API

| Field | Type | Required | Description |
|---|---|---|---|
| `id` | integer (int64) |  | ID is the unique identifier for the notification thread |
| `pinned` | boolean |  | Pinned indicates if the notification is pinned |
| `repository` | `Repository` |  |  |
| `subject` | `NotificationSubject` |  |  |
| `unread` | boolean |  | Unread indicates if the notification has been read |
| `updated_at` | string (date-time) |  | UpdatedAt is the time when the notification was last updated |
| `url` | string (uri) |  | URL is the API URL for this notification thread |

## OAuth2Application

| Field | Type | Required | Description |
|---|---|---|---|
| `client_id` | string |  | The client ID of the OAuth2 application |
| `client_secret` | string |  | The client secret of the OAuth2 application |
| `confidential_client` | boolean |  | Whether the client is confidential |
| `created` | string (date-time) |  | The timestamp when the application was created |
| `id` | integer (int64) |  | The unique identifier of the OAuth2 application |
| `name` | string |  | The name of the OAuth2 application |
| `redirect_uris` | array of string |  | The list of allowed redirect URIs |
| `skip_secondary_authorization` | boolean |  | Whether to skip secondary authorization |

## ObjectFormatName

Type: string enum: sha1, sha256

## Organization

Organization represents an organization

| Field | Type | Required | Description |
|---|---|---|---|
| `avatar_url` | string (uri) |  | The URL of the organization's avatar |
| `description` | string |  | The description of the organization |
| `email` | string |  | The email address of the organization |
| `full_name` | string |  | The full display name of the organization |
| `id` | integer (int64) |  | The unique identifier of the organization |
| `location` | string |  | The location of the organization |
| `name` | string |  | The name of the organization |
| `repo_admin_change_team_access` | boolean |  | Whether repository administrators can change team access |
| `username` | string |  | username of the organization deprecated |
| `visibility` | allOf(`VisibilityString`) |  | The visibility level of the organization (public, limited, private) |
| `website` | string |  | The website URL of the organization |

## OrganizationPermissions

OrganizationPermissions list different users permissions on an organization

| Field | Type | Required | Description |
|---|---|---|---|
| `can_create_repository` | boolean |  | Whether the user can create repositories in the organization |
| `can_read` | boolean |  | Whether the user can read the organization |
| `can_write` | boolean |  | Whether the user can write to the organization |
| `is_admin` | boolean |  | Whether the user is an admin of the organization |
| `is_owner` | boolean |  | Whether the user is an owner of the organization |

## PRBranchInfo

PRBranchInfo information about a branch

| Field | Type | Required | Description |
|---|---|---|---|
| `label` | string |  | The display name of the branch |
| `ref` | string |  | The git reference of the branch |
| `repo` | `Repository` |  |  |
| `repo_id` | integer (int64) |  | The unique identifier of the repository |
| `sha` | string |  | The commit SHA of the branch head |

## Package

Package represents a package

| Field | Type | Required | Description |
|---|---|---|---|
| `created_at` | string (date-time) |  | The date and time when the package was created |
| `creator` | `User` |  |  |
| `html_url` | string (uri) |  | The HTML URL to view the package |
| `id` | integer (int64) |  | The unique identifier of the package |
| `name` | string |  | The name of the package |
| `owner` | `User` |  |  |
| `repository` | `Repository` |  |  |
| `type` | string |  | The type of the package (e.g., npm, maven, docker) |
| `version` | string |  | The version of the package |

## PackageFile

PackageFile represents a package file

| Field | Type | Required | Description |
|---|---|---|---|
| `id` | integer (int64) |  | The unique identifier of the package file |
| `md5` | string |  | The MD5 hash of the package file |
| `name` | string |  | The name of the package file |
| `sha1` | string |  | The SHA1 hash of the package file |
| `sha256` | string |  | The SHA256 hash of the package file |
| `sha512` | string |  | The SHA512 hash of the package file |
| `size` | integer (int64) |  | The size of the package file in bytes |

## PayloadCommit

PayloadCommit represents a commit

| Field | Type | Required | Description |
|---|---|---|---|
| `added` | array of string |  | List of files added in this commit |
| `author` | `PayloadUser` |  |  |
| `committer` | `PayloadUser` |  |  |
| `id` | string |  | sha1 hash of the commit |
| `message` | string |  | The commit message |
| `modified` | array of string |  | List of files modified in this commit |
| `removed` | array of string |  | List of files removed in this commit |
| `timestamp` | string (date-time) |  | The timestamp when the commit was made |
| `url` | string (uri) |  | The URL to view this commit |
| `verification` | `PayloadCommitVerification` |  |  |

## PayloadCommitVerification

PayloadCommitVerification represents the GPG verification of a commit

| Field | Type | Required | Description |
|---|---|---|---|
| `payload` | string |  | The signed payload content |
| `reason` | string |  | The reason for the verification status |
| `signature` | string |  | The GPG signature of the commit |
| `signer` | `PayloadUser` |  |  |
| `verified` | boolean |  | Whether the commit signature is verified |

## PayloadUser

PayloadUser represents the author or committer of a commit

| Field | Type | Required | Description |
|---|---|---|---|
| `email` | string (email) |  |  |
| `name` | string |  | Full name of the commit author |
| `username` | string |  | username of the user |

## Permission

Permission represents a set of permissions

| Field | Type | Required | Description |
|---|---|---|---|
| `admin` | boolean |  |  |
| `pull` | boolean |  |  |
| `push` | boolean |  |  |

## Project

Projects track issues and pull requests, standalone note cards are not supported.

| Field | Type | Required | Description |
|---|---|---|---|
| `card_type` | string |  | Card type: "text_only" or "images_and_text" |
| `closed_at` | string (date-time) |  |  |
| `created_at` | string (date-time) |  |  |
| `creator` | `User` |  |  |
| `creator_id` | integer (int64) |  | Deprecated: use Creator instead |
| `description` | string |  |  |
| `html_url` | string (uri) |  |  |
| `id` | integer (int64) |  |  |
| `is_closed` | boolean |  | Deprecated: use State instead |
| `num_closed_issues` | integer (int64) |  |  |
| `num_issues` | integer (int64) |  |  |
| `num_open_issues` | integer (int64) |  |  |
| `owner_id` | integer (int64) |  |  |
| `repo_id` | integer (int64) |  |  |
| `state` | `StateType` |  |  |
| `template_type` | string |  | Template type: "none", "basic_kanban" or "bug_triage" |
| `title` | string |  |  |
| `type` | string |  | Project type: "individual", "repository" or "organization" |
| `updated_at` | string (date-time) |  | null only for legacy rows that carry no update timestamp |

## ProjectColumn

ProjectColumn represents a project column (board)

| Field | Type | Required | Description |
|---|---|---|---|
| `color` | string |  |  |
| `created_at` | string (date-time) |  |  |
| `creator` | `User` |  |  |
| `default` | boolean |  |  |
| `id` | integer (int64) |  |  |
| `project_id` | integer (int64) |  |  |
| `sorting` | integer (int64) |  |  |
| `title` | string |  |  |
| `updated_at` | string (date-time) |  | null only for legacy rows that carry no update timestamp |

## PublicKey

PublicKey publickey is a user key to push code to repository

| Field | Type | Required | Description |
|---|---|---|---|
| `created_at` | string (date-time) |  | Created is the time when the key was added |
| `fingerprint` | string |  | Fingerprint is the key's fingerprint |
| `id` | integer (int64) |  | ID is the unique identifier for the public key |
| `key` | string |  | Key contains the actual SSH public key content |
| `key_type` | string |  | KeyType indicates the type of the SSH key |
| `last_used_at` | string (date-time) |  | Updated is the time when the key was last used |
| `read_only` | boolean |  | ReadOnly indicates if the key has read-only access |
| `title` | string |  | Title is the human-readable name for the key |
| `url` | string (uri) |  | URL is the API URL for this key |
| `user` | `User` |  |  |

## PullRequest

PullRequest represents a pull request

| Field | Type | Required | Description |
|---|---|---|---|
| `additions` | integer (int64) |  | The number of lines added in the pull request |
| `allow_maintainer_edit` | boolean |  | Whether maintainers can edit the pull request |
| `assignee` | `User` |  |  |
| `assignees` | array of `User` |  | The list of users assigned to the pull request |
| `base` | `PRBranchInfo` |  |  |
| `body` | string |  | The description body of the pull request |
| `changed_files` | integer (int64) |  | The number of files changed in the pull request |
| `closed_at` | string (date-time) |  |  |
| `comments` | integer (int64) |  | The number of comments on the pull request |
| `content_version` | integer (int64) |  | The version of the pull request content for optimistic locking |
| `created_at` | string (date-time) |  |  |
| `deletions` | integer (int64) |  | The number of lines deleted in the pull request |
| `diff_url` | string (uri) |  | The URL to download the diff patch |
| `draft` | boolean |  | Whether the pull request is a draft |
| `due_date` | string (date-time) |  |  |
| `head` | `PRBranchInfo` |  |  |
| `html_url` | string (uri) |  | The HTML URL to view the pull request |
| `id` | integer (int64) |  | The unique identifier of the pull request |
| `is_locked` | boolean |  | Whether the pull request conversation is locked |
| `labels` | array of `Label` |  | The labels attached to the pull request |
| `merge_base` | string |  | The merge base commit SHA |
| `merge_commit_sha` | string |  | The SHA of the merge commit |
| `mergeable` | boolean |  | Whether the pull request can be merged |
| `merged` | boolean |  | Whether the pull request has been merged |
| `merged_at` | string (date-time) |  |  |
| `merged_by` | `User` |  |  |
| `milestone` | `Milestone` |  |  |
| `number` | integer (int64) |  | The pull request number |
| `patch_url` | string (uri) |  | The URL to download the patch file |
| `pin_order` | integer (int64) |  | The pin order for the pull request |
| `requested_reviewers` | array of `User` |  | The users requested to review the pull request |
| `requested_reviewers_teams` | array of `Team` |  | The teams requested to review the pull request |
| `review_comments` | integer (int64) |  | number of review comments made on the diff of a PR review (not including comments on commits or issues in a PR) |
| `state` | allOf(`StateType`) |  | The current state of the pull request |
| `title` | string |  | The title of the pull request |
| `updated_at` | string (date-time) |  |  |
| `url` | string (uri) |  | The API URL of the pull request |
| `user` | `User` |  |  |

## PullRequestMeta

PullRequestMeta PR info if an issue is a PR

| Field | Type | Required | Description |
|---|---|---|---|
| `draft` | boolean |  |  |
| `html_url` | string (uri) |  |  |
| `merged` | boolean |  |  |
| `merged_at` | string (date-time) |  |  |

## PullRequestMinimal

PullRequestMinimal is the minimal information about a pull request, as
returned in the `pull_requests` field of a workflow run.

| Field | Type | Required | Description |
|---|---|---|---|
| `base` | `PullRequestMinimalHead` |  |  |
| `head` | `PullRequestMinimalHead` |  |  |
| `id` | integer (int64) |  |  |
| `number` | integer (int64) |  |  |
| `url` | string (uri) |  |  |

## PullRequestMinimalHead

| Field | Type | Required | Description |
|---|---|---|---|
| `ref` | string |  |  |
| `repo` | `PullRequestMinimalHeadRepo` |  |  |
| `sha` | string |  |  |

## PullRequestMinimalHeadRepo

| Field | Type | Required | Description |
|---|---|---|---|
| `id` | integer (int64) |  |  |
| `name` | string |  |  |
| `url` | string (uri) |  |  |

## PullReview

PullReview represents a pull request review

| Field | Type | Required | Description |
|---|---|---|---|
| `body` | string |  |  |
| `comments_count` | integer (int64) |  |  |
| `commit_id` | string |  |  |
| `dismissed` | boolean |  |  |
| `html_url` | string (uri) |  | HTMLURL is the web URL for viewing the review |
| `id` | integer (int64) |  |  |
| `official` | boolean |  |  |
| `pull_request_url` | string (uri) |  | HTMLPullURL is the web URL for the pull request |
| `stale` | boolean |  |  |
| `state` | `ReviewStateType` |  |  |
| `submitted_at` | string (date-time) |  |  |
| `team` | `Team` |  |  |
| `updated_at` | string (date-time) |  |  |
| `user` | `User` |  |  |

## PullReviewComment

PullReviewComment represents a comment on a pull request review

| Field | Type | Required | Description |
|---|---|---|---|
| `body` | string |  |  |
| `commit_id` | string |  |  |
| `created_at` | string (date-time) |  |  |
| `diff_hunk` | string |  |  |
| `html_url` | string (uri) |  |  |
| `id` | integer (int64) |  |  |
| `original_commit_id` | string |  |  |
| `original_position` | integer (uint64) |  |  |
| `path` | string |  |  |
| `position` | integer (uint64) |  |  |
| `pull_request_review_id` | integer (int64) |  |  |
| `pull_request_url` | string (uri) |  |  |
| `resolver` | `User` |  |  |
| `updated_at` | string (date-time) |  |  |
| `user` | `User` |  |  |

## PullReviewRequestOptions

PullReviewRequestOptions are options to add or remove pull request review requests

| Field | Type | Required | Description |
|---|---|---|---|
| `reviewers` | array of string |  |  |
| `team_reviewers` | array of string |  |  |

## PushMirror

PushMirror represents information of a push mirror

| Field | Type | Required | Description |
|---|---|---|---|
| `created` | string (date-time) |  |  |
| `interval` | string |  | The sync interval for automatic updates |
| `last_error` | string |  | The last error message encountered during sync |
| `last_update` | string (date-time) |  |  |
| `remote_address` | string |  | The remote repository URL being mirrored to |
| `remote_name` | string |  | The name of the remote in the git configuration |
| `repo_name` | string |  | The name of the source repository |
| `sync_on_commit` | boolean |  | Whether to sync on every commit |

## Reaction

Reaction contain one reaction

| Field | Type | Required | Description |
|---|---|---|---|
| `content` | string |  | The reaction content (e.g., emoji or reaction type) |
| `created_at` | string (date-time) |  | The date and time when the reaction was created |
| `user` | `User` |  |  |

## Reference

| Field | Type | Required | Description |
|---|---|---|---|
| `object` | `GitObject` |  |  |
| `ref` | string |  | The name of the Git reference (e.g., refs/heads/main) |
| `url` | string (uri) |  | The URL to access this Git reference |

## Release

Release represents a repository release

| Field | Type | Required | Description |
|---|---|---|---|
| `assets` | array of `Attachment` |  | The files attached to the release |
| `author` | `User` |  |  |
| `body` | string |  | The release notes or description |
| `created_at` | string (date-time) |  |  |
| `draft` | boolean |  | Whether the release is a draft |
| `html_url` | string (uri) |  | The HTML URL to view the release |
| `id` | integer (int64) |  | The unique identifier of the release |
| `name` | string |  | The display title of the release |
| `prerelease` | boolean |  | Whether the release is a prerelease |
| `published_at` | string (date-time) |  |  |
| `tag_name` | string |  | The name of the git tag associated with the release |
| `tarball_url` | string (uri) |  | The URL to download the tarball archive |
| `target_commitish` | string |  | The target commitish for the release |
| `upload_url` | string (uri) |  | The URL template for uploading release assets |
| `url` | string (uri) |  | The API URL of the release |
| `zipball_url` | string (uri) |  | The URL to download the zip archive |

## RenameBranchRepoOption

RenameBranchRepoOption options when renaming a branch in a repository

| Field | Type | Required | Description |
|---|---|---|---|
| `name` | string | yes | New branch name |

## RenameOrgOption

RenameOrgOption options when renaming an organization

| Field | Type | Required | Description |
|---|---|---|---|
| `new_name` | string | yes | New username for this org. This name cannot be in use yet by any other user. |

## RenameUserOption

RenameUserOption options when renaming a user

| Field | Type | Required | Description |
|---|---|---|---|
| `new_username` | string | yes | New username for this user. This name cannot be in use yet by any other user. |

## RepoCollaboratorPermission

RepoCollaboratorPermission to get repository permission for a collaborator

| Field | Type | Required | Description |
|---|---|---|---|
| `permission` | allOf(`AccessLevelName`) |  | Permission level of the collaborator |
| `role_name` | string |  | RoleName is the name of the permission role |
| `user` | `User` |  |  |

## RepoCommit

| Field | Type | Required | Description |
|---|---|---|---|
| `author` | `CommitUser` |  |  |
| `committer` | `CommitUser` |  |  |
| `message` | string |  | Message is the commit message |
| `tree` | `CommitMeta` |  |  |
| `url` | string (uri) |  | URL is the API URL for the commit |
| `verification` | `PayloadCommitVerification` |  |  |

## RepoTopicOptions

RepoTopicOptions a collection of repo topic names

| Field | Type | Required | Description |
|---|---|---|---|
| `topics` | array of string |  | list of topic names |

## RepoTransfer

RepoTransfer represents a pending repo transfer

| Field | Type | Required | Description |
|---|---|---|---|
| `doer` | `User` |  |  |
| `recipient` | `User` |  |  |
| `teams` | array of `Team` |  |  |

## RepoWritePermission

Type: string enum: read, write, admin

## Repository

Repository represents a repository

| Field | Type | Required | Description |
|---|---|---|---|
| `allow_fast_forward_only_merge` | boolean |  |  |
| `allow_manual_merge` | boolean |  |  |
| `allow_merge_commits` | boolean |  |  |
| `allow_merge_update` | boolean |  |  |
| `allow_rebase` | boolean |  |  |
| `allow_rebase_explicit` | boolean |  |  |
| `allow_rebase_update` | boolean |  |  |
| `allow_squash_merge` | boolean |  |  |
| `archived` | boolean |  |  |
| `archived_at` | string (date-time) |  |  |
| `autodetect_manual_merge` | boolean |  |  |
| `avatar_url` | string (uri) |  |  |
| `branch_count` | integer (int64) |  |  |
| `clone_url` | string (uri) |  |  |
| `created_at` | string (date-time) |  |  |
| `default_allow_maintainer_edit` | boolean |  |  |
| `default_branch` | string |  |  |
| `default_delete_branch_after_merge` | boolean |  |  |
| `default_merge_style` | string |  |  |
| `default_target_branch` | string |  |  |
| `default_update_style` | string |  |  |
| `description` | string |  |  |
| `empty` | boolean |  |  |
| `external_tracker` | `ExternalTracker` |  |  |
| `external_wiki` | `ExternalWiki` |  |  |
| `fork` | boolean |  |  |
| `forks_count` | integer (int64) |  |  |
| `full_name` | string |  |  |
| `has_actions` | boolean |  |  |
| `has_code` | boolean |  |  |
| `has_issues` | boolean |  |  |
| `has_packages` | boolean |  |  |
| `has_projects` | boolean |  |  |
| `has_pull_requests` | boolean |  |  |
| `has_releases` | boolean |  |  |
| `has_wiki` | boolean |  |  |
| `html_url` | string (uri) |  |  |
| `id` | integer (int64) |  |  |
| `ignore_whitespace_conflicts` | boolean |  |  |
| `internal` | boolean |  |  |
| `internal_tracker` | `InternalTracker` |  |  |
| `language` | string |  |  |
| `languages_url` | string (uri) |  |  |
| `licenses` | array of string |  |  |
| `link` | string |  |  |
| `mirror` | boolean |  |  |
| `mirror_interval` | string |  |  |
| `mirror_last_sync_at` | string (date-time) |  |  |
| `mirror_updated` | string (date-time) |  |  |
| `name` | string |  |  |
| `object_format_name` | allOf(`ObjectFormatName`) |  | ObjectFormatName of the underlying git repository |
| `open_issues_count` | integer (int64) |  |  |
| `open_pr_counter` | integer (int64) |  |  |
| `original_url` | string (uri) |  |  |
| `owner` | `User` |  |  |
| `parent` | `Repository` |  |  |
| `permissions` | `Permission` |  |  |
| `private` | boolean |  |  |
| `projects_mode` | string |  |  |
| `release_counter` | integer (int64) |  |  |
| `repo_transfer` | `RepoTransfer` |  |  |
| `size` | integer (int64) |  |  |
| `ssh_url` | string (uri) |  |  |
| `stars_count` | integer (int64) |  |  |
| `template` | boolean |  |  |
| `topics` | array of string |  |  |
| `updated_at` | string (date-time) |  |  |
| `url` | string (uri) |  |  |
| `watchers_count` | integer (int64) |  |  |
| `website` | string |  |  |

## RepositoryMeta

RepositoryMeta basic repository information

| Field | Type | Required | Description |
|---|---|---|---|
| `full_name` | string |  |  |
| `id` | integer (int64) |  |  |
| `name` | string |  |  |
| `owner` | string |  |  |

## ReviewStateType

Type: string enum: APPROVED, PENDING, COMMENT, REQUEST_CHANGES, REQUEST_REVIEW

## RunDetails

RunDetails returns workflow_dispatch runid and url

| Field | Type | Required | Description |
|---|---|---|---|
| `html_url` | string (uri) |  |  |
| `run_url` | string (uri) |  |  |
| `workflow_run_id` | integer (int64) |  |  |

## SearchResults

SearchResults results of a successful search

| Field | Type | Required | Description |
|---|---|---|---|
| `data` | array of `Repository` |  | Data contains the repository search results |
| `ok` | boolean |  | OK indicates if the search was successful |

## Secret

Secret represents a secret

| Field | Type | Required | Description |
|---|---|---|---|
| `created_at` | string (date-time) |  |  |
| `description` | string |  | the secret's description |
| `name` | string |  | the secret's name |

## ServerVersion

ServerVersion wraps the version of the server

| Field | Type | Required | Description |
|---|---|---|---|
| `version` | string |  | Version is the server version string |

## StateType

Type: string enum: open, closed

## StopWatch

StopWatch represent a running stopwatch

| Field | Type | Required | Description |
|---|---|---|---|
| `created` | string (date-time) |  | Created is the time when the stopwatch was started |
| `duration` | string |  | Duration is a human-readable duration string |
| `issue_index` | integer (int64) |  | IssueIndex is the index number of the associated issue |
| `issue_title` | string |  | IssueTitle is the title of the associated issue |
| `repo_name` | string |  | RepoName is the name of the repository |
| `repo_owner_name` | string |  | RepoOwnerName is the name of the repository owner |
| `seconds` | integer (int64) |  | Seconds is the total elapsed time in seconds |

## SubmitPullReviewOptions

SubmitPullReviewOptions are options to submit a pending pull request review

| Field | Type | Required | Description |
|---|---|---|---|
| `body` | string |  |  |
| `event` | `ReviewStateType` |  |  |

## Tag

Tag represents a repository tag

| Field | Type | Required | Description |
|---|---|---|---|
| `commit` | `CommitMeta` |  |  |
| `id` | string |  | The ID (SHA) of the tag |
| `message` | string |  | The message associated with the tag |
| `name` | string |  | The name of the tag |
| `tarball_url` | string (uri) |  | The URL to download the tarball archive |
| `zipball_url` | string (uri) |  | The URL to download the zipball archive |

## TagProtection

TagProtection represents a tag protection

| Field | Type | Required | Description |
|---|---|---|---|
| `created_at` | string (date-time) |  | The date and time when the tag protection was created |
| `id` | integer (int64) |  | The unique identifier of the tag protection |
| `name_pattern` | string |  | The pattern to match tag names for protection |
| `updated_at` | string (date-time) |  | The date and time when the tag protection was last updated |
| `whitelist_teams` | array of string |  | List of team names allowed to create/delete protected tags |
| `whitelist_usernames` | array of string |  | List of usernames allowed to create/delete protected tags |

## Team

Team represents a team in an organization

| Field | Type | Required | Description |
|---|---|---|---|
| `can_create_org_repo` | boolean |  | Whether the team can create repositories in the organization |
| `description` | string |  | The description of the team |
| `id` | integer (int64) |  | The unique identifier of the team |
| `includes_all_repositories` | boolean |  | Whether the team has access to all repositories in the organization |
| `name` | string |  | The name of the team |
| `organization` | `Organization` |  |  |
| `permission` | `AccessLevelName` |  |  |
| `units` | array of string |  | Deprecated: This variable should be replaced by UnitsMap and will be dropped in later versions. |
| `units_map` | object |  |  |
| `visibility` | allOf(`TeamVisibility`) |  | Team visibility within the organization. "private" teams are only listable by members and org owners; "limited" teams are listable by any organization member; "public" teams are listable by any signed-in user. |

## TeamVisibility

Type: string enum: public, limited, private

## TimeStamp

TimeStamp defines a timestamp

Type: integer (int64)

## TimelineComment

TimelineComment represents a timeline comment (comment of any type) on a commit or issue

| Field | Type | Required | Description |
|---|---|---|---|
| `assignee` | `User` |  |  |
| `assignee_team` | `Team` |  |  |
| `body` | string |  | Body contains the timeline event content |
| `created_at` | string (date-time) |  |  |
| `dependent_issue` | `Issue` |  |  |
| `html_url` | string (uri) |  | HTMLURL is the web URL for viewing the comment |
| `id` | integer (int64) |  | ID is the unique identifier for the timeline comment |
| `issue_url` | string (uri) |  | IssueURL is the API URL for the issue |
| `label` | `Label` |  |  |
| `milestone` | `Milestone` |  |  |
| `new_ref` | string |  |  |
| `new_title` | string |  |  |
| `old_milestone` | `Milestone` |  |  |
| `old_project_id` | integer (int64) |  |  |
| `old_ref` | string |  |  |
| `old_title` | string |  |  |
| `project_id` | integer (int64) |  |  |
| `pull_request_url` | string (uri) |  | PRURL is the API URL for the pull request (if applicable) |
| `ref_action` | string |  |  |
| `ref_comment` | `Comment` |  |  |
| `ref_commit_sha` | string |  | commit SHA where issue/PR was referenced |
| `ref_issue` | `Issue` |  |  |
| `removed_assignee` | boolean |  | whether the assignees were removed or added |
| `resolve_doer` | `User` |  |  |
| `review_id` | integer (int64) |  |  |
| `tracked_time` | `TrackedTime` |  |  |
| `type` | string |  | Type indicates the type of timeline event |
| `updated_at` | string (date-time) |  |  |
| `user` | `User` |  |  |

## TopicListResponse

TopicListResponse returns a list of TopicResponse

| Field | Type | Required | Description |
|---|---|---|---|
| `topics` | array of `TopicResponse` |  |  |

## TopicName

TopicName a list of repo topic names

| Field | Type | Required | Description |
|---|---|---|---|
| `topics` | array of string |  | List of topic names |

## TopicResponse

TopicResponse for returning topics

| Field | Type | Required | Description |
|---|---|---|---|
| `created` | string (date-time) |  | The date and time when the topic was created |
| `id` | integer (int64) |  | The unique identifier of the topic |
| `repo_count` | integer (int64) |  | The number of repositories using this topic |
| `topic_name` | string |  | The name of the topic |
| `updated` | string (date-time) |  | The date and time when the topic was last updated |

## TrackedTime

TrackedTime worked time for an issue / pr

| Field | Type | Required | Description |
|---|---|---|---|
| `created` | string (date-time) |  |  |
| `id` | integer (int64) |  | ID is the unique identifier for the tracked time entry |
| `issue` | `Issue` |  |  |
| `issue_id` | integer (int64) |  | deprecated (only for backwards compatibility) |
| `time` | integer (int64) |  | Time in seconds |
| `user_id` | integer (int64) |  | deprecated (only for backwards compatibility) |
| `user_name` | string |  | username of the user |

## TransferRepoOption

TransferRepoOption options when transfer a repository's ownership

| Field | Type | Required | Description |
|---|---|---|---|
| `new_owner` | string | yes |  |
| `team_ids` | array of integer (int64) |  | ID of the team or teams to add to the repository. Teams can only be added to organization-owned repositories. |

## UpdateBranchProtectionPriories

UpdateBranchProtectionPriories a list to update the branch protection rule priorities

| Field | Type | Required | Description |
|---|---|---|---|
| `ids` | array of integer (int64) |  |  |

## UpdateBranchRepoOption

UpdateBranchRepoOption options when updating a branch reference in a repository

| Field | Type | Required | Description |
|---|---|---|---|
| `force` | boolean |  | Force update even if the change is not a fast-forward |
| `new_commit_id` | string | yes | New commit SHA (or any ref) the branch should point to |
| `old_commit_id` | string |  | Expected old commit SHA of the branch; if provided it must match the current tip |

## UpdateFileOptions

UpdateFileOptions options for updating or creating a file
Note: `author` and `committer` are optional (if only one is given, it will be used for the other, otherwise the authenticated user will be used)

| Field | Type | Required | Description |
|---|---|---|---|
| `author` | `Identity` |  |  |
| `branch` | string |  | branch (optional) is the base branch for the changes. If not supplied, the default branch is used |
| `committer` | `Identity` |  |  |
| `content` | string | yes | content must be base64 encoded |
| `dates` | `CommitDateOptions` |  |  |
| `force_push` | boolean |  | force_push (optional) will do a force-push if the new branch already exists |
| `from_path` | string |  | from_path (optional) is the path of the original file which will be moved/renamed to the path in the URL |
| `message` | string |  | message (optional) is the commit message of the changes. If not supplied, a default message will be used |
| `new_branch` | string |  | new_branch (optional) will make a new branch from base branch for the changes. If not supplied, the changes will be committed to the base branch |
| `sha` | string |  | the blob ID (SHA) for the file that already exists to update, or leave it empty to create a new file |
| `signoff` | boolean |  | Add a Signed-off-by trailer by the committer at the end of the commit log message. |

## UpdateRepoAvatarOption

UpdateRepoAvatarUserOption options when updating the repo avatar

| Field | Type | Required | Description |
|---|---|---|---|
| `image` | string |  | image must be base64 encoded |

## UpdateUserAvatarOption

UpdateUserAvatarUserOption options when updating the user avatar

| Field | Type | Required | Description |
|---|---|---|---|
| `image` | string |  | image must be base64 encoded |

## UpdateVariableOption

UpdateVariableOption the option when updating variable

| Field | Type | Required | Description |
|---|---|---|---|
| `description` | string |  | Description of the variable to update |
| `name` | string |  | New name for the variable. If the field is empty, the variable name won't be updated. |
| `value` | string | yes | Value of the variable to update |

## User

User represents a user

| Field | Type | Required | Description |
|---|---|---|---|
| `active` | boolean |  | Is user active |
| `avatar_url` | string (uri) |  | URL to the user's avatar |
| `created` | string (date-time) |  |  |
| `description` | string |  | the user's description |
| `email` | string (email) |  |  |
| `followers_count` | integer (int64) |  | user counts |
| `following_count` | integer (int64) |  |  |
| `full_name` | string |  | the user's full name |
| `html_url` | string (uri) |  | URL to the user's gitea page |
| `id` | integer (int64) |  | the user's id |
| `is_admin` | boolean |  | Is the user an administrator |
| `language` | string |  | User locale |
| `last_login` | string (date-time) |  |  |
| `location` | string |  | the user's location |
| `login` | string |  | login of the user, same as `username` |
| `login_name` | string |  | identifier of the user, provided by the external authenticator (if configured) |
| `prohibit_login` | boolean |  | Is user login prohibited |
| `restricted` | boolean |  | Is user restricted |
| `source_id` | integer (int64) |  | The ID of the user's Authentication Source |
| `starred_repos_count` | integer (int64) |  |  |
| `type` | allOf(`UserTypeString`) |  | the user type |
| `visibility` | allOf(`VisibilityString`) |  | User visibility level option: public, limited, private |
| `website` | string |  | the user's website |

## UserBadgeOption

UserBadgeOption options for link between users and badges

| Field | Type | Required | Description |
|---|---|---|---|
| `badge_slugs` | array of string |  |  |

## UserHeatmapData

UserHeatmapData represents the data needed to create a heatmap

| Field | Type | Required | Description |
|---|---|---|---|
| `contributions` | integer (int64) |  |  |
| `timestamp` | `TimeStamp` |  |  |

## UserMeta

| Field | Type | Required | Description |
|---|---|---|---|
| `id` | integer (int64) |  | The unique identifier of the user |
| `login` | string |  | The username of the user |

## UserSettings

UserSettings represents user settings

| Field | Type | Required | Description |
|---|---|---|---|
| `description` | string |  |  |
| `diff_view_style` | string |  |  |
| `full_name` | string |  |  |
| `hide_activity` | boolean |  |  |
| `hide_email` | boolean |  | Privacy |
| `language` | string |  |  |
| `location` | string |  |  |
| `theme` | string |  |  |
| `website` | string |  |  |

## UserSettingsOptions

UserSettingsOptions represents options to change user settings

| Field | Type | Required | Description |
|---|---|---|---|
| `description` | string |  |  |
| `diff_view_style` | string |  |  |
| `full_name` | string |  |  |
| `hide_activity` | boolean |  |  |
| `hide_email` | boolean |  | Privacy |
| `language` | string |  |  |
| `location` | string |  |  |
| `theme` | string |  |  |
| `website` | string |  |  |

## UserTypeString

Type: string enum: User, Organization, Bot

## VisibilityString

Type: string enum: public, limited, private

## WatchInfo

WatchInfo represents an API watch status of one repository

| Field | Type | Required | Description |
|---|---|---|---|
| `created_at` | string (date-time) |  | The timestamp when the watch status was created |
| `ignored` | boolean |  | Whether notifications for the repository are ignored |
| `reason` | object |  | The reason for the current watch status |
| `repository_url` | string (uri) |  | The URL of the repository being watched |
| `subscribed` | boolean |  | Whether the repository is being watched for notifications |
| `url` | string (uri) |  | The URL for managing the watch status |

## WikiCommit

WikiCommit page commit/revision

| Field | Type | Required | Description |
|---|---|---|---|
| `author` | `CommitUser` |  |  |
| `commiter` | `CommitUser` |  |  |
| `message` | string |  | The commit message |
| `sha` | string |  | The commit SHA hash |

## WikiCommitList

WikiCommitList commit/revision list

| Field | Type | Required | Description |
|---|---|---|---|
| `commits` | array of `WikiCommit` |  | The list of wiki commits |
| `count` | integer (int64) |  | The total count of commits |

## WikiPage

WikiPage a wiki page

| Field | Type | Required | Description |
|---|---|---|---|
| `commit_count` | integer (int64) |  | The number of commits that modified this page |
| `content_base64` | string |  | Page content, base64 encoded |
| `footer` | string |  | The footer content for the wiki page |
| `html_url` | string (uri) |  | The HTML URL to view the wiki page |
| `last_commit` | `WikiCommit` |  |  |
| `sidebar` | string |  | The sidebar content for the wiki page |
| `sub_url` | string (uri) |  | The sub URL path for the wiki page |
| `title` | string |  | The title of the wiki page |

## WikiPageMetaData

WikiPageMetaData wiki page meta information

| Field | Type | Required | Description |
|---|---|---|---|
| `html_url` | string (uri) |  | The HTML URL to view the wiki page |
| `last_commit` | `WikiCommit` |  |  |
| `sub_url` | string (uri) |  | The sub URL path for the wiki page |
| `title` | string |  | The title of the wiki page |

