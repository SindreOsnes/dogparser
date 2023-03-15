import struct
from typing import List, Union
from datetime import date

from ...utils import graceful_conversion, date_conversion, extract_decimal

class Sykdom:
    _kull: str # Litter number (KULL in original schema)
    _farens_reg_nr: Union[str, None] # Fathers egistration number (FARENS REG.NR in original schema)
    _far: Union[str, None] # Father (FAR in original schema)
    _morens_reg_nr: Union[str, None] # Mothers egistration number (MORENS REG.NR in original schema)
    _mor: Union[str, None] # Mother (MOR in original schema)
    _ant_fe: Union[str, None] # ANT.FE (ANT.FE in original schema)
    _kilde: Union[str, None] # Source (KILDE in original schema)
    _langhaar: Union[str, None] # Longhair (LANGHÅR in original schema)
    _tenner_bitt: Union[str, None] # Teeth and bite (TENNER/BITT in original schema)
    _mono_krypto: Union[str, None] # MONO/KRYPTO (MONO/KRYPTO in original schema)
    _gemytt: Union[str, None] # GEMYTT (GEMYTT in original schema)
    _pancreass: Union[str, None] # PANCREASS (PANCREASS in original schema)
    _immunsvikt: Union[str, None] # Immune deficiency (IMMUNSVIKT in original schema)
    _strupebrokk: Union[str, None] # STRUPEBROKK (STRUPEBROKK in original schema)
    _navlebrokk: Union[str, None] # NAVLEBROKK (NAVLEBROKK in original schema)
    _albueartrose: Union[str, None] # Elbow artrosis (ALBUEARTROSE in original schema)
    _kloe: Union[str, None] # Itching (KLØE in original schema)
    _forkalkn: Union[str, None] # FORKALKN (FORKALKN in original schema)
    _orer: Union[str, None] # Ears (ØRER in original schema)
    _hud: Union[str, None] # Skin (HUD in original schema)
    _annet: Union[str, None] # Other (ANNET in original schema)
    _tekst: Union[str, None] # Text (TEKST in original schema)

    def __init__(self, kull: str, farens_reg_nr: Union[str, None], far: Union[str, None]
               , morens_reg_nr: Union[str, None], mor: Union[str, None], ant_fe: Union[str, None]
               , kilde: Union[str, None], langhaar: Union[str, None], tenner_bitt: Union[str, None]
               , mono_krypto: Union[str, None], gemytt: Union[str, None], pancreass: Union[str, None]
               , immunsvikt: Union[str, None], strupebrokk: Union[str, None], navlebrokk: Union[str, None]
               , albueartrose: Union[str, None], kloe: Union[str, None], forkalkn: Union[str, None]
               , orer: Union[str, None], hud: Union[str, None], annet: Union[str, None]
               , tekst: Union[str, None]) -> None:
        self._kull = kull
        self._farens_reg_nr = farens_reg_nr
        self._far = far
        self._morens_reg_nr = morens_reg_nr
        self._mor = mor
        self._ant_fe = ant_fe
        self._kilde = kilde
        self._langhaar = langhaar
        self._tenner_bitt = tenner_bitt
        self._mono_krypto = mono_krypto
        self._gemytt = gemytt
        self._pancreass = pancreass
        self._immunsvikt = immunsvikt
        self._strupebrokk = strupebrokk
        self._navlebrokk = navlebrokk
        self._albueartrose = albueartrose
        self._kloe = kloe
        self._forkalkn = forkalkn
        self._orer = orer
        self._hud = hud
        self._annet = annet
        self._tekst = tekst

    @classmethod
    def from_bytes(cls, content: bytes):
        if len(content) != 720:
            raise AssertionError("Input for Sykdom should be 720 bytes")

        # The Awards descriptions table contains a 7 byte header that does not contain useful data
        # Remove used data from next entries
        sub_content = content[7:]

        # Parse the KULL property
        kull = graceful_conversion(sub_content[:5]) # KULL (Litter number is a string capped at 5 characters)
        # Remove used data from next entries
        sub_content = sub_content[5:]

        # Parse the FARENS REG.NR property
        farens_reg_nr = graceful_conversion(sub_content[:12]) # FARENS REG.NR (Fathers egistration number is a string capped at 12 characters)
        # Remove used data from next entries
        sub_content = sub_content[12:]

        # Parse the FAR property
        far = graceful_conversion(sub_content[:36]) # FAR (Father is a string capped at 36 characters)
        # Remove used data from next entries
        sub_content = sub_content[36:]

        # Parse the MORENS REG.NR property
        morens_reg_nr = graceful_conversion(sub_content[:12]) # MORENS REG.NR (Mothers egistration number is a string capped at 12 characters)
        # Remove used data from next entries
        sub_content = sub_content[12:]

        # Parse the MOR property
        mor = graceful_conversion(sub_content[:36]) # MOR (Mother is a string capped at 36 characters)
        # Remove used data from next entries
        sub_content = sub_content[36:]

        # Parse the ANT.FE property
        ant_fe = graceful_conversion(sub_content[:2]) # ANT.FE (ANT.FE is a string capped at 2 characters)
        # Remove used data from next entries
        sub_content = sub_content[2:]

        # Parse the KILDE property
        kilde = graceful_conversion(sub_content[:20]) # KILDE (Source is a string capped at 20 characters)
        # Remove used data from next entries
        sub_content = sub_content[20:]

        # Parse the LANGHÅR property
        langhaar = graceful_conversion(sub_content[:30]) # LANGHÅR (Longhair is a string capped at 30 characters)
        # Remove used data from next entries
        sub_content = sub_content[30:]

        # Parse the TENNER/BITT property
        tenner_bitt = graceful_conversion(sub_content[:30]) # TENNER/BITT (Teeth and bite is a string capped at 30 characters)
        # Remove used data from next entries
        sub_content = sub_content[30:]

        # Parse the MONO/KRYPTO property
        mono_krypto = graceful_conversion(sub_content[:30]) # MONO/KRYPTO (MONO/KRYPTO is a string capped at 30 characters)
        # Remove used data from next entries
        sub_content = sub_content[30:]

        # Parse the GEMYTT property
        gemytt = graceful_conversion(sub_content[:30]) # GEMYTT (GEMYTT is a string capped at 30 characters)
        # Remove used data from next entries
        sub_content = sub_content[30:]

        # Parse the PANCREASS property
        pancreass = graceful_conversion(sub_content[:30]) # PANCREASS (PANCREASS is a string capped at 30 characters)
        # Remove used data from next entries
        sub_content = sub_content[30:]

        # Parse the IMMUNSVIKT property
        immunsvikt = graceful_conversion(sub_content[:30]) # IMMUNSVIKT (Immune deficiency is a string capped at 30 characters)
        # Remove used data from next entries
        sub_content = sub_content[30:]

        # Parse the STRUPEBROKK property
        strupebrokk = graceful_conversion(sub_content[:30]) # STRUPEBROKK (STRUPEBROKK is a string capped at 30 characters)
        # Remove used data from next entries
        sub_content = sub_content[30:]

        # Parse the NAVLEBROKK property
        navlebrokk = graceful_conversion(sub_content[:30]) # NAVLEBROKK (NAVLEBROKK is a string capped at 30 characters)
        # Remove used data from next entries
        sub_content = sub_content[30:]

        # Parse the ALBUEARTROSE property
        albueartrose = graceful_conversion(sub_content[:30]) # ALBUEARTROSE (Elbow artrosis is a string capped at 30 characters)
        # Remove used data from next entries
        sub_content = sub_content[30:]

        # Parse the KLØE property
        kloe = graceful_conversion(sub_content[:30]) # KLØE (Itching is a string capped at 30 characters)
        # Remove used data from next entries
        sub_content = sub_content[30:]

        # Parse the FORKALKN property
        forkalkn = graceful_conversion(sub_content[:30]) # FORKALKN (FORKALKN is a string capped at 30 characters)
        # Remove used data from next entries
        sub_content = sub_content[30:]

        # Parse the ØRER property
        orer = graceful_conversion(sub_content[:30]) # ØRER (Ears is a string capped at 30 characters)
        # Remove used data from next entries
        sub_content = sub_content[30:]

        # Parse the HUD property
        hud = graceful_conversion(sub_content[:30]) # HUD (Skin is a string capped at 30 characters)
        # Remove used data from next entries
        sub_content = sub_content[30:]

        # Parse the ANNET property
        annet = graceful_conversion(sub_content[:45]) # ANNET (Other is a string capped at 45 characters)
        # Remove used data from next entries
        sub_content = sub_content[45:]

        # Parse the TEKST property
        tekst = graceful_conversion(sub_content[:155]) # TEKST (Text is a string capped at 155 characters)
        # Remove used data from next entries
        sub_content = sub_content[155:]

        return cls(kull=kull,
                   farens_reg_nr=farens_reg_nr,
                   far=far,
                   morens_reg_nr=morens_reg_nr,
                   mor=mor,
                   ant_fe=ant_fe,
                   kilde=kilde,
                   langhaar=langhaar,
                   tenner_bitt=tenner_bitt,
                   mono_krypto=mono_krypto,
                   gemytt=gemytt,
                   pancreass=pancreass,
                   immunsvikt=immunsvikt,
                   strupebrokk=strupebrokk,
                   navlebrokk=navlebrokk,
                   albueartrose=albueartrose,
                   kloe=kloe,
                   forkalkn=forkalkn,
                   orer=orer,
                   hud=hud,
                   annet=annet,
                   tekst=tekst)

    @property
    def kull(self) -> str:
        return self._kull

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
    def ant_fe(self) -> Union[str, None]:
        return None if not self._ant_fe else self._ant_fe

    @property
    def kilde(self) -> Union[str, None]:
        return None if not self._kilde else self._kilde

    @property
    def langhaar(self) -> Union[str, None]:
        return None if not self._langhaar else self._langhaar

    @property
    def tenner_bitt(self) -> Union[str, None]:
        return None if not self._tenner_bitt else self._tenner_bitt

    @property
    def mono_krypto(self) -> Union[str, None]:
        return None if not self._mono_krypto else self._mono_krypto

    @property
    def gemytt(self) -> Union[str, None]:
        return None if not self._gemytt else self._gemytt

    @property
    def pancreass(self) -> Union[str, None]:
        return None if not self._pancreass else self._pancreass

    @property
    def immunsvikt(self) -> Union[str, None]:
        return None if not self._immunsvikt else self._immunsvikt

    @property
    def strupebrokk(self) -> Union[str, None]:
        return None if not self._strupebrokk else self._strupebrokk

    @property
    def navlebrokk(self) -> Union[str, None]:
        return None if not self._navlebrokk else self._navlebrokk

    @property
    def albueartrose(self) -> Union[str, None]:
        return None if not self._albueartrose else self._albueartrose

    @property
    def kloe(self) -> Union[str, None]:
        return None if not self._kloe else self._kloe

    @property
    def forkalkn(self) -> Union[str, None]:
        return None if not self._forkalkn else self._forkalkn

    @property
    def orer(self) -> Union[str, None]:
        return None if not self._orer else self._orer

    @property
    def hud(self) -> Union[str, None]:
        return None if not self._hud else self._hud

    @property
    def annet(self) -> Union[str, None]:
        return None if not self._annet else self._annet

    @property
    def tekst(self) -> Union[str, None]:
        return None if not self._tekst else self._tekst

    @property
    def native(self) -> dict:
        """Method converts class instance to native python classes for serialization purposes"""

        obj_dict = {
            'kull': self.kull,
            'farens_reg_nr': self.farens_reg_nr,
            'far': self.far,
            'morens_reg_nr': self.morens_reg_nr,
            'mor': self.mor,
            'ant_fe': self.ant_fe,
            'kilde': self.kilde,
            'langhaar': self.langhaar,
            'tenner_bitt': self.tenner_bitt,
            'mono_krypto': self.mono_krypto,
            'gemytt': self.gemytt,
            'pancreass': self.pancreass,
            'immunsvikt': self.immunsvikt,
            'strupebrokk': self.strupebrokk,
            'navlebrokk': self.navlebrokk,
            'albueartrose': self.albueartrose,
            'kloe': self.kloe,
            'forkalkn': self.forkalkn,
            'orer': self.orer,
            'hud': self.hud,
            'annet': self.annet,
            'tekst': self.tekst,
        }

        return obj_dict

class SykdomList:

    _contents: List[Sykdom]

    def __init__(self, contents:List[Sykdom]=[]) -> None:
        self._contents = contents
    
    @property
    def native(self) -> dict:
        """Method converts class instance to native python classes for serialization purposes"""

        return [i.native for i in self._contents]
