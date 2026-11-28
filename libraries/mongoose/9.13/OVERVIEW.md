# Mongoose 9.13 — overview

Mongoose is the object modelling library for MongoDB on Node.js. You define **schemas**, compile
them into **models**, and get casting, validation, middleware (hooks), query building and
population (joins). This set covers the **9.13** line; the latest release is **9.13.1**
(2026-11-24). It needs Node.js ≥ 20.19.0 and uses MongoDB Node.js driver `~7.9`.
- Guides and API reference: every page in mongoosejs.com's `llms.txt`, fetched as the site's own
  Markdown. The site was built from **9.13.0** at fetch time.
- TypeScript declarations (`types/*.d.ts`) and `CHANGELOG.md`: from git tag `9.13.1`.
- Licence: MIT.

## Layout

| Folder | What it holds |
|---|---|
| `content/docs/` | Guides: `guide.md` (schemas and every schema option), `schematypes.md`, `connections.md`, `models.md`, `documents.md`, `subdocs.md`, `queries.md`, `validation.md`, `middleware.md`, `populate.md`, `discriminators.md`, `transactions.md`, `timestamps.md`, `plugins.md`, `change-streams.md`, `field-level-encryption.md`, `atlas-search.md`, `atlas-vector-search.md`, `faq.md`, `migrating_to_5…9.md`, `compatibility.md`, `deprecations.md`, plus Jest, Lambda, Next.js and browser notes |
| `content/docs/tutorials/` | Focused how-tos: `lean.md`, `findoneandupdate.md`, `virtuals.md`, `getters-setters.md`, `query_casting.md`, `custom-casting.md`, `dates.md`, `ssl.md` |
| `content/docs/typescript/` | TypeScript guides: schemas, statics and methods, query helpers, queries, populate, subdocuments, virtuals (intro in `content/docs/typescript.md`) |
| `content/docs/production/` | `indexes.md` |
| `content/api-reference/` | One page per class: `model.md`, `query.md`, `schema.md`, `document.md`, `connection.md`, `mongoose.md`, `aggregate.md`, `schematype.md`, `schematypeoptions.md`, the `schema<type>.md` / `schema<type>options.md` pages for each SchemaType, `virtualtype.md`, cursors, `error.md`… |
| `content/release-notes/CHANGELOG.md` | Full changelog, newest first (9.13.1 at the top) |
| `api/types/` | Mongoose's TypeScript declarations at 9.13.1 (`index.d.ts`, `models.d.ts`, `query.d.ts`, `inferschematype.d.ts`, `pipelinestage.d.ts`…). Not in the semantic search index; grep them (`rg 'QueryFilter' api/types`) |

## Where to look for…

- **Getting started / first model** → `docs/index.md`
- **Defining schemas, schema options (`strict`, `strictQuery`, `timestamps`, `toJSON`, `versionKey`, `defaultSort`, `autoSearchIndex`…)** → `docs/guide.md` (each option is a `## option: <name>` heading)
- **Field types and per-type options (`required`, `enum`, `min`, `index`, `unique`…)** → `docs/schematypes.md`, `api-reference/schematypeoptions.md`
- **Connecting, connection options, events, multiple connections, pools** → `docs/connections.md`, `api-reference/connection.md`, `api-reference/mongoose.md` (`connect()`)
- **A Model method's signature and options (`find`, `findOneAndUpdate`, `bulkWrite`, `insertMany`…)** → `api-reference/model.md`
- **Query builder methods, `lean()`, cursors** → `api-reference/query.md`, `docs/queries.md`, `docs/tutorials/lean.md`
- **Validation and custom validators** → `docs/validation.md`
- **Pre/post hooks** → `docs/middleware.md`
- **Populate (refs, `refPath`, virtual populate, deep populate)** → `docs/populate.md`
- **Transactions** → `docs/transactions.md`
- **TypeScript typing (`InferSchemaType`, generics, methods, statics)** → `docs/typescript.md`, `docs/typescript/`, `api/types/`
- **Upgrading 8 → 9** → `docs/migrating_to_9.md`
- **Which MongoDB server versions are supported** → `docs/compatibility.md`
- **What changed in a given release** → `release-notes/CHANGELOG.md`

## Version notes

From `docs/migrating_to_9.md` and the changelog:

- **Pre middleware no longer supports `next()`.** Use `async` functions or throw. `isAsync` middleware
  and callbacks in hooks for custom methods and statics are gone too.
- **Update pipelines are blocked by default** (`updateOne({}, [{ $set: … }])` throws); opt in with
  `updatePipeline: true`.
- **`new` and `returnOriginal` are deprecated** for `findOneAndUpdate()` / `findOneAndReplace()` (since
  9.2.0); use `returnDocument: 'after'`.
- `Schema.prototype.doValidate()` returns a promise. `mongoose.isValidObjectId()` returns false for
  numbers. UUIDs are now MongoDB driver UUID objects. The `background` index option and
  `skipOriginalStackTraces` were removed.
- **TypeScript:** `FilterQuery` is renamed `QueryFilter`, and its properties no longer resolve to `any`.
  `create()` and `insertOne()` no longer take a generic parameter, and document `id` is no longer `any`.
- **9.13.0** upgraded the driver to 7.9 and added the `defaultSort` schema option (a sort applied to
  every query unless one is given). **9.13.1** is fixes only (schema alias removal, `castNonArrays` on
  nested arrays, `$pull` error paths, `$vectorSearch` types).
- `docs/deprecations.md`: `Document.prototype.validateSync()` is deprecated and will be removed in
  Mongoose 10.

## Search tips

- API headings are written as `Model.findOneAndUpdate()` (statics) or `Document.prototype.save()`
  (instance methods). Search those exact forms.
- Schema options in `guide.md` are under headings named `option: <name>`.
- "Lean" = query results as plain JavaScript objects instead of Mongoose documents. "Discriminator" = schema
  inheritance in one collection. "Subdocument" = embedded document. "Virtual" = a computed property
  that isn't stored.
- Code fences labelled ` ```javascript acquit:<name> ` hold ordinary examples. The label names the test
  each example was taken from.
- `docs/version-support.md` gives old "latest release" numbers. Take versions from the changelog instead.
