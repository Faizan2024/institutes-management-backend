from src.interface.teacher_interface import TeacherInterface
from sqlalchemy.orm import Session
from sqlalchemy import select
from src.models.teacher_model import Teacher

class StudentRepository(TeacherInterface):
    def __init__(self, db: Session):
        self.db = db

    def create_teacher(self, teacher: Teacher):
        self.db.add(teacher)
        self.db.commit()
        self.db.refresh(teacher)
        return teacher

    def get_teacher(self, id):
        statment = select(Teacher).where(id == Teacher.id)
        result = self.db.execute(statment)
        return result.scalar_one_or_none()

    def get_all_teachers(self):
        statement = select(Teacher)
        result = self.db.execute(statement)
        return  result.scalars().all()

    def update_teacher(self, id, teacher: Teacher):
        self.db.commit()
        self.db.refresh(teacher)
        return  teacher

    def delete_teacher(self, teacher: Teacher):
        self.db.delete(teacher)
        return None