from typing import Union

from ...utils import graceful_conversion

class Hund:
    _reg_nr: str
    def __init__(self, reg_nr: str) -> None:
        self._reg_nr = reg_nr
    
    @classmethod
    def from_bytes(cls, content: bytes):
        if len(content) != 250:
            raise AssertionError('Input for Hund should be 250 bytes')
        
        # The dog table contains a 10 byte header that does not contain usefull data
        header = content[:10]

        # ELiminate the already used data and set the next property
        sub_content = content[10:] # 240 bytes remaining
        reg_nr = graceful_conversion(sub_content[:12]) # REG.NR (registration number is a string capped at 12 character)

        return cls(reg_nr=reg_nr)