from fastapi import APIRouter, Body

from database.database import *
from Models.Patient import *
from Controller.PatientController import *

router = APIRouter()

@router.post("/addPatient", response_description="Student data added into the database", response_model=Response)
async def addPatientRoute(patient: Patient= Body(...)):
    new_patient = await addPatient(patient)
    return {
        "status_code": 200,
        "response_type": "success",
        "description": "Student created successfully",
        "data": new_patient
    }
