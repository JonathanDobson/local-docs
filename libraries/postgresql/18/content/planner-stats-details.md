---
source: https://www.postgresql.org/docs/18/planner-stats-details.html
title: "Chapter 69. How the Planner Uses Statistics"
---


## Chapter 69. How the Planner Uses Statistics

This chapter builds on the material covered in [Section 14.1](using-explain.html "14.1. Using EXPLAIN") and [Section 14.2](planner-stats.html "14.2. Statistics Used by the Planner") to show some additional details about how the planner uses the system statistics to estimate the number of rows each part of a query might return. This is a significant part of the planning process, providing much of the raw material for cost calculation.

The intent of this chapter is not to document the code in detail, but to present an overview of how it works. This will perhaps ease the learning curve for someone who subsequently wishes to read the code.
