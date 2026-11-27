# ChromeOS

Source: https://developer.chrome.com/docs/chromedriver/get-started/chromeos

| **Warning:** ChromeOS test images [no longer](https://crrev.com/c/5422567) include Selenium. You need to install a Selenium version compatible with the Chrome and ChromeDriver versions installed in the ChromeOS image.

All ChromeOS test images have ChromeDriver binary installed in
`/usr/local/chromedriver/`. The binary is updated to the same version of Chrome
in that test image. That is, you always are using the latest build of
ChromeDriver.

If your test expects to run against a stable build of ChromeDriver binary,
you need to write your own code in your test to download the specific binary and
replace the binary in `/usr/local/chromedriver/`.

## Use ChromeDriver in an Autotest test

You can write a test that uses ChromeDriver to interact with ChromeOS. There's
[a wrapper class](https://chromium.googlesource.com/chromiumos/third_party/autotest/+/main/client/common_lib/cros/chromedriver.py)
to use ChromeDriver available in ChromeOS/Autotest. The wrapper class acts as a
context manager type and handles the following tasks for you:

1. Signs into ChromeOS using Telemetry.
2. Starts ChromeDriver with Remote mode on the Device under Test (DUT) and connects to the remote debug port of the Chrome instance after sign in.
3. Exposes a driver instance for you to make any ChromeDriver calls.
4. Shutdowns ChromeDriver process, and logs out of ChromeOS.

Follow this example of test: [`desktopui_UrlFetchWithChromeDriver`](https://chromium.googlesource.com/chromiumos/third_party/autotest/+/main/client/site_tests/desktopui_UrlFetchWithChromeDriver/desktopui_UrlFetchWithChromeDriver.py).

To get started:

1. Import the wrapper class.

       from autotest_lib.client.common_lib.cros import chromedriver

2. Create an instance of the ChromeDriver and make calls.

       with chromedriver.chromedriver() as chromedriver_instance:
       driver = chromedriver_instance.driver
       # Here you can make standard ChromeDriver calls through the driver instance.
       # For example, browse a given url with |driver.get(url)|