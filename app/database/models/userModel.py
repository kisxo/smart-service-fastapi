from pygments.lexer import default
from sqlmodel import Field, SQLModel
from pydantic import BaseModel

class User(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    phone: str = Field(unique=True)
    name: str
    password: str

class UserCreate(BaseModel):
    phone: str
    name: str
    password: str