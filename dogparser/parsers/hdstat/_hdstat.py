import struct
from typing import List, Union
from datetime import date

from ...utils import graceful_conversion, date_conversion

class HDStat:
    _reg_nr: str # Registration number (REG.NR in original schema)
    _fodselsaar: Union[int, None] # Birth year (FØDSELSÅR in original schema)
    _navn: Union[str, None] # Name (NAVN in original schema)
    _kjonn_id: int # Sex of dog (KJØNN in original schema)
    _antkull: Union[int, None] # Number of litters (ANTKULL in original schema)
    _ant: Union[int, None] # Number of children (ANT in original schema)
    _ro: int # RØ (RØ in original schema)
    _sistedato: Union[date, None] # Last child date (SISTEDATO in original schema)
    _sistedato_raw: Union[str, None] # Last child date raw value (SISTEDATO in original schema)
    _fri: Union[int, None] # FRI? (FRI in original schema)
    _svak: Union[int, None] # SVAK? (SVAK in original schema)
    _midd: Union[int, None] # MIDD? (MIDD in original schema)
    _sterk: Union[int, None] # STERK (STERK in original schema)
    _hd: Union[int, None] # HD? (HD in original schema)

    def __init__(self, reg_nr: str, fodselsaar: Union[int, None], navn: Union[str, None]
               , kjonn_id: int, antkull: Union[int, None], ant: Union[int, None]
               , ro: int, sistedato: Union[date, None], sistedato_raw: Union[str, None], fri: Union[int, None]
               , svak: Union[int, None], midd: Union[int, None], sterk: Union[int, None]
               , hd: Union[int, None]) -> None:
        self._reg_nr = reg_nr
        self._fodselsaar = fodselsaar
        self._navn = navn
        self._kjonn_id = kjonn_id
        self._antkull = antkull
        self._ant = ant
        self._ro = ro
        self._sistedato = sistedato
        self._sistedato_raw = sistedato_raw
        self._fri = fri
        self._svak = svak
        self._midd = midd
        self._sterk = sterk
        self._hd = hd

    @classmethod
    def from_bytes(cls, content: bytes):
        if len(content) != 79:
            raise AssertionError("Input for HDStat should be 79 bytes")

        # The HD Statistics table contains a 5 byte header that does not contain useful data
        # Remove used data from next entries
        sub_content = content[5:]

        # Parse the REG.NR property
        reg_nr = graceful_conversion(sub_content[:12]) # REG.NR (Registration number is a string capped at 12 characters)
        # Remove used data from next entries
        sub_content = sub_content[12:]

        # Parse the FØDSELSÅR property
        fodselsaar = sub_content[0] # FØDSELSÅR (Birth year is a 1 byte integer)
        fodselsaar = None if fodselsaar == 128 else fodselsaar # Set to python None if value indicates null
        # Remove used data from next entries
        sub_content = sub_content[1:]

        # Parse the NAVN property
        navn = graceful_conversion(sub_content[:38]) # NAVN (Name is a string capped at 38 characters)
        # Remove used data from next entries
        sub_content = sub_content[38:]

        # Parse the KJØNN property
        kjonn_id = sub_content[0] # KJØNN (Sex of dog is an enum represented by a 1 byte integer)
        # Remove used data from next entries
        sub_content = sub_content[1:]

        # Parse the ANTKULL property
        antkull = struct.unpack('H', sub_content[:2])[0] # ANTKULL (Number of litters is a 2 byte integer)
        antkull = None if antkull == 32768 else antkull # Set to python None if value indicates null
        # Remove used data from next entries
        sub_content = sub_content[2:]

        # Parse the ANT property
        ant = struct.unpack('H', sub_content[:2])[0] # ANT (Number of children is a 2 byte integer)
        ant = None if ant == 32768 else ant # Set to python None if value indicates null
        # Remove used data from next entries
        sub_content = sub_content[2:]

        # Parse the RØ property
        ro = struct.unpack('H', sub_content[:2])[0] # RØ (RØ is a 2 byte integer)
        # Remove used data from next entries
        sub_content = sub_content[2:]

        # Parse the SISTEDATO property
        sistedato = None
        sistedato_raw = graceful_conversion(sub_content[:6])
        try:
            sistedato = date_conversion(sub_content[:6]) # SISTEDATO (Last child date is represented by a 6 digit numerical string)
        except ValueError as e:
            print(e)        # Remove used data from next entries
        sub_content = sub_content[6:]

        # Parse the FRI property
        fri = struct.unpack('H', sub_content[:2])[0] # FRI (FRI? is a 2 byte integer)
        fri = None if fri == 32768 else fri # Set to python None if value indicates null
        # Remove used data from next entries
        sub_content = sub_content[2:]

        # Parse the SVAK property
        svak = struct.unpack('H', sub_content[:2])[0] # SVAK (SVAK? is a 2 byte integer)
        svak = None if svak == 32768 else svak # Set to python None if value indicates null
        # Remove used data from next entries
        sub_content = sub_content[2:]

        # Parse the MIDD property
        midd = struct.unpack('H', sub_content[:2])[0] # MIDD (MIDD? is a 2 byte integer)
        midd = None if midd == 32768 else midd # Set to python None if value indicates null
        # Remove used data from next entries
        sub_content = sub_content[2:]

        # Parse the STERK property
        sterk = struct.unpack('H', sub_content[:2])[0] # STERK (STERK is a 2 byte integer)
        sterk = None if sterk == 32768 else sterk # Set to python None if value indicates null
        # Remove used data from next entries
        sub_content = sub_content[2:]

        # Parse the HD property
        hd = struct.unpack('H', sub_content[:2])[0] # HD (HD? is a 2 byte integer)
        hd = None if hd == 32768 else hd # Set to python None if value indicates null
        # Remove used data from next entries
        sub_content = sub_content[2:]

        return cls(reg_nr=reg_nr,
                   fodselsaar=fodselsaar,
                   navn=navn,
                   kjonn_id=kjonn_id,
                   antkull=antkull,
                   ant=ant,
                   ro=ro,
                   sistedato=sistedato,
                   sistedato_raw=sistedato_raw,
                   fri=fri,
                   svak=svak,
                   midd=midd,
                   sterk=sterk,
                   hd=hd)

    @property
    def reg_nr(self) -> str:
        return self._reg_nr

    @property
    def fodselsaar(self) -> Union[int, None]:
        return None if not self._fodselsaar else self._fodselsaar

    @property
    def navn(self) -> Union[str, None]:
        return None if not self._navn else self._navn

    @property
    def kjonn_id(self) -> int:
        return self._kjonn_id

    @property
    def antkull(self) -> Union[int, None]:
        return None if not self._antkull else self._antkull

    @property
    def ant(self) -> Union[int, None]:
        return None if not self._ant else self._ant

    @property
    def ro(self) -> int:
        return self._ro

    @property
    def sistedato(self) -> Union[date, None]:
        return None if not self._sistedato else self._sistedato

    @property
    def sistedato_str(self) -> Union[str, None]:
        return None if not self.sistedato else self.sistedato.isoformat()

    @property
    def sistedato_raw(self) -> Union[str, None]:
        return None if not self._sistedato_raw else self._sistedato_raw

    @property
    def fri(self) -> Union[int, None]:
        return None if not self._fri else self._fri

    @property
    def svak(self) -> Union[int, None]:
        return None if not self._svak else self._svak

    @property
    def midd(self) -> Union[int, None]:
        return None if not self._midd else self._midd

    @property
    def sterk(self) -> Union[int, None]:
        return None if not self._sterk else self._sterk

    @property
    def hd(self) -> Union[int, None]:
        return None if not self._hd else self._hd

    @property
    def native(self) -> dict:
        """Method converts class instance to native python classes for serialization purposes"""

        obj_dict = {
            'reg_nr': self.reg_nr,
            'fodselsaar': self.fodselsaar,
            'navn': self.navn,
            'kjonn_id': self.kjonn_id,
            'antkull': self.antkull,
            'ant': self.ant,
            'ro': self.ro,
            'sistedato': self.sistedato_str,
            'sistedato_raw': self.sistedato_raw,
            'fri': self.fri,
            'svak': self.svak,
            'midd': self.midd,
            'sterk': self.sterk,
            'hd': self.hd,
        }

        return obj_dict

class HDStatList:

    _contents: List[HDStat]

    def __init__(self, contents:List[HDStat]=[]) -> None:
        self._contents = contents
    
    @property
    def native(self) -> dict:
        """Method converts class instance to native python classes for serialization purposes"""

        return [i.native for i in self._contents]
