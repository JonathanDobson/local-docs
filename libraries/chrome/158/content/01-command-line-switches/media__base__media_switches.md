# Command-line switches: `media/base/media_switches`

Generated from `media/base/media_switches.h` and `media/base/media_switches.cc` in the Chromium source. Each switch is passed to the browser as `--name` or `--name=value`. The description is the source comment verbatim; *Condition* is the build/platform `#if` it is defined under.

55 switches.

## `--document-user-activation-required`

- Constant: `kDocumentUserActivationRequiredPolicy`

Autoplay policy that requires a document user activation.

## `--no-user-gesture-required`

- Constant: `kNoUserGestureRequiredPolicy`

Autoplay policy that does not require any user gesture.

## `--user-gesture-required`

- Constant: `kUserGestureRequiredPolicy`

Autoplay policy to require a user gesture in order to play.

## `--audio-buffer-size`

- Constant: `kAudioBufferSize`

Allow users to specify a custom buffer size for debugging purpose.

## `--auto-grant-captured-surface-control-prompt`

- Constant: `kAutoGrantCapturedSurfaceControlPrompt`

Skip the permission prompt for Captured Surface Control.

## `--autoplay-policy`

- Constant: `kAutoplayPolicy`

Command line flag name to set the autoplay policy.

## `--cast-streaming-force-disable-hardware-av1`

- Constant: `kCastStreamingForceDisableHardwareAv1`

NOTE: callers should always use the free functions in /media/cast/encoding/encoding_support.h instead of accessing these features directly.  TODO(crbug.com/286443864): Guard Cast Sender flags with !IS_ANDROID. If enabled, completely disables use of AV1 hardware encoding for Cast Streaming sessions.

## `--cast-streaming-force-disable-hardware-h264`

- Constant: `kCastStreamingForceDisableHardwareH264`

If enabled, completely disables use of H264 hardware encoding for Cast Streaming sessions. Takes precedence over kCastStreamingForceEnableHardwareH264.

## `--cast-streaming-force-disable-hardware-hevc`

- Constant: `kCastStreamingForceDisableHardwareHevc`

If enabled, completely disables use of HEVC hardware encoding for Cast Streaming sessions. Takes precedence over kCastStreamingForceEnableHardwareHevc.

## `--cast-streaming-force-disable-hardware-vp8`

- Constant: `kCastStreamingForceDisableHardwareVp8`

If enabled, completely disables use of VP8 hardware encoding for Cast Streaming sessions. Takes precedence over kCastStreamingForceEnableHardwareVp8.

## `--cast-streaming-force-disable-hardware-vp9`

- Constant: `kCastStreamingForceDisableHardwareVp9`

If enabled, completely disables use of VP9 hardware encoding for Cast Streaming sessions. Takes precedence over kCastStreamingForceEnableHardwareVp9.

## `--cast-streaming-force-enable-hardware-av1`

- Constant: `kCastStreamingForceEnableHardwareAv1`

If enabled, allows use of AV1 hardware encoding for Cast Streaming sessions, even on platforms where it is disabled due to performance and reliability issues. kCastStreamingForceDisableHardwareAv1 must be disabled for this flag to take effect.

## `--cast-streaming-force-enable-hardware-h264`

- Constant: `kCastStreamingForceEnableHardwareH264`

If enabled, allows use of H264 hardware encoding for Cast Streaming sessions, even on platforms where it is disabled due to performance and reliability issues. kCastStreamingForceDisableHardwareH264 must be disabled for this flag to take effect.

## `--cast-streaming-force-enable-hardware-hevc`

- Constant: `kCastStreamingForceEnableHardwareHevc`

If enabled, allows use of HEVC hardware encoding for Cast Streaming sessions, even on platforms where it is disabled due to performance and reliability issues. kCastStreamingForceDisableHardwareHevc must be disabled for this flag to take effect.

## `--cast-streaming-force-enable-hardware-vp8`

- Constant: `kCastStreamingForceEnableHardwareVp8`

