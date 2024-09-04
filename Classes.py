# Define a class called "Book"
class Book:
    # Initialize the class with attributes (data)
    # The __init__ constructor initializes an object's attributes when it's created.
    def __init__(self, title: str, author: str, year: int):
        self.title = title
        self.author = author
        self.year = year

    # Define a method (function) to print a summary of the book
    def summary(self):
        print(f"{self.title} is a book written by {self.author} in {self.year}.")

    # Define a special method to return a string representation of the object
    def __str__(self) -> str:
        return f"{self.title} by {self.author}"

# Create an object (instance) of the Book class
my_book = Book("Mr.Robot", "Dave", 1907)

# Access and print the attributes of the object
print(my_book.title) 
print(my_book.author) 
print(my_book.year)  

# Call the method on the object
my_book.summary()  

# Print the string representation of the object
print(my_book)  