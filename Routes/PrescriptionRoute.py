from fastapi import APIRouter, Body

from database.database import *
from Models.Prescription import *
from Controller.PrescriptionController import *

router = APIRouter()

@router.post("/addRx", response_description="Prescription data added into the database", response_model=Response)
async def addRxRoute(prescription : Prescription= Body(...)):
    new_rx = await addRx(prescription)
    if new_rx:
        return {
            "status_code": 201,
            "response_type": "success",
            "description": "Prescreption created successfully",
            "data": new_rx
        }
    else:
        return {
            "status_code": 404,
            "response_type": "error",
            "description": "An error occurred. Unale to create Rx",
            "data": False
            }
    
    

@router.get('/', response_description="Prescription fetched Successfully", response_model=Response)
async def findRxbyIdRoute(Id:Optional[str]):
    rx = await findRxbyId(Id)
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
            "description": "An error occurred. Rx with ID: {} not found".format(Id),
            "data": False
            }

@router.get('/_id/', response_description="Prescription fetched Successfully", response_model=Response)
async def findRxby_idRoute(id: PydanticObjectId):
    rx = await findRxby_Id(id)
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
            "description": "An error occurred. Rx with ID: {} not found".format(id),
            "data": False
            }


@router.get('/doc/', response_description="Prescription fetched Successfully", response_model=Response)
async def findRxbyDocIdRoute(docId:Optional[str]):
    rx = await findRxbyDocId(docId)
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
            "description": "An error occurred. Rx with ID: {} not found".format(docId),
            "data": False
            }

@router.get('/patient/', response_description="Prescription fetched Successfully", response_model=Response)
async def findAllofPatientRxRoute(patientId:Optional[str]):
    rx = await findAllofPatientRx(patientId)
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
            "description": "An error occurred. Rx with ID: {} not found".format(patientId),
            "data": False
            }


@router.get('/unique/', response_description="Prescription fetched Successfully", response_model=Response)
async def findAllofPatientRxRoute(unique_health_id:Optional[str]):
    rx = await findAllofPatientRxbyUniqueHealthId(unique_health_id)
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
            "description": "An error occurred. Rx with ID: {} not found".format(unique_health_id),
            "data": False
            }

@router.put("/updateRx/{id}", response_model=Response)
async def UpdateRxRoute(id: PydanticObjectId, rx: UpdatePrescriptionModel = Body(...)):
    updatedRx = await UpdateRx(id, rx.dict())
    if updatedRx:
        return {
            "status_code": 200,
            "response_type": "success",
            "description": "Rx with ID: {} updated".format(id),
            "data": updatedRx
        }
    return {
        "status_code": 404,
        "response_type": "error",
        "description": "An error occurred. Rx with ID: {} not found".format(id),
        "data": False
    }