If enabled, allows use of VP8 hardware encoding for Cast Streaming sessions, even on platforms where it is disabled due to performance and reliability issues. kCastStreamingForceDisableHardwareVp8 must be disabled for this flag to take effect.

## `--cast-streaming-force-enable-hardware-vp9`

- Constant: `kCastStreamingForceEnableHardwareVp9`

If enabled, allows use of VP9 hardware encoding for Cast Streaming sessions, even on platforms where it is disabled due to performance and reliability issues. kCastStreamingForceDisableHardwareVp9 must be disabled for this flag to take effect.

## `--clear-key-cdm-path-for-testing`

- Constant: `kClearKeyCdmPathForTesting`

Specifies the path to the Clear Key CDM for testing, which is necessary to support External Clear Key key system when library CDM is enabled. Note that External Clear Key key system support is also controlled by feature kExternalClearKeyForTesting.

## `--disable-accelerated-mjpeg-decode`

- Constant: `kDisableAcceleratedMjpegDecode`

Disable hardware acceleration of mjpeg decode for captured frame, where available.

## `--disable-audio-input`

- Constant: `kDisableAudioInput`

Forces input and output stream creation to use fake audio streams.

## `--disable-audio-output`

- Constant: `kDisableAudioOutput`

_No description in the source._

## `--disable-background-media-suspend`

- Constant: `kDisableBackgroundMediaSuspend`

Do not immediately suspend media in background tabs.

## `--disable-rtc-smoothness-algorithm`

- Constant: `kDisableRTCSmoothnessAlgorithm`

Disables the new rendering algorithm for webrtc, which is designed to improve the rendering smoothness.

## `--enable-live-caption-pref-for-testing`

- Constant: `kEnableLiveCaptionPrefForTesting`

Sets the default value for the kLiveCaptionEnabled preference to true.

## `--fail-audio-stream-creation`

- Constant: `kFailAudioStreamCreation`

Causes the AudioManager to fail creating audio streams. Used when testing various failure cases.

## `--fake-background-blur-toggle-period`

- Constant: `kFakeBackgroundBlurTogglePeriod`

Inserts fake background blur state into `VideoFrameMetadata`. The value represents the period in milliseconds. eg. Setting it to 1000ms, will cause the blur state to cycle between reporting ENABLED for 500ms and DISABLED for 500ms.

## `--force-video-overlays`

- Constant: `kForceVideoOverlays`

Force media player using SurfaceView instead of SurfaceTexture on Android. Note: This is used by the Cast playback pipeline and must be kept.

## `--mse-audio-buffer-size-limit-mb`

- Constant: `kMSEAudioBufferSizeLimitMb`

Allows explicitly specifying MSE audio/video buffer sizes as megabytes. Default values are 150M for video and 12M for audio.

## `--mse-video-buffer-size-limit-mb`

- Constant: `kMSEVideoBufferSizeLimitMb`

_No description in the source._

## `--mute-audio`

- Constant: `kMuteAudio`

Mutes audio sent to the audio device so it is not audible during automated testing.

## `--override-enabled-cdm-interface-version`

- Constant: `kOverrideEnabledCdmInterfaceVersion`

Overrides the default enabled library CDM interface version(s) with the one specified with this switch, which will be the only version enabled. For example, on a build where CDM 8, CDM 9 and CDM 10 are all supported (implemented), but only CDM 8 and CDM 9 are enabled by default: --override-enabled-cdm-interface-version=8 : Only CDM 8 is enabled --override-enabled-cdm-interface-version=9 : Only CDM 9 is enabled --override-enabled-cdm-interface-version=10 : Only CDM 10 is enabled --override-enabled-cdm-interface-version=11 : No CDM interface is enabled This can be used for local testing and debugging. It can also be used to enable an experimental CDM interface (which is always disabled by default) for testing while it's still in development.

## `--override-hardware-secure-codecs-for-testing`

- Constant: `kOverrideHardwareSecureCodecsForTesting`

