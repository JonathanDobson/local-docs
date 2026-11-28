# Animation domain *(experimental)*

Copyright 2017 The Chromium Authors Use of this source code is governed by a BSD-style license that can be found in the LICENSE file.  Contributing to Chrome DevTools Protocol: https://goo.gle/devtools-contribution-guide-cdp

Depends on: [Runtime](Runtime.md), [DOM](DOM.md)

Methods are called as `Animation.<command>` and events arrive as `Animation.<event>`.

## Commands

### Animation.disable

Disables animation domain notifications.

### Animation.enable

Enables animation domain notifications.

### Animation.getCurrentTime

Returns the current time of the an animation.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `id` | string | Id of animation. |

**Returns**

| Name | Type | Description |
|---|---|---|
| `currentTime` | number | Current time of the page. |

### Animation.getPlaybackRate

Gets the playback rate of the document timeline.

**Returns**

| Name | Type | Description |
|---|---|---|
| `playbackRate` | number | Playback rate for animations on page. |

### Animation.releaseAnimations

Releases a set of animations to no longer be manipulated.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `animations` | array of string | List of animation ids to seek. |

### Animation.resolveAnimation

Gets the remote object of the Animation.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `animationId` | string | Animation id. |

**Returns**

| Name | Type | Description |
|---|---|---|
| `remoteObject` | [Runtime.RemoteObject](Runtime.md#type-remoteobject) | Corresponding remote object. |

### Animation.seekAnimations

Seek a set of animations to a particular time within each animation.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `animations` | array of string | List of animation ids to seek. |
| `currentTime` (optional) | number | Set each animation to the same time. |
| `currentTimes` (optional) | array of number | Set each animation to a different time. If set, should have the same length as animations. Exactly one of currentTime or currentTimes should be set. |

### Animation.setPaused

Sets the paused state of a set of animations.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `animations` | array of string | Animations to set the pause state of. |
| `paused` | boolean | Paused state to set to. |

### Animation.setPlaybackRate

Sets the playback rate of the document timeline.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `playbackRate` | number | Playback rate for animations on page |

### Animation.setTiming

Sets the timing of an animation node.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `animationId` | string | Animation id. |
| `duration` | number | Duration of the animation. |
| `delay` | number | Delay of the animation. |

## Events

### Animation.animationCanceled

Event for when an animation has been cancelled.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `id` | string | Id of the animation that was cancelled. |

### Animation.animationCreated

Event for each animation that has been created.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `id` | string | Id of the animation that was created. |

### Animation.animationStarted

Event for animation that has been started.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `animation` | [Animation](#type-animation) | Animation that was started. |

### Animation.animationUpdated

Event for animation that has been updated.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `animation` | [Animation](#type-animation) | Animation that was updated. |

## Types

<a id="type-animation"></a>
### Animation.Animation

Type: object

Animation instance.

**Properties**

| Name | Type | Description |
|---|---|---|
| `id` | string | `Animation`'s id. |
| `name` | string | `Animation`'s name. |
| `pausedState` | boolean | `Animation`'s internal paused state. |
| `playState` | string | `Animation`'s play state. |
| `playbackRate` | number | `Animation`'s playback rate. |
| `startTime` | number | `Animation`'s start time. Milliseconds for time based animations and percentage [0 - 100] for scroll driven animations (i.e. when viewOrScrollTimeline exists). |
| `currentTime` | number | `Animation`'s current time. |
| `type` | enum: `CSSTransition`, `CSSAnimation`, `WebAnimation` | Animation type of `Animation`. |
| `source` (optional) | [AnimationEffect](#type-animationeffect) | `Animation`'s source animation node. |
| `cssId` (optional) | string | A unique ID for `Animation` representing the sources that triggered this CSS animation/transition. |
| `viewOrScrollTimeline` (optional) | [ViewOrScrollTimeline](#type-vieworscrolltimeline) | View or scroll timeline |

<a id="type-vieworscrolltimeline"></a>
### Animation.ViewOrScrollTimeline

Type: object

Timeline instance

**Properties**

| Name | Type | Description |
|---|---|---|
| `sourceNodeId` (optional) | [DOM.BackendNodeId](DOM.md#type-backendnodeid) | Scroll container node |
| `startOffset` (optional) | number | Represents the starting scroll position of the timeline as a length offset in pixels from scroll origin. |
| `endOffset` (optional) | number | Represents the ending scroll position of the timeline as a length offset in pixels from scroll origin. |
| `subjectNodeId` (optional) | [DOM.BackendNodeId](DOM.md#type-backendnodeid) | The element whose principal box's visibility in the scrollport defined the progress of the timeline. Does not exist for animations with ScrollTimeline |
| `axis` | [DOM.ScrollOrientation](DOM.md#type-scrollorientation) | Orientation of the scroll |

<a id="type-animationeffect"></a>
### Animation.AnimationEffect

Type: object

AnimationEffect instance

**Properties**

| Name | Type | Description |
|---|---|---|
| `delay` | number | `AnimationEffect`'s delay. |
| `endDelay` | number | `AnimationEffect`'s end delay. |
| `iterationStart` | number | `AnimationEffect`'s iteration start. |
| `iterations` (optional) | number | `AnimationEffect`'s iterations. Omitted if the value is infinite. |
| `duration` | number | `AnimationEffect`'s iteration duration. Milliseconds for time based animations and percentage [0 - 100] for scroll driven animations (i.e. when viewOrScrollTimeline exists). |
| `direction` | string | `AnimationEffect`'s playback direction. |
| `fill` | string | `AnimationEffect`'s fill mode. |
| `backendNodeId` (optional) | [DOM.BackendNodeId](DOM.md#type-backendnodeid) | `AnimationEffect`'s target node. |
| `keyframesRule` (optional) | [KeyframesRule](#type-keyframesrule) | `AnimationEffect`'s keyframes. |
| `easing` | string | `AnimationEffect`'s timing function. |

<a id="type-keyframesrule"></a>
### Animation.KeyframesRule

Type: object

Keyframes Rule

**Properties**

| Name | Type | Description |
|---|---|---|
| `name` (optional) | string | CSS keyframed animation's name. |
| `keyframes` | array of [KeyframeStyle](#type-keyframestyle) | List of animation keyframes. |

<a id="type-keyframestyle"></a>
### Animation.KeyframeStyle

Type: object

Keyframe Style

**Properties**

| Name | Type | Description |
|---|---|---|
| `offset` | string | Keyframe's time offset. |
| `easing` | string | `AnimationEffect`'s timing function. |

