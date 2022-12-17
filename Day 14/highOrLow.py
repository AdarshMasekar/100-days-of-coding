import random
dict = ['Miley Cyrus',"Kourtney Kardashian","Nicki Minaj","Virat Kohli","Jennifer Lopez","Tayler Swift","National Geography","Dwayne ‘The Rock’ Johnson","Nike"," Beyoncé","Kendal Jenner","Justin Bieber",'Khloé Kardashian',"Kylie Jenner","Lionel Messi","Cristiano Ronaldo"]
followers = [186,204,205,223,226,231,245,248,263,193,200,264,364,372,373,516]
score = 0
while True:
    first = random.randint(0,16)
    second = random.randint(0,16)
    result = ''
    
    while first == second:
        second = random.randint(0,16) 

    one = dict[first]
    two = dict[second]

    one1 = followers[first]
    two2 = followers[second]


    print(f"Compare A: {one}")

    print(f"Against B: {two}")

    ans = input("Who has more followers : Type 'A' or 'B' ")
    ans = ans.upper()
    if one1 > two2:
        result = 'A'
    else:
        result = 'B'
     
    if result == ans:
        score += 1
        print(f"\nYou are right, Your score is {score}\n")
    else:
        print(f"\nSorry you lost,Your score is {score}\n")
        break
    
