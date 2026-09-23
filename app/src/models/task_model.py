from typing import TYPE_CHECKING
from src.core.database import Base
from sqlalchemy import String, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship
from src.models.students_tasks_model import student_task
if TYPE_CHECKING:
    from src.models.user_model import User
    from src.models.teacher_model import Teacher
    from src.models.task_model import Task
    from src.models.student_model import Student

class Task(Base):
    __tablename__ = "tasks"

    id: Mapped[int] = mapped_column(primary_key=True)
    title: Mapped[str] = mapped_column(String(250), nullable=False)
    status: Mapped[str] = mapped_column(String(250), nullable=False)
    teacher_id: Mapped[int] = mapped_column(ForeignKey('teachers.id', ondelete="CASCADE"))

    teacher: Mapped['Teacher'] = relationship(
        'Teacher',
        back_populates='tasks'
    )

    students: Mapped[list['Student']] = relationship(
        'Student',
        back_populates="tasks",
        uselist=True,
        secondary="student_task"
    )