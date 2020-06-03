import enum

from ib_common.constants import BaseEnumClass


class CodeLanguage(BaseEnumClass, enum.Enum):
    python = "PYTHON"
    c_language = "C"
    c_plus_plus = "CPP"
    python36 = "PYTHON36"
    python37 = "PYTHON37"
    python38 = "PYTHON38"
    python38_datascience = "PYTHON38_DATASCIENCE"
    python38_aiml = "PYTHON38_AIML"

class AssetType(BaseEnumClass, enum.Enum):
    
    parcel = "parcel"
    bags = "bags"
    others = "others"

class SensitivityType(BaseEnumClass, enum.Enum):
    
    HighlySensitive = "Highly Sensitive"
    Sensitive = "Sensitive"
    Normal = "Normal"


class MediumType(BaseEnumClass, enum.Enum):
    
    Bus = "Bus"
    Train = "Train"
    Flight = "Flight"

class StatusValue(BaseEnumClass, enum.Enum):
    
    Expired = "Expired"
    Pending = "Pending"
    Confirmed = "Confirmed"