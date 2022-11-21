import os
import json

from ...utils import extract_enum, extract_values
from ._oppdretter import Oppdretter, OppdretterList

def parse(source_definition: str, destination_folder: str):
    
    # Parse the schem
    parse_schema(source_definition=source_definition, destination_folder=destination_folder)
    
    # Read the data
    data_file = source_definition + '.DBM'

    eier_list = []

    element_len = 250

    with open(data_file, 'rb') as f:
        i = 0
        data = f.read(element_len)

        while len(data) == element_len:
            if i and not i% 1000:
                print(f'{i} records parsed')
            eier = Oppdretter.from_bytes(data)
            eier_list.append(eier)
            data = f.read(element_len)
            i+=1

    # Write the data
    os.makedirs(os.path.join(destination_folder, 'DATA'), exist_ok=True)
    with open(os.path.join(destination_folder, 'DATA/opdretter.json'), 'w', encoding='utf8') as f:
        json.dump(OppdretterList(eier_list).native, f, indent=2, ensure_ascii=False)


def parse_schema(source_definition: str, destination_folder: str):
    
    # Read the schema
    schema_file = source_definition + '.DBA'

    with open(schema_file, 'rb') as f:
        schema_data = f.read()
    
    # Strip the extraneous data and split into elements
    stripped_schema_data = schema_data[schema_data.index(b'KENNEL')-1:]
    schema_split = stripped_schema_data.split(b'\x00')
    columns, _ = extract_values(schema_split, 0, schema_data[schema_data.index(b'KENNEL')-1])
    print(columns)


    stripped_schema_data = schema_data[schema_data.index(b'nei\x00ja'):]
    schema_split = stripped_schema_data.split(b'\x00')

    enums = [
        (b'PREFIKS', 'PREFIKS.json'),
        (b'LAND', 'LAND.json'),
        (b'OPREFIKS', 'OPREFIKS.json'),
    ]

    for target, file in enums:
        # Get the enumerator
        enum, schema_split = extract_enum(schema_split, target)

        with open(os.path.join(destination_folder, file), 'w') as f:
            json.dump(enum, f, ensure_ascii=False, indent=True)
    
    print(schema_split[0])
