from src.core.database import Base
from sqlalchemy import String, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship
from src.models.students_teachers_model import student_teacher

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from src.models.user_model import User
    from src.models.teacher_model import Teacher
    from src.models.task_model import Task
    from src.models.student_model import Student

class Teacher(Base):
    __tablename__ = "teachers"
    id: Mapped[int] = mapped_column(primary_key=True)
    subject: Mapped[str] = mapped_column(String(250), nullable=False)
    user_id: Mapped[int] = mapped_column(ForeignKey("users.id", ondelete="CASCADE"), nullable=False, unique=True)

    user: Mapped['User'] = relationship(
        'User',
        back_populates="teacher",
        uselist=False
    )

    tasks: Mapped[list['Task']] = relationship(
        'Task',
        back_populates="teacher",
        uselist=True,
        cascade="all, delete-orphan"
    )

    students: Mapped[list['Student']] = relationship(
        'Student',
        back_populates="teachers",
        uselist=True,
        secondary=student_teacher
    )