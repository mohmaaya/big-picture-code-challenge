import axios from 'axios';
import { Book } from "../types/book"

export class bookHTTPService {


    public static async getBook(isbn: string): Promise<Book> {

        const response = await axios.get(`http://localhost:5001/isbn/${isbn}`);
        return response.data;
    }

    public static async getAllBooks(): Promise<Book[]> {

        const response = await axios.get("http://localhost:5001/books");
        return response.data;
    }

    public static async addToDatabase(isbn: string) {

        const response = await axios.put(`http://localhost:5001/books`, {
            isbn: isbn
        });

        return response.data;
    }


}