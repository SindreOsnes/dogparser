import json
import os
from typing import List, Tuple

def parse(source_definition: str, destination_folder: str):
    
    # Read the schema
    schema_file = source_definition + '.DBA'

    with open(schema_file, 'rb') as f:
        schema_data = f.read()
    
    # Strip the extraneous data and split into elements
    stripped_schema_data = schema_data[schema_data.index(b'REG.NR')-1:]
    schema_split = stripped_schema_data.split(b'\x00')
    columns, _ = extract_values(schema_split, 0, schema_data[schema_data.index(b'REG.NR')-1])
    print(columns)


    stripped_schema_data = schema_data[schema_data.index(b'nei\x00ja'):]
    schema_split = stripped_schema_data.split(b'\x00')

    enums = [
        (b'LAND', 'LAND.json') # Country
        ,(b'kj\x9bnn', 'KJONN.json') # Sex
        ,(b'HD', 'HD.json') # HD
        ,(b'AD', 'AD.json') # AD
        ,(b'HEM', 'HEM.json') # HEM
        ,(b'UTD', 'UTD.json') # UTD
        ,(b'UTD2', 'UTD2.json') # UTD2
        ,(b'UTMER', 'UTMER.json') # UTMER
        ,(b'VIN', 'VIN.json') # VIN
        ,(b'K\x8fRET', 'K.json') # K
        ,(b'ZB', 'ZB.json') # ZB
        ,(b'KKL', 'KKL.json') # KKL
        ,(b'BRUKS', 'BRUKS.json') # BRUKS
        ,(b'PREM', 'PREM.json') # PREM
        ,(b'KVAL', 'KVAL.json') # KVAL
        ,(b'KVAL2', 'KVAL2.json') # KVAL2
        ,(b'TEST', 'TEST.json') # TEST
    ]

    for target, file in enums:
        # Get the enumerator
        enum, schema_split = extract_enum(schema_split, target)

        with open(os.path.join(destination_folder, file), 'w') as f:
            json.dump(enum, f, ensure_ascii=False, indent=True)

    print(schema_split)
    print(columns)
    print(schema_split[0])

def extract_enum(elements: List[bytes], query_term: bytes) -> Tuple[List[str], List[bytes]]:
    query_idx = elements.index(query_term)
    query_len = elements[query_idx+1][0]
    
    print(f'{query_term} contains {query_len+1} entries including leading NULL')

    enum, return_elements = extract_values(elements, query_idx+1, query_len)
    enum = [''] + enum

    return enum, return_elements

def extract_values(elements: List[bytes], idx: int, count: int)  -> Tuple[List[str], List[bytes]]:
    query = elements[idx:idx+count]
    query[0] = query[0][1:]

    enum = [graceful_conversion(x) for x in query]

    return enum, elements[idx+count:]

def graceful_conversion(input_element: bytes) -> str:
    data_out = input_element
    data_out = sure_conversion(data_out)
    return data_out.decode('utf8')

def sure_conversion(input_element: bytes) -> bytes:
    data_out = input_element
    data_out = data_out.replace(b'\x86', b'\xc3\xa5') # å | HUNDER BRUKS(B-kåret)
    data_out = data_out.replace(b'\x91', b'\xc3\xa6') # æ | HUNDER UTD(Færd.)
    data_out = data_out.replace(b'\x92', b'\xc3\x86') # Æ | HUNDER HEM(BÆRER)
    data_out = data_out.replace(b'\x94', b'\xc3\xb6') # ö | HUNDER BRUKS(Godkj Mögl)
    data_out = data_out.replace(b'\x9b', b'\xc3\xb8') # ø | HUNDER HD(Død)
    data_out = data_out.replace(b'\x9d', b'\xc3\x98') # Ø | HUNDER HEM(BLØDER)
    
    return data_out

