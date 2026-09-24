from src.interface.task_interface import TaskInterface
from sqlalchemy.orm import Session
from sqlalchemy import select
from src.models.task_model import Task

class StudentRepository(TaskInterface):
    def __init__(self, db: Session):
        self.db = db

    def create_task(self, task: Task):
        self.db.add(task)
        self.db.commit()
        self.db.refresh(task)
        return task

    def get_task(self, id):
        statment = select(Task).where(id == Task.id)
        result = self.db.execute(statment)
        return result.scalar_one_or_none()

    def get_all_tasks(self):
        statement = select(Task)
        result = self.db.execute(statement)
        return  result.scalars().all()

    def update_task(self, id, task: Task):
        self.db.commit()
        self.db.refresh(task)
        return task

    def update_task_by_id_and_student_id(self, task: Task):
        self.db.commit()
        self.db.refresh(task)
        return task
        
    def delete_task(self, task: Task):
        self.db.delete(task)
        return None

    def delete_task_by_id_and_student_id(self, task):
        self.db.delete(task)
        return None