"""Main application"""
from fastapi import Depends, FastAPI

from .dependencies import get_db
from .routers import items, users
from .internal import admin

app = FastAPI(dependencies=[Depends(get_db)])

app.include_router(items.router)
app.include_router(users.router)
app.include_router(
    admin.router,
    prefix="/admin",
    tags=["admin"],
    dependencies=[Depends(get_db)],
    responses={ 418: { "description": "I'm a teapot" } }
)

@app.get("/")
async def root():
    return { "message": "Hello Bigger Applications" }
