# Console domain

Chrome DevTools Protocol, JavaScript / V8 inspector protocol (protocol 1.3).

**Deprecated**

This domain is deprecated - use Runtime or Log instead.

Depends on: [Runtime](Runtime.md)

3 methods, 1 events, 1 types.

## Methods

### Console.clearMessages

Does nothing.

No parameters.

### Console.disable

Disables console domain, prevents further console messages from being reported to the client.

No parameters.

### Console.enable

Enables console domain, sends the messages collected so far to the client by means of the
`messageAdded` notification.

No parameters.

## Events

### Console.messageAdded

Issued when new console message is added.

**Event parameters**

| Name | Type | Description |
|---|---|---|
| `message` | [Console.ConsoleMessage](#type-consolemessage) | Console message that has been added. |

## Types

<a id="type-consolemessage"></a>
### Console.ConsoleMessage

Console message.

Type: object

**Properties**

| Name | Type | Description |
|---|---|---|
| `source` | string | Message source. Allowed values: `xml`, `javascript`, `network`, `console-api`, `storage`, `appcache`, `rendering`, `security`, `other`, `deprecation`, `worker` |
| `level` | string | Message severity. Allowed values: `log`, `warning`, `error`, `debug`, `info` |
| `text` | string | Message text. |
| `url` (optional) | string | URL of the message origin. |
| `line` (optional) | integer | Line number in the resource that generated this message (1-based). |
| `column` (optional) | integer | Column number in the resource that generated this message (1-based). |
