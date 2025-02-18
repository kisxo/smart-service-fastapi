from pygments.lexer import default
from sqlmodel import Field, SQLModel
from pydantic import BaseModel

class User(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    phone: int = Field(unique=True)
    name: str
    password: str

class UserCreate(BaseModel):
    phone: int
    name: str
    password: str