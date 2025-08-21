from enum import Enum

__NAMESPACE__ = "urn:tva:mpeg7:2008"


class SummaryComponentTypeValue(Enum):
    AUDIO = "audio"
    VISUAL = "visual"
    AUDIO_VISUAL = "audioVisual"
    TEXTUAL = "textual"
    KEY_AUDIO_CLIPS = "keyAudioClips"
    KEY_VIDEO_CLIPS = "keyVideoClips"
    KEY_AUDIO_VISUAL_CLIPS = "keyAudioVisualClips"
    KEY_FRAMES = "keyFrames"
    KEY_SOUNDS = "keySounds"
    KEY_THEMES = "keyThemes"
