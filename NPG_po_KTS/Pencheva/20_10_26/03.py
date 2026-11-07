import math

class Triangle: # Описание на
    def __init__(self,a,b,c): # Конструктор на класа
        self.a=a
        self.b=b
        self.c=c
    def show(self): # Метод за извеждане на страните на триъгълника
        s_a= f"{self.a:.2f}"
        s_b= f"{self.b:.2f}"
        s_c= f"{self.c:.2f}"
        return f"a={s_a} cm, b={s_b} cm, c={s_c} cm"
    def lice(self): # Метод за изчисляване на лице
        p=(self.a+self.b+self.c)/2
        s=math.sqrt(p*(p-self.a)*(p-self.b)*(p-self.c))
        return s
    def perimetar(self): # Метод за изчисляване на периметър
        return self.a+self.b+self.c

x=float(input("a1="))
y=float(input("b1="))
z=float(input("c1="))

T1=Triangle(x, y ,z)

x1=float(input("a2="))
y1=float(input("b2="))
z1=float(input("c2="))
T2=Triangle(x1, y1,z1)

print(f"stranite sa :{T1.show()}")

print (T1.lice())
print (T1.perimetar())
print(T1.show())

print(T2.lice())
print(T2.perimetar())
print(T2.show())