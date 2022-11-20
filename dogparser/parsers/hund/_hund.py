from typing import List, Union
from datetime import date

from ...utils import graceful_conversion, date_conversion

class Hund:
    _reg_nr: str

    _fodt: Union[date, None] # Birthdate (FØDT in original schema)

    def __init__(self, reg_nr: str, fodt: Union[date, None] = None) -> None:
        self._reg_nr = reg_nr
        self._fodt = fodt
    
    @classmethod
    def from_bytes(cls, content: bytes):
        if len(content) != 250:
            raise AssertionError('Input for Hund should be 250 bytes')
        
        # The dog table contains a 10 byte header that does not contain usefull data
        header = content[:10]

        # Eliminate the already used data and set the next property
        sub_content = content[10:] # 240 bytes remaining
        reg_nr = graceful_conversion(sub_content[:12]) # REG.NR (registration number is a string capped at 12 character)

        # Eliminate the already used data and set the next property
        sub_content = sub_content[12:] # 228 bytes remaining
        fodt = date_conversion(sub_content[:6]) # FØDT (birthdate/født is represented by a 6 digit numerical string)

        return cls(reg_nr=reg_nr, fodt=fodt)
    
    @property
    def reg_nr(self) -> str:
        return self._reg_nr
    
    @property
    def fodt(self) -> str:
        return self._fodt

    @property
    def native(self) -> dict:
        """Method converts class instance to native python classes for serialization purposes"""

        return {'reg_nr': self.reg_nr, 'fodt': self.fodt}


class HundList:

    _contents: List[Hund]

    def __init__(self, contents:List[Hund]=[]) -> None:
        self._contents = contents
    
    @property
    def native(self) -> dict:
        """Method converts class instance to native python classes for serialization purposes"""

        return [i.native for i in self._contents]