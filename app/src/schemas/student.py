from pydantic import BaseModel, Field


class StudentCreate(BaseModel):
    user_id: int

    course: str = Field(
        ...,
        min_length=1,
        max_length=250
    )

    batch: str = Field(
        ...,
        min_length=1,
        max_length=250
    )


class StudentResponse(BaseModel):
    id: int
    course: str
    batch: str
    user_id: int

    model_config = {
        "from_attributes": True
    }


class AssignStudentToTask(BaseModel):
    student_id: int