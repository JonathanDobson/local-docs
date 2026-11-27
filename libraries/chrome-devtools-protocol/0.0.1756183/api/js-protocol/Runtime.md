# Runtime domain

Chrome DevTools Protocol, JavaScript / V8 inspector protocol (protocol 1.3).

Runtime domain exposes JavaScript runtime by means of remote evaluation and mirror objects.
Evaluation results are returned as mirror object that expose object type, string representation
and unique identifier that can be used for further object reference. Original objects are
maintained in memory unless they are either explicitly released or are released along with the
other objects in their object group.

23 methods, 8 events, 23 types.

## Methods

### Runtime.awaitPromise

Add handler to promise with given promise object id.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `promiseObjectId` | [Runtime.RemoteObjectId](#type-remoteobjectid) | Identifier of the promise. |
| `returnByValue` (optional) | boolean | Whether the result is expected to be a JSON object that should be sent by value. |
| `generatePreview` (optional) | boolean | Whether preview should be generated for the result. |

**Return object**

| Name | Type | Description |
|---|---|---|
| `result` | [Runtime.RemoteObject](#type-remoteobject) | Promise result. Will contain rejected value if promise was rejected. |
| `exceptionDetails` (optional) | [Runtime.ExceptionDetails](#type-exceptiondetails) | Exception details if stack strace is available. |

### Runtime.callFunctionOn

Calls function with given declaration on the given object. Object group of the result is
inherited from the target object.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `functionDeclaration` | string | Declaration of the function to call. |
| `objectId` (optional) | [Runtime.RemoteObjectId](#type-remoteobjectid) | Identifier of the object to call function on. Either objectId or executionContextId should be specified. |
| `arguments` (optional) | array of [Runtime.CallArgument](#type-callargument) | Call arguments. All call arguments must belong to the same JavaScript world as the target object. |
| `silent` (optional) | boolean | In silent mode exceptions thrown during evaluation are not reported and do not pause execution. Overrides `setPauseOnException` state. |
| `returnByValue` (optional) | boolean | Whether the result is expected to be a JSON object which should be sent by value. Can be overriden by `serializationOptions`. |
| `generatePreview` (optional) | boolean | **Experimental** Whether preview should be generated for the result. |
| `userGesture` (optional) | boolean | Whether execution should be treated as initiated by user in the UI. |
| `awaitPromise` (optional) | boolean | Whether execution should `await` for resulting value and return once awaited promise is resolved. |
| `executionContextId` (optional) | [Runtime.ExecutionContextId](#type-executioncontextid) | Specifies execution context which global object will be used to call function on. Either executionContextId or objectId should be specified. |
| `objectGroup` (optional) | string | Symbolic group name that can be used to release multiple objects. If objectGroup is not specified and objectId is, objectGroup will be inherited from object. |
| `throwOnSideEffect` (optional) | boolean | **Experimental** Whether to throw an exception if side effect cannot be ruled out during evaluation. |
| `uniqueContextId` (optional) | string | **Experimental** An alternative way to specify the execution context to call function on. Compared to contextId that may be reused across processes, this is guaranteed to be system-unique, so it can be used to prevent accidental function call in context different than intended (e.g. as a result of navigation across process boundaries). This is mutually exclusive with `executionContextId`. |
| `serializationOptions` (optional) | [Runtime.SerializationOptions](#type-serializationoptions) | **Experimental** Specifies the result serialization. If provided, overrides `generatePreview` and `returnByValue`. |

**Return object**

| Name | Type | Description |
|---|---|---|
| `result` | [Runtime.RemoteObject](#type-remoteobject) | Call result. |
| `exceptionDetails` (optional) | [Runtime.ExceptionDetails](#type-exceptiondetails) | Exception details. |

### Runtime.compileScript

Compiles expression.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `expression` | string | Expression to compile. |
| `sourceURL` | string | Source url to be set for the script. |
| `persistScript` | boolean | Specifies whether the compiled script should be persisted. |
| `executionContextId` (optional) | [Runtime.ExecutionContextId](#type-executioncontextid) | Specifies in which execution context to perform script run. If the parameter is omitted the evaluation will be performed in the context of the inspected page. |

**Return object**

| Name | Type | Description |
|---|---|---|
| `scriptId` (optional) | [Runtime.ScriptId](#type-scriptid) | Id of the script. |
| `exceptionDetails` (optional) | [Runtime.ExceptionDetails](#type-exceptiondetails) | Exception details. |

### Runtime.disable

Disables reporting of execution contexts creation.

No parameters.

### Runtime.discardConsoleEntries

Discards collected exceptions and console API calls.

No parameters.

### Runtime.enable

Enables reporting of execution contexts creation by means of `executionContextCreated` event.
When the reporting gets enabled the event will be sent immediately for each existing execution
context.

No parameters.

### Runtime.evaluate

Evaluates expression on global object.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `expression` | string | Expression to evaluate. |
| `objectGroup` (optional) | string | Symbolic group name that can be used to release multiple objects. |
| `includeCommandLineAPI` (optional) | boolean | Determines whether Command Line API should be available during the evaluation. |
| `silent` (optional) | boolean | In silent mode exceptions thrown during evaluation are not reported and do not pause execution. Overrides `setPauseOnException` state. |
| `contextId` (optional) | [Runtime.ExecutionContextId](#type-executioncontextid) | Specifies in which execution context to perform evaluation. If the parameter is omitted the evaluation will be performed in the context of the inspected page. This is mutually exclusive with `uniqueContextId`, which offers an alternative way to identify the execution context that is more reliable in a multi-process environment. |
| `returnByValue` (optional) | boolean | Whether the result is expected to be a JSON object that should be sent by value. |
| `generatePreview` (optional) | boolean | **Experimental** Whether preview should be generated for the result. |
| `userGesture` (optional) | boolean | Whether execution should be treated as initiated by user in the UI. |
| `awaitPromise` (optional) | boolean | Whether execution should `await` for resulting value and return once awaited promise is resolved. |
| `throwOnSideEffect` (optional) | boolean | **Experimental** Whether to throw an exception if side effect cannot be ruled out during evaluation. This implies `disableBreaks` below. |
| `timeout` (optional) | [Runtime.TimeDelta](#type-timedelta) | **Experimental** Terminate execution after timing out (number of milliseconds). |
| `disableBreaks` (optional) | boolean | **Experimental** Disable breakpoints during execution. |
| `replMode` (optional) | boolean | **Experimental** Setting this flag to true enables `let` re-declaration and top-level `await`. Note that `let` variables can only be re-declared if they originate from `replMode` themselves. |
| `allowUnsafeEvalBlockedByCSP` (optional) | boolean | **Experimental** The Content Security Policy (CSP) for the target might block 'unsafe-eval' which includes eval(), Function(), setTimeout() and setInterval() when called with non-callable arguments. This flag bypasses CSP for this evaluation and allows unsafe-eval. Defaults to true. |
| `uniqueContextId` (optional) | string | **Experimental** An alternative way to specify the execution context to evaluate in. Compared to contextId that may be reused across processes, this is guaranteed to be system-unique, so it can be used to prevent accidental evaluation of the expression in context different than intended (e.g. as a result of navigation across process boundaries). This is mutually exclusive with `contextId`. |
| `serializationOptions` (optional) | [Runtime.SerializationOptions](#type-serializationoptions) | **Experimental** Specifies the result serialization. If provided, overrides `generatePreview` and `returnByValue`. |

**Return object**

| Name | Type | Description |
|---|---|---|
| `result` | [Runtime.RemoteObject](#type-remoteobject) | Evaluation result. |
| `exceptionDetails` (optional) | [Runtime.ExceptionDetails](#type-exceptiondetails) | Exception details. |

### Runtime.getIsolateId

**Experimental**

Returns the isolate id.

No parameters.

**Return object**

| Name | Type | Description |
|---|---|---|
| `id` | string | The isolate id. |

### Runtime.getHeapUsage

**Experimental**

Returns the JavaScript heap usage.
It is the total usage of the corresponding isolate not scoped to a particular Runtime.

No parameters.

**Return object**

| Name | Type | Description |
|---|---|---|
| `usedSize` | number | Used JavaScript heap size in bytes. |
| `totalSize` | number | Allocated JavaScript heap size in bytes. |
| `embedderHeapUsedSize` | number | Used size in bytes in the embedder's garbage-collected heap. |
| `backingStorageSize` | number | Size in bytes of backing storage for array buffers and external strings. |

### Runtime.getProperties

Returns properties of a given object. Object group of the result is inherited from the target
object.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `objectId` | [Runtime.RemoteObjectId](#type-remoteobjectid) | Identifier of the object to return properties for. |
| `ownProperties` (optional) | boolean | If true, returns properties belonging only to the element itself, not to its prototype chain. |
| `accessorPropertiesOnly` (optional) | boolean | **Experimental** If true, returns accessor properties (with getter/setter) only; internal properties are not returned either. |
| `generatePreview` (optional) | boolean | **Experimental** Whether preview should be generated for the results. |
| `nonIndexedPropertiesOnly` (optional) | boolean | **Experimental** If true, returns non-indexed properties only. |

**Return object**

| Name | Type | Description |
|---|---|---|
| `result` | array of [Runtime.PropertyDescriptor](#type-propertydescriptor) | Object properties. |
| `internalProperties` (optional) | array of [Runtime.InternalPropertyDescriptor](#type-internalpropertydescriptor) | Internal object properties (only of the element itself). |
| `privateProperties` (optional) | array of [Runtime.PrivatePropertyDescriptor](#type-privatepropertydescriptor) | **Experimental** Object private properties. |
| `exceptionDetails` (optional) | [Runtime.ExceptionDetails](#type-exceptiondetails) | Exception details. |

### Runtime.globalLexicalScopeNames

Returns all let, const and class variables from global scope.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `executionContextId` (optional) | [Runtime.ExecutionContextId](#type-executioncontextid) | Specifies in which execution context to lookup global scope variables. |

**Return object**

| Name | Type | Description |
|---|---|---|
| `names` | array of string |  |

### Runtime.queryObjects

**Parameters**

| Name | Type | Description |
|---|---|---|
| `prototypeObjectId` | [Runtime.RemoteObjectId](#type-remoteobjectid) | Identifier of the prototype to return objects for. |
| `objectGroup` (optional) | string | Symbolic group name that can be used to release the results. |

**Return object**

| Name | Type | Description |
|---|---|---|
| `objects` | [Runtime.RemoteObject](#type-remoteobject) | Array with objects. |

### Runtime.releaseObject

Releases remote object with given id.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `objectId` | [Runtime.RemoteObjectId](#type-remoteobjectid) | Identifier of the object to release. |

### Runtime.releaseObjectGroup

Releases all remote objects that belong to a given group.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `objectGroup` | string | Symbolic object group name. |

### Runtime.runIfWaitingForDebugger

Tells inspected instance to run if it was waiting for debugger to attach.

No parameters.

### Runtime.runScript

Runs script with given id in a given context.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `scriptId` | [Runtime.ScriptId](#type-scriptid) | Id of the script to run. |
| `executionContextId` (optional) | [Runtime.ExecutionContextId](#type-executioncontextid) | Specifies in which execution context to perform script run. If the parameter is omitted the evaluation will be performed in the context of the inspected page. |
| `objectGroup` (optional) | string | Symbolic group name that can be used to release multiple objects. |
| `silent` (optional) | boolean | In silent mode exceptions thrown during evaluation are not reported and do not pause execution. Overrides `setPauseOnException` state. |
| `includeCommandLineAPI` (optional) | boolean | Determines whether Command Line API should be available during the evaluation. |
| `returnByValue` (optional) | boolean | Whether the result is expected to be a JSON object which should be sent by value. |
| `generatePreview` (optional) | boolean | Whether preview should be generated for the result. |
| `awaitPromise` (optional) | boolean | Whether execution should `await` for resulting value and return once awaited promise is resolved. |

**Return object**

| Name | Type | Description |
|---|---|---|
| `result` | [Runtime.RemoteObject](#type-remoteobject) | Run result. |
| `exceptionDetails` (optional) | [Runtime.ExceptionDetails](#type-exceptiondetails) | Exception details. |

### Runtime.setAsyncCallStackDepth

Enables or disables async call stacks tracking.

Implemented by the `Debugger` domain.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `maxDepth` | integer | Maximum depth of async call stacks. Setting to `0` will effectively disable collecting async call stacks (default). |

### Runtime.setCustomObjectFormatterEnabled

**Experimental**

**Parameters**

| Name | Type | Description |
|---|---|---|
| `enabled` | boolean |  |

### Runtime.setMaxCallStackSizeToCapture

**Experimental**

**Parameters**

| Name | Type | Description |
|---|---|---|
| `size` | integer |  |

### Runtime.terminateExecution

**Experimental**

Terminate current or next JavaScript execution.
Will cancel the termination when the outer-most script execution ends.

No parameters.

### Runtime.addBinding

If executionContextId is empty, adds binding with the given name on the
global objects of all inspected contexts, including those created later,
bindings survive reloads.
Binding function takes exactly one argument, this argument should be string,
in case of any other input, function throws an exception.
Each binding function call produces Runtime.bindingCalled notification.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `name` | string |  |
| `executionContextId` (optional) | [Runtime.ExecutionContextId](#type-executioncontextid) | **Experimental** · **Deprecated** If specified, the binding would only be exposed to the specified execution context. If omitted and `executionContextName` is not set, the binding is exposed to all execution contexts of the target. This parameter is mutually exclusive with `executionContextName`. Deprecated in favor of `executionContextName` due to an unclear use case and bugs in implementation (crbug.com/1169639). `executionContextId` will be removed in the future. |
| `executionContextName` (optional) | string | If specified, the binding is exposed to the executionContext with matching name, even for contexts created after the binding is added. See also `ExecutionContext.name` and `worldName` parameter to `Page.addScriptToEvaluateOnNewDocument`. This parameter is mutually exclusive with `executionContextId`. |

### Runtime.removeBinding

This method does not remove binding function from global object but
unsubscribes current runtime agent from Runtime.bindingCalled notifications.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `name` | string |  |

### Runtime.getExceptionDetails

**Experimental**

This method tries to lookup and populate exception details for a
JavaScript Error object.
Note that the stackTrace portion of the resulting exceptionDetails will
only be populated if the Runtime domain was enabled at the time when the
Error was thrown.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `errorObjectId` | [Runtime.RemoteObjectId](#type-remoteobjectid) | The error object for which to resolve the exception details. |

**Return object**

| Name | Type | Description |
|---|---|---|
| `exceptionDetails` (optional) | [Runtime.ExceptionDetails](#type-exceptiondetails) |  |

## Events

### Runtime.bindingCalled

**Experimental**

Notification is issued every time when binding is called.

**Event parameters**

| Name | Type | Description |
|---|---|---|
| `name` | string |  |
| `payload` | string |  |
| `executionContextId` | [Runtime.ExecutionContextId](#type-executioncontextid) | Identifier of the context where the call was made. |

### Runtime.consoleAPICalled

Issued when console API was called.

**Event parameters**

| Name | Type | Description |
|---|---|---|
| `type` | string | Type of the call. Allowed values: `log`, `debug`, `info`, `error`, `warning`, `dir`, `dirxml`, `table`, `trace`, `clear`, `startGroup`, `startGroupCollapsed`, `endGroup`, `assert`, `profile`, `profileEnd`, `count`, `timeEnd` |
| `args` | array of [Runtime.RemoteObject](#type-remoteobject) | Call arguments. |
| `executionContextId` | [Runtime.ExecutionContextId](#type-executioncontextid) | Identifier of the context where the call was made. |
| `timestamp` | [Runtime.Timestamp](#type-timestamp) | Call timestamp. |
| `stackTrace` (optional) | [Runtime.StackTrace](#type-stacktrace) | Stack trace captured when the call was made. The async stack chain is automatically reported for the following call types: `assert`, `error`, `trace`, `warning`. For other types the async call chain can be retrieved using `Debugger.getStackTrace` and `stackTrace.parentId` field. |
| `context` (optional) | string | **Experimental** Console context descriptor for calls on non-default console context (not console.*): 'anonymous#unique-logger-id' for call on unnamed context, 'name#unique-logger-id' for call on named context. |

### Runtime.exceptionRevoked

Issued when unhandled exception was revoked.

**Event parameters**

| Name | Type | Description |
|---|---|---|
| `reason` | string | Reason describing why exception was revoked. |
| `exceptionId` | integer | The id of revoked exception, as reported in `exceptionThrown`. |

### Runtime.exceptionThrown

Issued when exception was thrown and unhandled.

**Event parameters**

| Name | Type | Description |
|---|---|---|
| `timestamp` | [Runtime.Timestamp](#type-timestamp) | Timestamp of the exception. |
| `exceptionDetails` | [Runtime.ExceptionDetails](#type-exceptiondetails) |  |

### Runtime.executionContextCreated

Issued when new execution context is created.

**Event parameters**

| Name | Type | Description |
|---|---|---|
| `context` | [Runtime.ExecutionContextDescription](#type-executioncontextdescription) | A newly created execution context. |

### Runtime.executionContextDestroyed

Issued when execution context is destroyed.

**Event parameters**

| Name | Type | Description |
|---|---|---|
| `executionContextId` | [Runtime.ExecutionContextId](#type-executioncontextid) | **Deprecated** Id of the destroyed context |
| `executionContextUniqueId` | string | **Experimental** Unique Id of the destroyed context |

### Runtime.executionContextsCleared

Issued when all executionContexts were cleared in browser

### Runtime.inspectRequested

Issued when object should be inspected (for example, as a result of inspect() command line API
call).

**Event parameters**

| Name | Type | Description |
|---|---|---|
| `object` | [Runtime.RemoteObject](#type-remoteobject) |  |
| `hints` | object |  |
| `executionContextId` (optional) | [Runtime.ExecutionContextId](#type-executioncontextid) | **Experimental** Identifier of the context where the call was made. |

## Types

<a id="type-scriptid"></a>
### Runtime.ScriptId

Unique script identifier.

Type: string

<a id="type-serializationoptions"></a>
### Runtime.SerializationOptions

Represents options for serialization. Overrides `generatePreview` and `returnByValue`.

Type: object

**Properties**

| Name | Type | Description |
|---|---|---|
| `serialization` | string | Allowed values: `deep`, `json`, `idOnly` |
| `maxDepth` (optional) | integer | Deep serialization depth. Default is full depth. Respected only in `deep` serialization mode. |
| `additionalParameters` (optional) | object | Embedder-specific parameters. For example if connected to V8 in Chrome these control DOM serialization via `maxNodeDepth: integer` and `includeShadowTree: "none" \| "open" \| "all"`. Values can be only of type string or integer. |

<a id="type-deepserializedvalue"></a>
### Runtime.DeepSerializedValue

Represents deep serialized value.

Type: object

**Properties**

| Name | Type | Description |
|---|---|---|
| `type` | string | Allowed values: `undefined`, `null`, `string`, `number`, `boolean`, `bigint`, `regexp`, `date`, `symbol`, `array`, `object`, `function`, `map`, `set`, `weakmap`, `weakset`, `error`, `proxy`, `promise`, `typedarray`, `arraybuffer`, `node`, `window`, `generator` |
| `value` (optional) | any |  |
| `objectId` (optional) | string |  |
| `weakLocalObjectReference` (optional) | integer | Set if value reference met more then once during serialization. In such case, value is provided only to one of the serialized values. Unique per value in the scope of one CDP call. |

<a id="type-remoteobjectid"></a>
### Runtime.RemoteObjectId

Unique object identifier.

Type: string

<a id="type-unserializablevalue"></a>
### Runtime.UnserializableValue

Primitive value which cannot be JSON-stringified. Includes values `-0`, `NaN`, `Infinity`,
`-Infinity`, and bigint literals.

Type: string

<a id="type-remoteobject"></a>
### Runtime.RemoteObject

Mirror object referencing original JavaScript object.

Type: object

**Properties**

| Name | Type | Description |
|---|---|---|
| `type` | string | Object type. Allowed values: `object`, `function`, `undefined`, `string`, `number`, `boolean`, `symbol`, `bigint` |
| `subtype` (optional) | string | Object subtype hint. Specified for `object` type values only. NOTE: If you change anything here, make sure to also update `subtype` in `ObjectPreview` and `PropertyPreview` below. Allowed values: `array`, `null`, `node`, `regexp`, `date`, `map`, `set`, `weakmap`, `weakset`, `iterator`, `generator`, `error`, `proxy`, `promise`, `typedarray`, `arraybuffer`, `dataview`, `webassemblymemory`, `wasmvalue`, `deferredmodule`, `trustedtype` |
| `className` (optional) | string | Object class (constructor) name. Specified for `object` type values only. |
| `value` (optional) | any | Remote object value in case of primitive values or JSON values (if it was requested). Not set in `deep` serialization mode, see `deepSerializedValue`. |
| `unserializableValue` (optional) | [Runtime.UnserializableValue](#type-unserializablevalue) | Primitive value which can not be JSON-stringified does not have `value`, but gets this property. Not set in `deep` serialization mode, see `deepSerializedValue`. |
| `description` (optional) | string | String representation of the object. |
| `deepSerializedValue` (optional) | [Runtime.DeepSerializedValue](#type-deepserializedvalue) | **Experimental** Deep serialized value. |
| `objectId` (optional) | [Runtime.RemoteObjectId](#type-remoteobjectid) | Unique object identifier (for non-primitive values). |
| `preview` (optional) | [Runtime.ObjectPreview](#type-objectpreview) | **Experimental** Preview containing abbreviated property values. Specified for `object` type values only. |
| `customPreview` (optional) | [Runtime.CustomPreview](#type-custompreview) | **Experimental** |

<a id="type-custompreview"></a>
### Runtime.CustomPreview

**Experimental**

Type: object

**Properties**

| Name | Type | Description |
|---|---|---|
| `header` | string | The JSON-stringified result of formatter.header(object, config) call. It contains json ML array that represents RemoteObject. |
| `bodyGetterId` (optional) | [Runtime.RemoteObjectId](#type-remoteobjectid) | If formatter returns true as a result of formatter.hasBody call then bodyGetterId will contain RemoteObjectId for the function that returns result of formatter.body(object, config) call. The result value is json ML array. |

<a id="type-objectpreview"></a>
### Runtime.ObjectPreview

**Experimental**

Object containing abbreviated remote object value.

Type: object

**Properties**

| Name | Type | Description |
|---|---|---|
| `type` | string | Object type. Allowed values: `object`, `function`, `undefined`, `string`, `number`, `boolean`, `symbol`, `bigint` |
| `subtype` (optional) | string | Object subtype hint. Specified for `object` type values only. Allowed values: `array`, `null`, `node`, `regexp`, `date`, `map`, `set`, `weakmap`, `weakset`, `iterator`, `generator`, `error`, `proxy`, `promise`, `typedarray`, `arraybuffer`, `dataview`, `webassemblymemory`, `wasmvalue`, `deferredmodule`, `trustedtype` |
| `description` (optional) | string | String representation of the object. |
| `overflow` | boolean | True iff some of the properties or entries of the original object did not fit. |
| `properties` | array of [Runtime.PropertyPreview](#type-propertypreview) | List of the properties. |
| `entries` (optional) | array of [Runtime.EntryPreview](#type-entrypreview) | List of the entries. Specified for `map` and `set` subtype values only. |

<a id="type-propertypreview"></a>
### Runtime.PropertyPreview

**Experimental**

Type: object

**Properties**

| Name | Type | Description |
|---|---|---|
| `name` | string | Property name. |
| `type` | string | Object type. Accessor means that the property itself is an accessor property. Allowed values: `object`, `function`, `undefined`, `string`, `number`, `boolean`, `symbol`, `accessor`, `bigint` |
| `value` (optional) | string | User-friendly property value string. |
| `valuePreview` (optional) | [Runtime.ObjectPreview](#type-objectpreview) | Nested value preview. |
| `subtype` (optional) | string | Object subtype hint. Specified for `object` type values only. Allowed values: `array`, `null`, `node`, `regexp`, `date`, `map`, `set`, `weakmap`, `weakset`, `iterator`, `generator`, `error`, `proxy`, `promise`, `typedarray`, `arraybuffer`, `dataview`, `webassemblymemory`, `wasmvalue`, `deferredmodule`, `trustedtype` |

<a id="type-entrypreview"></a>
### Runtime.EntryPreview

**Experimental**

Type: object

**Properties**

| Name | Type | Description |
|---|---|---|
| `key` (optional) | [Runtime.ObjectPreview](#type-objectpreview) | Preview of the key. Specified for map-like collection entries. |
| `value` | [Runtime.ObjectPreview](#type-objectpreview) | Preview of the value. |

<a id="type-propertydescriptor"></a>
### Runtime.PropertyDescriptor

Object property descriptor.

Type: object

**Properties**

| Name | Type | Description |
|---|---|---|
| `name` | string | Property name or symbol description. |
| `value` (optional) | [Runtime.RemoteObject](#type-remoteobject) | The value associated with the property. |
| `writable` (optional) | boolean | True if the value associated with the property may be changed (data descriptors only). |
| `get` (optional) | [Runtime.RemoteObject](#type-remoteobject) | A function which serves as a getter for the property, or `undefined` if there is no getter (accessor descriptors only). |
| `set` (optional) | [Runtime.RemoteObject](#type-remoteobject) | A function which serves as a setter for the property, or `undefined` if there is no setter (accessor descriptors only). |
| `configurable` | boolean | True if the type of this property descriptor may be changed and if the property may be deleted from the corresponding object. |
| `enumerable` | boolean | True if this property shows up during enumeration of the properties on the corresponding object. |
| `wasThrown` (optional) | boolean | True if the result was thrown during the evaluation. |
| `isOwn` (optional) | boolean | True if the property is owned for the object. |
| `symbol` (optional) | [Runtime.RemoteObject](#type-remoteobject) | Property symbol object, if the property is of the `symbol` type. |

<a id="type-internalpropertydescriptor"></a>
### Runtime.InternalPropertyDescriptor

Object internal property descriptor. This property isn't normally visible in JavaScript code.

Type: object

**Properties**

| Name | Type | Description |
|---|---|---|
| `name` | string | Conventional property name. |
| `value` (optional) | [Runtime.RemoteObject](#type-remoteobject) | The value associated with the property. |

<a id="type-privatepropertydescriptor"></a>
### Runtime.PrivatePropertyDescriptor

**Experimental**

Object private field descriptor.

Type: object

**Properties**

| Name | Type | Description |
|---|---|---|
| `name` | string | Private property name. |
| `value` (optional) | [Runtime.RemoteObject](#type-remoteobject) | The value associated with the private property. |
| `get` (optional) | [Runtime.RemoteObject](#type-remoteobject) | A function which serves as a getter for the private property, or `undefined` if there is no getter (accessor descriptors only). |
| `set` (optional) | [Runtime.RemoteObject](#type-remoteobject) | A function which serves as a setter for the private property, or `undefined` if there is no setter (accessor descriptors only). |

<a id="type-callargument"></a>
### Runtime.CallArgument

Represents function call argument. Either remote object id `objectId`, primitive `value`,
unserializable primitive value or neither of (for undefined) them should be specified.

Type: object

**Properties**

| Name | Type | Description |
|---|---|---|
| `value` (optional) | any | Primitive value or serializable javascript object. |
| `unserializableValue` (optional) | [Runtime.UnserializableValue](#type-unserializablevalue) | Primitive value which can not be JSON-stringified. |
| `objectId` (optional) | [Runtime.RemoteObjectId](#type-remoteobjectid) | Remote object handle. |

<a id="type-executioncontextid"></a>
### Runtime.ExecutionContextId

Id of an execution context.

Type: integer

<a id="type-executioncontextdescription"></a>
### Runtime.ExecutionContextDescription

Description of an isolated world.

Type: object

**Properties**

| Name | Type | Description |
|---|---|---|
| `id` | [Runtime.ExecutionContextId](#type-executioncontextid) | Unique id of the execution context. It can be used to specify in which execution context script evaluation should be performed. |
| `origin` | string | Execution context origin. |
| `name` | string | Human readable name describing given context. |
| `uniqueId` | string | **Experimental** A system-unique execution context identifier. Unlike the id, this is unique across multiple processes, so can be reliably used to identify specific context while backend performs a cross-process navigation. |
| `auxData` (optional) | object | Embedder-specific auxiliary data likely matching {isDefault: boolean, type: 'default'\|'isolated'\|'worker', frameId: string} |

<a id="type-exceptiondetails"></a>
### Runtime.ExceptionDetails

Detailed information about exception (or error) that was thrown during script compilation or
execution.

Type: object

**Properties**

| Name | Type | Description |
|---|---|---|
| `exceptionId` | integer | Exception id. |
| `text` | string | Exception text, which should be used together with exception object when available. |
| `lineNumber` | integer | Line number of the exception location (0-based). |
| `columnNumber` | integer | Column number of the exception location (0-based). |
| `scriptId` (optional) | [Runtime.ScriptId](#type-scriptid) | Script ID of the exception location. |
| `url` (optional) | string | URL of the exception location, to be used when the script was not reported. |
| `stackTrace` (optional) | [Runtime.StackTrace](#type-stacktrace) | JavaScript stack trace if available. |
| `exception` (optional) | [Runtime.RemoteObject](#type-remoteobject) | Exception object if available. |
| `executionContextId` (optional) | [Runtime.ExecutionContextId](#type-executioncontextid) | Identifier of the context where exception happened. |
| `exceptionMetaData` (optional) | object | **Experimental** Dictionary with entries of meta data that the client associated with this exception, such as information about associated network requests, etc. |

<a id="type-timestamp"></a>
### Runtime.Timestamp

Number of milliseconds since epoch.

Type: number

<a id="type-timedelta"></a>
### Runtime.TimeDelta

Number of milliseconds.

Type: number

<a id="type-callframe"></a>
### Runtime.CallFrame

Stack entry for runtime errors and assertions.

Type: object

**Properties**

| Name | Type | Description |
|---|---|---|
| `functionName` | string | JavaScript function name. |
| `scriptId` | [Runtime.ScriptId](#type-scriptid) | JavaScript script id. |
| `url` | string | JavaScript script name or url. |
| `lineNumber` | integer | JavaScript script line number (0-based). |
| `columnNumber` | integer | JavaScript script column number (0-based). |

<a id="type-stacktrace"></a>
### Runtime.StackTrace

Call frames for assertions or error messages.

Type: object

**Properties**

| Name | Type | Description |
|---|---|---|
| `description` (optional) | string | String label of this stack trace. For async traces this may be a name of the function that initiated the async call. |
| `callFrames` | array of [Runtime.CallFrame](#type-callframe) | JavaScript function name. |
| `parent` (optional) | [Runtime.StackTrace](#type-stacktrace) | Asynchronous JavaScript stack trace that preceded this stack, if available. |
| `parentId` (optional) | [Runtime.StackTraceId](#type-stacktraceid) | **Experimental** Asynchronous JavaScript stack trace that preceded this stack, if available. |

<a id="type-uniquedebuggerid"></a>
### Runtime.UniqueDebuggerId

**Experimental**

Unique identifier of current debugger.

Type: string

<a id="type-stacktraceid"></a>
### Runtime.StackTraceId

**Experimental**

If `debuggerId` is set stack trace comes from another debugger and can be resolved there. This
allows to track cross-debugger calls. See `Runtime.StackTrace` and `Debugger.paused` for usages.

Type: object

**Properties**

| Name | Type | Description |
|---|---|---|
| `id` | string |  |
| `debuggerId` (optional) | [Runtime.UniqueDebuggerId](#type-uniquedebuggerid) |  |
