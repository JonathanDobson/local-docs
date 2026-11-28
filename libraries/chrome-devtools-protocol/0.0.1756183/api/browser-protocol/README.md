# Chrome DevTools Protocol — browser protocol (tip-of-tree)

Generated from `browser_protocol.json` (protocol version 1.3). One page per domain.

| Domain | Status | Methods | Events | Types | Summary |
|---|---|---|---|---|---|
| [Accessibility](Accessibility.md) | **Experimental** | 8 | 2 | 10 |  |
| [Ads](Ads.md) | **Experimental** | 2 | 0 | 3 | A domain for ad-related metrics and data. |
| [Animation](Animation.md) | **Experimental** | 10 | 4 | 5 |  |
| [Audits](Audits.md) | **Experimental** | 4 | 1 | 70 | Audits domain allows investigation of page violations and possible improvements. |
| [Autofill](Autofill.md) | **Experimental** | 4 | 1 | 7 | Defines commands and events for Autofill. |
| [BackgroundService](BackgroundService.md) | **Experimental** | 4 | 2 | 3 | Defines events for background web platform features. |
| [BluetoothEmulation](BluetoothEmulation.md) | **Experimental** | 16 | 3 | 9 | This domain allows configuring virtual Bluetooth devices to test the web-bluetooth API. |
| [Browser](Browser.md) | stable | 21 | 2 | 10 | The Browser domain defines methods and events for browser managing. |
| [CSS](CSS.md) | **Experimental** | 40 | 6 | 46 | This domain exposes CSS read/write operations |
| [CacheStorage](CacheStorage.md) | **Experimental** | 5 | 0 | 6 |  |
| [Cast](Cast.md) | **Experimental** | 6 | 2 | 1 | A domain for interacting with Cast, Presentation API, and Remote Playback API functionalities. |
| [CrashReportContext](CrashReportContext.md) | **Experimental** | 1 | 0 | 1 | This domain exposes the current state of the CrashReportContext API. |
| [DOM](DOM.md) | stable | 57 | 19 | 18 | This domain exposes DOM read/write operations |
| [DOMDebugger](DOMDebugger.md) | stable | 10 | 0 | 3 | DOM debugging allows setting breakpoints on particular DOM operations and events |
| [DOMSnapshot](DOMSnapshot.md) | **Experimental** | 4 | 0 | 15 | This domain facilitates obtaining document snapshots with DOM, layout, and style information. |
| [DOMStorage](DOMStorage.md) | **Experimental** | 6 | 4 | 3 | Query and modify DOM storage. |
| [DeviceAccess](DeviceAccess.md) | **Experimental** | 4 | 1 | 3 |  |
| [DeviceOrientation](DeviceOrientation.md) | **Experimental** | 2 | 0 | 0 |  |
| [DigitalCredentials](DigitalCredentials.md) | **Experimental** | 1 | 0 | 1 | This domain allows interacting with the Digital Credentials API for automation. |
| [Emulation](Emulation.md) | stable | 48 | 2 | 21 | This domain emulates different environments for the page. |
| [EventBreakpoints](EventBreakpoints.md) | **Experimental** | 3 | 0 | 0 | EventBreakpoints permits setting JavaScript breakpoints on operations and events occurring in native code invoked from JavaScript |
| [Extensions](Extensions.md) | **Experimental** | 8 | 0 | 2 | Defines commands and events for browser extensions. |
| [FedCm](FedCm.md) | **Experimental** | 7 | 2 | 5 | This domain allows interacting with the FedCM dialog. |
| [Fetch](Fetch.md) | stable | 9 | 2 | 6 | A domain for letting clients substitute browser's network layer with client code. |
| [FileSystem](FileSystem.md) | **Experimental** | 1 | 0 | 3 |  |
| [FindInPage](FindInPage.md) | **Experimental** | 4 | 0 | 0 | This domain provides commands to trigger the "Find in page" feature. |
| [HeadlessExperimental](HeadlessExperimental.md) | **Experimental** | 3 | 0 | 1 | This domain provides experimental commands only supported in headless mode. |
| [IO](IO.md) | stable | 3 | 0 | 1 | Input/Output operations for streams produced by DevTools. |
| [IndexedDB](IndexedDB.md) | **Experimental** | 9 | 0 | 7 |  |
| [Input](Input.md) | stable | 13 | 1 | 6 |  |
| [Inspector](Inspector.md) | **Experimental** | 2 | 4 | 0 |  |
| [LayerTree](LayerTree.md) | **Experimental** | 9 | 2 | 7 |  |
| [Log](Log.md) | stable | 5 | 1 | 2 | Provides access to log entries. |
| [Media](Media.md) | **Experimental** | 2 | 5 | 8 | This domain allows detailed inspection of media elements. |
| [Memory](Memory.md) | **Experimental** | 11 | 0 | 5 |  |
| [Network](Network.md) | stable | 35 | 43 | 89 | Network domain allows tracking network activities of the page |
| [Overlay](Overlay.md) | **Experimental** | 31 | 6 | 24 | This domain provides various functionality related to drawing atop the inspected page. |
| [PWA](PWA.md) | **Experimental** | 7 | 0 | 3 | This domain allows interacting with the browser to control PWAs. |
| [Page](Page.md) | stable | 67 | 28 | 59 | Actions and events related to the inspected page belong to the page domain. |
| [Performance](Performance.md) | stable | 4 | 1 | 1 |  |
| [PerformanceTimeline](PerformanceTimeline.md) | **Experimental** | 1 | 1 | 4 | Reporting of performance timeline events, as specified in https://w3c.github.io/performance-timeline/#dom-performanceobserver. |
| [Preload](Preload.md) | **Experimental** | 2 | 6 | 12 |  |
| [Security](Security.md) | stable | 5 | 3 | 10 |  |
| [ServiceWorker](ServiceWorker.md) | **Experimental** | 12 | 3 | 11 |  |
| [SmartCardEmulation](SmartCardEmulation.md) | **Experimental** | 12 | 14 | 9 |  |
| [Storage](Storage.md) | **Experimental** | 27 | 7 | 9 |  |
| [SystemInfo](SystemInfo.md) | **Experimental** | 3 | 0 | 8 | The SystemInfo domain defines methods and events for querying low-level system information. |
| [Target](Target.md) | stable | 19 | 7 | 7 | Supports additional targets discovery and allows to attach to them. |
| [Tethering](Tethering.md) | **Experimental** | 2 | 1 | 0 | The Tethering domain defines methods and events for browser port binding. |
| [Tracing](Tracing.md) | stable | 6 | 3 | 6 |  |
| [WebAudio](WebAudio.md) | **Experimental** | 3 | 13 | 13 | This domain allows inspection of Web Audio API |
| [WebAuthn](WebAuthn.md) | **Experimental** | 13 | 4 | 6 | This domain allows configuring virtual authenticators to test the WebAuthn API. |
| [WebMCP](WebMCP.md) | **Experimental** | 4 | 4 | 5 |  |
