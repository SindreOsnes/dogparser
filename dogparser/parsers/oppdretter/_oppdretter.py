from typing import List, Union
from datetime import date

from ...utils import graceful_conversion, date_conversion

class Oppdretter:
    _kennel: str # Kennel name (KENNEL in original schema)
    _oppdr: Union[str, None] # Breeder (OPPDR in original schema)
    _adresse: Union[str, None] # Adress (ADRESSE in original schema)
    _postnr: Union[str, None] # Postal code (POSTNR in original schema)
    _tlf: Union[str, None] # Telephone number(TLF in original schema)
    _tlfa: Union[str, None] # Telephone number(TLFA in original schema)
    _tlfm: Union[str, None] # Telephone number(TLFM in original schema)
    _kunkennel: Union[str, None] # Kennel property? (KUNKENNEL in original schema)
    _nkennel: Union[str, None] # Kennel property? (NKENNEL in original schema)

    # Enum ids
    _prefiks_id: int # Prefix identifier (PREFIks in original schema)
    _fd_land_id: int # Birth country (FD-LAND in original schema)
    _oprefiks_id: int # Breeder prefix identifier (OPREFIKS in original schema)

    def __init__(self, kennel: str, prefiks_id: int, fd_land_id: int, oprefiks_id: int,
                 oppdr: Union[str, None] = None, adresse: Union[str, None] = None,
                 postnr: Union[str, None] = None, tlf: Union[str, None] = None, tlfa: Union[str, None] = None,
                 tlfm: Union[str, None] = None, kunkennel: Union[str, None] = None, nkennel: Union[str, None] = None,) -> None:

        self._kennel = kennel
        self._prefiks_id = prefiks_id
        self._fd_land_id = fd_land_id
        self._oppdr = oppdr
        self._adresse = adresse
        self._postnr = postnr
        self._tlf = tlf
        self._tlfm = tlfa
        self._tlfa = tlfm
        self._oprefiks_id = oprefiks_id
        self._kunkennel = kunkennel
        self._nkennel = nkennel
    
    @classmethod
    def from_bytes(cls, content: bytes):
        if len(content) != 250:
            raise AssertionError('Input for OPDRETTER should be 250 bytes')
        
        # The breeder table contains a 5 byte header that does not contain usefull data
        header = content[:5]
        sub_content = content

        # Eliminate the already used data and set the next property
        sub_content = sub_content[5:] # 245 bytes remaining
        kennel = graceful_conversion(sub_content[:32]) # KENNEL (name of kennel is a string capped at 32 characters)
        
        # Eliminate the already used data and set the next property
        sub_content = sub_content[32:] # 213 bytes remaining
        prefiks_id = sub_content[0] # OPREFIKS (Breeder prefix identifier)
        
        # Eliminate the already used data and set the next property
        sub_content = sub_content[1:] # 212 bytes remaining
        fd_land_id = sub_content[0] # OPREFIKS (Breeder prefix identifier)
        
        # Eliminate the already used data and set the next property
        sub_content = sub_content[1:] # 211 bytes remaining
        oppdr = graceful_conversion(sub_content[:60]) # OPPDR (name of breeder is a string capped at 50 characters)
        
        # Eliminate the already used data and set the next property
        sub_content = sub_content[60:] # 151 bytes remaining
        adresse = graceful_conversion(sub_content[:40]) # ADRESSE (Address is a string capped at 40 characters)
        
        # Eliminate the already used data and set the next property
        sub_content = sub_content[40:] # 111 bytes remaining
        postnr = graceful_conversion(sub_content[:7]) # POSTNR (postal code is a string capped at 7 characters)
        
        # Eliminate the already used data and set the next property
        sub_content = sub_content[7:] # 104 bytes remaining
        tlf = graceful_conversion(sub_content[:15]) # TLF (TELEPHONE is a string capped at 15 characters)
        
        # Eliminate the already used data and set the next property
        sub_content = sub_content[15:] # 89 bytes remaining
        tlfa = graceful_conversion(sub_content[:13]) # TLFA (TELEPHONE A is a string capped at 15 characters)
        
        # Eliminate the already used data and set the next property
        sub_content = sub_content[13:] # 76 bytes remaining
        tlfm = graceful_conversion(sub_content[:15]) # TLFM (TELEPHONE M is a string capped at 15 characters)
        
        # Eliminate the already used data and set the next property
        sub_content = sub_content[15:] # 61 bytes remaining
        oprefiks_id = sub_content[0] # OPREFIKS (Breeder prefix identifier)
        
        # Eliminate the already used data and set the next property
        sub_content = sub_content[1:] # 60 bytes remaining
        kunkennel = graceful_conversion(sub_content[:28]) # KUNNKENNEL (kennel name, without prefix, is a string capped at 28 characters)
        
        # Eliminate the already used data and set the next property
        sub_content = sub_content[28:] # 32 bytes remaining
        nkennel = graceful_conversion(sub_content[:32]) # NKENNEL (nkennel is a string capped at 32 characters)
        
        return cls(
            kennel=kennel,
            prefiks_id=prefiks_id,
            fd_land_id=fd_land_id,
            oppdr=oppdr,
            adresse=adresse,
            postnr=postnr,
            tlf=tlf,
            tlfa=tlfa,
            tlfm=tlfm,
            oprefiks_id=oprefiks_id,
            kunkennel=kunkennel,
            nkennel=nkennel,
            )
    
    @property
    def kennel(self) -> Union[str, None]:
        return None if not self._kennel else self._kennel
    
    @property
    def prefiks_id(self) -> int:
        return self._prefiks_id
    
    @property
    def fd_land_id(self) -> int:
        return self._fd_land_id
    
    @property
    def oppdr(self) -> Union[str, None]:
        return None if not self._oppdr else self._oppdr
    
    @property
    def adresse(self) -> Union[str, None]:
        return None if not self._adresse else self._adresse
    
    @property
    def postnr(self) -> Union[str, None]:
        return None if not self._postnr else self._postnr
    
    @property
    def tlf(self) -> Union[str, None]:
        return None if not self._tlf else self._tlf
    
    @property
    def tlfa(self) -> Union[str, None]:
        return None if not self._tlfa else self._tlfa
    
    @property
    def tlfm(self) -> Union[str, None]:
        return None if not self._tlfm else self._tlfm
    
    @property
    def oprefiks_id(self) -> int:
        return self._oprefiks_id
    
    @property
    def kunkennel(self) -> Union[str, None]:
        return None if not self._kunkennel else self._kunkennel
    
    @property
    def nkennel(self) -> Union[str, None]:
        return None if not self._nkennel else self._nkennel
    

    @property
    def native(self) -> dict:
        """Method converts class instance to native python classes for serialization purposes"""

        obj_dict = {
            'kennel': self.kennel,
            'prefiks_id': self.prefiks_id,
            'fd_land_id': self.fd_land_id,
            'oppdr': self.oppdr,
            'adresse': self.adresse,
            'postnr': self.postnr,
            'tlf': self.tlf,
            'tlfa': self.tlfa,
            'tlfm': self.tlfm,
            'oprefiks_id': self.oprefiks_id,
            'kunkennel': self.kunkennel,
            'nkennel': self.nkennel,
        }

        return obj_dict

class OppdretterList:

    _contents: List[Oppdretter]

    def __init__(self, contents:List[Oppdretter]=[]) -> None:
        self._contents = contents
    
    @property
    def native(self) -> dict:
        """Method converts class instance to native python classes for serialization purposes"""

        return [i.native for i in self._contents]
