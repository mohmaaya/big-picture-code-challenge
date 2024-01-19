
from app.repository.book_repository import get_database
import json
from typing import Optional
from fastapi import HTTPException
import requests

class BookService:
    def __init__(self):
       self.dbname = get_database()
       self.collection_name = self.dbname["user_books"]


    def extract_book_info(self,book_data):
    
        author = book_data.get('authors', [{}])[0].get('name', None)
        title = book_data.get('title', '')
        summary = book_data.get('subtitle', '')
        cover_url_medium = book_data.get('cover', {}).get('medium', '')
        

        return {
            "author": author,
            "title": title,
            "summary": summary,
            "cover_url_medium": cover_url_medium
        }
    
    def get_book(self, isbn: str):

        api_url = f"http://openlibrary.org/api/volumes/brief/isbn/{isbn}.json"

        response = requests.get(api_url)
        if response.status_code == 200:
            data = response.json()

            if "items" in data:

                items_list = data.get('items', [])
                match_type = items_list[0].get("match", None) if items_list else None
                if match_type in ["exact", "similar", None]:

                    records = data["records"]
                    first_book_key, first_book_data = next(iter(records.items()))
                    book_info = self.extract_book_info(first_book_data['data'])
        
                    return book_info

                else:
                     raise HTTPException(status_code=400, detail="Invalid match type")
                 
            else:
                raise HTTPException(status_code=404, detail="No book found for the ISBN")
        else:
           raise HTTPException(status_code=response.status_code, detail="Failed to fetch data from the Open Library API")
    
    
    def save_book(self, isbn: str):

        if isbn is None:
            raise HTTPException(status_code=400, error="ISBN is empty")

        if self.collection_name.find_one({"isbn": isbn}):
            raise HTTPException(status_code=400, detail="Book with this ISBN already exists")

        book_details = self.get_book(isbn)
        book_details["isbn"] = isbn

        self.collection_name.insert_one(book_details)

        raise HTTPException(status_code=200, detail="Book Saved")

    def get_all_books(self):

        cursor = self.collection_name.find()
        all_books = []

        for document in cursor:
        
            book_dict = {
                'author': document['author'],
                'title': document['title'],
                'summary': document['summary'],
                'cover_url_medium': document['cover_url_medium']  
            }

            all_books.append(book_dict)
       
        return all_books
