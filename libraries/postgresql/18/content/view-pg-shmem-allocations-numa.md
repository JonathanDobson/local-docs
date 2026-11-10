---
source: https://www.postgresql.org/docs/18/view-pg-shmem-allocations-numa.html
title: "53.28. pg_shmem_allocations_numa"
---


## 53.28. `pg_shmem_allocations_numa`

The `pg_shmem_allocations_numa` shows how shared memory allocations in the server's main shared memory segment are distributed across NUMA nodes. This includes both memory allocated by PostgreSQL itself and memory allocated by extensions using the mechanisms detailed in [Section 36.10.11](xfunc-c.html#XFUNC-SHARED-ADDIN "36.10.11. Shared Memory"). This view will output multiple rows for each of the shared memory segments provided that they are spread across multiple NUMA nodes. This view should not be queried by monitoring systems as it is very slow and may end up allocating shared memory in case it was not used earlier. Current limitation for this view is that won't show anonymous shared memory allocations.

Note that this view does not include memory allocated using the dynamic shared memory infrastructure.

### Warning

When determining the NUMA node, the view touches all memory pages for the shared memory segment. This will force allocation of the shared memory, if it wasn't allocated already, and the memory may get allocated in a single NUMA node (depending on system configuration).

**Table 53.28. `pg_shmem_allocations_numa` Columns**

| Column Type  Description |
| --- |
| `name` `text`  The name of the shared memory allocation. |
| `numa_node` `int4`  ID of NUMA node |
| `size` `int8`  Size of the allocation on this particular NUMA memory node in bytes |

  

By default, the `pg_shmem_allocations_numa` view can be read only by superusers or roles with privileges of the `pg_read_all_stats` role.
