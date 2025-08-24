import os
import sys
from dotenv import load_dotenv

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.database import Base
from app.db import init_db
from app.routers import auth, user, resume

# Load environment variables early
load_dotenv()

# Add project root to sys.path for imports (Windows friendly)
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

# Create FastAPI app instance once at the top
app = FastAPI(
    title="AI Career Navigator Backend",
    version="0.2.0",
    description="Backend with Auth, Resume Parsing, Career Advice, Analytics, Learning Plans, and Trends."
)

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # tighten in production
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include your routers after app creation
app.include_router(auth.router, prefix="/auth", tags=["auth"])
app.include_router(user.router, prefix="/user", tags=["user"])
app.include_router(resume.router, prefix="/resume", tags=["resume"])

# Initialize database on startup
@app.on_event("startup")
def on_startup():
    init_db()

# Root health check endpoint
@app.get("/", tags=["health"])
def root():
    return {"message": "Backend is running"}
