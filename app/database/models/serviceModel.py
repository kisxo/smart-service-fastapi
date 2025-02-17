from sqlmodel import Field, SQLModel
from pydantic import BaseModel

class Service(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    name: str
    phone: str
    category: str
    area: str

class ServiceCreate(BaseModel):
    name: str
    phone: str
    category: str
    area: str