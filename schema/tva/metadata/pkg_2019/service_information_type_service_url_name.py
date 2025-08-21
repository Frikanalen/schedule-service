from enum import Enum

__NAMESPACE__ = "urn:tva:metadata:2019"


class ServiceInformationTypeServiceUrlName(Enum):
    DTT = "DTT"
    CATV = "CATV"
    DTH = "DTH"
    WWW = "WWW"
    IPTV = "IPTV"
    OTHER = "other"
