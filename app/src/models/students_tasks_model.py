from sqlalchemy import Table, ForeignKey, Column
from src.core.database import Base

student_task = Table(
    "student_task",
    Base.metadata,
    Column("student_id",
           ForeignKey("students.id"), 
           primary_key=True
    ),
    
    Column("task_id",
            ForeignKey("tasks.id"), 
            primary_key=True
    )
)