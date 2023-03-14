import struct
from typing import List, Union
from datetime import date

from ...utils import graceful_conversion, date_conversion, extract_decimal

class UtStStatTotal:
    _reg_nr: str # Registration number (REG.NR in original schema)
    _farens_reg_nr: str # Fathers registration number (FARENS_REG.NR in original schema)
    _morfars_reg_nr: str # Grandfathers registration number (MORFARS_REG.NR in original schema)
    _fodt: Union[date, None] # Birthdate (FØDT in original schema)
    _fodt_raw: Union[str, None] # Birthdate raw value (FØDT in original schema)
    _kjonn_id: int # Sex of dog (KJØNN in original schema)
    _oppdateringsdato: Union[date, None] # Update date (OPPDATERINGSDATO in original schema)
    _oppdateringsdato_raw: Union[str, None] # Update date raw value (OPPDATERINGSDATO in original schema)
    _totantavkom: Union[int, None] # Number of children (TOTANTAVKOM in original schema)
    _antkull: Union[int, None] # Number of litters (ANTKULL in original schema)
    _antavkutstbar: Union[int, None] # Number of children displayable (ANTAVKUTSTBAR in original schema)
    _antavkutstbarpros: Union[int, None] # Percentage of children diplayable (ANTAVKUTSTBARPROS in original schema)
    _antkullutstbar: Union[int, None] # Number of litters displayable (ANTKULLUTSTBAR in original schema)
    _antutstilt: Union[int, None] # Number displayed (ANTUTSTILT in original schema)
    _antutstiltpros: Union[int, None] # Percentage diplayed (ANTUTSTILTPROS in original schema)
    _antgangutstilt: Union[int, None] # Number of times displayed (ANTGANGUTSTILT in original schema)
    _1premieant: Union[int, None] # First prize number (1PREMIEANT in original schema)
    _1premiepros: Union[int, None] # First prize percentage (1PREMIEPROS in original schema)
    _2premieant: Union[int, None] # Second prize number (2PREMIEANT in original schema)
    _2premiepros: Union[int, None] # Second prize percentage (2PREMIEPROS in original schema)
    _3premieant: Union[int, None] # Third prize number (3PREMIEANT in original schema)
    _3premiepros: Union[int, None] # Third prize percentage (3PREMIEPROS in original schema)
    _kibant: Union[int, None] # KIB (KIBANT in original schema)
    _kibpros: Union[int, None] # KIB (KIBPROS in original schema)
    _hpant: Union[int, None] # HP (HPANT in original schema)
    _hppros: Union[int, None] # HP (HPPROS in original schema)
    _ckant: Union[int, None] # CK (CKANT in original schema)
    _ckpros: Union[int, None] # CK (CKPROS in original schema)
    _certant: Union[int, None] # CK (CERTANT in original schema)
    _certpros: Union[int, None] # CK (CERTPROS in original schema)

    def __init__(self, reg_nr: str, farens_reg_nr: str, morfars_reg_nr: str
               , fodt: Union[date, None], fodt_raw: Union[str, None], kjonn_id: int, oppdateringsdato: Union[date, None], oppdateringsdato_raw: Union[str, None]
               , totantavkom: Union[int, None], antkull: Union[int, None], antavkutstbar: Union[int, None]
               , antavkutstbarpros: Union[int, None], antkullutstbar: Union[int, None], antutstilt: Union[int, None]
               , antutstiltpros: Union[int, None], antgangutstilt: Union[int, None], n1premieant: Union[int, None]
               , n1premiepros: Union[int, None], n2premieant: Union[int, None], n2premiepros: Union[int, None]
               , n3premieant: Union[int, None], n3premiepros: Union[int, None], kibant: Union[int, None]
               , kibpros: Union[int, None], hpant: Union[int, None], hppros: Union[int, None]
               , ckant: Union[int, None], ckpros: Union[int, None], certant: Union[int, None]
               , certpros: Union[int, None]) -> None:
        self._reg_nr = reg_nr
        self._farens_reg_nr = farens_reg_nr
        self._morfars_reg_nr = morfars_reg_nr
        self._fodt = fodt
        self._fodt_raw = fodt_raw
        self._kjonn_id = kjonn_id
        self._oppdateringsdato = oppdateringsdato
        self._oppdateringsdato_raw = oppdateringsdato_raw
        self._totantavkom = totantavkom
        self._antkull = antkull
        self._antavkutstbar = antavkutstbar
        self._antavkutstbarpros = antavkutstbarpros
        self._antkullutstbar = antkullutstbar
        self._antutstilt = antutstilt
        self._antutstiltpros = antutstiltpros
        self._antgangutstilt = antgangutstilt
        self._1premieant = n1premieant
        self._1premiepros = n1premiepros
        self._2premieant = n2premieant
        self._2premiepros = n2premiepros
        self._3premieant = n3premieant
        self._3premiepros = n3premiepros
        self._kibant = kibant
        self._kibpros = kibpros
        self._hpant = hpant
        self._hppros = hppros
        self._ckant = ckant
        self._ckpros = ckpros
        self._certant = certant
        self._certpros = certpros

    @classmethod
    def from_bytes(cls, content: bytes):
        if len(content) != 97:
            raise AssertionError("Input for UtStStatTotal should be 97 bytes")

        # The Total Awards Statistics table contains a 6 byte header that does not contain useful data
        # Remove used data from next entries
        sub_content = content[6:]

        # Parse the REG.NR property
        reg_nr = graceful_conversion(sub_content[:12]) # REG.NR (Registration number is a string capped at 12 characters)
        # Remove used data from next entries
        sub_content = sub_content[12:]

        # Parse the FARENS_REG.NR property
        farens_reg_nr = graceful_conversion(sub_content[:12]) # FARENS_REG.NR (Fathers registration number is a string capped at 12 characters)
        # Remove used data from next entries
        sub_content = sub_content[12:]

        # Parse the MORFARS_REG.NR property
        morfars_reg_nr = graceful_conversion(sub_content[:12]) # MORFARS_REG.NR (Grandfathers registration number is a string capped at 12 characters)
        # Remove used data from next entries
        sub_content = sub_content[12:]

        # Parse the FØDT property
        fodt = None
        fodt_raw = graceful_conversion(sub_content[:6])
        try:
            fodt = date_conversion(sub_content[:6]) # FØDT (Birthdate is represented by a 6 digit numerical string)
        except ValueError as e:
            print(e)        # Remove used data from next entries
        sub_content = sub_content[6:]

        # Parse the KJØNN property
        kjonn_id = sub_content[0] # KJØNN (Sex of dog is an enum represented by a 1 byte integer)
        # Remove used data from next entries
        sub_content = sub_content[1:]

        # Parse the OPPDATERINGSDATO property
        oppdateringsdato = None
        oppdateringsdato_raw = graceful_conversion(sub_content[:6])
        try:
            oppdateringsdato = date_conversion(sub_content[:6]) # OPPDATERINGSDATO (Update date is represented by a 6 digit numerical string)
        except ValueError as e:
            print(e)        # Remove used data from next entries
        sub_content = sub_content[6:]

        # Parse the TOTANTAVKOM property
        totantavkom = struct.unpack('H', sub_content[:2])[0] # TOTANTAVKOM (Number of children is a 2 byte integer)
        totantavkom = None if totantavkom == 32768 else totantavkom # Set to python None if value indicates null
        # Remove used data from next entries
        sub_content = sub_content[2:]

        # Parse the ANTKULL property
        antkull = sub_content[0] # ANTKULL (Number of litters is a 1 byte integer)
        antkull = None if antkull == 128 else antkull # Set to python None if value indicates null
        # Remove used data from next entries
        sub_content = sub_content[1:]

        # Parse the ANTAVKUTSTBAR property
        antavkutstbar = struct.unpack('H', sub_content[:2])[0] # ANTAVKUTSTBAR (Number of children displayable is a 2 byte integer)
        antavkutstbar = None if antavkutstbar == 32768 else antavkutstbar # Set to python None if value indicates null
        # Remove used data from next entries
        sub_content = sub_content[2:]

        # Parse the ANTAVKUTSTBARPROS property
        antavkutstbarpros = struct.unpack('H', sub_content[:2])[0] # ANTAVKUTSTBARPROS (Percentage of children diplayable is a 2 byte integer)
        antavkutstbarpros = None if antavkutstbarpros == 32768 else antavkutstbarpros # Set to python None if value indicates null
        # Remove used data from next entries
        sub_content = sub_content[2:]

        # Parse the ANTKULLUTSTBAR property
        antkullutstbar = sub_content[0] # ANTKULLUTSTBAR (Number of litters displayable is a 1 byte integer)
        antkullutstbar = None if antkullutstbar == 128 else antkullutstbar # Set to python None if value indicates null
        # Remove used data from next entries
        sub_content = sub_content[1:]

        # Parse the ANTUTSTILT property
        antutstilt = struct.unpack('H', sub_content[:2])[0] # ANTUTSTILT (Number displayed is a 2 byte integer)
        antutstilt = None if antutstilt == 32768 else antutstilt # Set to python None if value indicates null
        # Remove used data from next entries
        sub_content = sub_content[2:]

        # Parse the ANTUTSTILTPROS property
        antutstiltpros = struct.unpack('H', sub_content[:2])[0] # ANTUTSTILTPROS (Percentage diplayed is a 2 byte integer)
        antutstiltpros = None if antutstiltpros == 32768 else antutstiltpros # Set to python None if value indicates null
        # Remove used data from next entries
        sub_content = sub_content[2:]

        # Parse the ANTGANGUTSTILT property
        antgangutstilt = struct.unpack('H', sub_content[:2])[0] # ANTGANGUTSTILT (Number of times displayed is a 2 byte integer)
        antgangutstilt = None if antgangutstilt == 32768 else antgangutstilt # Set to python None if value indicates null
        # Remove used data from next entries
        sub_content = sub_content[2:]

        # Parse the 1PREMIEANT property
        n1premieant = struct.unpack('H', sub_content[:2])[0] # 1PREMIEANT (First prize number is a 2 byte integer)
        n1premieant = None if n1premieant == 32768 else n1premieant # Set to python None if value indicates null
        # Remove used data from next entries
        sub_content = sub_content[2:]

        # Parse the 1PREMIEPROS property
        n1premiepros = struct.unpack('H', sub_content[:2])[0] # 1PREMIEPROS (First prize percentage is a 2 byte integer)
        n1premiepros = None if n1premiepros == 32768 else n1premiepros # Set to python None if value indicates null
        # Remove used data from next entries
        sub_content = sub_content[2:]

        # Parse the 2PREMIEANT property
        n2premieant = struct.unpack('H', sub_content[:2])[0] # 2PREMIEANT (Second prize number is a 2 byte integer)
        n2premieant = None if n2premieant == 32768 else n2premieant # Set to python None if value indicates null
        # Remove used data from next entries
        sub_content = sub_content[2:]

        # Parse the 2PREMIEPROS property
        n2premiepros = struct.unpack('H', sub_content[:2])[0] # 2PREMIEPROS (Second prize percentage is a 2 byte integer)
        n2premiepros = None if n2premiepros == 32768 else n2premiepros # Set to python None if value indicates null
        # Remove used data from next entries
        sub_content = sub_content[2:]

        # Parse the 3PREMIEANT property
        n3premieant = struct.unpack('H', sub_content[:2])[0] # 3PREMIEANT (Third prize number is a 2 byte integer)
        n3premieant = None if n3premieant == 32768 else n3premieant # Set to python None if value indicates null
        # Remove used data from next entries
        sub_content = sub_content[2:]

        # Parse the 3PREMIEPROS property
        n3premiepros = struct.unpack('H', sub_content[:2])[0] # 3PREMIEPROS (Third prize percentage is a 2 byte integer)
        n3premiepros = None if n3premiepros == 32768 else n3premiepros # Set to python None if value indicates null
        # Remove used data from next entries
        sub_content = sub_content[2:]

        # Parse the KIBANT property
        kibant = struct.unpack('H', sub_content[:2])[0] # KIBANT (KIB is a 2 byte integer)
        kibant = None if kibant == 32768 else kibant # Set to python None if value indicates null
        # Remove used data from next entries
        sub_content = sub_content[2:]

        # Parse the KIBPROS property
        kibpros = struct.unpack('H', sub_content[:2])[0] # KIBPROS (KIB is a 2 byte integer)
        kibpros = None if kibpros == 32768 else kibpros # Set to python None if value indicates null
        # Remove used data from next entries
        sub_content = sub_content[2:]

        # Parse the HPANT property
        hpant = struct.unpack('H', sub_content[:2])[0] # HPANT (HP is a 2 byte integer)
        hpant = None if hpant == 32768 else hpant # Set to python None if value indicates null
        # Remove used data from next entries
        sub_content = sub_content[2:]

        # Parse the HPPROS property
        hppros = struct.unpack('H', sub_content[:2])[0] # HPPROS (HP is a 2 byte integer)
        hppros = None if hppros == 32768 else hppros # Set to python None if value indicates null
        # Remove used data from next entries
        sub_content = sub_content[2:]

        # Parse the CKANT property
        ckant = struct.unpack('H', sub_content[:2])[0] # CKANT (CK is a 2 byte integer)
        ckant = None if ckant == 32768 else ckant # Set to python None if value indicates null
        # Remove used data from next entries
        sub_content = sub_content[2:]

        # Parse the CKPROS property
        ckpros = struct.unpack('H', sub_content[:2])[0] # CKPROS (CK is a 2 byte integer)
        ckpros = None if ckpros == 32768 else ckpros # Set to python None if value indicates null
        # Remove used data from next entries
        sub_content = sub_content[2:]

        # Parse the CERTANT property
        certant = struct.unpack('H', sub_content[:2])[0] # CERTANT (CK is a 2 byte integer)
        certant = None if certant == 32768 else certant # Set to python None if value indicates null
        # Remove used data from next entries
        sub_content = sub_content[2:]

        # Parse the CERTPROS property
        certpros = struct.unpack('H', sub_content[:2])[0] # CERTPROS (CK is a 2 byte integer)
        certpros = None if certpros == 32768 else certpros # Set to python None if value indicates null
        # Remove used data from next entries
        sub_content = sub_content[2:]

        return cls(reg_nr=reg_nr,
                   farens_reg_nr=farens_reg_nr,
                   morfars_reg_nr=morfars_reg_nr,
                   fodt=fodt,
                   fodt_raw=fodt_raw,
                   kjonn_id=kjonn_id,
                   oppdateringsdato=oppdateringsdato,
                   oppdateringsdato_raw=oppdateringsdato_raw,
                   totantavkom=totantavkom,
                   antkull=antkull,
                   antavkutstbar=antavkutstbar,
                   antavkutstbarpros=antavkutstbarpros,
                   antkullutstbar=antkullutstbar,
                   antutstilt=antutstilt,
                   antutstiltpros=antutstiltpros,
                   antgangutstilt=antgangutstilt,
                   n1premieant=n1premieant,
                   n1premiepros=n1premiepros,
                   n2premieant=n2premieant,
                   n2premiepros=n2premiepros,
                   n3premieant=n3premieant,
                   n3premiepros=n3premiepros,
                   kibant=kibant,
                   kibpros=kibpros,
                   hpant=hpant,
                   hppros=hppros,
                   ckant=ckant,
                   ckpros=ckpros,
                   certant=certant,
                   certpros=certpros)

    @property
    def reg_nr(self) -> str:
        return self._reg_nr

    @property
    def farens_reg_nr(self) -> str:
        return self._farens_reg_nr

    @property
    def morfars_reg_nr(self) -> str:
        return self._morfars_reg_nr

    @property
    def fodt(self) -> Union[date, None]:
        return None if not self._fodt else self._fodt

    @property
    def fodt_str(self) -> Union[str, None]:
        return None if not self.fodt else self.fodt.isoformat()

    @property
    def fodt_raw(self) -> Union[str, None]:
        return None if not self._fodt_raw else self._fodt_raw

    @property
    def kjonn_id(self) -> int:
        return self._kjonn_id

    @property
    def oppdateringsdato(self) -> Union[date, None]:
        return None if not self._oppdateringsdato else self._oppdateringsdato

    @property
    def oppdateringsdato_str(self) -> Union[str, None]:
        return None if not self.oppdateringsdato else self.oppdateringsdato.isoformat()

    @property
    def oppdateringsdato_raw(self) -> Union[str, None]:
        return None if not self._oppdateringsdato_raw else self._oppdateringsdato_raw

    @property
    def totantavkom(self) -> Union[int, None]:
        return None if not self._totantavkom else self._totantavkom

    @property
    def antkull(self) -> Union[int, None]:
        return None if not self._antkull else self._antkull

    @property
    def antavkutstbar(self) -> Union[int, None]:
        return None if not self._antavkutstbar else self._antavkutstbar

    @property
    def antavkutstbarpros(self) -> Union[int, None]:
        return None if not self._antavkutstbarpros else self._antavkutstbarpros

    @property
    def antkullutstbar(self) -> Union[int, None]:
        return None if not self._antkullutstbar else self._antkullutstbar

    @property
    def antutstilt(self) -> Union[int, None]:
        return None if not self._antutstilt else self._antutstilt

    @property
    def antutstiltpros(self) -> Union[int, None]:
        return None if not self._antutstiltpros else self._antutstiltpros

    @property
    def antgangutstilt(self) -> Union[int, None]:
        return None if not self._antgangutstilt else self._antgangutstilt

    @property
    def n1premieant(self) -> Union[int, None]:
        return None if not self._1premieant else self._1premieant

    @property
    def n1premiepros(self) -> Union[int, None]:
        return None if not self._1premiepros else self._1premiepros

    @property
    def n2premieant(self) -> Union[int, None]:
        return None if not self._2premieant else self._2premieant

    @property
    def n2premiepros(self) -> Union[int, None]:
        return None if not self._2premiepros else self._2premiepros

    @property
    def n3premieant(self) -> Union[int, None]:
        return None if not self._3premieant else self._3premieant

    @property
    def n3premiepros(self) -> Union[int, None]:
        return None if not self._3premiepros else self._3premiepros

    @property
    def kibant(self) -> Union[int, None]:
        return None if not self._kibant else self._kibant

    @property
    def kibpros(self) -> Union[int, None]:
        return None if not self._kibpros else self._kibpros

    @property
    def hpant(self) -> Union[int, None]:
        return None if not self._hpant else self._hpant

    @property
    def hppros(self) -> Union[int, None]:
        return None if not self._hppros else self._hppros

    @property
    def ckant(self) -> Union[int, None]:
        return None if not self._ckant else self._ckant

    @property
    def ckpros(self) -> Union[int, None]:
        return None if not self._ckpros else self._ckpros

    @property
    def certant(self) -> Union[int, None]:
        return None if not self._certant else self._certant

    @property
    def certpros(self) -> Union[int, None]:
        return None if not self._certpros else self._certpros

    @property
    def native(self) -> dict:
        """Method converts class instance to native python classes for serialization purposes"""

        obj_dict = {
            'reg_nr': self.reg_nr,
            'farens_reg_nr': self.farens_reg_nr,
            'morfars_reg_nr': self.morfars_reg_nr,
            'fodt': self.fodt_str,
            'fodt_raw': self.fodt_raw,
            'kjonn_id': self.kjonn_id,
            'oppdateringsdato': self.oppdateringsdato_str,
            'oppdateringsdato_raw': self.oppdateringsdato_raw,
            'totantavkom': self.totantavkom,
            'antkull': self.antkull,
            'antavkutstbar': self.antavkutstbar,
            'antavkutstbarpros': self.antavkutstbarpros,
            'antkullutstbar': self.antkullutstbar,
            'antutstilt': self.antutstilt,
            'antutstiltpros': self.antutstiltpros,
            'antgangutstilt': self.antgangutstilt,
            '1premieant': self.n1premieant,
            '1premiepros': self.n1premiepros,
            '2premieant': self.n2premieant,
            '2premiepros': self.n2premiepros,
            '3premieant': self.n3premieant,
            '3premiepros': self.n3premiepros,
            'kibant': self.kibant,
            'kibpros': self.kibpros,
            'hpant': self.hpant,
            'hppros': self.hppros,
            'ckant': self.ckant,
            'ckpros': self.ckpros,
            'certant': self.certant,
            'certpros': self.certpros,
        }

        return obj_dict

class UtStStatTotalList:

    _contents: List[UtStStatTotal]

    def __init__(self, contents:List[UtStStatTotal]=[]) -> None:
        self._contents = contents
    
    @property
    def native(self) -> dict:
        """Method converts class instance to native python classes for serialization purposes"""

        return [i.native for i in self._contents]
