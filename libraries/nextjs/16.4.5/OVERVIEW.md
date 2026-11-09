# Next.js 16.4.5 — overview

Next.js is Vercel's React framework for full-stack web apps: file-system routing,
server rendering and prerendering, caching, Server Functions, image/font/script
optimisation and the Turbopack bundler. This set is the official documentation at
the **v16.4.5** release tag (the latest stable release on 2026-11-09), taken from
the `docs/` folder of `github.com/vercel/next.js` — the same MDX source nextjs.org
renders — plus GitHub release notes for every stable 16.x release and the 16.0–16.4
announcement posts from nextjs.org/blog. See `manifest.json` for commits and gaps.

**Two routers.** Next.js has two routing systems. The **App Router** (`app/`
directory, `01-app/`) is the current one and where all new features land. The
**Pages Router** (`pages/` directory, `02-pages/`) is the **older router**: still
supported, but the docs recommend migrating to the App Router. Unless the question
is about a `pages/` project (`getServerSideProps`, `getStaticProps`, `_app.js`,
`_document.js`, API Routes), read `01-app/`.

## Layout

| Folder | What it holds |
|---|---|
| `content/index.mdx` | Docs home: what Next.js is, App Router vs Pages Router |
| `content/01-app/01-getting-started/` | The App Router tutorial path: installation, project structure, layouts and pages, linking, Server and Client Components, fetching/mutating data, caching, revalidating, error handling, CSS, images, fonts, metadata, route handlers, proxy, deploying, upgrading |
| `content/01-app/02-guides/` | ~80 task guides: authentication, data security, caching (with and without Cache Components), ISR, instant navigation, prefetching, streaming, forms/Server Actions, environment variables, self-hosting, deploying to platforms, static exports, internationalisation, testing (Jest, Vitest, Playwright, Cypress), migrating (from CRA, Vite, Pages Router), upgrading (v14, v15, v16, codemods, agent upgrade), AI agents and MCP |
| `content/01-app/api-reference/` | App Router API reference: `01-directives` (`use client`, `use server`, `use cache`, `use cache: private`, `use cache: remote`), `02-components` (Font, Form, Image, Link, Script), `03-file-conventions` (page, layout, route, proxy, error, loading, not-found, parallel/intercepting routes, `01-metadata` files, `02-route-segment-config`), `04-functions` (cookies, headers, cacheLife, cacheTag, updateTag, revalidatePath/Tag, redirect, navigation hooks, after, connection, ...), `05-config` (every `next.config.js` option, TypeScript, ESLint), `06-cli` (`create-next-app`, `next`), `07-adapters` (Build Adapters API) |
| `content/01-app/04-glossary.mdx` | Next.js's own glossary of terms |
| `content/02-pages/` | **Pages Router (older router)**: getting started, guides, `03-building-your-application` (routing, rendering, data fetching), `api-reference/` (components, file conventions, functions such as `getStaticProps`/`getServerSideProps`, config, CLI, adapters) |
| `content/03-architecture/` | Accessibility, Fast Refresh, the Next.js Compiler, supported browsers |
| `content/04-community/` | Contribution guide (how the docs are written), Rspack |
| `content/release-notes/v16.*.md` | GitHub release notes for all stable 16.x releases (v16.0.0–v16.4.5); mostly lists of PRs |
| `content/release-notes/blog/` | Announcement posts for 16, 16.1, 16.2, 16.3, 16.4 and companion posts (16.2/16.3 AI and Turbopack, 16.3 Instant Navigations) — the readable "what's new" |

Pages Router pages that nextjs.org shares with the App Router (those with a
`source:` key in their frontmatter) were filled in with the shared text, keeping
only the Pages-Router-specific parts, as the website does. Each App Router page has
had its Pages-Router-only parts removed, and vice versa.

## Where to look for…

