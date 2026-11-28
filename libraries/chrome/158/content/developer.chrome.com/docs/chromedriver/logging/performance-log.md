# Performance log

ChromeDriver supports performance logging, from which you can get events of
domains "Timeline", "Network", and "Page", as well as
[trace data](http://www.chromium.org/developers/how-tos/trace-event-profiling-tool)
for specified trace categories.

## Enable performance logs

Performance logging is NOT enabled by default. So when creating a new session,
you have to enable it.  

    DesiredCapabilities cap = DesiredCapabilities.chrome();
    LoggingPreferences logPrefs = new LoggingPreferences();
    logPrefs.enable(LogType.PERFORMANCE, Level.ALL);
    cap.setCapability(CapabilityType.LOGGING_PREFS, logPrefs);
    RemoteWebDriver driver = new RemoteWebDriver(new URL("http://127.0.0.1:9515"), cap);

When enabled, the performance log collects Timeline, Network, and Page
events. To also enable tracing, or to customize performance logging, keep
reading.

View a [complete example of performance logging with default options](https://gist.github.com/klepikov/5457750), written by Michael Klepikov.

[Angular Benchpress](https://github.com/angular/angular/tree/main/packages/benchpress)
also uses performance logging.

## Tracing and custom logging

If you need to customize performance logging, to enable tracing for example, you
can use the [perfLoggingPrefs capability](https://developer.chrome.com/docs/chromedriver/logging/performance-log)
(via ChromeOptions). Tracing can be enabled by specifying one or more Chrome
trace categories. Read more information about
[Chrome tracing](http://www.chromium.org/developers/how-tos/trace-event-profiling-tool).

When tracing is enabled, the Timeline domain is implicitly disabled. You still
need to enable the performance log with the `loggingPrefs` capability.  

    DesiredCapabilities cap = DesiredCapabilities.chrome();
    LoggingPreferences logPrefs = new LoggingPreferences();
    logPrefs.enable(LogType.PERFORMANCE, Level.ALL);
    cap.setCapability(CapabilityType.LOGGING_PREFS, logPrefs);
    Map<String, Object> perfLogPrefs = new HashMap<String, Object>();
    perfLogPrefs.put("traceCategories", "browser,devtools.timeline,devtools"); // comma-separated trace categories
    ChromeOptions options = new ChromeOptions();
    options.setExperimentalOption("perfLoggingPrefs", perfLogPrefs);
    caps.setCapability(ChromeOptions.CAPABILITY, options);
    RemoteWebDriver driver = new RemoteWebDriver(new URL("http://127.0.0.1:9515"), cap);

You can also use `perfLoggingPrefs` to enable or disable the Network and Page
domains individually. For example, you can explicitly enable the Network domain
while tracing:  

    ...

    Map<String, Object> perfLogPrefs = new HashMap<String, Object>();
    perfLogPrefs.put("traceCategories", "browser,devtools.timeline,devtools");
    perfLogPrefs.put("enableNetwork", true);
    ChromeOptions options = new ChromeOptions();
    options.setExperimentalOption("perfLoggingPrefs", perfLogPrefs);
    caps.setCapability(ChromeOptions.CAPABILITY, options);

    ...

If tracing is enabled, ChromeDriver starts a browser-wide trace when Chrome
is launched and continues tracing until Chrome closes. When a trace is
running, Chrome buffers trace events in memory until the trace is stopped.

Once the trace buffer is full, trace events are no longer be recorded. To avoid
a full buffer (and thus lost trace data), ChromeDriver periodically stops the
current trace, collects the buffered events, and re-starts tracing at certain
points during a test.

Collecting trace events can add overhead to a test, so ChromeDriver only
collects trace events at appropriate points during a test. Trace
events are only collected on page navigation events and when any ChromeDriver
log (such as the performance log) is requested.

There is always a possibility that the buffer still fills up, so ChromeDriver
monitors the buffer usage for supported Chrome versions (r263512 and later).
If the buffer fills, ChromeDriver logs a warning and adds an entry to the
performance log.

## Collect log entries

In the test, you can get performance log entries. Read the
[WebDriver logging documentation](http://selenium.googlecode.com/git/docs/api/java/org/openqa/selenium/logging/Logs.html)
for more information.  

    for (LogEntry entry : driver.manage().logs().get(LogType.PERFORMANCE)) {
      System.out.println(entry.toString());
    }

Each entry is a JSON string of the following structure:  

    {
      "webview": <originating WebView ID>,
      "message": { "method": "...", "params": { ... }} // DevTools message.
    }

The method value is the method of the [DevTools event](https://chromedevtools.github.io/devtools-protocol/).
For example, Timeline events have a method of `Timeline.eventRecorded` for all
versions of the protocol up to and including version 1.1 (the latest at the time
this was written).

## Trace log entries

Tracing is not part of the published DevTools protocol as of version 1.1, so
details are provided here.

All trace events have a webview value of "browser," since the events are
collected browser-wide.

There are two possible trace event methods:

- `tracing.dataCollected`: params are a single trace event in the form of a dictionary.
- `tracing.bufferUsage`: params contain a single error key, with a message indicating that the DevTools trace buffer filled during the test.

Here is an example trace event:  

    {
      "webview":"browser",
      "message":{
        "method":"Tracing.dataCollected",
        "params":{
          "args":{"layerTreeId":1},
          "cat":"cc,devtools",
          "name":"DrawFrame",
          "ph":"i",
          "pid":11405,
          "s":"t",
          "tid":11405,
          "ts":3846117219.0,
          "tts":1134680
        }
      }
    }