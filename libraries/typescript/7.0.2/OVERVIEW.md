# TypeScript 7.0.2 — overview

TypeScript is a typed superset of JavaScript; `tsc` type-checks it and compiles it to
JavaScript. **7.0.2** is the latest stable release (npm `latest`, released 2026-08-20). It is the
native port of the compiler, written in Go (codename **Corsa**; the old JavaScript-based compiler
is **Strada**). 7.0 is meant to give the same types and errors as **6.0**, and
removes the options 6.0 deprecated. These docs come from three places:

- the typescriptlang.org source (`microsoft/TypeScript-Website`, branch `v2`, commit `bfee36f`,
  CC-BY-4.0). The site is unversioned and **still builds against 6.0.3**, so the handbook and TSConfig
  reference describe 6.0
- release notes up to 6.0, from the same repo
- `CHANGES.md` + `README.md` from `microsoft/typescript-go` at tag `typescript/v7.0.2`, which list the
  intentional differences between 7.0 and 6.0

The 7.0 announcement blog post is **not** included because of its licence (see `manifest.json` gaps).
On machines that have it, the **local-only** set `libraries/typescript-blog/7.0/` (listed in `INDEX.local.md`, not in git) holds that post and the other official TypeScript 7 posts. Search it with `-l typescript-blog` for questions about adopting 7.0: the missing compiler API, running 7.0 alongside 6.0 for typescript-eslint, `--checkers`/`--builders`, editor support, and Vue, Svelte and Angular.

## Layout

| Folder | What it holds |
|---|---|
| `content/handbook/handbook-v2/` | The current Handbook: Basics, Everyday Types, Narrowing, More on Functions, Object Types, Classes, Modules, `Type Manipulation/` (generics, keyof, typeof, indexed access, conditional, mapped, template literal types) |
| `content/handbook/handbook-v1/` | Older handbook pages still on the site (Basic Types, Interfaces, …) |
| `content/handbook/get-started/` | "TS for JS Programmers", "…for OOPers", "…for Functional Programmers", "…for the New Programmer" |
| `content/handbook/reference/` | Utility Types, Decorators, Enums, JSX, Declaration Merging, Mixins, Namespaces, Symbols, Triple-Slash Directives, Type Compatibility, Type Inference, Iterators and Generators |
| `content/handbook/modules-reference/` | Modules Theory, Reference (`module` and `moduleResolution` options), guides/Choosing Compiler Options, appendices/ESM-CJS-Interop |
| `content/handbook/declaration-files/` | Writing and publishing `.d.ts` files, plus `templates/` |
| `content/handbook/javascript/` | Type-checking JS files, JSDoc Reference, creating `.d.ts` from JS |
| `content/handbook/project-config/` | `tsconfig.json`, Compiler Options (tsc CLI flags with types and defaults), Project References, Configuring Watch, build-tool integration, MSBuild |
| `content/handbook/tutorials/` | React, Angular, Babel, Gulp, DOM manipulation, migrating from JavaScript, ASP.NET Core |
| `content/tsconfig-reference/options/` | One page per tsconfig option (136), e.g. `strict.md`, `moduleResolution.md`, `paths.md` |
| `content/tsconfig-reference/sections/`, `categories/` | Text for the top-level tsconfig sections (`compilerOptions`, `watchOptions`, `typeAcquisition`, `buildOptions`) and option categories |
| `content/release-notes/` | "TypeScript X.Y.md" for 1.1 → 6.0 |
| `content/typescript-7/` | `CHANGES.md` (7.0 vs 6.0 intentional changes), `README.md` (tsgo repo README) |
| `api/tsconfig.schema.json` | JSON Schema for `tsconfig.json` (option descriptions, types, enums) |

## Where to look for…

