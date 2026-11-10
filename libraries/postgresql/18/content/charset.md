---
source: https://www.postgresql.org/docs/18/charset.html
title: "Chapter 23. Localization"
---


## Chapter 23. Localization

This chapter describes the available localization features from the point of view of the administrator. PostgreSQL supports two localization facilities:

- Using the locale features of the operating system to provide locale-specific collation order, number formatting, translated messages, and other aspects. This is covered in [Section 23.1](locale.html "23.1. Locale Support") and [Section 23.2](collation.html "23.2. Collation Support").
- Providing a number of different character sets to support storing text in all kinds of languages, and providing character set translation between client and server. This is covered in [Section 23.3](multibyte.html "23.3. Character Set Support").
