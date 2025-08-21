from dataclasses import dataclass

from schema.tva.metadata.pkg_2019.tvamain_type import TvamainType

__NAMESPACE__ = "urn:tva:metadata:2019"


@dataclass
class Tvamain(TvamainType):
    class Meta:
        name = "TVAMain"
        namespace = "urn:tva:metadata:2019"
