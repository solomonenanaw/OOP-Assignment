# Base class
class Book:
    def __init__(self, title, author, pages, genre):
        self.title = title
        self.author = author
        self.pages = pages
        self.genre = genre
        self.__is_checked_out = False  # Encapsulation: private attribute

    def read(self):
        return f"You start reading '{self.title}' by {self.author}."

    def check_out(self):
        if not self.__is_checked_out:
            self.__is_checked_out = True
            return f"'{self.title}' has been checked out."
        else:
            return f"'{self.title}' is already checked out."

    def return_book(self):
        if self.__is_checked_out:
            self.__is_checked_out = False
            return f"'{self.title}' has been returned."
        else:
            return f"'{self.title}' was not checked out."

    def is_checked_out(self):
        return self.__is_checked_out

# Subclass
class EBook(Book):
    def __init__(self, title, author, pages, genre, file_size_mb):
        super().__init__(title, author, pages, genre)
        self.file_size_mb = file_size_mb

    # Polymorphism: override method
    def read(self):
        return f"You open the ebook '{self.title}' on your device."

    def download(self):
        return f"'{self.title}' ({self.file_size_mb}MB) is downloading..."

# Example usage
physical_book = Book("1984", "George Orwell", 328, "Dystopian")
ebook = EBook("Digital Fortress", "Dan Brown", 356, "Thriller", 2.5)

print(physical_book.read())
print(physical_book.check_out())
print(physical_book.return_book())

print(ebook.read())           # Polymorphic behavior
print(ebook.download())
print(ebook.check_out())      # Inherited method
