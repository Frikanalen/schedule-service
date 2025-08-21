from dataclasses import dataclass, field
from typing import Optional

from schema.tva.mpeg7.pkg_2008.dstype import Dstype
from schema.tva.mpeg7.pkg_2008.summary_preferences_type_summary_theme import (
    SummaryPreferencesTypeSummaryTheme,
)
from schema.tva.mpeg7.pkg_2008.summary_preferences_type_summary_type import (
    SummaryPreferencesTypeSummaryType,
)

__NAMESPACE__ = "urn:tva:mpeg7:2008"


@dataclass
class SummaryPreferencesType(Dstype):
    summary_type: list[SummaryPreferencesTypeSummaryType] = field(
        default_factory=list,
        metadata={
            "name": "SummaryType",
            "type": "Element",
            "namespace": "urn:tva:mpeg7:2008",
        },
    )
    summary_theme: list[SummaryPreferencesTypeSummaryTheme] = field(
        default_factory=list,
        metadata={
            "name": "SummaryTheme",
            "type": "Element",
            "namespace": "urn:tva:mpeg7:2008",
        },
    )
    summary_duration: Optional[str] = field(
        default=None,
        metadata={
            "name": "SummaryDuration",
            "type": "Element",
            "namespace": "urn:tva:mpeg7:2008",
            "pattern": r"\-?P(\d+D)?(T(\d+H)?(\d+M)?(\d+S)?(\d+N)?)?(\d+F)?",
        },
    )
    min_summary_duration: Optional[str] = field(
        default=None,
        metadata={
            "name": "MinSummaryDuration",
            "type": "Element",
            "namespace": "urn:tva:mpeg7:2008",
            "pattern": r"\-?P(\d+D)?(T(\d+H)?(\d+M)?(\d+S)?(\d+N)?)?(\d+F)?",
        },
    )
    max_summary_duration: Optional[str] = field(
        default=None,
        metadata={
            "name": "MaxSummaryDuration",
            "type": "Element",
            "namespace": "urn:tva:mpeg7:2008",
            "pattern": r"\-?P(\d+D)?(T(\d+H)?(\d+M)?(\d+S)?(\d+N)?)?(\d+F)?",
        },
    )
    num_of_key_frames: Optional[int] = field(
        default=None,
        metadata={
            "name": "NumOfKeyFrames",
            "type": "Element",
            "namespace": "urn:tva:mpeg7:2008",
        },
    )
    min_num_of_key_frames: Optional[int] = field(
        default=None,
        metadata={
            "name": "MinNumOfKeyFrames",
            "type": "Element",
            "namespace": "urn:tva:mpeg7:2008",
        },
    )
    max_num_of_key_frames: Optional[int] = field(
        default=None,
        metadata={
            "name": "MaxNumOfKeyFrames",
            "type": "Element",
            "namespace": "urn:tva:mpeg7:2008",
        },
    )
    num_of_chars: Optional[int] = field(
        default=None,
        metadata={
            "name": "NumOfChars",
            "type": "Element",
            "namespace": "urn:tva:mpeg7:2008",
        },
    )
    min_num_of_chars: Optional[int] = field(
        default=None,
        metadata={
            "name": "MinNumOfChars",
            "type": "Element",
            "namespace": "urn:tva:mpeg7:2008",
        },
    )
    max_num_of_chars: Optional[int] = field(
        default=None,
        metadata={
            "name": "MaxNumOfChars",
            "type": "Element",
            "namespace": "urn:tva:mpeg7:2008",
        },
    )
    preference_value: int = field(
        default=10,
        metadata={
            "name": "preferenceValue",
            "type": "Attribute",
            "min_inclusive": -100,
            "max_inclusive": 100,
        },
    )
