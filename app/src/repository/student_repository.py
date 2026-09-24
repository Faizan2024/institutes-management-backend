from src.interface.student_interface import StudentInterface
from sqlalchemy.orm import Session
from sqlalchemy import select
from src.models.student_model import Student

class StudentRepository(StudentInterface):
    def __init__(self, db: Session):
        self.db = db

    def create_student(self, student: Student):
        self.db.add(student)
        self.db.commit()
        self.db.refresh(student)
        return student

    def get_student(self, id):
        statment = select(Student).where(id == Student.id)
        result = self.db.execute(statment)
        return result.scalar_one_or_none()

    def get_all_students(self):
        statement = select(Student)
        result = self.db.execute(statement)
        return  result.scalars().all()

    def update_student(self, id, student: Student):
        self.db.commit()
        self.db.refresh(student)
        return  student

    def delete_student(self, student: Student):
        self.db.delete(student)
        return   None