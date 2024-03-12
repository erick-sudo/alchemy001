"""CRUD"""
from sqlalchemy.orm import Session
from fastapi import Depends
from app.data import models, schemas
from app.dependencies import get_db

dpDep: Session = Depends(get_db)

def get_user(user_id: int, db = dpDep):
    return db.query(models.User).filter(models.User.id == user_id).first()

def get_user_by_email(email: str, db = dpDep):
    return db.query(models.User).filter(models.User.email == email).first()

def get_users(skip: int = 0, limit: int = 100, db = dpDep):
    return db.query(models.User).offset(skip).limit(limit).all()

def create_user(user: schemas.UserCreate, db = dpDep):
    fake_hashed_password = user.password + "notreallyhashed"
    db_user = models.User(email=user.email, hashed_password=fake_hashed_password)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

def get_items(skip: int = 0, limit: int = 100, db = dpDep):
    return db.query(models.Item).offset(skip).limit(limit).all()

def create_user_item(item: schemas.ItemCreate, user_id: int, db = dpDep):
    db_item = models.Item(**item.model_dump(), owner_id=user_id)
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return db_item