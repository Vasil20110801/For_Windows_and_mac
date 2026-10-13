class file:
    def metod1(self):
        try:
            with open("01txt.txt", 'r', encoding='utf-8') as file:
                print(file.read())
        except FileNotFoundError:
            print("File not found ,try again")


n1 = file()
n1.metod1()