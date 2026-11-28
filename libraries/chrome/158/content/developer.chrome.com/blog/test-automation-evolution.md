# A look back in time: the evolution of test automation

Source: https://developer.chrome.com/blog/test-automation-evolution

![Jecelyn Yeen](https://web.dev/images/authors/jecelynyeen.jpg) Jecelyn Yeen [X](https://twitter.com/jecfish) [GitHub](https://github.com/jecfish) [Bluesky](https://bsky.app/profile/jec.fish) [Homepage](https://jec.fish/) ![Maksim Sadym](https://web.dev/images/authors/sadym.jpg) Maksim Sadym [X](https://twitter.com/maximsadym) [GitHub](https://github.com/sadym-chromium)

<br />

[Video](https://www.youtube.com/watch?v=6oXic6dcn9w)

## The birth of test automation

Let's rewind back to the 1990s when the web browser was born. Test automation didn't become a reality until the 2000s, with the emergence of [Selenium](https://www.selenium.dev/history/) and [WebDriver](https://www.selenium.dev/history/#:%7E:text=testing%20tool%20called-,WebDriver.,-It%20did%20not) projects to tackle cross-browser and multi-device testing challenges.

These two projects joined forces in 2011 as [Selenium WebDriver](https://www.selenium.dev/documentation/webdriver/) and became a [W3C standard](https://w3c.github.io/webdriver/) in 2018. We usually refer to it as WebDriver or **WebDriver "Classic"**.
![The evolution of the Selenium WebDriver project.](https://developer.chrome.com/static/blog/test-automation-evolution/image/the-evolution-the-seleni-469e6e4dcd20b.png) The evolution of the Selenium WebDriver project

Test automation prior to WebDriver "Classic" was quite tricky. Being able to automate browser testing significantly improved the quality of developers' and testers' lives.

## The rise of JavaScript

As web development evolved to rely more on JavaScript, new automation solutions such as WebdriverIO, Appium, Nightwatch, Protractor (deprecated), Testcafe, Cypress, Puppeteer, and Playwright emerged.
![JavaScript automation tools.](https://developer.chrome.com/static/blog/test-automation-evolution/image/javascript-automation-too-164b40e684111.png) JavaScript automation tools

## Automation approaches

Broadly, these tools can be organized into two major groups based on how they automate browsers:

- **High level** : Tools that execute JavaScript **within the browser** . For instance, [Cypress](https://bit.ly/cypress-architecture) and [TestCafe](https://bit.ly/testcafe-architecture) leverage web APIs and Node.js to run tests directly in the browser. Fun fact---the first version of [Selenium](https://www.selenium.dev/) also used the same approach.
- **Low level** : Tools that execute remote commands **outside of the browser** . When tools require even greater control, such as opening multiple tabs or simulating device mode, that's when they need to execute remote commands to control the browser via protocols. The two main automation protocols are **WebDriver "Classic"** and **Chrome DevTools Protocol (CDP)**.

In the next section, we will take a look at these two protocols to understand their strengths and limitations.

![WebDriver Classic and CDP.](https://developer.chrome.com/static/blog/test-automation-evolution/image/webdriver-classic-cdp-7f0963f43bf99.png)

## WebDriver "Classic" versus Chrome DevTools Protocol (CDP)

[WebDriver "Classic"](https://w3c.github.io/webdriver/) is a web standard supported by all major browsers. Automation scripts issue commands via HTTP requests to a driver server, which then communicates with browsers through internal, browser-specific protocols.

While it has excellent cross-browser support and its APIs are designed for testing, it can be slow and does not support some low-level controls.
![WebDriver 'Classic'.](https://developer.chrome.com/static/blog/test-automation-evolution/image/webdriver-classic-37cc82b8fb3d.png) WebDriver "Classic"

For example, imagine you have a test script that clicks on an element `await coffee.click();`. It is translated into a series of HTTP requests.

```bash
# WebDriver: Click on a coffee element

curl -X POST http://127.0.0.1:4444/session/:element_id/element/click
   -H 'Content-Type: application/json'
   -d '{}'
```

On the other hand, [Chrome DevTools Protocol (CDP)](https://chromedevtools.github.io/devtools-protocol) was initially designed for Chrome DevTools and debugging, but was adopted by [Puppeteer](https://pptr.dev/) for automation. CDP communicates directly with Chromium-based browsers through WebSocket connections, providing faster performance and low-level control.

However, it only works with Chromium-based browsers and is not an open standard. On top of that, CDP APIs are relatively complex. In some cases, working with CDP is not ergonomic. For example, working with out-of-process iframes takes a lot of effort.
![CDP.](https://developer.chrome.com/static/blog/test-automation-evolution/image/cdp-e8535120383e7.png) Chrome DevTools Protocol

For example, clicking on an element `await coffee.click();` is translated into a series of CDP commands.

```javascript
// CDP: Click on a coffee element

// Mouse pressed
{ 
  command: 'Input.dispatchMouseEvent', 
  parameters: {
    type: 'mousePressed', x: 10.34, y: 27.1, clickCount: 1 }
}

// Mouse released
{ 
  command: 'Input.dispatchMouseEvent', 
  parameters: {
    type: 'mouseReleased', x: 10.34, y: 27.1, clickCount: 1 }
}
```

## What are the low-level controls?

Back in the days when WebDriver "Classic" was developed, there wasn't a need for low-level control. But times have changed, the web is much more capable now, and testing today demands more fine-grained actions.

Since CDP was designed to cover all debugging needs, it supports more low-level controls compared to WebDriver "Classic". It's capable of handling features like:

- Capturing console messages
- Intercepting network requests
- Simulating device mode
- Simulating geolocation
- And more!

These weren't possible in WebDriver "Classic" because of the different architecture---WebDriver "Classic" is HTTP-based, making it tricky to subscribe and listen to browser events. CDP, on the other hand, is WebSocket-based, supporting bi-directional messaging by default.

## What's next: WebDriver BiDi

Here is a summary of the strengths of both WebDriver "Classic" and CDP:

| WebDriver "Classic" | Chrome DevTools Protocol (CDP) |
|---|---|
| Best cross-browser support | Fast, bi-directional messaging |
| W3C standard | Provides low-level control |
| Built for testing |   |

[WebDriver BiDi](https://developer.chrome.com/articles/webdriver-bidi) aims to combine the best aspects of WebDriver "Classic" and CDP. It's a new standard browser automation protocol currently under development.

Learn more about the [WebDriver BiDi project](https://developer.chrome.com/articles/webdriver-bidi)---how it works, the vision, and the standardization process.