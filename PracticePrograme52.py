my_number=[1,2,3,4]
try:
    my_number[4]
except IndexError:
    print("the index you used is invalid")