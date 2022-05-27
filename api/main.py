from fastapi import FastAPI
from . import  models
from .database import engine
from  .routers import student,address

models.Base.metadata.create_all(engine)

app = FastAPI()

app.include_router(student.router)
app.include_router(address.router)