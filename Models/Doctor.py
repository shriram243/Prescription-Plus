from datetime import datetime
from enum import unique
from typing import Optional, Any

from beanie import Document
from fastapi import Query
from Constants import constants as const
from pydantic import BaseModel, EmailStr, Field

class AddressDetails(BaseModel):
    name:Optional[str]
    locality:Optional[str]
    city:Optional[str]
    pincode:Optional[int]
    state:Optional[str]

class CouncilDetails(BaseModel):
    state:Optional[str]
    id:Optional[str]

class Doctor(Document):
    firstname: str
    lastname:Optional[str]
    email: Optional[EmailStr]
    mobile: str = Query(..., regex=const.PHONE_NO_REGEX)
    mci: Optional[str]
    degree: Optional[str]
    signature:Optional[str]
    Id:Optional[str]
    council:Optional[CouncilDetails]
    visitingCard:Optional[str]
    documents:Optional[list[str]]
    address:Optional[AddressDetails]
    sex:Optional[str]
    age:Optional[int]
    created:Optional[datetime]
    updated:Optional[datetime]

class UpdateDoctorModel(BaseModel):
    firstname:Optional[str]
    lastname:Optional[str]
    email: Optional[EmailStr]
    mobile: Optional[str ]= Query(..., regex=const.PHONE_NO_REGEX)
    mci: Optional[str]
    degree: Optional[str]
    signature:Optional[str]
    council:Optional[CouncilDetails]
    visitingCard:Optional[str]
    documents:Optional[list[str]]
    address:Optional[AddressDetails]
    sex:Optional[str]
    age:Optional[int]
    updated:Optional[datetime]

class Response(BaseModel):
    status_code: int
    response_type: str
    description: str
    data: Optional[Any]