| Task | File(s) |
|---|---|
| Create a project, system requirements | `01-app/01-getting-started/01-installation.mdx`, `01-app/api-reference/06-cli/create-next-app.mdx` |
| Routing: layouts, pages, dynamic segments, route groups, parallel/intercepting routes | `01-app/01-getting-started/03-layouts-and-pages.mdx`, `01-app/api-reference/03-file-conventions/` (`layout.mdx`, `page.mdx`, `dynamic-routes.mdx`, `route-groups.mdx`, `parallel-routes.mdx`, `intercepting-routes.mdx`, `default.mdx`) |
| Server vs Client Components, `'use client'` | `01-app/01-getting-started/05-server-and-client-components.mdx`, `01-app/02-guides/server-and-client-boundary.mdx`, `01-app/api-reference/01-directives/use-client.mdx` |
| Data fetching, streaming, Suspense | `01-app/01-getting-started/06-fetching-data.mdx`, `01-app/02-guides/streaming.mdx`, `01-app/api-reference/04-functions/fetch.mdx` |
| Caching with Cache Components (`'use cache'`, `cacheLife`, `cacheTag`) | `01-app/01-getting-started/08-caching.mdx`, `01-app/api-reference/01-directives/use-cache.mdx`, `04-functions/cacheLife.mdx`, `04-functions/cacheTag.mdx`, `05-config/01-next-config-js/cacheComponents.mdx`, `01-app/02-guides/migrating-to-cache-components.mdx` |
| Caching in apps **without** Cache Components (older model) | `01-app/02-guides/caching-without-cache-components.mdx`, `04-functions/unstable_cache.mdx` |
| Revalidation (`updateTag`, `revalidateTag`, `revalidatePath`, `refresh`) | `01-app/01-getting-started/09-revalidating.mdx`, `01-app/02-guides/how-revalidation-works.mdx`, matching files in `01-app/api-reference/04-functions/` |
| Mutations, forms, Server Actions | `01-app/01-getting-started/07-mutating-data.mdx`, `01-app/02-guides/forms.mdx`, `01-app/02-guides/server-actions.mdx`, `01-directives/use-server.mdx` |
| API endpoints (Route Handlers) | `01-app/01-getting-started/15-route-handlers.mdx`, `03-file-conventions/route.mdx`, `04-functions/next-request.mdx`, `next-response.mdx` |
| Proxy (formerly Middleware) | `01-app/01-getting-started/16-proxy.mdx`, `03-file-conventions/proxy.mdx` (`middleware.mdx` covers the deprecated name) |
| Request data: cookies, headers, params, searchParams | `04-functions/cookies.mdx`, `headers.mdx`, `03-file-conventions/page.mdx`, `04-functions/next-root-params.mdx` |
| Errors, not-found, loading states | `01-app/01-getting-started/10-error-handling.mdx`, `03-file-conventions/error.mdx`, `not-found.mdx`, `loading.mdx`, `04-functions/catchError.mdx` |
| Metadata, SEO, OG images, sitemap, robots | `01-app/01-getting-started/14-metadata-and-og-images.mdx`, `04-functions/generate-metadata.mdx`, `03-file-conventions/01-metadata/` |
| Authentication and data security | `01-app/02-guides/authentication.mdx`, `authentication-with-cache-components.mdx`, `data-security.mdx` |
| `next.config.js` options | `01-app/api-reference/05-config/01-next-config-js/<option>.mdx` (one file per option, e.g. `images.mdx`, `turbopack.mdx`, `redirects.mdx`, `output.mdx`) |
| CLI (`next dev/build/start/upgrade`, flags) | `01-app/api-reference/06-cli/next.mdx` |
| Environment variables | `01-app/02-guides/environment-variables.mdx` |
| Deploying and self-hosting | `01-app/01-getting-started/17-deploying.mdx`, `01-app/02-guides/self-hosting.mdx`, `deploying-to-platforms.mdx`, `01-app/api-reference/07-adapters/` |
| Upgrading to 16, breaking changes, codemods | `01-app/02-guides/upgrading/version-16.mdx`, `upgrading/codemods.mdx`, `upgrading/agent-upgrade.mdx` |
| Pages Router data fetching (`getStaticProps`, `getServerSideProps`, `getStaticPaths`) | `02-pages/03-building-your-application/03-data-fetching/`, `02-pages/api-reference/03-functions/` |
| Moving from Pages Router to App Router | `01-app/02-guides/migrating/app-router-migration.mdx` |

