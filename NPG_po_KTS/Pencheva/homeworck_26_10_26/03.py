class TriangleChecker:
    def __init__(self, n1, n2, n3):
        self.n1 = n1
        self.n2 = n2
        self.n3 = n3

    def is_triangle(self):
        if not all(isinstance(x, (int, float)) for x in (self.n1, self.n2, self.n3)): # това е от чата
            return "Трябва да въведете само числа!"

        if self.n1 < 0 or self.n2 < 0 or self.n3 < 0:
            return "Нищо няма да работи с отрицателни числа!"

        if (self.n1 + self.n2 > self.n3) and (self.n1 + self.n3 > self.n2) and (self.n2 + self.n3 > self.n1):
            return "Ура, можете да построите триъгълник!"
        else:
            return "Жалко, но не можете да направите триъгълник от това ."