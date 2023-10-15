import json
import random

Cnumber=random.randrange(1,101)
userInput=int(input("ENter the number"))
if userInput>Cnumber:
    print("the number is grater")
elif userInput<Cnumber:
    print("the number is  less then")
else:
    print("the number is equal")