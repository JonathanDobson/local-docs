# ChromeDriver crashes

To diagnose and fix ChromeDriver crashes, you have a few options. This is only
for ChromeDriver crashes, which is not the same as Chrome crashing or closing.

On Windows, you may see something like this:

![ChromeDriver executable error window](https://developer.chrome.com/static/docs/chromedriver/help/chromedriver-crashes/image/chromedriver-error.png)

## Create a repro case

Create a repro case that ChromeDriver contributors can use to reproduce and
debug the problem. It's okay if the crash does not occur 100% of the time.

File a bug with your repro case. This is usually the fastest option to get help.

## Get a crash dump (Windows only)

To create and debug a crash dump, you need a debug version of ChromeDriver. We
don't have official releases of debug build of ChromeDriver, but you
can check out Chrome sources and build the debug version of ChromeDriver. When
the crash happens, attach the debugger to look at what's happening. This requires
some C++ experience and knowledge of your system's debugger.

Read the [contributing guide](https://developer.chrome.com/docs/chromedriver/contributing) for help.

Configure your system to create a fulldump on crash. Read Microsoft's
[Collecting User-Mode Dumps](https://learn.microsoft.com/windows/win32/wer/collecting-user-mode-dumps)
for help.

After a crash dump is created, use WinDbg to analyze it:

`<ctrl-d>` and choose dump file  

    .sympath+ SRV*C:\symbols*http://msdl.microsoft.com/download/symbols;D:\path\to\directory\containing\pdb
    !sym noisy          # just to show any problems we have finding symbols
    ld chromedriver     # or !reload
    lmvm chromedriver   # Should show chromedriver has private/debug symbols
    !analyze -v         # Tells windbg to analyze the exception