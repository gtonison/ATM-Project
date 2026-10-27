from fastapi import FastAPI
from uuid import UUID

app = FastAPI()

books = {}

book_data = {"id": 0, "title": "", "author": "",
             "year": 0, "pages": 0, "language": ""}


@app.get("/")
def home():
    return {"message": "hello from the books api"}


@app.get("/books")
def get_books():
    return books


@app.get("/book/{id}")
def get_book_by_id(id: str):
    book = books.get(id)
    if not book:
        return {"message": "book not found"}
    return book


@app.post("/books")
def add_book(
    title: str, author: str, year: int, language: str, pages: str
):
    new_book = book_data.copy
    new_book["id"] = str(UUID(int=len(books)))
    new_book["year"] = year
    new_book["pages"] = pages
    new_book["language"] = language
    new_book["author"] = author
    new_book["title"] = title
