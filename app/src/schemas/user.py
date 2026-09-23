# from pydantic import BaseModel
# from typing import Literal

# class UserSchema(BaseModel):
#     name: str
#     username: str
#     email: str
#     password: str
#     role: str = Literal["Teacher", "Student"]

# class UserResponseSchema(BaseModel):
#     name: str
#     username: str
#     email: str
#     role: str = Literal["Teacher", "Student"]

# class UserUpdateSchema(BaseModel):
#     username: str
#     email: str
#     password: str