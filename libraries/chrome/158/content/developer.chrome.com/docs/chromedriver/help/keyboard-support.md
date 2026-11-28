# Keyboard support

At this time, ChromeDriver only supports systems that have a US keyboard
configured.

When ChromeDriver detects this state, it logs the following:  

    [INFO]: Cannot switch to US keyboard layout - some keys may be interpreted incorrectly

Users without a US keyboard may experience lost keys during `sendKeys` or
`TypeElement` commands.

As a workaround, we recommend such users add a US Keyboard with QWERTY layout as
a secondary option to their system configuration. This makes the US Keyboard
configuration available to ChromeDriver.

As always, ChromeDriver is an open source project, and we welcome contributions.