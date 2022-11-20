from typing import List, Union
from datetime import date

from ...utils import graceful_conversion, date_conversion

class Hund:
    _reg_nr: str # Registration number (REG.NR in original schema)
    _navn: str # Name (NAVN in original schema)
    _fodt: Union[date, None] # Birthdate (FØDT in original schema)
    _fodt_raw: Union[date, None] # Birthdate raw value (FØDT in original schema)
    _kullnr: Union[str, None] # Litter identifier (KULLNR in original schema)
    _kennel: Union[str, None] # Kennel name (KENNEL in original schema)

    # Enum ids
    _fd_land_id: int # Birth country (FD-LAND in original schema)
    _kjonn_id: int # Sex (KJØNN in original schema)
    _hd_id: int # hd? (HD in original schema)
    _ad_id: int # ad? (AD in original schema)
    _hem_id: int # hem? (HEM in original schema)

    def __init__(self, reg_nr: str, navn: str, fd_land_id: int, kjonn_id: int,
                 hd_id: int, ad_id: int, hem_id: int,
                 fodt: Union[date, None] = None, fodt_raw: Union[str, None] = None, kullnr: Union[str, None] = None,
                 kennel: Union[str, None] = None) -> None:
        self._reg_nr = reg_nr
        self._navn = navn
        self._fodt = fodt
        self._fodt_raw = fodt_raw
        self._fd_land_id = fd_land_id
        self._kjonn_id = kjonn_id
        self._kullnr = kullnr
        self._hd_id = hd_id
        self._ad_id = ad_id
        self._kennel = kennel
        self._hem_id = hem_id
    
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
        fd_land_id = sub_content[0] # FD-LAND index
        
        # Eliminate the already used data and set the next property
        sub_content = sub_content[1:] # 221 bytes remaining
        kjonn_id = sub_content[0] # KJØNN index
        
        # Eliminate the already used data and set the next property
        sub_content = sub_content[1:] # 220 bytes remaining
        kullnr = graceful_conversion(sub_content[:5]) # KULLNR (litter number/identifier is a string capped at 5 characters)
        
        # Eliminate the already used data and set the next property
        sub_content = sub_content[5:] # 215 bytes remaining
        navn = graceful_conversion(sub_content[:38]) # NAVN (name of dog is a string capped at 38 characters)
        
        # Eliminate the already used data and set the next property
        sub_content = sub_content[38:] # 177 bytes remaining
        hd_id = sub_content[0] # HD index
        
        # Eliminate the already used data and set the next property
        sub_content = sub_content[1:] # 176 bytes remaining
        ad_id = sub_content[0] # AD index
        
        # Eliminate the already used data and set the next property
        sub_content = sub_content[1:] # 175 bytes remaining
        kennel = graceful_conversion(sub_content[:32]) # KENNEL (name of kennel is a string capped at 32 characters)
        
        # Eliminate the already used data and set the next property
        sub_content = sub_content[32:] # 143 bytes remaining
        hem_id = sub_content[0] # HEM index

        return cls(
            reg_nr=reg_nr,
            fodt=fodt,
            fodt_raw=fodt_raw,
            fd_land_id=fd_land_id,
            kjonn_id=kjonn_id,
            kullnr=kullnr,
            navn=navn,
            hd_id=hd_id,
            ad_id=ad_id,
            kennel=kennel,
            hem_id=hem_id,
            )
    
    @property
    def reg_nr(self) -> str:
        return self._reg_nr
    
    @property
    def navn(self) -> str:
        return self._navn
    
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
    def hd_id(self) -> int:
        return self._hd_id
    
    @property
    def ad_id(self) -> int:
        return self._ad_id
    
    @property
    def fodt_raw(self) -> Union[str, None]:
        return self._fodt_raw
    
    @property
    def kennel(self) -> Union[str, None]:
        return None if not self._kennel else self._kennel
    
    @property
    def hem_id(self) -> int:
        return self._hem_id

    @property
    def native(self) -> dict:
        """Method converts class instance to native python classes for serialization purposes"""

        return {
            'reg_nr': self.reg_nr,
            'navn': self.navn,
            'fodt': self.fodt_str,
            'fodt_raw': self.fodt_raw,
            'fd_land_id': self._fd_land_id,
            'kjonn_id': self.kjonn_id,
            'kullnr': self.kullnr,
            'hd_id': self.hd_id,
            'ad_id': self.ad_id,
            'kennel': self.kennel,
            'hem_id': self.hem_id,
            }

class HundList:

    _contents: List[Hund]

    def __init__(self, contents:List[Hund]=[]) -> None:
        self._contents = contents
    
    @property
    def native(self) -> dict:
        """Method converts class instance to native python classes for serialization purposes"""

        return [i.native for i in self._contents]