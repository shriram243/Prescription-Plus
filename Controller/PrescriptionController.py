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