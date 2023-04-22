from pydantic import BaseModel
from enum import Enum

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