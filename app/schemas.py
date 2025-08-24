# app/schemas.py

from pydantic import BaseModel, EmailStr, constr
from pydantic import BaseModel

class TokenRefreshRequest(BaseModel):
    refresh_token: str


class UserCreate(BaseModel):
    email: EmailStr          # Ensures the email is valid format
    password: constr(min_length=6)  # Enforces minimum length 6 for password
