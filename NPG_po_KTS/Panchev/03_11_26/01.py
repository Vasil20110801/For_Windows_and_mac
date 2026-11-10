lst = []
while len(lst) < 20 :
    n = int(input())
    lst.append(n)


for i in lst:
    if i % 2 == 0:
        print(i)

sred = sum(lst) / len(lst)
lst.append(sred)
print(lst)