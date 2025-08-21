from dataclasses import dataclass

from schema.tva.mpeg7.pkg_2008.mpeg7_base_type import Mpeg7BaseType

__NAMESPACE__ = "urn:tva:mpeg7:2008"


@dataclass
class Dtype(Mpeg7BaseType):
    class Meta:
        name = "DType"
