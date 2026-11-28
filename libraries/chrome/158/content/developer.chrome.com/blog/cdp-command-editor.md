# Craft your Chrome Devtools Protocol (CDP) commands efficiently with the new command editor

Source: https://developer.chrome.com/blog/cdp-command-editor

![Hadrien Jaubert](https://web.dev/images/authors/hadrijau.jpg) Hadrien Jaubert [GitHub](https://github.com/hadrijau) [Homepage](https://www.hadrienjaubert.com)

<br />

> [!NOTE]
> **Note:** Interested in helping improve DevTools? Sign up to participate in [Google User Research here](https://google.qualtrics.com/jfe/form/SV_9YbKj35IGoGsDBj?reserved=1&utm_source=Website+feature&Q_Language=en&utm_medium=own_web&utm_campaign=Q4&productTag=chrm&campaignDate=November2020&referral_code=UXFm430458).

[Chrome DevTools Protocol (CDP)](https://chromedevtools.github.io/devtools-protocol/) is a remote debugging protocol (API) that lets developers communicate with a running Chrome browser. Chrome DevTools uses CDP to help you inspect the browser's state, control its behavior, and collect debugging information. You can also build Chrome extensions that use CDP.

For example, this is a CDP command that inserts a new rule with the given `ruleText` in a stylesheet with given `styleSheetId`, at the position specified by `location`.

```javascript
{ 
    command: 'CSS.addRule', 
    parameters: {
        styleSheetId: '2',
        ruleText:'Example', 
        location: {
            startLine: 1,
            startColumn: 1,
            endLine: 1,
            endColumn: 1
        }
    }
}
```

The [Protocol monitor](https://developer.chrome.com/blog/new-in-devtools-92.md.txt#protocol-monitor) drawer tab provides you with a way to send CDP requests and view all the CDP requests and responses DevTools sends and receives.

![The command line bar at the bottom of Protocol monitor.](https://developer.chrome.com/static/blog/cdp-command-editor/image/the-command-line-bar-the-45dda192c7625.png)

Previously it was difficult to craft the command by hand, especially a command with many parameters. Not only did you need to be mindful of opening and closing brackets and quotation marks, you also had to remember the command's parameters which, in turn, makes you look up the [CDP documentation](https://chromedevtools.github.io/devtools-protocol/).

To solve this problem, DevTools introduced a new CDP editor whose main goals are to:

- **Auto-complete commands**. Simplify your CDP command input by providing you with the list of available commands via an auto completion feature.
- **Auto-populate command parameters**. Reduce the need to check the CDP documentation for the list of available command parameters.
- **Simplify the typing of parameter**. You just have to fill in the values of the parameters you want to send.
- **Edit and resend**. Improve prototyping speed by making it quicker to modify a CDP command.

Now, let's have a look at what this new editor offers, and how you can make use of it!

## Autocompletion feature

![The autocompletion drop-down menu.](https://developer.chrome.com/static/blog/cdp-command-editor/image/the-autocompletion-drop-d-ab9b5b9899e6d.png)

An auto completion feature now powers the command input bar. It helps you write the names of the CDP commands you have access to. This can be very handy for commands that don't accept parameters.

## String and number parameters

With this new editor, you can now easily edit the values of primitive parameters. To open the editor, click the ![Open left panel.](https://developer.chrome.com/static/blog/cdp-command-editor/image/open-left-panel-e23b32e5774b7.svg) icon next to the command input.

Once you enter the command name, the editor shows you the corresponding parameters automatically. You don't have to look up documentation to know what parameters go with what commands. Furthermore, the editor displays the parameters in a given order: the mandatory ones first (in red) and the optional ones next (in blue).

To add a value to an optional parameter, hover over its name and click the `+` button. To reset the parameter to undefined, click the **Reset to default value** button.

![The + and 'Reset to default value' buttons.](https://developer.chrome.com/static/blog/cdp-command-editor/image/the-reset-default-va-03f3775cd1f65.png)

## Enum and boolean parameters

When editing enum or boolean parameters, you'll see a drop-down menu that provides a selection of potential values (for enums) or the straightforward true or false option for booleans. This feature reduces the possibility of typing the wrong value for enum parameters and maintains accuracy and simplicity.

![The boolean and enum drop-down menus.](https://developer.chrome.com/static/blog/cdp-command-editor/image/the-boolean-enum-drop-do-30d45d03d589b.png)

## Array parameters

For array parameters, you can manually add values to the array. Hover over the parameter's row and click the `+` button.

![The + button that adds an array item.](https://developer.chrome.com/static/blog/cdp-command-editor/image/the-button-adds-array-4397b91176822.png)

To delete array items one by one, click the bin button next to the items. You can also clear all the parameters from the array with the block button. In this case, the array parameter is reset to `[]`.

![The 'Delete parameter' and 'Reset to default' buttons.](https://developer.chrome.com/static/blog/cdp-command-editor/image/the-delete-parameter-3f6a0e8e36d79.png)

## Object parameters

When you enter a command that accepts object parameters, the editor lists the keys of this object and you can edit their values directly. This works for all types of nested parameters.

![Nested parameters.](https://developer.chrome.com/static/blog/cdp-command-editor/image/nested-parameters-5b9b453c5c064.png)

## Discover what the command and parameters do in the editor

Were you ever uncertain about the purpose of a parameter or command? Now, you can hover over a command or parameter, and a descriptive tooltip will pop up, complete with a link to the online documentation.

![The descriptive tooltip that appears when you hover over a command.](https://developer.chrome.com/static/blog/cdp-command-editor/image/the-descriptive-tooltip-bc7c1c83abf99.png)

## Be warned before sending incorrect parameters

Previously, if you didn't know if a parameter's value was of the correct type and had to wait to read the error response, this new editor is for you. It shows you real-time errors if the parameter can't accept the value you entered.

![An error icon next to a parameter with an incorrect value.](https://developer.chrome.com/static/blog/cdp-command-editor/image/an-error-icon-next-a-par-f165fd057308e.png)

## Resend a command

If you need to tweak a parameter of the command you just sent, you don't have to type it again. To edit and resend the command, right-click an item in the datagrid and select **Edit and resend** from the drop-down menu. This will automatically reopen the CDP editor and prefill it with the command you selected.

![The drop-down menu of a command in the datagrid with the 'Edit and resend' option.](https://developer.chrome.com/static/blog/cdp-command-editor/image/the-drop-down-menu-a-com-dfb6d6775c61c.png)

## Copy a command to JSON format

To copy the CDP command in JSON format to your clipboard, click the ![Copy.](https://developer.chrome.com/static/blog/cdp-command-editor/image/copy-e4ce7758a2f15.svg) copy icon at the leftmost end of the toolbar. Additionally, keep in mind that if you input a command directly into the input bar, it will seamlessly populate the editor, and the other way around.

## Conclusion

The DevTools team's goal behind the design of this new CDP editor was to simplify the typing of CDP commands. The new editor can also be used to view parameters alongside the documentation and to provide you with an easier way to send your CDP commands.

## Download the preview channels

Consider using the Chrome [Canary](https://www.google.com/chrome/canary/), [Dev](https://www.google.com/chrome/dev/), or [Beta](https://www.google.com/chrome/beta/) as your default development browser. These preview channels give you access to the latest DevTools features, let you test cutting-edge web platform APIs, and help you find issues on your site before your users do!

## Get in touch with the Chrome DevTools team

Use the following options to discuss the new features, updates, or anything else related to DevTools.

- Submit feedback and feature requests to us at [crbug.com](https://crbug.com).
- Report a DevTools issue using the **More options** \> **Help** \> **Report a DevTools issue** in DevTools.
- Tweet at [@ChromeDevTools](https://twitter.com/intent/tweet?text=@ChromeDevTools).
- Leave comments on [What's new in DevTools YouTube videos](https://goo.gle/devtools-youtube) or [DevTools Tips YouTube videos](https://goo.gle/devtools-tips).