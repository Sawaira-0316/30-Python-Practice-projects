class Employee:
    @staticmethod
    def sample(x):
        print('Inside static method', x)
Employee.sample(10)

emp = Employee()
emp.sample(10)