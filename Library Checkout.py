class Book:
    def __init__(self, title, author, isbn):
        self.title = title
        self.author = author
        self.isbn = isbn

class Member:
    def __init__(self, name, id):
        self.name = name
        self.id = id

#Test
Book1 = Book("Atomic", "John", 123456789)
Book1.title = "Habits"
print(Book1.title)