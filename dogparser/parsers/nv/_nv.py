import struct
from typing import List, Union
from datetime import date

from ...utils import graceful_conversion, date_conversion, extract_decimal

class Nv:
    _aar: Union[str, None] # Year (ÅR in original schema)
    _reg_nr: str # Registration number (REG.NR in original schema)
    _katalog_nummer: str # Catalog number (KATALOG_NUMMER in original schema)
    _navn: Union[str, None] # Name (NAVN in original schema)
    _grad_id: int # Grade (GRAD in original schema)
    _plass: Union[int, None] # Place (PLASS in original schema)
    _plassering: Union[str, None] # Placement (PLASSERING in original schema)
    _l_id: int # Country code (L in original schema)
    _aaaar: Union[str, None] # Year (ÅÅR in original schema)
    _plass2: Union[str, None] # Place column 2 (PLASS2 in original schema)
    _klasse_id: int # Class (KLASSE in original schema)
    _far: str # Fathers name (FAR in original schema)
    _mor: str # Mothers name (MOR in original schema)
    _katnr: Union[int, None] # Category number (KATNR in original schema)
    _plassiffer: Union[str, None] # Placement number (PLASSIFFER in original schema)

    def __init__(self, aar: Union[str, None], reg_nr: str, katalog_nummer: str
               , navn: Union[str, None], grad_id: int, plass: Union[int, None]
               , plassering: Union[str, None], l_id: int, aaaar: Union[str, None]
               , plass2: Union[str, None], klasse_id: int, far: str
               , mor: str, katnr: Union[int, None], plassiffer: Union[str, None]) -> None:
        self._aar = aar
        self._reg_nr = reg_nr
        self._katalog_nummer = katalog_nummer
        self._navn = navn
        self._grad_id = grad_id
        self._plass = plass
        self._plassering = plassering
        self._l_id = l_id
        self._aaaar = aaaar
        self._plass2 = plass2
        self._klasse_id = klasse_id
        self._far = far
        self._mor = mor
        self._katnr = katnr
        self._plassiffer = plassiffer

    @classmethod
    def from_bytes(cls, content: bytes):
        if len(content) != 163:
            raise AssertionError("Input for Nv should be 163 bytes")

        # The Awards Statistics table contains a 7 byte header that does not contain useful data
        # Remove used data from next entries
        sub_content = content[7:]

        # Parse the ÅR property
        aar = graceful_conversion(sub_content[:4]) # ÅR (Year is a string capped at 4 characters)
        # Remove used data from next entries
        sub_content = sub_content[4:]

        # Parse the REG.NR property
        reg_nr = graceful_conversion(sub_content[:12]) # REG.NR (Registration number is a string capped at 12 characters)
        # Remove used data from next entries
        sub_content = sub_content[12:]

        # Parse the KATALOG_NUMMER property
        katalog_nummer = graceful_conversion(sub_content[:4]) # KATALOG_NUMMER (Catalog number is a string capped at 4 characters)
        # Remove used data from next entries
        sub_content = sub_content[4:]

        # Parse the NAVN property
        navn = graceful_conversion(sub_content[:36]) # NAVN (Name is a string capped at 36 characters)
        # Remove used data from next entries
        sub_content = sub_content[36:]

        # Parse the GRAD property
        grad_id = sub_content[0] # GRAD (Grade is an enum represented by a 1 byte integer)
        # Remove used data from next entries
        sub_content = sub_content[1:]

        # Parse the PLASS property
        plass = struct.unpack('H', sub_content[:2])[0] # PLASS (Place is a 2 byte integer)
        plass = None if plass == 32768 else plass # Set to python None if value indicates null
        # Remove used data from next entries
        sub_content = sub_content[2:]

        # Parse the PLASSERING property
        plassering = graceful_conversion(sub_content[:11]) # PLASSERING (Placement is a string capped at 11 characters)
        # Remove used data from next entries
        sub_content = sub_content[11:]

        # Parse the L property
        l_id = sub_content[0] # L (Country code is an enum represented by a 1 byte integer)
        # Remove used data from next entries
        sub_content = sub_content[1:]

        # Parse the ÅÅR property
        aaaar = graceful_conversion(sub_content[:4]) # ÅÅR (Year is a string capped at 4 characters)
        # Remove used data from next entries
        sub_content = sub_content[4:]

        # Parse the PLASS2 property
        plass2 = graceful_conversion(sub_content[:3]) # PLASS2 (Place column 2 is a string capped at 3 characters)
        # Remove used data from next entries
        sub_content = sub_content[3:]

        # Parse the KLASSE property
        klasse_id = sub_content[0] # KLASSE (Class is an enum represented by a 1 byte integer)
        # Remove used data from next entries
        sub_content = sub_content[1:]

        # Parse the FAR property
        far = graceful_conversion(sub_content[:36]) # FAR (Fathers name is a string capped at 36 characters)
        # Remove used data from next entries
        sub_content = sub_content[36:]

        # Parse the MOR property
        mor = graceful_conversion(sub_content[:36]) # MOR (Mothers name is a string capped at 36 characters)
        # Remove used data from next entries
        sub_content = sub_content[36:]

        # Parse the KATNR property
        katnr = struct.unpack('H', sub_content[:2])[0] # KATNR (Category number is a 2 byte integer)
        katnr = None if katnr == 32768 else katnr # Set to python None if value indicates null
        # Remove used data from next entries
        sub_content = sub_content[2:]

        # Parse the PLASSIFFER property
        plassiffer = graceful_conversion(sub_content[:3]) # PLASSIFFER (Placement number is a string capped at 3 characters)
        # Remove used data from next entries
        sub_content = sub_content[3:]

        return cls(aar=aar,
                   reg_nr=reg_nr,
                   katalog_nummer=katalog_nummer,
                   navn=navn,
                   grad_id=grad_id,
                   plass=plass,
                   plassering=plassering,
                   l_id=l_id,
                   aaaar=aaaar,
                   plass2=plass2,
                   klasse_id=klasse_id,
                   far=far,
                   mor=mor,
                   katnr=katnr,
                   plassiffer=plassiffer)

    @property
    def aar(self) -> Union[str, None]:
        return None if not self._aar else self._aar

    @property
    def reg_nr(self) -> str:
        return self._reg_nr

    @property
    def katalog_nummer(self) -> str:
        return self._katalog_nummer

    @property
    def navn(self) -> Union[str, None]:
        return None if not self._navn else self._navn

    @property
    def grad_id(self) -> int:
        return self._grad_id

    @property
    def plass(self) -> Union[int, None]:
        return None if not self._plass else self._plass

    @property
    def plassering(self) -> Union[str, None]:
        return None if not self._plassering else self._plassering

    @property
    def l_id(self) -> int:
        return self._l_id

    @property
    def aaaar(self) -> Union[str, None]:
        return None if not self._aaaar else self._aaaar

    @property
    def plass2(self) -> Union[str, None]:
        return None if not self._plass2 else self._plass2

    @property
    def klasse_id(self) -> int:
        return self._klasse_id

    @property
    def far(self) -> str:
        return self._far

    @property
    def mor(self) -> str:
        return self._mor

    @property
    def katnr(self) -> Union[int, None]:
        return None if not self._katnr else self._katnr

    @property
    def plassiffer(self) -> Union[str, None]:
        return None if not self._plassiffer else self._plassiffer

    @property
    def native(self) -> dict:
        """Method converts class instance to native python classes for serialization purposes"""

        obj_dict = {
            'aar': self.aar,
            'reg_nr': self.reg_nr,
            'katalog_nummer': self.katalog_nummer,
            'navn': self.navn,
            'grad_id': self.grad_id,
            'plass': self.plass,
            'plassering': self.plassering,
            'l_id': self.l_id,
            'aaaar': self.aaaar,
            'plass2': self.plass2,
            'klasse_id': self.klasse_id,
            'far': self.far,
            'mor': self.mor,
            'katnr': self.katnr,
            'plassiffer': self.plassiffer,
        }

        return obj_dict

class NvList:

    _contents: List[Nv]

    def __init__(self, contents:List[Nv]=[]) -> None:
        self._contents = contents
    
    @property
    def native(self) -> dict:
        """Method converts class instance to native python classes for serialization purposes"""

        return [i.native for i in self._contents]
