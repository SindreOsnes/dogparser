from typing import List, Union
from datetime import date

from ...utils import graceful_conversion, date_conversion

class Eier:
    _reg_nr: str # Registration number (REG.NR in original schema)
    _kullnr: Union[str, None] # Litter identifier (KULLNR in original schema)
    _navn: str # Name (NAVN in original schema)
    _kennel: Union[str, None] # Kennel name (KENNEL in original schema)
    _eier: Union[str, None] # Owners name (EIER in original schema)
    _sted: Union[str, None] # Address (STED in original schema)
    _postnr: Union[str, None] # Postal code (POSTNR in original schema)

    def __init__(self, reg_nr: str, navn: str, kullnr: Union[str, None] = None,
                 kennel: Union[str, None] = None, eier: Union[str, None] = None,
                 sted: Union[str, None] = None, postnr: Union[str, None] = None) -> None:

        self._reg_nr = reg_nr
        self._navn = navn
        self._kullnr = kullnr
        self._kennel = kennel
        self._eier = eier
        self._sted = sted
        self._postnr = postnr
    
    @classmethod
    def from_bytes(cls, content: bytes):
        if len(content) != 180:
            raise AssertionError('Input for Eier should be 180 bytes')
        
        # The owner table contains a 4 byte header that does not contain usefull data
        header = content[:4]

        # Eliminate the already used data and set the next property
        sub_content = content[4:] # 176 bytes remaining
        reg_nr = graceful_conversion(sub_content[:12]) # REG.NR (registration number is a string capped at 12 characters)
        
        # Eliminate the already used data and set the next property
        sub_content = sub_content[12:] # 164 bytes remaining
        kullnr = graceful_conversion(sub_content[:5]) # KULLNR (litter number/identifier is a string capped at 5 characters)
        
        # Eliminate the already used data and set the next property
        sub_content = sub_content[5:] # 159 bytes remaining
        navn = graceful_conversion(sub_content[:36]) # NAVN (name of dog is a string capped at 36 characters)
        
        # Eliminate the already used data and set the next property
        sub_content = sub_content[36:] # 123 bytes remaining
        kennel = graceful_conversion(sub_content[:26]) # KENNEL (name of kennel is a string capped at 26 characters)
        
        # Eliminate the already used data and set the next property
        sub_content = sub_content[26:] # 97 bytes remaining
        eier = graceful_conversion(sub_content[:50]) # EIER (name of owner is a string capped at 50 characters)
        
        # Eliminate the already used data and set the next property
        sub_content = sub_content[50:] # 47 bytes remaining
        sted = graceful_conversion(sub_content[:40]) # STED (Adress is a string capped at 50 characters)
        
        # Eliminate the already used data and set the next property
        sub_content = sub_content[40:] # 7 bytes remaining
        postnr = graceful_conversion(sub_content[:7]) # POSTNR (postal code is a string capped at 7 characters)
        
        return cls(
            reg_nr=reg_nr,
            kullnr=kullnr,
            navn=navn,
            kennel=kennel,
            eier=eier,
            sted=sted,
            postnr=postnr,
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
    def kennel(self) -> Union[str, None]:
        return None if not self._kennel else self._kennel
    
    @property
    def eier(self) -> Union[str, None]:
        return None if not self._eier else self._eier
    
    @property
    def sted(self) -> Union[str, None]:
        return None if not self._sted else self._sted
    
    @property
    def postnr(self) -> Union[str, None]:
        return None if not self._postnr else self._postnr
    

    @property
    def native(self) -> dict:
        """Method converts class instance to native python classes for serialization purposes"""

        obj_dict = {
            'reg_nr': self.reg_nr,
            'navn': self.navn,
            'kullnr': self.kullnr,
            'kennel': self.kennel,
            'eier': self.eier,
            'sted': self.sted,
            'postnr':  self.postnr,
        }

        return obj_dict

class EierList:

    _contents: List[Eier]

    def __init__(self, contents:List[Eier]=[]) -> None:
        self._contents = contents
    
    @property
    def native(self) -> dict:
        """Method converts class instance to native python classes for serialization purposes"""

        return [i.native for i in self._contents]