# Stripe API 2023-10-16 — files

Operations under `/v1/files` for API version 2023-10-16, generated from Stripe's OpenAPI spec (spec3.json).

## GET /v1/files

operationId: `GetFiles`

Returns a list of the files that your account has access to. Stripe sorts and returns the files by their creation dates, placing the most recently created files at the top.

Parameters (query string for GET/DELETE, form-encoded body for POST):

| Field | Type | Required | Description |
|---|---|---|---|
| `created` | object or integer |  | Only return files that were created during the given date interval. |
| `created.gt` | integer |  |  |
| `created.gte` | integer |  |  |
| `created.lt` | integer |  |  |
| `created.lte` | integer |  |  |
| `ending_before` | string |  | A cursor for use in pagination. `ending_before` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, starting with `obj_bar`, your subsequent call can include `ending_before=obj_bar` in order to fetch the previous page of the list. |
| `expand` | array of string |  | Specifies which fields in the response should be expanded. |
| `limit` | integer |  | A limit on the number of objects to be returned. Limit can range between 1 and 100, and the default is 10. |
| `purpose` | enum: `account_requirement`, `additional_verification`, `business_icon`, `business_logo`, `customer_signature`, `dispute_evidence`, `document_provider_identity_document`, `finance_report_run`, `identity_document`, `identity_document_downloadable`, `pci_document`, `selfie`, `sigma_scheduled_query`, `tax_document_user_upload`, `terminal_reader_splashscreen` |  | Filter queries by the file purpose. If you don't provide a purpose, the queries return unfiltered files. |
| `starting_after` | string |  | A cursor for use in pagination. `starting_after` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, ending with `obj_foo`, your subsequent call can include `starting_after=obj_foo` in order to fetch the next page of the list. |

Returns: object

## POST /v1/files

operationId: `PostFiles`

To upload a file to Stripe, you need to send a request of type `multipart/form-data`. Include the file you want to upload in the request, and the parameters for creating a file.

All of Stripe’s officially supported Client libraries support sending `multipart/form-data`.

Returns: `file`

## GET /v1/files/{file}

operationId: `GetFilesFile`

Retrieves the details of an existing file object. After you supply a unique file ID, Stripe returns the corresponding file object. Learn how to [access file contents](https://stripe.com/docs/file-upload#download-file-contents).

Parameters (query string for GET/DELETE, form-encoded body for POST):

| Field | Type | Required | Description |
|---|---|---|---|
| `expand` | array of string |  | Specifies which fields in the response should be expanded. |
| `file (path)` | string | yes |  |

Returns: `file`

# Objects returned

## The `file` object

This object represents files hosted on Stripe's servers. You can upload
files with the [create file](https://stripe.com/docs/api#create_file) request
(for example, when uploading dispute evidence). Stripe also
creates files independently (for example, the results of a [Sigma scheduled
query](#scheduled_queries)).

Related guide: [File upload guide](https://stripe.com/docs/file-upload)

Expandable fields (pass `expand[]=<field>`): `links`

| Field | Type | Required | Description |
|---|---|---|---|
| `created` | timestamp (Unix seconds) | yes | Time at which the object was created. Measured in seconds since the Unix epoch. |
| `expires_at` | timestamp (Unix seconds) |  | The file expires and isn't available at this time in epoch seconds. |
| `filename` | string |  | The suitable name for saving the file to a filesystem. |
| `id` | string | yes | Unique identifier for the object. |
| `links` | object |  | A list of [file links](https://stripe.com/docs/api#file_links) that point at this file. |
| `object` | enum: `file` | yes | String representing the object's type. Objects of the same type share the same value. |
| `purpose` | enum: `account_requirement`, `additional_verification`, `business_icon`, `business_logo`, `customer_signature`, `dispute_evidence`, `document_provider_identity_document`, `finance_report_run`, `identity_document`, `identity_document_downloadable`, `pci_document`, `selfie`, `sigma_scheduled_query`, `tax_document_user_upload`, `terminal_reader_splashscreen` | yes | The [purpose](https://stripe.com/docs/file-upload#uploading-a-file) of the uploaded file. |
| `size` | integer | yes | The size of the file object in bytes. |
| `title` | string |  | A suitable title for the document. |
| `type` | string |  | The returned file type (for example, `csv`, `pdf`, `jpg`, or `png`). |
| `url` | string |  | Use your live secret API key to download the file from this URL. |