Overrides hardware secure codecs support for testing. If specified, real platform hardware secure codecs check will be skipped. Valid codecs are: - video: "vp8", "vp9", "avc1", "hevc", "dolbyvision", "av01" - video that does not support clear lead: `<video>-no-clearlead`, where <video> is from the list above. - audio: "mp4a", "vorbis" Codecs are separated by comma. For example: --override-hardware-secure-codecs-for-testing=vp8,vp9-no-clearlead,vorbis --override-hardware-secure-codecs-for-testing=avc1,mp4a CENC encryption scheme is assumed to be supported for the specified codecs. If no valid codecs specified, no hardware secure codecs are supported. This can be used to disable hardware secure codecs support: --override-hardware-secure-codecs-for-testing

## `--report-vp9-as-an-unsupported-mime-type`

- Constant: `kReportVp9AsAnUnsupportedMimeType`

Force to report VP9 as an unsupported MIME type.

## `--use-fake-device-for-media-stream`

- Constant: `kUseFakeDeviceForMediaStream`

Use fake device for Media Stream to replace actual camera and microphone. For the list of allowed parameters, see FakeVideoCaptureDeviceFactory::ParseFakeDevicesConfigFromOptionsString().

## `--use-fake-mjpeg-decode-accelerator`

- Constant: `kUseFakeMjpegDecodeAccelerator`

Use a fake device for accelerated decoding of MJPEG. This allows, for example, testing of the communication to the GPU service without requiring actual accelerator hardware to be present.

## `--use-file-for-fake-audio-capture`

- Constant: `kUseFileForFakeAudioCapture`

Play a .wav file as the microphone. Note that for WebRTC calls we'll treat the bits as if they came from the microphone, which means you should disable audio processing (lest your audio file will play back distorted). The input file is converted to suit Chrome's audio buses if necessary, so most sane .wav files should work. You can pass either <path> to play the file looping or <path>%noloop to stop after playing the file to completion.  Must also be used with kDisableAudioInput or kUseFakeDeviceForMediaStream.

## `--use-file-for-fake-video-capture`

- Constant: `kUseFileForFakeVideoCapture`

Use an .y4m file to play as the webcam. See the comments in media/capture/video/file_video_capture_device.h for more details.

## `--video-threads`

- Constant: `kVideoThreads`

Set number of threads to use for video decoding.

## `--audio-codecs-from-edid`

- Constant: `kAudioCodecsFromEDID`
- Condition: `BUILDFLAG(ENABLE_PASSTHROUGH_AUDIO_CODECS)`

Audio codecs supported by the HDMI sink is retrieved from the audio service process. EDID contains the Short Audio Descriptors, which list the audio decoders supported, and the information is presented as a bitmask of supported audio codecs.

## `--allow-ra-in-dev-mode`

- Constant: `kAllowRAInDevMode`
- Condition: `BUILDFLAG(IS_CHROMEOS)`

Allows remote attestation (RA) in dev mode for testing purpose. Usually RA is disabled in dev mode because it will always fail. However, there are cases in testing where we do want to go through the permission flow even in dev mode. This can be enabled by this flag.

## `--audio-capturer-with-echo-cancellation`

- Constant: `kAudioCapturerWithEchoCancellation`
- Condition: `BUILDFLAG(IS_FUCHSIA)`

Forces AudioManagerFuchsia to assume that the AudioCapturer implements echo cancellation. TODO(crbug.com/42050621): Remove this once AudioManagerFuchsia is updated to get this information from AudioCapturerFactory.

## `--enable-protected-video-buffers`

- Constant: `kEnableProtectedVideoBuffers`
- Condition: `BUILDFLAG(IS_FUCHSIA)`

Enables protected buffers for encrypted video streams.

## `--force-protected-video-output-buffers`

- Constant: `kForceProtectedVideoOutputBuffers`
- Condition: `BUILDFLAG(IS_FUCHSIA)`

Forces protected memory for all output video buffers generated by FuchsiaVideoDecoder, including unencrypted streams. Ignored unless --enable-protected-video-buffers is also specified.

