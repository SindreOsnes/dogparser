from typing import Union
from datetime import date

def graceful_conversion(input_element: bytes) -> str:
    data_out = input_element
    data_out = sure_conversion(data_out)
    data_out = uncertain_conversions(data_out)
    return data_out.rstrip(b'\x00').decode('utf8')

def sure_conversion(input_element: bytes) -> bytes:
    data_out = input_element
    data_out = data_out.replace(b'\x86', b'\xc3\xa5') # å | HUNDER BRUKS(B-kåret)
    data_out = data_out.replace(b'\x91', b'\xc3\xa6') # æ | HUNDER UTD(Færd.)
    data_out = data_out.replace(b'\x92', b'\xc3\x86') # Æ | HUNDER HEM(BÆRER)
    data_out = data_out.replace(b'\x94', b'\xc3\xb6') # ö | HUNDER BRUKS(Godkj Mögl)
    data_out = data_out.replace(b'\x9b', b'\xc3\xb8') # ø | HUNDER HD(Død)
    data_out = data_out.replace(b'\x9d', b'\xc3\x98') # Ø | HUNDER HEM(BLØDER)
    
    return data_out

def uncertain_conversions(input_element: bytes) -> bytes:

    data_out = input_element
    data_out = data_out.replace(b'\x8e', b'?x8e') # HUNDER (reg_nr: S138B?x8e/72, value(reg_nr): S138B?x8e/72)
    data_out = data_out.replace(b'\x8f', b'?x8f') # HUNDER (reg_nr: SBR?x8fFLI, value(reg_nr): SBR?x8fFLI)
    data_out = data_out.replace(b'\x99', b'?x99') # HUNDER (reg_nr: NKKR3214?x99, value(reg_nr): NKKR3214?x99)
    data_out = data_out.replace(b'\x9a', b'?x9a') # HUNDER (reg_nr: SZNIXL?x9aF, value(reg_nr): SZNIXL?x9aF)
    
    return data_out

def date_conversion(data: bytes) -> Union[str, None]:
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

            return date(day=day, month=month, year=year).isoformat()
        except Exception as e:
            print(datestr, data)
            raise e
