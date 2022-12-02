import math
 
print("Welcome to the tip calculator") 

totalBill = float(input("What was the total bill ? $"))

noOfPeople = int(input("How many people to split the bill ? "))

tip = int(input("Whaa percentage tip would  you like to give ? 10 ,12 or 15 ? "))

tip = (tip/100)*totalBill
eachPersonPay = (totalBill+tip)/noOfPeople

print("Each person should pay $" + str(math.ceil(eachPersonPay)))
