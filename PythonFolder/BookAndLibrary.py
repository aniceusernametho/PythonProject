class createBook:
    def __init__(self, title, Author):
        self.title = title
        self.Author = Author
        self.IsBorrowed = False

class createLibrary:
    def __init__(self):
        self.Books = []

    def AddBook(self, book):
        self.Books.append(book)

    def allBooks(self):
        for i in self.Books:
            print(i)

    def FindBook(self, title):
        for i in self.Books:
            if i.lower() == title.lower():
                print(f"Found book {i} ")
            else:
                print(f"Cannot find {i}. Please try again.")
                