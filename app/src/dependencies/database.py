from src.core.database import LocalSession

SessionLocal = LocalSession()

def get_db():
    db = SessionLocal
    try:
        yield db
    finally:
        db.close()