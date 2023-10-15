#def greet():
  #   print("hello")
#greet()
def myfunc(n):
     return lambda a:a*n
mydoubler=myfunc(2)
print(mydoubler(11))


