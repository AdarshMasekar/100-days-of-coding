year = int(input("enter the year : \n"))

if year%4 ==0 and year%100 !=0 or  year%400 ==0  :
    print(f"{year} is leep year")
elif year%4 !=0 or year % 100 ==0 or year %400 !=0 :
    print(f"{year} is not a leep year")
