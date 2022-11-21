from typing import List, Union
from datetime import date

from ...utils import graceful_conversion, date_conversion

class TysKull:

    _kullb: Union[str, None] # The litter letter (KULLB in original schema)
    _kennel: Union[str, None] # The kennel that the litter was born to (KENNEL in original schema)
    _fodt: Union[date, None] # The date that the litter was born (FØDT in original schema)
    _kullnr: Union[str, None] # The litter identifier (KULLNR in original schema)

    _farens_reg_nr: str # Fathers registration number (FARENS REG.NR in original schema)
    _farens_navn: str #Fathers name (FARENS NAVN in original schema)

    _morens_reg_nr: str # Mothers registration number (MORENS REG.NR in original schema)
    _morens_navn: str # Mothers name (MORENS NAVN in original schema)

    _alle_id: int # Identifier for enum/boolean specifying if the litter information is omplete (ALLE in original schema)

    _sosken: Union[str, None] # Sibling list (SØSKEN in original schema)

    # Siblings
    _hund1: Union[str, None] # The name of the sibling (HUNDX in the original schema)
    _kj1_id: int # The sex identifier of the sibling (KJX in the original schema)
    _k1_id: int # The k identifier of the sibling (KX in the original schema)
    _m1_id: int # The award identifier of the sibling (MX in the original schema)
    _hd1_id: int # The hd identifier of the sibling (HDX in the original schema)

    _hund2: Union[str, None] # The name of the sibling (HUNDX in the original schema)
    _kj2_id: int # The sex identifier of the sibling (KJX in the original schema)
    _k2_id: int # The k identifier of the sibling (KX in the original schema)
    _m2_id: int # The award identifier of the sibling (MX in the original schema)
    _hd2_id: int # The hd identifier of the sibling (HDX in the original schema)

    _hund3: Union[str, None] # The name of the sibling (HUNDX in the original schema)
    _kj3_id: int # The sex identifier of the sibling (KJX in the original schema)
    _k3_id: int # The k identifier of the sibling (KX in the original schema)
    _m3_id: int # The award identifier of the sibling (MX in the original schema)
    _hd3_id: int # The hd identifier of the sibling (HDX in the original schema)

    _hund4: Union[str, None] # The name of the sibling (HUNDX in the original schema)
    _kj4_id: int # The sex identifier of the sibling (KJX in the original schema)
    _k4_id: int # The k identifier of the sibling (KX in the original schema)
    _m4_id: int # The award identifier of the sibling (MX in the original schema)
    _hd4_id: int # The hd identifier of the sibling (HDX in the original schema)

    _hund5: Union[str, None] # The name of the sibling (HUNDX in the original schema)
    _kj5_id: int # The sex identifier of the sibling (KJX in the original schema)
    _k5_id: int # The k identifier of the sibling (KX in the original schema)
    _m5_id: int # The award identifier of the sibling (MX in the original schema)
    _hd5_id: int # The hd identifier of the sibling (HDX in the original schema)

    _hund6: Union[str, None] # The name of the sibling (HUNDX in the original schema)
    _kj6_id: int # The sex identifier of the sibling (KJX in the original schema)
    _k6_id: int # The k identifier of the sibling (KX in the original schema)
    _m6_id: int # The award identifier of the sibling (MX in the original schema)
    _hd6_id: int # The hd identifier of the sibling (HDX in the original schema)

    _hund7: Union[str, None] # The name of the sibling (HUNDX in the original schema)
    _kj7_id: int # The sex identifier of the sibling (KJX in the original schema)
    _k7_id: int # The k identifier of the sibling (KX in the original schema)
    _m7_id: int # The award identifier of the sibling (MX in the original schema)
    _hd7_id: int # The hd identifier of the sibling (HDX in the original schema)

    _hund8: Union[str, None] # The name of the sibling (HUNDX in the original schema)
    _kj8_id: int # The sex identifier of the sibling (KJX in the original schema)
    _k8_id: int # The k identifier of the sibling (KX in the original schema)
    _m8_id: int # The award identifier of the sibling (MX in the original schema)
    _hd8_id: int # The hd identifier of the sibling (HDX in the original schema)

    _hund9: Union[str, None] # The name of the sibling (HUNDX in the original schema)
    _kj9_id: int # The sex identifier of the sibling (KJX in the original schema)
    _k9_id: int # The k identifier of the sibling (KX in the original schema)
    _m9_id: int # The award identifier of the sibling (MX in the original schema)
    _hd9_id: int # The hd identifier of the sibling (HDX in the original schema)

    _hund10: Union[str, None] # The name of the sibling (HUNDX in the original schema)
    _kj10_id: int # The sex identifier of the sibling (KJX in the original schema)
    _k10_id: int # The k identifier of the sibling (KX in the original schema)
    _m10_id: int # The award identifier of the sibling (MX in the original schema)
    _hd10_id: int # The hd identifier of the sibling (HDX in the original schema)

    _hund11: Union[str, None] # The name of the sibling (HUNDX in the original schema)
    _kj11_id: int # The sex identifier of the sibling (KJX in the original schema)
    _k11_id: int # The k identifier of the sibling (KX in the original schema)
    _m11_id: int # The award identifier of the sibling (MX in the original schema)
    _hd11_id: int # The hd identifier of the sibling (HDX in the original schema)

    _hund12: Union[str, None] # The name of the sibling (HUNDX in the original schema)
    _kj12_id: int # The sex identifier of the sibling (KJX in the original schema)
    _k12_id: int # The k identifier of the sibling (KX in the original schema)
    _m12_id: int # The award identifier of the sibling (MX in the original schema)
    _hd12_id: int # The hd identifier of the sibling (HDX in the original schema)

    def __init__(self, alle_id: int,
                 kj1_id: int, k1_id: int, m1_id: int, hd1_id: int,
                 kj2_id: int, k2_id: int, m2_id: int, hd2_id: int,
                 kj3_id: int, k3_id: int, m3_id: int, hd3_id: int,
                 kj4_id: int, k4_id: int, m4_id: int, hd4_id: int,
                 kj5_id: int, k5_id: int, m5_id: int, hd5_id: int,
                 kj6_id: int, k6_id: int, m6_id: int, hd6_id: int,
                 kj7_id: int, k7_id: int, m7_id: int, hd7_id: int,
                 kj8_id: int, k8_id: int, m8_id: int, hd8_id: int,
                 kj9_id: int, k9_id: int, m9_id: int, hd9_id: int,
                 kj10_id: int, k10_id: int, m10_id: int, hd10_id: int,
                 kj11_id: int, k11_id: int, m11_id: int, hd11_id: int,
                 kj12_id: int, k12_id: int, m12_id: int, hd12_id: int,  
                 kullb: Union[str, None] = None,
                 kennel: Union[str, None] = None, fodt: Union[str, None] = None,
                 kullnr: Union[str, None] = None,
                 farens_reg_nr: Union[str, None] = None, farens_navn: Union[str, None] = None,
                 morens_reg_nr: Union[str, None] = None, morens_navn: Union[str, None] = None,
                 sosken: Union[str, None] = None,
                 hund1: Union[str, None] = None, hund2: Union[str, None] = None,
                 hund3: Union[str, None] = None, hund4: Union[str, None] = None,
                 hund5: Union[str, None] = None, hund6: Union[str, None] = None,
                 hund7: Union[str, None] = None, hund8: Union[str, None] = None,
                 hund9: Union[str, None] = None, hund10: Union[str, None] = None,
                 hund11: Union[str, None] = None, hund12: Union[str, None] = None,
                 ) -> None:
        
        self._kullb = kullb
        self._kennel = kennel
        self._fodt = fodt
        self._kullnr = kullnr
        
        self._farens_reg_nr = farens_reg_nr
        self._farens_navn = farens_navn

        self._morens_navn = morens_navn
        self._morens_reg_nr = morens_reg_nr

        self._alle_id = alle_id
        self._sosken = sosken

        # Siblings
        self._hund1 = hund1
        self._kj1_id = kj1_id
        self._k1_id = k1_id
        self._m1_id = m1_id
        self._hd1_id = hd1_id

        self._hund2 = hund2
        self._kj2_id = kj2_id
        self._k2_id = k2_id
        self._m2_id = m2_id
        self._hd2_id = hd2_id

        self._hund3 = hund3
        self._kj3_id = kj3_id
        self._k3_id = k3_id
        self._m3_id = m3_id
        self._hd3_id = hd3_id

        self._hund4 = hund4
        self._kj4_id = kj4_id
        self._k4_id = k4_id
        self._m4_id = m4_id
        self._hd4_id = hd4_id

        self._hund5 = hund5
        self._kj5_id = kj5_id
        self._k5_id = k5_id
        self._m5_id = m5_id
        self._hd5_id = hd5_id

        self._hund6 = hund6
        self._kj6_id = kj6_id
        self._k6_id = k6_id
        self._m6_id = m6_id
        self._hd6_id = hd6_id

        self._hund7 = hund7
        self._kj7_id = kj7_id
        self._k7_id = k7_id
        self._m7_id = m7_id
        self._hd7_id = hd7_id

        self._hund8 = hund8
        self._kj8_id = kj8_id
        self._k8_id = k8_id
        self._m8_id = m8_id
        self._hd8_id = hd8_id

        self._hund9 = hund9
        self._kj9_id = kj9_id
        self._k9_id = k9_id
        self._m9_id = m9_id
        self._hd9_id = hd9_id

        self._hund10 = hund10
        self._kj10_id = kj10_id
        self._k10_id = k10_id
        self._m10_id = m10_id
        self._hd10_id = hd10_id

        self._hund11 = hund11
        self._kj11_id = kj11_id
        self._k11_id = k11_id
        self._m11_id = m11_id
        self._hd11_id = hd11_id

        self._hund12 = hund12
        self._kj12_id = kj12_id
        self._k12_id = k12_id
        self._m12_id = m12_id
        self._hd12_id = hd12_id
    
    @classmethod
    def from_bytes(cls, content: bytes):
        if len(content) != 587:
            raise AssertionError('Input for TysKull should be 250 bytes')
        
        # The german litter table contains a 17 byte header that does not contain usefull data
        header = content[:17]
        sub_content = content

        # Eliminate the already used data and set the next property
        sub_content = sub_content[17:] # 570 bytes remaining
        kullb = graceful_conversion(sub_content[:1]) # KULLB (Litter letter is a string capped at 1 character)

        # Eliminate the already used data and set the next property
        sub_content = sub_content[1:] # 569 bytes remaining
        kennel = graceful_conversion(sub_content[:32]) # KENNEL (Kennel is a string capped at 32 characters)

        # Eliminate the already used data and set the next property
        sub_content = sub_content[32:] # 537 bytes remaining
        fodt = date_conversion(sub_content[:6])  # FØDT (birthdate/født is represented by a 6 digit numerical string)

        # Eliminate the already used data and set the next property
        sub_content = sub_content[6:] # 531 bytes remaining
        kullnr = graceful_conversion(sub_content[:5]) # KULLNR (Litter number/identifier is a string capped at 6 characters)

        # Eliminate the already used data and set the next property
        sub_content = sub_content[5:] # 526 bytes remaining
        farens_reg_nr = graceful_conversion(sub_content[:12]) # FARENS REG.NR (registration number is a string capped at 12 characters)

        # Eliminate the already used data and set the next property
        sub_content = sub_content[12:] # 514 bytes remaining
        farens_navn = graceful_conversion(sub_content[:38]) # FARens_navn (name of father is a string capped at 38 characters)

        # Eliminate the already used data and set the next property
        sub_content = sub_content[38:] # 476 bytes remaining
        morens_reg_nr = graceful_conversion(sub_content[:12]) # MORENS REG.NR (registration number is a string capped at 12 characters)

        # Eliminate the already used data and set the next property
        sub_content = sub_content[12:] # 464 bytes remaining
        morens_navn = graceful_conversion(sub_content[:38]) # MORENS NAVN (name of mother is a string capped at 38 characters)

        # Eliminate the already used data and set the next property
        sub_content = sub_content[38:] # 426 bytes remaining
        alle_id = sub_content[0]# ALLE index

        # Eliminate the already used data and set the next property
        sub_content = sub_content[1:] # 425 bytes remaining
        sosken = graceful_conversion(sub_content[:233]) # SIBLINGS (sibling information is a string capped at 233 characters)

        # Siblings 192 bytes remaining

        # Eliminate the already used data and set the next property
        sub_content = sub_content[233:]
        hund1 = graceful_conversion(sub_content[:12]) # HUND1 (Individual dog name is a string capped at 12 characters)

        # Eliminate the already used data and set the next property
        sub_content = sub_content[12:]
        kj1_id = sub_content[0]# KJ1 index

        # Eliminate the already used data and set the next property
        sub_content = sub_content[1:]
        k1_id = sub_content[0]# K1 index

        # Eliminate the already used data and set the next property
        sub_content = sub_content[1:]
        m1_id = sub_content[0]# M1 index

        # Eliminate the already used data and set the next property
        sub_content = sub_content[1:]
        hd1_id = sub_content[0]# HD1 index

        # Eliminate the already used data and set the next property
        sub_content = sub_content[1:]
        hund2 = graceful_conversion(sub_content[:12]) # HUND2 (Individual dog name is a string capped at 12 characters)

        # Eliminate the already used data and set the next property
        sub_content = sub_content[12:]
        kj2_id = sub_content[0]# KJ2 index

        # Eliminate the already used data and set the next property
        sub_content = sub_content[1:]
        k2_id = sub_content[0]# K2 index

        # Eliminate the already used data and set the next property
        sub_content = sub_content[1:]
        m2_id = sub_content[0]# M2 index

        # Eliminate the already used data and set the next property
        sub_content = sub_content[1:]
        hd2_id = sub_content[0]# HD2 index

        # Eliminate the already used data and set the next property
        sub_content = sub_content[1:]
        hund3 = graceful_conversion(sub_content[:12]) # HUND3 (Individual dog name is a string capped at 12 characters)

        # Eliminate the already used data and set the next property
        sub_content = sub_content[12:]
        kj3_id = sub_content[0]# KJ3 index

        # Eliminate the already used data and set the next property
        sub_content = sub_content[1:]
        k3_id = sub_content[0]# K3 index

        # Eliminate the already used data and set the next property
        sub_content = sub_content[1:]
        m3_id = sub_content[0]# M3 index

        # Eliminate the already used data and set the next property
        sub_content = sub_content[1:]
        hd3_id = sub_content[0]# HD3 index

        # Eliminate the already used data and set the next property
        sub_content = sub_content[1:]
        hund4 = graceful_conversion(sub_content[:12]) # HUND4 (Individual dog name is a string capped at 12 characters)

        # Eliminate the already used data and set the next property
        sub_content = sub_content[12:]
        kj4_id = sub_content[0]# KJ4 index

        # Eliminate the already used data and set the next property
        sub_content = sub_content[1:]
        k4_id = sub_content[0]# K4 index

        # Eliminate the already used data and set the next property
        sub_content = sub_content[1:]
        m4_id = sub_content[0]# M4 index

        # Eliminate the already used data and set the next property
        sub_content = sub_content[1:]
        hd4_id = sub_content[0]# HD4 index

        # Eliminate the already used data and set the next property
        sub_content = sub_content[1:]
        hund5 = graceful_conversion(sub_content[:12]) # HUND5 (Individual dog name is a string capped at 12 characters)

        # Eliminate the already used data and set the next property
        sub_content = sub_content[12:]
        kj5_id = sub_content[0]# KJ5 index

        # Eliminate the already used data and set the next property
        sub_content = sub_content[1:]
        k5_id = sub_content[0]# K5 index

        # Eliminate the already used data and set the next property
        sub_content = sub_content[1:]
        m5_id = sub_content[0]# M5 index

        # Eliminate the already used data and set the next property
        sub_content = sub_content[1:]
        hd5_id = sub_content[0]# HD5 index

        # Eliminate the already used data and set the next property
        sub_content = sub_content[1:]
        hund6 = graceful_conversion(sub_content[:12]) # HUND6 (Individual dog name is a string capped at 12 characters)

        # Eliminate the already used data and set the next property
        sub_content = sub_content[12:]
        kj6_id = sub_content[0]# KJ6 index

        # Eliminate the already used data and set the next property
        sub_content = sub_content[1:]
        k6_id = sub_content[0]# K6 index

        # Eliminate the already used data and set the next property
        sub_content = sub_content[1:]
        m6_id = sub_content[0]# M6 index

        # Eliminate the already used data and set the next property
        sub_content = sub_content[1:]
        hd6_id = sub_content[0]# HD6 index

        # Eliminate the already used data and set the next property
        sub_content = sub_content[1:]
        hund7 = graceful_conversion(sub_content[:12]) # HUND7 (Individual dog name is a string capped at 12 characters)

        # Eliminate the already used data and set the next property
        sub_content = sub_content[12:]
        kj7_id = sub_content[0]# KJ7 index

        # Eliminate the already used data and set the next property
        sub_content = sub_content[1:]
        k7_id = sub_content[0]# K7 index

        # Eliminate the already used data and set the next property
        sub_content = sub_content[1:]
        m7_id = sub_content[0]# M7 index

        # Eliminate the already used data and set the next property
        sub_content = sub_content[1:] 
        hd7_id = sub_content[0]# HD7 index

        # Eliminate the already used data and set the next property
        sub_content = sub_content[1:]
        hund8 = graceful_conversion(sub_content[:12]) # HUND8 (Individual dog name is a string capped at 12 characters)

        # Eliminate the already used data and set the next property
        sub_content = sub_content[12:] 
        kj8_id = sub_content[0]# KJ8 index

        # Eliminate the already used data and set the next property
        sub_content = sub_content[1:] 
        k8_id = sub_content[0]# K8 index

        # Eliminate the already used data and set the next property
        sub_content = sub_content[1:] 
        m8_id = sub_content[0]# M8 index

        # Eliminate the already used data and set the next property
        sub_content = sub_content[1:] 
        hd8_id = sub_content[0]# HD8 index

        # Eliminate the already used data and set the next property
        sub_content = sub_content[1:]
        hund9 = graceful_conversion(sub_content[:12]) # HUND9 (Individual dog name is a string capped at 12 characters)

        # Eliminate the already used data and set the next property
        sub_content = sub_content[12:] 
        kj9_id = sub_content[0]# KJ9 index

        # Eliminate the already used data and set the next property
        sub_content = sub_content[1:] 
        k9_id = sub_content[0]# K9 index

        # Eliminate the already used data and set the next property
        sub_content = sub_content[1:] 
        m9_id = sub_content[0]# M9 index

        # Eliminate the already used data and set the next property
        sub_content = sub_content[1:]
        hd9_id = sub_content[0]# HD9 index

        # Eliminate the already used data and set the next property
        sub_content = sub_content[1:]
        hund10 = graceful_conversion(sub_content[:12]) # HUND10 (Individual dog name is a string capped at 12 characters)

        # Eliminate the already used data and set the next property
        sub_content = sub_content[12:]
        kj10_id = sub_content[0]# KJ10 index

        # Eliminate the already used data and set the next property
        sub_content = sub_content[1:]
        k10_id = sub_content[0]# K10 index

        # Eliminate the already used data and set the next property
        sub_content = sub_content[1:]
        m10_id = sub_content[0]# M10 index

        # Eliminate the already used data and set the next property
        sub_content = sub_content[1:]
        hd10_id = sub_content[0]# HD10 index

        # Eliminate the already used data and set the next property
        sub_content = sub_content[1:]
        hund11 = graceful_conversion(sub_content[:12]) # HUND11 (Individual dog name is a string capped at 12 characters)

        # Eliminate the already used data and set the next property
        sub_content = sub_content[12:]
        kj11_id = sub_content[0]# KJ11 index

        # Eliminate the already used data and set the next property
        sub_content = sub_content[1:]
        k11_id = sub_content[0]# K11 index

        # Eliminate the already used data and set the next property
        sub_content = sub_content[1:]
        m11_id = sub_content[0]# M11 index

        # Eliminate the already used data and set the next property
        sub_content = sub_content[1:]
        hd11_id = sub_content[0]# HD11 index

        # Eliminate the already used data and set the next property
        sub_content = sub_content[1:]
        hund12 = graceful_conversion(sub_content[:12]) # HUND12 (Individual dog name is a string capped at 12 characters)

        # Eliminate the already used data and set the next property
        sub_content = sub_content[12:] 
        kj12_id = sub_content[0]# KJ12 index

        # Eliminate the already used data and set the next property
        sub_content = sub_content[1:] 
        k12_id = sub_content[0]# K12 index

        # Eliminate the already used data and set the next property
        sub_content = sub_content[1:]
        m12_id = sub_content[0]# M12 index

        # Eliminate the already used data and set the next property
        sub_content = sub_content[1:]
        hd12_id = sub_content[0]# HD12 index

        return cls(
            kullb=kullb,
            kennel=kennel,
            fodt=fodt,
            kullnr=kullnr,
            farens_reg_nr=farens_reg_nr,
            farens_navn=farens_navn,
            morens_reg_nr=morens_reg_nr,
            morens_navn=morens_navn,
            alle_id=alle_id,
            sosken=sosken,
            
            hund1=hund1,
            kj1_id=kj1_id,
            k1_id=k1_id,
            m1_id=m1_id,
            hd1_id=hd1_id,

            hund2=hund2,
            kj2_id=kj2_id,
            k2_id=k2_id,
            m2_id=m2_id,
            hd2_id=hd2_id,

            hund3=hund3,
            kj3_id=kj3_id,
            k3_id=k3_id,
            m3_id=m3_id,
            hd3_id=hd3_id,

            hund4=hund4,
            kj4_id=kj4_id,
            k4_id=k4_id,
            m4_id=m4_id,
            hd4_id=hd4_id,

            hund5=hund5,
            kj5_id=kj5_id,
            k5_id=k5_id,
            m5_id=m5_id,
            hd5_id=hd5_id,

            hund6=hund6,
            kj6_id=kj6_id,
            k6_id=k6_id,
            m6_id=m6_id,
            hd6_id=hd6_id,

            hund7=hund7,
            kj7_id=kj7_id,
            k7_id=k7_id,
            m7_id=m7_id,
            hd7_id=hd7_id,

            hund8=hund8,
            kj8_id=kj8_id,
            k8_id=k8_id,
            m8_id=m8_id,
            hd8_id=hd8_id,

            hund9=hund9,
            kj9_id=kj9_id,
            k9_id=k9_id,
            m9_id=m9_id,
            hd9_id=hd9_id,

            hund10=hund10,
            kj10_id=kj10_id,
            k10_id=k10_id,
            m10_id=m10_id,
            hd10_id=hd10_id,

            hund11=hund11,
            kj11_id=kj11_id,
            k11_id=k11_id,
            m11_id=m11_id,
            hd11_id=hd11_id,

            hund12=hund12,
            kj12_id=kj12_id,
            k12_id=k12_id,
            m12_id=m12_id,
            hd12_id=hd12_id,
        )
    
    @property
    def kullb(self) -> Union[str, None]:
        return None if not self._kullb else self._kullb
    
    @property
    def kennel(self) -> Union[str, None]:
        return None if not self._kennel else self._kennel
    
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
    def farens_reg_nr(self) -> Union[str, None]:
        return None if not self._farens_reg_nr else self._farens_reg_nr
    
    @property
    def farens_navn(self) -> Union[str, None]:
        return None if not self._farens_navn else self._farens_navn
    
    @property
    def morens_reg_nr(self) -> Union[str, None]:
        return None if not self._morens_reg_nr else self._morens_reg_nr
    
    @property
    def morens_navn(self) -> Union[str, None]:
        return None if not self._morens_navn else self._morens_navn
    
    @property
    def alle_id(self) -> int:
        return self._alle_id
    
    @property
    def sosken(self) -> Union[str, None]:
        return None if not self._sosken else self._sosken
    
    @property
    def hund1(self) -> Union[str, None]:
        return None if not self._hund1 else self._hund1
    
    @property
    def kj1_id(self) -> int:
        return self._kj1_id
    
    @property
    def k1_id(self) -> int:
        return self._k1_id
    
    @property
    def m1_id(self) -> int:
        return self._m1_id
    
    @property
    def hd1_id(self) -> int:
        return self._hd1_id
 
    @property
    def hund2(self) -> Union[str, None]:
        return None if not self._hund2 else self._hund2
    
    @property
    def kj2_id(self) -> int:
        return self._kj2_id
    
    @property
    def k2_id(self) -> int:
        return self._k2_id
    
    @property
    def m2_id(self) -> int:
        return self._m2_id
    
    @property
    def hd2_id(self) -> int:
        return self._hd2_id
 
    @property
    def hund3(self) -> Union[str, None]:
        return None if not self._hund3 else self._hund3
    
    @property
    def kj3_id(self) -> int:
        return self._kj3_id
    
    @property
    def k3_id(self) -> int:
        return self._k3_id
    
    @property
    def m3_id(self) -> int:
        return self._m3_id
    
    @property
    def hd3_id(self) -> int:
        return self._hd3_id
 
    @property
    def hund4(self) -> Union[str, None]:
        return None if not self._hund4 else self._hund4
    
    @property
    def kj4_id(self) -> int:
        return self._kj4_id
    
    @property
    def k4_id(self) -> int:
        return self._k4_id
    
    @property
    def m4_id(self) -> int:
        return self._m4_id
    
    @property
    def hd4_id(self) -> int:
        return self._hd4_id
 
    @property
    def hund5(self) -> Union[str, None]:
        return None if not self._hund5 else self._hund5
    
    @property
    def kj5_id(self) -> int:
        return self._kj5_id
    
    @property
    def k5_id(self) -> int:
        return self._k5_id
    
    @property
    def m5_id(self) -> int:
        return self._m5_id
    
    @property
    def hd5_id(self) -> int:
        return self._hd5_id
 
    @property
    def hund6(self) -> Union[str, None]:
        return None if not self._hund6 else self._hund6
    
    @property
    def kj6_id(self) -> int:
        return self._kj6_id
    
    @property
    def k6_id(self) -> int:
        return self._k6_id
    
    @property
    def m6_id(self) -> int:
        return self._m6_id
    
    @property
    def hd6_id(self) -> int:
        return self._hd6_id
 
    @property
    def hund7(self) -> Union[str, None]:
        return None if not self._hund7 else self._hund7
    
    @property
    def kj7_id(self) -> int:
        return self._kj7_id
    
    @property
    def k7_id(self) -> int:
        return self._k7_id
    
    @property
    def m7_id(self) -> int:
        return self._m7_id
    
    @property
    def hd7_id(self) -> int:
        return self._hd7_id
 
    @property
    def hund8(self) -> Union[str, None]:
        return None if not self._hund8 else self._hund8
    
    @property
    def kj8_id(self) -> int:
        return self._kj8_id
    
    @property
    def k8_id(self) -> int:
        return self._k8_id
    
    @property
    def m8_id(self) -> int:
        return self._m8_id
    
    @property
    def hd8_id(self) -> int:
        return self._hd8_id
 
    @property
    def hund9(self) -> Union[str, None]:
        return None if not self._hund9 else self._hund9
    
    @property
    def kj9_id(self) -> int:
        return self._kj9_id
    
    @property
    def k9_id(self) -> int:
        return self._k9_id
    
    @property
    def m9_id(self) -> int:
        return self._m9_id
    
    @property
    def hd9_id(self) -> int:
        return self._hd9_id
 
    @property
    def hund10(self) -> Union[str, None]:
        return None if not self._hund10 else self._hund10
    
    @property
    def kj10_id(self) -> int:
        return self._kj10_id
    
    @property
    def k10_id(self) -> int:
        return self._k10_id
    
    @property
    def m10_id(self) -> int:
        return self._m10_id
    
    @property
    def hd10_id(self) -> int:
        return self._hd10_id
 
    @property
    def hund11(self) -> Union[str, None]:
        return None if not self._hund11 else self._hund11
    
    @property
    def kj11_id(self) -> int:
        return self._kj11_id
    
    @property
    def k11_id(self) -> int:
        return self._k11_id
    
    @property
    def m11_id(self) -> int:
        return self._m11_id
    
    @property
    def hd11_id(self) -> int:
        return self._hd11_id
 
    @property
    def hund12(self) -> Union[str, None]:
        return None if not self._hund12 else self._hund12
    
    @property
    def kj12_id(self) -> int:
        return self._kj12_id
    
    @property
    def k12_id(self) -> int:
        return self._k12_id
    
    @property
    def m12_id(self) -> int:
        return self._m12_id
    
    @property
    def hd12_id(self) -> int:
        return self._hd12_id

    @property
    def native(self) -> dict:
        """Method converts class instance to native python classes for serialization purposes"""

        obj_dict = {
            'kullb': self.kullb,
            'kennel': self.kennel,
            'fodt': self.fodt_str,
            'kullnr': self.kullnr,
            'farens_reg_nr': self.farens_reg_nr,
            'farens_navn': self.farens_navn,
            'morens_reg_nr': self.morens_reg_nr,
            'morens_navn': self.morens_navn,
            'alle_id': self.alle_id,
            'sosken': self.sosken,
            'hund1': self.hund1,
            'kj1_id': self.kj1_id,
            'k1_id': self.k1_id,
            'm1_id': self.m1_id,
            'hd1_id': self.hd1_id,
            'hund2': self.hund2,
            'kj2_id': self.kj2_id,
            'k2_id': self.k2_id,
            'm2_id': self.m2_id,
            'hd2_id': self.hd2_id,
            'hund3': self.hund3,
            'kj3_id': self.kj3_id,
            'k3_id': self.k3_id,
            'm3_id': self.m3_id,
            'hd3_id': self.hd3_id,
            'hund4': self.hund4,
            'kj4_id': self.kj4_id,
            'k4_id': self.k4_id,
            'm4_id': self.m4_id,
            'hd4_id': self.hd4_id,
            'hund5': self.hund5,
            'kj5_id': self.kj5_id,
            'k5_id': self.k5_id,
            'm5_id': self.m5_id,
            'hd5_id': self.hd5_id,
            'hund6': self.hund6,
            'kj6_id': self.kj6_id,
            'k6_id': self.k6_id,
            'm6_id': self.m6_id,
            'hd6_id': self.hd6_id,
            'hund7': self.hund7,
            'kj7_id': self.kj7_id,
            'k7_id': self.k7_id,
            'm7_id': self.m7_id,
            'hd7_id': self.hd7_id,
            'hund8': self.hund8,
            'kj8_id': self.kj8_id,
            'k8_id': self.k8_id,
            'm8_id': self.m8_id,
            'hd8_id': self.hd8_id,
            'hund9': self.hund9,
            'kj9_id': self.kj9_id,
            'k9_id': self.k9_id,
            'm9_id': self.m9_id,
            'hd9_id': self.hd9_id,
            'hund10': self.hund10,
            'kj10_id': self.kj10_id,
            'k10_id': self.k10_id,
            'm10_id': self.m10_id,
            'hd10_id': self.hd10_id,
            'hund11': self.hund11,
            'kj11_id': self.kj11_id,
            'k11_id': self.k11_id,
            'm11_id': self.m11_id,
            'hd11_id': self.hd11_id,
            'hund12': self.hund12,
            'kj12_id': self.kj12_id,
            'k12_id': self.k12_id,
            'm12_id': self.m12_id,
            'hd12_id': self.hd12_id,
        }

        return obj_dict



class TysKullList:

    _contents: List[TysKull]

    def __init__(self, contents:List[TysKull]=[]) -> None:
        self._contents = contents
    
    @property
    def native(self) -> dict:
        """Method converts class instance to native python classes for serialization purposes"""

        return [i.native for i in self._contents]
