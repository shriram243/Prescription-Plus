from datetime import datetime
from typing import Optional, Any

from beanie import Document
from fastapi import Query
from Constants import constants as const
from pydantic import BaseModel, EmailStr

class AddressDetails(BaseModel):
    locality:Optional[str]
    city:Optional[str]
    pincode:Optional[int]
    state:Optional[str]

class Patient(Document):
    firstname: str
    lastname:Optional[str]
    email: Optional[EmailStr]
    mobile: str = Query(..., regex=const.PHONE_NO_REGEX)
    whatsapp:Optional[str]
    Id:Optional[str]
    address:Optional[AddressDetails]
    sex:Optional[str]
    age:Optional[int]
    created:Optional[datetime]
    updated:Optional[datetime]

class UpdatePatientModel(BaseModel):
    firstname: Optional[str]
    lastname:Optional[str]
    email: Optional[EmailStr]
    mobile: Optional[str]= Query(..., regex=const.PHONE_NO_REGEX)
    whatsapp:Optional[str]
    address:Optional[AddressDetails]
    sex:Optional[str]
    age:Optional[int]
    updated:Optional[datetime]


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
