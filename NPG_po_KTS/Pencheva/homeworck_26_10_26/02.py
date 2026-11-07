class Person:
    def __init__(self, name, famili,age,nationaliti,):
        self.name = name
        self.famili = famili
        self.age = age
        self.nationaliti = nationaliti

    def print_personaliti(self):
        print(f"name = {self.name}, nationaliti = {self.nationaliti}")

p1 = Person("Ivan","Draganow",44,"Bulgarian")

p1.print_personaliti()

