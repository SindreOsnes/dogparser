import struct
from typing import List, Union
from datetime import date

from ...utils import graceful_conversion, date_conversion, extract_decimal

class Kaaringsbeskrivelse:
    _reg_nr: str # Registration number (REG.NR in original schema)
    _navn: str # Name (NAVN in original schema)
    _k1: Union[str, None] # K1 (K1 in original schema)
    _k2: Union[str, None] # K2 (K2 in original schema)
    _v: Union[str, None] # V (V in original schema)
    _vi: Union[str, None] # VI (VI in original schema)

    def __init__(self, reg_nr: str, navn: str, k1: Union[str, None]
               , k2: Union[str, None], v: Union[str, None], vi: Union[str, None]) -> None:
        self._reg_nr = reg_nr
        self._navn = navn
        self._k1 = k1
        self._k2 = k2
        self._v = v
        self._vi = vi

    @classmethod
    def from_bytes(cls, content: bytes):
        if len(content) != 839:
            raise AssertionError("Input for Kaaringsbeskrivelse should be 839 bytes")

        # The Awards descriptions table contains a 5 byte header that does not contain useful data
        # Remove used data from next entries
        sub_content = content[5:]

        # Parse the REG.NR property
        reg_nr = graceful_conversion(sub_content[:12]) # REG.NR (Registration number is a string capped at 12 characters)
        # Remove used data from next entries
        sub_content = sub_content[12:]

        # Parse the NAVN property
        navn = graceful_conversion(sub_content[:36]) # NAVN (Name is a string capped at 36 characters)
        # Remove used data from next entries
        sub_content = sub_content[36:]

        # Parse the K1 property
        k1 = graceful_conversion(sub_content[:255]) # K1 (K1 is a string capped at 255 characters)
        # Remove used data from next entries
        sub_content = sub_content[255:]

        # Parse the K2 property
        k2 = graceful_conversion(sub_content[:255]) # K2 (K2 is a string capped at 255 characters)
        # Remove used data from next entries
        sub_content = sub_content[255:]

        # Parse the V property
        v = graceful_conversion(sub_content[:135]) # V (V is a string capped at 135 characters)
        # Remove used data from next entries
        sub_content = sub_content[135:]

        # Parse the VI property
        vi = graceful_conversion(sub_content[:141]) # VI (VI is a string capped at 141 characters)
        # Remove used data from next entries
        sub_content = sub_content[141:]

        return cls(reg_nr=reg_nr,
                   navn=navn,
                   k1=k1,
                   k2=k2,
                   v=v,
                   vi=vi)

    @property
    def reg_nr(self) -> str:
        return self._reg_nr

    @property
    def navn(self) -> str:
        return self._navn

    @property
    def k1(self) -> Union[str, None]:
        return None if not self._k1 else self._k1

    @property
    def k2(self) -> Union[str, None]:
        return None if not self._k2 else self._k2

    @property
    def v(self) -> Union[str, None]:
        return None if not self._v else self._v

    @property
    def vi(self) -> Union[str, None]:
        return None if not self._vi else self._vi

    @property
    def native(self) -> dict:
        """Method converts class instance to native python classes for serialization purposes"""

        obj_dict = {
            'reg_nr': self.reg_nr,
            'navn': self.navn,
            'k1': self.k1,
            'k2': self.k2,
            'v': self.v,
            'vi': self.vi,
        }

        return obj_dict

class KaaringsbeskrivelseList:

    _contents: List[Kaaringsbeskrivelse]

    def __init__(self, contents:List[Kaaringsbeskrivelse]=[]) -> None:
        self._contents = contents
    
    @property
    def native(self) -> dict:
        """Method converts class instance to native python classes for serialization purposes"""

        return [i.native for i in self._contents]
