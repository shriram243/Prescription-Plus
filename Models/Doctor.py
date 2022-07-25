from datetime import datetime
from typing import Optional, Any

from beanie import Document
from fastapi import Query
from Constants import constants as const
from pydantic import BaseModel, EmailStr

class AddressDetails(BaseModel):
    locality:str
    city:str
    pincode:int
    state:str

class CouncilDetails(BaseModel):
    state:str
    id:str

class Doctor(Document):
    firstname: str
    lastname:str
    email: EmailStr
    mobile: str = Query(..., regex=const.PHONE_NO_REGEX)
    mci: str
    degree: str
    signature:str
    Id:Optional[str]
    council:Optional[CouncilDetails]
    visitingCard:str
    documents:Optional[list[str]]
    address:Optional[AddressDetails]
    sex:str
    age:int
    created:Optional[datetime]
    updated:Optional[datetime]


    class Config:
        schema_extra = {
            "example": {
                "fullname": "Abdulazeez Abdulazeez Adeshina",
                "email": "abdul@school.com",
                "course_of_study": "Water resources engineering",
                "year": 4,
                "gpa": "3.76"
            }
        }


class UpdateStudentModel(BaseModel):
    fullname: Optional[str]
    email: Optional[EmailStr]
    course_of_study: Optional[str]
    year: Optional[int]
    gpa: Optional[float]

    class Collection:
        name = "student"

    class Config:
        schema_extra = {
            "example": {
                "fullname": "Abdulazeez Abdulazeez",
                "email": "abdul@school.com",
                "course_of_study": "Water resources and environmental engineering",
                "year": 4,
                "gpa": "5.0"
            }
        }


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
