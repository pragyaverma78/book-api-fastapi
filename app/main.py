from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI(title="Mini Book API")

class Book(BaseModel):
    title: str
    author: str

books = []

@app.get("/")
def home():
    return {"message": "Book API is running"}

@app.get("/books")
def get_books():
    return books

@app.post("/books")
def add_book(book: Book):
    books.append(book.model_dump())
    return {"message": "Book added", "book": book}
