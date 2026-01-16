from typing import List, Union
from pydantic import BaseModel

class Data(BaseModel):
    pesel: int
    name: str
    address: Union[str, None]
    dieseses: List[str]
    tel_number: int