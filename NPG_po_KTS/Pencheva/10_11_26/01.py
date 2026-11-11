class Figura :
    def __init__(self,name):
        self.name = name

    def describe (self):
        print(f"Name is {self.name}")
    def area (self):
        return 0
    def perimeter(self):
        return 0

class Rect(Figura):
    def __init__(self,width,height,name):
        self.width = width
        self.height = height
        super().__init__(name)

    def area(self):
        return self.width * self.height

    def perimeter(self):
        return self.width + self.height

    def describe (self):
        super().describe()
        print(f"weight == {self.width}, height == {self.height}")


class Circle(Figura):
    def __init__(self,radius,name):
        self.radius = radius
        super().__init__(name)

    def area(self):
        return 3.14 * self.radius * self.radius

    def perimeter(self):
        return 0

    def describe(self):
        super().describe()
        print(f"radius == {self.radius}")


r1 = Rect(10,10,"ivan")
c1 = Circle(10,"ivan")
r1.describe()
c1.describe()