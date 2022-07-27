from tkinter import N
from fastapi import APIRouter, Body, File, UploadFile
from fastapi.responses import FileResponse
import os
from database.database import *
from Models.Patient import *
from Controller.PatientController import *

router = APIRouter()

@router.post("/addPatient", response_description="Patient data added into the database", response_model=Response)
async def addPatientRoute(patient: Patient= Body(...)):
    new_patient = await addPatient(patient)
    if new_patient:
        return {
            "status_code": 200,
            "response_type": "success",
            "description": " Patient Added successfully",
            "data": new_patient
        }
    else:
        return {
            "status_code": 404,
            "response_type": "error",
            "description": "Not able to add patient in DB",
            "data": False
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
async def UpdatePatientRoute(id: PydanticObjectId, pat: UpdatePatientModel = Body(...)):
    updatedpat = await UpdatePatient(id, pat.dict())
    if updatedpat:
        return {
            "status_code": 200,
            "response_type": "success",
            "description": "Patient with ID: {} updated".format(id),
            "data": updatedpat
        }
    return {
        "status_code": 404,
        "response_type": "error",
        "description": "An error occurred. Patient with ID: {} not found".format(id),
        "data": False
    }

@router.post("/uploadRx/{id}")
async def UploadRxRoute(file: UploadFile,id:PydanticObjectId):
    rx = await UploadRx(file,id)
    if rx:
        return {
            "status_code": 200,
            "response_type": "success",
            "description": "Patient with ID: {} updated".format(id),
            "data":rx
        }
    else:
        return{
        "status_code": 404,
        "response_type": "error",
        "description": "An error occurred. Patient with ID: {} not found".format(id),
        "data": False
    }

@router.get("/getpdf/",response_model=Response)
async def GetRxPdfRoute(id:Optional[str]):
    rx = str(id)+".pdf"
    file_path = os.path.join("./Uploaded Rx/",rx)
    if os.path.exists(file_path):
        return FileResponse("./Uploaded Rx/"+rx)
    else:
        return {
            "status_code": 404,
            "response_type": "error",
            "description": "An error occurred. Rx with ID:{} not found".format(id),
            "data": False
            }
