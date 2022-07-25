from datetime import datetime
from typing import Optional, Any

from beanie import Document
from fastapi import Query
from Constants import constants as const
from pydantic import BaseModel, EmailStr

class MedicineDetails(BaseModel):
    name:str
    sctid:Optional[str]
    fkid:Optional[str]
    frequency:int=0

class Medicine(Document):
    docID:str
    medicines:Optional[list[MedicineDetails]]
    ID:str


class Response(BaseModel):
    status_code: int
    response_type: str
    description: str
    data: Optional[Any]

    class Config:
        schema_extra = {
            "example": {
                "status_code": 200,
                "response_type": "success",
                "description": "Operation successful",
                "data": "Sample data"
            }
        }
