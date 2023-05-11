from enum import Enum
from typing import Optional
from uuid import UUID, uuid4

from pydantic import BaseModel


class DataType(str, Enum):
    length = 'length'
    depth = 'depth'


class Entry(BaseModel):
    id: Optional[UUID] = uuid4()
    type: DataType
    value: list[float]
    comment: Optional[str]


class List(BaseModel):
    __root__: list[Entry]
