num1 = [2, 5, 3, 8]
num2 = []

for i in range(len(num1) - 1):
    num2.append(num1[i])
    num2.append(num1[i] + num1[i + 1])

num2.append(num1[-1])

print(num2)