# Clicking issues

## 'Element is not clickable' error

ChromeDriver clicking works by simulating a mouse click in the middle of the
element's first client rect (or bounding client rect if it doesn't have a first
client rect). The easiest way to find out where ChromeDriver is attempting to
click is to open the chrome devtools and inspect the element to be clicked right
before your click operation is called. Select the element in the inspector and
notice the blue box(es) representing the client rects of the element, as
pictured below. ChromeDriver will attempt to click the middle of the first one.

If ChromeDriver is throwing the 'Element is not clickable' error, it's most
likely because that location is not actually clickable by the user. To test,
place your cursor in the middle of the first client rect yourself and see if
that location is clickable.

In the case above, the test was attempting to click the anchor element. The
anchor is not clickable in this case; only the child image is. Because of a
`margin-bottom` style on the image element, the middle of the anchor element
falls outside the clickable image bounds, and thus ChromeDriver throws an error.
For more info on how positioning or sizing is determined, see the W3 spec. To fix
the case above, click the image instead of the anchor.

The 'Element is not clickable' error often occurs in the following situations when a test tries to:

- Click an anchor whose clickable descendant elements are not within the anchor bounds (as above)
- Click an element fully or partially under another element
- Click an element offscreen when a fixed overlay is present (the element will be scrolled into view, but it may be scrolled under the fixed overlay)
- Click an element that is not clickable in the middle (for example, some types of convex SVG elements)

These issues can often be resolved either by clicking a child of the given element, by programmatically removing or hiding the blocking element, by using the advanced interactions API to click at an offset from the top-left of the element, or by simulating a mouse click event in javascript.

## 'Element is not clickable' error

This most likely occurs because the element's location has changed some time
after ChromeDriver determined the element's location but before ChromeDriver
actually issues a click at the location.

To determine if this is your problem, catch the exception from the click and
immediately log the current location and size of the element. Compare
that with the location that ChromeDriver reports it attempted to click in the
exception and see if they are different. If so, you need to wait for the element
to stop moving or try to click again. If not, file a bug with a small test page
that can be used to reproduce your problem (even if it only occasionally
triggers the problem).

## ChromeDriver can't click a moving element

This isn't a supported feature of ChromeDriver. If the element eventually
stops, wait for that to occur. If the element never stops moving, ChromeDriver
does not guarantee the click will be successful.