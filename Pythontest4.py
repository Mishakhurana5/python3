class Book:
    def __init__(self,title,author):
        self.title = title
        self.author = author
        self.is_borrowed = False

    def borrow(self):
        self.is_borrowed = True
        print("You borrowed the book:" + self.title)

    def return_book(self):
        self.is_borrowed = False
        print("You returned the book:" + self.title)

b1= Book("Diary of a wimpy kid", "Jeff Kinney")
b2 = Book("Percy Jackson", "Rick Riordan")
b3 = Book("Harry Potter", "J.K Rowling")

b1.borrow()
b1.return_book()

b2.borrow()
b2.return_book()

b3.borrow()
b3.return_book()