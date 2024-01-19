import React, { useState, useEffect } from "react";
import BookCard from "./BookCard";
import "./IndexPage.css";
import { bookHTTPService } from "./api/books.service";
import { Book } from "./types/book";

const IndexPage = () => {
    const [book, setBook] = useState<Book | null>();
    const [allBooks, setAllBooks] = useState<Book[] | null>();
    const [searchValue, setSearchValue] = useState("");
    const [message, setMessage] = useState<string | null>(null);


    const fetchAllBooks = async () => {
        try {
            const books = await bookHTTPService.getAllBooks();
            setAllBooks(books);
            setBook(null)
            setMessage(null);
        } catch (error: any) {
            setMessage(`${error.response.data.detail}`);
        }
    };

    const handleSearch = async () => {
        const isbn = encodeURIComponent(searchValue);
        try {
            const book = await bookHTTPService.getBook(isbn);
            setBook(book);
            setAllBooks(null);
            setMessage(null);
        } catch (error: any) {
            setMessage(`${error.response.data.detail}`);
        }
    };

    const handleAddToDatabase = async () => {
        if (book) {
            try {
               const response =  await bookHTTPService.addToDatabase(searchValue);
                   
               if(response) {
                   setMessage(response.detail);
               }
   
            } catch (error: any) {
                setMessage(`${error.response.data.detail}`);
            }
        }
    };

    return (
        <div className="container">
            <h1 className="heading">Find Books based on ISBN</h1>

            <div className="search-container">
                <input
                    className="text-input"
                    type="text"
                    placeholder="Enter the isbn number of a book. Eg: 9780590353427"
                    value={searchValue}
                    onChange={(e) => setSearchValue(e.target.value)}
                />
                <div className="button-container">
                <button className="button" onClick={handleSearch}>
                    Search
                </button>
                <button className="button" onClick={fetchAllBooks}>
                    Show All Books
                    </button>
                </div>
            </div>

            {book && (
                <div>
                    <h2>Book with the corresponding ISBN is:</h2>
                    <BookCard book={book} />
                    <button className="button" onClick={handleAddToDatabase}>
                        Add to Database
                    </button>
                </div>
            )}

            {message && <div className="error-message">{message}</div>}

            {allBooks && (
                <div className="book-card-container">
                    {allBooks.map((book) => (
                        <BookCard key={book.isbn} book={book} />
                    ))}
                </div>
            )}
        </div>
    );
};

export default IndexPage;
