import os
import json

from ...utils import extract_enum, extract_values
from ._kull import Kull, KullList

def parse(source_definition: str, destination_folder: str):
    
    # Parse the schem
    parse_schema(source_definition=source_definition, destination_folder=destination_folder)
    
    # Read the data
    data_file = source_definition + '.DBM'

    element_list = []

    element_len = 844

    with open(data_file, 'rb') as f:
        i = 0
        data = f.read(element_len)

        while len(data) == element_len:
            if i and not i% 1000:
                print(f'{i} records parsed')
            element = Kull.from_bytes(data)
            element_list.append(element)
            data = f.read(element_len)
            i+=1

    # Write the data
    os.makedirs(os.path.join(destination_folder, 'DATA'), exist_ok=True)
    with open(os.path.join(destination_folder, 'DATA/kull.json'), 'w', encoding='utf8') as f:
        json.dump(KullList(element_list).native, f, indent=2, ensure_ascii=False)


def parse_schema(source_definition: str, destination_folder: str):
    
    # Read the schema
    schema_file = source_definition + '.DBA'

    with open(schema_file, 'rb') as f:
        schema_data = f.read()
    
    # Strip the extraneous data and split into elements
    stripped_schema_data = schema_data[schema_data.index(b'b1')-1:]
    schema_split = stripped_schema_data.split(b'\x00')
    columns, _ = extract_values(schema_split, 0, schema_data[schema_data.index(b'b1')-1])
    print(columns)


    stripped_schema_data = schema_data[schema_data.index(b'nei\x00ja'):]
    schema_split = stripped_schema_data.split(b'\x00')

    enums = [
        (b'LAND', 'LAND.json'),# Country
        (b'HD', 'HD.json'),# ZB?
    ]

    for target, file in enums:
        # Get the enumerator
        enum, schema_split = extract_enum(schema_split, target)

        with open(os.path.join(destination_folder, file), 'w') as f:
            json.dump(enum, f, ensure_ascii=False, indent=True)
    
    print(schema_split[0])
