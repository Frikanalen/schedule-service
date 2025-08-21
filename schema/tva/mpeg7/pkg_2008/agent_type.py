from dataclasses import dataclass, field

from schema.tva.mpeg7.pkg_2008.dstype import Dstype
from schema.tva.mpeg7.pkg_2008.media_locator_type import MediaLocatorType

__NAMESPACE__ = "urn:tva:mpeg7:2008"


@dataclass
class AgentType(Dstype):
    icon: list[MediaLocatorType] = field(
        default_factory=list,
        metadata={
            "name": "Icon",
            "type": "Element",
            "namespace": "urn:tva:mpeg7:2008",
        },
    )
