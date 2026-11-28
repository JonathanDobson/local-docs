# Version selection is the process of matching a Chrome binary of a given version
to a compatible ChromeDriver binary.

## For versions 115 and newer

Starting with M115 the ChromeDriver release process is integrated with that of Chrome. The latest Chrome + ChromeDriver releases per release channel (Stable, Beta, Dev, Canary) are available at [the Chrome for Testing (CfT) availability dashboard](https://googlechromelabs.github.io/chrome-for-testing/). As a result, you might no longer have a need for version selection --- you could choose any available CfT version and download the correspondingly-versioned ChromeDriver binary.

For automated version downloading one can use the convenient [CfT JSON endpoints](https://github.com/GoogleChromeLabs/chrome-for-testing#json-api-endpoints).

If you still have a need for version selection (e.g. to match a non-CfT Chrome binary with a compatible ChromeDriver binary), look up the Chrome binary's `MAJOR.MINOR.BUILD` version in the `latest-patch-versions-per-build` [JSON endpoints](https://github.com/GoogleChromeLabs/chrome-for-testing#json-api-endpoints) to find the corresponding ChromeDriver version. If there is no entry for the `MAJOR.MINOR.BUILD` version yet, fall back to the `latest-versions-per-milestone` JSON endpoint instead.
Alternatively, you can use [the `LATEST_RELEASE_` endpoints at the new location](https://github.com/GoogleChromeLabs/chrome-for-testing#other-api-endpoints).

## For versions 114 and older

We maintain multiple versions of ChromeDriver. Which version to select depends on the version of Chrome you are using it with. Specifically:

- ChromeDriver uses the same version number scheme as Chrome. See https://www.chromium.org/developers/version-numbers for more details.
- Each version of ChromeDriver supports Chrome with matching major, minor, and build version numbers. For example, ChromeDriver `73.0.3683.20``supports all Chrome versions that start with`73.0.3683\`.
- Before a new major version of Chrome goes to Beta, a matching version of ChromeDriver will be released.
- After the initial release of a new major version, we will release patches as needed. These patches may or may not coincide with updates to Chrome.

Here are the steps to select the version of ChromeDriver to download:

- First, find out which version of Chrome you are using. Let's say you have Chrome `72.0.3626.81`\`.
- Take the Chrome version number, remove the last part, and append the result to URL `https://chromedriver.storage.googleapis.com/LATEST_RELEASE_`. For example, with Chrome version `72.0.3626.81`, you'd get a URL `https://chromedriver.storage.googleapis.com/LATEST_RELEASE_72.0.3626`.
- Use the URL created in the last step to retrieve a small file containing the version of ChromeDriver to use. For example, the above URL will get your a file containing `72.0.3626.69`. (The actual number may change in the future, of course.)
- Use the version number retrieved from the previous step to construct the URL to download ChromeDriver. With version `72.0.3626.69`, the URL would be `https://chromedriver.storage.googleapis.com/index.html?path=72.0.3626.69/`.
- After the initial download, it is recommended that you occasionally go through the above process again to see if there are any bug fix releases.

We always provide ChromeDriver for the current Stable and Beta versions of Chrome. However, if you use Chrome from Dev or Canary channel, or build your own custom version of Chrome, It is possible that there is no available ChromeDriver that officially supports it. In this case, please try the following:

- First, construct a LATEST_RELEASE URL using Chrome's major version number. For example, with Chrome version `73.0.3683.86`, use URL `https://chromedriver.storage.googleapis.com/LATEST_RELEASE_73`. Try to download a small file from this URL. If it successful, the file contains the ChromeDriver version to use.
- If the above step failed, reduce the Chrome major version by 1 and try again. For example, with Chrome version `75.0.3745.4`, use URL `https://chromedriver.storage.googleapis.com/LATEST_RELEASE_74` to download a small file, which contains the ChromeDriver version to use.
- You can also use [ChromeDriver Canary build](https://chromedriver.chromium.org/chromedriver-canary).

In addition, the version of ChromeDriver for the current stable release of Chrome can be found at [`https://chromedriver.storage.googleapis.com/LATEST_RELEASE`](https://chromedriver.storage.googleapis.com/LATEST_RELEASE). However, using this file may be less reliable than methods described above.