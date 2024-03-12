"""Dependencies"""
from app.data import models
from app.config.database import SessionLocal, engine

models.Base.metadata.create_all(bind=engine)

# Dependency
def get_db():
    """Database session initialization"""
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