- **Basic types, unions, type aliases vs interfaces** → `handbook/handbook-v2/Everyday Types.md`
- **Narrowing, type guards, discriminated unions, `never`** → `handbook/handbook-v2/Narrowing.md`
- **Generics, keyof, conditional / mapped / template literal types** → `handbook/handbook-v2/Type Manipulation/`
- **Built-in utility types (`Partial`, `Pick`, `Omit`, `Record`, `ReturnType`, `Awaited`, `NoInfer`…)** → `handbook/reference/Utility Types.md`
- **What one tsconfig option does** → `tsconfig-reference/options/<optionName>.md`
- **CLI flags with type and default** → `handbook/project-config/Compiler Options.md`
- **Choosing `module` / `moduleResolution` (`nodenext`, `bundler`…), ESM vs CommonJS** → `handbook/modules-reference/guides/Choosing Compiler Options.md`, `modules-reference/Reference.md`, `appendices/ESM-CJS-Interop.md`
- **Monorepos / `tsc --build`** → `handbook/project-config/Project References.md`
- **Writing or publishing `.d.ts` types for a library** → `handbook/declaration-files/` (start at `Introduction.md`, then `Publishing.md`)
- **Using TypeScript checking in plain JS via JSDoc** → `handbook/javascript/JSDoc Reference.md`, `Type Checking JavaScript Files.md`
- **Decorators** → `handbook/reference/Decorators.md`
- **Upgrading to 6.0 / preparing for 7.0** → `release-notes/TypeScript 6.0.md` ("Breaking Changes and Deprecations in TypeScript 6.0", "Preparing for TypeScript 7.0")
- **What behaves differently in 7.0 (the Go compiler)** → `typescript-7/CHANGES.md`
- **What a given older version added** → `release-notes/TypeScript X.Y.md`

## Version notes

- **7.0 is the Go port (Corsa).** According to the typescript-go README, it uses the same module
  resolution, types and errors as TS 6.0 (types in error messages may print differently).
  `CHANGES.md` lists the intentional differences. Most of them are in **JavaScript/JSDoc support**:
  Closure-specific features are gone, constructor functions in JS are no longer supported,
  `@class`/`@constructor` no longer makes a constructor function, and declaration emit for JS is
  closer to TS. There are also a few checker changes, for example: with `"strict": false` you can no
  longer omit arguments for parameters typed `undefined`, `unknown` or `any`.
- **Everything 6.0 deprecated is removed in 7.0.** In 6.0, `"ignoreDeprecations": "6.0"` silences the
  warnings; 7.0 doesn't support those options at all. Deprecated in 6.0: `target: es5`,
  `--downlevelIteration`, `--moduleResolution node`/`node10` and `classic`, `amd`/`umd`/`systemjs`
  values of `module`, `--baseUrl`, `outFile`, `--esModuleInterop false`, `--alwaysStrict false`, the old
  `module` keyword for namespaces, `asserts` on imports, and `no-default-lib` directives.
- **6.0 changed defaults:** `strict` is now `true`, `module` is `esnext`, `target` is the latest ES
  version (`es2025`), `noUncheckedSideEffectImports` is `true`, `libReplacement` is `false`,
  `rootDir` is `.`, and `types` is `[]`. Many projects need `"types": ["node"]` and an explicit
  `"rootDir": "./src"`. Also new in 6.0: `--stableTypeOrdering`, `es2025` target/lib, `Temporal`
  types, `RegExp.escape`, subpath imports starting with `#/`, and `bundler` resolution combined with
  `module commonjs`. Passing files on the command line when a `tsconfig.json` exists is now an error.
- Some TSConfig option pages still give pre-6.0 defaults (for example `options/rootDir.md`). Where
  they disagree with `release-notes/TypeScript 6.0.md`, the release notes are right.

## Search tips

- Option pages are named exactly after the tsconfig key, in camelCase (`noUncheckedIndexedAccess.md`,
  `verbatimModuleSyntax.md`). Search for the key itself.
- **Corsa** = the TS 7 Go compiler; **Strada** = the old TS ≤6 JavaScript compiler. `tsgo` was the
  command name in the preview package `@typescript/native-preview`; since 7.0 RC the command is `tsc`.
- Code samples use the site's **twoslash** markers: `// @errors: 2322` lists the error codes the sample
  is expected to produce, and `// ^?` asks the site to show the type at that point. They are not
  part of the language.
- "Expando" = a property declared just by assigning to it (`f.called = false`); this matters for the 7.0 JS changes.
- Release-note headings are the feature names (e.g. "The `satisfies` Operator"), so searching the
  feature plus "release notes" usually finds the version that introduced it.
