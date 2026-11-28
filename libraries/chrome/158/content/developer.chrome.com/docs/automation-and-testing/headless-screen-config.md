# Configure virtual screens in Headless mode

Source: https://developer.chrome.com/docs/automation-and-testing/headless-screen-config

![Peter Kvitek](https://web.dev/images/authors/peterkvitek.jpg) Peter Kvitek

<br />

Chrome Headless Mode (`chrome --headless`)
(and the old Headless Shell (`chrome-headless-shell`)) use a fully configurable
virtual headless screen which is independent of physical displays attached to
the system Chrome is running on. Initial headless screen configuration can be
specified using the --screen-info [command line switch](https://chromium.googlesource.com/chromium/src/+/main/components/headless/screen_info/README.md).
This switch defines properties like origin, size, scale factor, orientation, and
work area for each display.

While Chrome is running in headless mode, virtual headless screens can be added
and removed using [Chrome DevTools Protocol](https://chromedevtools.github.io/devtools-protocol/) (CDP) commands
[Emulation.addScreen](https://chromedevtools.github.io/devtools-protocol/tot/Emulation/#method-addScreen)
and [Emulation.removeScreen](https://chromedevtools.github.io/devtools-protocol/tot/Emulation/#method-removeScreen).

These new Headless Chrome capabilities are fully supported by Puppeteer,
letting you automate complex, real-world display scenarios that were
previously hard to test. Whether you need to verify a kiosk application
running full-screen on a high-resolution 3K display, orchestrate
multi-window workflows across a dual-monitor setup, or ensure your UI
adapts gracefully when a user suddenly disconnects a secondary screen,
Headless Chrome and Puppeteer now have you covered.

### Test static screen configurations

Use static screen configuration through the `--screen-info` switch to evaluate
your website within a static screen environment. The following are a list of
common scenarios:

- Test behavior with `--start-maximized` and `--start-fullscreen` switches, considering screen work area and scale factor (e.g., kiosk mode).
- Evaluate `element.requestFullscreen()` and `document.exitFullscreen()` behavior across various screen sizes and in multiscreen configurations.
- Observe split-screen behavior when a window spans multiple screens or is moved between them.
- Verify the handling of diverse display settings, including scaling, resolutions, and high-DPI displays.
- Assess the opening of windows or pop-ups on primary and secondary screens.

#### Dual screen configuration

The following [Puppeteer](https://pptr.dev/) script configures Chrome to run in
a dual-screen configuration using the `--screen-info` switch. The primary
800x600 screen is configured in a landscape orientation and the secondary
600x800 screen, positioned directly to the right of the primary screen, is in a
portrait orientation.

```javascript
import puppeteer from 'puppeteer-core';

const browser = await puppeteer.launch({
  args: ['--screen-info={800x600 label=1st}{600x800 label=2nd}'],
});

const screens = await browser.screens();
const screenInfos = screens.map(
    s =>  `Screen [${s.id}]`

+   ` ${s.left},${s.top} ${s.width}x${s.height}`
+   ` label='${s.label}'`
+   ` isPrimary=${s.isPrimary}`
+   ` isExtended=${s.isExtended}`
+   ` isInternal=${s.isInternal}`
+   ` colorDepth=${s.colorDepth}`
+   ` devicePixelRatio=${s.devicePixelRatio}`
+   ` avail=${s.availLeft},${s.availTop} ${s.availWidth}x${s.availHeight}`
+   ` orientation.type=${s.orientation.type}`
+   ` orientation.angle=${s.orientation.angle}`
);

console.log(`Number of screens: ${screens.length}\n` + screenInfos.join('\n'));

await browser.close();
```

**Output**:

    Number of screens: 2
    Screen [1] 0,0 800x600 label='1st' isPrimary=true isExtended=true isInternal=false colorDepth=24 devicePixelRatio=1 avail=0,0 800x600 orientation.type=landscapePrimary orientation.angle=0
    Screen [2] 800,0 600x800 label='2nd' isPrimary=false isExtended=true isInternal=false colorDepth=24 devicePixelRatio=1 avail=800,0 600x800 orientation.type=portraitPrimary orientation.angle=0

### Test dynamic screen configurations

Dynamically configure your screen environment to test how your website reacts to
unexpected monitor connections or disconnections, mirroring real-world user
actions like connecting a notebook to a desktop monitor. These scenarios are
emulated using [CDP](https://chromedevtools.github.io/devtools-protocol/)
commands as
[Emulation.addScreen](https://chromedevtools.github.io/devtools-protocol/tot/Emulation/#method-addScreen)
and
[Emulation.removeScreen](https://chromedevtools.github.io/devtools-protocol/tot/Emulation/#method-removeScreen).
With these commands, you can do the following:

- Verify that connecting a new monitor enables web pages to open new windows and pop-ups within the new monitor's work area.
- Ensure that when a monitor is disconnected while a web page is active, its window size and position adapt gracefully to the remaining displays.

#### Open and maximize the window on a new screen

The following [Puppeteer](https://pptr.dev/) script opens a window at the
default position on a 800x600 screen, then moves and maximizes the window to a
newly created screen. It then restores the window to its normal state.

```javascript
import puppeteer from 'puppeteer-core';

const browser = await puppeteer.launch({
  args: ['--screen-info={800x600}'],
});

async function logWindowBounds() {
  const bounds = await browser.getWindowBounds(windowId);
  console.log(`${bounds.left},${bounds.top}` +
     ` ${bounds.width}x${bounds.height}` +
     ` ${bounds.windowState}`);
}

const page = await browser.newPage({type: 'window'});
const windowId = await page.windowId();
await logWindowBounds();

const screenInfo = await browser.addScreen({
  left: 800,
  top: 0,
  width: 1600,
  height: 1200,
});

await browser.setWindowBounds(windowId, {
  left: screenInfo.left + 50,
  top: screenInfo.top + 50,
  width: screenInfo.width - 100,
  height: screenInfo.height - 100,
});
await logWindowBounds();

await browser.setWindowBounds(windowId, {windowState: 'maximized'});
await logWindowBounds();

await browser.setWindowBounds(windowId, {windowState: 'normal'});
await logWindowBounds();

await browser.close();
```

**Output**:

    20,20 780x580 normal
    850,50 1500x1100 normal
    800,0 1600x1200 maximized
    850,50 1500x1100 normal

### More use cases, examples and availability

[Find more code samples on pptr.dev](https://pptr.dev/category/guides). If you
are encountering issues, let us know through Puppeteer's [public bug tracker on GitHub](https://github.com/puppeteer/puppeteer).

Headless screen configuration functionality is available in stable Chrome
releases starting from version 142.