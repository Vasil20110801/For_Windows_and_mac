# ex 1
class TV:
    def __init__(self, brand, model, price, color, manifactur_year):
        self.brand = brand
        self.model = model
        self.price = price
        self.color = color
        self.manifactur_year = manifactur_year

    def tv_discount(self):
        if 2015 <= self.manifactur_year <= 2020:
            price = self.price - self.price * 0.05
        elif self.manifactur_year < 2015:
            price = self.price - self.price * 0.15
        else:
            price = self.price
        print(f" Крайна цена за {self.brand} след отстъпка: {price} лв.")
        return price

    def iztrivane_tv(self):
        marka = input("Въведи марка за изтриване: ")
        cvqt = input("Въведи цвят за изтриване: ")
        for television in tv:
            if television.brand == marka and television.color == cvqt:
                tv.remove(television)
                break
        print(f" Остават {len(tv)} телевизора в списъка.")

    def tv_expensive(self):
        expensive_tv = None
        godina = int(input("Въведете година за най-скъп модел: "))
        for television in tv:
            if television.manifactur_year == godina:
                if expensive_tv is None:
                    expensive_tv = television
                elif television.price > expensive_tv.price:
                    expensive_tv = television
        if expensive_tv:
            print(
                f" Най-скъпият модел от {godina} г. е {expensive_tv.brand} {expensive_tv.model} ({expensive_tv.price} лв.)")
        else:
            print(f" Няма намерен телевизор от {godina} година.")
        return expensive_tv

    def sorting_tv(self):
        ceni = []
        for television in tv:
            ceni.append(television.price)
        ceni.sort()
        sortiran_tv = []
        for price in ceni:
            for television in tv:
                if television.price == price and television not in sortiran_tv:
                    sortiran_tv.append(television)
        print("Сортирани по цена:")
        print(" Списък, сортиран по цена във възходящ ред:")
        for television in sortiran_tv:
            print(f" - {television.brand} {television.model}: {television.price} лв.")
        return sortiran_tv

    def tursene_tv(self):
        tursena_cena = float(input("Въведи цена за търсене: "))
        tursena_marka = input("Въведи марка за търсене: ")
        rezultat = []
        for television in tv:
            if television.price < tursena_cena and television.brand == tursena_marka:
                rezultat.append(television)
        for television in rezultat:
            print(f" - {television.brand} {television.model} ({television.price} лв.)")
        return rezultat


tv1 = TV('Samsung', '5G', 1000, 'black', 2011)
tv2 = TV('Apple', '8X', 8000, 'pink', 2017)
tv3 = TV('Motorowa', '7G', 800, 'black', 2000)
tv4 = TV('LG', '5G', 400, 'black', 2000)
tv5 = TV('Samsung', '10X', 1001, 'white', 2010)

tv = [tv1, tv2, tv3, tv4, tv5]

#извикване?
tv1.tv_discount()
tv1.iztrivane_tv()
tv1.tv_expensive()
tv1.sorting_tv()
tv1.tursene_tv()

#ex2
class Book:
    def __init__(self, title, genre, author, price, publication_year):
        self.title = title
        self.genre = genre
        self.author = author
        self.price = price
        self.publication_year = publication_year

    def book_discount(self):
        if 2017 <= self.publication_year <= 2021:
            price = self.price - self.price * 0.05
        elif self.publication_year < 2017:
            price = self.price - self.price * 0.1
        else:
            price = self.price
        print(f" Крайна цена за {self.title} след отстъпка: {price} лв.")
        return price

    def iztrivane_book(self, book_list):
        janr = input("Въведи жанр за изтриване: ")
        cena = float(input("Въведи цена за изтриване: "))
        for kniga in book_list:
            if kniga.genre == janr and kniga.price == cena:
                book_list.remove(kniga)
                break
        print(f"Остават {len(book_list)} книги в списъка.")

    def sredna_cena(self, book_list):
        godina = int(input("Въведи година на издаване: "))
        obshta_suma = 0
        broi_knigi = 0
        for kniga in book_list:
            if kniga.publication_year > godina:
                obshta_suma += kniga.price
                broi_knigi += 1
        if broi_knigi == 0:
            print("Няма намерени книги след тази година.")
            return 0
        sredna = obshta_suma / broi_knigi
        print(f"Средна цена: {sredna} лв.")
        return sredna

book1 = Book("Под игото", "Роман", "Иван Вазов", 25, 1894)
book2 = Book("Патиланско царство", "Детска литература", "Ран Босилек", 12, 1925)
book3 = Book("Малкият принц", "Детска литература", "Антоан дьо Сент-Екзюпери", 15, 1943)
book4 = Book("Пипи Дългото чорапче", "Детска литература", "Астрид Линдгрен", 16, 1945)
book5 = Book("Хари Потър", "Фентъзи", "Дж. К. Роулинг", 35, 1997)
book6 = Book("Приключенията на Том Сойер", "Детска литература", "Марк Твен", 12, 1876)

book = [book1, book2, book3, book4, book5, book6]

# Извикване
book1.book_discount()
book1.iztrivane_book(book)
book1.sredna_cena(book)