## Version notes

From `01-app/02-guides/upgrading/version-16.mdx`, the release-notes blog posts and
API pages' "Version History" tables:

- **16.0 (breaking):** minimum Node.js `20.9.0` and TypeScript `5.1.0`; Turbopack is
  the default bundler for `next dev` and `next build` (opt out with `--webpack`);
  `turbopack` config moved from `experimental` to top level. Request-time APIs are
  async only — `await params`, `await searchParams`, `await cookies()`,
  `await headers()`, `await draftMode()`. `middleware.ts` is deprecated and renamed
  `proxy.ts`. `cacheComponents` became a top-level stable option (replacing
  `experimental.dynamicIO` / `experimental.useCache` / `experimental.ppr`).
  `revalidateTag(tag)` needs a second `cacheLife` profile argument; new `updateTag()`
  and `refresh()`. Removed: AMP, `next lint` (use ESLint or Biome directly),
  `serverRuntimeConfig`/`publicRuntimeConfig`, `unstable_rootParams`. Parallel route
  slots need an explicit `default.js`. `next/image` defaults changed
  (`minimumCacheTTL` 4 hours, `qualities` `[75]`, `16` removed from `imageSizes`,
  `maximumRedirects` 3, local IPs blocked unless `dangerouslyAllowLocalIP`; local
  `src` with query strings needs `images.localPatterns`); `images.domains` and
  `next/legacy/image` deprecated. React 19.2.
- **16.1:** Turbopack file-system caching for `next dev`, experimental bundle
  analyzer, `next dev --inspect`.
- **16.2:** `unstable_catchError()` and the `unstable_retry` prop for `error.tsx`,
  `transitionTypes` prop on `next/link`, `next start --inspect`.
- **16.3:** Instant Navigations (Partial Prefetching via `partialPrefetching`, the
  `instant` route segment export), `catchError` and the `error.js` `retry` prop
  became stable, `next/root-params` and `io()` added, `agentRules` config,
  TypeScript 7 type checking, lower dev memory.
- **16.4:** Cache Components recommended for every app and on by default in
  `create-next-app` (App Router); `ensureStatic` route segment config;
  `next upgrade --agent`, `experimental.agentUpgrade` and `experimental.agentFeedback`;
  React 19.3; smaller Turbopack disk cache and production bundles.

## Search tips

- Pages use site URLs in links: `/docs/app/api-reference/functions/cookies` is
  `content/01-app/api-reference/04-functions/cookies.mdx` (folders carry `NN-`
  ordering prefixes; `index.mdx` is the folder's own page).
- **Cache Components** is the name of the current caching/rendering model
  (`cacheComponents: true`, `'use cache'`, `cacheLife`, `cacheTag`). Questions about
  older `fetch` caching, `export const revalidate`/`dynamic`, or `unstable_cache`
  belong to "caching without Cache Components".
- **Partial Prerendering (PPR)** = a static shell plus streamed dynamic parts; there
  is no separate `ppr` flag any more. **Partial Prefetching** is a different thing
  (what `<Link>` prefetches).
- **Proxy** = what was called **Middleware** (`proxy.ts`).
- **Request-time APIs** = `cookies()`, `headers()`, `searchParams`, `draftMode()`
  (older pages and codemods call them "Dynamic APIs").
- **Server Function** = any `'use server'` function; a **Server Action** is a
  Server Function used as a form action or passed to a Client Component.
- **Route Handler** = an App Router `route.ts` endpoint; **API Routes** are the
  Pages Router equivalent (`pages/api/`).
- Code blocks have `filename="..."` and `switcher` attributes; most examples exist
  in both TypeScript and JavaScript.
- Next.js's own definitions: `content/01-app/04-glossary.mdx`.
