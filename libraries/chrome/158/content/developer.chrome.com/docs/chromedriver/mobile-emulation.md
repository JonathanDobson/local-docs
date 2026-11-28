# Mobile emulation

Chrome allows users to emulate Chrome on a mobile device from the desktop
version of Chrome, by enabling the
[device mode with Chrome DevTools](https://developer.chrome.com/docs/devtools/device-mode). This feature
speeds up web development, allows developers to quickly test how a website
renders in a mobile device, without requiring a real device. ChromeDriver can
also emulate devices with the "mobileEmulation" capability, specified with a
dictionary value.

Like in the DevTools, there are two ways in ChromeDriver to enable Mobile Emulation:

- Specify a known device
- Specify individual device attributes

The format of the "mobileEmulation" dictionary depends on which method is needed.

## Specify a known mobile device

To enable device emulation with a specific device, the "mobileEmulation" dictionary must contain a "deviceName." Use a valid device name from the [DevTools Emulated Devices settings](https://developer.chrome.com/docs/devtools/device-mode) as the value for "deviceName."

![Screenshot of Devices setting](https://developer.chrome.com/static/docs/chromedriver/mobile-emulation/image/emulated-devices-devtools.png)

### Java

    Map<String, String> mobileEmulation = new HashMap<>();
    mobileEmulation.put("deviceName", "Nexus 5");
    ChromeOptions chromeOptions = new ChromeOptions();
    chromeOptions.setExperimentalOption("mobileEmulation", mobileEmulation);
    WebDriver driver = new ChromeDriver(chromeOptions);

### Ruby

    mobile_emulation = { "deviceName" => "Nexus 5" }
    caps = Selenium::WebDriver::Remote::Capabilities.chrome(
       "chromeOptions" => { "mobileEmulation" => mobile_emulation })
    driver = Selenium::WebDriver.for :remote, url: 'http://localhost:4444/wd/hub',
    desired_capabilities: caps

### Python

    from selenium import webdriver
    mobile_emulation = { "deviceName": "Nexus 5" }
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_experimental_option("mobileEmulation", mobile_emulation)
    driver = webdriver.Remote(command_executor='http://127.0.0.1:4444/wd/hub',
    desired_capabilities = chrome_options.to_capabilities())

### Source of known devices

The list of known devices is generated from the DevTools Emulation panel.
However, you can use a different version of ChromeDriver against a version of
Chrome that has a newer or older list of devices.

If you try a device name that ChromeDriver doesn't recognize, you receive an
error: "`<your device name>` must be a valid device." To emulate a device that ChromeDriver doesn't know, enable Mobile Emulation using individual device
metrics.

## Specify individual device attributes

You can enable Mobile Emulation by specifying individual attributes. The
"mobileEmulation" dictionary can contain `deviceMetrics`, `clientHints`
dictionaries, and a `userAgent` string.

The following device metrics must be specified in the "deviceMetrics" dictionary:

- "width" - the width in pixels of the device's screen
- "height" - the height in pixels of the device's screen
- "pixelRatio" - the device's pixel ratio
- "touch" - whether to emulate touch events. The value defaults to true and usually can be omitted.
- "mobile" - whether the browser must behave as a mobile user agent (overlay scrollbars, emit orientation events, shrink the content to fit the viewport, etc.). The value defaults to true and usually can be omitted.

The "clientHints" dictionary can have the following entries:

- "platform" - the operating system. It can be either a known value ("Android", "Chrome OS", "Chromium OS", "Fuchsia", "Linux", "macOS", "Windows"), that exactly matches the value returned by Chrome running on the given platform, or it can be a user defined value. This value is mandatory.
- "mobile" - whether the browser should request a mobile or desktop resource version. Usually Chrome running on a mobile phone with Android sets this value to true. Chrome on a tablet Android device sets this value to false. Chrome on a desktop device also sets this value to false. You can use this information to specify a realistic emulation. This value is mandatory.
- The remaining entries are optional and can be omitted unless if they are relevant for the test:
  - "brands" - list of brand / major version pairs. If omitted the browser uses its own values.
  - "fullVersionList" - list of brand / version pairs. It omitted the browser uses its own values.
  - "platformVersion" - OS version. Defaults to empty string.
  - "model" - device model. Defaults to empty string.
  - "architecture" - CPU architecture. Known values are "x86" and "arm". The user is free to provide any string value. Defaults to empty string.
  - "bitness" - platform bitness. Known values are "32" and "64". The user is free to provide any string value. Defaults to empty string.
  - "wow64" - emulation of windows 32 on windows 64. A boolean value that defaults to false.

ChromeDriver is capable to infer "userAgent" value from "clientHints" on the following platforms: "Android", "Chrome OS", "Chromium OS", "Fuchsia", "Linux", "macOS", "Windows". Therefore this value can be omitted.

If "clientHints" dictionary is omitted (legacy mode) ChromeDriver does its best
to infer the "clientHints" from "userAgent". This feature is not reliable, due to internal ambiguities of "userAgent" value format.

The phones and tablets that are available under the Mobile Emulation panel can
be found in the [DevTools source code](https://chromium.googlesource.com/chromium/src/+/167a7f5e03f8b9bd297d2663ec35affa0edd5076/third_party/WebKit/Source/devtools/front_end/emulated_devices/module.json).

### Java

    Map<String, Object> deviceMetrics = new HashMap<>();
    deviceMetrics.put("width", 360);
    deviceMetrics.put("height", 640);
    deviceMetrics.put("pixelRatio", 3.0);
    Map<String, Object> mobileEmulation = new HashMap<>();
    mobileEmulation.put("deviceMetrics", deviceMetrics);
    mobileEmulation.put("userAgent", "Mozilla/5.0 (Linux; Android 4.2.1; en-us; Nexus 5 Build/JOP40D) AppleWebKit/535.19 (KHTML, like Gecko) Chrome/18.0.1025.166 Mobile Safari/535.19");
    Map<String, Object> clientHints = new HashMap<>();
    clientHints.put("platform", "Android");
    clientHints.put("mobile", true);
    mobileEmulation.put("clientHints", clientHints);
    ChromeOptions chromeOptions = new ChromeOptions(); chromeOptions.setExperimentalOption("mobileEmulation", mobileEmulation); WebDriver driver = new ChromeDriver(chromeOptions);

### Ruby

    mobile_emulation = {
       "deviceMetrics" => { "width" => 360, "height" => 640, "pixelRatio" => 3.0 },
       "userAgent" => "Mozilla/5.0 (Linux; Android 4.2.1; en-us; Nexus 5 Build/JOP40D) AppleWebKit/535.19 (KHTML, like Gecko) Chrome/18.0.1025.166 Mobile Safari/535.19",
       "clientHints" => { "platform" => "Android", "mobile" => true}
    }
    caps = Selenium::WebDriver::Remote::Capabilities.chrome("chromeOptions" => mobile_emulation)
    driver = Selenium::WebDriver.for :remote, url: 'http://localhost:4444/wd/hub', desired_capabilities: caps

### Python

    from selenium import webdriver
    from selenium.webdriver.chrome.options import Options
    mobile_emulation = {
       "deviceMetrics": { "width": 360, "height": 640, "pixelRatio": 3.0 },
       "userAgent": "Mozilla/5.0 (Linux; Android 4.2.1; en-us; Nexus 5 Build/JOP40D) AppleWebKit/535.19 (KHTML, like Gecko) Chrome/18.0.1025.166 Mobile Safari/535.19",
       "clientHints": {"platform": "Android", "mobile": True} }
    chrome_options = Options()
    chrome_options.add_experimental_option("mobileEmulation", mobile_emulation)
    driver = webdriver.Chrome(chrome_options = chrome_options)

### JSON

Example of full mobile emulation configuration:  

    "mobileEmulation": {
      "userAgent": "Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko)
    Chrome/111.0.0.0 Mobile Safari/537.36",
      "deviceMetrics": {
         "mobile": true,
         "touch": true,
         "width": 412,
         "height": 823,
         "pixelRatio": 1.75
      },
      "clientHints": {
         "brands": [
            {"brand": "Google Chrome", "version": "111"},
            {"brand": "Chromium", "version": "111"}
         ],
         "fullVersionList": [
            {"brand": "Google Chrome", "version": "111.0.5563.64"},
            {"brand": "Chromium", "version": "111.0.5563.64"}
         ],
         "platform": "Android",
         "platformVersion": "11",
         "architecture": "arm",
         "model": "lorem ipsum (2022)"
         "mobile": true,
         "bitness": "32",
         "wow64": false
      }
    }

## Mobile emulation versus real devices

It's helpful to test websites on a desktop with mobile emulation,
but it's not a perfect replication of testing on the actual device.
There are some key differences, including:

- Mobile devices often have a different GPU, which may lead to big performance changes.
- Mobile UI is not emulated (in particular, hiding the address bar affects page height).
- Disambiguation popups (where you select one of a few touch targets) is not supported.
- Many hardware APIs (for example, `orientationchange` event) are unavailable.