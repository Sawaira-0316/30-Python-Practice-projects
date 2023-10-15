class Employee:
    def __init__(self, name, Salary, Project):
        self.name = name
        self.Salary = Salary
        self.Project = Project

    def show(self):
        print("Name:", self.name, "Salary:", self.Salary)

    def work(self):
        print(self.name, "is working on", self.Project)
obj = Employee("Sawaira", 100000, 'PythonProject')
obj.show()
obj.work()






