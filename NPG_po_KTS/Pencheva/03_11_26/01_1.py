class Parents:
    def __init__(self,a,b):
        self.a = a
        self.b = b
    def show(self):
        print(f"Parent = {self.a}")

class Child(Parents):
    def __init__(self,name,age,town):
        super().__init__(name,age)
        self.town = town

    def show(self):
        print(f"name = {self.a},\n age = {self.b}, \n town = {self.town}")

p = Parents("Ivana",30)
p.show()
ch = Child("Milena",30,"Sofiq")
ch.show()