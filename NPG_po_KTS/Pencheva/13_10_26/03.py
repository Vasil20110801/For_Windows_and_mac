class Phone:
    def __init__(self, brand,model,price,color,manifacture_year):
        self.brand = brand
        self.model = model
        self.price = price
        self.color = color
        self.manifacture_year = manifacture_year


    def otstupka(self):
        otstupka1 = 0
        if self.manifacture_year >= 2015 or self.manifacture_year <= 2021 :
            otstupka1 += (self.price * 0.05)
        elif self.manifacture_year < 2015:
            otstupka1 += (self.price * 0.15)
        print(otstupka1)



brand1 = input()
model1 = input()
price1 = int(input())
color1 = input()
manifacture_year1 = int(input())


p1 = Phone(brand1,model1,price1,color1,manifacture_year1)
p1.otstupka()
