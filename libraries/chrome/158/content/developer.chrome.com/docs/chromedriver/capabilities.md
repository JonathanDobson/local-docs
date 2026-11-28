# Capabilities and ChromeOptions

Capabilities are options that you can use to customize and configure a ChromeDriver session. This page documents all ChromeDriver supported capabilities and how to use them.

The WebDriver language APIs provides ways to pass capabilities to ChromeDriver. The exact mechanism differs by the language, but most languages use one or both of the following mechanisms:

1. Use the `ChromeOptions` class. This is supported by Java, Python, etc.
2. Use the `DesiredCapabilities` class. This is supported by Python, Ruby, etc. While it's also available in Java, its usage in Java is deprecated.

## Using the ChromeOptions class

You can create an instance of `ChromeOptions`, which has convenient methods for setting ChromeDriver-specific capabilities. You can then pass the `ChromeOptions`
object into the ChromeDriver constructor:  

    ChromeOptions options = new ChromeOptions();
    options.addExtensions(new File("/path/to/extension.crx"));
    ChromeDriver driver = new ChromeDriver(options);

Since Selenium version 3.6.0, the `ChromeOptions` class in Java also implement
the `Capabilities` interface, allowing you to specify other WebDriver
capabilities not specific to ChromeDriver.  

    ChromeOptions options = new ChromeOptions();

    // Add the WebDriver proxy capability.
    Proxy proxy = new Proxy();
    proxy.setHttpProxy("myhttpproxy:3337");
    options.setCapability("proxy", proxy);

    // Add a ChromeDriver-specific capability.
    options.addExtensions(new File("/path/to/extension.crx"));
    ChromeDriver driver = new ChromeDriver(options);

## Use DesiredCapabilities

