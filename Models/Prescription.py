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

class CouncilDetails(BaseModel):
    state:str
    id:str

class DoctorDetails(BaseModel):
    firstname:str
    lastname:Optional[str]
    Id:str
    degree:str
    council:Optional[CouncilDetails]
    mobile:str = Query(..., regex=const.PHONE_NO_REGEX)
    signature:Optional[str]
    address:Optional[AddressDetails]

class PatientDetails(BaseModel):
    firstname:str
    lastname:Optional[str]
    Id:str
    unique_health_id:Optional[str]
    mobile:str = Query(..., regex=const.PHONE_NO_REGEX)
    address:Optional[AddressDetails]
    sex:Optional[str]
    age:int

class ComplaintsDetails(BaseModel):
    term:str
    sctid:Optional[str]
    duration:Optional[str]
    severity:Optional[str]
    additional_info:Optional[str]

class DurationDetails(BaseModel):
    frequency:Optional[int]
    type:Optional[str]

class MedicineDetails(BaseModel):
    term:str
    sctid:Optional[str]
    fkid:Optional[str]
    dosage:Optional[str]
    duration:Optional[DurationDetails]
    when:Optional[str]
    quantity:Optional[str]
    additional_info:Optional[str]

class LabTestDetails(BaseModel):
    term:Optional[str]
    id:Optional[str]
    additional_info:Optional[str]

class FollowUpDateDetails(BaseModel):
    next:Optional[int]
    type:Optional[str]
    date:Optional[str]

class Prescription(Document):
    doctor_details:Optional[DoctorDetails]
    patient_details:Optional[PatientDetails]
    complaints:Optional[list[ComplaintsDetails]]
    medicine:Optional[list[MedicineDetails]]
    advice:Optional[str]
    labtest:Optional[list[LabTestDetails]]
    follow_up_date:Optional[FollowUpDateDetails]
    pdf:Optional[str]
    picture:Optional[str]
    Id:Optional[str]
    created:Optional[datetime]
    updated:Optional[datetime]


class UpdatePrescriptionModel(BaseModel):
    doctor_details:Optional[DoctorDetails]
    patient_details:Optional[PatientDetails]
    complaints:Optional[list[ComplaintsDetails]]
    medicine:Optional[list[MedicineDetails]]
    advice:Optional[str]
    labtest:Optional[list[LabTestDetails]]
    follow_up_date:Optional[FollowUpDateDetails]
    pdf:Optional[str]
    picture:Optional[str]
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
 