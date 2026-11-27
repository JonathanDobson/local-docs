# Emulate user experiences with AI agents

Source: https://developer.chrome.com/docs/devtools/agents/use-cases/emulation

![Matthias Rohmer](https://web.dev/images/authors/mrohmer.jpg) Matthias Rohmer [X](https://twitter.com/matthiasrohmer) [GitHub](https://github.com/matthiasrohmer) [LinkedIn](https://www.linkedin.com/in/matthias-rohmer-b09191b0) [Bluesky](https://bsky.app/profile/matthiasrohmer.bsky.social) ![José Luis Zapata](https://web.dev/images/authors/zapata.jpg) José Luis Zapata [GitHub](https://github.com/zapata131) [LinkedIn](https://www.linkedin.com/in/zapata131) [Bluesky](https://bsky.app/profile/zapata131.bsky.social) [Homepage](https://www.zapata131.com)

<br />

[Video](https://www.youtube.com/watch?v=kFi1yuGlCcA)

Chrome DevTools for agents lets your agent verify responsive layouts, test
location-aware APIs, and simulate varied CPU or network speeds. Use these tools
to identify edge cases and automate performance audits more effectively.

These emulation features work with other tools that enable your agent to
interact with your site such as clicking elements, filling forms, and navigating
pages.

Things you can emulate include:

- [**Viewport**](https://developer.mozilla.org/docs/Web/CSS/Guides/CSSOM_view/Viewport_concepts) **and [user
  agent](https://developer.mozilla.org/docs/Web/HTTP/Reference/Headers/User-Agent):** Emulate specific screen sizes and device identifiers.
- **Geolocation:** Spoof location coordinates to test location-aware APIs.
- **Network and CPU:** Throttle network conditions and CPU speed to simulate real-world performance constraints.
- **Color scheme:** Toggle between light and dark modes.

When using emulation, keep the following in mind:

- **Device support:** Your agent can emulate any device in the [Puppeteer's
  `KnownDevices`
  list](https://github.com/puppeteer/puppeteer/blob/main/docs/api/puppeteer.knowndevices.md). This includes simulating touch events for mobile viewports.
- **Browser engine behavior**: While the tool emulates device characteristics, it does not simulate non-Chromium browser engines or different operating systems. Your agent always executes in Chrome in your current operating system.

## Use cases for user emulation

Instruct your agent to emulate environments and verify the UI for you, rather
than manually resizing browsers, spoofing IPs, or throttling networks after
every code change.

Integrate emulation into your development process with these workflows.

> [!NOTE]
> **Note:** Agent execution steps are examples of potential behavior. Your agent may act differently.

### Iterate on responsive design

Navigation patterns often change drastically between mobile and desktop form
factors. As you build your application, you can instruct your agent to verify
that the components it just wrote render correctly and provide the same content
across devices.

**Example prompt:**

    Go to developer.chrome.com. Click the burger menu on mobile, check the top level
    items and ensure the same items are available for a desktop device.

**Example agent execution:** Your agent opens a Chrome window, navigates to the
page, starts emulation, and compares items across both viewports. It confirms
that the mobile view (Burger Menu) and the desktop view (Header) contain
the expected links.

### Validate cross-viewport interactions

Layouts break during interactions, not just in the CSS. Static screenshots often
miss bugs that happen when users actually touch the UI. You can task your agent
with testing specific interaction flows across multiple viewports to catch
hidden functional bugs.

**Example prompt:**

    Go to https://developer.chrome.com/ on mobile, tablet and desktop device, type
    in a search query but don't submit it and wait for the type-ahead suggestions.
    Ensure the Sign in button is visible all the time. Let me know if that's not the
    case.

**Example agent execution:** Your agent types in a search query and resizes the
screen to each of the three sizes. In this example, your agent catches that on
tablet and mobile, the search bar expands to fill the entire width of the
header, obscuring the **Sign in** link.

### Prototype location-aware features

Testing APIs that rely on the user's physical location (like "Near Me" searches
or store locators) usually requires you to manually override sensors. Now, you
can instruct your agent to spoof specific geolocations to verify your frontend
and backend logic frictionlessly.

**Example prompt:**

    Go to chrome.dev/devtools-store-locator. Search for Berlin, and confirm there's
    a store showing. Confirm there's no store for Washington. Finally, simulate
    Paris as location and verify there are stores listed.

**Example agent execution:** Your agent navigates to the site, searches for
Berlin, and then dynamically injects specific latitude and longitude coordinates
to emulate Paris, before interacting with the **Use My Location** feature to
ensure the correct stores populate.