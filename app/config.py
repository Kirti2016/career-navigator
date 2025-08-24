from pydantic import BaseModel
from fastapi_jwt_auth import AuthJWT

# Settings class to hold JWT secret key
class Settings(BaseModel):
    authjwt_secret_key: str = "your-secret-key"  # Replace with a strong secret key in production!

# Function to load the JWT config for fastapi-jwt-auth
@AuthJWT.load_config
def get_config():
    return Settings()
