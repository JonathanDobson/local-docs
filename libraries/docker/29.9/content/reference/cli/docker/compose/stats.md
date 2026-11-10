---
title: "docker compose stats"
source: https://docs.docker.com/reference/cli/docker/compose/stats/
---

# docker compose stats

**Description:** Display a live stream of container(s) resource usage statistics

**Usage:** `docker compose stats [OPTIONS] [SERVICE]`










## Description

Display a live stream of container(s) resource usage statistics


## Options

| Option | Default | Description |
|--------|---------|-------------|
| `--aggregate` |  |  Show one line per project, summing the resource usage of its containers (only 'table' and 'json' formats)<br> |
| `-a`, `--all` |  |  Show all containers (default shows just running) |
| `--all-projects` |  |  Show the containers of all projects instead of the current one, with their project (only 'table' and 'json' formats)<br> |
| `--format` |  |  Format output using a custom template:<br>'table':            Print output in table format with column headers (default)<br>'table TEMPLATE':   Print output in table format using the given Go template<br>'json':             Print in JSON format<br>'TEMPLATE':         Print output using the given Go template.<br>Refer to https://docs.docker.com/engine/cli/formatting/ for more information about formatting output with templates |
| `--no-stream` |  |  Disable streaming stats and only pull the first result |
| `--no-trunc` |  |  Do not truncate output |
