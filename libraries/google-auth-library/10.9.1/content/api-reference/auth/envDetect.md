---
title: Type declarations: build/src/auth/envDetect.d.ts
source: https://registry.npmjs.org/google-auth-library/-/google-auth-library-10.9.1.tgz (package/build/src/auth/envDetect.d.ts)
---

# Type declarations: build/src/auth/envDetect.d.ts

Verbatim file from the official source, wrapped in a code block for search.

```ts
export declare enum GCPEnv {
    APP_ENGINE = "APP_ENGINE",
    KUBERNETES_ENGINE = "KUBERNETES_ENGINE",
    CLOUD_FUNCTIONS = "CLOUD_FUNCTIONS",
    COMPUTE_ENGINE = "COMPUTE_ENGINE",
    CLOUD_RUN = "CLOUD_RUN",
    CLOUD_RUN_JOBS = "CLOUD_RUN_JOBS",
    NONE = "NONE"
}
export declare function clear(): void;
export declare function getEnv(): Promise<GCPEnv>;
```
