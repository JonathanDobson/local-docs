# Chrome doesn&#39;t start or crashes immediately

This often happens when running ChromeDriver or Chrome using a special test
harness (perhaps an IDE) or continuous build system (such as Jenkins).

Try launching the same Chrome binary that your test uses from a normal
user command prompt. Confirm which Chrome binary is in use in the
`chromedriver.log` file. If you pass special command line switches or arguments
to Chrome, make sure to include those, too. If Chrome fails to start correctly,
you need to fix your installation of Chrome. Try re-installing.

Assuming you can run Chrome from a command prompt, your next step is to see if
the same problem occurs when running your test in a testing environment.
Preferably, you launch the test binary or script directly from a normal user's
command prompt. Confirm that you can launch Chrome directly from your test,
without using WebDriver or ChromeDriver. For example, in
Java, you may use the ProcessBuilder API to start the Chrome binary directly.
If your test exhibits the same problem even in a testing environment, file a new
issue with instructions on how to reproduce the problem.

Otherwise, if the problem only occurs in your special testing environment:

Use Chrome's
[alternate installer](http://www.google.com/chrome/eula.html?system=true&standalone=1).
This installs Chrome for all users. This often fixes problems if you are running
Selenium as a background service.

A common cause for Chrome to crash during startup is running Chrome as root user
(administrator) on Linux. While it is possible to work around this issue by
passing `--no-sandbox` flag when creating your WebDriver session, such a
configuration is unsupported and highly discouraged. Configure your environment
to run Chrome as a regular user instead.

If none of these solutions fixes the problem, file a new issue with instructions
on how to reproduce the problem. If your issue only occurs in a special,
uncommon testing environment, be aware that the ChromeDriver developers may
choose not to investigate and resolve your issue.