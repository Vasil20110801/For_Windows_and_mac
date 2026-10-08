n = int(input())
lst = []
for i in range(n):
    lst.append(i + 1)

dct = {}
for i in range(len(lst)):
    dct[lst[i]] = lst[-1 - i]

print(dct)