from pydantic import BaseModel, Field


class TeacherCreate(BaseModel):
    user_id: int

    subject: str = Field(
        ...,
        min_length=1,
        max_length=250
    )


class TeacherResponse(BaseModel):
    id: int
    subject: str
    user_id: int

    model_config = {
        "from_attributes": True
    }


class AssignStudentToTeacher(BaseModel):
    student_id: int