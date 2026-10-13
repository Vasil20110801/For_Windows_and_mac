from time import sleep

with open("02txt.txt", "r", encoding="utf-8") as f2:
    for line in f2:
        print(line.strip())
        sleep(0.5)
