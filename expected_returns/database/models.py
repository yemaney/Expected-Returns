from typing import Optional

from sqlmodel import Field, SQLModel


class GlobalCape(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    cape: float
    date: str


class CountryCape(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    cape: float
    country: str
    date: str
