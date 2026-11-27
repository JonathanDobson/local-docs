# Canary

| **Warning:** If you're using Chrome version 115 or newer, consult the [Chrome for Testing availability dashboard](https://googlechromelabs.github.io/chrome-for-testing/).

ChromeDriver Canary has the latest new ChromeDriver features. New binaries are
built and made available multiple times a day.

Be aware, it's designed for developers and early adopters and can
sometimes break down completely.

Starting with M115 the latest Chrome + ChromeDriver releases per release
channel, including Canary, are available at the Chrome for Testing availability
dashboard. For automated version downloading one can use the convenient JSON
endpoints.

For earlier versions, you can find the Canary builds as follows:

- [Linux (64-bit)](https://commondatastorage.googleapis.com/chromium-browser-snapshots/index.html?prefix=Linux_x64/)
- [Mac OS X (64-bit)](https://commondatastorage.googleapis.com/chromium-browser-snapshots/index.html?prefix=Mac/)
- [Mac ARM (64-bit)](https://commondatastorage.googleapis.com/chromium-browser-snapshots/index.html?prefix=Mac_Arm/)
- [Windows (32-bit)](https://commondatastorage.googleapis.com/chromium-browser-snapshots/index.html?prefix=Win/)

It's generally a good idea to pick the latest build. In each of those folders,
there is a file named `LAST_CHANGE`, that you can use to find the latest build
number. Open one of the Canary builds, dependent on your system
architecture, and type `LAST_CHANGE` in the filter box near the top. It may take
the site some time to locate the file (up to a minute). When the `LAST_CHANGE`
file link appears, click it to download the file, and find a build number
inside it. Then type that build number into the filter box, and click the
folder link that appears.
| **Note:** The Canary builds list only provides ChromeDriver built on Feb 21, 2019 or later.