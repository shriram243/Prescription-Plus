from typing import Optional

from beanie import init_beanie
from motor.motor_asyncio import AsyncIOMotorClient
from pydantic import BaseSettings

from Models.Admin import Admin
from Models.Doctor import Doctor
from Models.Patient import Patient
from Models.Prescription import Prescription


class Settings(BaseSettings):
    # database configurations
    DATABASE_URL: Optional[str] = None

    # JWT
    secret_key: str 
    algorithm: str = "HS256"

    class Config:
        env_file = ".env.dev"
        orm_mode = False


async def initiate_database():
    client = AsyncIOMotorClient(Settings().DATABASE_URL)
    await init_beanie(database=client.get_default_database(),
                      document_models=[Admin,Doctor,Patient,Prescription])
