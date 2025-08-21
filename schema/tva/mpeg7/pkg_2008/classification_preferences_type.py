from dataclasses import dataclass, field

from schema.tva.mpeg7.pkg_2008.classification_preferences_type_caption_language import (
    ClassificationPreferencesTypeCaptionLanguage,
)
from schema.tva.mpeg7.pkg_2008.classification_preferences_type_country import (
    ClassificationPreferencesTypeCountry,
)
from schema.tva.mpeg7.pkg_2008.classification_preferences_type_date_period import (
    ClassificationPreferencesTypeDatePeriod,
)
from schema.tva.mpeg7.pkg_2008.classification_preferences_type_form import (
    ClassificationPreferencesTypeForm,
)
from schema.tva.mpeg7.pkg_2008.classification_preferences_type_genre import (
    ClassificationPreferencesTypeGenre,
)
from schema.tva.mpeg7.pkg_2008.classification_preferences_type_language import (
    ClassificationPreferencesTypeLanguage,
)
from schema.tva.mpeg7.pkg_2008.classification_preferences_type_language_format import (
    ClassificationPreferencesTypeLanguageFormat,
)
from schema.tva.mpeg7.pkg_2008.classification_preferences_type_parental_guidance import (
    ClassificationPreferencesTypeParentalGuidance,
)
from schema.tva.mpeg7.pkg_2008.classification_preferences_type_review import (
    ClassificationPreferencesTypeReview,
)
from schema.tva.mpeg7.pkg_2008.classification_preferences_type_subject import (
    ClassificationPreferencesTypeSubject,
)
from schema.tva.mpeg7.pkg_2008.dstype import Dstype

__NAMESPACE__ = "urn:tva:mpeg7:2008"


@dataclass
class ClassificationPreferencesType(Dstype):
    country: list[ClassificationPreferencesTypeCountry] = field(
        default_factory=list,
        metadata={
            "name": "Country",
            "type": "Element",
            "namespace": "urn:tva:mpeg7:2008",
        },
    )
    date_period: list[ClassificationPreferencesTypeDatePeriod] = field(
        default_factory=list,
        metadata={
            "name": "DatePeriod",
            "type": "Element",
            "namespace": "urn:tva:mpeg7:2008",
        },
    )
    language_format: list[ClassificationPreferencesTypeLanguageFormat] = field(
        default_factory=list,
        metadata={
            "name": "LanguageFormat",
            "type": "Element",
            "namespace": "urn:tva:mpeg7:2008",
        },
    )
    language: list[ClassificationPreferencesTypeLanguage] = field(
        default_factory=list,
        metadata={
            "name": "Language",
            "type": "Element",
            "namespace": "urn:tva:mpeg7:2008",
        },
    )
    caption_language: list[ClassificationPreferencesTypeCaptionLanguage] = (
        field(
            default_factory=list,
            metadata={
                "name": "CaptionLanguage",
                "type": "Element",
                "namespace": "urn:tva:mpeg7:2008",
            },
        )
    )
    form: list[ClassificationPreferencesTypeForm] = field(
        default_factory=list,
        metadata={
            "name": "Form",
            "type": "Element",
            "namespace": "urn:tva:mpeg7:2008",
        },
    )
    genre: list[ClassificationPreferencesTypeGenre] = field(
        default_factory=list,
        metadata={
            "name": "Genre",
            "type": "Element",
            "namespace": "urn:tva:mpeg7:2008",
        },
    )
    subject: list[ClassificationPreferencesTypeSubject] = field(
        default_factory=list,
        metadata={
            "name": "Subject",
            "type": "Element",
            "namespace": "urn:tva:mpeg7:2008",
        },
    )
    review: list[ClassificationPreferencesTypeReview] = field(
        default_factory=list,
        metadata={
            "name": "Review",
            "type": "Element",
            "namespace": "urn:tva:mpeg7:2008",
        },
    )
    parental_guidance: list[ClassificationPreferencesTypeParentalGuidance] = (
        field(
            default_factory=list,
            metadata={
                "name": "ParentalGuidance",
                "type": "Element",
                "namespace": "urn:tva:mpeg7:2008",
            },
        )
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