To use `DesiredCapabilities`, you need to know the name of the capability and
the type of value it takes. See the [full list](https://developer.chrome.com/docs/chromedriver/capabilities#recognized_capabilities).

### Python

    caps = webdriver.DesiredCapabilities.CHROME.copy()
    caps['acceptInsecureCerts'] = True
    driver = webdriver.Chrome(desired_capabilities=caps)

### Ruby

    caps = Selenium::WebDriver::Remote::Capabilities.chrome(
      "goog:chromeOptions" => {"args" => [ "window-size=1000,800" ]})
    driver = Selenium::WebDriver.for :chrome, desired_capabilities: caps

## Common use cases

### Use a custom profile

By default, ChromeDriver creates a new temporary profile for each session. You
may want to set special preferences or just use a custom profile altogether,
also called the user data directory.

If using the temporary profile, you can use the `chrome.prefs` capability to
specify preferences to apply after Chrome starts. For custom profiles, you can
use the `user-data-dir` Chrome command-line switch to tell Chrome which profile
to use:  

    ChromeOptions options = new ChromeOptions();
    options.addArguments("user-data-dir=/path/to/your/custom/profile");

Create your own custom profile by running Chrome on the command-line or
with ChromeDriver, using the `user-data-dir` switch set to some new directory.

If the path doesn't exist, Chrome creates a new profile in the specified
location. You can then modify the profile settings, and ChromeDriver can use
the profile in the future. Open `chrome://version` in the browser to see what
profile Chrome is using.

### Start Chrome maximized

Start Chrome maximized by using the `start-maximized` switch:  

    ChromeOptions options = new ChromeOptions();
    options.addArguments("start-maximized");

### Use a Chrome executable in a non-standard location

    ChromeOptions options = new ChromeOptions();
    options.setBinary("/path/to/other/chrome/binary");

### Block dialog windows

By default, ChromeDriver configures Chrome to allow pop-up windows. If you want
to block pop-ups, and restore the normal Chrome behavior when it isn't
controlled by ChromeDriver, do the following:  

    ChromeOptions options = new ChromeOptions();
    options.setExperimentalOption("excludeSwitches",
         Arrays.asList("disable-popup-blocking"));

## Set download directory

The following code can be used to configure Chrome to download files to a
specific directory. However, there are several caveats to be aware of:

- Chrome disallows using certain directories for download. In particular, you cannot use the desktop folder as the download directory. On Linux, you cannot use the home directory for download. The exact list of forbidden directories is subject to change, so we recommended that you use a unique directory that has no special meaning to the system.
- ChromeDriver does not automatically wait for download to complete. If you call `driver.quit()` too soon, Chrome might terminate before the download has finished.
- For best results, use full paths, as relative paths don't always work.
- On Windows, use ``\` as path separators.``/\` isn't reliable on Windows.

    ChromeOptions options = new ChromeOptions();
    Map<String, Object> prefs = new HashMap<String, Object>();
    prefs.put("download.default_directory", "/directory/path");
    options.setExperimentalOption("prefs", prefs);

## Recognized capabilities

Read the [Selenium documentation](https://www.selenium.dev/downloads/) and
[W3C WebDriver standard](https://www.w3.org/TR/webdriver/) for standard
capabilities accepted by ChromeDriver. Here, we list the Chrome-specific
capabilities.

### `ChromeOptions` object

Most Chrome-specific capabilities are exposed through the `ChromeOptions`
object. In some languages, they're implemented by the `ChromeOptions` class. In
other languages, they're stored under the `goog:chromeOptions` dictionary in
selected capabilities.  

|           Name           |      Type       | Default |                                                                                                                                                 Description                                                                                                                                                 |
|--------------------------|-----------------|---------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `args`                   | list of strings |         | List of command-line arguments to use when starting Chrome. Arguments with an associated value should be separated by a '=' sign (such as, \['start-maximized', 'user-data-dir=/tmp/temp_profile'\]). See a list of [Chrome arguments](http://peter.sh/experiments/chromium-command-line-switches/).        |
| `binary`                 | string          |         | Path to the Chrome executable to use. On macOS X, this should be the actual binary, not just the app, such as, `/Applications/Google Chrome.app/Contents/MacOS/Google Chrome`.                                                                                                                              |
| `extensions`             | list of strings |         | A list of Chrome extensions to install on startup. Each item in the list should be a base-64 encoded packed Chrome extension (.crx)                                                                                                                                                                         |
| `localState`             | dictionary      |         | A dictionary with each entry consisting of the name of the preference and its value. These preferences are applied to the Local State file in the user data folder.                                                                                                                                         |
| `prefs`                  | dictionary      |         | A dictionary with each entry consisting of the name of the preference and its value. These preferences are only applied to the user profile in use. See the 'Preferences' file in Chrome's user data directory for examples.                                                                                |
| `detach`                 | boolean         | false   | If false, Chrome is quit when ChromeDriver is killed, regardless of whether the session is quit. If true, Chrome only quits if the session is quit or closed. If true and the session isn't quit, ChromeDriver cannot clean up the temporary user data directory that the running Chrome instance is using. |
| `debuggerAddress`        | string          |         | An address of a Chrome debugger server to connect to, in the form of \<hostname/ip:port\>, such as '127.0.0.1:38947'                                                                                                                                                                                        |
| `excludeSwitches`        | list of strings |         | List of Chrome command line switches to exclude that ChromeDriver by default passes when starting Chrome. Don't prefix switches with `--`.                                                                                                                                                                  |
| `minidumpPath`           | string          |         | Directory to store Chrome minidumps. (Supported only on Linux.)                                                                                                                                                                                                                                             |
| `mobileEmulation`        | dictionary      |         | A dictionary with either a value for "deviceName," or values for "deviceMetrics", and "userAgent." Refer to [Mobile Emulation](https://developer.chrome.com/docs/chromedriver/mobile-emulation) for more information.                                                                                       |
| `perfLoggingPrefs`       | dictionary      |         | An optional dictionary that specifies performance logging preferences. See below for more information.                                                                                                                                                                                                      |
| `windowTypes`            | list of strings |         | A list of window types that appear in the list of window handles. For access to webview elements, include "webview" in this list.                                                                                                                                                                           |
| `enableExtensionTargets` | boolean         | false   | Enable introspection of Chrome Extension targets. By default ChromeDriver does not include extension targets (from Chrome 136).                                                                                                                                                                             |

### `perfLoggingPrefs` object

The `perfLoggingPrefs` dictionary has the following format. All keys are optional:  

|              Name              |       Type       | Default |                                                                                                                   Description                                                                                                                    |
|--------------------------------|------------------|---------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `enableNetwork`                | boolean          | true    | Whether or not to collect events from Network domain.                                                                                                                                                                                            |
| `enablePage`                   | boolean          | true    | Whether or not to collect events from Page domain.                                                                                                                                                                                               |
| `traceCategories`              | string           | (empty) | A comma-separated string of Chrome tracing categories for which trace events should be collected. An unspecified or empty string disables tracing.                                                                                               |
| `bufferUsageReportingInterval` | positive integer | 1000    | The requested number of milliseconds between DevTools trace buffer usage events. For example, if 1000, then once per second, DevTools reports how full the trace buffer is. If a report indicates the buffer usage is 100%, a warning is issued. |

## Returned Capabilities

Here's a list of all the Chrome-specific returned capabilities, in other words,
what ChromeDriver returns when you create a new session.  

|             Name             |  Type  |                                         Description                                          |
|------------------------------|--------|----------------------------------------------------------------------------------------------|
| `chrome.chromedriverVersion` | string | version of ChromeDriver                                                                      |
| `userDataDir`                | string | path to user data directory that Chrome is using; note, this is inside a 'chrome' dictionary |