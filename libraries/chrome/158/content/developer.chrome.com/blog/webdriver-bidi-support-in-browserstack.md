# Automation with WebDriver BiDi now available on BrowserStack

Source: https://developer.chrome.com/blog/webdriver-bidi-support-in-browserstack

![Matthias Rohmer](https://web.dev/images/authors/mrohmer.jpg) Matthias Rohmer [X](https://twitter.com/matthiasrohmer) [GitHub](https://github.com/matthiasrohmer) [LinkedIn](https://www.linkedin.com/in/matthias-rohmer-b09191b0) [Bluesky](https://bsky.app/profile/matthiasrohmer.bsky.social)

<br />

Over the last three years Chrome's Browser Automation team has been
collaborating with other major browser and tooling vendors like BrowserStack to
create [WebDriver BiDi](https://developer.chrome.com/blog/webdriver-bidi.md.txt)---a new browser automation protocol
which enables bi-directional automation workflows across browsers. These
workflows were previously only possible with the proprietary Chrome DevTools
Protocol in Chromium-based browsers.

Today marks an important milestone of this shared effort as WebDriver BiDi
finally becomes production-ready for developers, starting with BrowserStack
today.

> [!TIP]
> **Tip:** Learn more about WebDriver BiDi in [WebDriver BiDi - The future of cross-browser automation.](https://developer.chrome.com/blog/webdriver-bidi.md.txt).

## Selenium and BrowserStack

Recently [BrowserStack became an official Development Partner of Selenium](https://www.browserstack.com/browserstack-selenium?utm_campaign=chrome-blog&utm_campaigncode=701OW000009sQwVYAU&utm_medium=partnered&utm_source=seleniumorg),
a mature, open-source browser automation framework that also contributed to
WebDriver BiDi. This partnership is a testament to BrowserStack's continued
investment in a thriving testing ecosystem, with BrowserStack also employing
several core maintainers of Selenium.

Part of the [Selenium project](https://www.selenium.dev/) is Selenium Grid,
which lets you run tests across multiple devices in parallel. But setting a Grid
up on your own, acquiring and maintaining dozens of different devices, and
keeping them available can be challenging or even impossible for some.

Hosted Selenium Grid solutions like BrowserStack can make it easier to run your
tests across many different platforms and devices---without managing them on your
own.

## WebDriver BiDi on Selenium Grid

Selenium is based on the WebDriver standard (note the missing BiDi) but has had
experimental support for WebDriver BiDi for a while. Starting today, you can use
WebDriver BiDi commands in production on BrowserStack's hosted Selenium Grid!

This finally enables features like request interception, advanced emulation, and
handling browser events in real-time---and not just in Chrome, but in every
browser that supports WebDriver BiDi.

The following example shows how to listen for log events, using WebDriver BiDi
on BrowserStack. Caught logs are then also available for inspection on
automate.browserstack.com:

```javascript
const webdriver = require('selenium-webdriver');

// Insert credentials from https://www.browserstack.com/accounts/profile/details
const USERNAME = '<YOUR_USERNAME>';
const ACCESS_KEY = '<YOUR_ACCESS_KEY>';

(async () => {
  const driver = await (new webdriver.Builder()
    .withCapabilities({
      browserName: 'chrome',
      'bstack:options': {
        seleniumVersion: '4.22.0',
        seleniumBidi: true, // Enable WebDriver BiDi.
      },
    })
    .usingServer(
      `https://${USERNAME}:${ACCESS_KEY}@hub-cloud.browserstack.com/wd/hub`
    )
    .build());

  // Add a listener for log events.
  await driver.script().addConsoleMessageHandler((logEntry) => {
    console.log(logEntry.text);
  });

  await driver.get(
    'https://www.selenium.dev/selenium/web/bidi/logEntryAdded.html'
  );

  // Trigger a console log on the demo page.
  await driver.findElement({ id: 'consoleLog' }).click();
  await driver.quit();

  // Inspect logs on automate.browserstack.com!
})();
```

> [!TIP]
> **Tip:** Learn more about the WebDriver BiDi capabilities supported on BrowserStack [in the BrowserStack event-driven testing documentation](https://www.browserstack.com/docs/automate/selenium/bidi-event-driven-testing?utm_campaign=chrome-blog&utm_campaigncode=701OW000009sQwVYAU&utm_medium=partnered&utm_source=seleniumorg).

## BrowserStack is just the beginning

The Chrome Browser Automation team congratulates the team at BrowserStack for
launching their WebDriver BiDi support today! We are also looking forward to
seeing the support for WebDriver BiDi expand across BrowserStack, other tools
like Selenium, as well as other major browsers in the coming weeks.

And if this announcement made you excited about testing, but you haven't started
your testing journey yet, make sure to [check out our Learn Testing course on web.dev](http://web.dev/learn/testing).