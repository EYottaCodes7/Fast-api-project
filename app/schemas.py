from pydantic import BaseModel, EmailStr

# Base
class UserBase(BaseModel):
    email: EmailStr

# For creating user
class UserCreate(UserBase):
    password: str

# For reading user (response)
class UserRead(UserBase):
    id: int
    is_active: bool

    class Config:
        from_attributes = True