# Android

The latest [binaries for ChromeDriver](https://googlechromelabs.github.io/chrome-for-testing/)
are packaged as zip files for various host platforms.

Earlier versions of ChromeDriver can be found in
[Downloads](https://developer.chrome.com/docs/chromedriver/downloads).

### Supported apps

ChromeDriver supports running tests on Chrome browser (version 30+) and
WebView-based apps starting in [Android 4.4 (KitKat)](https://developers.google.com/chrome/mobile/docs/webview/overview) that have enabled [web debugging](https://developer.chrome.com/docs/devtools/remote-debugging/webviews) and [JavaScript](http://developer.android.com/reference/android/webkit/WebSettings.html#setJavaScriptEnabled%28boolean%29).

You can install Chrome app from:

Stable: <https://play.google.com/store/apps/details?id=com.android.chrome>
| **Beta:** <https://play.google.com/store/apps/details?id=com.chrome.beta>

### Selenium WebDriver Language Bindings

The standard Selenium project WebDriver language bindings need to be installed
for your language of choice to write your tests. This library is available in
your local package manager or the [Selenium project](https://www.selenium.dev/downloads/).

For example, the language bindings for Python can be installed with pip.  

    $ pip install selenium

### Android SDK

The SDK can be downloaded from
[developer.android.com/sdk/](https://developer.android.com/sdk/).

## Device requirements

As of Chrome version 33, a rooted device is not required. If running tests
on earlier versions of Chrome, devices must be rooted as ChromeDriver
required write access to the `/data/local` directory to set Chrome's command
line arguments.

## Run ChromeDriver

1. Start the Android SDK's Android Debug Bridge (adb) server:

       $ adb start-server

2. If testing on Chrome app prior to version 33, ensure adb shell has read and
   write access to `/data/local` directory on the device:

       $ adb shell su -c chmod 777 /data/local

3. We recommend that you start ChromeDriver through the Selenium library, though
   you can also manually start it from the command line.

       $ ./chromedriver

## Android-only options

The following Chrome Options are applicable to both Chrome and WebView apps:

- `androidPackage`: The package name of the Chrome or WebView app.
- `androidDeviceSerial`: (Optional) The device serial number on which to launch the app (See Multiple Devices section below).
- `androidUseRunningApp`: (Optional) Attach to an already-running app instead of launching the app with a clear data directory.

The following capabilities are only applicable to WebView apps.

- *androidActivity*: Name of the Activity hosting the WebView.
- *androidProcess* : (Optional) Process name of the Activity hosting the WebView (as given by ps). If not given, the process name is assumed to be the same as `androidPackage`.

## Run a test

Tests should pass the app's package name to the ChromeDriver through the
`androidPackage` option. For example, a minimal Python test looks like this:  

    from selenium import webdriver
    options = webdriver.ChromeOptions()
    options.add_experimental_option('androidPackage', 'com.android.chrome')
    driver = webdriver.Chrome('./chromedriver', options=options)
    driver.get('https://google.com')
    driver.quit()

## Multiple devices

To use a particular device for a session, specify `androidDeviceSerial` as a
Chrome option.

If the serial number isn't specified, the server selects an unused device at
random to associate with each session. An error is returned if all devices
already have active sessions, so tests should make sure to call quit when
finished.

## Connect to `wd/hub`

If your tests expect to connect to `wd/hub`, you can add `--url-base=wd/hub`
when launching the server:  

    $ ./chromedriver --url-base=wd/hub