from typing import List, Union
from datetime import date

from ...utils import graceful_conversion, date_conversion

class Poststed:
    _postnr: str # Postal code (POSTNR in original schema)
    _sted: Union[str, None] # Location (STED in original schema)
    _land_id: int # Country (LAND in original schema)
    _fylke_id: int # County (FYLKE in original schema)

    def __init__(self, postnr: str, sted: Union[str, None], land_id: int
, fylke_id: int) -> None:
        self._postnr = postnr
        self._sted = sted
        self._land_id = land_id
        self._fylke_id = fylke_id

    @classmethod
    def from_bytes(cls, content: bytes):
        if len(content) != 32:
            raise AssertionError("Input for Poststed should be 32 bytes")

        # The postal location table contains a 3 byte header that does not contain useful data
        # Remove used data from next entries
        sub_content = content[3:]

        # Parse the POSTNR property
        postnr = graceful_conversion(sub_content[:7]) # POSTNR (Postal code is a string capped at 7 characters)
        # Remove used data from next entries
        sub_content = sub_content[7:]

        # Parse the STED property
        sted = graceful_conversion(sub_content[:20]) # STED (Location is a string capped at 20 characters)
        # Remove used data from next entries
        sub_content = sub_content[20:]

        # Parse the LAND property
        land_id = sub_content[0] # LAND (Country is an enum represented by a 1 byte integer)
        # Remove used data from next entries
        sub_content = sub_content[1:]

        # Parse the FYLKE property
        fylke_id = sub_content[0] # FYLKE (County is an enum represented by a 1 byte integer)
        # Remove used data from next entries
        sub_content = sub_content[1:]

        return cls(postnr=postnr,
                   sted=sted,
                   land_id=land_id,
                   fylke_id=fylke_id)

    @property
    def postnr(self) -> str:
        return self._postnr

    @property
    def sted(self) -> Union[str, None]:
        return None if not self._sted else self._sted

    @property
    def land_id(self) -> int:
        return self._land_id

    @property
    def fylke_id(self) -> int:
        return self._fylke_id

    @property
    def native(self) -> dict:
        """Method converts class instance to native python classes for serialization purposes"""

        obj_dict = {
            'postnr': self.postnr,
            'sted': self.sted,
            'land_id': self.land_id,
            'fylke_id': self.fylke_id,
        }

        return obj_dict

class PoststedList:

    _contents: List[Poststed]

    def __init__(self, contents:List[Poststed]=[]) -> None:
        self._contents = contents
    
    @property
    def native(self) -> dict:
        """Method converts class instance to native python classes for serialization purposes"""

        return [i.native for i in self._contents]
