from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.routers.resolve import router
from app.database import create_table

app = FastAPI(
    title="Smart Problem Resolution Agent",
    description="A system that analyzes problems and suggests the appropriate department.",
    version="1.0.0"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

create_table()

app.include_router(router)


@app.get("/")
def home():
    return {
        "message": "Smart Problem Resolution Agent is running"
    }


@app.get("/health")
def health():
    return {
        "status": "healthy"
    }