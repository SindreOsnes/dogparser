from typing import List, Union
from datetime import date

from ...utils import graceful_conversion, date_conversion

class Kull:
    _kullb: Union[str, None] # Litter letter (KULLB in original schema)
    _kennel: Union[str, None] # Kennel (KENNEL in original schema)
    _kullnr: str # Litter number/identifier (KULLNR in original schema)
    _fodt: Union[date, None] # Birthdate (FØDT in original schema)
    _fodt_raw: Union[str, None] # Birthdate raw value (FØDT in original schema)
    _fd_land_id: int # Birth country index (FD-LAND in original schema)
    _oppdr: Union[str, None] # Breeder (OPPDR in original schema)
    _adresse: Union[str, None] # Address (ADRESSE in original schema)
    _postnr: Union[str, None] # Postal code (POSTNR in original schema)
    _farens_reg_nr: Union[str, None] # Fathers registration number (FARENS REG.NR in original schema)
    _morfars_reg_nr: Union[str, None] # Grandfathers registration number (MORFARS REG.NR in original schema)
    _morens_reg_nr: Union[str, None] # Mothers registration number (MORENS REG.NR in original schema)
    _sosken: Union[str, None] # Siblings (SØSKEN in original schema)
    _innavl: Union[str, None] # Inbreeding (INNAVL in original schema)
    _merkn: Union[str, None] # Remarks (MERKN in original schema)
    _ant: Union[int, None] # Number (ANT in original schema)
    _h: Union[int, None] # H? (H in original schema)
    _t: Union[int, None] # T? (T in original schema)
    _utmrkber: Union[int, None] # UTMRKBER? (UTMRKBER in original schema)
    _friber: Union[int, None] # FRIBER? (FRIBER in original schema)
    _svakber: Union[int, None] # SVAKBER? (SVAKBER in original schema)
    _middelsber: Union[int, None] # MIDDELSBER? (MIDDELSBER in original schema)
    _sterkber: Union[int, None] # STERKBER? (STERKBER in original schema)
    _utmrk: Union[int, None] # UTMRK? (UTMRK in original schema)
    _fri: Union[int, None] # FRI? (FRI in original schema)
    _svak: Union[int, None] # SVAK? (SVAK in original schema)
    _middels: Union[int, None] # MIDDELS? (MIDDELS in original schema)
    _sterk: Union[int, None] # STERK? (STERK in original schema)
    _ro: Union[int, None] # RØ? (RØ in original schema)
    _tothd: Union[int, None] # TOTHD? (TOTHD in original schema)
    _friberad: Union[int, None] # FRIBERAD? (FRIBERAD in original schema)
    _svakberad: Union[int, None] # SVAKBERAD? (SVAKBERAD in original schema)
    _middelsberad: Union[int, None] # MIDDELSBERAD? (MIDDELSBERAD in original schema)
    _sterkberad: Union[int, None] # STERKBERAD? (STERKBERAD in original schema)
    _friad: Union[int, None] # FRIAD? (FRIAD in original schema)
    _svakad: Union[int, None] # SVAKAD? (SVAKAD in original schema)
    _middelsad: Union[int, None] # MIDDELSAD? (MIDDELSAD in original schema)
    _sterkad: Union[int, None] # STERKAD? (STERKAD in original schema)
    _road: Union[int, None] # RØAD? (RØAD in original schema)
    _totad: Union[int, None] # TOTAD? (TOTAD in original schema)
    _reg_nr1: Union[str, None] # Registration number for dog number 1 (REG.NR1 in original schema)
    _reg_nr2: Union[str, None] # Registration number for dog number 2 (REG.NR2 in original schema)
    _reg_nr3: Union[str, None] # Registration number for dog number 3 (REG.NR3 in original schema)
    _reg_nr4: Union[str, None] # Registration number for dog number 4 (REG.NR4 in original schema)
    _reg_nr5: Union[str, None] # Registration number for dog number 5 (REG.NR5 in original schema)
    _reg_nr6: Union[str, None] # Registration number for dog number 6 (REG.NR6 in original schema)
    _reg_nr7: Union[str, None] # Registration number for dog number 7 (REG.NR7 in original schema)
    _reg_nr8: Union[str, None] # Registration number for dog number 8 (REG.NR8 in original schema)
    _reg_nr9: Union[str, None] # Registration number for dog number 9 (REG.NR9 in original schema)
    _reg_nr10: Union[str, None] # Registration number for dog number 10 (REG.NR10 in original schema)
    _reg_nr11: Union[str, None] # Registration number for dog number 11 (REG.NR11 in original schema)
    _reg_nr12: Union[str, None] # Registration number for dog number 12 (REG.NR12 in original schema)
    _reg_nr13: Union[str, None] # Registration number for dog number 13 (REG.NR13 in original schema)
    _reg_nr14: Union[str, None] # Registration number for dog number 14 (REG.NR14 in original schema)

    def __init__(self, kullb: Union[str, None], kennel: Union[str, None], kullnr: str
               , fodt: Union[date, None], fodt_raw: Union[str, None], fd_land_id: int, oppdr: Union[str, None]
               , adresse: Union[str, None], postnr: Union[str, None], farens_reg_nr: Union[str, None]
               , morfars_reg_nr: Union[str, None], morens_reg_nr: Union[str, None], sosken: Union[str, None]
               , innavl: Union[str, None], merkn: Union[str, None], ant: Union[int, None]
               , h: Union[int, None], t: Union[int, None], utmrkber: Union[int, None]
               , friber: Union[int, None], svakber: Union[int, None], middelsber: Union[int, None]
               , sterkber: Union[int, None], utmrk: Union[int, None], fri: Union[int, None]
               , svak: Union[int, None], middels: Union[int, None], sterk: Union[int, None]
               , ro: Union[int, None], tothd: Union[int, None], friberad: Union[int, None]
               , svakberad: Union[int, None], middelsberad: Union[int, None], sterkberad: Union[int, None]
               , friad: Union[int, None], svakad: Union[int, None], middelsad: Union[int, None]
               , sterkad: Union[int, None], road: Union[int, None], totad: Union[int, None]
               , reg_nr1: Union[str, None], reg_nr2: Union[str, None], reg_nr3: Union[str, None]
               , reg_nr4: Union[str, None], reg_nr5: Union[str, None], reg_nr6: Union[str, None]
               , reg_nr7: Union[str, None], reg_nr8: Union[str, None], reg_nr9: Union[str, None]
               , reg_nr10: Union[str, None], reg_nr11: Union[str, None], reg_nr12: Union[str, None]
               , reg_nr13: Union[str, None], reg_nr14: Union[str, None]) -> None:
        self._kullb = kullb
        self._kennel = kennel
        self._kullnr = kullnr
        self._fodt = fodt
        self._fodt_raw = fodt_raw
        self._fd_land_id = fd_land_id
        self._oppdr = oppdr
        self._adresse = adresse
        self._postnr = postnr
        self._farens_reg_nr = farens_reg_nr
        self._morfars_reg_nr = morfars_reg_nr
        self._morens_reg_nr = morens_reg_nr
        self._sosken = sosken
        self._innavl = innavl
        self._merkn = merkn
        self._ant = ant
        self._h = h
        self._t = t
        self._utmrkber = utmrkber
        self._friber = friber
        self._svakber = svakber
        self._middelsber = middelsber
        self._sterkber = sterkber
        self._utmrk = utmrk
        self._fri = fri
        self._svak = svak
        self._middels = middels
        self._sterk = sterk
        self._ro = ro
        self._tothd = tothd
        self._friberad = friberad
        self._svakberad = svakberad
        self._middelsberad = middelsberad
        self._sterkberad = sterkberad
        self._friad = friad
        self._svakad = svakad
        self._middelsad = middelsad
        self._sterkad = sterkad
        self._road = road
        self._totad = totad
        self._reg_nr1 = reg_nr1
        self._reg_nr2 = reg_nr2
        self._reg_nr3 = reg_nr3
        self._reg_nr4 = reg_nr4
        self._reg_nr5 = reg_nr5
        self._reg_nr6 = reg_nr6
        self._reg_nr7 = reg_nr7
        self._reg_nr8 = reg_nr8
        self._reg_nr9 = reg_nr9
        self._reg_nr10 = reg_nr10
        self._reg_nr11 = reg_nr11
        self._reg_nr12 = reg_nr12
        self._reg_nr13 = reg_nr13
        self._reg_nr14 = reg_nr14

    @classmethod
    def from_bytes(cls, content: bytes):
        if len(content) != 844:
            raise AssertionError("Input for Kull should be 844 bytes")

        # The litter table contains a 16 byte header that does not contain useful data
        # Remove used data from next entries
        sub_content = content[16:]

        # Parse the KULLB property
        kullb = graceful_conversion(sub_content[:1]) # KULLB (Litter letter is a string capped at 1 characters)
        # Remove used data from next entries
        sub_content = sub_content[1:]

        # Parse the KENNEL property
        kennel = graceful_conversion(sub_content[:32]) # KENNEL (Kennel is a string capped at 32 characters)
        # Remove used data from next entries
        sub_content = sub_content[32:]

        # Parse the KULLNR property
        kullnr = graceful_conversion(sub_content[:5]) # KULLNR (Litter number/identifier is a string capped at 5 characters)
        # Remove used data from next entries
        sub_content = sub_content[5:]

        # Parse the FØDT property
        fodt = None
        fodt_raw = graceful_conversion(sub_content[:6])
        try:
            fodt = date_conversion(sub_content[:6]) # FØDT (Birthdate is represented by a 6 digit numerical string)
        except ValueError as e:
            print(e)        # Remove used data from next entries
        sub_content = sub_content[6:]

        # Parse the FD-LAND property
        fd_land_id = sub_content[0] # FD-LAND (Birth country index is an enum represented by a 1 byte integer)
        # Remove used data from next entries
        sub_content = sub_content[1:]

        # Parse the OPPDR property
        oppdr = graceful_conversion(sub_content[:60]) # OPPDR (Breeder is a string capped at 60 characters)
        # Remove used data from next entries
        sub_content = sub_content[60:]

        # Parse the ADRESSE property
        adresse = graceful_conversion(sub_content[:35]) # ADRESSE (Address is a string capped at 35 characters)
        # Remove used data from next entries
        sub_content = sub_content[35:]

        # Parse the POSTNR property
        postnr = graceful_conversion(sub_content[:7]) # POSTNR (Postal code is a string capped at 7 characters)
        # Remove used data from next entries
        sub_content = sub_content[7:]

        # Parse the FARENS REG.NR property
        farens_reg_nr = graceful_conversion(sub_content[:12]) # FARENS REG.NR (Fathers registration number is a string capped at 12 characters)
        # Remove used data from next entries
        sub_content = sub_content[12:]

        # Parse the MORFARS REG.NR property
        morfars_reg_nr = graceful_conversion(sub_content[:12]) # MORFARS REG.NR (Grandfathers registration number is a string capped at 12 characters)
        # Remove used data from next entries
        sub_content = sub_content[12:]

        # Parse the MORENS REG.NR property
        morens_reg_nr = graceful_conversion(sub_content[:12]) # MORENS REG.NR (Mothers registration number is a string capped at 12 characters)
        # Remove used data from next entries
        sub_content = sub_content[12:]

        # Parse the SØSKEN property
        sosken = graceful_conversion(sub_content[:233]) # SØSKEN (Siblings is a string capped at 233 characters)
        # Remove used data from next entries
        sub_content = sub_content[233:]

        # Parse the INNAVL property
        innavl = graceful_conversion(sub_content[:153]) # INNAVL (Inbreeding is a string capped at 153 characters)
        # Remove used data from next entries
        sub_content = sub_content[153:]

        # Parse the MERKN property
        merkn = graceful_conversion(sub_content[:66]) # MERKN (Remarks is a string capped at 66 characters)
        # Remove used data from next entries
        sub_content = sub_content[66:]

        # Parse the ANT property
        ant = sub_content[0] # ANT (Number is a 1 byte integer)
        ant = None if ant == 128 else ant # Set to python None if value indicates null
        # Remove used data from next entries
        sub_content = sub_content[1:]

        # Parse the H property
        h = sub_content[0] # H (H? is a 1 byte integer)
        h = None if h == 128 else h # Set to python None if value indicates null
        # Remove used data from next entries
        sub_content = sub_content[1:]

        # Parse the T property
        t = sub_content[0] # T (T? is a 1 byte integer)
        t = None if t == 128 else t # Set to python None if value indicates null
        # Remove used data from next entries
        sub_content = sub_content[1:]

        # Parse the UTMRKBER property
        utmrkber = sub_content[0] # UTMRKBER (UTMRKBER? is a 1 byte integer)
        utmrkber = None if utmrkber == 128 else utmrkber # Set to python None if value indicates null
        # Remove used data from next entries
        sub_content = sub_content[1:]

        # Parse the FRIBER property
        friber = sub_content[0] # FRIBER (FRIBER? is a 1 byte integer)
        friber = None if friber == 128 else friber # Set to python None if value indicates null
        # Remove used data from next entries
        sub_content = sub_content[1:]

        # Parse the SVAKBER property
        svakber = sub_content[0] # SVAKBER (SVAKBER? is a 1 byte integer)
        svakber = None if svakber == 128 else svakber # Set to python None if value indicates null
        # Remove used data from next entries
        sub_content = sub_content[1:]

        # Parse the MIDDELSBER property
        middelsber = sub_content[0] # MIDDELSBER (MIDDELSBER? is a 1 byte integer)
        middelsber = None if middelsber == 128 else middelsber # Set to python None if value indicates null
        # Remove used data from next entries
        sub_content = sub_content[1:]

        # Parse the STERKBER property
        sterkber = sub_content[0] # STERKBER (STERKBER? is a 1 byte integer)
        sterkber = None if sterkber == 128 else sterkber # Set to python None if value indicates null
        # Remove used data from next entries
        sub_content = sub_content[1:]

        # Parse the UTMRK property
        utmrk = sub_content[0] # UTMRK (UTMRK? is a 1 byte integer)
        utmrk = None if utmrk == 128 else utmrk # Set to python None if value indicates null
        # Remove used data from next entries
        sub_content = sub_content[1:]

        # Parse the FRI property
        fri = sub_content[0] # FRI (FRI? is a 1 byte integer)
        fri = None if fri == 128 else fri # Set to python None if value indicates null
        # Remove used data from next entries
        sub_content = sub_content[1:]

        # Parse the SVAK property
        svak = sub_content[0] # SVAK (SVAK? is a 1 byte integer)
        svak = None if svak == 128 else svak # Set to python None if value indicates null
        # Remove used data from next entries
        sub_content = sub_content[1:]

        # Parse the MIDDELS property
        middels = sub_content[0] # MIDDELS (MIDDELS? is a 1 byte integer)
        middels = None if middels == 128 else middels # Set to python None if value indicates null
        # Remove used data from next entries
        sub_content = sub_content[1:]

        # Parse the STERK property
        sterk = sub_content[0] # STERK (STERK? is a 1 byte integer)
        sterk = None if sterk == 128 else sterk # Set to python None if value indicates null
        # Remove used data from next entries
        sub_content = sub_content[1:]

        # Parse the RØ property
        ro = sub_content[0] # RØ (RØ? is a 1 byte integer)
        ro = None if ro == 128 else ro # Set to python None if value indicates null
        # Remove used data from next entries
        sub_content = sub_content[1:]

        # Parse the TOTHD property
        tothd = sub_content[0] # TOTHD (TOTHD? is a 1 byte integer)
        tothd = None if tothd == 128 else tothd # Set to python None if value indicates null
        # Remove used data from next entries
        sub_content = sub_content[1:]

        # Parse the FRIBERAD property
        friberad = sub_content[0] # FRIBERAD (FRIBERAD? is a 1 byte integer)
        friberad = None if friberad == 128 else friberad # Set to python None if value indicates null
        # Remove used data from next entries
        sub_content = sub_content[1:]

        # Parse the SVAKBERAD property
        svakberad = sub_content[0] # SVAKBERAD (SVAKBERAD? is a 1 byte integer)
        svakberad = None if svakberad == 128 else svakberad # Set to python None if value indicates null
        # Remove used data from next entries
        sub_content = sub_content[1:]

        # Parse the MIDDELSBERAD property
        middelsberad = sub_content[0] # MIDDELSBERAD (MIDDELSBERAD? is a 1 byte integer)
        middelsberad = None if middelsberad == 128 else middelsberad # Set to python None if value indicates null
        # Remove used data from next entries
        sub_content = sub_content[1:]

        # Parse the STERKBERAD property
        sterkberad = sub_content[0] # STERKBERAD (STERKBERAD? is a 1 byte integer)
        sterkberad = None if sterkberad == 128 else sterkberad # Set to python None if value indicates null
        # Remove used data from next entries
        sub_content = sub_content[1:]

        # Parse the FRIAD property
        friad = sub_content[0] # FRIAD (FRIAD? is a 1 byte integer)
        friad = None if friad == 128 else friad # Set to python None if value indicates null
        # Remove used data from next entries
        sub_content = sub_content[1:]

        # Parse the SVAKAD property
        svakad = sub_content[0] # SVAKAD (SVAKAD? is a 1 byte integer)
        svakad = None if svakad == 128 else svakad # Set to python None if value indicates null
        # Remove used data from next entries
        sub_content = sub_content[1:]

        # Parse the MIDDELSAD property
        middelsad = sub_content[0] # MIDDELSAD (MIDDELSAD? is a 1 byte integer)
        middelsad = None if middelsad == 128 else middelsad # Set to python None if value indicates null
        # Remove used data from next entries
        sub_content = sub_content[1:]

        # Parse the STERKAD property
        sterkad = sub_content[0] # STERKAD (STERKAD? is a 1 byte integer)
        sterkad = None if sterkad == 128 else sterkad # Set to python None if value indicates null
        # Remove used data from next entries
        sub_content = sub_content[1:]

        # Parse the RØAD property
        road = sub_content[0] # RØAD (RØAD? is a 1 byte integer)
        road = None if road == 128 else road # Set to python None if value indicates null
        # Remove used data from next entries
        sub_content = sub_content[1:]

        # Parse the TOTAD property
        totad = sub_content[0] # TOTAD (TOTAD? is a 1 byte integer)
        totad = None if totad == 128 else totad # Set to python None if value indicates null
        # Remove used data from next entries
        sub_content = sub_content[1:]

        # Parse the REG.NR1 property
        reg_nr1 = graceful_conversion(sub_content[:12]) # REG.NR1 (Registration number for dog number 1 is a string capped at 12 characters)
        # Remove used data from next entries
        sub_content = sub_content[12:]

        # Parse the REG.NR2 property
        reg_nr2 = graceful_conversion(sub_content[:12]) # REG.NR2 (Registration number for dog number 2 is a string capped at 12 characters)
        # Remove used data from next entries
        sub_content = sub_content[12:]

        # Parse the REG.NR3 property
        reg_nr3 = graceful_conversion(sub_content[:12]) # REG.NR3 (Registration number for dog number 3 is a string capped at 12 characters)
        # Remove used data from next entries
        sub_content = sub_content[12:]

        # Parse the REG.NR4 property
        reg_nr4 = graceful_conversion(sub_content[:12]) # REG.NR4 (Registration number for dog number 4 is a string capped at 12 characters)
        # Remove used data from next entries
        sub_content = sub_content[12:]

        # Parse the REG.NR5 property
        reg_nr5 = graceful_conversion(sub_content[:12]) # REG.NR5 (Registration number for dog number 5 is a string capped at 12 characters)
        # Remove used data from next entries
        sub_content = sub_content[12:]

        # Parse the REG.NR6 property
        reg_nr6 = graceful_conversion(sub_content[:12]) # REG.NR6 (Registration number for dog number 6 is a string capped at 12 characters)
        # Remove used data from next entries
        sub_content = sub_content[12:]

        # Parse the REG.NR7 property
        reg_nr7 = graceful_conversion(sub_content[:12]) # REG.NR7 (Registration number for dog number 7 is a string capped at 12 characters)
        # Remove used data from next entries
        sub_content = sub_content[12:]

        # Parse the REG.NR8 property
        reg_nr8 = graceful_conversion(sub_content[:12]) # REG.NR8 (Registration number for dog number 8 is a string capped at 12 characters)
        # Remove used data from next entries
        sub_content = sub_content[12:]

        # Parse the REG.NR9 property
        reg_nr9 = graceful_conversion(sub_content[:12]) # REG.NR9 (Registration number for dog number 9 is a string capped at 12 characters)
        # Remove used data from next entries
        sub_content = sub_content[12:]

        # Parse the REG.NR10 property
        reg_nr10 = graceful_conversion(sub_content[:12]) # REG.NR10 (Registration number for dog number 10 is a string capped at 12 characters)
        # Remove used data from next entries
        sub_content = sub_content[12:]

        # Parse the REG.NR11 property
        reg_nr11 = graceful_conversion(sub_content[:12]) # REG.NR11 (Registration number for dog number 11 is a string capped at 12 characters)
        # Remove used data from next entries
        sub_content = sub_content[12:]

        # Parse the REG.NR12 property
        reg_nr12 = graceful_conversion(sub_content[:12]) # REG.NR12 (Registration number for dog number 12 is a string capped at 12 characters)
        # Remove used data from next entries
        sub_content = sub_content[12:]

        # Parse the REG.NR13 property
        reg_nr13 = graceful_conversion(sub_content[:12]) # REG.NR13 (Registration number for dog number 13 is a string capped at 12 characters)
        # Remove used data from next entries
        sub_content = sub_content[12:]

        # Parse the REG.NR14 property
        reg_nr14 = graceful_conversion(sub_content[:12]) # REG.NR14 (Registration number for dog number 14 is a string capped at 12 characters)
        # Remove used data from next entries
        sub_content = sub_content[12:]

        return cls(kullb=kullb,
                   kennel=kennel,
                   kullnr=kullnr,
                   fodt=fodt,
                   fodt_raw=fodt_raw,
                   fd_land_id=fd_land_id,
                   oppdr=oppdr,
                   adresse=adresse,
                   postnr=postnr,
                   farens_reg_nr=farens_reg_nr,
                   morfars_reg_nr=morfars_reg_nr,
                   morens_reg_nr=morens_reg_nr,
                   sosken=sosken,
                   innavl=innavl,
                   merkn=merkn,
                   ant=ant,
                   h=h,
                   t=t,
                   utmrkber=utmrkber,
                   friber=friber,
                   svakber=svakber,
                   middelsber=middelsber,
                   sterkber=sterkber,
                   utmrk=utmrk,
                   fri=fri,
                   svak=svak,
                   middels=middels,
                   sterk=sterk,
                   ro=ro,
                   tothd=tothd,
                   friberad=friberad,
                   svakberad=svakberad,
                   middelsberad=middelsberad,
                   sterkberad=sterkberad,
                   friad=friad,
                   svakad=svakad,
                   middelsad=middelsad,
                   sterkad=sterkad,
                   road=road,
                   totad=totad,
                   reg_nr1=reg_nr1,
                   reg_nr2=reg_nr2,
                   reg_nr3=reg_nr3,
                   reg_nr4=reg_nr4,
                   reg_nr5=reg_nr5,
                   reg_nr6=reg_nr6,
                   reg_nr7=reg_nr7,
                   reg_nr8=reg_nr8,
                   reg_nr9=reg_nr9,
                   reg_nr10=reg_nr10,
                   reg_nr11=reg_nr11,
                   reg_nr12=reg_nr12,
                   reg_nr13=reg_nr13,
                   reg_nr14=reg_nr14)

    @property
    def kullb(self) -> Union[str, None]:
        return None if not self._kullb else self._kullb

    @property
    def kennel(self) -> Union[str, None]:
        return None if not self._kennel else self._kennel

    @property
    def kullnr(self) -> str:
        return self._kullnr

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
    def farens_reg_nr(self) -> Union[str, None]:
        return None if not self._farens_reg_nr else self._farens_reg_nr

    @property
    def morfars_reg_nr(self) -> Union[str, None]:
        return None if not self._morfars_reg_nr else self._morfars_reg_nr

    @property
    def morens_reg_nr(self) -> Union[str, None]:
        return None if not self._morens_reg_nr else self._morens_reg_nr

    @property
    def sosken(self) -> Union[str, None]:
        return None if not self._sosken else self._sosken

    @property
    def innavl(self) -> Union[str, None]:
        return None if not self._innavl else self._innavl

    @property
    def merkn(self) -> Union[str, None]:
        return None if not self._merkn else self._merkn

    @property
    def ant(self) -> Union[int, None]:
        return None if not self._ant else self._ant

    @property
    def h(self) -> Union[int, None]:
        return None if not self._h else self._h

    @property
    def t(self) -> Union[int, None]:
        return None if not self._t else self._t

    @property
    def utmrkber(self) -> Union[int, None]:
        return None if not self._utmrkber else self._utmrkber

    @property
    def friber(self) -> Union[int, None]:
        return None if not self._friber else self._friber

    @property
    def svakber(self) -> Union[int, None]:
        return None if not self._svakber else self._svakber

    @property
    def middelsber(self) -> Union[int, None]:
        return None if not self._middelsber else self._middelsber

    @property
    def sterkber(self) -> Union[int, None]:
        return None if not self._sterkber else self._sterkber

    @property
    def utmrk(self) -> Union[int, None]:
        return None if not self._utmrk else self._utmrk

    @property
    def fri(self) -> Union[int, None]:
        return None if not self._fri else self._fri

    @property
    def svak(self) -> Union[int, None]:
        return None if not self._svak else self._svak

    @property
    def middels(self) -> Union[int, None]:
        return None if not self._middels else self._middels

    @property
    def sterk(self) -> Union[int, None]:
        return None if not self._sterk else self._sterk

    @property
    def ro(self) -> Union[int, None]:
        return None if not self._ro else self._ro

    @property
    def tothd(self) -> Union[int, None]:
        return None if not self._tothd else self._tothd

    @property
    def friberad(self) -> Union[int, None]:
        return None if not self._friberad else self._friberad

    @property
    def svakberad(self) -> Union[int, None]:
        return None if not self._svakberad else self._svakberad

    @property
    def middelsberad(self) -> Union[int, None]:
        return None if not self._middelsberad else self._middelsberad

    @property
    def sterkberad(self) -> Union[int, None]:
        return None if not self._sterkberad else self._sterkberad

    @property
    def friad(self) -> Union[int, None]:
        return None if not self._friad else self._friad

    @property
    def svakad(self) -> Union[int, None]:
        return None if not self._svakad else self._svakad

    @property
    def middelsad(self) -> Union[int, None]:
        return None if not self._middelsad else self._middelsad

    @property
    def sterkad(self) -> Union[int, None]:
        return None if not self._sterkad else self._sterkad

    @property
    def road(self) -> Union[int, None]:
        return None if not self._road else self._road

    @property
    def totad(self) -> Union[int, None]:
        return None if not self._totad else self._totad

    @property
    def reg_nr1(self) -> Union[str, None]:
        return None if not self._reg_nr1 else self._reg_nr1

    @property
    def reg_nr2(self) -> Union[str, None]:
        return None if not self._reg_nr2 else self._reg_nr2

    @property
    def reg_nr3(self) -> Union[str, None]:
        return None if not self._reg_nr3 else self._reg_nr3

    @property
    def reg_nr4(self) -> Union[str, None]:
        return None if not self._reg_nr4 else self._reg_nr4

    @property
    def reg_nr5(self) -> Union[str, None]:
        return None if not self._reg_nr5 else self._reg_nr5

    @property
    def reg_nr6(self) -> Union[str, None]:
        return None if not self._reg_nr6 else self._reg_nr6

    @property
    def reg_nr7(self) -> Union[str, None]:
        return None if not self._reg_nr7 else self._reg_nr7

    @property
    def reg_nr8(self) -> Union[str, None]:
        return None if not self._reg_nr8 else self._reg_nr8

    @property
    def reg_nr9(self) -> Union[str, None]:
        return None if not self._reg_nr9 else self._reg_nr9

    @property
    def reg_nr10(self) -> Union[str, None]:
        return None if not self._reg_nr10 else self._reg_nr10

    @property
    def reg_nr11(self) -> Union[str, None]:
        return None if not self._reg_nr11 else self._reg_nr11

    @property
    def reg_nr12(self) -> Union[str, None]:
        return None if not self._reg_nr12 else self._reg_nr12

    @property
    def reg_nr13(self) -> Union[str, None]:
        return None if not self._reg_nr13 else self._reg_nr13

    @property
    def reg_nr14(self) -> Union[str, None]:
        return None if not self._reg_nr14 else self._reg_nr14

    @property
    def native(self) -> dict:
        """Method converts class instance to native python classes for serialization purposes"""

        obj_dict = {
            'kullb': self.kullb,
            'kennel': self.kennel,
            'kullnr': self.kullnr,
            'fodt': self.fodt_str,
            'fodt_raw': self.fodt_raw,
            'fd_land_id': self.fd_land_id,
            'oppdr': self.oppdr,
            'adresse': self.adresse,
            'postnr': self.postnr,
            'farens_reg_nr': self.farens_reg_nr,
            'morfars_reg_nr': self.morfars_reg_nr,
            'morens_reg_nr': self.morens_reg_nr,
            'sosken': self.sosken,
            'innavl': self.innavl,
            'merkn': self.merkn,
            'ant': self.ant,
            'h': self.h,
            't': self.t,
            'utmrkber': self.utmrkber,
            'friber': self.friber,
            'svakber': self.svakber,
            'middelsber': self.middelsber,
            'sterkber': self.sterkber,
            'utmrk': self.utmrk,
            'fri': self.fri,
            'svak': self.svak,
            'middels': self.middels,
            'sterk': self.sterk,
            'ro': self.ro,
            'tothd': self.tothd,
            'friberad': self.friberad,
            'svakberad': self.svakberad,
            'middelsberad': self.middelsberad,
            'sterkberad': self.sterkberad,
            'friad': self.friad,
            'svakad': self.svakad,
            'middelsad': self.middelsad,
            'sterkad': self.sterkad,
            'road': self.road,
            'totad': self.totad,
            'reg_nr1': self.reg_nr1,
            'reg_nr2': self.reg_nr2,
            'reg_nr3': self.reg_nr3,
            'reg_nr4': self.reg_nr4,
            'reg_nr5': self.reg_nr5,
            'reg_nr6': self.reg_nr6,
            'reg_nr7': self.reg_nr7,
            'reg_nr8': self.reg_nr8,
            'reg_nr9': self.reg_nr9,
            'reg_nr10': self.reg_nr10,
            'reg_nr11': self.reg_nr11,
            'reg_nr12': self.reg_nr12,
            'reg_nr13': self.reg_nr13,
            'reg_nr14': self.reg_nr14,
        }

        return obj_dict

class KullList:

    _contents: List[Kull]

    def __init__(self, contents:List[Kull]=[]) -> None:
        self._contents = contents
    
    @property
    def native(self) -> dict:
        """Method converts class instance to native python classes for serialization purposes"""

        return [i.native for i in self._contents]
