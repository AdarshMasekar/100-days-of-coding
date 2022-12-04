import random 

namesInput = input("Enter the names one by one with comma seperated :\n")

names = namesInput.split(",")

people = len(names)

banker = names[random.randint(0,people-1)]

print(f"{banker} is going to buy the food")
