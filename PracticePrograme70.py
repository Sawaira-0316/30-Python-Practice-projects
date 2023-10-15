class Person:
    def __init__(self,fname,lname):
        self.fname=fname
        self.lname=lname
        print(self.fname,self.lname)
class Human(Person):
    def __init__(self,fname,lname):
        super().__init__(fname,lname)
obj=Human("Sawaira","Asghar")
obj.printname()