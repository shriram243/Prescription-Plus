from fastapi import APIRouter, Body

from database.database import *
from Models.Prescription import *
from Controller.PrescriptionController import *

router = APIRouter()

@router.post("/addRx", response_description="Student data added into the database", response_model=Response)
async def addRxRoute(prescription : Prescription= Body(...)):
    print(prescription)
    new_rx = await addRx(prescription)
    return {
        "status_code": 200,
        "response_type": "success",
        "description": "Student created successfully",
        "data": new_rx
    }
