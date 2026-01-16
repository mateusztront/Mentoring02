from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from ..deps import get_db, get_current_user
from ..models import User

router = APIRouter(
    prefix="/users",
    tags=["users"]
)

@router.get("/me")
def get_me(
    user: User = Depends(get_current_user)
):
    return {
        "id": user.id,
        "email": user.email,
        "role": user.role
    }


@router.get("/{user_id}")
def get_user(
    user_id: int,
    db: Session = Depends(get_db),
):
    user = db.get(User, user_id)
    return user
