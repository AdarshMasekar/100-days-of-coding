print("Welcome to the Roller coaster")
height = int(input("please enter your height in cm : "))
age = int(input("Please enter your age "))
if height > 120 :
    print("You an ride the roller coaster!")
    if(age<18):
        print("price of the ticket is $7")
    else:
        print("price of the ticket is $12")
else:
    print("Sorry, You can't ride the rollar coaster")
