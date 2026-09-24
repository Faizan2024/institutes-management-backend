from src.interface.user_interface import UserInterface
from sqlalchemy.orm import Session
from sqlalchemy import select
from src.models.user_model import User

class StudentRepository(UserInterface):
    def __init__(self, db: Session):
        self.db = db

    def create_user(self, user: User):
        self.db.add(user)
        self.db.commit()
        self.db.refresh(user)
        return user

    def get_user(self, id):
        statment = select(User).where(id == User.id)
        result = self.db.execute(statment)
        return result.scalar_one_or_none()

    def get_all_users(self):
        statement = select(User)
        result = self.db.execute(statement)
        return  result.scalars().all()

    def update_user(self, id, user: User):
        self.db.commit()
        self.db.refresh(user)
        return  user

    def delete_user(self, user: User):
        self.db.delete(user)
        return   None