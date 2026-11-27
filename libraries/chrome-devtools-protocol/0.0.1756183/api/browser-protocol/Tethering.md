# Tethering domain

Chrome DevTools Protocol, browser protocol (tip-of-tree) (protocol 1.3).

**Experimental**

The Tethering domain defines methods and events for browser port binding.

2 methods, 1 events, 0 types.

## Methods

### Tethering.bind

Request browser port binding.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `port` | integer | Port number to bind. |

### Tethering.unbind

Request browser port unbinding.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `port` | integer | Port number to unbind. |

## Events

### Tethering.accepted

Informs that port was successfully bound and got a specified connection id.

**Event parameters**

| Name | Type | Description |
|---|---|---|
| `port` | integer | Port number that was successfully bound. |
| `connectionId` | string | Connection id to be used. |
