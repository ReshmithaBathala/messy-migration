from pydantic import BaseModel, EmailStr, ValidationError
from typing import Optional


class UserCreateSchema(BaseModel):
    name: str
    email: EmailStr
    password: str

class UserUpdateSchema(BaseModel):
    name: str
    email: EmailStr

class LoginSchema(BaseModel):
    email: EmailStr
    password: str
