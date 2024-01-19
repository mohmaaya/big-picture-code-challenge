import uvicorn
import configparser
from fastapi import Depends, FastAPI, Request, HTTPException
from fastapi.responses import JSONResponse
from fastapi.middleware.cors import CORSMiddleware
from app.service.book_service import BookService

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

book_service = BookService()

@app.get("/isbn/{isbn}")
async def get_book(
    isbn: str
):
    print(isbn)
    return book_service.get_book(isbn)
      

@app.get("/books")
async def get_all_books():
   return book_service.get_all_books()
     

@app.put("/books")
async def update_ticket_status(
    request: Request
):
    request_body = await request.json()
    isbn = request_body.get("isbn")
    print(isbn)
    return book_service.save_book(isbn)

   

      
if __name__ == "__main__":
    uvicorn.run("app.main:app", host="0.0.0.0", port=5001, reload=True)
