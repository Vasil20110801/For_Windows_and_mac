class Number:
    def __init__(self, number):
        self.number = number

    def show(self):
        return self.number

class Doublenum(Number):
    def __init__(self, number_1,number_2):
        super().__init__(numnber)
        super().show()

        self.number_2 = number_2
    def show(self):

        print(self.number_1)
        print(self.number_2)

n1 = Number(3)
n1.show()
d1 = Doublenum(10,20)
d1.show()