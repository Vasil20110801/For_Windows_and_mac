from pandas.core.interchange.from_dataframe import primitive_column_to_ndarray


class Aritmetika:
    def __init__(self,x,y   ):
        self.x=x
        self.y=y

    def print_stoinosti(self):
        print(f"x e {self.x}")
        print(f"y e { self.y}")

    def print_sum(self):
        s = self.x + self.y
        print(f"sumata e {s}")

    def print_razlika(self):
        s = self.x - self.y
        print(f"razlikata e {s}")

    def delenie(self):
        if self.x > 0 or  self.x <  0:
            print(f"delenieto e {self.x / self.y}")
        else:
            print("Na 0 ne se deli")


n1 = float(input("n1="))
n2 = float(input("n2="))
ar1 = Aritmetika(n1,n2)
ar1.print_stoinosti()
ar1.print_razlika()
ar1.delenie()
ar1.print_sum()
