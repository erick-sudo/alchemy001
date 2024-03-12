"""Admins router"""
from fastapi import APIRouter

router = APIRouter()

@router.post("/")
async def update_admin():
    """Update the admin"""
    return {"message": "Admin getting schwifty"}
