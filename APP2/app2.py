from typing import Union, List

from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


class Data(BaseModel):
    pesel: int
    name: str
    address: Union[str, None]
    dieseses: List[str]
    tel_number: int


# Dummy data
dummy_users = {
    12345: {"pesel": 12345, "name": "John Doe", "address": "123 Main St", "dieseses": ["flu"], "tel_number": 5551234567},
    67890: {"pesel": 67890, "name": "Jane Smith", "address": "456 Oak Ave", "dieseses": [], "tel_number": 5559876543}
}


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/users/{pesel}")
def read_item(pesel: int):
    user = dummy_users.get(pesel)
    if user:
        return user
    return {"error": "User not found"}


@app.put("/users/{pesel}")
def update_item(pesel: int, data: Data):
    dummy_users[pesel] = {"pesel": pesel, **data.model_dump()}
    return dummy_users[pesel]