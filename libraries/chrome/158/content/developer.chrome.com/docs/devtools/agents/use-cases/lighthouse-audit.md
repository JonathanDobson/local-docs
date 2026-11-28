# Automate Lighthouse audits with AI agents

Source: https://developer.chrome.com/docs/devtools/agents/use-cases/lighthouse-audit

![Matthias Rohmer](https://web.dev/images/authors/mrohmer.jpg) Matthias Rohmer [X](https://twitter.com/matthiasrohmer) [GitHub](https://github.com/matthiasrohmer) [LinkedIn](https://www.linkedin.com/in/matthias-rohmer-b09191b0) [Bluesky](https://bsky.app/profile/matthiasrohmer.bsky.social) ![José Luis Zapata](https://web.dev/images/authors/zapata.jpg) José Luis Zapata [GitHub](https://github.com/zapata131) [LinkedIn](https://www.linkedin.com/in/zapata131) [Bluesky](https://bsky.app/profile/zapata131.bsky.social) [Homepage](https://www.zapata131.com)

<br />

[Video](https://www.youtube.com/watch?v=2q9d7ANaXeA)

Lighthouse in Chrome DevTools for agents lets your coding agent evaluate website
quality by performing live health checks for accessibility, SEO, best practices,
and agentic browsing.

In an agentic workflow, your coding agent uses Lighthouse audits to identify
specific, measurable runtime issues rather than searching your codebase randomly
for general improvements.

This targeted approach provides actionable advice directly within your agent's
context, allowing your coding agent to find and fix bugs more accurately than
broad, static searches across your codebase.

Lighthouse audits focus on these main categories:

- **Accessibility (a11y)**: Ensures your site is usable by everyone, including people who use screen readers.
- **SEO**: Runs technical checks to ensure search engines can find and understand your content.
- **Best practices**: Confirm your site follows modern web development standards.
- **Agentic browsing**: Measure how much AI assistants can understand and interact with your website.

> [!NOTE]
> **Note:** To learn more about Lighthouse and how it helps you improve the quality of your web pages, see the [Lighthouse
> documentation](https://developer.chrome.com/docs/lighthouse).

When using Lighthouse, keep the following in mind:

- **Local and staging support** : Your agent can audit any page visible in Chrome, including local development servers and local HTML files accessed through the `file://` protocol.
- **Browser behavior**: Audits may briefly disrupt your view. You might see the page resize or reload as the tool simulates different devices.

## Audit web quality

Use the following workflows and examples to integrate Lighthouse into your
development process.

> [!NOTE]
> **Note:** Agent execution steps are examples of potential behavior. Your agent may act differently.

### Verify accessibility

When you change a UI, task your agent with verifying that the page remains
accessible.

**Example prompt:**

    How can I improve accessibility on this page as measured by Lighthouse?

**Example agent execution:** Your agent triggers a Lighthouse audit with
`formFactor` set to `mobile`. It analyzes the results, such as insufficient
color contrast or missing [ARIA
labels](https://developer.mozilla.org/docs/Web/Accessibility/ARIA/Reference/Attributes/aria-label),
and suggests specific code fixes.

### Audit SEO for search visibility

Technical SEO requirements are often caught too late in the development cycle.
You can ask your agent to find and fix technical blockers while you build.

**Example prompt:**

    According to Lighthouse audit, how can I improve this page for better discoverability in search?

**Example agent execution:** Your agent runs the SEO audit and identifies
missing meta tags, canonical links, or descriptive text. It can then offer to
update the source code to resolve the audit failure.

### Validate best practices

Ensure your local server or staging site adheres to security and technical best
practices.

**Example prompt:**

    Does my site follow best practices as measured by Lighthouse?

**Example agent execution:** Your agent reviews technical aspects like HTTPS
usage, console errors, and deprecated API calls reported by Lighthouse.

### General site improvement

You can run full Lighthouse audits of your site and help you define improvement
areas in early stages of development.

**Example prompt:**

    Run a full Lighthouse audit of my site, in mobile and desktop, and suggest improvement areas and possible fixes for any problems you find.

**Example agent execution:** Your agent runs a full Lighthouse audit of your
site in both mobile and desktop and suggests changes that could improve the
scores of the different audits. If your agent has full contextual knowledge of
the source code, it may directly suggest fixes. If it has access to the right
context, it can also suggest how to improve server configuration or other
backend configuration.