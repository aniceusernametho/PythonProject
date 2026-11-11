from BookAndLibrary import *

Book1 = createBook("Diary of a Wimpy Kid", "Jeff Kinney")
Library = createLibrary()
Library.AddBook(Book1)


while True:
    print("Welcome to the library! Choose an action.")
    print("1: Add a book")
    print("2: See all available books")
    print("3: Find a book")
    answer = str(input("Choose an option"))
    CustomBook = str(input("Enter name of book."))
    Author =  str(input("Enter author of book."))
    Book2 = createBook(CustomBook, Author)
    print("Book added sucessfully.")

    
    
 
