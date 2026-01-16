from typing import Annotated
from fastapi import APIRouter, Depends
from sqlmodel import Session
from models import User, get_session

from schemas import Data

router = APIRouter()

SessionDep = Annotated[Session, Depends(get_session)]

@router.get("/") # move to a separate file
def read_root():
    return {"Hello": "World"}


@router.get("/{pesel}")
def read_item(pesel: int,
    session: SessionDep) -> User:
    user = session.get(User, pesel)
    if user:
        return user
    return {"error": "User not found"}


# @router.put("/{pesel}")
# def update_item(pesel: int, data: Data):
#     dummy_users[pesel] = {"pesel": pesel, **data.model_dump()}
#     return dummy_users[pesel]


def get_curent_user(token: str):
    ...
    return {...}


@router.get('/profile')
def get_profile(user=Depends(get_curent_user)):
    return {
        "message": "User profile",
        "user": user
    }