n = input()
lst = []
for i in n:
    lst.append(int(i))
lst2 = lst.copy()
lst2.reverse()
lst3 = lst + lst2
tup1 = tuple(lst3)
print(tup1)