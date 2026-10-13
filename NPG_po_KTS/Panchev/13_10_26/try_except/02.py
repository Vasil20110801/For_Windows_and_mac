
try:
    while True:
        try:
            n = int(input())
        except:
            print("invalid number")
            continue

        if n < 0:
            print("enter a positive number")
            continue
        else:
            print("Good Bye")
            break
except:
    print("ERROR")





