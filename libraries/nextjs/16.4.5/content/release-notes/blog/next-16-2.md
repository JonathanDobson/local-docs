---
title: Next.js 16.2
description: Next.js 16.2 includes Adapters, rendering performance improvements, improved debugging and error pages, and more.
url: "https://nextjs.org/blog/next-16-2"
docs_index: /docs/llms.txt
publishedAt: March 18th 2026
authors:
  - Jimmy Lai
  - Tim Neutkens
---



Next.js 16.2 includes performance improvements, better debugging, improvements for Agents, and over 200 Turbopack fixes and improvements.

- [**Faster Time-to-URL**](#faster-time-to-url-in-development): ~400% faster `next dev` startup
- [**Faster Rendering**](#faster-rendering): ~50% faster rendering
- [**New Default Error Page**](#new-default-error-page): Redesigned built-in 500 page
- [**Server Function Logging**](#server-function-logging): Dev terminal logs for Server Function execution
- [**Hydration Diff Indicator**](#hydration-diff-indicator): Clear server/client diff in the error overlay
- [**`--inspect` for `next start`**](#--inspect-for-next-start): Attach the Node.js debugger to your production server

We also published dedicated deep-dive posts for two major areas of this release:

- [**Turbopack**](/blog/next-16-2-turbopack): Faster builds, SRI support, `postcss.config.ts`, tree shaking improvements, Server Fast Refresh, and 200+ bug fixes
- [**AI Improvements**](/blog/next-16-2-ai): `AGENTS.md` in `create-next-app`, browser log forwarding, and `next-browser` (experimental)

Upgrade today, or get started with:

```bash filename="terminal"
# Use the automated upgrade CLI
npx @next/codemod@canary upgrade latest

# ...or upgrade manually
npm install next@latest react@latest react-dom@latest

# ...or start a new project
npx create-next-app@latest
```

## Faster Time-to-URL in Development

We've significantly improved the time it takes before `localhost:3000` is ready during `next dev`. On the same machine and project, startup is ~87% faster compared to Next.js 16.1 on the default application.

## Faster Rendering

We [contributed a change](https://github.com/facebook/react/pull/35776) to React that makes Server Components payload deserialization up to 350% faster. The previous implementation used a `JSON.parse` reviver callback, which crosses the C++/JavaScript boundary in V8 for every key-value pair in the parsed JSON. Even a trivial no-op reviver makes `JSON.parse` roughly 4x slower than without one.

The new approach uses a two-step process: plain `JSON.parse()` followed by a recursive walk in pure JavaScript. This eliminates the boundary-crossing overhead and adds optimizations like short-circuiting plain strings that don't need transformation.

In real-world Next.js applications, this translates to 25% to 60% faster rendering to HTML, depending on the RSC payload size.

<ComparisonChart
  title="Server render time"
  ariaLabel="Server render time comparison showing improvements"
  groups={[
    {
      label: 'Server Component Table with 1000 items',
      improvement: '26% faster',
      ariaLabel: 'Server Component Table render times',
      bars: [
        {
          label: 'Before',
          value: '19ms',
          percentage: 100,
          ariaLabel: 'Before: 19 milliseconds',
        },
        {
          label: 'After',
          value: '15ms',
          percentage: 80.3,
          ariaLabel: 'After: 15 milliseconds',
        },
      ],
    },
    {
      label: 'Server Component with nested Suspense',
      improvement: '33% faster',
      ariaLabel: 'Server Component with nested Suspense render times',
      bars: [
        {
          label: 'Before',
          value: '80ms',
          percentage: 100,
          ariaLabel: 'Before: 80 milliseconds',
        },
        {
          label: 'After',
          value: '60ms',
          percentage: 75,
          ariaLabel: 'After: 60 milliseconds',
        },
      ],
    },
    {
      label: 'Payload CMS homepage',
      improvement: '34% faster',
      ariaLabel: 'Payload CMS homepage render times',
      bars: [
        {
          label: 'Before',
          value: '43ms',
          percentage: 100,
          ariaLabel: 'Before: 43 milliseconds',
        },
        {
          label: 'After',
          value: '32ms',
          percentage: 74.4,
          ariaLabel: 'After: 32 milliseconds',
        },
      ],
    },
    {
      label: 'Payload CMS with rich text',
      improvement: '60% faster',
      ariaLabel: 'Payload CMS with rich text render times',
      bars: [
        {
          label: 'Before',
          value: '52ms',
          percentage: 100,
          ariaLabel: 'Before: 52 milliseconds',
        },
        {
          label: 'After',
          value: '33ms',
          percentage: 63.5,
          ariaLabel: 'After: 33 milliseconds',
        },
      ],
    },
  ]}
/>

## New Default Error Page

The default error page shown in production has been redesigned. When your application encounters an error and you haven't defined a custom `global-error.tsx` or `error.tsx`, Next.js renders a built-in fallback page. This fallback has been updated with a cleaner, more modern design.

<figure>
  <div className="overflow-hidden" style={{ aspectRatio: '1024 / 620' }}>
    <Image
      srcLight="/static/blog/next-16-2/updated_error_page_light_2.png"
      srcDark="/static/blog/next-16-2/updated_error_page_dark.png"
      width={1024}
      height={822}
    />
  </div>
  <figcaption>The redesigned default error page in Next.js 16.2</figcaption>
</figure>

## Server Function Logging

Next.js now logs Server Function execution in the terminal during development. Each log shows the function name, its arguments, execution time, and the file it's defined in.

<figure>
  <div className="overflow-hidden" style={{ aspectRatio: '1024 / 500' }}>
    <Image
      srcDark="/static/blog/next-16-2/server_fn_log_dark.png"
      srcLight="/static/blog/next-16-2/server_fn_log_light_2.png"
      width={1024}
      height={685}
    />
  </div>
  <figcaption>
    Server Function execution logs in the development terminal
  </figcaption>
</figure>

## Hydration Diff Indicator

When a hydration mismatch occurs, the error overlay now clearly labels which content came from the server and which from the client. The diff uses a `+ Client` / `- Server` legend, making it immediately clear what diverged.

<figure>
  <Image
    srcDark="/static/blog/next-16-2/hydration_pure_dark.png"
    srcLight="/static/blog/next-16-2/hydration_diff_light.png"
    width={1024}
    height={576}
  />
  <figcaption>
    The hydration diff indicator showing client/server content differences
  </figcaption>
</figure>

## `--inspect` for `next start`

Next.js 16.1 introduced `next dev --inspect` for attaching the Node.js debugger during development. In 16.2, this extends to `next start`, allowing you to attach a Node.js debugger to your production server.

```bash filename="terminal"
next start --inspect
```

This is useful for debugging issues or profiling CPU and memory usage.

For more information on how to use the Node.js debugger, see the [Chrome documentation](https://developer.chrome.com/docs/devtools/performance/nodejs).

## `transitionTypes` Prop for `next/link`

The `<Link>` component now accepts a [`transitionTypes`](https://react.dev/reference/react/addTransitionType) prop — an array of strings that specifies the types of View Transitions to apply when navigating. Each type is passed to `React.addTransitionType` during the navigation Transition, allowing you to trigger different animations based on the navigation direction or context.

```tsx
<Link href="/about" transitionTypes={['slide']}>
  About
</Link>
```

This is only supported in the App Router, since the Pages Router does not use React Transitions for navigation. `transitionTypes` on Pages Router links is silently ignored, so shared link components work across both routers.

To learn more about view transitions, see the [documentation](/docs/app/api-reference/config/next-config-js/viewTransition).

## Faster `ImageResponse`

`ImageResponse` has been updated with significant improvements:

- **2x faster** `ImageResponse` for basic images, up to **20x faster** for complex images
- Improved CSS and SVG coverage, including support for inline CSS variables, `text-indent`, `text-decoration-skip-ink`, `box-sizing`, `display: contents`, `position: static`, and percentage values for `gap`
- Default font changed from Noto Sans to Geist Sans

Learn more about [ImageResponse](/docs/app/api-reference/functions/image-response).

## Error Causes in the Dev Overlay

The error overlay now displays `Error.cause` chains, making it easier to debug errors that wrap other errors. Causes are shown in a flat list below the top-level error, up to 5 levels deep.

<figure>
  <Image
    srcDark="/static/blog/next-16-2/error_trace_dark.png"
    srcLight="/static/blog/next-16-2/error_trace_light.png"
    width={1024}
    height={738}
  />
  <figcaption>The error overlay showing the full error cause chain</figcaption>
</figure>

## Adapters

[Adapters](/docs/app/api-reference/config/next-config-js/adapterPath) are now stable. This is a new API that allows platforms to customize the build process.

This is useful for deployment platforms or custom build integrations that need to modify the Next.js configuration or process the build output.

We will share a more detailed overview of Adapters next week.

## Multiple Icon Formats

Multiple icon files with the same base name but different extensions are now handled automatically in your app directory (e.g., `icon.png` and `icon.svg`). This is useful for browser fallback support. Modern browsers can use SVG icons while older browsers fall back to PNG. Both formats are rendered as separate `<link>` tags.

## Experimental Features

### `unstable_catchError()`

Extending the error recovery experience with the [`error.js`](/docs/app/api-reference/file-conventions/error) file convention, [`unstable_catchError()`](/docs/app/api-reference/functions/catchError) provides more granular control of the error boundaries on the component level. By creating a custom error boundary using `unstable_catchError()`, you can place it anywhere in your component tree.

Compared to a custom React error boundary, `unstable_catchError()` is designed to work with Next.js out of the box:

- **Built-in error recovery**: [`unstable_retry()`](/docs/app/api-reference/file-conventions/error#unstable_retry) re-renders the page from the server in transition.
- **Framework-aware integration**: APIs like `redirect()` and `notFound()` work by throwing special errors under the hood. `unstable_catchError()` handles these seamlessly, so they're not accidentally caught by your error boundary.
- **Client navigation handling**: The error state automatically clears when you do a client navigation to a different route.

The error boundary created by `unstable_catchError()` receives the props passed from the call site and the `ErrorInfo` value as the second argument, which is the same shape as the props passed to the `error.js` file convention.

Just like `error.js`, `unstable_catchError()` can only be called from [Client Components](/docs/app/getting-started/server-and-client-components).

```tsx filename="app/custom-error-boundary.tsx"
'use client';

import { unstable_catchError, type ErrorInfo } from 'next/error';

function CustomErrorBoundary(
  props: { title: string },
  { error, unstable_retry }: ErrorInfo,
) {
  return (
    <div>
      <h2>{props.title}</h2>
      <p>{error.message}</p>
      <button onClick={() => unstable_retry()}>Try again</button>
    </div>
  );
}

export default unstable_catchError(CustomErrorBoundary);
```

```tsx filename="app/page.tsx"
import CustomErrorBoundary from './custom-error-boundary';

export default function Page() {
  return (
    <CustomErrorBoundary title="Oops! Something went wrong!">
      <Component />
    </CustomErrorBoundary>
  );
}
```

### `unstable_retry()` in `error.tsx`

A new [`unstable_retry()`](/docs/app/api-reference/file-conventions/error#unstable_retry) prop is now available in `error.tsx` components. Previously, the `reset()` prop only cleared the error state and re-rendered the children, which works for temporary rendering errors but doesn't help when the error originates from data fetching or the RSC phase.

`unstable_retry()` calls `router.refresh()` and `reset()` within a `startTransition()`, providing built-in retry logic that re-fetches data and re-renders the segment. This is expected to be preferred over `reset()` for most error recovery scenarios.

```tsx filename="app/error.tsx"
'use client';

import type { ErrorInfo } from 'next/error';

export default function Error({ error, unstable_retry }: ErrorInfo) {
  return (
    <div>
      <h2>Something went wrong</h2>
      <p>{error.message}</p>
      <button onClick={() => unstable_retry()}>Try again</button>
    </div>
  );
}
```

### `experimental.prefetchInlining`

Next.js 16 introduced per-segment prefetching, where the client issues individual requests for each segment in the route tree. This improves cache efficiency as shared layouts between sibling routes are fetched once and reused, but increases request volume.

The new `experimental.prefetchInlining` option bundles all segment data for a route into a single response, reducing the number of prefetch requests to one per link. The trade-off is that shared layout data is duplicated across inlined responses rather than being cached and reused.

```ts filename="next.config.ts"
const nextConfig = {
  experimental: {
    prefetchInlining: true,
  },
};

export default nextConfig;
```

This is a stepping stone toward a size-based heuristic where small segments are inlined automatically and larger segments remain separate.

### `experimental.cachedNavigations`

This flag independently controls the Cached Navigations behavior, which caches static and dynamic Server Components data from navigations and the initial HTML loads so that repeat visits can be served instantly. Requires `cacheComponents` to be enabled.

### `experimental.appNewScrollHandler`

A reworked scroll and focus management system for App Router using React Fragment refs. The new handler improves how focus is managed after navigations. Instead of focusing the first focusable descendant deep within a segment (which could skip past content), it now blurs the active element, matching how browser navigations work.

```ts filename="next.config.ts"
const nextConfig = {
  experimental: {
    appNewScrollHandler: true,
  },
};

export default nextConfig;
```

## Feedback and Community

Share your feedback and help shape the future of Next.js:

- [GitHub Discussions](https://github.com/vercel/next.js/discussions)
- [GitHub Issues](https://github.com/vercel/next.js/issues)
- [Discord Community](https://nextjs.org/discord)

## Contributors

Next.js is the result of the combined work of over 3,770 individual developers. This release was brought to you by:

- The **Next.js** team: [Andrew](https://github.com/acdlite), [Hendrik](https://github.com/unstubbable), [Janka](https://github.com/lubieowoce), [Jiachi](https://github.com/huozhi), [Jimmy](https://github.com/feedthejim), [Jiwon](https://github.com/devjiwonchoi), [JJ](https://github.com/ijjk), [Josh](https://github.com/gnoff), [Jude](https://github.com/gaojude), [Sam](https://x.com/samselikoff), [Sebbie](https://github.com/eps1lon), [Tim](https://github.com/timneutkens), and [Zack](https://github.com/ztanner).
- The **Turbopack** team: [Benjamin](https://github.com/bgw), [Andrew](https://github.com/andrewimm), [Luke](https://github.com/lukesandberg), [Niklas](https://github.com/mischnic), [Tobias](https://github.com/sokra), and [Will](https://github.com/wbinnssmith).
- The **Next.js Docs** team: [Delba](https://github.com/delbaoliveira), [Rich](https://github.com/molebox), [Ismael](https://github.com/ismaelrumzan), [Joseph](https://github.com/icyJoseph) and [Aurora](https://github.com/aurorascharff).

Huge thanks to @acdlite, @unstubbable, @mischnic, @sokra, @ztanner, @mmastrac, @bgw, @lukesandberg, @wyattjoh, @huozhi, @eps1lon, @jwueller, @brookemosby, @delbaoliveira, @icyJoseph, @gaojude, @hanzala-sohrab, @dango0812, @ijjk, @msmx-mnakagawa, @Juneezee, @davidgolden, @LucianBuzzo, @devjiwonchoi, @alexcarpenter, @jaffarkeikei, @BradErz, @mintydev789, @naaa760, @Suhaib3100, @pavan-sh, @amannn, @fireairforce, @JamBalaya56562, @wheresrhys, @ericrav, @lubieowoce, @Thomas465xd, @bgub, @wbinnssmith, @Netail, @robert-j-webb, @bencmbrook, @shadcn, @sigmachirality, @abhishekmardiya, @vvscode, @feedthejim, @freek-boon-greenberry, @andrewimm, @alubbe, @FurryR, @01-binary, @andrewdamelio, @swarnava, @gnoff, @kristiyan-velkov, @styfle, @haydenbleasel, @rishishanbhag, @tdarthur, @lavanitha, and @karlhorky for helping!
