from enum import Enum

__NAMESPACE__ = "urn:tva:metadata:2019"


class SegmentGroupTypeTypeValue(Enum):
    HIGHLIGHTS = "highlights"
    HIGHLIGHTS_OBJECTS = "highlights/objects"
    HIGHLIGHTS_EVENTS = "highlights/events"
    BOOKMARKS = "bookmarks"
    BOOKMARKS_OBJECTS = "bookmarks/objects"
    BOOKMARKS_EVENTS = "bookmarks/events"
    THEME_GROUP = "themeGroup"
    PREVIEW = "preview"
    PREVIEW_TITLE = "preview/title"
    PREVIEW_SLIDESHOW = "preview/slideshow"
    TABLE_OF_CONTENTS = "tableOfContents"
    SYNOPSIS = "synopsis"
    SHOTS = "shots"
    INSERTION_POINTS = "insertionPoints"
    ALTERNATIVE_GROUPS = "alternativeGroups"
    ALTERNATIVE_SEGMENTS = "alternativeSegments"
    OTHER = "other"
