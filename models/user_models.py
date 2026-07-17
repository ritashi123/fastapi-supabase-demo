from datetime import  datetime
from typing import Literal, Optional
from uuid import UUID
from pydantic import BaseModel, EmailStr, Field

class UserRegister (BaseModel):
    full_name: str = Field(..., min_length=3, max_length=50)
    email: EmailStr
    password: str = Field(..., min_length=8, max_length=50)

class UserLogin (BaseModel):
    email: EmailStr
    password: str = Field(..., min_length=8, max_length=50)    

class UserResponse (BaseModel):
    id: UUID
    full_name: str
    email: EmailStr
    role: Literal["user", "admin"] 
    is_active: bool
    created_at: datetime
    
class UserActionResponse (BaseModel):
    message: str
    user: UserResponse


