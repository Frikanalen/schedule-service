from dataclasses import dataclass, field
from typing import Optional

from schema.tva.metadata.pkg_2019.base_program_group_type_type import (
    BaseProgramGroupTypeType,
)
from schema.tva.metadata.pkg_2019.program_group_type_type_value import (
    ProgramGroupTypeTypeValue,
)

__NAMESPACE__ = "urn:tva:metadata:2019"


@dataclass
class ProgramGroupTypeType(BaseProgramGroupTypeType):
    value: Optional[ProgramGroupTypeTypeValue] = field(
        default=None,
        metadata={
            "type": "Attribute",
            "required": True,
        },
    )
