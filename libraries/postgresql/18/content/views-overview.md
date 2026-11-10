---
source: https://www.postgresql.org/docs/18/views-overview.html
title: "53.1. Overview"
---


## 53.1. Overview

[Table 53.1](views-overview.html#VIEW-TABLE "Table 53.1. System Views") lists the system views. More detailed documentation of each catalog follows below. Except where noted, all the views described here are read-only.

**Table 53.1. System Views**

| View Name | Purpose |
| --- | --- |
| [`pg_aios`](view-pg-aios.html "53.2. pg_aios") | In-use asynchronous IO handles |
| [`pg_available_extensions`](view-pg-available-extensions.html "53.3. pg_available_extensions") | available extensions |
| [`pg_available_extension_versions`](view-pg-available-extension-versions.html "53.4. pg_available_extension_versions") | available versions of extensions |
| [`pg_backend_memory_contexts`](view-pg-backend-memory-contexts.html "53.5. pg_backend_memory_contexts") | backend memory contexts |
| [`pg_config`](view-pg-config.html "53.6. pg_config") | compile-time configuration parameters |
| [`pg_cursors`](view-pg-cursors.html "53.7. pg_cursors") | open cursors |
| [`pg_file_settings`](view-pg-file-settings.html "53.8. pg_file_settings") | summary of configuration file contents |
| [`pg_group`](view-pg-group.html "53.9. pg_group") | groups of database users |
| [`pg_hba_file_rules`](view-pg-hba-file-rules.html "53.10. pg_hba_file_rules") | summary of client authentication configuration file contents |
| [`pg_ident_file_mappings`](view-pg-ident-file-mappings.html "53.11. pg_ident_file_mappings") | summary of client user name mapping configuration file contents |
| [`pg_indexes`](view-pg-indexes.html "53.12. pg_indexes") | indexes |
| [`pg_locks`](view-pg-locks.html "53.13. pg_locks") | locks currently held or awaited |
| [`pg_matviews`](view-pg-matviews.html "53.14. pg_matviews") | materialized views |
| [`pg_policies`](view-pg-policies.html "53.15. pg_policies") | policies |
| [`pg_prepared_statements`](view-pg-prepared-statements.html "53.16. pg_prepared_statements") | prepared statements |
| [`pg_prepared_xacts`](view-pg-prepared-xacts.html "53.17. pg_prepared_xacts") | prepared transactions |
| [`pg_publication_tables`](view-pg-publication-tables.html "53.18. pg_publication_tables") | publications and information of their associated tables |
| [`pg_replication_origin_status`](view-pg-replication-origin-status.html "53.19. pg_replication_origin_status") | information about replication origins, including replication progress |
| [`pg_replication_slots`](view-pg-replication-slots.html "53.20. pg_replication_slots") | replication slot information |
| [`pg_roles`](view-pg-roles.html "53.21. pg_roles") | database roles |
| [`pg_rules`](view-pg-rules.html "53.22. pg_rules") | rules |
| [`pg_seclabels`](view-pg-seclabels.html "53.23. pg_seclabels") | security labels |
| [`pg_sequences`](view-pg-sequences.html "53.24. pg_sequences") | sequences |
| [`pg_settings`](view-pg-settings.html "53.25. pg_settings") | parameter settings |
| [`pg_shadow`](view-pg-shadow.html "53.26. pg_shadow") | database users |
| [`pg_shmem_allocations`](view-pg-shmem-allocations.html "53.27. pg_shmem_allocations") | shared memory allocations |
| [`pg_shmem_allocations_numa`](view-pg-shmem-allocations-numa.html "53.28. pg_shmem_allocations_numa") | NUMA node mappings for shared memory allocations |
| [`pg_stats`](view-pg-stats.html "53.29. pg_stats") | planner statistics |
| [`pg_stats_ext`](view-pg-stats-ext.html "53.30. pg_stats_ext") | extended planner statistics |
| [`pg_stats_ext_exprs`](view-pg-stats-ext-exprs.html "53.31. pg_stats_ext_exprs") | extended planner statistics for expressions |
| [`pg_tables`](view-pg-tables.html "53.32. pg_tables") | tables |
| [`pg_timezone_abbrevs`](view-pg-timezone-abbrevs.html "53.33. pg_timezone_abbrevs") | time zone abbreviations |
| [`pg_timezone_names`](view-pg-timezone-names.html "53.34. pg_timezone_names") | time zone names |
| [`pg_user`](view-pg-user.html "53.35. pg_user") | database users |
| [`pg_user_mappings`](view-pg-user-mappings.html "53.36. pg_user_mappings") | user mappings |
| [`pg_views`](view-pg-views.html "53.37. pg_views") | views |
| [`pg_wait_events`](view-pg-wait-events.html "53.38. pg_wait_events") | wait events |
