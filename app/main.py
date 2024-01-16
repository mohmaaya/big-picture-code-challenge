import uvicorn
import configparser
from fastapi import Depends, FastAPI, Request, HTTPException
from fastapi.responses import JSONResponse
from fastapi.middleware.cors import CORSMiddleware
from app.repositories.pymongo_get_database import get_database 

app = FastAPI()

origins = [
    "http://localhost:3000", 
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

db = get_database()
collection_name = db["user_books"]


if __name__ == "__main__":
    uvicorn.run("app.main:app", host="0.0.0.0", port=5001, reload=True)
