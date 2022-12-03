print("""
    Menu 
Small Pizza : $15
Medium Pizza : $20
Large Pizza : $25

Pepperoni for Small Pizza : +$2
Pepperoni for Medium or Large : +$3

Extra cheese for any size Pizza : +$1
""")

size = input("Enter size of Pizza you want? i.e S - small , M - Medium , L - Large :")
add_pepperoni = input("Do you want Pepperoni ? i.e 'Y - yes , N - No :")
extra_cheese = input("Do you want Extra Cheese ? i.e Y - yes , N - no  :")

total = 0

if size == 'S' or size == 's':
    total += 15
elif size == 'M' or size == "m":
    total += 20
elif size == 'L' or size == 'l':
    total+= 25
else:
    print("invalid input")

if(add_pepperoni == 'y' or add_pepperoni == 'Y'):
    if size == 'S' or size == 's':
        total += 2
    elif size == 'M' or size == "m":
        total += 3
    elif size == 'L' or size == 'l':
        total+= 3
if extra_cheese == 'Y' or extra_cheese == 'y':
    total += 1

print(f"Total prize of your pizza is ${total}")
