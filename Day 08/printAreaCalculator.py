height = int( input("enter the height of the wall : "))
width = int(input("enter the width of the wall : "))
coverage = int(input("enter the coverage : "))

cans = round((height * width) / coverage) 
print(f"cans needed are : {cans}")
