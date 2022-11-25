import struct

from typing import List, Union
from datetime import date

from ...utils import graceful_conversion, date_conversion

class Utstillingsamleres:
    _reg_nr: str # Registration number (REG.NR in original schema)
    _farens_reg_nr: Union[str, None] # Fathers registration number (FARENS REG.NR in original schema)
    _morfars_reg_nr: Union[str, None] # Grandfathers registration number (MORFARS REG.NR in original schema)
    _fodt: Union[date, None] # Birthdate (FØDT in original schema)
    _fodt_raw: Union[str, None] # Birthdate raw value (FØDT in original schema)
    _kjonn_id: int # Sex of dog (KJØNN in original schema)
    _oppdateringsdato: Union[date, None] # Update date (OPPDATERINGSDATO in original schema)
    _oppdateringsdato_raw: Union[str, None] # Update date raw value (OPPDATERINGSDATO in original schema)
    _antgangutstilt: int # Number of times displayed (ANTGANGUTSTILT in original schema)
    _premieant1: int # Number of times won (1PREMIEANT in original schema)
    _premiepros1: int # Winning percentage (1PREMIEPROS in original schema)
    _premieant2: int # Number of times placed 2nd (2PREMIEANT in original schema)
    _premiepros2: int # 2nd place percentage (2PREMIEPROS in original schema)
    _premieant3: int # Number of times placed 3rd (3PREMIEANT in original schema)
    _premiepros3: int # 3rd place percentage (3PREMIEPROS in original schema)
    _kibant: int # KIB number (KIBANT in original schema)
    _kibpros: int # KIB Percentage (KIBPROS in original schema)
    _hpant: int # HP number (HPANT in original schema)
    _hppros: int # HP Percentage (HPPROS in original schema)
    _ckant: int # CK number (CKANT in original schema)
    _ckpros: int # CK Percentage (CKPROS in original schema)
    _certant: int # CERT number (CERTANT in original schema)
    _certpros: int # CERT Percentage (CERTPROS in original schema)

    def __init__(self, reg_nr: str, farens_reg_nr: Union[str, None], morfars_reg_nr: Union[str, None]
, fodt: Union[date, None], fodt_raw: Union[str, None], kjonn_id: int, oppdateringsdato: Union[date, None], oppdateringsdato_raw: Union[str, None]
, antgangutstilt: int, premieant1: int, premiepros1: int
, premieant2: int, premiepros2: int, premieant3: int
, premiepros3: int, kibant: int, kibpros: int
, hpant: int, hppros: int, ckant: int
, ckpros: int, certant: int, certpros: int) -> None:
        self._reg_nr = reg_nr
        self._farens_reg_nr = farens_reg_nr
        self._morfars_reg_nr = morfars_reg_nr
        self._fodt = fodt
        self._fodt_raw = fodt_raw
        self._kjonn_id = kjonn_id
        self._oppdateringsdato = oppdateringsdato
        self._oppdateringsdato_raw = oppdateringsdato_raw
        self._antgangutstilt = antgangutstilt
        self._premieant1 = premieant1
        self._premiepros1 = premiepros1
        self._premieant2 = premieant2
        self._premiepros2 = premiepros2
        self._premieant3 = premieant3
        self._premiepros3 = premiepros3
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
        if len(content) != 84:
            raise AssertionError("Input for Utstillingsamleres should be 84 bytes")

        # The showcase table contains a 5 byte header that does not contain useful data
        # Remove used data from next entries
        sub_content = content[5:]

        # Parse the REG.NR property
        reg_nr = graceful_conversion(sub_content[:12]) # REG.NR (Registration number is a string capped at 12 characters)
        # Remove used data from next entries
        sub_content = sub_content[12:]

        # Parse the FARENS REG.NR property
        farens_reg_nr = graceful_conversion(sub_content[:12]) # FARENS REG.NR (Fathers registration number is a string capped at 12 characters)
        # Remove used data from next entries
        sub_content = sub_content[12:]

        # Parse the MORFARS REG.NR property
        morfars_reg_nr = graceful_conversion(sub_content[:12]) # MORFARS REG.NR (Grandfathers registration number is a string capped at 12 characters)
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

        # Parse the ANTGANGUTSTILT property
        antgangutstilt = struct.unpack('H', sub_content[:2])[0] # ANTGANGUTSTILT (Number of times displayed is a 2 byte integer)
        antgangutstilt = None if antgangutstilt == 32768 else antgangutstilt # Set to python None if value indicates null
        # Remove used data from next entries
        sub_content = sub_content[2:]

        # Parse the 1PREMIEANT property
        premieant1 = struct.unpack('H', sub_content[:2])[0] # 1PREMIEANT (Number of times won is a 2 byte integer)
        premieant1 = None if premieant1 == 32768 else premieant1 # Set to python None if value indicates null
        # Remove used data from next entries
        sub_content = sub_content[2:]

        # Parse the 1PREMIEPROS property
        premiepros1 = struct.unpack('H', sub_content[:2])[0] # 1PREMIEPROS (Winning percentage is a 2 byte integer)
        premiepros1 = None if premiepros1 == 32768 else premiepros1 # Set to python None if value indicates null
        # Remove used data from next entries
        sub_content = sub_content[2:]

        # Parse the 2PREMIEANT property
        premieant2 = struct.unpack('H', sub_content[:2])[0] # 2PREMIEANT (Number of times placed 2nd is a 2 byte integer)
        premieant2 = None if premieant2 == 32768 else premieant2 # Set to python None if value indicates null
        # Remove used data from next entries
        sub_content = sub_content[2:]

        # Parse the 2PREMIEPROS property
        premiepros2 = struct.unpack('H', sub_content[:2])[0] # 2PREMIEPROS (2nd place percentage is a 2 byte integer)
        premiepros2 = None if premiepros2 == 32768 else premiepros2 # Set to python None if value indicates null
        # Remove used data from next entries
        sub_content = sub_content[2:]

        # Parse the 3PREMIEANT property
        premieant3 = struct.unpack('H', sub_content[:2])[0] # 3PREMIEANT (Number of times placed 3rd is a 2 byte integer)
        premieant3 = None if premieant3 == 32768 else premieant3 # Set to python None if value indicates null
        # Remove used data from next entries
        sub_content = sub_content[2:]

        # Parse the 3PREMIEPROS property
        premiepros3 = struct.unpack('H', sub_content[:2])[0] # 3PREMIEPROS (3rd place percentage is a 2 byte integer)
        premiepros3 = None if premiepros3 == 32768 else premiepros3 # Set to python None if value indicates null
        # Remove used data from next entries
        sub_content = sub_content[2:]

        # Parse the KIBANT property
        kibant = struct.unpack('H', sub_content[:2])[0] # KIBANT (KIB number is a 2 byte integer)
        kibant = None if kibant == 32768 else kibant # Set to python None if value indicates null
        # Remove used data from next entries
        sub_content = sub_content[2:]

        # Parse the KIBPROS property
        kibpros = struct.unpack('H', sub_content[:2])[0] # KIBPROS (KIB Percentage is a 2 byte integer)
        kibpros = None if kibpros == 32768 else kibpros # Set to python None if value indicates null
        # Remove used data from next entries
        sub_content = sub_content[2:]

        # Parse the HPANT property
        hpant = struct.unpack('H', sub_content[:2])[0] # HPANT (HP number is a 2 byte integer)
        hpant = None if hpant == 32768 else hpant # Set to python None if value indicates null
        # Remove used data from next entries
        sub_content = sub_content[2:]

        # Parse the HPPROS property
        hppros = struct.unpack('H', sub_content[:2])[0] # HPPROS (HP Percentage is a 2 byte integer)
        hppros = None if hppros == 32768 else hppros # Set to python None if value indicates null
        # Remove used data from next entries
        sub_content = sub_content[2:]

        # Parse the CKANT property
        ckant = struct.unpack('H', sub_content[:2])[0] # CKANT (CK number is a 2 byte integer)
        ckant = None if ckant == 32768 else ckant # Set to python None if value indicates null
        # Remove used data from next entries
        sub_content = sub_content[2:]

        # Parse the CKPROS property
        ckpros = struct.unpack('H', sub_content[:2])[0] # CKPROS (CK Percentage is a 2 byte integer)
        ckpros = None if ckpros == 32768 else ckpros # Set to python None if value indicates null
        # Remove used data from next entries
        sub_content = sub_content[2:]

        # Parse the CERTANT property
        certant = struct.unpack('H', sub_content[:2])[0] # CERTANT (CERT number is a 2 byte integer)
        certant = None if certant == 32768 else certant # Set to python None if value indicates null
        # Remove used data from next entries
        sub_content = sub_content[2:]

        # Parse the CERTPROS property
        certpros = struct.unpack('H', sub_content[:2])[0] # CERTPROS (CERT Percentage is a 2 byte integer)
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
                   antgangutstilt=antgangutstilt,
                   premieant1=premieant1,
                   premiepros1=premiepros1,
                   premieant2=premieant2,
                   premiepros2=premiepros2,
                   premieant3=premieant3,
                   premiepros3=premiepros3,
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
    def farens_reg_nr(self) -> Union[str, None]:
        return None if not self._farens_reg_nr else self._farens_reg_nr

    @property
    def morfars_reg_nr(self) -> Union[str, None]:
        return None if not self._morfars_reg_nr else self._morfars_reg_nr

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
    def antgangutstilt(self) -> int:
        return self._antgangutstilt

    @property
    def premieant1(self) -> int:
        return self._premieant1

    @property
    def premiepros1(self) -> int:
        return self._premiepros1

    @property
    def premieant2(self) -> int:
        return self._premieant2

    @property
    def premiepros2(self) -> int:
        return self._premiepros2

    @property
    def premieant3(self) -> int:
        return self._premieant3

    @property
    def premiepros3(self) -> int:
        return self._premiepros3

    @property
    def kibant(self) -> int:
        return self._kibant

    @property
    def kibpros(self) -> int:
        return self._kibpros

    @property
    def hpant(self) -> int:
        return self._hpant

    @property
    def hppros(self) -> int:
        return self._hppros

    @property
    def ckant(self) -> int:
        return self._ckant

    @property
    def ckpros(self) -> int:
        return self._ckpros

    @property
    def certant(self) -> int:
        return self._certant

    @property
    def certpros(self) -> int:
        return self._certpros

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
            'antgangutstilt': self.antgangutstilt,
            'premieant1': self.premieant1,
            'premiepros1': self.premiepros1,
            'premieant2': self.premieant2,
            'premiepros2': self.premiepros2,
            'premieant3': self.premieant3,
            'premiepros3': self.premiepros3,
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

class UtstillingsamleresList:

    _contents: List[Utstillingsamleres]

    def __init__(self, contents:List[Utstillingsamleres]=[]) -> None:
        self._contents = contents
    
    @property
    def native(self) -> dict:
        """Method converts class instance to native python classes for serialization purposes"""

        return [i.native for i in self._contents]
