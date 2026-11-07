class Car:
    def __init__(self, make, model, year, speed):
        self.make = make
        self.model = model
        self.year = year
        self.speed = speed

    def honk(self):
        print("Beep,Beep")

    def accelerate(self,rate):
        self.speed += rate

    def get_speed(self):
        return self.speed



my_car = Car("Toyota","Corola",2020,0)
my_car.honk()
my_car.accelerate(40)
print(my_car.get_speed())

