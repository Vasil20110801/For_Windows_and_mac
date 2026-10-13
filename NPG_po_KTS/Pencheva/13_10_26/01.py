import math
class Numbers:
    def __init__(self,n):
        self.n = n

    def stepen2(self):
        print(self.n ** 2 )

    def stepen3(self):
        print(self.n ** 3 )
    def fact(self):
        print(math.factorial(self.n))

x = int(input())
n1 = Numbers(x)
n1.stepen2()
n1.stepen3()
if x  %  2 == 0 or x == 0:
    n1.fact()
else:
    print("Числото няма фактуриел")

