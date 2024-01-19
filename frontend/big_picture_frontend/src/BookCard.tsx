import { Book } from './types/book';
import "./BookCard.css"; 

// This function is for showing details of each book as in a card 
const BookCard = (props: { book: Book; }) => {
    const book = props.book;

    return (
        <div className="book-card">
            {book.cover_url_medium ? (
                <img src={book.cover_url_medium} alt="BookCard" className="book-card-image" />
            ) : (
                <div className="book-card-image no-image">Image not provided</div>
            )}
            <div className="book-card-body">
                <h3 className="book-card-details">Author: {book.author}</h3>
                <h3 className="book-card-details">Title: {book.title}</h3>
                <h3 className="book-card-details"> Summary: {book.summary}</h3>
                
            </div>
        </div>
    );
};

export default BookCard;