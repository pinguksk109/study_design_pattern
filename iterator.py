class Book:
    def __init__(self, title):
        self.title = title

class BookCollection:
    def __init__(self):
        self.books = []

    def add_book(self, book: Book):
        self.books.append(book)

    def __iter__(self):
        return BookIterator(self.books)

class BookIterator:
    def __init__(self, books):
        self.books = books
        self.index = 0

    def __next__(self):
        if self.index < len(self.books):
            book = self.books[self.index]
            self.index += 1
            return book
        raise StopIteration

library = BookCollection()
library.add_book(Book("Book A"))
library.add_book(Book("Book B"))
library.add_book(Book("Book C"))

for book in library:
    print(book.title)
