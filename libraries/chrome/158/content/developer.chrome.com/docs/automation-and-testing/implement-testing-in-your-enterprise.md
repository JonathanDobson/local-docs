# Implement testing in your enterprise with Chrome

Source: https://developer.chrome.com/docs/automation-and-testing/implement-testing-in-your-enterprise

![Demián Renzulli](https://web.dev/images/authors/demianrenzulli.jpg) Demián Renzulli [X](https://twitter.com/drenzulli) [GitHub](https://github.com/demianrenzulli) ![Matthias Rohmer](https://web.dev/images/authors/mrohmer.jpg) Matthias Rohmer [X](https://twitter.com/matthiasrohmer) [GitHub](https://github.com/matthiasrohmer) [LinkedIn](https://www.linkedin.com/in/matthias-rohmer-b09191b0) [Bluesky](https://bsky.app/profile/matthiasrohmer.bsky.social)

<br />

Imagine your company's most important software suddenly breaks---what would
happen? Orders could get lost, deadlines might be missed, but customers would
definitely be complaining.

This nightmare scenario is avoidable: by implementing a continuous and rigorous
testing process, that catches problems before they cause chaos. But implementing
such a process in your organization is easier said than done.

This document will show you everything you need to think about when getting
started with testing in your company, and how you can benefit from testing in
the long-term.

> [!NOTE]
> **Note:** This document covers guidance for product teams, as well as system administrators. While you can only read the guidance relevant to you, we encourage you to read it all. Gaining a better understanding of the individual challenges can help to overcome them collaboratively!

## Testing best practices for product teams

The first part of This document covers the process of starting to implement
testing in your workflow.

### Implement a testing culture in your team

Successfully introducing testing in your team requires that everyone shares a
common mindset, and sees quality not as a burden, but as an investment. This is
a process that, as every other cultural shift, requires time and consistency.

One thing that can help shape this culture are regular meetings to discuss
defects, the impact they had, where they came from, and what it took to get them
fixed. This helps to create awareness for why it's good to prevent such defects
in the first place.

Having a dedicated person in the team who oversees and drives the effort can
strongly increase the chance of success. Someone that defines team---or even
organization-wide---guidelines, collects best practices and shares them and
advocates for the effort across levels.

Another useful instrument can be to rotate the support role of your product.
Getting first-hand, unfiltered insights from your customers and learning about
the everyday problems they face with your product can be a valuable experience
for product managers, designers, and developers.

The goal is that everyone in your team understands that quality is a feature, as
important as any other functionality that you build for your product. Once
everyone adopted that mindset, it's a natural progression to understand that
tests are a feature as well. Because tests are what ensure the shipped quality.

### A step by step testing process

Once there is alignment between the different teams involved in product
development, you can further formalize the existence and usage of tests.

#### Make tests part of the "Definition of Done"

By adding tests as a feature requirement, you state a feature is not ready to
ship until it is properly and automatically tested

> [!TIP]
> **Tip:** We believe that automated testing can greatly improve product quality beyond what manual testing can provide. Learn more in [Tools from Chrome for
> frictionless, automated
> testing](https://developer.chrome.com/blog/tools-from-chrome-for-frictionless-testing).

#### Run tests regularly

Once implemented, automated tests can be your safeguard in every step of the
development process. They need no human intervention, and can be run on every
critical step of your development pipeline. For example:

- On every commit.
- On every pull request.
- After every full release or environment change.

If you are relying on third-party services in your production environment it can
even make sense to run your tests against production to ensure third-party APIs
behave as expected.

#### Define and collect metrics

Defining a set of metrics is important in order to measure the effectiveness of
your tests and the impact of testing workflows on your business. Here are some
examples of metrics that you can use:

- **Releases per month**: A higher number of releases per month can indicate a more agile development process. Automated testing plays a key role here by ensuring releases can proceed with confidence.
- **Bug reports**: A decreasing trend in bug reports can be a positive sign that your testing (and development processes) are effective.
- **Test coverage**: While never an exact metric, coverage can be a good indicator of how deeply you're testing critical use cases.

Note that these metrics are also influenced by other factors which might skew
them. For example, your release count might go down in a holiday season, while
bug reports go up. So don't rely on only a few and make sure to crossmap them
with other data available to your team.

When you successfully implement those steps with your team, your product health
will definitely benefit in the long term. But there still is more you can do!

## Testing best practices for system administrators

Product teams can't work on their own. They rely on the hardware, tools and
infrastructure maintained by system administrators. While system administrators
usually don't directly contribute to the product development, they can still
influence the development workflow for good. For example by actively managing
the browser version certain user groups in the company use.

This second part of the article explains how this works, using [Chrome's release channels](https://developer.chrome.com/docs/automation-and-testing/release-channels.md.txt)
and enterprise policies.

### Chrome release channels

There are four release channels: Stable, Beta, Dev, and Canary.

To learn more, see [Chrome release channels](https://developer.chrome.com/docs/automation-and-testing/release-channels.md.txt).

### Using channels in an exemplary organization

The structure of product teams varies among organizations, as there's no one
size fits all approach to software development. As an example we'll assume a
team with the following roles: Product Management, UX and UI, Engineering,
Operations and Support.

For an organization like this, you can think about the following channel split:

- **Product Management** : PMs can usually be on the **stable** channel, in order to use the same version as most users. Occasionally they could use the **beta or dev** channel if they are working on a feature that requires an API that has not been launched yet.
- **Engineering and UX** : Parts of these teams can be on the **dev** channel, to give them access to the latest features, like [View
  Transitions](https://developer.chrome.com/docs/web-platform/view-transitions), even before they are in stable.
- **Operations** : Could be on **beta**, to foresee breakage impacting users next.
- **Support** : Can stay on the **stable** channel, to make sure they are interacting with the product with the same browser as most of your customers.

![A diagram showing flow of channels throughout the example team](https://developer.chrome.com/static/docs/automation-and-testing/implement-testing-in-your-enterprise/image/team-channel-split.jpg)

> [!NOTE]
> **Note:** If you are a solo developer, not part of a big organization or any enterprise, we recommend to test on the **beta** channel of the browser, at least once per browser release, to not be surprised by changes to the ever-changing web platform.

### Use enterprise policies to manage channels

Rather than giving guidelines and leaving the decision about which channel to
use, Chrome also offers enterprise and administration tools to actively manage
which channel each user ends up using. This is useful as it immediately
increases the testing surface from a few individual to a deterministic set of
users, which helps identifying breakage as early as possible and in a traceable
way.

If you want to use that level of control, here is the configuration we would
recommend:

- **Employees (app users)** : To minimize the risk of disruption, most employees should be on the **stable** channel, which has been fully tested by the Chrome test team. Additionally, a small percentage of users (from 5 to 10%) can be on the **beta** channel. This channel gets a 4--6 week preview of Stable and can help admins to discover possible issues with a release, giving more time to address the issues before the release is rolled out to everyone else.
- **IT department** : Members of the IT department, including system admins themselves can be on the **beta** or **dev** channel to get a 4--6 or 9--12 week preview of what's coming to the stable version of Chrome.

![A diagram showing the split of channels between other employees and the IT department](https://developer.chrome.com/static/docs/automation-and-testing/implement-testing-in-your-enterprise/image/org-channel-split.jpg)

> [!NOTE]
> **Note:** It's not always you who is on the hook to fix what breaks. Sometimes Chrome itself can have a bug which is on us to fix. If you think that's the case, file it at [crbug.com](https://crbug.com).

### Long term release channels

Product development might not go as quickly as planned and Chrome's release
cadence of a month might be too high. For this use case Chrome provides an
Extended stable channel that allows to get feature updates less frequently, but
still receive security fixes. This channel is updated every eight weeks.

The following diagram shows how different milestones proceed through
[Chrome's different release channels](https://chromestatus.com/roadmap):

![A flow diagram showing the overlap of stable and extended stable versions](https://developer.chrome.com/static/docs/automation-and-testing/implement-testing-in-your-enterprise/image/extended-stable-flow.png)

- Both stable and extended stable ship the same versions for the first four weeks, after which the two diverge.
- There is no extended beta channel; instead, the standard four week beta cycle is used to stabilize both stable and extended stable. Enterprises who choose to opt into the eight week extended stable should continue to run the beta channel as they do today in order to proactively identify issues that may impact their environments.

## The continued importance of dev and beta channels for extended stable users

While the stable channel is accelerating to a two-week release cycle and your
organization is adopting the eight-week extended stable cycle to gain more time
for testing, it is still critical to use the dev and beta channels.
There are no separate "extended dev or beta" channels;
the standard dev and beta channels are used to stabilize both the stable and
extended stable releases.

By continuing to run the dev and beta channels,
enterprises maintain the ability to proactively identify issues that could
impact their environments. Dev and beta channels provide a four week preview of
the upcoming stable release. For extended stable users, this preview window is
essential for discovering and addressing potential breakage well in advance of the eight-week feature update.

The dev and beta channels essentially act as the primary early warning system
for any changes coming to your eight-week extended stable environment,
ensuring your enterprise apps remain compatible.
System administrators can continue to assign a small, deterministic group of
users (for example, 5-10% of app users) to the dev and beta channels to maximize this benefit.

## Conclusion

Testing is a crucial part of software development companies to ensure the
quality of their products and also an important step for system administrators,
to give employees of an organization access to high quality software and avoid
disrupting business processes.

In order to succeed when implementing a testing workflow inside your
organization it's important that everyone shares the common mindset that quality
and therefore testing is a feature.

In This document, we have reviewed different ways to integrate testing best
practices into your organization, for an in depth review of the existing testing
tools check out our article [Tools from Chrome for frictionless, automated
testing](https://developer.chrome.com/blog/tools-from-chrome-for-frictionless-testing).

For guidance to testing, from start to end, also check out our recent
[Learn Testing course](https://web.dev/learn/testing) and [test automation best practices](https://web.dev/explore/test-automation)
on web.dev.