# app/models/user.py
from pydantic import BaseModel, EmailStr

class UserCreate(BaseModel):
    email: EmailStr
    password: str
    full_name: str | None = None

class UserPublic(BaseModel):
    email: EmailStr
    full_name: str | None = None

# quick in-memory store for demo; replace with DB later
FAKE_USERS = {}  # email -> {"email":..., "hashed_password":..., "full_name":...}
