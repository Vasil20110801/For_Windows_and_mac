class Book:
    def __init__(self,title,author):
        self.title = title
        self.author = author



b1_1 = Book("Опълченицте на шипка","Иван Вазов")


class Library:
    def __init__(self,name):
        self.name = name
        self.dct = {}

    def add_book(self, book_title):
        self.dct[book_title] = True

    def borrow(self, book_title):
        if book_title in self.dct and self.dct[book_title] == True:
            self.dct[book_title] = False
            print(f"Взимаш я: {book_title}")
        else:
            print(f"Не може да вземеш: {book_title}")

    def return_books(self, book_title):
        if book_title in self.dct:
            self.dct[book_title] = True
            print(f"Върната е: {book_title}")

    def list_availiable_books(self):
        print("Налични книги:")
        for title, is_available in self.dct.items():
            if is_available:
                print(f"- {title}")


class Books(Library):
    def __init__(self,book_title,author):
        super().__init__(book_title)
        self.author = author
        self.dct = {}

    def add_book(self, book_title):
        self.dct[book_title] = True

    def borrow(self, book_title):
        if book_title in self.dct and self.dct[book_title] == True:
            self.dct[book_title] = False
            print(f"Взимаш я: {book_title}")
        else:
            print(f"Не може да вземеш: {book_title}")

    def return_books(self, book_title):
        if book_title in self.dct:
            self.dct[book_title] = True
            print(f"Върната е: {book_title}")

    def list_availiable_books(self):
        print("Налични книги:")
        for title, is_available in self.dct.items():
            if is_available:
                print(f"- {title}")


b1 = Library()
b1.add_book("Opylcencite na shipka")
b1.add_book("Tainata na tainite")

b1.borrow("Opylcencite na shipka")
b1.list_availiable_books()

b1.return_books("Opylcencite na shipka")
b1.list_availiable_books()