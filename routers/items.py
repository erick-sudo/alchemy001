"""Items router"""
from fastapi import APIRouter, HTTPException, Depends

from app.data import schemas, crud
from app.dependencies import get_db

router = APIRouter(
    prefix="/items",
    tags=["items"],
    dependencies=[Depends(get_db)],
    responses={404: {"description": "Not found"}},
)

@router.get("/", response_model=list[schemas.Item])
def read_items(skip: int = 0, limit: int = 100):
    items = crud.get_items(skip=skip, limit=limit)
    return items

@router.get("/{item_id}", response_model=schemas.Item)
def read_item(user_id: int):
    db_user = crud.get_user(user_id=user_id)
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return db_user