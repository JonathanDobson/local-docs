# Chrome release channels

Source: https://developer.chrome.com/docs/automation-and-testing/release-channels

![Demián Renzulli](https://web.dev/images/authors/demianrenzulli.jpg) Demián Renzulli [X](https://twitter.com/drenzulli) [GitHub](https://github.com/demianrenzulli) ![Matthias Rohmer](https://web.dev/images/authors/mrohmer.jpg) Matthias Rohmer [X](https://twitter.com/matthiasrohmer) [GitHub](https://github.com/matthiasrohmer) [LinkedIn](https://www.linkedin.com/in/matthias-rohmer-b09191b0) [Bluesky](https://bsky.app/profile/matthiasrohmer.bsky.social)

<br />

By default Chrome auto-updates to ensure every user is running the latest, most
stable and secure version of Chrome including every latest feature---the version
of Chrome released on the stable channel.

As a company developing a web-based product you may want to use a browser version ahead
of the stable channel, to give your product teams time to adapt your product to
changes to the web platform.

For this use case Chrome offers a total of four release channels, intended for
different user groups.

> [!NOTE]
> **Note:** All major browser vendors offer something close to the concept of Chrome's release channels.

In the case of Chrome, there are different release channels that you can use, to
anticipate future browser changes and test the latest features before they are
widely available:

- **Stable channel** : This is where most of the users are. The stable channel automatically updates when there is a new [Chrome release](https://developer.chrome.com/release-notes), which happens monthly.
- **Beta channel**: This version will become stable in four to six weeks, giving you a chance to preview and test an upcoming stable release and prepare for it.
- **Dev channel**: This channel gets a new version of Chrome once a week and includes all the latest fixes that will eventually move into beta. As the channel name suggests, it's in development and might therefore break unexpectedly---but it also includes the newest features, sometimes long before they make their way into stable. That makes the dev channel a great tool for prototyping and cutting-edge development.
- **Canary channel**: The most experimental channel, containing every latest feature but without much testing. At least released daily.

If you want to learn more about Chrome's channels, checkout the relevant
[Chrome Concepts episode](https://www.youtube.com/watch?v=WL1guL5n9PU&list=PLNYkxOF6rcIBzsbjZKyOdO-iwQTjidz1P&index=7).

![The product icons of Chrome stable, beta and dev together with their description.](https://developer.chrome.com/static/docs/automation-and-testing/release-channels/image/channels-overview.jpg)

See [What are Chrome release channels?](https://developer.chrome.com/docs/web-platform/chrome-release-channels.md.txt) to learn more about Chrome release channels.

## Chrome for Testing

![](https://developer.chrome.com/docs/chrome-for-testing/image/Wn5kQQRVssFAHozIWDX3.svg)

Chrome provides a solution for reliable downloads for browser automation called [Chrome for Testing](https://developer.chrome.com/docs/automation-and-testing/chrome-for-testing.md.txt). This isn't a channel but a dedicated Chrome flavor that specifically targets web app testing and automation use cases.