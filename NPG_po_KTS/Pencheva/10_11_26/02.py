class Lekar:
    def __init__(self,name,speciality,patient):
        self.name = name
        self.speciality = speciality
        self.patient = patient
    def diagnose(self):
        print(f"Доктор с име {self.name},преглежда пациент {self.patient}")

    def inform(self):
        print(f"Speciality is {self.speciality}")

class Surgeon(Lekar):
    def __init__(self,name,speciality,patient):
        super().__init__(name,speciality,patient)
        self.operation = 0

    def operate(self):
        print(f"Хирургът {self.name} оперира {self.patient}")

    def inform(self):
        super().inform()
        self.operation += 1

s1 = Surgeon("IVAN","hIRURG","PESHO")
s1.operate()
s1.inform()