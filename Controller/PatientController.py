import imp
from typing import List, Union
# from datetime import datetime
import datetime
from beanie import PydanticObjectId

from Models.Patient import Patient

patient_collection = Patient


async def addPatient(patient: Patient) -> Patient:
    patient.created = datetime.datetime.now()
    patient.updated=datetime.datetime.now()
    ts = datetime.datetime.now().timestamp()
    ts = round(ts)
    patient.Id ="Pat"+str(ts)
    doc = await patient.create()
    return doc