## `--min-video-decoder-output-buffer-size`

- Constant: `kMinVideoDecoderOutputBufferSize`
- Condition: `BUILDFLAG(IS_FUCHSIA)`

Minimum size for buffer size used for output video frames in FuchsiaVideoDecoder. May be set to avoid re-allocating video buffers when an application upgrades video resolution mid-stream.

## `--alsa-input-device`

- Constant: `kAlsaInputDevice`
- Condition: `BUILDFLAG(IS_LINUX) || BUILDFLAG(IS_CHROMEOS) || BUILDFLAG(IS_FREEBSD) || \`

The Alsa device to use when opening an audio input stream.

## `--alsa-output-device`

- Constant: `kAlsaOutputDevice`
- Condition: `BUILDFLAG(IS_LINUX) || BUILDFLAG(IS_CHROMEOS) || BUILDFLAG(IS_FREEBSD) || \`

The Alsa device to use when opening an audio stream.

## `--enable-exclusive-audio`

- Constant: `kEnableExclusiveAudio`
- Condition: `BUILDFLAG(IS_WIN)`

Use exclusive mode audio streaming for Windows Vista and higher. Leads to lower latencies for audio streams which uses the AudioParameters::AUDIO_PCM_LOW_LATENCY audio path. See http://msdn.microsoft.com/en-us/library/windows/desktop/dd370844.aspx for details.

## `--force-wave-audio`

- Constant: `kForceWaveAudio`
- Condition: `BUILDFLAG(IS_WIN)`

Use Windows WaveOut/In audio API even if Core Audio is supported.

## `--try-supported-channel-layouts`

- Constant: `kTrySupportedChannelLayouts`
- Condition: `BUILDFLAG(IS_WIN)`

Instead of always using the hardware channel layout, check if a driver supports the source channel layout.  Avoids outputting empty channels and permits drivers to enable stereo to multichannel expansion.  Kept behind a flag since some drivers lie about supported layouts and hang when used.  See http://crbug.com/259165 for more details.

## `--waveout-buffers`

- Constant: `kWaveOutBuffers`
- Condition: `BUILDFLAG(IS_WIN)`

Number of buffers to use for WaveOut.

## `--system-aec-enabled`

- Constant: `kSystemAecEnabled`
- Condition: `BUILDFLAG(USE_CRAS)`

Enforce system audio echo cancellation.

## `--use-cras`

- Constant: `kUseCras`
- Condition: `BUILDFLAG(USE_CRAS)`

Use CRAS, the ChromeOS audio server.

## `--hardware-video-decode-framerate`

- Constant: `kHardwareVideoDecodeFrameRate`
- Condition: `BUILDFLAG(USE_V4L2_CODEC)`

Some (Qualcomm only at the moment) V4L2 video decoders require setting the framerate so that the hardware decoder can scale the clocks efficiently. This provides a mechanism during testing to lock the decoder framerate to a specific value.

## `--enable-primary-node-access-for-vkms-testing`

- Constant: `kEnablePrimaryNodeAccessForVkmsTesting`
- Condition: `BUILDFLAG(USE_V4L2_CODEC) || BUILDFLAG(USE_VAAPI)`

This is needed for V4L2/VAAPI testing using VISL or libfake (virtual drivers) on cros VMs. Minigbm buffer allocation is done using the dumb driver with vkms.

## `--hardware-video-device-path`

- Constant: `kHardwareVideoDevicePath`
- Condition: `BUILDFLAG(USE_VAAPI)`

Allows explicitly picking a device path to find the device for VA-API video decoding and encoding.

## `--unsafely-allow-protected-media-identifier-for-domain`

- Constant: `kUnsafelyAllowProtectedMediaIdentifierForDomain`

For automated testing of protected content, this switch allows specific domains (e.g. example.com) to always allow the permission to share the protected media identifier. In this context, domain does not include the port number. User's content settings will not be affected by enabling this switch. Reference: https://crbug.com/41317087 Example: --unsafely-allow-protected-media-identifier-for-domain=a.com,b.ca
