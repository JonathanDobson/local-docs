---
source: https://www.postgresql.org/docs/18/logical-replication-config.html
title: "29.12. Configuration Settings"
---


## 29.12. Configuration Settings

Logical replication requires several configuration options to be set. These options are relevant only on one side of the replication.

### 29.12.1. Publishers

[`wal_level`](runtime-config-wal.html#GUC-WAL-LEVEL) must be set to `logical`.

[`max_replication_slots`](runtime-config-replication.html#GUC-MAX-REPLICATION-SLOTS) must be set to at least the number of subscriptions expected to connect, plus some reserve for table synchronization.

Logical replication slots are also affected by [`idle_replication_slot_timeout`](runtime-config-replication.html#GUC-IDLE-REPLICATION-SLOT-TIMEOUT).

[`max_wal_senders`](runtime-config-replication.html#GUC-MAX-WAL-SENDERS) should be set to at least the same as `max_replication_slots`, plus the number of physical replicas that are connected at the same time.

Logical replication walsender is also affected by [`wal_sender_timeout`](runtime-config-replication.html#GUC-WAL-SENDER-TIMEOUT).

### 29.12.2. Subscribers

[`max_active_replication_origins`](runtime-config-replication.html#GUC-MAX-ACTIVE-REPLICATION-ORIGINS) must be set to at least the number of subscriptions that will be added to the subscriber, plus some reserve for table synchronization.

[`max_logical_replication_workers`](runtime-config-replication.html#GUC-MAX-LOGICAL-REPLICATION-WORKERS) must be set to at least the number of subscriptions (for leader apply workers), plus some reserve for the table synchronization workers and parallel apply workers.

[`max_worker_processes`](runtime-config-resource.html#GUC-MAX-WORKER-PROCESSES) may need to be adjusted to accommodate for replication workers, at least ([`max_logical_replication_workers`](runtime-config-replication.html#GUC-MAX-LOGICAL-REPLICATION-WORKERS) + `1`). Note, some extensions and parallel queries also take worker slots from `max_worker_processes`.

[`max_sync_workers_per_subscription`](runtime-config-replication.html#GUC-MAX-SYNC-WORKERS-PER-SUBSCRIPTION) controls the amount of parallelism of the initial data copy during the subscription initialization or when new tables are added.

[`max_parallel_apply_workers_per_subscription`](runtime-config-replication.html#GUC-MAX-PARALLEL-APPLY-WORKERS-PER-SUBSCRIPTION) controls the amount of parallelism for streaming of in-progress transactions with subscription parameter `streaming = parallel`.

Logical replication workers are also affected by [`wal_receiver_timeout`](runtime-config-replication.html#GUC-WAL-RECEIVER-TIMEOUT), [`wal_receiver_status_interval`](runtime-config-replication.html#GUC-WAL-RECEIVER-STATUS-INTERVAL) and [`wal_retrieve_retry_interval`](runtime-config-replication.html#GUC-WAL-RETRIEVE-RETRY-INTERVAL).
