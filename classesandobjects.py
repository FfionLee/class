class StudentProfile():

    def __init__(self):
        print("making a copy of the class")
        self.name=""
        self.surname=""
        self.age=13
        self.teacher=""
    def showdetails(self):
        print("name:",self.name)
        print("surname: ",self.surname)
        print("age:",self.age)
        print("teacher: ",self.teacher)
    def changedetails(self):
        self.name=input("Enter your name: ")
        self.surname=input("Enter your surname: ")
        self.age=int(input("Enter your age: "))
        self.teacher=input("Enter your teacher name: ")

student1=StudentProfile()
student1.showdetails()
student1.changedetails()
student1.showdetails()

student2=StudentProfile()
student2.showdetails()