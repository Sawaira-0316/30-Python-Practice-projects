class person:
    def __init__(self,name,age):
        self.name=name
        self.age=age
def myfunc(self):
    print("hello i am sawiar")
p1=person("sawaira",21)
#p1.age=22
del p1.age
print(p1.age)