# Jest 29.7 — overview

Jest is a JavaScript test framework (test runner, assertion library and mocking in one).
This set is the official jestjs.io documentation for the **29.7** line (newest release
**v29.7.0**), from `jestjs/jest` `website/versioned_docs/version-29.7` (main, commit
`aa88f7c`), plus the `jest-each` package README and the 29.x changelog from the `v29.7.0` tag.

## Layout

- `content/docs/` — the 37 site pages (Getting Started, guides, API reference, CLI,
  Configuration).
- `content/packages/jest-each/README.md` — the `jest-each` README at v29.7.0 (the engine behind
  `test.each` / `describe.each`), including asynchronous each-tests with `done`.
- `content/release-notes/CHANGELOG-29.x.md` — CHANGELOG sections 29.0.0 to 29.7.0.

## Where to look for…

| Task | File |
|---|---|
| `test` / `it`, `describe`, `.only`, `.skip`, `.todo`, `.concurrent` | `content/docs/GlobalAPI.md` |
| `test.each` / `it.each` / `describe.each` (array table and tagged template, `%s`/`$var` titles, per-row timeout) | `content/docs/GlobalAPI.md` (`### test.each(table)(name, fn, timeout)`) |
| Each-test that takes `done` (the extra argument after the row's values) | `content/packages/jest-each/README.md` (`#### Asynchronous .test(name, fn(done))`) |
| `done` callbacks, promises, async/await, `.resolves`/`.rejects` | `content/docs/TestingAsyncCode.md`, `content/docs/GlobalAPI.md` |
| `beforeAll` / `afterAll` / `beforeEach` / `afterEach`, scoping and order | `content/docs/SetupAndTeardown.md`, `content/docs/GlobalAPI.md` |
| Timeouts: per-test `timeout` argument, `jest.setTimeout`, `testTimeout` config (default 5000 ms), `--testTimeout` | `content/docs/GlobalAPI.md`, `content/docs/JestObjectAPI.md`, `content/docs/Configuration.md`, `content/docs/CLI.md` |
| `--runInBand` (`-i`), `--forceExit`, `--detectOpenHandles`, `--maxWorkers`, `--watch` | `content/docs/CLI.md` |
| `jest.spyOn`, `jest.fn`, `jest.mock`, `jest.restoreAllMocks`, fake timers | `content/docs/JestObjectAPI.md` |
| `mockImplementation`, `mockReturnValue`, `mockResolvedValue`, `mock.calls`, `mockRestore` | `content/docs/MockFunctionAPI.md`, `content/docs/MockFunctions.md` |
| Module mocks (`__mocks__`), ES6 class mocks, `jest.requireActual` | `content/docs/ManualMocks.md`, `content/docs/Es6ClassMocks.md`, `content/docs/BypassingModuleMocks.md` |
| Matchers (`toBe`, `toEqual`, `toThrow`, `toHaveBeenCalledWith`, asymmetric matchers) | `content/docs/ExpectAPI.md`, `content/docs/UsingMatchers.md` |
| Config file options (`testEnvironment`, `setupFiles`, `globalSetup`, `globalTeardown`, `testMatch`) | `content/docs/Configuration.md` |
| Jest not exiting / open handles / slow tests | `content/docs/Troubleshooting.md`, `content/docs/CLI.md` |
| Testing with MongoDB / DynamoDB | `content/docs/MongoDB.md`, `content/docs/DynamoDB.md` |
| Upgrading from 28 | `content/docs/UpgradingToJest29.md` |

## Version notes

- 29.7.0 is a small release: `create-jest` initialiser (`npm init jest@latest`), deprecation warnings
  for unknown options in `jest-validate`, and fixes (`moduleNameMapper` unmatched capture
  groups, inline snapshot strings). See `content/release-notes/CHANGELOG-29.x.md`.
- Jest 29 itself (from `UpgradingToJest29.md`): changed default snapshot format
  (`snapshotFormat`), JSDOM upgrade, `pretty-format` changes, TypeScript changes; see that page
  for the supported Node.js versions.
- Newer lines (30.x) exist on jestjs.io; this set is 29.7 only.

## Search tips

- Global API headings include the signature, e.g. `` ### `test.each(table)(name, fn, timeout)` ``,
  `` ### `jest.spyOn(object, methodName)` ``, `` ### `mockFn.mockImplementation(fn)` ``.
- `it` is an alias of `test`; `it.each` is documented under `test.each`.
- `--forceExit` is documented as an escape hatch; the page points to `--detectOpenHandles` to
  find what keeps Jest running.
- `--runInBand` runs tests serially in the current process instead of a worker pool.
