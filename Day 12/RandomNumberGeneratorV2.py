""" game by : Adarsh Masekar """

print("""
 ____                                       __    __                                              __                      
/\  _`\                                    /\ \__/\ \                                            /\ \                     
\ \ \L\_\  __  __     __    ____    ____   \ \ ,_\ \ \___      __         ___   __  __    ___ ___\ \ \____     __   _ __  
 \ \ \L_L /\ \/\ \  /'__`\ /',__\  /',__\   \ \ \/\ \  _ `\  /'__`\     /' _ `\/\ \/\ \ /' __` __`\ \ '__`\  /'__`\/\`'__\
  \ \ \/, \ \ \_\ \/\  __//\__, `\/\__, `\   \ \ \_\ \ \ \ \/\  __/     /\ \/\ \ \ \_\ \/\ \/\ \/\ \ \ \L\ \/\  __/\ \ \/ 
   \ \____/\ \____/\ \____\/\____/\/\____/    \ \__\\ \_\ \_\ \____\    \ \_\ \_\ \____/\ \_\ \_\ \_\ \_,__/\ \____\\ \_\ 
    \/___/  \/___/  \/____/\/___/  \/___/      \/__/ \/_/\/_/\/____/     \/_/\/_/\/___/  \/_/\/_/\/_/\/___/  \/____/ \/_/""")
import random 
print(" Welcoome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100.")

number = random.randint(1,100)
print(number)
level = input("type 'easy' or 'hard' : ")
choices = 0

if level == 'easy':
    choices = 10
elif level == 'hard':
    choices = 5
else:
    print("incorrect option!")

while choices != 0:
    print(f"\nYou have {choices} attempts remaining to guess the number. ")
    guess = int(input("Make a guess : "))
    choices -= 1
    if number == guess:
        print("You guessed the correct number!")
        break
    if number < guess:
        print("Too high")
    elif number > guess:
        print("Too low")
    
print("You lost the game try again")
