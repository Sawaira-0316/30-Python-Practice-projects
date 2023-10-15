class Person:
    def __init__(self,fname,Lname):
        self.fname=fname
        self.Lname=Lname
    def print(self):
        print(self.fname,self.Lname)
class Student(Person):
    def __init__(self,fname,Lname):
        super().__init__(fname,Lname)
        self.RollNumber=98

x=Student("sajida","BIBI")
print(x.RollNumbe)
