# A program with a base class Book and two derived classes, EBook and PrintBook, showcasing inheritance and a library class that uses them all.
#Base class
class Book:
    def __init__(self, title="", author=""):
        self.title = title
        self.author = author
    def __str__(self):
       return f"{self.title} by {self.author}."    

#Derived class
class EBook(Book):
    def __init__(self, title, author, file_size):
        super().__init__(title, author) #Called the parent class constructor
        self.file_size = file_size
    def __str__(self):
       return f"{self.title} by {self.author}."

#Derived class
class PrintBook(Book):
    def __init__(self, title, author, page_count):
        super().__init__(title, author) #Called the parent class constructor
        self.page_count = page_count
    def __str__(self):
       return f"{self.title} by {self.author}, of {self.page_count} pages"

class Library:
    def __init__ (self):
        self.books = []

    def add_book(self, books):
        self.books.append(books)

    # def list_book(self):
    #     for every book in self.books:
    #         if the book belongs to class Ebook:
    #            print(f"EBook: {self.title} by {self.author}, File Size: {self.file_size}") 
    #         elif the book belongs to class Book:
    #             print(f"Book: {self.title} by {self.author}")
    #         else:
    #             print(f"PrintBook: {self.title} by {self.author}, Page Count: {self.page_count}")

    def list_books(self):
        for book in self.books:
            if isinstance(book, EBook):
                print(f"EBook: {book.title} by {book.author}, File Size: {book.file_size}KB")
            elif isinstance(book, PrintBook):
                print(f"PrintBook: {book.title} by {book.author}, Page Count: {book.page_count}")
            else:
                print(f"Book: {book.title} by {book.author}")
