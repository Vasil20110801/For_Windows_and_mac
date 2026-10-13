class Firma:
    def __init__(self, id_num,fname,experience_firma,salary,age):
        self.id_num = id_num
        self.fname = fname
        self.experience_firma = experience_firma
        self.salary = salary
        self.age = age

    def empoyer(self):
        print(id_num1)
        print(fname1)
        print(experience_firma1)
        print(salary1)
        print(age1)

    def dobavka(self,salary1):
        new_salary = salary1
        if experience_firma1 > 10:
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


