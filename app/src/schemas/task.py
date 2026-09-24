from pydantic import BaseModel, Field


class TaskCreate(BaseModel):
    title: str = Field(
        ...,
        min_length=1,
        max_length=250
    )

    status: str = Field(
        ...,
        min_length=1,
        max_length=250
    )


class TaskResponse(BaseModel):
    id: int
    title: str
    status: str
    teacher_id: int

    model_config = {
        "from_attributes": True
    }