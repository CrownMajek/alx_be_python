class Book:
    def __init__(self, title: str, author: str):
        self.title = title
        self.author = author
    def display_info(self):
        print(f"Book: {self.title} by {self.author}")

#derived class1
class EBook(Book):
    def __init__(self, title: str, author: str, file_size: int):
        super().__init__(title, author)
        self.file_size = file_size
    
    def display_info(self):
        print(f"EBook: {self.title} by {self.author}, File Size: {self.file_size}KB")

   #derived class2 
class PrintBook(Book):
    def __init__(self, title: str, author: str, page_count: int):
        super().__init__(title, author)
        self.page_count = page_count
    def display_info(self):
        print(f"PrintBook: {self.title} by {self.author}")

#composition Class

class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)
        print(f"Added {book.title} to the library.")
        
    def list_books(self):
        for book in self.books:
            book.display_info()
