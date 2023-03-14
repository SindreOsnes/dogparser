import struct
from typing import List, Union
from datetime import date

from ...utils import graceful_conversion, date_conversion, extract_decimal

class Kaaringer:
    _reg_nr: str # Registration number (REG.NR in original schema)
    _navn: str # Name (NAVN in original schema)
    _ktid_id: int # KTID (KTID in original schema)
    _wid: Union[float, None] # WID (WID in original schema)
    _brt: Union[float, None] # BRT (BRT in original schema)
    _bru: Union[float, None] # BRU (BRU in original schema)
    _gew: Union[float, None] # GEW (GEW in original schema)

    def __init__(self, reg_nr: str, navn: str, ktid_id: int
               , wid: Union[float, None], brt: Union[float, None], bru: Union[float, None]
               , gew: Union[float, None]) -> None:
        self._reg_nr = reg_nr
        self._navn = navn
        self._ktid_id = ktid_id
        self._wid = wid
        self._brt = brt
        self._bru = bru
        self._gew = gew

    @classmethod
    def from_bytes(cls, content: bytes):
        if len(content) != 70:
            raise AssertionError("Input for Kaaringer should be 70 bytes")

        # The Awards Statistics table contains a 5 byte header that does not contain useful data
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

        # Parse the KTID property
        ktid_id = sub_content[0] # KTID (KTID is an enum represented by a 1 byte integer)
        # Remove used data from next entries
        sub_content = sub_content[1:]

        # Parse the WID property
        wid = extract_decimal(sub_content[:4]) # WID (WID is a 1 byte integer)
        # Remove used data from next entries
        sub_content = sub_content[4:]

        # Parse the BRT property
        brt = extract_decimal(sub_content[:4]) # BRT (BRT is a 1 byte integer)
        # Remove used data from next entries
        sub_content = sub_content[4:]

        # Parse the BRU property
        bru = extract_decimal(sub_content[:4]) # BRU (BRU is a 1 byte integer)
        # Remove used data from next entries
        sub_content = sub_content[4:]

        # Parse the GEW property
        gew = extract_decimal(sub_content[:4]) # GEW (GEW is a 1 byte integer)
        # Remove used data from next entries
        sub_content = sub_content[4:]

        return cls(reg_nr=reg_nr,
                   navn=navn,
                   ktid_id=ktid_id,
                   wid=wid,
                   brt=brt,
                   bru=bru,
                   gew=gew)

    @property
    def reg_nr(self) -> str:
        return self._reg_nr

    @property
    def navn(self) -> str:
        return self._navn

    @property
    def ktid_id(self) -> int:
        return self._ktid_id

    @property
    def wid(self) -> Union[float, None]:
        return None if not self._wid else self._wid

    @property
    def brt(self) -> Union[float, None]:
        return None if not self._brt else self._brt

    @property
    def bru(self) -> Union[float, None]:
        return None if not self._bru else self._bru

    @property
    def gew(self) -> Union[float, None]:
        return None if not self._gew else self._gew

    @property
    def native(self) -> dict:
        """Method converts class instance to native python classes for serialization purposes"""

        obj_dict = {
            'reg_nr': self.reg_nr,
            'navn': self.navn,
            'ktid_id': self.ktid_id,
            'wid': self.wid,
            'brt': self.brt,
            'bru': self.bru,
            'gew': self.gew,
        }

        return obj_dict

class KaaringerList:

    _contents: List[Kaaringer]

    def __init__(self, contents:List[Kaaringer]=[]) -> None:
        self._contents = contents
    
    @property
    def native(self) -> dict:
        """Method converts class instance to native python classes for serialization purposes"""

        return [i.native for i in self._contents]
