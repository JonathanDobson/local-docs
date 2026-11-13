# AWS Lambda — API reference

API version `2015-03-31` · protocol restJson1 · SDK for JavaScript v3 client `@aws-sdk/client-lambda`

Lambda

**Overview**

Lambda is a compute service that lets you run code without provisioning or managing servers. Lambda runs your code on a high-availability compute infrastructure and performs all of the administration of the compute resources, including server and operating system maintenance, capacity provisioning and automatic scaling, code monitoring and logging. With Lambda, you can run code for virtually any type of application or backend service. For more information about the Lambda service, see [What is Lambda](https://docs.aws.amazon.com/lambda/latest/dg/welcome.html) in the **Lambda Developer Guide**.

Lambda Event Functions, previously known as Lambda functions, run your code in response to events and API calls. In the Lambda API, the Amazon Web Services SDKs, and the CLI, Event Functions are still called *functions*, for example in `CreateFunction` and `Invoke`. You don't need to change any existing code.

The *Lambda API Reference* provides information about each of the API methods for Lambda Event Functions, including details about the parameters in each API request and response.

You can use Software Development Kits (SDKs), Integrated Development Environment (IDE) Toolkits, and command line tools to access the API. For installation instructions, see [Tools for Amazon Web Services](http://aws.amazon.com/tools/).

For a list of Region-specific endpoints that Lambda supports, see [Lambda endpoints and quotas](https://docs.aws.amazon.com/general/latest/gr/lambda-service.html)  in the *Amazon Web Services General Reference.*.

When making the API calls, you will need to authenticate your request by providing a signature. Lambda supports signature version 4. For more information, see [Signature Version 4 signing process](https://docs.aws.amazon.com/general/latest/gr/signature-version-4.html) in the *Amazon Web Services General Reference.*.

**CA certificates**

Because Amazon Web Services SDKs use the CA certificates from your computer, changes to the certificates on the Amazon Web Services servers can cause connection failures when you attempt to use an SDK. You can prevent these failures by keeping your computer's CA certificates and operating system up-to-date. If you encounter this issue in a corporate environment and do not manage your own computer, you might need to ask an administrator to assist with the update process. The following list shows minimum operating system and Java versions:

- Microsoft Windows versions that have updates from January 2005 or later installed contain at least one of the required CAs in their trust list.
- Mac OS X 10.4 with Java for Mac OS X 10.4 Release 5 (February 2007), Mac OS X 10.5 (October 2007), and later versions contain at least one of the required CAs in their trust list.
- Red Hat Enterprise Linux 5 (March 2007), 6, and 7 and CentOS 5, 6, and 7 all contain at least one of the required CAs in their default trusted CA list.
- Java 1.4.2\_12 (May 2006), 5 Update 2 (March 2005), and all later versions, including Java 6 (December 2006), 7, and 8, contain at least one of the required CAs in their default trusted CA list.

When accessing the Lambda management console or Lambda API endpoints, whether through browsers or programmatically, you will need to ensure your client machines support any of the following CAs:

- Amazon Root CA 1
- Starfield Services Root Certificate Authority - G2
- Starfield Class 2 Certification Authority

Root certificates from the first two authorities are available from [Amazon trust services](https://www.amazontrust.com/repository/), but keeping your computer up-to-date is the more straightforward solution. To learn more about ACM-provided certificates, see [Amazon Web Services Certificate Manager FAQs.](http://aws.amazon.com/certificate-manager/faqs/#certificates)

## Operations (88)

- [`AddLayerVersionPermission`](operations/AddLayerVersionPermission.md) — Adds permissions to the resource-based policy of a version of an [Lambda layer](https://docs.aws.amazon.com/lambda/latest/dg/configuration-layers.html).
- [`AddPermission`](operations/AddPermission.md) — Grants a [principal](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_elements_principal.html#Principal_specifying) permission to use a function.
- [`CheckpointDurableExecution`](operations/CheckpointDurableExecution.md) — Saves the progress of a [durable function](https://docs.aws.amazon.com/lambda/latest/dg/durable-functions.html) execution during runtime.
- [`CreateAlias`](operations/CreateAlias.md) — Creates an [alias](https://docs.aws.amazon.com/lambda/latest/dg/configuration-aliases.html) for a Lambda Event Function version.
- [`CreateCapacityProvider`](operations/CreateCapacityProvider.md) — Creates a capacity provider that manages compute resources for Lambda Event Functions
- [`CreateCodeSigningConfig`](operations/CreateCodeSigningConfig.md) — Creates a code signing configuration.
- [`CreateEventSourceMapping`](operations/CreateEventSourceMapping.md) — Creates a mapping between an event source and an Lambda Event Function.
- [`CreateFunction`](operations/CreateFunction.md) — Creates a Lambda Event Function.
- [`CreateFunctionUrlConfig`](operations/CreateFunctionUrlConfig.md) — Creates a Lambda function URL with the specified configuration parameters.
- [`DeleteAlias`](operations/DeleteAlias.md) — Deletes a Lambda Event Function [alias](https://docs.aws.amazon.com/lambda/latest/dg/configuration-aliases.html).
- [`DeleteCapacityProvider`](operations/DeleteCapacityProvider.md) — Deletes a capacity provider.
- [`DeleteCodeSigningConfig`](operations/DeleteCodeSigningConfig.md) — Deletes the code signing configuration.
- [`DeleteEventSourceMapping`](operations/DeleteEventSourceMapping.md) — Deletes an [event source mapping](https://docs.aws.amazon.com/lambda/latest/dg/intro-invocation-modes.html).
- [`DeleteFunction`](operations/DeleteFunction.md) — Deletes a Lambda Event Function.
- [`DeleteFunctionCodeSigningConfig`](operations/DeleteFunctionCodeSigningConfig.md) — Removes the code signing configuration from the function.
- [`DeleteFunctionConcurrency`](operations/DeleteFunctionConcurrency.md) — Removes a concurrent execution limit from a Lambda Event Function.
- [`DeleteFunctionEventInvokeConfig`](operations/DeleteFunctionEventInvokeConfig.md) — Deletes the configuration for asynchronous invocation for a function, version, or alias.
- [`DeleteFunctionUrlConfig`](operations/DeleteFunctionUrlConfig.md) — Deletes a Lambda function URL.
- [`DeleteLayerVersion`](operations/DeleteLayerVersion.md) — Deletes a version of an [Lambda layer](https://docs.aws.amazon.com/lambda/latest/dg/configuration-layers.html).
- [`DeleteProvisionedConcurrencyConfig`](operations/DeleteProvisionedConcurrencyConfig.md) — Deletes the provisioned concurrency configuration for a function.
- [`DeleteResourcePolicy`](operations/DeleteResourcePolicy.md) — Deletes a [resource-based policy](https://docs.aws.amazon.com/lambda/latest/dg/access-control-resource-based.html) from a Lambda resource.
- [`GetAccountSettings`](operations/GetAccountSettings.md) — Retrieves details about your account's [limits](https://docs.aws.amazon.com/lambda/latest/dg/limits.html) and usage in an Amazon Web Services Region.
- [`GetAlias`](operations/GetAlias.md) — Returns details about a Lambda Event Function [alias](https://docs.aws.amazon.com/lambda/latest/dg/configuration-aliases.html).
- [`GetCapacityProvider`](operations/GetCapacityProvider.md) — Retrieves information about a specific capacity provider, including its configuration, state, and associated resources.
- [`GetCodeSigningConfig`](operations/GetCodeSigningConfig.md) — Returns information about the specified code signing configuration.
- [`GetDurableExecution`](operations/GetDurableExecution.md) — Retrieves detailed information about a specific [durable execution](https://docs.aws.amazon.com/lambda/latest/dg/durable-functions.html), including its current status, input payload, result or error …
- [`GetDurableExecutionHistory`](operations/GetDurableExecutionHistory.md) — Retrieves the execution history for a [durable execution](https://docs.aws.amazon.com/lambda/latest/dg/durable-functions.html), showing all the steps, callbacks, and events that occurred during the e…
- [`GetDurableExecutionState`](operations/GetDurableExecutionState.md) — Retrieves the current execution state required for the replay process during [durable function](https://docs.aws.amazon.com/lambda/latest/dg/durable-functions.html) execution.
- [`GetEventSourceMapping`](operations/GetEventSourceMapping.md) — Returns details about an event source mapping.
- [`GetFunction`](operations/GetFunction.md) — Returns information about a Lambda Event Function or function version, with a link to download the deployment package that's valid for 10 minutes.
- [`GetFunctionCodeSigningConfig`](operations/GetFunctionCodeSigningConfig.md) — Returns the code signing configuration for the specified function.
- [`GetFunctionConcurrency`](operations/GetFunctionConcurrency.md) — Returns details about the reserved concurrency configuration for a function.
- [`GetFunctionConfiguration`](operations/GetFunctionConfiguration.md) — Returns the version-specific settings of a Lambda Event Function or version.
- [`GetFunctionEventInvokeConfig`](operations/GetFunctionEventInvokeConfig.md) — Retrieves the configuration for asynchronous invocation for a function, version, or alias.
- [`GetFunctionRecursionConfig`](operations/GetFunctionRecursionConfig.md) — Returns your function's [recursive loop detection](https://docs.aws.amazon.com/lambda/latest/dg/invocation-recursion.html) configuration.
- [`GetFunctionScalingConfig`](operations/GetFunctionScalingConfig.md) — Retrieves the scaling configuration for a Lambda Managed Instances function.
- [`GetFunctionUrlConfig`](operations/GetFunctionUrlConfig.md) — Returns details about a Lambda function URL.
- [`GetLayerVersion`](operations/GetLayerVersion.md) — Returns information about a version of an [Lambda layer](https://docs.aws.amazon.com/lambda/latest/dg/configuration-layers.html), with a link to download the layer archive that's valid for 10 minutes.
- [`GetLayerVersionByArn`](operations/GetLayerVersionByArn.md) — Returns information about a version of an [Lambda layer](https://docs.aws.amazon.com/lambda/latest/dg/configuration-layers.html), with a link to download the layer archive that's valid for 10 minutes.
- [`GetLayerVersionPolicy`](operations/GetLayerVersionPolicy.md) — Returns the permission policy for a version of an [Lambda layer](https://docs.aws.amazon.com/lambda/latest/dg/configuration-layers.html).
- [`GetPolicy`](operations/GetPolicy.md) — Returns the [resource-based IAM policy](https://docs.aws.amazon.com/lambda/latest/dg/access-control-resource-based.html) for a function, version, or alias.
- [`GetProvisionedConcurrencyConfig`](operations/GetProvisionedConcurrencyConfig.md) — Retrieves the provisioned concurrency configuration for a function's alias or version.
- [`GetResourcePolicy`](operations/GetResourcePolicy.md) — Retrieves the [resource-based policy](https://docs.aws.amazon.com/lambda/latest/dg/access-control-resource-based.html) attached to a Lambda resource.
- [`GetRuntimeManagementConfig`](operations/GetRuntimeManagementConfig.md) — Retrieves the runtime management configuration for a function's version.
- [`Invoke`](operations/Invoke.md) — Invokes a Lambda Event Function.
- [`InvokeAsync`](operations/InvokeAsync.md) — For asynchronous function invocation, use Invoke.
- [`InvokeWithResponseStream`](operations/InvokeWithResponseStream.md) — Configure your Lambda Event Functions to stream response payloads back to clients.
- [`ListAliases`](operations/ListAliases.md) — Returns a list of [aliases](https://docs.aws.amazon.com/lambda/latest/dg/configuration-aliases.html) for a Lambda Event Function.
- [`ListCapacityProviders`](operations/ListCapacityProviders.md) — Returns a list of capacity providers in your account.
- [`ListCodeSigningConfigs`](operations/ListCodeSigningConfigs.md) — Returns a list of [code signing configurations](https://docs.aws.amazon.com/lambda/latest/dg/configuring-codesigning.html).
- [`ListDurableExecutionsByFunction`](operations/ListDurableExecutionsByFunction.md) — Returns a list of [durable executions](https://docs.aws.amazon.com/lambda/latest/dg/durable-functions.html) for a specified Lambda function.
- [`ListEventSourceMappings`](operations/ListEventSourceMappings.md) — Lists event source mappings.
- [`ListFunctionEventInvokeConfigs`](operations/ListFunctionEventInvokeConfigs.md) — Retrieves a list of configurations for asynchronous invocation for a Lambda Event Function.
- [`ListFunctionUrlConfigs`](operations/ListFunctionUrlConfigs.md) — Returns a list of Lambda function URLs for the specified function.
- [`ListFunctionVersionsByCapacityProvider`](operations/ListFunctionVersionsByCapacityProvider.md) — Returns a list of function versions that are configured to use a specific capacity provider.
- [`ListFunctions`](operations/ListFunctions.md) — Returns a list of Lambda Event Functions, with the version-specific configuration of each.
- [`ListFunctionsByCodeSigningConfig`](operations/ListFunctionsByCodeSigningConfig.md) — List the functions that use the specified code signing configuration.
- [`ListLayerVersions`](operations/ListLayerVersions.md) — Lists the versions of an [Lambda layer](https://docs.aws.amazon.com/lambda/latest/dg/configuration-layers.html).
- [`ListLayers`](operations/ListLayers.md) — Lists [Lambda layers](https://docs.aws.amazon.com/lambda/latest/dg/invocation-layers.html) and shows information about the latest version of each.
- [`ListProvisionedConcurrencyConfigs`](operations/ListProvisionedConcurrencyConfigs.md) — Retrieves a list of provisioned concurrency configurations for a function.
- [`ListTags`](operations/ListTags.md) — Returns a function, event source mapping, or code signing configuration's [tags](https://docs.aws.amazon.com/lambda/latest/dg/tagging.html).
- [`ListVersionsByFunction`](operations/ListVersionsByFunction.md) — Returns a list of [versions](https://docs.aws.amazon.com/lambda/latest/dg/versioning-aliases.html) of a Lambda Event Function, with the version-specific configuration of each.
- [`PublishLayerVersion`](operations/PublishLayerVersion.md) — Creates an [Lambda layer](https://docs.aws.amazon.com/lambda/latest/dg/configuration-layers.html) from a ZIP archive.
- [`PublishVersion`](operations/PublishVersion.md) — Creates a [version](https://docs.aws.amazon.com/lambda/latest/dg/versioning-aliases.html) from the current code and configuration of a Lambda Event Function.
- [`PutFunctionCodeSigningConfig`](operations/PutFunctionCodeSigningConfig.md) — Update the code signing configuration for the function.
- [`PutFunctionConcurrency`](operations/PutFunctionConcurrency.md) — Sets the maximum number of simultaneous executions for a Lambda Event Function, and reserves capacity for that concurrency level.
- [`PutFunctionEventInvokeConfig`](operations/PutFunctionEventInvokeConfig.md) — Configures options for [asynchronous invocation](https://docs.aws.amazon.com/lambda/latest/dg/invocation-async.html) on a function, version, or alias.
- [`PutFunctionRecursionConfig`](operations/PutFunctionRecursionConfig.md) — Sets the [recursive loop detection](https://docs.aws.amazon.com/lambda/latest/dg/invocation-recursion.html) configuration for a Lambda Event Function.
- [`PutFunctionScalingConfig`](operations/PutFunctionScalingConfig.md) — Sets the scaling configuration for a Lambda Managed Instances function.
- [`PutProvisionedConcurrencyConfig`](operations/PutProvisionedConcurrencyConfig.md) — Adds a provisioned concurrency configuration to a function's alias or version.
- [`PutResourcePolicy`](operations/PutResourcePolicy.md) — Adds a [resource-based policy](https://docs.aws.amazon.com/lambda/latest/dg/access-control-resource-based.html) to a Lambda resource.
- [`PutRuntimeManagementConfig`](operations/PutRuntimeManagementConfig.md) — Sets the runtime management configuration for a function's version.
- [`RemoveLayerVersionPermission`](operations/RemoveLayerVersionPermission.md) — Removes a statement from the permissions policy for a version of an [Lambda layer](https://docs.aws.amazon.com/lambda/latest/dg/configuration-layers.html).
- [`RemovePermission`](operations/RemovePermission.md) — Revokes function-use permission from an Amazon Web Services service or another Amazon Web Services account.
- [`SendDurableExecutionCallbackFailure`](operations/SendDurableExecutionCallbackFailure.md) — Sends a failure response for a callback operation in a durable execution.
- [`SendDurableExecutionCallbackHeartbeat`](operations/SendDurableExecutionCallbackHeartbeat.md) — Sends a heartbeat signal for a long-running callback operation to prevent timeout.
- [`SendDurableExecutionCallbackSuccess`](operations/SendDurableExecutionCallbackSuccess.md) — Sends a successful completion response for a callback operation in a durable execution.
- [`StopDurableExecution`](operations/StopDurableExecution.md) — Stops a running [durable execution](https://docs.aws.amazon.com/lambda/latest/dg/durable-functions.html).
- [`TagResource`](operations/TagResource.md) — Adds [tags](https://docs.aws.amazon.com/lambda/latest/dg/tagging.html) to a function, event source mapping, or code signing configuration.
- [`UntagResource`](operations/UntagResource.md) — Removes [tags](https://docs.aws.amazon.com/lambda/latest/dg/tagging.html) from a function, event source mapping, or code signing configuration.
- [`UpdateAlias`](operations/UpdateAlias.md) — Updates the configuration of a Lambda Event Function [alias](https://docs.aws.amazon.com/lambda/latest/dg/configuration-aliases.html).
- [`UpdateCapacityProvider`](operations/UpdateCapacityProvider.md) — Updates the configuration of an existing capacity provider.
- [`UpdateCodeSigningConfig`](operations/UpdateCodeSigningConfig.md) — Update the code signing configuration.
- [`UpdateEventSourceMapping`](operations/UpdateEventSourceMapping.md) — Updates an event source mapping.
- [`UpdateFunctionCode`](operations/UpdateFunctionCode.md) — Updates a Lambda Event Function's code.
- [`UpdateFunctionConfiguration`](operations/UpdateFunctionConfiguration.md) — Modifies the version-specific settings of a Lambda Event Function.
- [`UpdateFunctionEventInvokeConfig`](operations/UpdateFunctionEventInvokeConfig.md) — Updates the configuration for asynchronous invocation for a function, version, or alias.
- [`UpdateFunctionUrlConfig`](operations/UpdateFunctionUrlConfig.md) — Updates the configuration for a function URL of a Lambda Event Function.
