from decouple import config
import uvicorn
from fastapi import FastAPI, APIRouter,Request, Body, status
from fastapi.middleware.cors import CORSMiddleware
from motor.motor_asyncio import AsyncIOMotorClient

