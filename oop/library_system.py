class Book:
    def __init__(self, title: str, author: str):
        self.title = title
        self.author = author
    def __str__(self):
        return f"'{self.title}' by {self.author}"

#derived class1
class EBook(Book):
    def __init__(self, title: str, author: str, file_size: int):
        super().__init__(title, author)
        self.file_size = file_size
    def __str__(self):
        return f"'{self.title}' by {self.author} (EBook: {self.file_size})"

   #derived class2 
class PrintBook(Book):
    def __init__(self, title: str, author: str, page_count: int):
        super().__init__(title, author)
        self.page_count = page_count
    def __str__(self):
        return f"'{self.title}' by {self.author} (PrintBook, {self.page_count})"

#composition Class

class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book: Book):
        self.books.append(book)
        print(f"Added {book.title} to the library.")
        
    def list_books(self):
        if not self.books:
            print("No books in the library.")
        else:
            print("Books in the library:")
            for book in self.books:
                print(f" - {book}")
