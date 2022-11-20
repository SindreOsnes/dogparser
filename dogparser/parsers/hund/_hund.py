from typing import List, Union
from datetime import date

from ...utils import graceful_conversion, date_conversion

class Hund:
    _reg_nr: str

    _fodt: Union[date, None] # Birthdate (FØDT in original schema)
    _fodt_raw: Union[date, None] # Birthdate raw value (FØDT in original schema)
    _fd_land_id: int # Birth country
    _kjonn_id: int # Sex
    _kullnr: Union[str, None] # Litter identifier

    def __init__(self, reg_nr: str, fd_land_id: int, kjonn_id: int,
                 fodt: Union[date, None] = None, fodt_raw: Union[str, None] = None, kullnr: Union[str, None] = None) -> None:
        self._reg_nr = reg_nr
        self._fodt = fodt
        self._fd_land_id = fd_land_id
        self._kjonn_id = kjonn_id
        self._kullnr = kullnr
        self._fodt_raw = fodt_raw
    
    @classmethod
    def from_bytes(cls, content: bytes):
        if len(content) != 250:
            raise AssertionError('Input for Hund should be 250 bytes')
        
        # The dog table contains a 10 byte header that does not contain usefull data
        header = content[:10]

        # Eliminate the already used data and set the next property
        sub_content = content[10:] # 240 bytes remaining
        reg_nr = graceful_conversion(sub_content[:12]) # REG.NR (registration number is a string capped at 12 characters)

        # Eliminate the already used data and set the next property
        sub_content = sub_content[12:] # 228 bytes remaining
        fodt = None
        fodt_raw = graceful_conversion(sub_content[:6])
        try:
            fodt = date_conversion(sub_content[:6]) # FØDT (birthdate/født is represented by a 6 digit numerical string)
        except ValueError as e:
            print(e)
        
        # Eliminate the already used data and set the next property
        sub_content = sub_content[6:] # 222 bytes remaining
        fd_land_id = sub_content[0]
        
        # Eliminate the already used data and set the next property
        sub_content = sub_content[1:] # 221 bytes remaining
        kjonn_id = sub_content[0]
        
        # Eliminate the already used data and set the next property
        sub_content = sub_content[1:] # 220 bytes remaining
        kullnr = graceful_conversion(sub_content[:5]) # KULLNR (litter number/identifier is a string capped at 5 characters)

        return cls(reg_nr=reg_nr, fodt=fodt, fodt_raw=fodt_raw, fd_land_id=fd_land_id, kjonn_id=kjonn_id, kullnr=kullnr)
    
    @property
    def reg_nr(self) -> str:
        return self._reg_nr
    
    @property
    def fd_land_id(self) -> int:
        return self._fd_land_id
    
    @property
    def kjonn_id(self) -> int:
        return self._kjonn_id
    
    @property
    def fodt(self) -> Union[date, None]:
        return self._fodt
    
    @property
    def fodt_str(self) -> Union[str, None]:
        return None if not self._fodt else self.fodt.isoformat()
    
    @property
    def kullnr(self) -> Union[str, None]:
        return None if not self._kullnr else self._kullnr
    
    @property
    def fodt_raw(self) -> Union[str, None]:
        return self._fodt_raw

    @property
    def native(self) -> dict:
        """Method converts class instance to native python classes for serialization purposes"""

        return {
            'reg_nr': self.reg_nr,
            'fodt': self.fodt_str,
            'fodt_raw': self.fodt_raw,
            'fd_land_id': self._fd_land_id,
            'kjonn_id': self.kjonn_id,
            'kullnr': self.kullnr
            }

class HundList:

    _contents: List[Hund]

    def __init__(self, contents:List[Hund]=[]) -> None:
        self._contents = contents
    
    @property
    def native(self) -> dict:
        """Method converts class instance to native python classes for serialization purposes"""

        return [i.native for i in self._contents]