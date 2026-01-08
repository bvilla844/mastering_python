# Magic methods = Dunder methods (double underscore) __init__, __str__,__eq__
# They are automatically called by many of python built-in operations
# they allow developers to define or customize the behavior of objects

class Book:

    def __init__(self, title, author, num_pages):
        self.title = title
        self.author = author
        self.num_pages = num_pages

    def __str__(self):
        return f"{self.title} by {self.author}"

    def __eq__(self, other):
        return self.title == other.title and self.author == other.author

    def __lt__(self, other):
        return self.num_pages < other.num_pages

    def __gt__(self, other):
        return self.num_pages > other.num_pages

    def __add__(self, other):
        return self.num_pages + other.num_pages

    def __contains__(self, keyword):
        return keyword in self.title or keyword in self.author

    def __getitem__(self, key):
        if key == "title":
            return self.title
        elif key == "author":
            return self.author
        elif key == "num_pages":
            return self.num_pages
        else:
            return f"{key} is not a valid keyword"

book1 = Book("The hobbit", "J.R.R Tolkien", 310)
book2 = Book("Harry potter", "J.K Rowling", 224)
book3 = Book("The lion, the wich and the wardrobe", "C.s lewis", 400)

print(book2)
print(book3 < book2)
print(book3 + book2)
print("lion" in book3)
print(book3['num_pages'])