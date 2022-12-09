number = int(input("enter the number : "))
i = 2
flag = 1
if number > 1:
    for i in range(2,int(number/2)+1):
        if number % i == 0:
            
            flag = 0

    if flag == 1:
        print("\nprime\n")
    else:
        print("\nnot a prime\n")
else:
    print("\nnot a prime\n")
