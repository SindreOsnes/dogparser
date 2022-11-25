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

    def __init__(self, reg_nr: str, farens_reg_nr: Union[str, None], morfars_reg_nr: Union[str, None]
, fodt: Union[date, None], fodt_raw: Union[str, None], kjonn_id: int, oppdateringsdato: Union[date, None], oppdateringsdato_raw: Union[str, None]
, antgangutstilt: int, premieant1: int) -> None:
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

        return cls(reg_nr=reg_nr,
                   farens_reg_nr=farens_reg_nr,
                   morfars_reg_nr=morfars_reg_nr,
                   fodt=fodt,
                   fodt_raw=fodt_raw,
                   kjonn_id=kjonn_id,
                   oppdateringsdato=oppdateringsdato,
                   oppdateringsdato_raw=oppdateringsdato_raw,
                   antgangutstilt=antgangutstilt,
                   premieant1=premieant1)

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
