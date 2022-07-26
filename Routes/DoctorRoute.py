from fastapi import APIRouter, Body

from database.database import *
from Models.Doctor import *
from Controller.DoctorController import *

router = APIRouter()


@router.post("/addDoc", response_description="Doctor data added into the database", response_model=Response)
async def addDoctorRoute(doctor: Doctor = Body(...)):
    print("check")
    new_doc = await addDoctor(doctor)
    if new_doc:
        return {
            "status_code": 200,
            "response_type": "success",
            "description": "Doctor created successfully",
            "data": new_doc
        }
    else:
        return {
            "status_code": 404,
            "response_type": "error",
            "description": "Unable to add to DB",
            "data": False
            }


@router.get('/', response_description="Doctor Details fetched Successfully", response_model=Response)
async def findDocbyIdRoute(Id:Optional[str]):
    rx = await findDocbyId(Id)
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
            "description": "An error occurred. Doctor with ID: {} not found".format(Id),
            "data": False
            }

@router.get('/_id/', response_description="Doctor Details Successfully", response_model=Response)
async def findDocby_idRoute(id: PydanticObjectId):
    rx = await findDocby_Id(id)
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
            "description": "An error occurred. Doctor with ID: {} not found".format(id),
            "data": False
            }

@router.put("/updateDoc/{id}", response_model=Response)
async def UpdateDocRoute(id: PydanticObjectId, rx: UpdateDoctorModel = Body(...)):
    updatedRx = await UpdateDoc(id, rx.dict())
    if updatedRx:
        return {
            "status_code": 200,
            "response_type": "success",
            "description": "Doctor with ID: {} updated".format(id),
            "data": updatedRx
        }
    return {
        "status_code": 404,
        "response_type": "error",
        "description": "An error occurred. Doctor with ID: {} not found".format(id),
        "data": False
    }