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