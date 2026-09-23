from src.core.database import Base
from sqlalchemy import String, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship
from src.models.students_teachers_model import student_teacher
from src.models.students_tasks_model import student_task

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from src.models.user_model import User
    from src.models.teacher_model import Teacher
    from src.models.task_model import Task
    from src.models.student_model import Student

class Student(Base):
    __tablename__ = "students"
    id: Mapped[int] = mapped_column(primary_key=True)
    course: Mapped[str] = mapped_column(String(250), nullable=False)
    batch: Mapped[str] = mapped_column(String(250), nullable=False)
    user_id: Mapped[int] = mapped_column(ForeignKey("users.id", ondelete="CASCADE"), nullable=False, unique=True)

    user: Mapped['User'] = relationship(
        'User',
        back_populates="student",
        uselist=False
    )

    tasks: Mapped[list['Task']] = relationship(
        'Task',
        back_populates="students",
        uselist=True,
        secondary=student_task
        # cascade="all, delete-orphan"
    )

    teachers: Mapped[list['Teacher']] = relationship(
        'Teacher',
        back_populates="students",
        uselist=True,
        secondary=student_teacher
    )