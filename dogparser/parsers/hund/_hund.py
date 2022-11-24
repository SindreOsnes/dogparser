from typing import List, Union
from datetime import date

from ...utils import graceful_conversion, date_conversion

class Hund:
    _reg_nr: str # Registration number (REG.NR in original schema)
    _navn: str # Name (NAVN in original schema)
    _fodt: Union[date, None] # Birthdate (FØDT in original schema)
    _fodt_raw: Union[str, None] # Birthdate raw value (FØDT in original schema)
    _kullnr: Union[str, None] # Litter identifier (KULLNR in original schema)
    _kennel: Union[str, None] # Kennel name (KENNEL in original schema)
    _farge: Union[str, None] # Color (FARGE in original schema)

    _farens_reg_nr: str # Fathers registration number (FARENS REG.NR in original schema)
    _far: str #Fathers name (FAR in original schema)

    _morens_reg_nr: str # Mothers registration number (MORENS REG.NR in original schema)
    _mor: str # Mothers name (MOR in original schema)

    # Enum ids
    _fd_land_id: int # Birth country (FD-LAND in original schema)
    _kjonn_id: int # Sex (KJØNN in original schema)
    _hd_id: int # hd? (HD in original schema)
    _ad_id: int # ad? (AD in original schema)
    _hem_id: int # hem? (HEM in original schema)
    _utd_id: int # utd? (UTD in original schema)
    _utd2_id: int # utd2? (UTD2 in original schema)
    _utd3_id: int # utd3? (UTD3 in original schema)
    _utmer_id: int # utmer? (UTMER in original schema)
    _vin_id: int # vin? (VIN in original schema)
    _k_id: int # k? (K in original schema)
    _zb_id: int # zb? (ZB in original schema)
    _kkl_id: int # kkl? (KKL in original schema)
    _bruks_id: int # bruks? (BRUKS in original schema)
    _bruks2_id: int # bruks2? (BRUKS2 in original schema)
    _bruks3_id: int # bruks3? (BRUKS3 in original schema)
    _bruks4_id: int # bruks4? (BRUKS4 in original schema)
    _prem_id: int # prem? (PREM in original schema)
    _kval_id: int # kval? (KVAL in original schema)
    _kval2_id: int # kval2? (KVAL2 in original schema)
    _test_id: int # test? (TEST in original schema)
    _test2_id: int # test2? (TEST2 in original schema)

    def __init__(self, reg_nr: str, navn: str, fd_land_id: int, kjonn_id: int,
                 hd_id: int, ad_id: int, hem_id: int, utd_id: int,
                 utd2_id: int, utd3_id: int, utmer_id: int,
                 vin_id: int, k_id: int, zb_id: int,
                 kkl_id: int, bruks_id: int, bruks2_id: int,
                 bruks3_id: int, bruks4_id: int, prem_id: int,
                 kval_id: int, kval2_id: int, test_id: int, test2_id: int,
                 fodt: Union[date, None] = None, fodt_raw: Union[str, None] = None, kullnr: Union[str, None] = None,
                 kennel: Union[str, None] = None, farge: Union[str, None] = None,
                 farens_reg_nr: Union[str, None] = None, far: Union[str, None] = None,
                 morens_reg_nr: Union[str, None] = None, mor: Union[str, None] = None,) -> None:
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
        self._farge = farge
        self._utd_id = utd_id
        self._utd2_id = utd2_id
        self._utd3_id = utd3_id
        self._utmer_id = utmer_id
        self._vin_id = vin_id
        self._k_id = k_id
        self._zb_id = zb_id
        self._kkl_id = kkl_id
        self._bruks_id = bruks_id
        self._bruks2_id = bruks2_id
        self._bruks3_id = bruks3_id
        self._bruks4_id = bruks4_id
        self._prem_id = prem_id
        self._kval_id = kval_id
        self._kval2_id = kval2_id
        self._test_id = test_id
        self._test2_id = test2_id
        self._farens_reg_nr = farens_reg_nr
        self._far = far
        self._morens_reg_nr = morens_reg_nr
        self._mor = mor
    
    @classmethod
    def from_bytes(cls, content: bytes):
        if len(content) != 250:
            raise AssertionError('Input for Hund should be 250 bytes')
        
        # The dog table contains a 10 byte header that does not contain useful data
        header = content[:10]
        sub_content = content

        # Eliminate the already used data and set the next property
        sub_content = sub_content[10:] # 240 bytes remaining
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
        
        # Eliminate the already used data and set the next property
        sub_content = sub_content[1:] # 142 bytes remaining
        farge = graceful_conversion(sub_content[:10]) # FARGE (color is a string capped at 10 characters)
        
        # Eliminate the already used data and set the next property
        sub_content = sub_content[10:] # 132 bytes remaining
        utd_id = sub_content[0] # UTD index
        
        # Eliminate the already used data and set the next property
        sub_content = sub_content[1:] # 131 bytes remaining
        utd2_id = sub_content[0] # UTD2 index
        
        # Eliminate the already used data and set the next property
        sub_content = sub_content[1:] # 130 bytes remaining
        utd3_id = sub_content[0] # UTD3 index
        
        # Eliminate the already used data and set the next property
        sub_content = sub_content[1:] # 129 bytes remaining
        utmer_id = sub_content[0] # UTMER index
        
        # Eliminate the already used data and set the next property
        sub_content = sub_content[1:] # 128 bytes remaining
        vin_id = sub_content[0] # VIN index
        
        # Eliminate the already used data and set the next property
        sub_content = sub_content[1:] # 127 bytes remaining
        k_id = sub_content[0] # K index
        
        # Eliminate the already used data and set the next property
        sub_content = sub_content[1:] # 126 bytes remaining
        zb_id = sub_content[0] # ZB index
        
        # Eliminate the already used data and set the next property
        sub_content = sub_content[1:] # 125 bytes remaining
        kkl_id = sub_content[0] # KKL index
        
        # Eliminate the already used data and set the next property
        sub_content = sub_content[1:] # 124 bytes remaining
        bruks_id = sub_content[0] # BRUKS index
        
        # Eliminate the already used data and set the next property
        sub_content = sub_content[1:] # 123 bytes remaining
        bruks2_id = sub_content[0] # BRUKS2 index
        
        # Eliminate the already used data and set the next property
        sub_content = sub_content[1:] # 122 bytes remaining
        bruks3_id = sub_content[0] # BRUKS3 index
        
        # Eliminate the already used data and set the next property
        sub_content = sub_content[1:] # 121 bytes remaining
        bruks4_id = sub_content[0] # BRUKS4 index
        
        # Eliminate the already used data and set the next property
        sub_content = sub_content[1:] # 120 bytes remaining
        prem_id = sub_content[0] # PREM index
        
        # Eliminate the already used data and set the next property
        sub_content = sub_content[1:] # 119 bytes remaining
        kval_id = sub_content[0] # KVAL index
        
        # Eliminate the already used data and set the next property
        sub_content = sub_content[1:] # 118 bytes remaining
        kval2_id = sub_content[0] # KVAL2 index
        
        # Eliminate the already used data and set the next property
        sub_content = sub_content[1:] # 117 bytes remaining
        test_id = sub_content[0] # TEST index
        
        # Eliminate the already used data and set the next property
        sub_content = sub_content[1:] # 116 bytes remaining
        test2_id = sub_content[0] # TEST2 index

        # Eliminate the already used data and set the next property (134-149 unused)
        sub_content = content[150:] # 100 bytes remaining
        farens_reg_nr = graceful_conversion(sub_content[:12]) # FARENS REG.NR (registration number is a string capped at 12 characters)

        # Eliminate the already used data and set the next property
        sub_content = sub_content[12:] # 88 bytes remaining
        far = graceful_conversion(sub_content[:38]) # FAR (name of father is a string capped at 38 characters)

        # Eliminate the already used data and set the next property
        sub_content = sub_content[38:] # 50 bytes remaining
        morens_reg_nr = graceful_conversion(sub_content[:12]) # MORENS REG.NR (registration number is a string capped at 12 characters)

        # Eliminate the already used data and set the next property
        sub_content = sub_content[12:] # 38 bytes remaining
        mor = graceful_conversion(sub_content[:38]) # MOR (name of mother is a string capped at 38 characters)

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
            farge=farge,
            utd_id=utd_id,
            utd2_id=utd2_id,
            utd3_id=utd3_id,
            utmer_id=utmer_id,
            vin_id=vin_id,
            k_id=k_id,
            zb_id=zb_id,
            kkl_id=kkl_id,
            bruks_id=bruks_id,
            bruks2_id=bruks2_id,
            bruks3_id=bruks3_id,
            bruks4_id=bruks4_id,
            prem_id=prem_id,
            kval_id=kval_id,
            kval2_id=kval2_id,
            test_id=test_id,
            test2_id=test2_id,
            farens_reg_nr=farens_reg_nr,
            far=far,
            morens_reg_nr=morens_reg_nr,
            mor=mor,
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
    def farge(self) -> Union[str, None]:
        return None if not self._farge else self._farge
    
    @property
    def utd_id(self) -> int:
        return self._utd_id
    
    @property
    def utd2_id(self) -> int:
        return self._utd2_id
    
    @property
    def utd3_id(self) -> int:
        return self._utd3_id
    
    @property
    def utmer_id(self) -> int:
        return self._utmer_id
    
    @property
    def vin_id(self) -> int:
        return self._vin_id
    
    @property
    def k_id(self) -> int:
        return self._k_id
    
    @property
    def zb_id(self) -> int:
        return self._zb_id
    
    @property
    def kkl_id(self) -> int:
        return self._kkl_id
    
    @property
    def bruks_id(self) -> int:
        return self._bruks_id
    
    @property
    def bruks2_id(self) -> int:
        return self._bruks2_id
    
    @property
    def bruks3_id(self) -> int:
        return self._bruks3_id
    
    @property
    def bruks4_id(self) -> int:
        return self._bruks4_id
    
    @property
    def prem_id(self) -> int:
        return self._prem_id
    
    @property
    def kval_id(self) -> int:
        return self._kval_id
    
    @property
    def kval2_id(self) -> int:
        return self._kval2_id
    
    @property
    def test_id(self) -> int:
        return self._test_id
    
    @property
    def test2_id(self) -> int:
        return self._test2_id
    
    @property
    def farens_reg_nr(self) -> Union[str, None]:
        return None if not self._farens_reg_nr else self._farens_reg_nr
    
    @property
    def far(self) -> Union[str, None]:
        return None if not self._far else self._far
    
    @property
    def morens_reg_nr(self) -> Union[str, None]:
        return None if not self._morens_reg_nr else self._morens_reg_nr
    
    @property
    def mor(self) -> Union[str, None]:
        return None if not self._mor else self._mor

    @property
    def native(self) -> dict:
        """Method converts class instance to native python classes for serialization purposes"""

        obj_dict = {
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
            'farge': self.farge,
            'utd_id':  self.utd_id,
            'utd2_id':  self.utd2_id,
            'utd3_id':  self.utd3_id,
            'utmer_id':  self.utmer_id,
            'vin_id':  self.vin_id,
            'k_id':  self.k_id,
            'zb_id':  self.zb_id,
            'kkl_id':  self.kkl_id,
            'bruks_id':  self.bruks_id,
            'bruks2_id':  self.bruks2_id,
            'bruks3_id':  self.bruks3_id,
            'bruks4_id':  self.bruks4_id,
            'prem_id':  self.prem_id,
            'kval_id':  self.kval_id,
            'kval2_id':  self.kval2_id,
            'test_id':  self.test_id,
            'test2_id':  self.test2_id,
            'farens_reg_nr': self.farens_reg_nr,
            'far': self.far,
            'morens_reg_nr': self.morens_reg_nr,
            'mor': self.mor,
        }

        return obj_dict

class HundList:

    _contents: List[Hund]

    def __init__(self, contents:List[Hund]=[]) -> None:
        self._contents = contents
    
    @property
    def native(self) -> dict:
        """Method converts class instance to native python classes for serialization purposes"""

        return [i.native for i in self._contents]
