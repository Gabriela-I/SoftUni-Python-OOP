from typing import List


class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.page = 0

    def turn_page(self, page):
        self.page = page


class Library:
    def __init__(self):
        self.books: List[Book] = []

    def add_book(self, book):
        self.books.append(book)

    def find_book(self, title):
        for b in self.books:
            if b.title == title:
                return book
        return None


book = Book('D', 'D.D')
library = Library()
library.add_book(book)
print(library.find_book('D'))
