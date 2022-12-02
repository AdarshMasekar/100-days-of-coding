
import math
print("Welcome to BMI calculator.")

weight  = int(input("Enter your weight in kg: \n"))

height = float(input("Enter your height in m: \n"))

BMI =weight/(height*height)

if BMI <= 18.5:
    print("your BMI is Under Weight")
elif BMI > 18.5 and BMI <= 25:  
    print("your BMI is Normal") 
elif BMI >25 and BMI <= 30 :
    print("your BMI is Over weight")
else:
    print("your BMI is Obese")

"""
conditions :
Under weight 
BMI < 18.5

Normal weight
BMI 18.5-25

Over weight 
BMI 25-30

Obese
BMI >30
"""
