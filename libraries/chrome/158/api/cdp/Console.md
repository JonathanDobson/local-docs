# Console domain *(deprecated)*

This domain is deprecated - use Runtime or Log instead.

Depends on: [Runtime](Runtime.md)

Methods are called as `Console.<command>` and events arrive as `Console.<event>`.

## Commands

### Console.clearMessages

Does nothing.

### Console.disable

Disables console domain, prevents further console messages from being reported to the client.

### Console.enable

Enables console domain, sends the messages collected so far to the client by means of the `messageAdded` notification.

## Events

### Console.messageAdded

Issued when new console message is added.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `message` | [ConsoleMessage](#type-consolemessage) | Console message that has been added. |

## Types

<a id="type-consolemessage"></a>
### Console.ConsoleMessage

Type: object

Console message.

**Properties**

| Name | Type | Description |
|---|---|---|
| `source` | enum: `xml`, `javascript`, `network`, `console-api`, `storage`, `appcache`, `rendering`, `security`, `other`, `deprecation`, `worker` | Message source. |
| `level` | enum: `log`, `warning`, `error`, `debug`, `info` | Message severity. |
| `text` | string | Message text. |
| `url` (optional) | string | URL of the message origin. |
| `line` (optional) | integer | Line number in the resource that generated this message (1-based). |
| `column` (optional) | integer | Column number in the resource that generated this message (1-based). |

