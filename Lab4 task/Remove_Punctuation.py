import os 
os.system('cls')
class Puntuation_Remove:
    def __init__(self,string):
        self.string=string
        self.puntuations="""!()-[]{};:'"\,<>./?@#$%^&*_~`"""
        self.Result=' '

    def Remove_fun(self):
        for char in self.string:
            if char not in self.puntuations:
                self.Result+=char

    def display(self):
        print()
        print("__________________Before_______________________")
        print()
        print(f"{self.string}")
        print()
        print("__________________After________________________")
        print()
        print(f"{self.Result}")
        print()


obj=Puntuation_Remove(input("Enter the string>"))
obj.Remove_fun()
obj.display()