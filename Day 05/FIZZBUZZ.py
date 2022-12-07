"""
if a number is divisible by 3 and 5 print "FIZZBUZZ"
if a number is divisible by 3 : print "FIZZBUZZ"
if a number is divisible by 5 : print "FIZZBUZZ"

"""

for numbers in range(1,101):
    if numbers % 3 == 0 and numbers % 5 == 0 :
        print("FIZZBUZZ")
    elif numbers % 3 == 0 :
        print("FIZZ")
    elif numbers % 5 == 0 :
        print("BUZZ")
    else:
        print(numbers)
