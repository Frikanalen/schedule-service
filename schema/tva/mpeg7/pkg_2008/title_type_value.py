from enum import Enum

__NAMESPACE__ = "urn:tva:mpeg7:2008"


class TitleTypeValue(Enum):
    MAIN = "main"
    SECONDARY = "secondary"
    ALTERNATIVE = "alternative"
    ORIGINAL = "original"
    POPULAR = "popular"
    OPUS_NUMBER = "opusNumber"
    SONG_TITLE = "songTitle"
    ALBUM_TITLE = "albumTitle"
    SERIES_TITLE = "seriesTitle"
    EPISODE_TITLE = "episodeTitle"
