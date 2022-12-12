print( """
__________
| ________ |
||12345678||
|'''''''''''|
 ----------
|[7|8|9][+]|
|[4|5|6][-]|
|[1|2|3][*]|
|[.|O|=][/]|
 ----------
""" )


firstNumber = float(input("What is your first number: "))
operation = input("""
+
-
*
/
Pick an operation : 
""")
secondNumber = float(input("What is your second number: "))
if operation == '+':
    print(f"Your Answer is : {firstNumber+secondNumber}")
elif operation == '-':
    print(f"Your Answer is : {firstNumber-secondNumber}")
elif operation == '*':
    print(f"Your Answer is : {firstNumber*secondNumber}")
elif operation == '/':
    try:
        print(f"Your Answer is : {firstNumber/secondNumber}")
    except:
        print("Divide by zero error")
else:
    print("Invalid inputs")
