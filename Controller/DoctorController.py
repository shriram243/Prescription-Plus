import imp
from typing import List, Union
# from datetime import datetime
import datetime
from beanie import PydanticObjectId

from Models.Doctor import Doctor

doctor_collection = Doctor


async def addDoctor(doctor: Doctor) -> Doctor:
    doctor.created = datetime.datetime.now()
    doctor.updated=datetime.datetime.now()
    ts = datetime.datetime.now().timestamp()
    ts = round(ts)
    doctor.Id ="Doc"+str(ts)
    doc = await doctor.create()
    return doc

async def findDocbyId(Id)->Doctor:
    try:
        rx = await doctor_collection.find_one({'Id':Id})
    except:
        return "Error Occur"
    return rx

async def findDocby_Id(_id)->Doctor:
    try:
        rx = await doctor_collection.get(_id)
    except:
        return "Error Occur"
    return rx

async def UpdateDoc(id,data:dict)->Union[bool, Doctor]:
    try:
        data['updated'] = datetime.datetime.now()
        des_body = {k: v for k, v in data.items() if v is not None}
        update_query = {"$set": {
            field: value for field, value in des_body.items()
        }}
        doc = await doctor_collection.get(id)
        print(doc)
        if doc:
            await doc.update(update_query)
            return doc
        else:
            return False
    except:
        return False