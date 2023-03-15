import struct
from typing import List, Union
from datetime import date

from ...utils import graceful_conversion, date_conversion, extract_decimal

class HdStatFarMorFar:
    _reg_nr: str # Registration number (REG.NR in original schema)
    _navn: str # Name (NAVN in original schema)
    _reg_nrmf: str # Grandfathers registration number (REG.NRMF in original schema)
    _morfar: str # Grandfather (MORFAR in original schema)
    _antkull: Union[int, None] # Number of litters (ANTKULL in original schema)
    _sistedato: Union[date, None] # Last child date (SISTEDATO in original schema)
    _sistedato_raw: Union[str, None] # Last child date raw value (SISTEDATO in original schema)
    _ant: Union[int, None] # Number of children (ANT in original schema)
    _ro: Union[int, None] # RØ (RØ in original schema)
    _fri: Union[int, None] # FRI? (FRI in original schema)
    _morant: Union[int, None] # MORANT? (MORANT in original schema)
    _svak: Union[int, None] # SVAK? (SVAK in original schema)
    _morro: Union[int, None] # MORRØ (MORRØ in original schema)
    _midd: Union[int, None] # MIDD? (MIDD in original schema)
    _morfri: Union[int, None] # MORFRI? (MORFRI in original schema)
    _sterk: Union[int, None] # STERK (STERK in original schema)
    _morc: Union[int, None] # MORD? (MORC in original schema)
    _mord: Union[int, None] # MORD? (MORD in original schema)
    _hd: Union[int, None] # HD? (HD in original schema)
    _more: Union[int, None] # MORD? (MORE in original schema)

    def __init__(self, reg_nr: str, navn: str, reg_nrmf: str
               , morfar: str, antkull: Union[int, None], sistedato: Union[date, None], sistedato_raw: Union[str, None]
               , ant: Union[int, None], ro: Union[int, None], fri: Union[int, None]
               , morant: Union[int, None], svak: Union[int, None], morro: Union[int, None]
               , midd: Union[int, None], morfri: Union[int, None], sterk: Union[int, None]
               , morc: Union[int, None], mord: Union[int, None], hd: Union[int, None]
               , more: Union[int, None]) -> None:
        self._reg_nr = reg_nr
        self._navn = navn
        self._reg_nrmf = reg_nrmf
        self._morfar = morfar
        self._antkull = antkull
        self._sistedato = sistedato
        self._sistedato_raw = sistedato_raw
        self._ant = ant
        self._ro = ro
        self._fri = fri
        self._morant = morant
        self._svak = svak
        self._morro = morro
        self._midd = midd
        self._morfri = morfri
        self._sterk = sterk
        self._morc = morc
        self._mord = mord
        self._hd = hd
        self._more = more

    @classmethod
    def from_bytes(cls, content: bytes):
        if len(content) != 137:
            raise AssertionError("Input for HdStatFarMorFar should be 137 bytes")

        # The Hd statistics table contains a 6 byte header that does not contain useful data
        # Remove used data from next entries
        sub_content = content[6:]

        # Parse the REG.NR property
        reg_nr = graceful_conversion(sub_content[:12]) # REG.NR (Registration number is a string capped at 12 characters)
        # Remove used data from next entries
        sub_content = sub_content[12:]

        # Parse the NAVN property
        navn = graceful_conversion(sub_content[:38]) # NAVN (Name is a string capped at 38 characters)
        # Remove used data from next entries
        sub_content = sub_content[38:]

        # Parse the REG.NRMF property
        reg_nrmf = graceful_conversion(sub_content[:12]) # REG.NRMF (Grandfathers registration number is a string capped at 12 characters)
        # Remove used data from next entries
        sub_content = sub_content[12:]

        # Parse the MORFAR property
        morfar = graceful_conversion(sub_content[:38]) # MORFAR (Grandfather is a string capped at 38 characters)
        # Remove used data from next entries
        sub_content = sub_content[38:]

        # Parse the ANTKULL property
        antkull = struct.unpack('H', sub_content[:2])[0] # ANTKULL (Number of litters is a 2 byte integer)
        antkull = None if antkull == 32768 else antkull # Set to python None if value indicates null
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

        # Parse the ANT property
        ant = struct.unpack('H', sub_content[:2])[0] # ANT (Number of children is a 2 byte integer)
        ant = None if ant == 32768 else ant # Set to python None if value indicates null
        # Remove used data from next entries
        sub_content = sub_content[2:]

        # Parse the RØ property
        ro = struct.unpack('H', sub_content[:2])[0] # RØ (RØ is a 2 byte integer)
        ro = None if ro == 32768 else ro # Set to python None if value indicates null
        # Remove used data from next entries
        sub_content = sub_content[2:]

        # Parse the FRI property
        fri = struct.unpack('H', sub_content[:2])[0] # FRI (FRI? is a 2 byte integer)
        fri = None if fri == 32768 else fri # Set to python None if value indicates null
        # Remove used data from next entries
        sub_content = sub_content[2:]

        # Parse the MORANT property
        morant = struct.unpack('H', sub_content[:2])[0] # MORANT (MORANT? is a 2 byte integer)
        morant = None if morant == 32768 else morant # Set to python None if value indicates null
        # Remove used data from next entries
        sub_content = sub_content[2:]

        # Parse the SVAK property
        svak = struct.unpack('H', sub_content[:2])[0] # SVAK (SVAK? is a 2 byte integer)
        svak = None if svak == 32768 else svak # Set to python None if value indicates null
        # Remove used data from next entries
        sub_content = sub_content[2:]

        # Parse the MORRØ property
        morro = struct.unpack('H', sub_content[:2])[0] # MORRØ (MORRØ is a 2 byte integer)
        morro = None if morro == 32768 else morro # Set to python None if value indicates null
        # Remove used data from next entries
        sub_content = sub_content[2:]

        # Parse the MIDD property
        midd = struct.unpack('H', sub_content[:2])[0] # MIDD (MIDD? is a 2 byte integer)
        midd = None if midd == 32768 else midd # Set to python None if value indicates null
        # Remove used data from next entries
        sub_content = sub_content[2:]

        # Parse the MORFRI property
        morfri = struct.unpack('H', sub_content[:2])[0] # MORFRI (MORFRI? is a 2 byte integer)
        morfri = None if morfri == 32768 else morfri # Set to python None if value indicates null
        # Remove used data from next entries
        sub_content = sub_content[2:]

        # Parse the STERK property
        sterk = struct.unpack('H', sub_content[:2])[0] # STERK (STERK is a 2 byte integer)
        sterk = None if sterk == 32768 else sterk # Set to python None if value indicates null
        # Remove used data from next entries
        sub_content = sub_content[2:]

        # Parse the MORC property
        morc = sub_content[0] # MORC (MORD? is a 1 byte integer)
        morc = None if morc == 128 else morc # Set to python None if value indicates null
        # Remove used data from next entries
        sub_content = sub_content[1:]

        # Parse the MORD property
        mord = sub_content[0] # MORD (MORD? is a 1 byte integer)
        mord = None if mord == 128 else mord # Set to python None if value indicates null
        # Remove used data from next entries
        sub_content = sub_content[1:]

        # Parse the HD property
        hd = struct.unpack('H', sub_content[:2])[0] # HD (HD? is a 2 byte integer)
        hd = None if hd == 32768 else hd # Set to python None if value indicates null
        # Remove used data from next entries
        sub_content = sub_content[2:]

        # Parse the MORE property
        more = sub_content[0] # MORE (MORD? is a 1 byte integer)
        more = None if more == 128 else more # Set to python None if value indicates null
        # Remove used data from next entries
        sub_content = sub_content[1:]

        return cls(reg_nr=reg_nr,
                   navn=navn,
                   reg_nrmf=reg_nrmf,
                   morfar=morfar,
                   antkull=antkull,
                   sistedato=sistedato,
                   sistedato_raw=sistedato_raw,
                   ant=ant,
                   ro=ro,
                   fri=fri,
                   morant=morant,
                   svak=svak,
                   morro=morro,
                   midd=midd,
                   morfri=morfri,
                   sterk=sterk,
                   morc=morc,
                   mord=mord,
                   hd=hd,
                   more=more)

    @property
    def reg_nr(self) -> str:
        return self._reg_nr

    @property
    def navn(self) -> str:
        return self._navn

    @property
    def reg_nrmf(self) -> str:
        return self._reg_nrmf

    @property
    def morfar(self) -> str:
        return self._morfar

    @property
    def antkull(self) -> Union[int, None]:
        return self._antkull

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
    def ant(self) -> Union[int, None]:
        return self._ant

    @property
    def ro(self) -> Union[int, None]:
        return self._ro

    @property
    def fri(self) -> Union[int, None]:
        return self._fri

    @property
    def morant(self) -> Union[int, None]:
        return self._morant

    @property
    def svak(self) -> Union[int, None]:
        return self._svak

    @property
    def morro(self) -> Union[int, None]:
        return self._morro

    @property
    def midd(self) -> Union[int, None]:
        return self._midd

    @property
    def morfri(self) -> Union[int, None]:
        return self._morfri

    @property
    def sterk(self) -> Union[int, None]:
        return self._sterk

    @property
    def morc(self) -> Union[int, None]:
        return self._morc

    @property
    def mord(self) -> Union[int, None]:
        return self._mord

    @property
    def hd(self) -> Union[int, None]:
        return self._hd

    @property
    def more(self) -> Union[int, None]:
        return self._more

    @property
    def native(self) -> dict:
        """Method converts class instance to native python classes for serialization purposes"""

        obj_dict = {
            'reg_nr': self.reg_nr,
            'navn': self.navn,
            'reg_nrmf': self.reg_nrmf,
            'morfar': self.morfar,
            'antkull': self.antkull,
            'sistedato': self.sistedato_str,
            'sistedato_raw': self.sistedato_raw,
            'ant': self.ant,
            'ro': self.ro,
            'fri': self.fri,
            'morant': self.morant,
            'svak': self.svak,
            'morro': self.morro,
            'midd': self.midd,
            'morfri': self.morfri,
            'sterk': self.sterk,
            'morc': self.morc,
            'mord': self.mord,
            'hd': self.hd,
            'more': self.more,
        }

        return obj_dict

class HdStatFarMorFarList:

    _contents: List[HdStatFarMorFar]

    def __init__(self, contents:List[HdStatFarMorFar]=[]) -> None:
        self._contents = contents
    
    @property
    def native(self) -> dict:
        """Method converts class instance to native python classes for serialization purposes"""

        return [i.native for i in self._contents]
