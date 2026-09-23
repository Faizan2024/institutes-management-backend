from src.core.database import Base
from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from src.models.user_model import User
    from src.models.teacher_model import Teacher
    from src.models.task_model import Task
    from src.models.student_model import Student

class User(Base):
    __tablename__ = "users"
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(250), nullable=False)
    username: Mapped[str] = mapped_column(String(250), nullable=False, unique=True)
    email: Mapped[str] = mapped_column(String(250), nullable=False, unique=True)
    password: Mapped[str] = mapped_column(String(250), nullable=False)
    role: Mapped[str] = mapped_column(String(30), nullable=False)

    teacher: Mapped['Teacher'] = relationship(
        'Teacher',
        back_populates="user",
        uselist=False,
        cascade="all, delete-orphan"
    )

    student: Mapped['Student'] = relationship(
        'Student',
        back_populates="user",
        uselist=False,
        cascade="all, delete-orphan"
    )