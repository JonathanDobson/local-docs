# Operation not supported when using remote debugging

Some WebDriver commands, such as resizing the browser window, require a Chrome
extension to be loaded into the browser. ChromeDriver normally loads this
"automation extension" every time it launches a new Chrome session.

However ChromeDriver can be instructed to connect to an existing Chrome session
instead of launching a new one. This is done using `debuggerAddress` in the
[Capabilities](https://developer.chrome.com/docs/chromedriver/capabilities) object, also known as
ChromeOptions.

As the automation extension is only loaded at startup, there are some commands
that ChromeDriver does not support when working with existing sessions through
remote debugging.

If you see the error "operation not supported when using remote debugging", try
rewriting the test so that it launches a new Chrome session. This can be done by
removing `debuggerAddress` from the Capabilities object.