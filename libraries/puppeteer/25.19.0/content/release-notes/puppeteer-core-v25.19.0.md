# puppeteer-core-v25.19.0

Published: 2026-11-25T17:43:28Z

## [25.19.0](https://github.com/puppeteer/puppeteer/compare/puppeteer-core-v25.18.1...puppeteer-core-v25.19.0) (2026-11-25)


### 🎉 Features

* add Target.close() ([#15830](https://github.com/puppeteer/puppeteer/issues/15830)) ([7133169](https://github.com/puppeteer/puppeteer/commit/71331695c42e75291f5e20ab3babfef72bd41983))
* roll to Chrome 158.0.8127.36 ([#15832](https://github.com/puppeteer/puppeteer/issues/15832)) ([680acbd](https://github.com/puppeteer/puppeteer/commit/680acbd014b8b4776a75edd9e89ea124457928fd))
* roll to Firefox 161.0 ([#15878](https://github.com/puppeteer/puppeteer/issues/15878)) ([a3f5581](https://github.com/puppeteer/puppeteer/commit/a3f5581797135ef966b6fb8beb566a61bd3aa240))


### 🛠️ Fixes

* **accessibility:** preserve iframe snapshots when root is specified ([#15875](https://github.com/puppeteer/puppeteer/issues/15875)) ([53e3573](https://github.com/puppeteer/puppeteer/commit/53e3573797bb77b425eb0042fb1b932b92e6fea4))
* **bidi:** propagate connection close and drain microtasks in BidiOverCdp ([#15776](https://github.com/puppeteer/puppeteer/issues/15776)) ([ceb4414](https://github.com/puppeteer/puppeteer/commit/ceb4414ef7ec1d3a708575e86517e5fdac071ffb))
* **bidi:** throw UnsupportedOperation for targetFilter ([#15779](https://github.com/puppeteer/puppeteer/issues/15779)) ([1670e54](https://github.com/puppeteer/puppeteer/commit/1670e5489b416e3b3dc9da091f931dbd5ec53406))
* **bidi:** use defaultNavigationTimeout for network-idle waits ([#15820](https://github.com/puppeteer/puppeteer/issues/15820)) ([e82d656](https://github.com/puppeteer/puppeteer/commit/e82d656004488cc2f635f878da7cede1b4631235))
* **cdp:** count concurrent manual attaches per target ([#15751](https://github.com/puppeteer/puppeteer/issues/15751)) ([47a6c68](https://github.com/puppeteer/puppeteer/commit/47a6c686b8dd58e8c9a5c3ac03ae36c84e2c6f7f))
* **cdp:** keep the media type when emulating media features ([#15745](https://github.com/puppeteer/puppeteer/issues/15745)) ([4ff12b3](https://github.com/puppeteer/puppeteer/commit/4ff12b308a69b6b55cc14fe6022623610a99995a))
* **cdp:** report the numpad location on keyup events ([#15845](https://github.com/puppeteer/puppeteer/issues/15845)) ([283aa65](https://github.com/puppeteer/puppeteer/commit/283aa65c790bbef6831ebd910050d77f0427a927))
* **cdp:** support getProperties on primitive and disposed handles ([#15858](https://github.com/puppeteer/puppeteer/issues/15858)) ([7ec3c95](https://github.com/puppeteer/puppeteer/commit/7ec3c95715b0365945d93ef150ce9dde9836fe89))
* **cdp:** terminate navigation immediately when page crashes ([#15774](https://github.com/puppeteer/puppeteer/issues/15774)) ([9c28591](https://github.com/puppeteer/puppeteer/commit/9c28591067f2dcdc7020c95777376bcb64c40529))
* copy options when cloning FunctionLocator ([#15834](https://github.com/puppeteer/puppeteer/issues/15834)) ([d68ee59](https://github.com/puppeteer/puppeteer/commit/d68ee5953bf9b0f02aabe591fe1cb6fa4cdb9b0f))
* copy the viewport in Page.setViewport() and Page.viewport() ([#15842](https://github.com/puppeteer/puppeteer/issues/15842)) ([6b9bc63](https://github.com/puppeteer/puppeteer/commit/6b9bc638b8ab90751d88380154096140132ec9de))
* do not hide the window of headful browsers on Windows ([#15836](https://github.com/puppeteer/puppeteer/issues/15836)) ([ddfefdf](https://github.com/puppeteer/puppeteer/commit/ddfefdf4c38f9d57be2408c1616a6f7aa7d16fe0))
* honor an already aborted signal in waitForFileChooser() and waitForDevicePrompt() ([#15804](https://github.com/puppeteer/puppeteer/issues/15804)) ([3ba5501](https://github.com/puppeteer/puppeteer/commit/3ba55014c00d50c02182b50d8f66ac1c0fa6a047))
* let off() remove listeners added with once() ([#15806](https://github.com/puppeteer/puppeteer/issues/15806)) ([fee3304](https://github.com/puppeteer/puppeteer/commit/fee3304834acc91458893bf22f8470338dcb611e))
* **page:** preserve special numbers in evaluateOnNewDocument arguments ([#15861](https://github.com/puppeteer/puppeteer/issues/15861)) ([e8f6920](https://github.com/puppeteer/puppeteer/commit/e8f69209b6f29edfbad2fb7f8c663264bf2ffa52))
* preserve custom and falsy AbortSignal reasons in WaitTask and QueryHandler ([#15839](https://github.com/puppeteer/puppeteer/issues/15839)) ([95b7f85](https://github.com/puppeteer/puppeteer/commit/95b7f8507a3141a93422e2959acd18a42fd0a9a6))
* roll to Chrome 158.0.8127.88 ([#15871](https://github.com/puppeteer/puppeteer/issues/15871)) ([e81f47a](https://github.com/puppeteer/puppeteer/commit/e81f47a3f70a1d0203f10a48bd9f2f76d85d5029))
* roll to Firefox 160.0.1 ([#15831](https://github.com/puppeteer/puppeteer/issues/15831)) ([e1f91c5](https://github.com/puppeteer/puppeteer/commit/e1f91c5e53c08034f17309f56be941aee19479a6))
* send a reason phrase for status codes Chrome doesn't know ([#15844](https://github.com/puppeteer/puppeteer/issues/15844)) ([66beb76](https://github.com/puppeteer/puppeteer/commit/66beb762aba251b12297755ded164415bc1f662b))
* send an empty post data override in request.continue() ([#15849](https://github.com/puppeteer/puppeteer/issues/15849)) ([f4bf4ac](https://github.com/puppeteer/puppeteer/commit/f4bf4ac07a3c1239d36f86368c9c34813e8f03d4))
* serialize page screenshots across browser contexts ([#15775](https://github.com/puppeteer/puppeteer/issues/15775)) ([8d0b92e](https://github.com/puppeteer/puppeteer/commit/8d0b92e3f0d16d5e3b7dad8dad9a1251ca54f413))
* stronger target subtype check ([#15837](https://github.com/puppeteer/puppeteer/issues/15837)) ([c90b385](https://github.com/puppeteer/puppeteer/commit/c90b3854cbfc130eba9d57a8bfec32dc2f1e0b17))
* **tracing:** reset state, avoid mutating categories, and handle disconnect ([#15870](https://github.com/puppeteer/puppeteer/issues/15870)) ([5860428](https://github.com/puppeteer/puppeteer/commit/5860428de49053533944a2a91a202850b22d9746))
* use the payload of the highest priority in Cooperative Intercept Mode ([#15825](https://github.com/puppeteer/puppeteer/issues/15825)) ([4ee6cff](https://github.com/puppeteer/puppeteer/commit/4ee6cff57442b7e03f7b27fb8018ee5ebaeab68b))
* **webdriver:** update the mouse position after a click over WebDriver BiDi ([#15807](https://github.com/puppeteer/puppeteer/issues/15807)) ([b4435d4](https://github.com/puppeteer/puppeteer/commit/b4435d4ded2b771ef54cb85144876bc3290027b5))


### 📄 Documentation

* fix the documented default of ReloadOptions.ignoreCache ([#15840](https://github.com/puppeteer/puppeteer/issues/15840)) ([aebed44](https://github.com/puppeteer/puppeteer/commit/aebed4488e7b9d828034521c7930daf47c6e82c5))


### Dependencies

* The following workspace dependencies were updated
  * dependencies
    * @puppeteer/browsers bumped from 3.2.7 to 3.3.0
