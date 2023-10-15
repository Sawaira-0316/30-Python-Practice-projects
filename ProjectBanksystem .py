class user:
    def __init__(self,name,age,gender):
        self.name=name
        self.age=age
        self.gender=gender
    def user_details(self):
        print("Personal details")
        print("")
        print("name",self.name)
        print("age",self.age)
        print("gender",self.gender)
class bank(user):
    def __init__(self,name,age,gender):
        super().__init__(name,age,gender)
        self.balance=0
    def deposit(amount):
     self.amount=amount
     self.balance=self.balance +amount
