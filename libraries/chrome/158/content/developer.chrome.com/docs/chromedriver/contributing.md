# Contribute to ChromeDriver

ChromeDriver is a Chromium project and the code lives in the Chromium
repository. Chromium is the open source project on which Google Chrome is based.
Follow the [instructions](https://www.chromium.org/developers/how-tos/get-the-code/)
to check out the entire Chromium source tree.

After you have your source checkout, make sure you have completed all the build
prerequisites for your platform. You don't need to actually build Chrome
(which can take hours); you just need to get your machine setup properly.

See the per-platform instructions:

- [linux](http://code.google.com/p/chromium/wiki/LinuxBuildInstructions)
- [mac](http://code.google.com/p/chromium/wiki/MacBuildInstructions)
- [windows](http://www.chromium.org/developers/how-tos/build-instructions-windows)

## Build, test, and understand ChromeDriver

In your source checkout, refer to `src/chrome/test/chromedriver/README.md`
([latest README](https://source.chromium.org/chromium/chromium/src/+/master:chrome/test/chromedriver/README.md)).

## Report issues

Read about how to [file bugs at our issue tracker](https://developer.chrome.com/docs/chromedriver/help) and
[read the mailing list](https://groups.google.com/forum/#!forum/chromedriver-users).

## Contribute

Create a branch and use `git cl upload` to upload your patch for review. Then,
go to the web interface and publish it to an appropriate reviewer. Take a look
at the history of the file (and any OWNERS file) to determine an appropriate
reviewer. The reviewer will guide you in making changes, using the try server
and committing the code.