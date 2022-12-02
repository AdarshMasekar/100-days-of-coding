"""
if a person is able to live 90 years print  the remaining days,weeks,months and years he/she has from their current age
"""

age = int(input("Enter your age : "))

yearsLeft = 90 - age 

monthsleft = yearsLeft * 12

weeksLeft = yearsLeft * 52

daysLeft = monthsleft * 30
 
print(f"You have {daysLeft} days, {weeksLeft} weeks, {monthsleft} months and {yearsLeft} years")
