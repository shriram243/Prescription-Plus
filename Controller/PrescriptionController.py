import imp
from typing import List, Union
# from datetime import datetime
import datetime
from beanie import PydanticObjectId
from Models.Medicine import Medicine

from Models.Prescription import Prescription

prescription_collection = Prescription
medicine_collection = Medicine


async def addRx(prescription: Prescription) -> Prescription:
    try:
        prescription.created = datetime.datetime.now()
        prescription.updated=datetime.datetime.now()
        ts = datetime.datetime.now().timestamp()
        ts = round(ts)
        prescription.Id ="Rx"+str(ts)
        doc = await prescription.create()
        docID = prescription.doctor_details.Id
        # med = await medicine_collection.find_one({docID})
        # if(med):
        return doc
    except:
        return False

async def findRxbyId(Id)->Prescription:
    try:
        rx = await prescription_collection.find_one({'Id':Id})
    except:
        return "Error Occur"
    return rx

async def findRxby_Id(_id)->Prescription:
    try:
        rx = await prescription_collection.get(_id)
    except:
        return "Error Occur"
    return rx

async def findRxbyDocId(docId)->Prescription:
    try:
        rx = await prescription_collection.find_one({'doctor_details.Id':docId})
    except:
        return "Error Occur"
    return rx

async def findAllofPatientRx(patiendId)->Prescription:
    try:
        rx = await prescription_collection.find_one({'patient_details.Id':patiendId})
    except:
        return "Error Occur"
    return rx

async def findAllofPatientRxbyUniqueHealthId(id)->Prescription:
    try:
        rx = await prescription_collection.find_one({'patient_details.unique_health_id':id})
    except:
        return "Error Occur"
    return rx

async def UpdateRx(id,data:dict)->Union[bool, Prescription]:
    try:
        data['updated'] = datetime.datetime.now()
        des_body = {k: v for k, v in data.items() if v is not None}
        update_query = {"$set": {
            field: value for field, value in des_body.items()
        }}
        rx = await prescription_collection.get(id)
        print(rx)
        if rx:
            await rx.update(update_query)
            return rx
        else:
            return False
    except:
        return False