class Employee:
    def __init__(self, name, age, salary):
        self.name = name
        self.age = age
        self.salary = salary

    def show(self):
        print(self.name, self.age, self.salary)
emma = Employee('sajida', 23, 7500)
emma.show()

kelly = Employee('SAwaira', 25, 8500)
kelly.show()