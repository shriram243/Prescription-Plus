from fastapi import APIRouter, Body

from database.database import *
from Models.Patient import *
from Controller.PatientController import *

router = APIRouter()

@router.post("/addPatient", response_description="Patient data added into the database", response_model=Response)
async def addPatientRoute(patient: Patient= Body(...)):
    new_patient = await addPatient(patient)
    return {
        "status_code": 200,
        "response_type": "success",
        "description": " Patient Added successfully",
        "data": new_patient
    }


@router.get('/', response_description="Patient Details fetched Successfully", response_model=Response)
async def findPatientbyIdRoute(Id:Optional[str]):
    rx = await findPatientbyId(Id)
    if rx:
        return {
            "status_code": 200,
            "response_type": "success",
            "description": "Data fetched successfully",
            "data": rx
        }
    else:
        return {
            "status_code": 404,
            "response_type": "error",
            "description": "An error occurred. Patient with ID: {} not found".format(Id),
            "data": False
            }

@router.get('/_id/', response_description="Patient Details Successfully", response_model=Response)
async def findPatientby_idRoute(id: PydanticObjectId):
    rx = await findPatientby_Id(id)
    if rx:
        return {
            "status_code": 200,
            "response_type": "success",
            "description": "Data fetched successfully",
            "data": rx
        }
    else:
        return {
            "status_code": 404,
            "response_type": "error",
            "description": "An error occurred. Patient with ID: {} not found".format(id),
            "data": False
            }

@router.put("/updatePatient/{id}", response_model=Response)
async def UpdateDocRoute(id: PydanticObjectId, rx: UpdatePatientModel = Body(...)):
    updatedRx = await UpdatePatient(id, rx.dict())
    if updatedRx:
        return {
            "status_code": 200,
            "response_type": "success",
            "description": "Student with ID: {} updated".format(id),
            "data": updatedRx
        }
    return {
        "status_code": 404,
        "response_type": "error",
        "description": "An error occurred. Student with ID: {} not found".format(id),
        "data": False
    }
