lst1 = []
lst2 = []
while len(lst1) < 5:
    n = int(input())
    if n < 0 :
        print("Числото требва да е положително")
        continue
    else:
        lst1.append(n)

for i in lst1:
    if i >= 10 :
        lst2.append(1)
    elif i < 10 :
        lst2.append(0)
        
print(lst2)



