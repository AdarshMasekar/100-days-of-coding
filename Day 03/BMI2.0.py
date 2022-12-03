import math
print("Welcome to BMI calculator.")

weight  = int(input("Enter your weight in kg: \n"))

height = float(input("Enter your height in m: \n"))

bmi =weight/(height*height)

if bmi < 18.5:
    print(f"Your bmi is {bmi} , you are underweight.")
elif bmi < 25 :
    print(f"Your bmi is {bmi}, you are a noraml weight.")
elif bmi < 30:
    print(f"Your bmi is {bmi}, you are overweight.")
elif bmi < 35:
    print(f"Your bmi is {bmi}, you are obesse.")
else:
    print(f"Your bmi is {bmi}, you are clinically obese")
