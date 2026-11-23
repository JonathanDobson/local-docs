# Jest changelog — 29.x (from CHANGELOG.md at tag v29.7.0)

## 29.7.0

### Features

- `[create-jest]` Add `npm init` / `yarn create` initialiser for Jest projects ([#14465](https://github.com/jestjs/jest/pull/14453))
- `[jest-validate]` Allow deprecation warnings for unknown options ([#14499](https://github.com/jestjs/jest/pull/14499))

### Fixes

- `[jest-resolver]` Replace unmatched capture groups in `moduleNameMapper` with empty string instead of `undefined` ([#14507](https://github.com/jestjs/jest/pull/14507))
- `[jest-snapshot]` Allow for strings as well as template literals in inline snapshots ([#14465](https://github.com/jestjs/jest/pull/14465))
- `[@jest/test-sequencer]` Calculate test runtime if `perStats.duration` is missing ([#14473](https://github.com/jestjs/jest/pull/14473))

### Performance

- `[@jest/create-cache-key-function]` Cache access of `NODE_ENV` and `BABEL_ENV` ([#14455](https://github.com/jestjs/jest/pull/14455))

### Chore & Maintenance

- `[jest-cli]` Move internal config initialisation logic to the `create-jest` package ([#14465](https://github.com/jestjs/jest/pull/14453))

## 29.6.4

### Fixes

- `[jest-core]` Fix typo in `scheduleAndRun` performance marker ([#14434](https://github.com/jestjs/jest/pull/14434))
- `[jest-environment-node]` Make sure `atob` and `btoa` are writeable in Node 20 ([#14446](https://github.com/jestjs/jest/pull/14446))
- `[jest-worker]` Additional error wrapper for `parentPort.postMessage` to fix unhandled `DataCloneError`. ([#14437](https://github.com/jestjs/jest/pull/14437))

## 29.6.3

### Fixes

- `[expect, @jest/expect-utils]` `ObjectContaining` support `sumbol` as key ([#14414](https://github.com/jestjs/jest/pull/14414))
- `[expect]` Remove `@types/node` from dependencies ([#14385](https://github.com/jestjs/jest/pull/14385))
- `[jest-core]` Use workers in watch mode by default to avoid crashes ([#14059](https://github.com/facebook/jest/pull/14059) & [#14085](https://github.com/facebook/jest/pull/14085)).
- `[jest-reporters]` Update `istanbul-lib-instrument` dependency to v6. ([#14401](https://github.com/jestjs/jest/pull/14401))
- `[jest-mock]` Revert [#13692](https://github.com/jestjs/jest/pull/13692) as it was a breaking change ([#14429](https://github.com/jestjs/jest/pull/14429))
- `[jest-mock]` Revert [#13866](https://github.com/jestjs/jest/pull/13866) as it was a breaking change ([#14429](https://github.com/jestjs/jest/pull/14429))
- `[jest-mock]` Revert [#13867](https://github.com/jestjs/jest/pull/13867) as it was a breaking change ([#14429](https://github.com/jestjs/jest/pull/14429))
- `[@jest/reporters]` Marks Reporter's hooks as optional ([#14433](https://github.com/jestjs/jest/pull/14433))
- `[jest-runtime]` Fix dynamic ESM import module bug when loaded module through `jest.isolateModulesAsync` ([#14397](https://github.com/jestjs/jest/pull/14397))

### Chore & Maintenance

- `[jest-changed-files, jest-circus, jest-console, @jest/core, @jest/runtime, @jest/transform]` Use `invariant` and `notEmpty` from `jest-util` rather than own internal ([#14366](https://github.com/jestjs/jest/pull/14366))

## 29.6.2

### Fixes

- `[jest-circus]` Fix snapshot matchers in concurrent tests when nr of tests exceeds `maxConcurrency` ([#14335](https://github.com/jestjs/jest/pull/14335))
- `[@jest/core]` When running global setup and teardown, do not try to change the `message` property of the thrown error object when the `message` property is unwritable ([#14113](https://github.com/jestjs/jest/pull/14113))
- `[jest-snapshot]` Move `@types/prettier` from `dependencies` to `devDependencies` ([#14328](https://github.com/jestjs/jest/pull/14328))
- `[jest-snapshot]` Throw an explicit error if Prettier v3 is used ([#14367](https://github.com/jestjs/jest/pull/14367))
- `[jest-reporters]` Add "skipped" and "todo" symbols to Github Actions Reporter ([#14309](https://github.com/jestjs/jest/pull/14309))

### Chore & Maintenance

- `[@jest/core]` Use `pluralize` from `jest-util` rather than own internal ([#14322](https://github.com/jestjs/jest/pull/14322))

## 29.6.1

### Fixes

- `[jest-circus]` Revert [#14110](https://github.com/jestjs/jest/pull/14110) as it was a breaking change ([#14304](https://github.com/jestjs/jest/pull/14304))

## 29.6.0

### Features

- `[jest-circus, jest-snapshot]` Add support for snapshot matchers in concurrent tests ([#14139](https://github.com/jestjs/jest/pull/14139))
- `[jest-cli]` Include type definitions to generated config files ([#14078](https://github.com/facebook/jest/pull/14078))
- `[jest-snapshot]` Support arrays as property matchers ([#14025](https://github.com/facebook/jest/pull/14025))
- `[jest-core, jest-circus, jest-reporter, jest-runner]` Added support for reporting about start individual test cases using jest-circus ([#14174](https://github.com/jestjs/jest/pull/14174))

### Fixes

- `[jest-circus]` Prevent false test failures caused by promise rejections handled asynchronously ([#14110](https://github.com/jestjs/jest/pull/14110))
- `[jest-config]` Handle frozen config object ([#14054](https://github.com/facebook/jest/pull/14054))
- `[jest-config]` Allow `coverageDirectory` and `collectCoverageFrom` in project config ([#14180](https://github.com/jestjs/jest/pull/14180))
- `[jest-core]` Always use workers in watch mode to avoid crashes ([#14059](https://github.com/facebook/jest/pull/14059)).
- `[jest-environment-jsdom, jest-environment-node]` Fix assignment of `customExportConditions` via `testEnvironmentOptions` when custom env subclass defines a default value ([#13989](https://github.com/facebook/jest/pull/13989))
- `[jest-matcher-utils]` Fix copying value of inherited getters ([#14007](https://github.com/facebook/jest/pull/14007))
- `[jest-mock]` Tweak typings to allow `jest.replaceProperty()` replace methods ([#14008](https://github.com/facebook/jest/pull/14008))
- `[jest-mock]` Improve user input validation and error messages of `spyOn` and `replaceProperty` methods ([#14087](https://github.com/facebook/jest/pull/14087))
- `[jest-runtime]` Bind `jest.isolateModulesAsync` to `this` ([#14083](https://github.com/facebook/jest/pull/14083))
- `[jest-runtime]` Forward `wrapperLength` to the `Script` constructor as `columnOffset` for accurate debugging ([#14148](https://github.com/facebook/jest/pull/14148))
- `[jest-runtime]` Guard `_isMockFunction` access with `in` ([#14188](https://github.com/facebook/jest/pull/14188))
- `[jest-snapshot]` Fix a potential bug when not using prettier and improve performance ([#14036](https://github.com/facebook/jest/pull/14036))
- `[@jest/transform]` Do not instrument `.json` modules ([#14048](https://github.com/facebook/jest/pull/14048))
- `[jest-worker]` Restart a shut down worker before sending it a task ([#14015](https://github.com/facebook/jest/pull/14015))

### Chore & Maintenance

- `[*]` Update `semver` dependency to get vulnerability fix ([#14262](https://github.com/jestjs/jest/pull/14262))
- `[docs]` Updated documentation for the `--runTestsByPath` CLI command ([#14004](https://github.com/facebook/jest/pull/14004))
- `[docs]` Updated documentation regarding the synchronous fallback when asynchronous code transforms are unavailable ([#14056](https://github.com/facebook/jest/pull/14056))
- `[docs]` Update jest statistics of use and downloads in website Index.

## 29.5.0

### Features

- `[jest-changed-files]` Support Sapling ([#13941](https://github.com/facebook/jest/pull/13941))
- `[jest-circus, @jest/cli, jest-config]` Add feature to randomize order of tests via CLI flag or through the config file([#12922](https://github.com/facebook/jest/pull/12922))
- `[jest-cli, jest-config, @jest/core, jest-haste-map, @jest/reporters, jest-runner, jest-runtime, @jest/types]` Add `workerThreads` configuration option to allow using [worker threads](https://nodejs.org/dist/latest/docs/api/worker_threads.html) for parallelization ([#13939](https://github.com/facebook/jest/pull/13939))
- `[jest-cli]` Export `yargsOptions` ([#13970](https://github.com/facebook/jest/pull/13970))
- `[jest-config]` Add `openHandlesTimeout` option to configure possible open handles warning. ([#13875](https://github.com/facebook/jest/pull/13875))
- `[@jest/create-cache-key-function]` Allow passing `length` argument to `createCacheKey()` function and set its default value to `16` on Windows ([#13827](https://github.com/facebook/jest/pull/13827))
- `[jest-message-util]` Add support for [AggregateError](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/AggregateError) ([#13946](https://github.com/facebook/jest/pull/13946) & [#13947](https://github.com/facebook/jest/pull/13947))
- `[jest-message-util]` Add support for [Error causes](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Error/cause) in `test` and `it` ([#13935](https://github.com/facebook/jest/pull/13935) & [#13966](https://github.com/facebook/jest/pull/13966))
- `[jest-reporters]` Add `summaryThreshold` option to summary reporter to allow overriding the internal threshold that is used to print the summary of all failed tests when the number of test suites surpasses it ([#13895](https://github.com/facebook/jest/pull/13895))
- `[jest-runtime]` Expose `@sinonjs/fake-timers` async APIs functions `advanceTimersByTimeAsync(msToRun)` (`tickAsync(msToRun)`), `advanceTimersToNextTimerAsync(steps)` (`nextAsync`), `runAllTimersAsync` (`runAllAsync`), and `runOnlyPendingTimersAsync` (`runToLastAsync`) ([#13981](https://github.com/facebook/jest/pull/13981))
- `[jest-runtime, @jest/transform]` Allow V8 coverage provider to collect coverage from files which were not loaded explicitly ([#13974](https://github.com/facebook/jest/pull/13974))
- `[jest-snapshot]` Add support to `cts` and `mts` TypeScript files to inline snapshots ([#13975](https://github.com/facebook/jest/pull/13975))
- `[jest-worker]` Add `start` method to worker farms ([#13937](https://github.com/facebook/jest/pull/13937))
- `[jest-worker]` Support passing a URL as path to worker ([#13982](https://github.com/facebook/jest/pull/13982))

### Fixes

- `[babel-plugin-jest-hoist]` Fix unwanted hoisting of nested `jest` usages ([#13952](https://github.com/facebook/jest/pull/13952))
- `[jest-circus]` Send test case results for `todo` tests ([#13915](https://github.com/facebook/jest/pull/13915))
- `[jest-circus]` Update message printed on test timeout ([#13830](https://github.com/facebook/jest/pull/13830))
- `[jest-circus]` Avoid creating the word "testfalse" when `takesDoneCallback` is `false` in the message printed on test timeout AND updated timeouts test ([#13954](https://github.com/facebook/jest/pull/13954))
- `[jest-environment-jsdom]` Stop setting `document` to `null` on teardown ([#13972](https://github.com/facebook/jest/pull/13972))
- `[@jest/expect-utils]` Update `toStrictEqual()` to be able to check `jest.fn().mock.calls` ([#13960](https://github.com/facebook/jest/pull/13960))
- `[@jest/test-result]` Allow `TestResultsProcessor` type to return a Promise ([#13950](https://github.com/facebook/jest/pull/13950))

### Chore & Maintenance

- `[jest-snapshot]` Remove dependency on `jest-haste-map` ([#13977](https://github.com/facebook/jest/pull/13977))

## 29.4.3

### Features

- `[expect]` Update `toThrow()` to be able to use error `cause`s ([#13606](https://github.com/facebook/jest/pull/13606))
- `[jest-core]` allow to use `workerIdleMemoryLimit` with only 1 worker or `runInBand` option ([#13846](https://github.com/facebook/jest/pull/13846))
- `[jest-message-util]` Add support for [error `cause`s](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Error/cause) ([#13868](https://github.com/facebook/jest/pull/13868) & [#13912](https://github.com/facebook/jest/pull/13912))
- `[jest-runtime]` Revert `import assertions` for JSON modules as it's been relegated to Stage 2 ([#13911](https://github.com/facebook/jest/pull/13911))

### Fixes

- `[@jest/expect-utils]` `subsetEquality` should consider also an object's inherited string keys ([#13824](https://github.com/facebook/jest/pull/13824))
- `[jest-mock]` Clear mock state when `jest.restoreAllMocks()` is called ([#13867](https://github.com/facebook/jest/pull/13867))
- `[jest-mock]` Prevent `mockImplementationOnce` and `mockReturnValueOnce` bleeding into `withImplementation` ([#13888](https://github.com/facebook/jest/pull/13888))
- `[jest-mock]` Do not restore mocks when `jest.resetAllMocks()` is called ([#13866](https://github.com/facebook/jest/pull/13866))

## 29.4.2

### Features

- `[@jest/core]` Instrument significant lifecycle events with [`performance.mark()`](https://nodejs.org/docs/latest-v16.x/api/perf_hooks.html#performancemarkname-options) ([#13859](https://github.com/facebook/jest/pull/13859))

### Fixes

- `[expect, @jest/expect]` Provide type of `actual` as a generic argument to `Matchers` to allow better-typed extensions ([#13848](https://github.com/facebook/jest/pull/13848))
- `[jest-circus]` Added explicit mention of test failing because `done()` is not being called in error message ([#13847](https://github.com/facebook/jest/pull/13847))
- `[jest-runtime]` Handle CJS re-exports of node core modules from ESM ([#13856](https://github.com/facebook/jest/pull/13856))
- `[jest-transform]` Downgrade `write-file-atomic` to v4 ([#13853](https://github.com/facebook/jest/pull/13853))
- `[jest-worker]` Ignore IPC messages not intended for Jest ([#13543](https://github.com/facebook/jest/pull/13543))

### Chore & Maintenance

- `[*]` make sure to exclude `.eslintcache` from published module ([#13832](https://github.com/facebook/jest/pull/13832))
- `[docs]` Cleanup incorrect links in CHANGELOG.md ([#13857](https://github.com/facebook/jest/pull/13857))

## 29.4.1

### Features

- `[expect, jest-circus, @jest/types]` Implement `numPassingAsserts` of testResults to track the number of passing asserts in a test ([#13795](https://github.com/facebook/jest/pull/13795))
- `[jest-core]` Add newlines to JSON output ([#13817](https://github.com/facebook/jest/pull/13817))
- `[@jest/reporters]` Automatic log folding in GitHub Actions Reporter ([#13626](https://github.com/facebook/jest/pull/13626))

### Fixes

- `[@jest/expect-utils]` `toMatchObject` diffs should include `Symbol` properties ([#13810](https://github.com/facebook/jest/pull/13810))
- `[jest-runtime]` Handle missing `replaceProperty` ([#13823](https://github.com/facebook/jest/pull/13823))
- `[@jest/types]` Add partial support for `done` callbacks in typings of `each` ([#13756](https://github.com/facebook/jest/pull/13756))

## 29.4.0

### Features

- `[expect, @jest/expect-utils]` Support custom equality testers ([#13654](https://github.com/facebook/jest/pull/13654))
- `[jest-config, jest-worker]` Use `os.availableParallelism` if available to calculate number of workers to spawn ([#13738](https://github.com/facebook/jest/pull/13738))
- `[@jest/globals, jest-mock]` Add `jest.replaceProperty()` that replaces property value ([#13496](https://github.com/facebook/jest/pull/13496))
- `[jest-haste-map]` ignore Sapling vcs directories (`.sl/`) ([#13674](https://github.com/facebook/jest/pull/13674))
- `[jest-resolve]` Support subpath imports ([#13705](https://github.com/facebook/jest/pull/13705), [#13723](https://github.com/facebook/jest/pull/13723), [#13777](https://github.com/facebook/jest/pull/13777))
- `[jest-runtime]` Add `jest.isolateModulesAsync` for scoped module initialization of asynchronous functions ([#13680](https://github.com/facebook/jest/pull/13680))
- `[jest-runtime]` Add `jest.isEnvironmentTornDown` function ([#13741](https://github.com/facebook/jest/pull/13741))
- `[jest-test-result]` Added `skipped` and `focused` status to `FormattedTestResult` ([#13700](https://github.com/facebook/jest/pull/13700))
- `[jest-transform]` Support for asynchronous `createTransformer` ([#13762](https://github.com/facebook/jest/pull/13762))

### Fixes

- `[jest-environment-node]` Fix non-configurable globals ([#13687](https://github.com/facebook/jest/pull/13687))
- `[@jest/expect-utils]` `toMatchObject` should handle `Symbol` properties ([#13639](https://github.com/facebook/jest/pull/13639))
- `[jest-mock]` Fix `mockReset` and `resetAllMocks` `undefined` return value([#13692](https://github.com/facebook/jest/pull/13692))
- `[jest-resolve]` Add global paths to `require.resolve.paths` ([#13633](https://github.com/facebook/jest/pull/13633))
- `[jest-resolve]` Correct node core module detection when using `node:` specifiers ([#13806](https://github.com/facebook/jest/pull/13806))
- `[jest-runtime]` Support WASM files that import JS resources ([#13608](https://github.com/facebook/jest/pull/13608))
- `[jest-runtime]` Use the `scriptTransformer` cache in `jest-runner` ([#13735](https://github.com/facebook/jest/pull/13735))
- `[jest-runtime]` Enforce import assertions when importing JSON in ESM ([#12755](https://github.com/facebook/jest/pull/12755) & [#13805](https://github.com/facebook/jest/pull/13805))
- `[jest-snapshot]` Make sure to import `babel` outside of the sandbox ([#13694](https://github.com/facebook/jest/pull/13694))
- `[jest-transform]` Ensure the correct configuration is passed to preprocessors specified multiple times in the `transform` option ([#13770](https://github.com/facebook/jest/pull/13770))

### Chore & Maintenance

- `[@jest/fake-timers]` Update `@sinonjs/fake-timers` ([#13612](https://github.com/facebook/jest/pull/13612))
- `[docs]` Improve custom puppeteer example to prevent worker warnings ([#13619](https://github.com/facebook/jest/pull/13619))

## 29.3.1

### Fixes

- `[jest-config]` Do not warn about `preset` in `ProjectConfig` ([#13583](https://github.com/facebook/jest/pull/13583))

### Performance

- `[jest-transform]` Defer creation of cache directory ([#13420](https://github.com/facebook/jest/pull/13420))

## 29.3.0

### Features

- `[jest-runtime]` Support WebAssembly (Wasm) imports in ESM modules ([#13505](https://github.com/facebook/jest/pull/13505))

### Fixes

- `[jest-config]` Add config validation for `projects` option ([#13565](https://github.com/facebook/jest/pull/13565))
- `[jest-mock]` Treat cjs modules as objects so they can be mocked ([#13513](https://github.com/facebook/jest/pull/13513))
- `[jest-worker]` Throw an error instead of hanging when jest workers terminate unexpectedly ([#13566](https://github.com/facebook/jest/pull/13566))

### Chore & Maintenance

- `[@jest/transform]` Update `convert-source-map` ([#13509](https://github.com/facebook/jest/pull/13509))
- `[docs]` Mention `toStrictEqual` in UsingMatchers docs. ([#13560](https://github.com/facebook/jest/pull/13560))

## 29.2.2

### Fixes

- `[@jest/test-sequencer]` Make sure sharding does not produce empty groups ([#13476](https://github.com/facebook/jest/pull/13476))
- `[jest-circus]` Test marked as `todo` are shown as todo when inside a focussed describe ([#13504](https://github.com/facebook/jest/pull/13504))
- `[jest-mock]` Ensure mock resolved and rejected values are promises from correct realm ([#13503](https://github.com/facebook/jest/pull/13503))
- `[jest-snapshot]` Don't highlight passing asymmetric property matchers in snapshot diff ([#13480](https://github.com/facebook/jest/issues/13480))

### Chore & Maintenance

- `[docs]` Update link to Jest 28 upgrade guide in error message ([#13483](https://github.com/facebook/jest/pull/13483))
- `[jest-runner, jest-watcher]` Update `emittery` ([#13490](https://github.com/facebook/jest/pull/13490))

## 29.2.1

### Features

- `[@jest/globals, jest-mock]` Add `jest.Spied*` utility types ([#13440](https://github.com/facebook/jest/pull/13440))

### Fixes

- `[jest-environment-node]` make `globalThis.performance` writable for Node 19 and fake timers ([#13467](https://github.com/facebook/jest/pull/13467))
- `[jest-mock]` Revert [#13398](https://github.com/facebook/jest/pull/13398) to restore mocking of setters ([#13472](https://github.com/facebook/jest/pull/13472))

### Performance

- `[*]` Use sha1 instead of sha256 for hashing ([#13421](https://github.com/facebook/jest/pull/13421))

## 29.2.0

### Features

- `[@jest/cli, jest-config]` A seed for the test run will be randomly generated, or set by a CLI option ([#13400](https://github.com/facebook/jest/pull/13400))
- `[@jest/cli, jest-config]` `--show-seed` will display the seed value in the report, and can be set via a CLI flag or through the config file ([#13400](https://github.com/facebook/jest/pull/13400))
- `[jest-config]` Add `readInitialConfig` utility function ([#13356](https://github.com/facebook/jest/pull/13356))
- `[jest-core]` Allow `testResultsProcessor` to be async ([#13343](https://github.com/facebook/jest/pull/13343))
- `[@jest/environment, jest-environment-node, jest-environment-jsdom, jest-runtime]` Add `getSeed()` to the `jest` object ([#13400](https://github.com/facebook/jest/pull/13400))
- `[expect, @jest/expect-utils]` Allow `isA` utility to take a type argument ([#13355](https://github.com/facebook/jest/pull/13355))
- `[expect]` Expose `AsyncExpectationResult` and `SyncExpectationResult` types ([#13411](https://github.com/facebook/jest/pull/13411))

### Fixes

- `[babel-plugin-jest-hoist]` Ignore `TSTypeQuery` when checking for hoisted references ([#13367](https://github.com/facebook/jest/pull/13367))
- `[jest-core]` Fix `detectOpenHandles` false positives for some special objects such as `TLSWRAP` ([#13414](https://github.com/facebook/jest/pull/13414))
- `[jest-mock]` Fix mocking of getters and setters on classes ([#13398](https://github.com/facebook/jest/pull/13398))
- `[jest-reporters]` Revert: Transform file paths into hyperlinks ([#13399](https://github.com/facebook/jest/pull/13399))
- `[@jest/types]` Infer type of `each` table correctly when the table is a tuple or array ([#13381](https://github.com/facebook/jest/pull/13381))
- `[@jest/types]` Rework typings to allow the `*ReturnedWith` matchers to be called with no argument ([#13385](https://github.com/facebook/jest/pull/13385))

### Chore & Maintenance

- `[*]` Update `@babel/*` deps, resulting in slightly different stack traces for `each` ([#13422](https://github.com/facebook/jest/pull/13422))

### Performance

- `[jest-runner]` Do not instrument v8 coverage data if coverage should not be collected ([#13282](https://github.com/facebook/jest/pull/13282))

## 29.1.2

### Fixes

- `[expect, @jest/expect]` Revert buggy inference of argument types for `*CalledWith` and `*ReturnedWith` matchers introduced in 29.1.0 ([#13339](https://github.com/facebook/jest/pull/13339))
- `[jest-worker]` Add missing dependency on `jest-util` ([#13341](https://github.com/facebook/jest/pull/13341))

## 29.1.1

### Fixes

- `[jest-mock]` Revert [#13145](https://github.com/facebook/jest/pull/13145) which broke mocking of transpiled ES modules

## 29.1.0

### Features

- `[expect, @jest/expect]` Support type inference for function parameters in `CalledWith` assertions ([#13268](https://github.com/facebook/jest/pull/13268))
- `[expect, @jest/expect]` Infer type of `*ReturnedWith` matchers argument ([#13278](https://github.com/facebook/jest/pull/13278))
- `[@jest/environment, jest-runtime]` Allow `jest.requireActual` and `jest.requireMock` to take a type argument ([#13253](https://github.com/facebook/jest/pull/13253))
- `[@jest/environment]` Allow `jest.mock` and `jest.doMock` to take a type argument ([#13254](https://github.com/facebook/jest/pull/13254))
- `[@jest/fake-timers]` Add `jest.now()` to return the current fake clock time ([#13244](https://github.com/facebook/jest/pull/13244), [#13246](https://github.com/facebook/jest/pull/13246))
- `[@jest/mock]` Add `withImplementation` method for temporarily overriding a mock ([#13281](https://github.com/facebook/jest/pull/13281))
- `[expect]` Export `toThrow*` matchers ([#13328](https://github.com/facebook/jest/pull/13328))

### Fixes

- `[jest-circus, jest-jasmine2]` Fix error messages for Node's `assert.throes` ([#13322](https://github.com/facebook/jest/pull/13322))
- `[jest-haste-map]` Remove `__proto__` usage ([#13256](https://github.com/facebook/jest/pull/13256))
- `[jest-mock]` Improve `spyOn` typings to handle optional properties ([#13247](https://github.com/facebook/jest/pull/13247))
- `[jest-mock]` Fix mocking of getters and setters on classes ([#13145](https://github.com/facebook/jest/pull/13145))
- `[jest-snapshot]` Throw useful error when an array is passed as property matchers ([#13263](https://github.com/facebook/jest/pull/13263))
- `[jest-snapshot]` Prioritize parser used in the project ([#13323](https://github.com/facebook/jest/pull/13323))
- `[jest-transform]` Attempt to work around issues with atomic writes on Windows ([#11423](https://github.com/facebook/jest/pull/11423))

## 29.0.3

### Features

- `[@jest/environment, jest-runtime]` Allow passing a generic type argument to `jest.createMockFromModule<T>()` method ([#13202](https://github.com/facebook/jest/pull/13202))
- `[expect]` Expose `ExpectationResult` type ([#13240](https://github.com/facebook/jest/pull/13240))
- `[jest-snapshot]` Expose `Context` type ([#13240](https://github.com/facebook/jest/pull/13240))
- `[@jest/globals]` Add `jest.Mock` type helper ([#13235](https://github.com/facebook/jest/pull/13235))

### Fixes

- `[jest-core]` Capture `execError` during `TestScheduler.scheduleTests` and dispatch to reporters ([#13203](https://github.com/facebook/jest/pull/13203))
- `[jest-resolve]` Make sure to resolve module paths after looking at `exports` ([#13242](https://github.com/facebook/jest/pull/13242))
- `[jest-resolve]` Improve error on module not found deep in the `require` stack ([#8704](https://github.com/facebook/jest/pull/8704))
- `[jest-snapshot]` Fix typings of snapshot matchers ([#13240](https://github.com/facebook/jest/pull/13240))

### Chore & Maintenance

- `[*]` Fix inconsistent workspace prefixes ([#13217](https://github.com/facebook/jest/pull/13217))
- `[jest-haste-map]` Expose a minimal public API to TypeScript ([#13023](https://github.com/facebook/jest/pull/13023))

## 29.0.2

### Features

- `[jest-transform]` Expose `TransformFactory` type ([#13184](https://github.com/facebook/jest/pull/13184))

### Fixes

- `[babel-plugin-jest-hoist]` Support imported `jest` in mock factory ([#13188](https://github.com/facebook/jest/pull/13188))
- `[jest-mock]` Align the behavior and return type of `generateFromMetadata` method ([#13207](https://github.com/facebook/jest/pull/13207))
- `[jest-runtime]` Support `jest.resetModules()` with ESM ([#13211](https://github.com/facebook/jest/pull/13211))

## 29.0.1

### Fixes

- `[jest-snapshot]` Pass `snapshotFormat` through when diffing snapshots ([#13181](https://github.com/facebook/jest/pull/13181))

## 29.0.0

### Features

- `[expect]` [**BREAKING**] Differentiate between `MatcherContext` `MatcherUtils` and `MatcherState` types ([#13141](https://github.com/facebook/jest/pull/13141))
- `[jest-circus]` Add support for `test.failing.each` ([#13142](https://github.com/facebook/jest/pull/13142))
- `[jest-config]` [**BREAKING**] Make `snapshotFormat` default to `escapeString: false` and `printBasicPrototype: false` ([#13036](https://github.com/facebook/jest/pull/13036))
- `[jest-config]` [**BREAKING**] Remove undocumented `collectCoverageOnlyFrom` option ([#13156](https://github.com/facebook/jest/pull/13156))
- `[jest-environment-jsdom]` [**BREAKING**] Upgrade to `jsdom@20` ([#13037](https://github.com/facebook/jest/pull/13037), [#13058](https://github.com/facebook/jest/pull/13058))
- `[@jest/globals]` Add `jest.Mocked`, `jest.MockedClass`, `jest.MockedFunction` and `jest.MockedObject` utility types ([#12727](https://github.com/facebook/jest/pull/12727))
- `[jest-mock]` [**BREAKING**] Refactor `Mocked*` utility types. `MaybeMockedDeep` and `MaybeMocked` became `Mocked` and `MockedShallow` respectively; only deep mocked variants of `MockedClass`, `MockedFunction` and `MockedObject` are exported ([#13123](https://github.com/facebook/jest/pull/13123), [#13124](https://github.com/facebook/jest/pull/13124))
- `[jest-mock]` [**BREAKING**] Change the default `jest.mocked` helper’s behavior to deep mocked ([#13125](https://github.com/facebook/jest/pull/13125))
- `[jest-snapshot]` [**BREAKING**] Let `babel` find config when updating inline snapshots ([#13150](https://github.com/facebook/jest/pull/13150))
- `[@jest/test-result, @jest/types]` [**BREAKING**] Replace `Bytes` and `Milliseconds` types with `number` ([#13155](https://github.com/facebook/jest/pull/13155))
- `[jest-worker]` Adds `workerIdleMemoryLimit` option which is used as a check for worker memory leaks >= Node 16.11.0 and recycles child workers as required ([#13056](https://github.com/facebook/jest/pull/13056), [#13105](https://github.com/facebook/jest/pull/13105), [#13106](https://github.com/facebook/jest/pull/13106), [#13107](https://github.com/facebook/jest/pull/13107))
- `[pretty-format]` [**BREAKING**] Remove `ConvertAnsi` plugin in favour of `jest-serializer-ansi-escapes` ([#13040](https://github.com/facebook/jest/pull/13040))
- `[pretty-format]` Allow to opt out from sorting object keys with `compareKeys: null` ([#12443](https://github.com/facebook/jest/pull/12443))

### Fixes

- `[jest-config]` Fix testing multiple projects with TypeScript config files ([#13099](https://github.com/facebook/jest/pull/13099))
- `[@jest/expect-utils]` Fix deep equality of ImmutableJS Record ([#13055](https://github.com/facebook/jest/pull/13055))
- `[jest-haste-map]` Increase the maximum possible file size that jest-haste-map can handle ([#13094](https://github.com/facebook/jest/pull/13094))
- `[jest-runtime]` Properly support CJS re-exports from dual packages ([#13170](https://github.com/facebook/jest/pull/13170))
- `[jest-snapshot]` Make `prettierPath` optional in `SnapshotState` ([#13149](https://github.com/facebook/jest/pull/13149))
- `[jest-snapshot]` Fix parsing error from inline snapshot files with `JSX` ([#12760](https://github.com/facebook/jest/pull/12760))
- `[jest-worker]` When a process runs out of memory worker exits correctly and doesn't spin indefinitely ([#13054](https://github.com/facebook/jest/pull/13054))

### Chore & Maintenance

- `[*]` [**BREAKING**] Drop support for Node v12 and v17 ([#13033](https://github.com/facebook/jest/pull/13033))
- `[docs]` Fix webpack name ([#13049](https://github.com/facebook/jest/pull/13049))
- `[docs]` Explicit how to set `n` for `--bail` ([#13128](https://github.com/facebook/jest/pull/13128))
- `[docs]` Update Enzyme URL ([#13166](https://github.com/facebook/jest/pull/13166))
- `[jest-leak-detector]` Remove support for `weak-napi` ([#13035](https://github.com/facebook/jest/pull/13035))
- `[jest-snapshot]` [**BREAKING**] Require `rootDir` as argument to `SnapshotState` ([#13150](https://github.com/facebook/jest/pull/13150))

