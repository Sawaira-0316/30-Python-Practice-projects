class Person:
    def __init__(self,fname,lname):
        self.fname=fname
        self.lname=lname
    def printname(self):
        print((self.fname,self.lname))
class Studednt(Person):
    def __init__(self, fname, lname):
        Person.__init__(self, fname, lname)
x=Studednt('sawaira','asghar')
x.printname()