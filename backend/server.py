from fastapi import FastAPI, status, Path, Query, Body, Request, Header, Form, File, UploadFile, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from typing import Optional, Dict

#Other dependencies
import pandas as pd
import shutil
# Importing the helper functions
from helpers import InsertCar, InsertUser, Petrol


# Create a FastAPI instance
app = FastAPI()

origins = [
    "http://localhost:3000",
]

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.post("/upload")
async def upload(picture: UploadFile = File(...), brand: str = Form(...), model: str = Form(...)):
    #save the picture
    with open("saved_file.png", "wb") as buffer:
        shutil.copyfileobj(picture.file, buffer)
    return {
        "filename": picture.filename, 
        "brand": brand, 
        "model": model
    }

# get headers from request -- which client is making the request
@app.get("/headers")
async def read_headers(user_agent:str | None = Header(None)):
    return {"User-Agent":user_agent}

@app.get("/", status_code=status.HTTP_208_ALREADY_REPORTED)
async def raw_fa_response():
    return {
        "message":"fastapi response"
    }

@app.post("/carsmodel")
async def new_car_model(car:InsertCar):
    if car.year>2022:
        raise HTTPException(
            status.HTTP_406_NOT_ACCEPTABLE,
            detail="The car doesn’t exist yet!"
        )
    return {
        "message":car
    }

@app.post("/cars")
async def insert_car(data:Dict=Body(...)):
    print(data)
    return {"Message":data}

@app.post("/car/user")
async def new_car_model(car: InsertCar, user: InsertUser, code: int=Body(None) ):
    return {
        "car":car,
        "user":user,
        "code":code
    }

@app.get("/cars")
async def raw_request(request: Request):
    return {"Message":request.base_url, "Query":request.query_params, "all":dir(request)}

@app.get("/cars/price")
async def car_by_price( min_price: int=0, max_price: int=100000 ):
    return {"Message":f'Car price between {min_price} and {max_price}'}

@app.get("/")
async def root():
    return {"Hello": "World"}

