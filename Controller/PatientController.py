from typing import List, Union
# from datetime import datetime
import datetime
from beanie import PydanticObjectId
from fastapi import File

from Models.Patient import Patient

patient_collection = Patient


async def addPatient(patient: Patient) -> Patient:
    try:
        patient.created = datetime.datetime.now()
        patient.updated=datetime.datetime.now()
        ts = datetime.datetime.now().timestamp()
        ts = round(ts)
        patient.Id ="Pat"+str(ts)
        doc = await patient.create()
        return doc
    except:
        return False

async def findPatientbyId(Id)->Patient:
    try:
        rx = await patient_collection.find_one({'Id':Id})
    except:
        return "Error Occur"
    return rx

async def findPatientby_Id(_id)->Patient:
    try:
        rx = await patient_collection.get(_id)
    except:
        return "Error Occur"
    return rx

async def UpdatePatient(id,data:dict)->Union[bool, Patient]:
    try:
        data['updated'] = datetime.datetime.now()
        des_body = {k: v for k, v in data.items() if v is not None}
        update_query = {"$set": {
            field: value for field, value in des_body.items()
        }}
        patient = await patient_collection.get(id)
        print(update_query)
        if patient:
            await patient.update(update_query)
            return patient
        else:
            return False
    except:
        return False

async def UploadRx(file:File,id:PydanticObjectId)->Union[bool,Patient]:
    try:
        FilePath = "./Uploaded Rx/{id}"
        filename = file.filename 
        patient = await patient_collection.get(id)
        file_content = await file.read() 
        # contents = file.file.read()
        with open(FilePath+patient.Id+".pdf",'wb') as out_file:
            out_file.write(file_content )
        return filename
    except:
        return "Unable to Upload File in MongoDb"