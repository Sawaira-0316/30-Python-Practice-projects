my_dict = {"name": "John", "age": 25}
try:
    print(my_dict["city"])
except KeyError:
    print("Error: Key not found.")