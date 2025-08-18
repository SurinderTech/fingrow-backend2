from fastapi import FastAPI
from routers import login, signup, profile
from fastapi.middleware.cors import CORSMiddleware
from dotenv import load_dotenv
from fastapi.responses import JSONResponse
from fastapi.requests import Request
from fastapi.middleware.cors import CORSMiddleware
from routers import upload_photo
from routers import me
from routers import quiz 

# Load environment variables from .env
load_dotenv()

# Create FastAPI app
app = FastAPI(
    title="FinGrow Backend",
    version="1.0.0",
    description="Backend API for FinGrow finance app"
)

# CORS configuration
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # TODO: Change to ["http://localhost:3000"] or your frontend domain in production
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Exception handler for all unhandled errors
@app.exception_handler(Exception)
async def global_exception_handler(request: Request, exc: Exception):
    return JSONResponse(
        status_code=500,
        content={"error": str(exc)}
    )

# API routers
app.include_router(login.router, prefix="/api/v1", tags=["Login"])
app.include_router(signup.router, prefix="/api/v1", tags=["Signup"])
app.include_router(upload_photo.router, prefix="/api/v1")
app.include_router(me.router, prefix="/api/v1", tags=["User"])
app.include_router(profile.router, prefix="/api/v1", tags=["Profile"])
app.include_router(quiz.router, prefix="/api/v1", tags=["Quiz"]) 

# Health check endpoint
@app.get("/")
def root():
    return {"status": "Backend is working", "version": "1.0.0"}
