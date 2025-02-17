from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.routers import users, services
from app.database.db import create_db_and_tables

#init database on app start
create_db_and_tables()

app = FastAPI(
    root_path="/api",
)
origins = [
    "http://localhost:5173",
    "http://localhost:8000",
]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/", name= "Api Status")
async def root():
    return {"status":"true", "message": "Smart Services Api server is running"}

app.include_router(
    users.router,
    prefix="/users",
    tags=["users"],
)

app.include_router(
    services.router,
    prefix="/services",
    tags=["services"],
)