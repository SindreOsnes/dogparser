import struct
from typing import List, Tuple, Union

from ._conversion import graceful_conversion

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

def extract_decimal(data: bytes) -> Union[float, None]:
    if data == b'\x00\x00\x00\x80':
        return None
    else:
        return str(struct.unpack('f', data)[0])