# Chrome Extensions can be either packed or unpacked.

- Packed extensions are a single file with a `.crx` extension.
- Unpacked extensions are a directory containing the extension, including a `manifest.json` file.

To pack an unpacked extension, use the Pack button in `chrome://extensions` or
use `Chrome: "chrome.exe --pack-extension=C:\path\to\unpacked\extension --pack-extension-key=C:\myext.pem"`. To unpack a packed extension,
extract the file. You may need to rename the filetype from `.crx` to `.zip` for your
zip utility to recognize it.

Refer to the [Extensions documentation](https://developer.chrome.com/docs/extensions) for other ways to do
this which are more automation friendly.

## Install Extensions with ChromeDriver

Packed (`.crx` file)  

    ChromeOptions options = new ChromeOptions();
    options.addExtensions(new File("/path/to/extension.crx"));
    ChromeDriver driver = new ChromeDriver(options);

Unpacked (directory)  

    ChromeOptions options = new ChromeOptions();
    options.addArguments("load-extension=/path/to/extension");
    ChromeDriver driver = new ChromeDriver(options);