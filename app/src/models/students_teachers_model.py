from sqlalchemy import Table, ForeignKey, Column
from src.core.database import Base

student_teacher = Table(
    "student_teacher",
    Base.metadata,
    Column("student_id",
           ForeignKey("students.id"), 
           primary_key=True
    ),
    
    Column("teacher_id",
            ForeignKey("teachers.id"), 
            primary_key=True
    )
)