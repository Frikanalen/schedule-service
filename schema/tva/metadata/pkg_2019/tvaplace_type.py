from dataclasses import dataclass, field

from schema.tva.mpeg7.pkg_2008.place_type import PlaceType

__NAMESPACE__ = "urn:tva:metadata:2019"


@dataclass
class TvaplaceType(PlaceType):
    class Meta:
        name = "TVAPlaceType"

    fictional: bool = field(
        default=False,
        metadata={
            "type": "Attribute",
        },
    )
