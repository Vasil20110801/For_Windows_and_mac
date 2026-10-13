class Phone:
    def __init__(self, brand,model,price,color,manifacture_year):
        self.brand = brand
        self.model = model
        self.price = price
        self.color = color
        self.manifacture_year = manifacture_year


    def otstupka(self):
        otstupka1 = 0
        if manifacture_year > 10:
            new_salary = new_salary * 1.02
        elif experience_firma1 >= 5 and experience_firma1 <= 10:
            new_salary = new_salary *  1.015
        elif  experience_firma1 < 5:
            new_salary = new_salary * 1.005
        print(new_salary)






id_num1 = int(input())
fname1 = input()
experience_firma1 = int(input())
salary1 = int(input())
age1 = int(input())

emp1 = Firma(id_num1,fname1,experience_firma1,salary1,age1)
emp1.empoyer()
emp1.dobavka(salary1)


