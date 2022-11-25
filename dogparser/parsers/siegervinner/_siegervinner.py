from typing import List, Union
from datetime import date

from ...utils import graceful_conversion, date_conversion

class Siegervinner:
    _reg_nr: str # Registration number (REG.NR in original schema)
    _katalog_nummer: str # Catalog number (KATALOG-NUMMER in original schema)
    _navn: str # Name of dog (NAVN in original schema)
    _grad_id: int # Grade (GRAD in original schema)
    _plass: int # Pacement (PLASS in original schema)
    _l_id: int # Country (L in original schema)
    _aar: Union[str, None] # Year (ÅR in original schema)
    _plassering: Union[str, None] # Placement string (PLASSERING in original schema)
    _klasse_id: int # Class (KLASSE in original schema)

    def __init__(self, reg_nr: str, katalog_nummer: str, navn: str
, grad_id: int, plass: int, l_id: int
, aar: Union[str, None], plassering: Union[str, None], klasse_id: int) -> None:
        self._reg_nr = reg_nr
        self._katalog_nummer = katalog_nummer
        self._navn = navn
        self._grad_id = grad_id
        self._plass = plass
        self._l_id = l_id
        self._aar = aar
        self._plassering = plassering
        self._klasse_id = klasse_id

    @classmethod
    def from_bytes(cls, content: bytes):
        if len(content) != 79:
            raise AssertionError("Input for Siegervinner should be 79 bytes")

        # The Showcase winners table contains a 5 byte header that does not contain useful data
        # Remove used data from next entries
        sub_content = content[5:]

        # Parse the REG.NR property
        reg_nr = graceful_conversion(sub_content[:12]) # REG.NR (Registration number is a string capped at 12 characters)
        # Remove used data from next entries
        sub_content = sub_content[12:]

        # Parse the KATALOG-NUMMER property
        katalog_nummer = graceful_conversion(sub_content[:4]) # KATALOG-NUMMER (Catalog number is a string capped at 4 characters)
        # Remove used data from next entries
        sub_content = sub_content[4:]

        # Parse the NAVN property
        navn = graceful_conversion(sub_content[:36]) # NAVN (Name of dog is a string capped at 36 characters)
        # Remove used data from next entries
        sub_content = sub_content[36:]

        # Parse the GRAD property
        grad_id = sub_content[0] # GRAD (Grade is an enum represented by a 1 byte integer)
        # Remove used data from next entries
        sub_content = sub_content[1:]

        # Parse the PLASS property
        plass = sub_content[0] # PLASS (Pacement is a 1 byte integer)
        # Remove used data from next entries
        sub_content = sub_content[1:]

        # Skip unused bytes
        sub_content = sub_content[1:]

        # Parse the L property
        l_id = sub_content[0] # L (Country is an enum represented by a 1 byte integer)
        # Remove used data from next entries
        sub_content = sub_content[1:]

        # Parse the ÅR property
        aar = graceful_conversion(sub_content[:4]) # ÅR (Year is a string capped at 4 characters)
        # Remove used data from next entries
        sub_content = sub_content[4:]

        # Parse the PLASSERING property
        plassering = graceful_conversion(sub_content[:13]) # PLASSERING (Placement string is a string capped at 13 characters)
        # Remove used data from next entries
        sub_content = sub_content[13:]

        # Parse the KLASSE property
        klasse_id = sub_content[0] # KLASSE (Class is an enum represented by a 1 byte integer)
        # Remove used data from next entries
        sub_content = sub_content[1:]

        return cls(reg_nr=reg_nr,
                   katalog_nummer=katalog_nummer,
                   navn=navn,
                   grad_id=grad_id,
                   plass=plass,
                   l_id=l_id,
                   aar=aar,
                   plassering=plassering,
                   klasse_id=klasse_id)

    @property
    def reg_nr(self) -> str:
        return self._reg_nr

    @property
    def katalog_nummer(self) -> str:
        return self._katalog_nummer

    @property
    def navn(self) -> str:
        return self._navn

    @property
    def grad_id(self) -> int:
        return self._grad_id

    @property
    def plass(self) -> int:
        return self._plass

    @property
    def l_id(self) -> int:
        return self._l_id

    @property
    def aar(self) -> Union[str, None]:
        return None if not self._aar else self._aar

    @property
    def plassering(self) -> Union[str, None]:
        return None if not self._plassering else self._plassering

    @property
    def klasse_id(self) -> int:
        return self._klasse_id

    @property
    def native(self) -> dict:
        """Method converts class instance to native python classes for serialization purposes"""

        obj_dict = {
            'reg_nr': self.reg_nr,
            'katalog_nummer': self.katalog_nummer,
            'navn': self.navn,
            'grad_id': self.grad_id,
            'plass': self.plass,
            'l_id': self.l_id,
            'aar': self.aar,
            'plassering': self.plassering,
            'klasse_id': self.klasse_id,
        }

        return obj_dict

class SiegervinnerList:

    _contents: List[Siegervinner]

    def __init__(self, contents:List[Siegervinner]=[]) -> None:
        self._contents = contents
    
    @property
    def native(self) -> dict:
        """Method converts class instance to native python classes for serialization purposes"""

        return [i.native for i in self._contents]
