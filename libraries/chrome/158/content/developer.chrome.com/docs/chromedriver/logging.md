# Logging

By default ChromeDriver logs only warnings and errors to stderr. When debugging
issues, it's helpful to enable more verbose logging.

To enable verbose logging, pass `--verbose` to the ChromeDriver server.
You can also pass `--log-path` to cause the log to be written to a file instead
of stderr. If you don't start the ChromeDriver server directly yourself, you
need to pass the switch with your WebDriver client library. Some clients don't
have an option for this yet, unfortunately.

When passing `--log-path` to Chrome launch command, the stderr on Chrome Linux
and Mac is saved in the log file. However, the stderr on Windows is not
saved because Chrome is a GUI application and the OS doesn't allow it to inherit
stderr handle from ChromeDriver.

To save stderr on Windows, Linux and Mac, use the `CHROME_LOG_FILE` environment
variable. Then, the file only contains logs from Chrome. If you specify
`logPath` in ChromeOptions, ChromeDriver copies its value to `CHROME_LOG_FILE`.

Android does not capture stderr or stdout. The stdout goes to the console
window on all platforms.

## Log with C

    var service = ChromeDriverService.CreateDefaultService();

    service.LogPath = "D:\\chromedriver.log";

    service.EnableVerboseLogging = true;

    driver = new ChromeDriver(service);

There are overloaded version of both functions, see the API documentation.

## Log with Java

    System.setProperty("webdriver.chrome.logfile", "D:\\chromedriver.log");

    System.setProperty("webdriver.chrome.verboseLogging", "true");

## Log with Python

    driver = webdriver.Chrome(executable_path="D:\\chromedriver.exe", service_args=["--verbose", "--log-path=D:\\qc1.log"])

## Log with all languages

Start ChromeDriver in the terminal with verbose logging, using the following
flags:  

    --verbose --log-path=chromedriver.log

Run your test using a RemoteWebDriver pointed at `http://localhost:9515`.