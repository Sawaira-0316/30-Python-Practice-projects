print("Welcome to my computer quiz!")

playing=input("do you want to play?")

if playing != "yes":
    quit()

print("oky! Lets Play")
answer=input("What does CPU stand for?")
if answer == "Central Processong unit":
    print("correct")
else:
    print("Incorrect ")