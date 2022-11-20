import json
import os

from ._hund import Hund, HundList
from ...utils import extract_enum, extract_values

def parse(source_definition: str, destination_folder: str):
    
    # Parse the schem
    parse_schema(source_definition=source_definition, destination_folder=destination_folder)
    
    # Read the data
    data_file = source_definition + '.DBM'

    hund_list = []

    element_len = 250

    with open(data_file, 'rb') as f:
        data = f.read(element_len)
        hund = Hund.from_bytes(data)

        hund_list.append(hund)

        hund_str = json.dumps(HundList(hund_list).native)
        print(hund_str)


def parse_schema(source_definition: str, destination_folder: str):
    
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
        ,(b'HDH', 'HDH.json') # HDH
    ]

    for target, file in enums:
        # Get the enumerator
        enum, schema_split = extract_enum(schema_split, target)

        with open(os.path.join(destination_folder, file), 'w') as f:
            json.dump(enum, f, ensure_ascii=False, indent=True)
