from typing import List, Union
from datetime import date

from ...utils import graceful_conversion, date_conversion

class Innavl:
    _reg_nr: str # Registration number (REG.NR in original schema)
    _kullnr: Union[str, None] # Litter identifier (KULLNR in original schema)
    _navn: str # Name (NAVN in original schema)
    _innavl: Union[str, None] # Inbreeding (INNAVL in original schema)

    def __init__(self, reg_nr: str, navn: str, kullnr: Union[str, None] = None,
                 innavl: Union[str, None] = None) -> None:

        self._reg_nr = reg_nr
        self._navn = navn
        self._kullnr = kullnr
        self._innavl = innavl
    
    @classmethod
    def from_bytes(cls, content: bytes):
        if len(content) != 289:
            raise AssertionError('Input for INNAVL should be 289 bytes')
        
        # The inbreeding table contains a 3 byte header that does not contain usefull data
        header = content[:3]

        # Eliminate the already used data and set the next property
        sub_content = content[3:] # 286 bytes remaining
        reg_nr = graceful_conversion(sub_content[:12]) # REG.NR (registration number is a string capped at 12 characters)
        
        # Eliminate the already used data and set the next property
        sub_content = sub_content[12:] # 274 bytes remaining
        kullnr = graceful_conversion(sub_content[:5]) # KULLNR (litter number/identifier is a string capped at 5 characters)
        
        # Eliminate the already used data and set the next property
        sub_content = sub_content[5:] # 269 bytes remaining
        navn = graceful_conversion(sub_content[:36]) # NAVN (name of dog is a string capped at 36 characters)
        
        # Eliminate the already used data and set the next property
        sub_content = sub_content[36:] # 233 bytes remaining
        innavl = graceful_conversion(sub_content[:233]) # KENNEL (name of kennel is a string capped at 26 characters)
        
        return cls(
            reg_nr=reg_nr,
            kullnr=kullnr,
            navn=navn,
            innavl=innavl,
            )
    
    @property
    def reg_nr(self) -> str:
        return self._reg_nr
    
    @property
    def navn(self) -> str:
        return self._navn

    @property
    def kullnr(self) -> Union[str, None]:
        return None if not self._kullnr else self._kullnr
    
    @property
    def innavl(self) -> Union[str, None]:
        return None if not self._innavl else self._innavl
    

    @property
    def native(self) -> dict:
        """Method converts class instance to native python classes for serialization purposes"""

        obj_dict = {
            'reg_nr': self.reg_nr,
            'navn': self.navn,
            'kullnr': self.kullnr,
            'innavl': self.innavl,
        }

        return obj_dict

class InnavlList:

    _contents: List[Innavl]

    def __init__(self, contents:List[Innavl]=[]) -> None:
        self._contents = contents
    
    @property
    def native(self) -> dict:
        """Method converts class instance to native python classes for serialization purposes"""

        return [i.native for i in self._contents]
