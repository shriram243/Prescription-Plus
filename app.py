import imp
from fastapi import FastAPI, Depends

from auth.jwt_bearer import JWTBearer
from config.config import initiate_database
from Routes.AdminRoute import router as AdminRouter
from Routes.DoctorRoute import router as DoctorRouter
from Routes.PatientRoute import router as PatientRouter
from Routes.PrescriptionRoute import router as PrescriptionRouter
from Routes.ElasticSearchRoute import router as ElasticSearchRouter
from fastapi.middleware.cors import CORSMiddleware


app = FastAPI()

token_listener = JWTBearer()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
) 

@app.on_event("startup")
async def start_database():
    await initiate_database()


@app.get("/", tags=["Root"])
async def read_root():
    return {"message": "Welcome to this fantastic app."}


app.include_router(AdminRouter, tags=["Administrator"], prefix="/admin")
app.include_router(DoctorRouter, tags=["Administrator"], prefix="/doctor")
app.include_router(PatientRouter, tags=["Administrator"], prefix="/patient")
app.include_router(PrescriptionRouter, tags=["Administrator"], prefix="/rx")
app.include_router(ElasticSearchRouter, tags=[
                   'Administrator'], prefix="/search")
