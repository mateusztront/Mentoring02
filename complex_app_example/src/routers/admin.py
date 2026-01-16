from fastapi import APIRouter, Depends
from .deps import get_db, require_admin

router = APIRouter(
    prefix="/admin",
    tags=["admin"],
    dependencies=[Depends(require_admin)]  # globalna ochrona routera
)

@router.get("/stats")
def get_stats(db=Depends(get_db)):
    return {
        "users": 120,
        "revenue": 9999,
        "db": db
    }


@router.delete("/users/{user_id}")
def delete_user(user_id: int, db=Depends(get_db)):
    return {
        "deleted_user_id": user_id
    }
