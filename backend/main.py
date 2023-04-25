from dependencies import *

from routers.cars import router as cars_router


DB_URL = config("DB_URL", cast=str)
DB_NAME = config("DB_NAME", cast=str)

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

@app.on_event("startup")
async def startup_db_client():
    app.mongodb_client = AsyncIOMotorClient(DB_URL)
    app.mongodb = app.mongodb_client[DB_NAME]

@app.on_event("shutdown")
async def shutdown_db_client():
    app.mongodb_client.close()


# Add the cars router to the FastAPI instance
app.include_router(cars_router, prefix="/cars", tags=["cars"])

if __name__ == "__main__":
    uvicorn.run("main:app", reload=True)