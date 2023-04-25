from pydantic import BaseModel, Field
from typing import Optional
from enum import Enum
from bson import ObjectId

#-----------------PyObjectId-----------------#
class PyObjectId(ObjectId):
    @classmethod
    def __get_validators__(cls):
        yield cls.validate

    @classmethod
    def validate(cls, v):
        if not ObjectId.is_valid(v):
            raise ValueError("Invalid object id")
        return ObjectId(v)

    @classmethod
    def __modify_schema__(cls, field_schema):
        field_schema.update(type="string")


#-----------------MongoBaseModel-----------------#
class MongoBaseModel(BaseModel):
    id: PyObjectId = Field(default_factory=PyObjectId, alias="_id")

    class Config:
        json_encoders = {
            ObjectId: str
        }
    
#-----------------CarBase-----------------#

class CarBase(MongoBaseModel):
    brand: str = Field(..., min_length=3, max_length=50)
    make: str = Field(..., min_length=3, max_length=50)
    year: int = Field(..., ge=1975, le=2023)
    price: int = Field(..., ge=0)
    km: int = Field(..., ge=0)
    cm3: int = Field(..., ge=0)

#-----------------UpdateCar-----------------#
class CarUpdate(MongoBaseModel):
    price: Optional[int] = Field(None, ge=0)

class CarDB(CarBase):
    pass



























#-----------------OLD Models-----------------#
class Petrol(str, Enum):
    petrol = "petrol"
    diesel = "diesel"
    cng = "cng"
    lpg = "lpg"


class InsertCar(BaseModel):
    name: str
    brand: str
    year: int

class InsertUser(BaseModel):
    username: str
    name: str