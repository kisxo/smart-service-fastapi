from sqlmodel import Field, SQLModel
from pydantic import BaseModel

class User(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    email: str = Field(unique=True)
    phone: str = Field(unique=True)
    name: str
    password: str

class UserCreate(BaseModel):
    email: str
    phone: str
    name: str
    password: str