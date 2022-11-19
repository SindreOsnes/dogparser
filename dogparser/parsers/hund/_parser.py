import json
import os
from typing import List, Tuple

def parse(source_definition: str, destination_folder: str):
    
    # Read the schema
    schema_file = source_definition + '.DBA'

    with open(schema_file, 'rb') as f:
        schema_data = f.read()
    
    # Strip the extraneous data and split into elements
    stripped_schema_data = schema_data[schema_data.index(b'nei\x00ja'):]
    schema_split = stripped_schema_data.split(b'\x00')

    enums = [
        (b'LAND', 'LAND.json'), # Country
        (b'kj\x9bnn', 'KJONN.json') # Sex
        (b'HD', 'HD.json') # Sex
    ]

    for target, file in enums:
        # Get the enumerator
        enum, schema_split = extract_enum(schema_split, target)

        with open(os.path.join(destination_folder, file), 'w') as f:
            json.dump(enum, f, ensure_ascii=False, indent=True)

    print(schema_split)

def extract_enum(elements: List[bytes], query_term: bytes) -> Tuple[List[str], List[bytes]]:
    query_idx = elements.index(query_term)
    query_len = elements[query_idx+1][0]
    
    print(f'{query_term} contains {query_len+1} entries including leading NULL')

    query = elements[query_idx+1:query_idx+query_len+1]

    enum = [''] + [graceful_conversion(x) for x in query]

    return enum, elements[query_idx+query_len+1:]

def graceful_conversion(input_element: bytes) -> str:
    data_out = input_element
    return data_out.decode('utf8')
