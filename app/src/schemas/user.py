from pydantic import BaseModel, EmailStr, Field


class UserCreate(BaseModel):
    name: str = Field(
        ...,
        min_length=2,
        max_length=250
    )

    username: str = Field(
        ...,
        min_length=3,
        max_length=250
    )

    email: EmailStr

    password: str = Field(
        ...,
        min_length=8,
        max_length=250
    )

    role: str = Field(
        ...,
        min_length=1,
        max_length=30
    )


class UserResponse(BaseModel):
    id: int
    name: str
    username: str
    email: EmailStr
    role: str

    model_config = {
        "from_attributes": True
    }