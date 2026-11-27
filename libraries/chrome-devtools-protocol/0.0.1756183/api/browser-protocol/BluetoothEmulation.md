# BluetoothEmulation domain

Chrome DevTools Protocol, browser protocol (tip-of-tree) (protocol 1.3).

**Experimental**

This domain allows configuring virtual Bluetooth devices to test
the web-bluetooth API.

16 methods, 3 events, 9 types.

## Methods

### BluetoothEmulation.enable

Enable the BluetoothEmulation domain.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `state` | [BluetoothEmulation.CentralState](#type-centralstate) | State of the simulated central. |
| `leSupported` | boolean | If the simulated central supports low-energy. |

### BluetoothEmulation.setSimulatedCentralState

Set the state of the simulated central.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `state` | [BluetoothEmulation.CentralState](#type-centralstate) | State of the simulated central. |

### BluetoothEmulation.disable

Disable the BluetoothEmulation domain.

No parameters.

### BluetoothEmulation.simulatePreconnectedPeripheral

Simulates a peripheral with |address|, |name| and |knownServiceUuids|
that has already been connected to the system.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `address` | string |  |
| `name` | string |  |
| `manufacturerData` | array of [BluetoothEmulation.ManufacturerData](#type-manufacturerdata) |  |
| `knownServiceUuids` | array of string |  |

### BluetoothEmulation.simulateAdvertisement

Simulates an advertisement packet described in |entry| being received by
the central.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `entry` | [BluetoothEmulation.ScanEntry](#type-scanentry) |  |

### BluetoothEmulation.simulateGATTOperationResponse

Simulates the response code from the peripheral with |address| for a
GATT operation of |type|. The |code| value follows the HCI Error Codes from
Bluetooth Core Specification Vol 2 Part D 1.3 List Of Error Codes.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `address` | string |  |
| `type` | [BluetoothEmulation.GATTOperationType](#type-gattoperationtype) |  |
| `code` | integer |  |

### BluetoothEmulation.simulateCharacteristicOperationResponse

Simulates the response from the characteristic with |characteristicId| for a
characteristic operation of |type|. The |code| value follows the Error
Codes from Bluetooth Core Specification Vol 3 Part F 3.4.1.1 Error Response.
The |data| is expected to exist when simulating a successful read operation
response.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `characteristicId` | string |  |
| `type` | [BluetoothEmulation.CharacteristicOperationType](#type-characteristicoperationtype) |  |
| `code` | integer |  |
| `data` (optional) | string |  |

### BluetoothEmulation.simulateDescriptorOperationResponse

Simulates the response from the descriptor with |descriptorId| for a
descriptor operation of |type|. The |code| value follows the Error
Codes from Bluetooth Core Specification Vol 3 Part F 3.4.1.1 Error Response.
The |data| is expected to exist when simulating a successful read operation
response.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `descriptorId` | string |  |
| `type` | [BluetoothEmulation.DescriptorOperationType](#type-descriptoroperationtype) |  |
| `code` | integer |  |
| `data` (optional) | string |  |

### BluetoothEmulation.addService

Adds a service with |serviceUuid| to the peripheral with |address|.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `address` | string |  |
| `serviceUuid` | string |  |

**Return object**

| Name | Type | Description |
|---|---|---|
| `serviceId` | string | An identifier that uniquely represents this service. |

### BluetoothEmulation.removeService

Removes the service respresented by |serviceId| from the simulated central.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `serviceId` | string |  |

### BluetoothEmulation.addCharacteristic

Adds a characteristic with |characteristicUuid| and |properties| to the
service represented by |serviceId|.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `serviceId` | string |  |
| `characteristicUuid` | string |  |
| `properties` | [BluetoothEmulation.CharacteristicProperties](#type-characteristicproperties) |  |

**Return object**

| Name | Type | Description |
|---|---|---|
| `characteristicId` | string | An identifier that uniquely represents this characteristic. |

### BluetoothEmulation.removeCharacteristic

Removes the characteristic respresented by |characteristicId| from the
simulated central.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `characteristicId` | string |  |

### BluetoothEmulation.addDescriptor

Adds a descriptor with |descriptorUuid| to the characteristic respresented
by |characteristicId|.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `characteristicId` | string |  |
| `descriptorUuid` | string |  |

**Return object**

| Name | Type | Description |
|---|---|---|
| `descriptorId` | string | An identifier that uniquely represents this descriptor. |

### BluetoothEmulation.removeDescriptor

Removes the descriptor with |descriptorId| from the simulated central.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `descriptorId` | string |  |

### BluetoothEmulation.simulateGATTDisconnection

Simulates a GATT disconnection from the peripheral with |address|.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `address` | string |  |

### BluetoothEmulation.simulateGATTMtuChange

Simulates the ATT MTU exchange procedure from Bluetooth Core Specification
Vol 3 Part F 3.4.2 establishing |mtu| for the connection to the peripheral
with |address|.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `address` | string |  |
| `mtu` | integer |  |

## Events

### BluetoothEmulation.gattOperationReceived

Event for when a GATT operation of |type| to the peripheral with |address|
happened.

**Event parameters**

| Name | Type | Description |
|---|---|---|
| `address` | string |  |
| `type` | [BluetoothEmulation.GATTOperationType](#type-gattoperationtype) |  |

### BluetoothEmulation.characteristicOperationReceived

Event for when a characteristic operation of |type| to the characteristic
respresented by |characteristicId| happened. |data| and |writeType| is
expected to exist when |type| is write.

**Event parameters**

| Name | Type | Description |
|---|---|---|
| `characteristicId` | string |  |
| `type` | [BluetoothEmulation.CharacteristicOperationType](#type-characteristicoperationtype) |  |
| `data` (optional) | string |  |
| `writeType` (optional) | [BluetoothEmulation.CharacteristicWriteType](#type-characteristicwritetype) |  |

### BluetoothEmulation.descriptorOperationReceived

Event for when a descriptor operation of |type| to the descriptor
respresented by |descriptorId| happened. |data| is expected to exist when
|type| is write.

**Event parameters**

| Name | Type | Description |
|---|---|---|
| `descriptorId` | string |  |
| `type` | [BluetoothEmulation.DescriptorOperationType](#type-descriptoroperationtype) |  |
| `data` (optional) | string |  |

## Types

<a id="type-centralstate"></a>
### BluetoothEmulation.CentralState

Indicates the various states of Central.

Type: string

Allowed values: `absent`, `powered-off`, `powered-on`

<a id="type-gattoperationtype"></a>
### BluetoothEmulation.GATTOperationType

Indicates the various types of GATT event.

Type: string

Allowed values: `connection`, `discovery`

<a id="type-characteristicwritetype"></a>
### BluetoothEmulation.CharacteristicWriteType

Indicates the various types of characteristic write.

Type: string

Allowed values: `write-default-deprecated`, `write-with-response`, `write-without-response`

<a id="type-characteristicoperationtype"></a>
### BluetoothEmulation.CharacteristicOperationType

Indicates the various types of characteristic operation.

Type: string

Allowed values: `read`, `write`, `subscribe-to-notifications`, `unsubscribe-from-notifications`

<a id="type-descriptoroperationtype"></a>
### BluetoothEmulation.DescriptorOperationType

Indicates the various types of descriptor operation.

Type: string

Allowed values: `read`, `write`

<a id="type-manufacturerdata"></a>
### BluetoothEmulation.ManufacturerData

Stores the manufacturer data

Type: object

**Properties**

| Name | Type | Description |
|---|---|---|
| `key` | integer | Company identifier https://bitbucket.org/bluetooth-SIG/public/src/main/assigned_numbers/company_identifiers/company_identifiers.yaml https://usb.org/developers |
| `data` | string | Manufacturer-specific data (Encoded as a base64 string when passed over JSON) |

<a id="type-scanrecord"></a>
### BluetoothEmulation.ScanRecord

Stores the byte data of the advertisement packet sent by a Bluetooth device.

Type: object

**Properties**

| Name | Type | Description |
|---|---|---|
| `name` (optional) | string |  |
| `uuids` (optional) | array of string |  |
| `appearance` (optional) | integer | Stores the external appearance description of the device. |
| `txPower` (optional) | integer | Stores the transmission power of a broadcasting device. |
| `manufacturerData` (optional) | array of [BluetoothEmulation.ManufacturerData](#type-manufacturerdata) | Key is the company identifier and the value is an array of bytes of manufacturer specific data. |

<a id="type-scanentry"></a>
### BluetoothEmulation.ScanEntry

Stores the advertisement packet information that is sent by a Bluetooth device.

Type: object

**Properties**

| Name | Type | Description |
|---|---|---|
| `deviceAddress` | string |  |
| `rssi` | integer |  |
| `scanRecord` | [BluetoothEmulation.ScanRecord](#type-scanrecord) |  |

<a id="type-characteristicproperties"></a>
### BluetoothEmulation.CharacteristicProperties

Describes the properties of a characteristic. This follows Bluetooth Core
Specification BT 4.2 Vol 3 Part G 3.3.1. Characteristic Properties.

Type: object

**Properties**

| Name | Type | Description |
|---|---|---|
| `broadcast` (optional) | boolean |  |
| `read` (optional) | boolean |  |
| `writeWithoutResponse` (optional) | boolean |  |
| `write` (optional) | boolean |  |
| `notify` (optional) | boolean |  |
| `indicate` (optional) | boolean |  |
| `authenticatedSignedWrites` (optional) | boolean |  |
| `extendedProperties` (optional) | boolean |  |
