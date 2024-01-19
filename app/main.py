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

# To enable CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# object of the Service Class where all the business logic is written
book_service = BookService()

# GET endpoint to fetch book based on ISBN
@app.get("/isbn/{isbn}")
async def get_book(
    isbn: str
):
    return book_service.get_book(isbn)
      
# GET endpoint to fetch all the book from the DB
@app.get("/books")
async def get_all_books():
   return book_service.get_all_books()
     
# PUT endpoint to add the book to the DB
@app.put("/books")
async def update_ticket_status(
    request: Request
):
    request_body = await request.json()
    isbn = request_body.get("isbn")
    return book_service.save_book(isbn)


if __name__ == "__main__":
    uvicorn.run("app.main:app", host="0.0.0.0", port=5001, reload=True)
