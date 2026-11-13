# GetDataset

Service: Amazon CloudWatch · SDK for JavaScript v3: `GetDatasetCommand` from `@aws-sdk/client-cloudwatch`

Returns information about the specified dataset. This includes its identifier,
Amazon Resource Name (ARN), and any customer managed Amazon Web Services Key
Management Service (Amazon Web Services KMS) key that is currently associated with
it.

Only the `default` dataset is supported. The `default` dataset
is implicit for every account in every Region — you can call `GetDataset`
for it without first creating it. If no customer managed KMS key has been associated
with the dataset, the response omits the `KmsKeyArn` field, indicating that
data is encrypted at rest using an Amazon Web Services owned key managed by
Amazon CloudWatch.

To associate a customer managed KMS key with a dataset, use [AssociateDatasetKmsKey](https://docs.aws.amazon.com/AmazonCloudWatch/latest/APIReference/API_AssociateDatasetKmsKey.html). To remove the association, use [DisassociateDatasetKmsKey](https://docs.aws.amazon.com/AmazonCloudWatch/latest/APIReference/API_DisassociateDatasetKmsKey.html).

## Input (`GetDatasetInput`)

### `DatasetIdentifier` — string · **required**

Specifies the identifier of the dataset to retrieve. For the `default`
dataset, you can specify either `default` or the full dataset Amazon
Resource Name (ARN) in the format
`arn:aws:cloudwatch:Region:account-id:dataset/default`.

## Output (`GetDatasetOutput`)

### `DatasetId` — string · **required**

Returns the identifier of the dataset.

### `Arn` — string · **required**

Returns the Amazon Resource Name (ARN) of the dataset, in the format
`arn:aws:cloudwatch:Region:account-id:dataset/dataset-id`.

### `KmsKeyArn` — string

Returns the Amazon Resource Name (ARN) of the customer managed Amazon Web Services
KMS key that is currently associated with the dataset, if any. If the dataset is not
associated with a customer managed KMS key, this field is not included in the
response and the dataset is encrypted at rest using an Amazon Web Services owned
key.

## Errors

- `ResourceNotFoundException` — The named resource does not exist.
