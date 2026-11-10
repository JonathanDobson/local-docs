---
source: https://www.postgresql.org/docs/18/view-pg-timezone-abbrevs.html
title: "53.33. pg_timezone_abbrevs"
---


## 53.33. `pg_timezone_abbrevs`

The view `pg_timezone_abbrevs` provides a list of time zone abbreviations that are currently recognized by the datetime input routines. The contents of this view change when the [TimeZone](runtime-config-client.html#GUC-TIMEZONE) or [timezone\_abbreviations](runtime-config-client.html#GUC-TIMEZONE-ABBREVIATIONS) run-time parameters are modified.

**Table 53.33. `pg_timezone_abbrevs` Columns**

| Column Type  Description |
| --- |
| `abbrev` `text`  Time zone abbreviation |
| `utc_offset` `interval`  Offset from UTC (positive means east of Greenwich) |
| `is_dst` `bool`  True if this is a daylight-savings abbreviation |

  

While most timezone abbreviations represent fixed offsets from UTC, there are some that have historically varied in value (see [Section B.4](datetime-config-files.html "B.4. Date/Time Configuration Files") for more information). In such cases this view presents their current meaning.
