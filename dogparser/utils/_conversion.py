from typing import Union
from datetime import date

def graceful_conversion(input_element: bytes) -> str:
    data_out = input_element.rstrip(b'\x00')
    out_str = base_conversions(data_out).decode('utf8')
    out_str = sure_conversion(out_str)
    return out_str

def sure_conversion(input_element: str) -> str:
    data_out = input_element
    data_out = data_out.replace('?x86?', 'å') # å | HUNDER BRUKS(B-kåret)
    data_out = data_out.replace('?x91?', 'æ') # æ | HUNDER UTD(Færd.)
    data_out = data_out.replace('?x92?', 'Æ') # Æ | HUNDER HEM(BÆRER)
    data_out = data_out.replace('?x94?', 'ö') # ö | HUNDER BRUKS(Godkj Mögl)
    data_out = data_out.replace('?x9b?', 'ø') # ø | HUNDER HD(Død)
    data_out = data_out.replace('?x9d?', 'Ø') # Ø | HUNDER HEM(BLØDER)
    
    return data_out

def base_conversions(input_element: bytes) -> bytes:

    data_out = input_element
    data_out = data_out.replace(b'\x86', b'?x86?') # å | HUNDER BRUKS(B-kåret)
    data_out = data_out.replace(b'\x91', b'?x91?') # æ | HUNDER UTD(Færd.)
    data_out = data_out.replace(b'\x92', b'?x92?') # Æ | HUNDER HEM(BÆRER)
    data_out = data_out.replace(b'\x94', b'?x94?') # ö | HUNDER BRUKS(Godkj Mögl)
    data_out = data_out.replace(b'\x9b', b'?x9b?') # ø | HUNDER HD(Død)
    data_out = data_out.replace(b'\x9d', b'?x9d?') # Ø | HUNDER HEM(BLØDER)
    data_out = data_out.replace(b'\x85', b'?x85?') # HUNDER (reg_nr: LOSH1006502, value(navn): FRISBEE D. PARC ?x85? MITRAILLES)
    data_out = data_out.replace(b'\x8e', b'?x8e?') # HUNDER (reg_nr: SZ2200013, value(navn): MACATO V. HOLTK?x8e?MPER SEE)
    data_out = data_out.replace(b'\x8f', b'?x8f?') # HUNDER (reg_nr: 16703/08, value(navn): ICCARO AV PERLEG?x8f?RDEN)
    data_out = data_out.replace(b'\x90', b'?x90?') # HUNDER (reg_nr: LOF536495, value(navn): SCOTT D. VAL DE LA HOU?x90?E)
    data_out = data_out.replace(b'\x99', b'?x99?') # HUNDER (reg_nr: SZ2074460, value(navn): LEILA V.D. R?x99?DERRBURG)
    data_out = data_out.replace(b'\x9a', b'?x9a?') # HUNDER (reg_nr: SZ2094024, value(navn): NOLA V.D. B?x9?aLTENSTIEGE)
    data_out = data_out.replace(b'\xa1', b'?xa1?') # HUNDER (reg_nr: S27950/91, value(navn): L?xa1?NDENDORFF S27950/91)
    data_out = data_out.replace(b'\xa5', b'?xa5?') # HUNDER (reg_nr: POA91698, value(navn): ISSO D. DO?xa5?A PURA)
    data_out = data_out.replace(b'\xb5', b'?xb5?') # HUNDER (reg_nr: LOSH1113792, value(navn): LITCHIES D. PARC ?xb5? MITRAILLES)
    data_out = data_out.replace(b'\xb7', b'?xb7?') # HUNDER (reg_nr: LOSH1054710, value(navn): HACH D. PARC ?xb7? MITRAILLES)
    data_out = data_out.replace(b'\xd4', b'?xd4?') # HUNDER (reg_nr: 20837/08, value(navn): G?xd?4NIE AV CHAMIROX)
    data_out = data_out.replace(b'\xe1', b'?xe1?') # HUNDER (reg_nr: SZ2162887, value(navn): LUNA V. SCHLO?xe1?G?x8e??xe1?CHEN)
    data_out = data_out.replace(b'\xf9', b'?xf9?') # HUNDER (reg_nr: 57747/18, value(kennnel): HEIAG?xf9?RDEN, AV) x8f collision
    data_out = data_out.replace(b'\xff', b'?xff?') # HUNDER (reg_nr: SZ1915923, value(navn): OLDO V. SCHLO?xe1? BIRKENSTEIN?xff?)
    
    return data_out

def date_conversion(data: bytes) -> Union[date, None]:
    datestr = graceful_conversion(data)
    if len(datestr) != 6:
        return None
    else:
        try:
            year = int(datestr[-2:])
            if year > 25:
                year += 1900
            else:
                year += 2000

            month = int(datestr[2:-2])
            day = int(datestr[0:2])

            return date(day=day, month=month, year=year)
        except Exception as e:
            print(datestr, data)
            raise e
