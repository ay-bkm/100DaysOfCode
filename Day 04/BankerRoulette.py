import random
names = input("Write Your names seperated by coma: \n")
theList = names.split(", ")
lastIndex = len(theList) - 1
print(f"{theList[random.randint(0, lastIndex)]} is the person who is going to pay today!")