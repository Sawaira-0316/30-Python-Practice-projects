
try:
    file=open("data.text")
except FileNotFoundError:
    print("error:filenot  found")